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
- Fiber Link Dead in a Westchester Building? — fiber-optic-installation-westchester-county
- We're re-letting a former corporate headquarters off I-287 floor by floor — should the landlord own the backbone, or should each tenant bring its own? — fiber-optic-installation-westchester-county
- The old corporate data centre in our building is being torn out — what happens to all the fiber that ran to it? — fiber-optic-installation-westchester-county
- Can tenants on different floors of one Westchester office building share a building-owned fiber backbone without sharing a network? — fiber-optic-installation-westchester-county
- The departed company's telephone room is still full of its old equipment — can it become the entrance room for our new tenants' carriers? — fiber-optic-installation-westchester-county
- Should the office-era fiber in a building being converted to apartments be reused, re-terminated or stripped out? — fiber-optic-installation-westchester-county
- Our office building is becoming self-storage — does it still need fiber, and where? — fiber-optic-installation-westchester-county
- When should a developer building under New Rochelle's downtown overlay bring in a fiber contractor? — fiber-optic-installation-westchester-county
- Our village offices connect to the county's Westchester Telecom Network — who is responsible for the fiber after the county's handoff? — fiber-optic-installation-westchester-county
- Our medical practice is moving into a suite in a Harrison or Purchase office park — what has to be in place before the clinical systems move? — fiber-optic-installation-westchester-county
- We're choosing between a downtown White Plains tower and an I-287 campus building — how does fiber change the comparison? — fiber-optic-installation-westchester-county
- Who owns the fiber after a building changes hands? (§10 EQUIPMENT table heading) — fiber-optic-installation-westchester-county
- Westchester Tenant Offline Right Now? (final repair heading) — fiber-optic-installation-westchester-county
- Do you cover northern Westchester towns such as Somers, North Salem and Pound Ridge, or only the southern cities? — fiber-optic-installation-westchester-county
- When one tenant expands onto a neighbour's floor, can its strands in the shared backbone be reassigned? — fiber-optic-installation-westchester-county
- Can fiber work start while the outgoing corporate tenant is still moving out? — fiber-optic-installation-westchester-county
- Can you work in an older Yonkers or Mount Vernon building that has no drawings at all? — fiber-optic-installation-westchester-county
- Can fiber be run through the parking garage under an office or apartment building? — fiber-optic-installation-westchester-county
- How much notice do you need before a Westchester tenant's move-in date? — fiber-optic-installation-westchester-county
- Can one tenant lease its spare strands to another tenant in the same building? — fiber-optic-installation-westchester-county
- Will you meet our broker and a prospective tenant at the building to answer fiber questions? — fiber-optic-installation-westchester-county
- What happens if we find asbestos-containing material in the ceilings or risers of an older building? — fiber-optic-installation-westchester-county
- Who do we call if a Westchester fiber link fails outside business hours? — fiber-optic-installation-westchester-county
- Can you remove the old corporate cabling without disturbing the fiber we're keeping? — fiber-optic-installation-westchester-county
- Do you install fiber for a business run from a house in Westchester? — fiber-optic-installation-westchester-county
- On our Pearl River campus the main fiber room is inside a building leased to another company — what happens when our strands need work there? — fiber-optic-installation-rockland-county
- Part of our Rockland office complex is being turned into apartments — how do we keep the offices' fiber out of the residential building? — fiber-optic-installation-rockland-county
- Nobody can tell us where the fiber on our newly bought Rockland property runs — how do you trace it from end to end? — fiber-optic-installation-rockland-county
- The seller kept one building on our campus and still rides the same fiber — how do we separate the two networks without cutting them off? — fiber-optic-installation-rockland-county
- Our two buildings face each other across a county road — what does it take to get private fiber from one side to the other? — fiber-optic-installation-rockland-county
- We have one site in Rockland and another a few miles over the line in Bergen County — can a single private fiber link serve both? — fiber-optic-installation-rockland-county
- Our building sat half-empty for years — is the fiber that was left in it still usable? — fiber-optic-installation-rockland-county
- Our inherited backbone is orange-jacketed multimode from decades ago — can it carry today's network? — fiber-optic-installation-rockland-county
- The parking-lot cameras at our Route 59 plaza ride on fiber that runs through a tenant's unit — how do we take them back? — fiber-optic-installation-rockland-county
- Between tenants in our Blauvelt or Orangeburg industrial building, what fiber should we leave in place for the next one? — fiber-optic-installation-rockland-county
- Our school or congregation uses neighbouring houses in Ramapo that belong to different owners — what agreement does a fiber link between them need? — fiber-optic-installation-rockland-county
- Our offices sit on both sides of the Hudson — can our own fiber cross between Rockland and Westchester? — fiber-optic-installation-rockland-county
- The shopping centre where we lease is being sold — what happens to our fiber and our carrier's fiber during the handover? — fiber-optic-installation-rockland-county
- Which parts of Rockland do you cover — every town, the river villages and Monsey? — fiber-optic-installation-rockland-county
- Can you test the fiber a seller says is included before we close on a Rockland building? — fiber-optic-installation-rockland-county
- Will you document and label an existing Rockland fiber plant without installing anything new? — fiber-optic-installation-rockland-county
- What licence and insurance paperwork can you hand a Rockland property manager before work starts? — fiber-optic-installation-rockland-county
- Can fiber work be done inside the lab and manufacturing buildings on Rockland's research campuses? — fiber-optic-installation-rockland-county
- What does it cost to have an inherited fiber plant tested and mapped in Rockland? — fiber-optic-installation-rockland-county
- How do you handle parking and deliveries in Nyack, Piermont and the other river villages? — fiber-optic-installation-rockland-county
- How is the cost of shared fiber divided when a Rockland campus has several owners? — fiber-optic-installation-rockland-county
- Can you supply fiber routing drawings for an Orangetown or Clarkstown site-plan application? — fiber-optic-installation-rockland-county
- Can a construction trailer or sales office on a Rockland redevelopment site get a temporary fiber link? — fiber-optic-installation-rockland-county
- Can the work start with one building on a split campus and reach the others later? — fiber-optic-installation-rockland-county
- Can our own consultant witness the acceptance tests on a Rockland fiber job? — fiber-optic-installation-rockland-county
- Shop or Office Link Dead on an Orange County Main Street? (repair capture heading) — fiber-optic-installation-orange-county
- Each tenant in our Newburgh building orders internet on its own — how do we stop every provider from drilling a new hole through the brick? — fiber-optic-installation-orange-county
- The only place for a rack in our Front Street building is the attic — is that a bad idea for fiber equipment? — fiber-optic-installation-orange-county
- We own two adjoining buildings on a village main street that share a party wall — can one network serve both? — fiber-optic-installation-orange-county
- The provider wants to mount its terminal on our storefront facade — can we ask for it somewhere else? — fiber-optic-installation-orange-county
- Our building used to be a church school — are the old intercom and telephone pathways in its walls usable for fiber? — fiber-optic-installation-orange-county
- Our practice moved into part of a large former hospital building — can we get fiber to our suite without depending on the landlord's old network? — fiber-optic-installation-orange-county
- Our restaurant near a Route 17 interchange is adding a second building on the lot — should it get its own internet service or a fiber link from the first? — fiber-optic-installation-orange-county
- The state plans a third lane on Route 17 — should a business near the highway hold off on buried fiber until the road work is done? — fiber-optic-installation-orange-county
- Our village hall, police desk and highway garage are in separate buildings — can fiber replace the leased lines between them? — fiber-optic-installation-orange-county
- Can fiber keep our firehouse's alerting equipment and cameras separate from the members' Wi-Fi? — fiber-optic-installation-orange-county
- Does Orange County's electrician licence apply to the people installing our fiber? — fiber-optic-installation-orange-county
- Our property in Warwick is a long drive from your Bronx office — how do you keep the job from stretching into extra trips? — fiber-optic-installation-orange-county
- Will a busy Newburgh or Middletown sidewalk have to be closed while the fiber comes in? — fiber-optic-installation-orange-county
- Do you take fiber work in western Orange County — Port Jervis, Otisville and the Deerpark side? — fiber-optic-installation-orange-county
- What should we send so a quote can come back before anyone visits the building? — fiber-optic-installation-orange-county
- Is fiber worth adding to a building we might sell in a few years? — fiber-optic-installation-orange-county
- Can fiber reach a second-floor office over a storefront without running through the shop? — fiber-optic-installation-orange-county
- Will trains on the Port Jervis Line next to our building disturb a fiber link? — fiber-optic-installation-orange-county
- Can fiber be added to a hotel or motel along Route 17 without taking rooms out of service? — fiber-optic-installation-orange-county
- Do outlet-center and shopping-plaza leases usually let a tenant hire its own fiber installer? — fiber-optic-installation-orange-county
- Can new fiber sit alongside an older alarm or fire-alarm panel in the same closet? — fiber-optic-installation-orange-county
- Our landlord lives outside New York — how do approvals work when the owner can't come to the building? — fiber-optic-installation-orange-county
- Do tenants have to be home when fiber is run through an occupied apartment in a two- or three-family house? — fiber-optic-installation-orange-county
- Does each end of a fiber link need a dedicated electrical outlet? — fiber-optic-installation-orange-county
- Can you install fiber in a bank branch or credit union on a village main street? — fiber-optic-installation-orange-county

### fiber-optic-installation-port-morris-bronx-ny
fiber-optic-installation-port-morris-bronx-ny
§9 Questions Answered (and other question headings):
- Port Morris Fiber Link Down This Morning? (repair capture heading)
- The provider's cable reaches our building through an old sidewalk vault that takes on water — can the entrance be moved?
- Before we sign a lease on an older industrial building, how can we find out which carriers can already serve it?
- Our lease may end when the owner redevelops the site — which parts of a fiber installation can a tenant take along when it moves?
- Can the fiber equipment share the main electrical room in a building with very large power service?
- Our stage has to stay silent during takes — will fiber enclosures and switches add noise the microphones pick up?
- We rent our loft for events a few nights a month — can visiting vendors get a network connection without touching ours?
- Our delivery fleet parks on the ground floor and the warehouse is upstairs — how does fiber get from dispatch to the upper bay?
- The electric-van chargers in our fleet garage need a network connection — is fiber worth running to them?
- Can fiber run through a metal fabrication or welding shop where sparks and hot slag fly?
- Does fiber get stolen for scrap the way copper cable does?
- We sublease from a company that itself leases the land from the State — how many sign-offs does a new fiber entrance need?
- Will exterior conduit on our street wall get tagged or broken, and how is it protected?
- Is there any help for industrial businesses in the Port Morris Industrial Business Zone that are planning a network upgrade?
- Our new building sits on a cleaned-up brownfield with a vapour barrier under the slab — can fiber conduit pass through it?
- Our new tower has post-tensioned concrete floors — how do you core through them without hitting a tendon?
- Our rental building has a resident co-working lounge — should it run on the building's own fiber or on a resident's internet account?
- Port Morris Studio, Loft or Warehouse Offline? (final repair heading)
§17 FAQ:
- Do you also take fiber jobs on Randall's Island, across the Bronx Kill?
- Can the labels and the closeout paperwork be in Spanish as well as English?
- What happens if the ceiling or attic space we need is fouled with pigeon droppings?
- Can fiber work go ahead while the building is still on temporary construction power?
- Our loft building has no working elevator — does carrying materials up the stairs change the price?
- Our construction lender pays out in draws — can your proposal be broken into the line items its inspector checks?
- Can fiber carry the monitoring link for rooftop solar panels or a battery system?
- Can fiber be pulled in an unheated building during a cold snap?
- Do you supply the hybrid fiber cables that broadcast cameras plug into?
- Can we see a sample test report before we hire you?
- Can the old fiber enclosures and patch panels a previous tenant left behind be reused?
- Do we need to tell our property insurer before fiber work starts?

De-dup notes: checked by meaning against the full register and the 16 live fiber pages plus the concurrent Midtown and St. George neighbourhood drafts. Two FAQs were replaced after the concurrent pages appeared (dust control while drilling — St. George; digital signage over fiber — Midtown). Sprinkler-pipe supports and exit-stair penetrations appear only as §8.5 compliance bullets, not as questions (Midtown asks both as questions). Post-tensioned-slab and brownfield items are answered once, in §9 only.

### fiber-optic-installation-st-george-staten-island-ny
fiber-optic-installation-st-george-staten-island-ny
§9 Questions Answered:
- Our house is built into the hillside, with the cellar at street level on one side and underground on the other — which level should the network start from?
- Does the Landmarks Preservation Commission care about conduit on the back of a historic-district house, where nobody on the street can see it?
- Can fiber follow the old radiator pipe chases up through a Victorian house?
- Would fiber to the top floor fix Wi-Fi that fades on the stairs of a four-storey house, or is a mesh kit enough?
- Our converted Victorian has no common hallway — every stair belongs to one apartment — so where can a building-wide fiber riser run?
- We're turning a three-family house back into a single home — what happens to the three sets of provider wiring, and where should the new fiber go?
- Our condo is in a 1930s poured-concrete factory building on the waterfront — how does fiber get through slabs and columns like that?
- Our co-op's alteration agreement asks for a scope of work — how much detail should the fiber section contain?
- The old telephone closet in our co-op is locked and nobody on the board knows who has the key — can fiber work start without it?
- We're a small law office near the courthouses with a records room in the basement — can scanning stations down there run over fiber without putting a server in the cellar?
- We're fitting out a shop or studio unit in a brand-new building by the ferry — what does the developer's telecom room give us, and what do we have to build ourselves?
- Our nonprofit shares an older building on Richmond Terrace with other tenants — can we have fiber of our own without paying for a whole-building system?
§17 FAQ:
- Do you work in the neighbourhoods next to St. George — Tompkinsville, New Brighton, Fort Hill and Randall Manor?
- How do you keep dust down when drilling through old plaster in a lived-in house?
- Can the small fiber box at each end be painted to match period woodwork?
- How tight can fiber bend around the corners of a narrow Victorian stair?
- Can the building's video intercom use the same fiber as the internet?
- Does fiber give off any radiation or signal that could bother people living next to it?
- If we change internet providers, does the fiber you installed still work?
- How are the strands labelled when each one serves a different apartment?
- Do we have to warn the neighbours in the attached house before you drill near the shared wall?
- Can fiber reach a turret room or attic studio at the very top of the house?
Other headings: none end in "?" (repair headings worded as statements).

De-dup notes: two draft questions were replaced after comparing with the concurrent Port Morris and Midtown drafts — "only entrance up a long flight of outdoor steps" (≈ Port Morris "no working elevator — carrying materials up the stairs") and "nonprofit … who has to sign off" (≈ Port Morris State-sublease sign-offs and SI SNAD sign-off). Closest remaining intents for the main run to judge: radiator-chase route vs Midtown "Con Edison steam beside the telecom entrance — will the heat harm fiber" (mine = route, theirs = heat proximity); FAQ bend radius vs Midtown "Is bend-insensitive single-mode worth paying for" (mine = limit, theirs = value); co-op scope-of-work vs Manhattan "drawings the landlord's engineer can review"; video intercom vs NYC-hub-family "phone system over the same fiber".

### fiber-optic-installation-midtown-manhattan-ny
§9 Questions Answered:
- Our floors are served by a different elevator bank from the building's telecom room, with a mechanical floor in between — what route does fiber take?
- The riser closets in our pre-war tower stop lining up above the setback floors — how does a backbone jog sideways to stay in a shaft?
- Can a backbone run up a fire stair when the riser closets are full?
- Can cable be hung from the sprinkler pipes that Local Law 26 added above our office ceiling?
- What should we check about a brand-new Midtown tower's telecom rooms before our fit-out drawings are final?
- The building's FDNY radio system or a carrier's in-building cellular system needs fiber to every floor — can that share our backbone?
- Two tenants on our stack want the last spare sleeve — how do buildings decide, and how do we avoid losing out?
- Does a trading floor need its fiber routed for low latency, or is that a myth inside one building?
- Our building's freight elevator is out of service for modernisation this year — can a riser job still go ahead?
- Our Times Square frontage has to keep its signs lit — can fiber feed the sign controllers and media players from the building's network room?
- Can fiber be installed in a Broadway theatre without disturbing a landmarked interior?
- Our jewellery business on 47th Street keeps its stock in a vault room — how does fiber reach the back office without creating a new way in?
- Con Edison steam enters our cellar right beside the telecom entrance — will the heat harm fiber, and how far away should it run?
- Riser cable or distribution cable: which suits a Midtown tower? (§10 EQUIPMENT table heading)
- Fiber Down Between Two Midtown Floors? (repair capture heading)
- Want the Transfer Floor Found Before Pricing? (mid-page CTA heading)
- Midtown Backbone Dark Before the Morning Rush? (final repair heading)
§17 FAQ:
- Does your Midtown coverage include Turtle Bay, Murray Hill, Koreatown and Hell's Kitchen as well as the office core?
- How is a long vertical fiber run supported so it does not hang on its own weight over dozens of floors?
- Do we need OM5 multimode for a new Midtown fit-out?
- Is bend-insensitive single-mode worth paying for in shallow Midtown closets?
- Can private fiber link the rooms of a full-floor condominium in a 57th Street residential tower?
- Do you work inside Grand Central or other transit-owned property?
- Does the building's chief engineer have to be with you for the whole job?
- Can our suite get a fiber path with no splice points or patch panels in any shared closet?
- Is armoured fiber required in a Midtown riser?
- Can the backbone go in before the landlord finishes its base-building work on our floor?

### fiber-optic-installation-downtown-brooklyn-ny
§9 Questions Answered:
- Can one fiber cable run from the cellar to the top floor of a 40-storey tower, or does it have to be broken into sections?
- Our tower has post-tensioned concrete floors — how does a new hole get made through a slab without hitting a tendon?
- How does fiber reach a gym, lounge or roof deck that sits dozens of storeys above the main telecom room?
- Our upper floors have poor mobile coverage — can the building's fiber feed an in-building cellular system?
- Our company owns the commercial condominium unit at the base of a residential tower — whose approval do we need to run fiber up to our floors?
- Our rental building bundles one provider's internet into every lease — can management still add its own fiber for cameras, doors and amenity Wi-Fi?
- We run a co-working floor where members change every month — how should the fiber be laid out so a new member doesn't mean new cable?
- Our shop is on a below-grade concourse of a mixed-use complex — how does fiber get down to a cellar-level storefront?
- We are planning video walls and digital signage on several floors of a flagship store — does that content need fiber?
- Our stall in a food hall needs a reliable wired line for card terminals — can fiber reach a single stall?
- Does a new Downtown Brooklyn high-rise need fiber for the FDNY's in-building radio system, and can it share our backbone?
Other headings (no "?"): "Same-Day Fiber Repair Across Downtown Brooklyn" (repair capture); "Have the Shaft Checked Before You Commit" (CTA); "A Downtown Brooklyn Floor Offline Right Now" (final repair).
§17 FAQ:
- Do you cover the blocks around Downtown Brooklyn — Brooklyn Heights, DUMBO, Fort Greene and Boerum Hill?
- Can you work inside a building that also houses a public school while classes are in session?
- We own one condominium apartment — can fiber be run between rooms inside it without the board's permission?
- Can the security desk in our lobby see cameras on every podium and garage level over the new fiber?
- Do electric-vehicle chargers in a tower's garage need a network connection, and can fiber provide it?
- Our new suite has glass partitions and an open ceiling — can fiber reach each room without visible cable?
- Does a very tall tower's movement in the wind put strain on a fiber riser?
- Can a student residence give every room its own wired port over a fiber backbone?
- Our building changed its street address — do the fiber records and provider orders need updating?
- Can fiber feed Wi-Fi or cameras on a privately owned public plaza in front of our building?
- Is fiber needed before a new Downtown Brooklyn building can get its certificate of occupancy?

### fiber-optic-installation-flushing-queens-ny
fiber-optic-installation-flushing-queens-ny
§9 Questions Answered (and other question headings):
- Flushing Office Floor Lost Its Uplink? (repair capture heading)
- We own one office condo unit in a Main Street building — does the board of managers have to approve fiber work, or can we hire an installer ourselves?
- Can a handful of unit owners pay for a fiber backbone that the whole condominium will end up owning?
- When an office condo unit is sold, do the fiber strands assigned to it go with the unit or stay with the building?
- We rent our office from the person who owns the condo unit — whose signature does a fiber installer need?
- Does new fiber count as replacing old wiring or as an improvement when a condo board sets its budget?
- Our board just took over from the sponsor — what fiber and cabling records should we ask for at turnover?
- Our offices sit above a retail podium owned by a different entity — how does the fiber reach us without crossing their space?
- A mall stall has no wall or ceiling of its own — how does a vendor get a wired connection from the mall's network room?
- A carrier ran its cable through our condominium's hallway ceiling without asking the board — what should the board do now?
- Can the lobby intercom, garage cameras and elevator phones all go on the condominium's fiber, or should building systems stay apart from owners' service?
- Who Owns the Riser? Fiber in Flushing's Condominium Buildings (section heading)
- Need a Number for the Next Board Meeting? (CTA heading)
§17 FAQ:
- Do you work in Murray Hill, Queensboro Hill, Auburndale and East Flushing as well as downtown?
- Who should receive the closeout file when a building has a board, a managing agent and individual unit owners?
- Can you plan the work from the condominium's original architectural drawings?
- Will you present the fiber proposal at a condo board meeting?
- Do we need the garage operator's permission before work on a parking level?
- Why label enclosures and ports with unit numbers instead of business names?
- Should we wait until the garage's Local Law 126 repairs are finished before installing fiber?
- Can spare strands be held for units whose owners have not signed up yet?
- Can the plant be extended to a later phase of the same development?
- How long does a walkthrough of a condominium tower usually take?
- Can the board see a sample strand map and test report before signing?
- Can a unit owner be shown only the strands that serve their own unit?

De-dup notes: checked by meaning against the full register. Deliberately avoided: per-tenant service in subdivided building (Queens), mixed-use separation (Queens), coax replacement (Queens), warranty and COI FAQs (Queens), garage-run question (Westchester), developer-timing question (Westchester), parking/deliveries (Rockland), medical imaging (Manhattan), non-adjacent floors (Manhattan), flood/cellar room (Manhattan/Brooklyn), seller-claims testing (Rockland), staged rollout (Rockland). Closest calls for a human read: "spare strands for units not yet signed up" vs Westchester "lease spare strands to another tenant"; "later phase of the same development" vs Rockland "start with one building and reach others later"; "carrier ran cable through hallway ceiling" vs Orange "stop every provider drilling a new hole".

### fiber-optic-installation-fordham-bronx-ny
fiber-optic-installation-fordham-bronx-ny
§9 Questions Answered (and other question headings):
- Fordham Storefront or Office Offline Mid-Shift? (repair capture heading)
- With the new offset bus lanes on Fordham Road, where does a fiber crew stop to unload reels and ladders?
- What hours can drilling happen in a building where people live above the shops?
- How do you keep shoppers and vendors clear when a cellar hatch or ceiling is open on a busy block?
- Our cellar runs out under the sidewalk into a vault — can fiber equipment live down there?
- Can an old bank vault or safe-deposit room become a building's telecom room?
- How does fiber reach a mezzanine or balcony built inside a double-height banking hall or showroom?
- Can fiber run up the stairwell of an older building that has no other vertical path?
- What does a student residence need from its fiber backbone that an ordinary apartment building doesn't?
- Do dorm rooms still need wired ports when every floor has Wi-Fi?
- What does a reopened theatre need wired before its first season?
- Tell Us What the Building Used to Be (CTA heading — not a question)
- Shop Dark on Fordham Road Right Now? (final repair heading)
§17 FAQ:
- Do you cover Belmont, Bedford Park, University Heights and Kingsbridge Heights as well as Fordham itself?
- Should a Fordham Road retailer avoid scheduling fiber work during the holiday shopping season?
- Will opening the ceiling set off our store's burglar alarm?
- Can fiber feed the digital screens and LED signs in a storefront window?
- Can fiber cable be hung from the sprinkler pipes in a ceiling?
- Why does a quote for a small building list so much more cable than the distance we measured?
- Our stockroom is in the cellar, two floors below the sales floor — copper or fiber?
- What should a store manager do in the first ten minutes when the network goes down?
- Is fiber harder to tap than copper for a clinic, bank or check-cashing office?
- Who pays if an internet provider's technician damages fiber you installed?
- Does adding fiber change our building's certificate of occupancy?

De-dup notes: checked against every question on the 16 live fiber pages (385 headings/FAQ items) and the full register. Deliberately avoided: landmark/historic-district entry (Manhattan) — landmark interiors handled in prose only; mixed-use stores-below-apartments separation (Queens); move-in lead time (Queens/Westchester); sidewalk closure (Orange); night/weekend availability (NYC hub) — the noise question is about the legal hours, not availability; old shafts for fiber (Dutchess) — stairwell question is about exit-stair code limits; medical imaging (Manhattan); hoistway (Bronx). Closest calls for a human read: dorm "wired ports vs Wi-Fi" vs NYC "Do we need fiber to every desk?"; "cellar stockroom copper or fiber" vs Brooklyn "How far can a camera sit from the rack before fiber is needed?"; "provider technician damages fiber" vs Brooklyn "fix a fiber cable a renovation crew cut".

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

## Queens — local research (2026-10-17 batch, fiber-optic-installation-queens)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md are reused where noted; only Queens research is added here.
Page thesis: Queens is the borough of shared buildings — subdivided commercial buildings (Flushing, Jamaica), mixed-use strips (Steinway St, Roosevelt Ave, Northern Blvd), multi-building garden-apartment co-ops (Jackson Heights, Sunnyside), LIC factories turned offices/studios beside new towers, and long cargo buildings around JFK. An owner backbone with per-tenant / per-building strands, locked enclosures and a strand map is the fix; active equipment kept out of flood-prone basements (Ida).

### Reddit / forums (local)
- `reddit r/Queens OR r/astoria OR r/flushing fiber internet building only Spectrum co-op` · Firecrawl search (excerpts only; reddit.com threads not opened).
  - https://www.reddit.com/r/astoria/comments/1iimex5/what_is_the_worst_internet_provider_in_astoria/ — excerpt: "I can get Spectrum, Fios or Astound in my building -- the key is your landlord or co-op board has to let them wire the place up." → §5 para 3.
  - https://www.reddit.com/r/astoria/comments/1lvsgmm/wifi_options_in_astoria/ — excerpt: "If the building doesn't have FiOS then you can't have FiOS. Simple as that." → §5 para 3; §10.5 H3 1.
  - https://www.reddit.com/r/Flushing/comments/1spiap6/experience_with_internet_services_around_flushing/ — excerpt: "Move to a different building. FIOS is the only OK option in Flushing if you want stability." → §10.5 H3 1 (quoted as a commenter's advice).
  - https://www.reddit.com/r/astoria/comments/94a2kn/ and /168cunt/ and /1o1cira/ — Spectrum price/outage complaints. Not used (consumer ISP pricing).
- `reddit Queens Astoria Fios not available building fiber internet landlord` · WebSearch → https://forums.verizon.com/t5/Fios-Internet/Bring-FIOS-service-in-my-building-Astoria-NYC/m-p/915574 (WebFetch; undated posts): Astoria tenant's request at "phase 2 which is reaching out to the landlord"; Community Leader: "you will need the owner to sign an easement form prepared by VZ regional operation center." → §5 para 3; §10.5 H3 1.
  - Same query → stopthecap.com 2013 "Your Landlord May Be the Problem" (title only, not fetched). Not used.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitute for §10.5 reality check (claims quoted as published):
- `fiber optic installation Queens NY contractor cost` · Firecrawl search →
  - https://ringandping.com/how-much-does-fiber-optic-cable-installation-cost-in-2026/ (excerpt): "Residential projects typically range from $1,500 to $6,000, while commercial fiber optic cabling services can scale into six figures for complex builds." → §10.5 H3 2.
  - https://www.streamlinetelecom.com/fiber-optic-services-for-new-york-city (excerpt): "Fiber-optic cable costs anywhere from $1-6 per linear foot to install" (silo source) → §10.5 H3 3.
  - https://lowvoltagenewyork.com/resources/fiber-optic-cabling-cost-new-york/ (silo source): $1–$6/ft indoor, up to $12; "singlemode glass is now cheaper than OM4"; SM transceivers "roughly 1.5–5×"; "Any fiber that leaves the building in NYC needs a street-opening permit"; Manhattan/Bronx rent underground conduit → §10.5 H3 3, 4, 5.
  - https://www.abstractenterprisessecuritysystems.com/structured-cabling-installation-queens (AESS's own page, excerpt + repo grep): "$150 to $300 per network connection point" → §10.5 H3 6.
  - https://www.facebook.com/groups/lowvoltagenation/posts/3612186332404503/ (excerpt; a contractor asking for Queens fiber subcontractors). Not used.
  - https://www.reddit.com/r/HomeNetworking/comments/8qcawt/ (Spectrum ~$6,000 pole quote, private land). Not used.
- Silo sources reused: unio.digital ($300–$800 per fiber drop, 2–3× Cat6) → §10.5 H3 6; T-Mobile "up to 4 hours", AT&T "four to six hours", Quantum Fiber multifamily 30/30/40–60 days → §10.5 H3 7; ampcom (OM4 ~400–550 m at 10G) → §9 legacy-multimode answer; cablinginstall (OFNR/OFNP) → §8.5; HPD broadband guidance (FCC bans exclusive / graduated revenue share / sale-leaseback of inside wiring) → §8.5, §9 "free wiring offer" question; Verizon end-2013 Queens 90% premises passed → §5.5.
- Angi / HomeAdvisor / Fixr: no fiber cost page returned (silo finding) — stated on page, not quoted. Yelp 1–3★: EMPTY.

### Landmarks, buildings, corridors
- `Long Island City rezoning 2001 Court Square office towers Hunters Point residential growth units` · WebSearch → https://www.nyc.gov/assets/planning/download/pdf/plans/long-island-city-mixed-use/lic.pdf (WebFetch, DCP summary updated Oct 2 2001): adopted July 26 2001; 37 blocks bounded roughly by 23rd St, 41st Ave and Sunnyside Yards; low-density manufacturing replaced with higher-density commercial/mixed use; large-floor-plate offices as of right; EIS projected ~5.0M sq ft office + 300 units; Court Square 1986 rezoning enabled the 1.25M sq ft Citibank tower. → §5 para 4, §5.5, LIC section para 1.
- `One Court Square Citigroup building Long Island City floors height tallest Queens Skyline Tower` · WebSearch → https://en.wikipedia.org/wiki/One_Court_Square (WebFetch): 673 ft, 50 storeys, completed 1989 for Citigroup, 2501 Jackson Ave above Court Square–23rd St station; tallest in Queens until Skyline Tower topped out 2019. → §8 card, §13 card.
- `Hunters Point South Long Island City housing units completed waterfront towers` · WebSearch → https://newyorkyimby.com/2021/12/tf-cornerstone-completes-1194-unit-residential-complex-in-hunters-point-south-queens.html (WebFetch, Dec 4 2021): 52-03 and 52-41 Center Blvd; 1,194 rentals incl. 719 affordable; 46 and 56 storeys. → §5 para 4, §8 card.
- `Silvercup Studios Long Island City former bakery stages history Silvercup sign` · WebSearch → https://en.wikipedia.org/wiki/Silvercup_Studios (WebFetch): former Silvercup Bakery, 42-25 21st St, built 1929–30 by Gordon Baking Co., closed 1975; studio founded 1983 by Alan and Stuart Suna; Sopranos, Sex and the City, 30 Rock, Mad Men etc. → §7 card, §8 card, §13 card.
- `Silvercup Studios Kaufman Astoria Studios Queens film studio stages square feet` · WebSearch → https://www.hollywoodreporter.com/business/business-news/kaufman-astoria-studios-original-home-of-paramount-sold-to-hackman-square-mile-1235045598/ (WebFetch): opened 1920, original home of Paramount; 11 soundstages; 325,000 sq ft production offices; buyers Hackman Capital Partners and Square Mile Capital (bids March 2021; Bloomberg URL dated 2021-11-10); same buyers acquired Silvercup Sept 2020. → §8 card, §13 card.
- `Long Island City data center colocation Queens building fiber carrier` · WebSearch → https://inflect.com/building/23-10-43rd-avenue-long-island-city (WebFetch): data-centre building listing at 23-10 43rd Ave, Zayo and Lumen shown in-building; operator/size not stated. → LIC section para 4 (as "industry directories list").
  - Same query → https://investor.conedison.com/news-releases/news-release-details/con-edison-communications-signs-15000-sq-ft-lease-long-island (WebFetch): 29-76 Northern Blvd lease, 15,000 sq ft; year not stated. NOT used (undated).
- `JFK airport New Terminal One Terminal 6 redevelopment cost opening 2026` · WebSearch → https://www.6sqft.com/works-begins-on-final-jfk-airport-project-terminal-6/ (WebFetch, Feb 24 2023): $18B JFK transformation; T6 $4.2B, ~1.2M sq ft, 10 gates, first gates 2026, completion 2028; New Terminal One $9.5B, 2.4M sq ft, largest international terminal. → §13 card, airport section para 1 ("reported at about $18 billion").
- `JFK airport cargo area air cargo warehouses Springfield Gardens Rockaway Boulevard logistics Queens` · WebSearch → https://www.stattimes.com/air-cargo/270-million-consolidated-cargo-handling-center-opened-at-jfk-airport-1355091 (WebFetch, Apr 25 2025): $270M, 350,000 sq ft, north cargo area, PANYNJ + Realterm, WFS operator, first new JFK cargo facility in 25 years, temperature-controlled space (2–8°C, 15–25°C); JFK 1.67M tonnes cargo 2024, 8th-busiest US cargo airport, ~25% of inbound low-value e-commerce. → §5.5, §8 card, §9 cold-room question, §13 card, airport section.
- `LaGuardia Airport Terminal B new terminal cost completed $8 billion redevelopment` · WebSearch → https://www.portauthoritybuilds.com/redevelopment/us/en/lga.html (WebFetch via redirect from anewlga.com fact sheet): $8B, "first complete rebuild of a U.S. airport in over 25 years", completed 2024, 78 gates; Terminal B 1.3M sq ft, phases 2018–2022. → §13 card, airport section.
- `Queens College campus acres buildings Flushing CUNY` · WebSearch → https://en.wikipedia.org/wiki/Queens_College,_City_University_of_New_York (WebFetch): 83 acres off Kissena Blvd, founded 1937, 40+ buildings incl. six early-20th-c. Spanish-style buildings. → §13 card.
- `Jackson Heights Historic District designated 1993 garden apartments buildings Landmarks Preservation Commission` · WebSearch → https://hdc.org/borough/jackson-heights/ (WebFetch): designated Oct 19 1993; built mainly 1914–1939; "first and largest garden-apartment community" in the US. → §8.5 landmark callout, neighbourhood section.
- `Willets Point redevelopment soccer stadium Queens opening 2027 housing units` · WebSearch → https://www.cbsnews.com/newyork/news/new-york-city-football-club-stadium-willets-point-queens/ (WebFetch, Nov 16 2022): 25,000 seats, expected 2027, 2,500 affordable units. → §5 para 4.
- `Downtown Jamaica rezoning 2007 368 blocks Jamaica Plan AirTrain commercial` · WebSearch → https://citylandnyc.org/jamaica-rezoning-approved-with-modifications (WebFetch, Sept 15 2007): Council approved Aug 22 2007; upzone downtown core / downtown shopping district; urban renewal near AirTrain/LIRR station; block count inconsistent (378 vs 368) — no block count used. → §8 card, neighbourhood section.
- `Flushing Main Street commercial district busiest intersection Queens business improvement district` · WebSearch → https://old.nyc.streetsblog.org/2019/12/10/flushing-hopes-for-its-own-miracle-on-main-street (WebFetch, ~Dec 2019): Chamber's Choe — pedestrian count "only second to Times Square"; ~200,000 daily bus passengers on Main St (DOT); 15+ bus lines. → §8 card.
- `Queens industrial business zones Maspeth JFK Steinway Long Island City IBZ number of businesses` · WebSearch → https://www.nycctp.com/ibzs/ (WebFetch): seven Queens IBZs — Jamaica, JFK, Long Island City, Maspeth, Ridgewood/SoMA, Steinway, Woodside; no business counts. → §5.5.
- `7 train elevated Roosevelt Avenue Queens Boulevard Flushing Line viaduct history` · WebSearch → https://en.wikipedia.org/wiki/52nd_Street_station_(IRT_Flushing_Line) (WebFetch): elevated station on a steel viaduct above Roosevelt Ave; line curves onto a concrete viaduct above Queens Blvd west of the station; opened April 21 1917. → §9 elevated-train question, neighbourhood section.
- `Queens housing stock share one- and two-family homes Queens co-op apartments garden apartment complexes statistic` · WebSearch → https://www.furmancenter.org/wp-content/uploads/ee-legacy/Queens%202010.pdf (WebFetch): 835,127 housing units (2010), rental vacancy 2.7%; no building-type shares. NOT used on page (no building-type split available). Building-type share for Queens: EMPTY.

### Local news / hyperlocal
- `Hurricane Ida 2021 Queens basement apartments deaths flooding` · WebSearch → https://queenspost.com/... → redirect https://qns.com/2021/09/queens-storm-death-toll-rises-to-11-after-three-bodies-found-in-flooded-flushing-basement-nypd/ (WebFetch, QNS Sept 3 2021): Queens toll 11 (citywide 13); 10 died in flooded basement apartments — East Flushing (153-10 Peck Ave near Kissena Park), Woodside, Jamaica, Forest Hills, Elmhurst. → §5 para 4, §5.5, "After Ida" section. (Street address not used on page.)
- NYC Council internet-access page (silo source) re-queried for Queens → https://council.nyc.gov/data/internet-access/ (WebFetch): "Jamaica-St. Albans-Hollis (Queens CD12): 41%" households without broadband subscription; no other Queens district named. → §5.5, neighbourhood section (Jamaica).
- Queens Chronicle / Queens Ledger / Patch / QNS items on fiber-installation contractors 2026: EMPTY (none retrieved).

### Local licensing / permits / building rules
- No new Queens-specific permit source. Silo sources reused: sub-50 V cabling generally no DOB permit (site's existing structured-cabling-pricing statement) + firestopping (unifinerds/nyflnerds) → §8.5; LPC permit for exterior work in historic districts (silo LPC sources) + Jackson Heights HD designation → §8.5; HPD/FCC fair-access → §8.5, §9.
- Port Authority / airport tenant alteration rules: not researched; page states we do not work inside terminals and makes no claim about airport approvals. EMPTY.

### Pricing used (existing AESS prices — no new prices)
- Drops from the live Queens configurator, repo file structured-cabling-pricing-queens.html: fiber_mm $391, fiber_sm $447.
- Remaining items = silo base (Brooklyn 1.00×) × blueprint §9 Queens 1.05×, rounded half-up: $35→$37 termination; $40→$42 OTDR/strand; $4,500–$7,000→$4,725–$7,350 (12-strand OM4); $8,000–$15,000+→$8,400–$15,750+ (24-strand OS2); $2,400→from $2,520 (second room). $195/hr, 3-hr minimum ($585) protected, unchanged.
- Starter package = 24 × $37 + 12 × $42 = $1,392.
- CONFLICT for review: §9 1.05× would make the drops $368 / $420; the live Queens configurator shows $391 / $447 (≈1.12×, same as the Bronx configurator). This page follows the Manhattan sibling's precedent (configurator drop prices + §9 multiplier for the rest), whereas the Long Island and Hudson Valley pages applied §9 to the drops too.

### Images (11) — permanent image rule; Drive folder `AESS Website Photos/Fiber Optic Installation` empty, CompanyCam not connected
images: 11 reused from images/low-voltage/ (no real Fiber Optic Installation photos yet). Scene check: all but the fusion-splice scene are scenes not used on any earlier fiber page (perceptual-hash comparison); source files taken from the first half of the alphabetical list (bronx/brooklyn/dutchess/long-island) to avoid the Bronx builder.
| File (images/fiber-optic-installation/) | Source (images/low-voltage/) | Shows |
|---|---|---|
| fiber-optic-installation-queens-fusion-splicer-cleaver-rack.webp | low-voltage-installation-dutchess-county-05-fiber-fusion-splice.jpg | fusion splicer, cleaver, pigtail tray, IPA bottle, fiber rack (scene also on earlier fiber pages, different source file) |
| fiber-optic-installation-queens-open-ceiling-jhook-bundle.webp | low-voltage-installation-bronx-02-jhook-pathway-bundle.jpg | blue cable bundle into J-hooks, open office ceiling |
| fiber-optic-installation-queens-wall-outlet-certification-pass.webp | low-voltage-installation-bronx-07-fluke-certification-pass.jpg | handheld certification tester showing PASS at a wall outlet |
| fiber-optic-installation-queens-keystone-wall-plate-punchdown.webp | low-voltage-installation-bronx-08-keystone-wall-plate-termination.jpg | keystone jack termination at a wall plate |
| fiber-optic-installation-queens-ceiling-access-point-cable.webp | low-voltage-installation-bronx-09-ceiling-access-point-drop.jpg | ceiling access point with cable from open grid |
| fiber-optic-installation-queens-entry-video-intercom-wiring.webp | low-voltage-installation-bronx-11-video-intercom-entry-wiring.jpg | video intercom panel wiring at an entrance |
| fiber-optic-installation-queens-door-card-reader-wiring.webp | low-voltage-installation-bronx-14-access-control-reader-wiring.jpg | card reader at a glass door |
| fiber-optic-installation-queens-conference-camera-display-mount.webp | low-voltage-installation-bronx-ptz-camera-mount.jpg | video-conference camera mounted above a wall display |
| fiber-optic-installation-queens-metal-stud-cable-fish.webp | low-voltage-installation-bronx-stud-rough-in-boxes.jpg | cable threaded through metal studs, outlet box |
| fiber-optic-installation-queens-retail-ceiling-cable-pull.webp | low-voltage-installation-brooklyn-retail-store-ceiling-pull.jpg | cable pull across an open retail-store ceiling |
| fiber-optic-installation-queens-school-corridor-ceiling-pull.webp | low-voltage-installation-long-island-02-school-ceiling-pathway.jpg | cable pull through a school corridor ceiling |
Review note: these library photos look AI-generated (garbled small text, uniform branding) and several show partial faces in profile and an 800-486-0943 number on shirts — same caveat already logged for the Long Island page. Only 3 of 11 show fiber specifically (splicer; the rest are general cabling/low-voltage scenes captioned as such).

### Keyword plan (Queens page)
Service: fiber optic installation Queens, building fiber backbone, multi-tenant fiber, co-op fiber, fusion splicing, OTDR testing, strand mapping, temporary/tactical fiber. Problem: provider won't wire building, landlord easement, hallway coax, unknown legacy multimode, flooded basement (Ida), cold-room penetration, elevated-train EMI/vibration, subdivided commercial buildings, preferred-vendor lease rules. Technology: OS2, OM4, OM1 legacy, indoor/outdoor, armoured, OFNR/OFNP, MPO/LC/SC, lockable enclosures, media converters, pre-terminated/tactical cable. Industry: co-ops/garden apartments, mixed-use landlords, subdivided commercial buildings, film/TV studios and post houses, cargo/forwarders/cold chain, office towers, schools/campuses. Geographic: Queens, Long Island City, Court Square, Queens Plaza, Hunters Point, Dutch Kills, Astoria, Steinway, Sunnyside, Woodside, Maspeth, Jackson Heights, Elmhurst, Corona, Flushing, College Point, Whitestone, Forest Hills, Rego Park, Kew Gardens, Jamaica, Hollis, St. Albans, Springfield Gardens, Ozone Park, Howard Beach, Bayside, Fresh Meadows, Rockaways, Broad Channel, JFK, LaGuardia, Willets Point.

### Question register additions
fiber-optic-installation-queens
§9 Questions Answered (and other question headings):
- Has a Queens Fiber Link Gone Dark? (repair capture heading)
- Our Flushing building has dozens of small shops and offices — how does each tenant get its own internet service without a new hole for every one?
- In a mixed-use building with stores below and apartments above, can one backbone serve both while keeping them apart?
- Can the coaxial cable a cable company left running through our hallways be replaced with fiber the building owns?
- A provider has offered to wire our building at no charge — what should an owner check before signing?
- Our Long Island City landlord has a preferred telecom contractor — can we still bring in our own fiber installer?
- Our co-op is several walk-up buildings around a shared garden — can one fiber plant serve every building from a single basement room?
- Do you need to get into individual apartments or offices to run a building backbone, and how is that arranged with shareholders?
- Our building has old multimode fiber from the 1990s — can it carry today's speeds or does it need replacing?
- We have fiber between floors but nobody knows which strands are in use — can you sort it out without taking the network down?
- We rent a stage or production space for a season — can temporary fiber go in and come out cleanly when the show wraps?
- Can fiber run into a refrigerated or freezer room in a warehouse near JFK?
- The elevated 7 train runs right past our building — will vibration or electrical noise from the trains affect fiber?
- Owner fiber, the provider's wiring, or more Wi-Fi: which fixes a Queens building? (§10 EQUIPMENT comparison heading)
§17 FAQ:
- Do you cover the Rockaways, Broad Channel and the neighbourhoods along the Nassau border?
- How far ahead of a move-in or lease date should we book fiber work?
- Can you issue a certificate of insurance that our property manager or co-op will accept?
- Is pre-terminated fiber faster to install than splicing on site?
- Can our phone system run over the same fiber as our data?
- Can the fiber enclosures be locked so other tenants cannot get into them?
- How much wall space does a fiber enclosure need?
- Is it safe for staff to handle fiber patch cords?
- Can existing fiber be rerouted when we renovate a floor or a basement?
- Do you offer an annual check of a building's fiber plant?
- What does the installation warranty cover?
- What should we have ready when we call for a Queens quote?

De-dup notes: checked against the register (NYC, Manhattan, Brooklyn, Long Island, Hudson Valley) and the parallel Bronx page. Deliberately avoided: cellar/flood-room question (Manhattan has it — Ida is covered in prose only), studio production-video question (Brooklyn), landmark-district question (Manhattan), cutover-downtime question (NYC hub), coverage-pricing question. Closest calls with the parallel Bronx page for a human read: my co-op-around-a-garden question vs Bronx "courtyard building with several wings … own riser?" (multi-building vs multi-wing); my unit-access question vs Bronx "notice residents need before hallway work"; my strand-mapping question vs Bronx "audit existing fiber before we buy or lease". The repair heading was changed from "Fiber Link Down Somewhere in Queens?" because the Bronx page uses the same masked wording.

## Bronx — local research (2026-10-17 batch, fiber-optic-installation-bronx)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources above are reused where noted; only Bronx research is added here. Page thesis: the Bronx builds big — fiber here is a site plan for many buildings/wings (Co-op City, Parkchester, courtyard apartment houses on the Concourse) and for 24-hour cold-chain operations at Hunts Point, not one cable between two closets.

### Reddit (local)
- Query: `reddit Bronx apartment building fiber internet Fios not available` · Firecrawl web search (excerpts only; reddit.com threads not opened).
  - https://www.reddit.com/r/Fios/comments/1rkb228/fios_available_to_all_my_neighbors_but_not_me/ — title "Fios available to all my neighbors but not me - Bronx Tremont area"; excerpt: "FiOS unavailable at my address, but available directly behind me and across the street." → §5 THE NEIGHBORHOOD para 2.
  - https://www.reddit.com/r/Fios/comments/1oz9xcz/1_gb_fios_installion_in_a_5thfloor_apt_bronx_nyc/ — title only ("1 GB Fios Installion in a 5th-Floor APT, Bronx NYC"). Not used.
- Query: `reddit bronx co-op building internet wiring old building ethernet landlord riverdale OR "grand concourse"` · Firecrawl web search.
  - https://www.reddit.com/r/Fios/comments/1s6zslh/coop_city_bronx_what_am_i_looking_at_here/ — title "Coop city Bronx - what am I looking at here?"; excerpt: "Incoming fiber and 2 distribution hubs." → §5 para 2.
  - https://www.buildinghealthx.com/services/internet-providers/riverdale — excerpt: "The advantage of 5G Home for Riverdale: no landlord or co-op board approval required, no wiring, plug-and-play setup in 15 minutes." → §10.5 H3 5.
  - https://www.verizon.com/home/internet/near-me/new-york-ny/ — excerpt: "In apartment buildings or homes not yet wired for Fios: Verizon coordinates with the property manager/owner to wire and install the service." → §10.5 H3 4.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitute for §10.5 reality check — claims quoted from published sources:
- Query: `fiber optic cable installation cost 2026 homeguide OR angi OR forbes per foot business building` · Firecrawl web search (excerpts):
  - https://www.angi.com/articles/fiber-optic-cable-installation-cost.htm (dated May 3, 2026 in excerpt): "Fiber optic cable installation costs average $4,500 for most homeowners, with most installations ranging from $1,500 to $7,000." → §10.5 H3 1.
  - https://ringandping.com/how-much-does-fiber-optic-cable-installation-cost-in-2026/ : "Residential projects typically range from $1,500 to $6,000, while commercial fiber optic cabling services can scale into six figures for complex builds." → §10.5 H3 2.
  - https://unio.digital/blog/fiber-optic-installation-cost : "single-mode fiber is cheap at roughly $0.09 to $1.49 per foot, while multimode OM3/OM4 runs about $1.50 to $6.00 per foot"; interior $1–$6/ft. → §10.5 H3 3.
  - Silo source reused: lowvoltagenewyork.com ("In Manhattan and the Bronx, you rent the underground… Empire City Subway, a franchise dating to 1891") → §10.5 H3 6.
  - CUF report (below) 99.8% figure → §10.5 H3 7.
- Yelp: not searched directly; no yelp.com results in any Bronx query. EMPTY.

### Broadband / digital divide (Bronx)
- Query: `Bronx broadband fiber internet news 2025 2026 NYCHA buildings Bronx Times` · Firecrawl web search →
  - https://nycfuture.org/research/understanding-and-overcoming-the-bronx-digital-divide (Firecrawl scrape, report dated July 2025): 22.4% of Bronx households lack home broadband (lowest adoption); 44% of households enrolled in ACP when it ended in 2024 (243,275 at peak); one in three households (184,000+) lack a computer; 113,000+ (19.2%) smartphone-only; "nearly 99.8 percent of the Bronx is now wired for high-speed internet"; "problems remain—including individual buildings not yet wired for broadband and limited competition in some areas"; broadband = 1.1% of household income in the Bronx vs 0.53% Manhattan. → §5 para 1, §5.5 facts, §10.5 H3 7, Affordable Housing section para 1.
  - https://www.bxtimes.com/mayor-mamdani-ritchie-torres-high-speed-internet/ (Bronx Times, May 4, 2026): $2M expansion of Neighborhood Internet; announced at St. John's House II near the Melrose Library; "microtrenching, rooftop network equipment installation, dedicated internet access systems and in-unit connectivity across approximately 50 buildings"; programme launched 2025. → Affordable Housing section para 2; "Across the Borough" Mott Haven H3.
  - https://www.osc.ny.gov/files/reports/pdf/report-20-2025.pdf (excerpt): Bronx 36.7% households with no broadband access (2023, different metric). NOT used (conflicting definition vs CUF/Council).
- Silo sources reused: council.nyc.gov internet-access (Melrose–Mott Haven–Port Morris 44%, highest district) → "Across the Borough" Mott Haven H3; nyc.gov Big Apple Connect (Sept 2025; ~220 NYCHA developments; extended through June 2028) → Affordable Housing para 2.

### Building stock, complexes, landmarks
- Query: `Co-op City Bronx buildings apartments number towers largest cooperative housing` · Firecrawl web search →
  - https://www.coopcity.com/ (excerpt): "Mitchell-Lama housing cooperative in the northeast Bronx with 15,372 residential units in 35 high-rise buildings and seven (7) townhouse clusters".
  - https://www.coopcity.com/apartments (excerpt): "world's largest housing cooperative"; ten chevron buildings 24 storeys/414 apts; fifteen towers 33 storeys/384; ten triple-core 26 storeys/500.
  - https://en.wikipedia.org/wiki/Co-op_City,_Bronx (excerpt): constructed 1966–73. → §5.5, Large Residential Sites section, §13 card, hero.
- Query: `Parkchester Bronx 171 buildings apartments complex history` · Firecrawl web search →
  - https://www.parkchesternyc.com/about-us/history/ (excerpt): MetLife, 129 acres, central heating plant, 51 building clusters, Richmond H. Shreve; 12,271 apartments; Macy's first branch.
  - https://www.parkchesternyc.com/about-us/ (excerpt): "171 buildings located on 129 landscaped acres".
  - https://en.wikipedia.org/wiki/Parkchester,_Bronx (excerpt): built 1939–1942; "51 groups of buildings were planned to house 12,000 families"; 171 brick buildings, eight or 13 storeys; Macy's branch 1941. → §5.5, Large Residential Sites, §13 card, regional H3.
- Query: `Grand Concourse Historic District art deco apartment buildings designated` · Firecrawl web search → https://hdc.org/buildings/grand-concourse-historic-district/ (excerpt): "Designated October 25, 2011 … incomparable concentration of Art Deco and Art Moderne apartment buildings … built between 1916 and 1941 in styles ranging from neo-Renaissance to … Art Deco." → §5.5, §7 cards, §13 card, regional H3.
- Query: `Hunts Point Food Distribution Center acres businesses jobs Bronx` · Firecrawl web search → https://huntspointcoopmkt.com/ (excerpt: ~2,400 employees in the Coop Market — not used, conflicts with EDC 2,000); https://www.nycfoodpolicy.org/hunts-point-food-distribution-center/ (excerpt: 103 acres — not used); https://edc.nyc/project/hunts-point-peninsula (Firecrawl scrape): FDC >100 wholesalers/distributors/manufacturers incl. Terminal Produce Market, Meat Market, Fulton Fish Market; 4.5 billion lbs/yr; 8,500 direct jobs; 12% of food distributed to NYC; Produce Market opened 1967, >100 acres, four primary warehouses, 26 merchants, ~2,000 employees; Dec 2025 Aurora-Primus conditional selection, NYCEDC's largest design-build; peninsula >12,600 residents. → §5.5, §8 card, Hunts Point section, §13 card, regional H3, New Construction section.
- Query: `Hunts Point Produce Market redevelopment new building NYCEDC 2025` · Firecrawl web search → https://edc.nyc/press-release/historic-agreement-advance-redevelopment-hunts-point-produce-market (excerpt: $405M; intermodal facility; nearly 13,000 residents); https://www.nyc.gov/mayors-office/news/2025/12/mayor-adams--nycedc-announce-historic-agreement-to-advance-redev (excerpt: "Construction is expected to begin in late 2026"). → Hunts Point section para 1, §13 card.
- Query: `Hunts Point resiliency flood risk peninsula energy project coastal storm Bronx` · Firecrawl → https://edc.nyc/project/hunts-point-resiliency (Firecrawl scrape): Hunts Point Energy Resiliency Project; HUD Rebuild by Design $20M; total budget $71M; microgrid/back-up power to FDC food businesses; solar + storage at MS 424 and PS 48; Sandy (Oct 2012) highlighted waterfront vulnerability. → Hunts Point section para 4.
- Query: `Kingsbridge Armory redevelopment 2025 plan Bronx square feet` · Firecrawl → https://edc.nyc/press-release/city-council-approves-historic-vision-kingsbridge-armory-bronx (Firecrawl scrape): 180,000 sq ft column-free Drill Hall; phase 1 groundbreaking 2026, completion 2030; ~500 permanently affordable units on adjacent National Guard site, 2032; $216M city/state/federal; ~3,600 jobs. → §5 para 4, §5.5, §9 high-ceiling Q, §13 card, New Construction section.
- Query: `Penn Station Access Metro-North new Bronx stations Hunts Point Parkchester Morris Park Co-op City opening` · Firecrawl →
  - https://www.nyc.gov/content/planning/pages/our-work/plans/bronx/bronx-metro-north-area (excerpt): four stations; plan approved by City Council August 2024 (~7,000 new homes per linked release); "MTA anticipates that the new stations will open in 2027".
  - https://www.cityandstateny.com/politics/2025/07/mtas-metro-north-penn-station-access-project-snags-another-delay/406937/ (excerpt, July 2025): "won't be completed until at least 2028." → §5 para 4, New Construction section, regional H3s. Both dates stated with attribution.
- Query: `Bronx Terminal Market Gateway Center retail square feet Major Deegan` · Firecrawl → https://en.wikipedia.org/wiki/Bronx_Terminal_Market (excerpt: just under 1M sq ft retail on 17-acre site south of Yankee Stadium); https://www.related.com/our-company/properties/bronx-terminal-market (excerpt: parking for 2,600 cars). → §8 card, regional H3.
- Query: `Hutchinson Metro Center Bronx office campus square feet tenants` · Firecrawl → https://www.hutchinsonmetrocenter.com/atrium.html (excerpt: Metro Center Atrium 360,000 sq ft, three floors Class A office and medical, retail, 125-room Residence Inn); https://simonedevelopment.com/... (excerpt: 1200 Waters Place). Secondary "1.4 million sq ft" figure (nancyjkelley.com case study) NOT used. → §8 card, regional H3.
- Query: `Montefiore Medical Center Moses campus Bronx beds hospitals number` · Firecrawl → ahd.com profile (excerpt: 1,499 staffed beds) — NOT used (third-party figure); Moses campus named only. → §8 card, regional H3.
- Query: `Jacobi Medical Center campus Pelham Parkway NYC Health + Hospitals Bronx beds Lincoln Hospital` · Firecrawl → https://www.nychealthandhospitals.org/locations/jacobi/ (excerpt): 1400 Pelham Parkway South; 457 beds; Level 1 trauma; "Only Burn Center in the Bronx or Southern Westchester". → §8 card, regional H3.
- Query: `Fordham University Rose Hill campus acres Bronx buildings` · Firecrawl → https://www.fordham.edu/about/campuses/rose-hill-campus/ (excerpt): 85 acres, Gothic architecture, north Bronx. → §13 card, §8 card.
- Query: `Lehman College campus acres Bedford Park Bronx Jerome Park Reservoir` · Firecrawl → https://www.lehman.edu/admissions/maps-and-directions/ (excerpt): 37-acre campus between Kingsbridge and Bedford Park along the Jerome Park Reservoir; neighbours Bronx High School of Science, Walton HS, DeWitt Clinton HS. → regional H3 (Fordham/Bedford Park).
- Query: `Manhattan College Riverdale campus acres Bronx; New York Botanical Garden 250 acres Bronx Park` · Firecrawl → https://en.wikipedia.org/wiki/New_York_Botanical_Garden (excerpt: 250 acres, Bronx Park, est. 1891). Manhattan College: no fact retrieved (named only). → §13 Fordham card.
- Query: `Port Morris Mott Haven industrial lofts Bruckner Boulevard warehouses converted offices Bronx waterfront development` · Firecrawl → https://www.nyc.gov/assets/planning/download/pdf/plans/port-morris/port_morris.pdf (Firecrawl scrape): Port Morris/Bruckner Boulevard rezoning adopted by City Council March 9, 2005; industrial/commercial uses in "large brick and concrete industrial buildings ranging from one to six stories" mainly along Bruckner Blvd; 50 lofts in the former Estey Piano Factory converted; "warehouse space is already being converted into lofts". → §7 card, §8 card, regional H3.

### Local codes / programmes used for Q&A
- Query: `NEC 620.37 wiring in elevator hoistway only elevator wiring permitted communication cables` · Firecrawl → https://up.codes/s/wiring-in-hoistways-machine-rooms-control-rooms-machinery-spaces-and-control-spa (excerpt: wiring "associated with elevators and dumbwaiters are allowed in hoistways"); https://www.electriciantalk.com/threads/elevator-pit-circuits-how-you-interpe-620-37.294313/ (excerpt quoting 620.37(A) "Only such electrical wiring, raceways, and cables used directly in connection with the elevator…"). → §8.5 callout, §9 hoistway Q.
- Query: `E-Rate Category Two internal connections cabling eligible schools libraries USAC` · Firecrawl → https://www.usac.org/e-rate/applicant-process/before-you-begin/eligible-services-overview/ (excerpt: C2 includes "routers, switches, wireless access points, and cabling" within instructional buildings of a school campus or non-administrative library buildings); https://www.usac.org/e-rate/get-started/ (excerpt: "discounts of up to 90 percent"). → §9 E-Rate Q, Medical & Education section.
- Silo sources reused: DOB sub-50 V permit statement (existing site content), firestopping (unifinerds/nyflnerds), OFNR/OFNP (cablinginstall), HPD/FCC exclusivity ban → §8.5 callouts, §10.
- Asbestos (FAQ) and sidewalk-shed/facade (Q&A) answers state general practice only — no statute, number or agency deadline cited. Flag for Anwar if a citation is wanted.
- Local news on Bronx fiber-installation contractors 2026: EMPTY (only the Neighborhood Internet item above).

### Pricing used (existing AESS prices only — no new prices)
- structured-cabling-pricing-bronx.html (live configurator): fiber_mm $391, fiber_sm $447 per drop.
- research "Pricing" (silo) + Brooklyn/Manhattan pages, Bronx = 1.00× (blueprint §9): $35/termination, $40/strand OTDR, 12-strand OM4 $4,500–$7,000, 24-strand OS2 $8,000–$15,000+; network-installation-bronx.html: "Additional zone room with fiber link back — from $2,400" (matches base); $195/hr 3-hr min ($585) protected.
- Packages: Starter $894 (2 × $447 SM drops), Standard $4,500–$7,000, Premium $8,000–$15,000+.
- CONFLICT for review: §9 says Bronx 1.00× (would give drops $350/$400), but the live Bronx configurator publishes $391/$447 (≈1.12×). Followed the Manhattan sibling's precedent (drops taken from that borough's live configurator, everything else at the §9 multiplier).

### Images (11) — permanent image rule; Drive folder `AESS Website Photos/Fiber Optic Installation` empty, CompanyCam not connected
All saved to images/fiber-optic-installation/ as WebP (q80, ≤1600 px). Sources taken from the second half of the alphabetical candidate lists (Rockland→Westchester names).
| File | Source | What it shows |
|---|---|---|
| fiber-optic-installation-bronx-fusion-splicer-fiber-patch-panel.webp (hero) | low-voltage/low-voltage-installation-rockland-county-hero-fiber-splice-tray.jpg | fusion splicer under rack of blue fiber adapters/yellow jumpers |
| fiber-optic-installation-bronx-splicer-screen-yellow-patch-cords.webp | low-voltage/low-voltage-installation-westchester-county-05-fiber-fusion-splice.jpg | splicer screen, yellow cords, cleaver, IPA |
| fiber-optic-installation-bronx-conduit-pull-box-block-wall.webp | low-voltage/low-voltage-installation-ulster-county-hero-riser-conduit-pull.jpg | pull box on EMT, block wall |
| fiber-optic-installation-bronx-corridor-bundle-ceiling-pull.webp | network/network-installation-suffolk-county-idf-riser-cable-bundle.webp | bundle pulled into open corridor ceiling |
| fiber-optic-installation-bronx-emt-conduit-sweep-pull.webp | network/network-installation-ulster-county-network-drop-conduit-emt-riser.webp | EMT sweep on block wall |
| fiber-optic-installation-bronx-idf-rack-patching-floor-closet.webp | low-voltage/low-voltage-installation-staten-island-hero-idf-rack.jpg | IDF rack patching, UPS |
| fiber-optic-installation-bronx-crew-open-ceiling-fitout.webp | low-voltage/low-voltage-installation-suffolk-county-03-crew-cable-pull.jpg | four-person crew, open ceiling, reels |
| fiber-optic-installation-bronx-service-van-reels-ladders.webp | low-voltage/low-voltage-installation-staten-island-van-load-out.jpg | service van with ladders/reels (no plate visible) |
| fiber-optic-installation-bronx-exterior-enclosure-brick-conduit.webp | low-voltage/low-voltage-installation-ulster-county-02-exterior-enclosure-install.jpg | outdoor enclosure on brick wall, EMT |
| fiber-optic-installation-bronx-warehouse-lift-cable-tray.webp | low-voltage/low-voltage-installation-orange-county-hero-warehouse-cable-tray.jpg | scissor lift, basket tray, dome camera, racking |
| fiber-optic-installation-bronx-core-drill-cmu-wall.webp | network/network-installation-westchester-county-core-drill-cmu-wall-penetration.webp | core drilling block wall |
Note: the same scenes exist under other area filenames and several overlap scenes on sibling fiber pages (splicer, EMT sweep, core drill, exterior enclosure, warehouse tray) because the library has few fiber scenes. Every library photo shows a technician's face in profile and shirts/van print a phone number (800-486-0943 or 844-386-7238); several look AI-rendered (garbled small text) — same flag as earlier builders, for Anwar's review. Photos with full frontal faces (toner-tracing, labeling) were rejected.

### Keyword plan (Bronx page)
Service: fiber optic installation Bronx, fiber backbone Bronx, multi-building complex fiber, courtyard building riser, cold storage fiber, fusion splicing, OTDR testing, fiber audit. Problem: building not wired, wings with separate stair halls, no riser/elevator hoistway off limits, freezer/cooler entries, forklifts, rodents, asbestos in cellars, sidewalk sheds, phased budgets. Technology: OS2, OM4, interlocking armor, indoor/outdoor, OFNR/OFNP, innerduct, splice trays, media converters/SFP. Industry: co-ops/Mitchell-Lama/NYCHA-adjacent affordable housing, food distribution/cold chain, hospitals/medical offices, colleges/schools/libraries (E-Rate), retail corridors, new construction, venues. Geographic: Bronx, Co-op City, Parkchester, Grand Concourse, Hunts Point, Port Morris, Mott Haven, Melrose, Fordham, Bedford Park, Norwood, Riverdale, Kingsbridge, Morris Park, Pelham Parkway, Westchester Square, Throgs Neck, City Island, Williamsbridge, Wakefield.

### Question register additions
fiber-optic-installation-bronx
§9 Questions Answered (and other question headings):
- Bronx Fiber Link Cut or Gone Dark? (repair capture heading)
- On a site with dozens of high-rises, which building should host the main fiber room?
- Can a complex's fiber be installed in phases over several budget years?
- Can fiber be run through an old steam or utility tunnel between buildings?
- In a courtyard building with several wings and stairwells, does each wing need its own fiber riser?
- How is fiber routed through an Art Deco lobby without harming the original finishes?
- Is the elevator hoistway ever allowed as the route for fiber between floors?
- What notice do residents need before fiber work starts in the hallways of an occupied building?
- How is fiber protected from forklifts and pallet jacks on a busy market or warehouse floor?
- Our building has a sidewalk shed up for facade work — can fiber work still go ahead?
- How do you keep rats and mice from chewing fiber in a basement or warehouse?
- Which fiber items belong on the architect's drawings for a new building, and which can wait for the fit-out?
- How is fiber supported across a hall with a very high, column-free ceiling?
- Can a Bronx school or library use E-Rate funding for internal fiber?
- How Many Buildings? Where Does Service Land? That's Our Starting Point. (CTA heading, no "?" at end — not a question)
- Bronx Building Offline Right Now? (final repair heading)
§17 FAQ:
- Can fiber connect our boiler-room controls or building management system to the office?
- Do you carry fiber materials on the truck, or does everything have to be ordered?
- What deposit is needed before a Bronx fiber job is scheduled?
- Can you audit an existing fiber installation before we buy or lease a building?
- Can the network rack sit in the super's office or a closet instead of a dedicated room?
- Who handles firestopping on the holes you make — you or the building's contractor?
- Do you patch and paint the walls and ceilings you open?
- What happens if our cellar has old pipe insulation or floor tile that might contain asbestos?
- Can you run fiber to a laundry room or package room for card readers and lockers?
- Can fiber run near the gas meters and gas piping in a cellar?
- Do we need an electrician as well as you?
- Will you give a fixed price, or is the work charged by the hour?

De-dup notes: after the concurrent Queens page appeared, four Bronx questions were replaced because Queens covers the same intent (provider offering free wiring, fiber into freezer rooms, vibration from elevated trains, installation warranty), plus the FAQ on routine maintenance (Queens asks about an annual fiber check). The repair heading was reworded because it masked to the same text as Queens' ("Fiber Link Down Somewhere in …?").

## Westchester — local research (2026-10-17 batch, fiber-optic-installation-westchester-county)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md are reused where noted. To be merged into research/fiber-optic-installation.md by the main run.

**Page thesis:** Westchester isn't short of carrier fiber; its problem is re-tenanting. Buildings and campuses wired for one corporate occupant (I-287 headquarters campuses, 1960s downtown towers) are being split among several tenants, converted to apartments or self-storage, or replaced by new downtown towers. The work is surveying inherited fiber and dividing or re-planning it so each new owner, tenant or household has its own tested, documented handoff. (Distinct from Manhattan = riser approvals, Brooklyn = warehouses/flood, LI = horizontal campuses, HV hub = distance and ground potential between scattered buildings.)

### Reddit (local)
- `reddit Westchester fiber internet Fios Optimum apartment building` · Firecrawl web search (excerpts only; reddit.com threads not opened).
  - https://www.reddit.com/r/Westchester/comments/1exqjsk/internet_only_providers/ — excerpt: "Optimum has fiber service now in several Westchester towns, including Briarcliff and Ossining." → §10.5 H3 7 (attributed to commenters).
  - https://www.reddit.com/r/Westchester/comments/1mbil21/optimum_vs_verizon/, /155gx0f/optimum_verizon/, /k4rfqc/optimum_vs_fios_for_internet/, /1w1kvlz/wifi_optimum_or_verizon/ — residents comparing Optimum and Verizon → §5 para 4 ("compare the two in thread after thread").
- `Westchester County office building converted to apartments former corporate headquarters 2025` · Firecrawl → https://www.reddit.com/r/Westchester/comments/13a9nda/whats_everyones_take_on_conversion_of_office/ (title only: "What's everyone's take on conversion of office buildings into rental housing?") → §5 para after facts list (no year claimed).
- `White Plains 1960s AT&T office building converted rentals apartments` · Firecrawl → https://www.reddit.com/r/Westchester/comments/1oo8vf0/white_plains_beats_houston_tx_in/ — excerpt: "White Plains added 468 new apartments after converting a 1960s AT&T office building". **NOT used**: conflicts with the 245-unit approval reported by The Journal News (could be a later revised count; unverified).
- `Westchester fiber optic cabling contractor cost office building yelp reviews` · Firecrawl → https://www.reddit.com/r/Westchester/comments/1ihhuks/handyman_contractor/ — excerpt: "he had great reviews online … 6 months of absolute nightmare contractor insanity" → §14 pricing, national-vs-local paragraph.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG — EMPTY (not accessible in build env)
### Yelp 1–3★ — EMPTY. Query `Westchester fiber optic cabling contractor cost office building yelp reviews` (Firecrawl) returned only out-of-area Yelp search pages (San Francisco, Westminster CA, Merrick, Los Angeles); no Westchester fiber reviews.
§10.5 substitutes (silo sources reused, quoted as published): unio.digital ($300–$800 per drop; 100–200 drops $15k–$30k; "orientation ranges") → H3 1; newtechcabling.com ("Small projects can take a day or two"; copper ~100 m) → H3 2, 3; lowvoltagenewyork.com (single-mode glass cheaper than OM4, SM optics 1.5–5×; OTDR $75–$150/hr, ~5%) → H3 4, 5; thenetworkinstallers.com (FBA 2025 $18.00/ft underground, $8.00 aerial) → H3 6; Westchester Telecom Network + Reddit Optimum excerpt → H3 7.

### Office market (building stock)
- `Westchester County office market report 2026 vacancy square feet` · Firecrawl search, then Firecrawl scrape (query) of https://lpc.com/wp-content/uploads/WCC_Office_MarketReport_Q2_2026.pdf — Lincoln Property Co. Q2 2026: overall vacancy 24.09%; inventory 22.66+ MSF; White Plains CBD 23.73% (1,254,200 SF vacant); East I-287 23.01% (2,009,500 SF vacant); West I-287 30.34%; Northern 16.21%; Southern 8.44%; Hudson Valley submarket 70.42%. Leases: Summit Health 86,991 SF renewal at 210 Westchester Ave (White Plains); Atlas Air 64,607 SF renewal at 1 North Lexington; Central National 62,888 SF renewal at 3 Manhattanville Rd, Purchase (East I-287); Jackson Lewis 45,868 SF new lease at 1 North Lexington; Cuddy & Feder 26,356 SF at 445 Hamilton Ave. → hero, §5 para 2 + facts, §8 cards, Q&A medical, "Reading Westchester's Office Numbers" section.
- Same search, excerpts only: https://www.colliers.com/en/research/new-york/westchester-county-office-market-snapshot-q1-2026 ("net absorption swung positive by 48,861 square feet, reducing the market's availability rate to 20.7%. The 'flight to quality' trend…") → office numbers section. https://rmfriedland.com/market_report/2026-q1-westchester-office-leasing/ ("tracks 26,445,018 square feet of office space … Class A and B buildings of 50,000 …") → office numbers section.
- Submarket geography (which towns fall in West vs East I-287) was NOT sourced; the page avoids assigning towns to West I-287 and only says East I-287 "takes in Purchase" (LPC lists 3 Manhattanville Rd, Purchase under East I-287).

### Conversions / redevelopment
- `Westchester County office building converted to apartments former corporate headquarters 2025` · Firecrawl search →
  - https://westchestermagazine.com/home/ginsburg-white-plains-1-martine/ (Firecrawl scrape, July 7 2021): former office building, 188 loft-style apartments, Ginsburg Development; "the county's first major office-to-residential redevelopment". → §5, §7 card, landmarks, conversions section.
  - https://www.multifamilyexecutive.com/design-development/corporate-park-converted-to-multifamily-real-estate-in-new-yorks-westchester-county_c (Firecrawl scrape, May 17 2021): Carraway, 421 units at 103 and 105 Corporate Park Drive, West Harrison; Toll Brothers and J.P. Morgan Global Alternatives; Platinum Mile "has seen a number of its former office sites demolished". → §5, landmarks, Campus Subdivision section, Q&A site selection.
  - https://westfaironline.com/construction/plan-to-covert-office-building-into-self-storage/ (excerpt): "540 WPR LLC, which owns an office building at 504 White Plains Road" plan to convert to self-storage. → Q&A self-storage (municipality not stated on page).
- `White Plains 1960s AT&T office building converted rentals apartments` · Firecrawl → https://www.lohud.com/story/news/local/westchester/white-plains/2017/03/09/white-plains-office-building-approved-apartments/98950974/ (scrape metadata, Mar 9 2017: "former AT&T building at 440 Hamilton Ave. will be converted into 245 luxury rental apartments"; search excerpt "12-story 1960s building"); https://dailyvoice.com/article/white-plains-reviews-plan-to-convert-old-att-building-to-apartments/ (excerpt: "boxy 12-story building at the corner of Hamilton Avenue and North Broadway"); https://westfaironline.com/economic-development/white-plains-common-council-approves-residential-conversion-for-former-att-building/ (excerpt: 245 units approved). → §5 facts, §7, landmarks, conversions section.
- `New Rochelle downtown development apartments towers number of units since 2015 rezoning` · Firecrawl →
  - https://www.newrochelleny.gov/1015/TOD-Downtown-Cluster (search excerpt: "permits construction of up to 12 million square feet of new development, 6,370 housing units and 1,200 hotel rooms"; scrape returned no body text). → §5, facts, landmarks.
  - https://www.pew.org/en/research-and-analysis/articles/2024/11/13/how-more-housing-revitalized-a-suburban-downtown (scrape, Nov 13 2024): zoning adopted late 2015; generic environmental review for the whole plan, later projects need lighter assessment; "only between a sixth and a fifth has been completed and fully occupied"; ~40-minute train to NYC. → §5 facts, Q&A New Rochelle.
  - https://www.governor.ny.gov/news/governor-hochul-announces-completion-more-200-affordable-apartments-new-rochelle (excerpt: Highgarden Tower, 219-unit affordable building completed). → §8 card, landmarks.

### Carrier / county fiber context
- `Westchester County broadband study fiber network county government Westchester 2023 2024` · Firecrawl →
  - https://www.intelligentcommunity.org/westchester_county_new_york (scrape, undated): Westchester Telecom Network, multi-gigabit backbone "over 800 miles … into every corner of the county"; county pooled budgets of 43 local governments, a library system, hospitals, school and water districts ($50M over five years) so Cablevision Lightpath built it; 3,500+ companies connected; more than half of municipal agencies; all schools, libraries and hospitals. → §5 para 4, facts, County Network section, Q&A village offices, Public Sector section, §10.5 H3 7.
  - https://doit.westchestercountyny.gov/images/stories/DoIT%20Annual%20Report%202023-2024%20WEB%20ADA.pdf (scrape): "expanded in 2001 when DoIT contracted with Cablevision Lightpath to build the countywide fiber-optic network known as the 'Westchester Telecom Network'"; county-negotiated pricing for municipalities. → same sections.
- `Optimum fiber Westchester towns available expansion Altice announcement` · Firecrawl → https://investors.optimum.com/news-events/press-releases/detail/202/optimum-reaches-500000-customers-on-100-fiber-internet (scrape, Nov 21 2024): 500,000 fiber customers; over 2.9 million homes passed across NY, NJ, CT; no Westchester mention. → County Network section.
- Hub source reused, not re-fetched: communitynetworks.org 2016 four-city gigabit compact — NOT used on this page (already on the HV hub).

### Storms / flooding
- `Hurricane Ida 2021 flooding Westchester Mamaroneck basements businesses damage` · Firecrawl → https://abc7ny.com/post/flooding-brooklyn-nj-nyc-flooded/10994078/ (Sept 2 2021, full excerpt): Mamaroneck "as much as 14 feet of water" in some neighbourhoods; 3 dead in Westchester County; basements filling, water rising to first floors; cars abandoned. → §5 facts, Storm and Flood section. https://www.townofmamaroneckny.gov/CivicSend/ViewMessage/message/153573 (excerpt, Sept 2021 newsletter) — background only.
- `Tropical Storm Isaias Westchester Con Edison customers without power 2020 Westchester` · Firecrawl → https://abc7ny.com/post/widespread-destruction-hundreds-of-thousands-still-in-the-dark/6345637/ (excerpt: "ConEd said 260,000 customers were left without power … throughout New York City and Westchester County"); https://www.lohud.com/story/weather/2020/08/12/eight-days-after-isaias-many-without-power-wednesday-morning-hudson-valley/3352805001/ (excerpt: "Eight days after … Con Edison still has 1,357 customers without power"). → Storm and Flood section.

### Landmarks / municipal structure
- `Westchester County Airport HPN terminal acres Harrison Purchase` · Firecrawl → https://en.wikipedia.org/wiki/Westchester_County_Airport (scrape): county-owned; North Castle, Harrison, Rye Brook; 702 acres; opened 1942; runways 16/34 6,549 ft and 11/29 4,451 ft; three-level terminal built 1995 ($35M), six gates; NY–CT border on eastern perimeter; ~33 miles north of Midtown. → landmarks card.
- `Purchase College SUNY campus acres buildings Anderson Hill Road` · Firecrawl → https://www.purchase.edu/about/our-campus/ (scrape: 500-acre former estate, Edward Larrabee Barnes); https://www.purchase.edu/ (excerpt: "only four-year SUNY in Westchester County … 735 Anderson Hill Road"). → landmarks card.
- `Ridge Hill Yonkers mixed-use square feet opened 2011 Cross County Parkway` · Firecrawl → https://maps.apple.com/place?place-id=I5370BAFC6F56FF0E (excerpt: "located between Interstate 87 and the Sprain Brook Parkway in Yonkers … grand opening in 2011"); https://en.wikipedia.org/wiki/Ridge_Hill_Mall (excerpt). → §8 Yonkers card.
- `Westchester County cities towns villages number ny.gov counties westchester population` · Firecrawl → https://www.ny.gov/counties/westchester (excerpt: 48 municipalities, White Plains county seat, population 990,817 (2023), full municipal list) → §5 facts, §8.5, Public Sector section, LocalBusiness areaServed list; https://en.wikipedia.org/wiki/Westchester_County,_New_York (excerpt: six cities, 19 towns, 23 villages; 450 sq mi; Yonkers 211,569 in 2020) → §5 facts, §8 Yonkers card.

### Licensing / permits / digging
- Hub sources reused (not re-fetched): https://consumer.westchestergov.com/trades/home-improvement-contractors ("Westchester law requires that home improvement contractors have a county license"; no low-voltage mention) → §8.5 county licensing callout. https://www.cenhud.com/en/my-energy/safety/dig-safely (811, at least two and no more than 10 days before digging) → §8.5, Campus Subdivision section.
- Westchester municipal building-department rules for low-voltage work: EMPTY (not researched per municipality; page says only that low-voltage work within a filed renovation follows that job's permit, and that each of the 48 municipalities has its own building department).
- Asbestos FAQ: no legal source fetched; the answer states only practice (stop and ask for the owner's survey), no legal claim.

### Local news on Westchester fiber-installation contractors 2026 — EMPTY (none retrieved).

### Pricing used (blueprint §9, Westchester 1.25×; same table as HV hub research)
$44 termination · $50 OTDR/strand · $438 MM drop · $500 SM drop · $5,625–$8,750 12-strand OM4 · $10,000–$18,750+ 24-strand OS2 · from $3,000 second room · starter $1,656 (24×$44 + 12×$50) · $195/hr 3-hr min ($585) protected. DISCREPANCY for review (already flagged by HV hub): structured-cabling-pricing-westchester-county configurator shows fiber drops at different figures; this page follows §9 as instructed.

### Images (11) — permanent image rule (Drive folder empty, CompanyCam not connected); every third file of `ls images/network` starting at position 1
| File (images/fiber-optic-installation/) | Source (images/network/, position) |
|---|---|
| fiber-optic-installation-westchester-county-port-labels-cable-map.webp | network-installation-bronx-cable-labeling-port-map.webp (1) |
| fiber-optic-installation-westchester-county-block-wall-drill-penetration.webp | network-installation-bronx-core-drill-cmu-wall-penetration.webp (4) |
| fiber-optic-installation-westchester-county-jhook-open-ceiling-pathway.webp | network-installation-bronx-jhook-ceiling-pathway-bundles.webp (7) |
| fiber-optic-installation-westchester-county-emt-conduit-riser-pull.webp | network-installation-bronx-network-drop-conduit-emt-riser.webp (10) |
| fiber-optic-installation-westchester-county-two-tech-corridor-pull.webp | network-installation-bronx-two-tech-corridor-cable-pull.webp (13) |
| fiber-optic-installation-westchester-county-closet-before-after.webp | network-installation-brooklyn-network-rack-cleanup-before-after.webp (25) |
| fiber-optic-installation-westchester-county-finished-rack-ups.webp | network-installation-dutchess-county-finished-network-rack-firewall-ups.webp (34) |
| fiber-optic-installation-westchester-county-corridor-bundle-lift.webp | network-installation-long-island-idf-riser-cable-bundle.webp (61) |
| fiber-optic-installation-westchester-county-ceiling-tile-cable-feed.webp | network-installation-westchester-county-ceiling-tile-cable-drop-occupied-office.webp (223) |
| fiber-optic-installation-westchester-county-certification-tester-wall-jack.webp | network-installation-westchester-county-fluke-dsx-certification-pass.webp (226) |
| fiber-optic-installation-westchester-county-tone-probe-panel-trace.webp | network-installation-westchester-county-network-cable-toner-tracing.webp (229) |
Note: all of these library photos show copper (Cat6 boxes, blue patch cable), not fiber; alts and captions describe only what is visible. Several look AI-generated (rendered logos and box text, "844-386-7238" printed on shirts) — same concern already logged for the LI page; for Anwar's review.

### Keyword plan (Westchester page)
Service: fiber optic installation Westchester County, multi-tenant fiber backbone, carrier demarc extension, conversion fiber, campus fiber, fusion splicing, OTDR testing, inherited fiber survey. Problem: single-tenant building re-let, old corporate data centre, telephone room full of old equipment, undocumented fiber, campus split into parcels, office-to-residential conversion, flooded basement telecom room, storm power loss. Technology: OS2, OM4, OFNR/OFNP, indoor/outdoor, armoured, lockable tenant enclosures, meet-me panel, innerduct. Industry: office landlords, property managers, developers, medical tenants, self-storage, municipalities, mixed-use towers. Geographic: Westchester, White Plains, Platinum Mile, Purchase, Harrison/West Harrison, Rye Brook, Elmsford, Tarrytown, Yonkers, Ridge Hill, Mount Vernon, New Rochelle, Mamaroneck, Port Chester, Ossining, Peekskill, Mount Kisco, Armonk, Somers, North Salem, Pound Ridge.

### Question register additions
fiber-optic-installation-westchester-county
§9 Questions Answered (and other question headings):
- Fiber Link Dead in a Westchester Building? — fiber-optic-installation-westchester-county
- We're re-letting a former corporate headquarters off I-287 floor by floor — should the landlord own the backbone, or should each tenant bring its own? — fiber-optic-installation-westchester-county
- The old corporate data centre in our building is being torn out — what happens to all the fiber that ran to it? — fiber-optic-installation-westchester-county
- Can tenants on different floors of one Westchester office building share a building-owned fiber backbone without sharing a network? — fiber-optic-installation-westchester-county
- The departed company's telephone room is still full of its old equipment — can it become the entrance room for our new tenants' carriers? — fiber-optic-installation-westchester-county
- Should the office-era fiber in a building being converted to apartments be reused, re-terminated or stripped out? — fiber-optic-installation-westchester-county
- Our office building is becoming self-storage — does it still need fiber, and where? — fiber-optic-installation-westchester-county
- When should a developer building under New Rochelle's downtown overlay bring in a fiber contractor? — fiber-optic-installation-westchester-county
- Our village offices connect to the county's Westchester Telecom Network — who is responsible for the fiber after the county's handoff? — fiber-optic-installation-westchester-county
- Our medical practice is moving into a suite in a Harrison or Purchase office park — what has to be in place before the clinical systems move? — fiber-optic-installation-westchester-county
- We're choosing between a downtown White Plains tower and an I-287 campus building — how does fiber change the comparison? — fiber-optic-installation-westchester-county
- Who owns the fiber after a building changes hands? (§10 EQUIPMENT table heading) — fiber-optic-installation-westchester-county
- Westchester Tenant Offline Right Now? (final repair heading) — fiber-optic-installation-westchester-county
§17 FAQ:
- Do you cover northern Westchester towns such as Somers, North Salem and Pound Ridge, or only the southern cities? — fiber-optic-installation-westchester-county
- When one tenant expands onto a neighbour's floor, can its strands in the shared backbone be reassigned? — fiber-optic-installation-westchester-county
- Can fiber work start while the outgoing corporate tenant is still moving out? — fiber-optic-installation-westchester-county
- Can you work in an older Yonkers or Mount Vernon building that has no drawings at all? — fiber-optic-installation-westchester-county
- Can fiber be run through the parking garage under an office or apartment building? — fiber-optic-installation-westchester-county
- How much notice do you need before a Westchester tenant's move-in date? — fiber-optic-installation-westchester-county
- Can one tenant lease its spare strands to another tenant in the same building? — fiber-optic-installation-westchester-county
- Will you meet our broker and a prospective tenant at the building to answer fiber questions? — fiber-optic-installation-westchester-county
- What happens if we find asbestos-containing material in the ceilings or risers of an older building? — fiber-optic-installation-westchester-county
- Who do we call if a Westchester fiber link fails outside business hours? — fiber-optic-installation-westchester-county
- Can you remove the old corporate cabling without disturbing the fiber we're keeping? — fiber-optic-installation-westchester-county
- Do you install fiber for a business run from a house in Westchester? — fiber-optic-installation-westchester-county

De-dup notes: checked against the register and the parallel Rockland/Orange drafts. Replaced this page's county-licence FAQ (Orange asks the same about its electrician licence), its COI, sale-documentation, phasing and spec-suite FAQs (Rockland covers those intents), and reworded two §9 questions to avoid Rockland's "strands of our own from a one-owner backbone" and Orange's "stop every provider drilling a new hole". Rockland's thesis (single-owner pharma/corporate campuses being split) overlaps this page's re-tenanting theme; Westchester's angle is downtown towers, conversions, the county network and office-market data. The main run should re-check meaning-level overlap after all three are final.

## Rockland — local research (2026-10-17 batch, fiber-optic-installation-rockland-county)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md are reused where noted; only Rockland research is added here. To be merged into research/fiber-optic-installation.md by the main run.

**Page thesis:** Rockland fiber work is inheritance work. The county's big commercial sites were built for one owner in the 1960s–70s growth years and are now being split, sold and converted (Hudson Valley iCampus from the Pfizer/Lederle site, Blue Hill Plaza's proposed partial residential conversion, Palisades Center's 2026 foreclosure sale, Nanuet Town Centre's apartments, Bradley Corporate Park and 108 Route 303 changing hands). The fiber inside them has to be found, tested, divided between owners and documented, and new links cross Orange & Rockland poles, county roads and the New Jersey line. Not a lightning/distance thesis (hub), not a riser thesis (Manhattan), not a warehouse thesis (Brooklyn/Orange).

### Reddit (local)
- Query: `reddit Rockland County internet fiber Fios Optimum Nanuet Pearl River` · Firecrawl web search (excerpts only; reddit.com threads not opened — Firecrawl does not scrape reddit).
  - https://www.reddit.com/r/Rockland/comments/1i0qwu0/optimum_vs_fios_in_rockland/ — excerpt: "Optimum - at least, in Nanuet - is a disaster. It's a DOCSIS 3.1 cable service, so the upload is asymmetric." → §10.5 H3 1 (quoted as one resident's opinion).
  - https://www.reddit.com/r/Rockland/comments/1ts3qhm/wifi_router_in_pearl_river/ — excerpt: "Fios vs Optimum is very town-dependent. I've had both for a few years each. In Pearl River Fios is better than Optimum…" → §5 para 4; §10.5 H3 1.
  - https://www.reddit.com/r/Rockland/comments/1ejr3em/optimum_fiber_outage/ — excerpt: "Is there a large optimum outage in Rockland? … I just got fiber yesterday and then it's out today" → §10.5 H3 1 (carrier fiber ≠ owner fiber; recorded as a resident post only).
  - https://www.reddit.com/r/Rockland/comments/1n447ip/nanuet_mall_rockland_county/ — excerpt: "Opened as an enclosed mall in 1969, it was redeveloped into an outdoor lifestyle center called 'The Shops at Nanuet', opening in 2013." → §8 Route 59 card (1969 stated as the poster's claim; 2013 corroborated by https://en.wikipedia.org/wiki/Nanuet_Town_Centre excerpt "Shops at Nanuet debuted in 2013").

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG — EMPTY (not accessible in build env)
Substitutes for §10.5 (claims quoted as published):
- Query: same Reddit query → https://ispreports.org/internet-service-providers-rockland-county-ny/ (search excerpt): "Optimum offers Fiber service to 91.5% of Rockland County homes." → §10.5 H3 1 (attributed to the comparison site, not stated as fact).
- Silo sources reused: unio.digital ($300–$800 per drop; aerial needs attachment rights) → §10.5 H3 3; newtechcabling.com ("Small projects can take a day or two") → §10.5 H3 5; lowvoltagenewyork.com (indoor $1–$6/ft) → §10.5 H3 4; thenetworkinstallers.com (FBA aerial median $8.00/ft) → §10.5 H3 3.
- Query: `OM1 62.5/125 multimode legacy fiber orange jacket bandwidth distance 10 gigabit 33 meters` · Firecrawl search → https://www.fs.com/blog/multimode-fiber-types-om1-vs-om2-vs-om3-vs-om4-vs-om5-1090.html (excerpt: OM1 62.5/125 µm, orange jacket, 10 GbE up to 33 m); https://www.truecable.com/blogs/cable-academy/guide-to-multimode-fiber-types (excerpt: "OM1 typically comes with an orange jacket · Core size of 62.5 micron · Supports 10 Gigabit Ethernet, but only up to 33 meters"). → §9 legacy-multimode question; §10.5 H3 2; §10 equipment.

### Yelp 1–3★ — EMPTY
- Query: `yelp network cabling fiber contractor Rockland County Nanuet Spring Valley reviews` · Firecrawl search → Yelp search-result pages only (e.g. https://www.yelp.com/search?find_desc=Telecommunications&find_loc=Spring+Valley%2C+NY+10977 — one "Cabling & Fiber Optic Wiring" listing at 51 Rockland Ctr, Nanuet, 4.0 from 1 review). No 1–3★ review text retrieved. Not used.

### County facts
- Query: `Rockland County five towns villages square miles population ny.gov` · Firecrawl search →
  - https://www.ny.gov/counties/rockland (excerpt): area 199 sq miles; established 1798; population 340,807 (2023); municipalities list (Clarkstown, Haverstraw, Orangetown, Ramapo, Stony Point and their villages; Spring Valley shared Clarkstown/Ramapo; Nyack shared Orangetown/Clarkstown; Pomona shared Ramapo/Haverstraw). → §5 facts, §13, FAQ coverage.
  - https://en.wikipedia.org/wiki/Rockland_County,_New_York (excerpt): land 173.55 sq mi; 2020 pop 338,329; census table 1950 89,276 → 1960 136,803 → 1970 229,903; Ramapo 148,919 (2020), Stony Point 14,655. → §5 para 1 (growth 1950–1970), §5 facts.
  - https://explorerocklandny.com/about/communities/ (excerpt): five towns, 19 incorporated villages, 16 hamlets. → §5 facts.

### Building stock, campuses, corridors (redevelopment thesis)
- Query: `Pfizer Pearl River campus sold redevelopment buildings acres` · Firecrawl search →
  - https://www.industrialrealtygroup.com/portfolio/icampus/ (scrape): Hudson Valley iCampus, Pearl River; ~2 million sq ft of laboratory, pharmaceutical manufacturing, office and support buildings; 200-acre campus; 20 miles north of Manhattan; Pfizer leased back ~1.26 million sq ft and will retain and operate 507,263 sq ft and 25 acres on the south side; future vision "mixed-use, multi-tenant campus". → §5 para 2, §5.5, thesis section, §8 card, §13 card.
  - https://www.lohud.com/story/news/local/rockland/2015/11/18/pfizer-sells-200-acres-pearl-river-campus/76005650/ (scrape, Nov 18 2015): Pfizer sold about 200 acres to Industrial Realty Group; 2 million sq ft and "about 38 buildings"; Pfizer retains about 25 acres including three buildings. → §5 para 2, thesis section.
  - https://hvicampus.com/meetings-underway-on-pfizer-470m-rockland-expansion/ (scrape, Aug 15 2022, reprinting Westchester & Fairfield County Business Journals): Pfizer in Rockland since acquiring Wyeth in 2009; 2015 sale of 207 acres and 25 buildings at 401 N. Middletown Road to IRG; Pfizer continues to own 33 acres, ~850,000 sq ft; $470M plan incl. new 260,000 sq ft lab building for 370 colleagues, "connected buildings". (Building/acre counts differ between sources; page attributes each figure to its source.) → §8 card, §13 card.
- Query: `Blue Hill Plaza Pearl River office complex square feet` · Firecrawl search →
  - https://en.wikipedia.org/wiki/Blue_Hill_Plaza (scrape): 21-storey tower + 8-storey building on 90 acres; nearly 1.2M sq ft; "about 40 percent of the office space leasing market in Rockland County" (citing Pearl River Patch, 2011); designed by Skidmore, Owings & Merrill; completed 1972; ~3,000 parking spaces; "fiber available from two central offices, entering two separate telephone equipment rooms"; on-site O&R substation; borders Bergen County NJ. (Article tagged as promotional in places — figures used are attributed.) → §5, §7 card, §8 card, §13 card, thesis.
  - https://rcbizjournal.com/2025/09/24/blue-hill-plaza-struggling-with-vacancies-proposes-partial-conversion-to-luxury-rental-apartments/ (search excerpt only; scrape failed — all engines blocked): "The proposal calls for changing 2 Blue Hill Plaza offices to 341 luxury units"; "two-building, 1.2 million square-foot office complex, situated on 90 acres along Route 304". → §5 para 2, §9 partial-conversion question, §13 card. Stated as a proposal.
- Query: `Palisades Center West Nyack Black Diamond foreclosure 2026 plans` · Firecrawl search → https://spinosoreg.com/resources/black-diamond-capital-management-palisades-center-long-term-ownership-operational-plans/ (excerpt, Feb 13 2026): Black Diamond funds plan to be long-term owners of the 2.3 million sq ft West Nyack property, operated by Spinoso; https://hudsonvalley.news12.com/2026/02/06/palisades-center-mall-foreclosure-auction-goes-for-175-million/5TQCf7BHIIywOsEqXQfQcj (excerpt): auction went for $175 million, no higher bids. → §5 facts, §8 card, §9 retail-handover question, §13 card.
- Query: `Shops at Nanuet former Nanuet Mall redevelopment opened 2013 Route 59` · Firecrawl search → https://www.lohud.com/story/news/local/rockland/2025/05/28/nanuet-town-centre-mall-could-add-280-apartments-in-rockland-county-new-york/83648817007/ (scrape, May 28 2025): new owners of Nanuet Town Centre (aka the Shops at Nanuet) embracing "live-work-play", adding apartments; outdoor mall along Route 59; Alexander Property Holdings. Apartment count only in URL slug — not used. → §8 Route 59 card.
- Query: `Orangeburg Route 303 industrial park warehouses Rockland Corporate Park Blauvelt Tappan` · Firecrawl search →
  - https://re-nj.com/onyx-angelo-gordon-acquire-1-2-million-sq-ft-industrial-park/ (scrape, May 9 2019): Bradley Corporate Park, 500 Bradley Hill Road, Blauvelt; 16 buildings across 180 acres; 1.2M sq ft; "about 90 percent occupied"; new owners "plan to upgrade the existing building infrastructure and lease up the current vacancies"; access to I-287, Thruway, Palisades Parkway, Route 303. → §8 card, §9 industrial-landlord question, §13 card.
  - https://rocklandnews.com/major-property-sales-drive-investment-across-rockland-county/ (scrape, July 8 2026): 54-acre industrial property at 108 Route 303, Tappan, bought by a PDI affiliate for ~$79M, associated with plans for a 337,000 sq ft industrial facility; Monsey Center (Route 59 & Saddle River Road) sold ~$10M; a Spring Valley strip center ~$2.9M; combined nearly $97M. → §5 facts, §8 cards, §9 strip-plaza question.
- Query: `Rockland Psychiatric Center Orangeburg campus redevelopment Orangetown acres buildings` · Firecrawl search → https://www.lohud.com/story/news/local/rockland/2017/02/02/rockland-psych-center-data-hub/97309060/ (scrape, Feb 2 2017): Orangetown Town Board considering selling 60 town-owned acres at the former Rockland Psychiatric Center to a not-yet-named data-center developer. Outcome not researched — stated only as a 2017 proposal. https://www.orangetown.com/wp-content/uploads/Chapter_2_Description_of_Proposed_Action.pdf (excerpt: rezoning ~97 acres of town-owned RPC land, 575 mostly age-restricted units) — undated, NOT used. → §8 Orangeburg card (2017 item only).
- Query: `Rockland Community College Suffern campus acres buildings Viola` · Firecrawl search → https://www.suny.edu/campuses/rockland/ (excerpt): 145 College Road, Suffern; 175-acre campus. → §13 card.
- Query: `Montefiore Nyack Hospital campus expansion building Route 9W Nyack` · Firecrawl search → https://montefiorenyackfoundation.org/the-transformation-project-building-the-future-of-care/ (scrape, Fall 2025 newsletter): multi-year Transformation Campaign; Phase III Reception Center incl. "Integrated Emergency Communication and Response Systems"; front door to welcome "more than 180,000 patients and visitors each year"; "130-year history". Facebook excerpt "$125 million capital transformation since 2017" — NOT used (social post only). → §7 healthcare card, §13 card.
- Query: `Nyack Main Street Broadway historic downtown buildings 19th century commercial district` · Firecrawl search → https://visitnyack.org/itinerary-historical-nyack/ (excerpt): "The Vanilla Factory is one of the earliest brick structures in Nyack, built in 1839". → §7 river-village card.

### Utility poles, county roads, state line
- Query: `Orange and Rockland Utilities pole attachment fiber third party attacher application` · Firecrawl search → https://www.oru.com/en/small-medium-sized-businesses/project-center/utility-pole-attachements-private-lighting (scrape): Joint Use Facilities handles projects "constructing a new communications line between buildings, installing security cameras, or running new fiber optics"; two License Agreements "for the appropriate state" (New York, New Jersey); Pole Attachment Survey Sheet, power supply, insurance certificates, tagging samples, application + pre/post-survey fees; fees: $350 initial agreement processing; make-ready labour $163.82/h overhead, $154.11/h underground; survey $8.40/pole pre-walk, $6.30/pole post-walk, $6.30 periodic inspection; attachment rate NY $26.55, NJ $12.96. → "Poles, Roads and the State Line" section, §10.5 H3 3, §9 NJ question.
- Same query → https://www.oru.com/en/community-affairs/community-issues/eruv (scrape): eruv attachments on O&R and Rockland Electric poles installed "consistent with practices used for all other pole attachments such as security cameras, Christmas lighting and private communication lines"; owned by the Rockland Eruv Association; rates filed with NYS PSC or NJ BPU. → poles section (context: poles already carry many private attachments).
- Query: `Rockland County Highway Department permit work within county right-of-way highway work permit utility` · Firecrawl search → https://www.rocklandcountyny.gov/departments/highway/permits-division (scrape): permits required for "Installing any utilities or other excavations within a County Road Right-of-Way"; permit types incl. "Road Work Utility Permit (Private)"; applications processed by permit technicians, reviewed by a Licensed Professional Engineer, approved by the Superintendent of Highways; "Typical Trench Restoration Detail" specification. → §9 county-road question, §8.5 callout, process step 3.
- Query: `Rockland County news 2026 fiber optic broadband installation Clarkstown Orangetown Ramapo` · Firecrawl search → https://www.rocklandcountyny.gov/departments/highway/highway-drainage-projects-construction/annual-paving (excerpt: 2026 Paving Program, e.g. Old Middletown Rd and Little Tor Rd in Clarkstown) → §9 county-road question (coordinate crossings with paving); https://documents.dps.ny.gov/public/Common/SearchResults.aspx?MC=1&CN=4135 (excerpt: 08/04/2026 petition of Cablevision of Rockland/Ramapo, LLC to renew its franchise with the Village of Chestnut Ridge) → §5 para 4 (cable franchises are granted municipality by municipality). Local news on fiber-installation contractors: EMPTY.
- Query: same county-permit query → https://www.dot.ny.gov/divisions/operating/oom/transportation-systems/traffic-operations-section/highway-permits (search excerpt only): "Who needs a highway work permit? Developers, utility companies, municipalities, residents, and others desiring to conduct activity within the right of way." → poles/roads section (state routes 59, 303, 9W). That those routes are state highways is stated from their NY route numbering, not from a fetched NYSDOT jurisdiction list — flag for review.
- New Jersey adjacency: Blue Hill Plaza Wikipedia (borders Bergen County; power from a Montvale NJ substation) and re-nj (Bradley Corporate Park "about six miles north of Bergen County"). → §9 NJ question, §8.

### Storm history
- Query: `Piermont Hurricane Sandy flooding storm surge businesses Rockland 2012` · Firecrawl search → https://rocklandtimes.com/2012/11/02/the-impact-of-hurricane-sandy/ (scrape, Nov 2 2012): O&R called Sandy "the worst storm in company history"; 230,000 outages vs Snowtober 134,000 and Irene 120,000; 80% of customers lost power; Piermont business district dark, basements pumped; Nyack closed streets to the riverfront; Stony Point Bar-Mar trailer park evacuated; Route 59 traffic lights out in Nanuet. → §5 facts, §7 river-village card, §9 (equipment placement in the empty-building question).
- Silo/hub source reused: Earth Networks 2020 NY lightning report (in research file, HV hub section): Rockland 64,575 pulses, 28 thunder days — lowest of the six HV counties. → §5 para 3 (why Rockland's problem is not mainly lightning).
- Query: `Rockland County Hurricane Ida 2021 flooding Spring Valley Suffern damage` · Firecrawl search → excerpts only (lohud live blog, ABC7 Facebook post on Spring Valley flash flooding). Not used (no fetched article). EMPTY.

### Local licensing / permits
- Query: `Rockland County home improvement license Chapter 250 low voltage electrician license requirement` · Firecrawl search → https://www.rocklandcountyny.gov/departments/consumer-protection-weights-measures/for-contractors/licenses-and-permits (scrape): Master Electrician Licence and Electrical Inspection Agency under Chapter 250 Articles I and II; Home Improvement Licence under Chapter 286 ("all individuals performing home improvement work must obtain a Home Improvement License"), three application types (experience, out-of-jurisdiction, surety bond); Chapter 286 version "Effective May 14, 2026"; renewals online only since April 2025. → §8.5 callout, FAQ licence/paperwork.
- https://ecode360.com/9665912 (Firecrawl query mode): Chapter 250 page returned no text on low-voltage / communications / fiber exemptions. → page makes NO claim that either county licence does or doesn't cover fiber; it tells owners to ask and says AESS confirms in writing which applies.
- https://www.businesslicenses.com/... (excerpt: lists "low voltage" among activities needing licences) — third-party aggregator, NOT used.

### Pricing used (existing AESS prices × blueprint §9 Rockland 1.30; same table as HV hub research)
$46/termination · $52/strand OTDR · $455 multimode drop · $520 single-mode drop · 12-strand OM4 backbone $5,850–$9,100 · 24-strand OS2 building-to-building $10,400–$19,500+ · second telecom room with fiber link from $3,120 · starter = 24 terminations + 12 OTDR = $1,728 · $195/hr, 3-hr minimum ($585) protected. DISCREPANCY (as noted in HV research): live structured-cabling-pricing-rockland-county configurator shows $453/$517 per drop; page follows blueprint §9.

### Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected
Taken only from `ls images/network` positions 2,5,8,11,… (every third from 2). Each viewed before use.
| File (images/fiber-optic-installation/) | Source (images/network/, position) |
|---|---|
| fiber-optic-installation-rockland-county-inherited-closet-before-after.webp | network-installation-bronx-network-rack-cleanup-before-after.webp (11) |
| fiber-optic-installation-rockland-county-finished-rack-firewall-ups.webp | network-installation-bronx-finished-network-rack-firewall-ups.webp (5) |
| fiber-optic-installation-rockland-county-switch-sfp-rack-mount.webp | network-installation-bronx-managed-poe-switch-rack-install.webp (8) |
| fiber-optic-installation-rockland-county-reel-boxes-fitout-staging.webp | network-installation-bronx-cat6-cable-box-staging-fitout.webp (2) |
| fiber-optic-installation-rockland-county-ceiling-access-point-office.webp | network-installation-bronx-wireless-access-point-ceiling-install.webp (14) |
| fiber-optic-installation-rockland-county-ceiling-tile-cable-feed.webp | network-installation-rockland-county-ceiling-tile-cable-drop-occupied-office.webp (164) |
| fiber-optic-installation-rockland-county-corridor-bundle-idf.webp | network-installation-rockland-county-idf-riser-cable-bundle.webp (167) |
| fiber-optic-installation-rockland-county-emt-conduit-block-wall.webp | network-installation-long-island-network-drop-conduit-emt-riser.webp (65) |
| fiber-optic-installation-rockland-county-patch-panel-punchdown.webp | network-installation-nyc-patch-panel-punchdown-rack.webp (113) |
| fiber-optic-installation-rockland-county-hammer-drill-block-wall.webp | network-installation-long-island-core-drill-cmu-wall-penetration.webp (59) |
| fiber-optic-installation-rockland-county-certification-tester-pass.webp | network-installation-dutchess-county-fluke-dsx-certification-pass.webp (35) |
Note for Anwar: every library photo shows a technician's face and an 844-386-7238 number on shirts/signs, and several show garbled box/label text typical of generated images (e.g. "H50 MHz", "TRUENET"). None shows fiber itself. Flagged for review; captions describe only what is visible and never claim a Rockland job.

### Keyword plan (Rockland page)
Service: fiber optic installation Rockland County, campus fiber, fiber re-termination, fiber audit/inventory, fusion splicing, OTDR testing, building-to-building fiber, fiber documentation. Problem: inherited/unmapped fiber, campus split between owners, partial office-to-residential conversion, empty buildings brought back, legacy OM1 multimode, county-road crossing, NJ state line, pole attachment paperwork, retail centre ownership change. Technology: OS2, OM4, OM1 legacy, MPO, splice enclosures, locking trays, OTDR, light source/power meter, armored, indoor/outdoor. Industry: research/pharma campuses, suburban office towers, malls and strip plazas, flex/industrial parks, hospitals, colleges, schools and congregations on adjoining lots, river-village storefronts. Geographic: Rockland County, Clarkstown, Orangetown, Ramapo, Haverstraw, Stony Point, Pearl River, Orangeburg, Blauvelt, Tappan, Nanuet, West Nyack, Nyack, Piermont, Spring Valley, Monsey, Suffern, New City, Route 59, Route 303, Route 304, Veterans Memorial Drive.

### Question register additions
fiber-optic-installation-rockland-county
§9 Questions Answered:
- On our Pearl River campus the main fiber room is inside a building leased to another company — what happens when our strands need work there? — fiber-optic-installation-rockland-county
- Part of our Rockland office complex is being turned into apartments — how do we keep the offices' fiber out of the residential building? — fiber-optic-installation-rockland-county
- Nobody can tell us where the fiber on our newly bought Rockland property runs — how do you trace it from end to end? — fiber-optic-installation-rockland-county
- The seller kept one building on our campus and still rides the same fiber — how do we separate the two networks without cutting them off? — fiber-optic-installation-rockland-county
- Our two buildings face each other across a county road — what does it take to get private fiber from one side to the other? — fiber-optic-installation-rockland-county
- We have one site in Rockland and another a few miles over the line in Bergen County — can a single private fiber link serve both? — fiber-optic-installation-rockland-county
- Our building sat half-empty for years — is the fiber that was left in it still usable? — fiber-optic-installation-rockland-county
- Our inherited backbone is orange-jacketed multimode from decades ago — can it carry today's network? — fiber-optic-installation-rockland-county
- The parking-lot cameras at our Route 59 plaza ride on fiber that runs through a tenant's unit — how do we take them back? — fiber-optic-installation-rockland-county
- Between tenants in our Blauvelt or Orangeburg industrial building, what fiber should we leave in place for the next one? — fiber-optic-installation-rockland-county
- Our school or congregation uses neighbouring houses in Ramapo that belong to different owners — what agreement does a fiber link between them need? — fiber-optic-installation-rockland-county
- Our offices sit on both sides of the Hudson — can our own fiber cross between Rockland and Westchester? — fiber-optic-installation-rockland-county
- The shopping centre where we lease is being sold — what happens to our fiber and our carrier's fiber during the handover? — fiber-optic-installation-rockland-county
§17 FAQ:
- Which parts of Rockland do you cover — every town, the river villages and Monsey? — fiber-optic-installation-rockland-county
- Can you test the fiber a seller says is included before we close on a Rockland building? — fiber-optic-installation-rockland-county
- Will you document and label an existing Rockland fiber plant without installing anything new? — fiber-optic-installation-rockland-county
- What licence and insurance paperwork can you hand a Rockland property manager before work starts? — fiber-optic-installation-rockland-county
- Can fiber work be done inside the lab and manufacturing buildings on Rockland's research campuses? — fiber-optic-installation-rockland-county
- What does it cost to have an inherited fiber plant tested and mapped in Rockland? — fiber-optic-installation-rockland-county
- How do you handle parking and deliveries in Nyack, Piermont and the other river villages? — fiber-optic-installation-rockland-county
- How is the cost of shared fiber divided when a Rockland campus has several owners? — fiber-optic-installation-rockland-county
- Can you supply fiber routing drawings for an Orangetown or Clarkstown site-plan application? — fiber-optic-installation-rockland-county
- Can a construction trailer or sales office on a Rockland redevelopment site get a temporary fiber link? — fiber-optic-installation-rockland-county
- Can the work start with one building on a split campus and reach the others later? — fiber-optic-installation-rockland-county
- Can our own consultant witness the acceptance tests on a Rockland fiber job? — fiber-optic-installation-rockland-county

De-dup notes: no question on pole attachment permission (LI §9 covers it — O&R process is in a body section instead), flooding/cellar placement (Manhattan/Brooklyn), removal of a previous tenant's fiber (Manhattan), property managers with several parks (LI), working nights/weekends (NYC), coordinating with the ISP (Brooklyn), conversion planning from scratch (Manhattan — this page's conversion question is about separating two uses inside a partly converted complex), area pricing (LI/Manhattan — explained in body only). After reading the parallel Westchester and Orange drafts: reframed the campus-tenant question (Orange has 'own fiber in a former hospital without the landlord's network') to access to a main room inside another tenant's building; reframed the plaza question (Orange has 'stop every provider drilling') to taking landlord cameras back from a tenant's path; reframed the adjoining-houses question (Orange has 'two adjoining buildings share a party wall') to the cross-owner agreement; sharpened the unmapped-fiber question (Westchester has 'building with no drawings') to tracing method.

## Orange — local research (2026-10-17 batch, fiber-optic-installation-orange-county)

Area page; up = /fiber-optic-installation-hudson-valley; phone (845) 640-3835 (800 only in shared header); GBP Bronx (#bronx, 460 E Fordham Rd). Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts only unless scraped); "FC scrape" = mcp__Firecrawl__firecrawl_scrape; "WS" = WebSearch; "WF" = WebFetch. Silo-wide sources already in research/fiber-optic-installation.md are reused where noted and not repeated.

**Thesis (distinct from the HV hub's scattered-outbuildings / lightning / warehouse-belt thesis):** Orange County is a county of main streets — 3 cities and 20 villages with 19th-century mixed-use cores, plus reused institutional buildings, civic clusters and Route 17 retail/hospitality. New provider fiber is arriving village by village (Greenlight 2023→2026) and stops at the outside wall; the owner-side job is one planned shared entrance + enclosure per multi-tenant building, tenant extensions through common areas, civic links between a village's own buildings, and backbones in reused schools/hospitals/mills. Hub topics deliberately avoided: lightning/ground potential, barns/outbuildings, Stewart/Montgomery warehouses, grant-funded provider arrival.

### 1. Reddit
- `reddit Newburgh OR Middletown OR "Orange County NY" fiber internet Greenlight Spectrum business` · FC search → no Orange County NY reddit thread returned (r/Rochester Greenlight threads, and https://www.reddit.com/r/orangecounty/comments/1elllat/… which is very likely Orange County, **California** — not used). Local Reddit on fiber: **EMPTY**.
- Substitute local social source, same query → https://www.facebook.com/groups/717097027718808/posts/1022228077205700/ (FC search excerpt, Newburgh group post "What is the contact information for Newburgh's internet provider…"): "Bringing the fiber optic cable inside your home and setting up the electronics and wiring necessary to provide a WiFi (wireless) signal" → §5 THE NEIGHBORHOOD para after facts list (quoted as a group reply excerpt).
- Prior AESS research (research/soundbar-installation.md, Orange section): r/hudsonvalley "what is the deal with orange county" newcomer thread — background only, not used.

### 2–5, 8, 11. PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
- Angi / HomeAdvisor / Fixr fiber-installation pages: EMPTY (silo searches returned none; stated on page in §10.5 intro).
- Yelp: the FC search above returned only a Yelp Orange County **CA** listing — not used. EMPTY.
- §10.5 substitutes (claims quoted as published):
  - `fiber optic installation Orange County NY Newburgh Middletown contractor cabling` · FC search → https://fischsolutions.com/solutions/structured-wiring/ (FC scrape; competitor HQ 3188 Route 9W, New Windsor; page published 2026-05-12): "Low-voltage cabling under 50 volts typically does not require an electrical permit in Hudson Valley municipalities"; "For most single-floor Hudson Valley offices under 30,000 square feet, Cat6A copper is enough"; OS2 "cost per meter is similar to multi-mode"; "A 30-drop office fit-out in Orange or Dutchess County usually takes 2-4 days". → §10.5 H3 1, 2, 5, 7 (attributed as "a structured-wiring firm based in New Windsor", not named).
  - Silo sources reused: streamlinetelecom "$1-6 per linear foot" → H3 3; unio.digital "$300 to $800 per fiber drop" / "orientation ranges, not quotes" → H3 4; lowvoltagenewyork (SM glass cheaper than OM4; SM optics ~1.5–5×) → H3 5; T-Mobile "up to 4 hours", AT&T "four to six hours" → H3 6.

### 6/7. Landmarks, building stock, corridors
- `Orange County NY cities towns villages number ny.gov counties orange` · WS → https://citypopulation.de/en/usa/places/newyork/36071__orange/ (WF): 3 cities — Middletown 30,348, Newburgh 28,863, Port Jervis 8,763 (2020); 20 villages; 17 CDPs; county 401,312 (2020). → §5 para 1, §5.5 facts.
- `Orange County New York "20 towns" "3 cities" villages county government` · WS → https://en.wikipedia.org/wiki/Orange_County,_New_York (WF): county seat Goshen; 401,310 (2020); 840 sq mi total; I-84, I-87, NY 17 "Future Interstate 86"; only NY county bordering both NJ and PA; SUNY Orange (Middletown), Mount Saint Mary College (Newburgh), Touro COM (Middletown); town count not given (historic "20 town supervisors" only — page does NOT state a town count). → §5.5 facts, town-by-town intro ("roughly 840 square miles").
- `Newburgh East End Historic District number of buildings largest historic district New York` · WS → https://en.wikipedia.org/wiki/East_End_Historic_District_(Newburgh,_New_York) (WF): 445 acres; 2,217 buildings (article also says 2,239 resources — inconsistent, page uses "more than 2,200"); with Montgomery-Grand-Liberty ~4,000 contributing properties; city recognised 1973; NRHP 1985; Italianate 2–3-storey brick townhouses, Second Empire, Gothic Revival; commercial on Liberty Street, Broadway, William Street. → §5 para 4, §5.5, §7 card 2, §8 Newburgh card, §13 card 1, town-by-town.
- `Orange County Government Center Goshen Paul Rudolph renovation reopened new building square feet` · WS → https://en.wikipedia.org/wiki/Orange_County_Government_Center (WF): Rudolph, designed 1963, completed 1967; Irene 2011 flood damage, closed; centre section demolished by Dec 2015; renovated, reopened 2017. → §5 para 4, §13 card 2.
- `Touro College of Osteopathic Medicine Middletown campus former Middletown Psychiatric Center building` · WS → https://blog.randrealty.com/2014/09/touro-medical-college-opens-their-new-horton-campus-in-middletown/ (WF, dated Sept 8 2014): Horton Campus = former Horton Hospital; complex 375,000 SF (200,000+ special-purpose); 135 incoming students; opening Aug 31 2014. → §5 para 4, §7 card 3, §8 Middletown card, §13 card 3.
- `SUNY Orange Newburgh campus Kaplan Hall former Masonic building Newburgh renovation` · WS → https://en.wikipedia.org/wiki/SUNY_Orange (WF): Middletown campus 37 acres, 12 buildings, former Webb Horton House property; Newburgh campus two buildings on the Hudson. → §13 "we also work in".
- `LEGOLAND New York Goshen opened 2021 acres` · WS → https://en.wikipedia.org/wiki/Legoland_New_York (WF): Goshen; opened May/July 2021; ~150 acres themed within 500-acre property; 250-room hotel (Aug 2021); NY 17 exit 125 ramp moved ~4,000 ft, built to Interstate standards, $40M ($10M state, $30M Merlin); DEC fine $346,000 (not used). → §13 card 5, §7 card 5, §8 Goshen card.
- `Woodbury Common Premium Outlets number of stores Central Valley NY` · WS → https://en.wikipedia.org/wiki/Woodbury_Common_Premium_Outlets (WF): Central Valley section of Woodbury; opened 1985; 220 stores; 845,000 sq ft; "one of the largest contiguous outlet centers in the world"; Simon. → §5.5, §13 card 4, §8 card 4.
- Port Jervis: https://en.wikipedia.org/wiki/Port_Jervis,_New_York (WF; URL reached from the county article): Tri-States Monument 1882 under I-84 viaduct; Delaware at Neversink confluence; Erie Railroad division centre; Front Street small businesses; Pike Street (youth centre); pop. 8,775 (2020). → §5.5, §8 Port Jervis card, §13 card 6, town-by-town.
- Port Jervis Line (FAQ 5): prior AESS research (research/soundbar-installation.md Orange section, https://en.wikipedia.org/wiki/Port_Jervis_Line) — line exists and runs through Orange County; not re-fetched. FAQ answer is technical (fiber immune to EMI), no local statistic.
- `Route 17 Interstate 86 conversion Orange County NYSDOT 2025 2026 project Harriman Middletown` · WS → https://hgar.com/gov-hochul-earmarks-up-to-1-billion-for-route-17-expansion (WF, Apr 18 2022): up to $1B; third lane Exit 131 Harriman → Exit 103 Monticello; greatest need Exits 120 (NY 211, Wallkill) to 131 (Woodbury), ~22 miles; conversion to I-86. → §5.5, §9 Route 17 third-lane Q, Route 17 retail section.
- Galleria at Crystal Run (Town of Wallkill): named in the Greenlight July 2025 release below. → §8 Middletown card, town-by-town.

### 9/10. Local news / hyperlocal (fiber providers)
- `Greenlight Networks Orange County New York 2026 expansion Newburgh Monroe Warwick fiber` · FC search; FC scrape https://www.greenlightnetworks.com/greenlight-networks-fuels-regional-growth-with-continued-expansion-across-orange-county/ (July 24 2025, provider press release): began building in region 2023; $4M Port Jervis build (downtown first; network equipment hosted by City of Port Jervis Police Department); construction in Goshen, Middletown, Wallkill; $24M+ to reach additional 16,200 homes in 12 months; Village of Goshen >1,000 homes connected; Middletown 6,000 homes in 12 months; Wallkill hamlets Circleville and Mechanicstown; Orange County Fair Speedway 8-gig business service; Galleria at Crystal Run. → §5 para 2, §8 Port Jervis card, §9 civic-link Q, town-by-town (Middletown, Goshen, Port Jervis).
- FC scrape https://www.greenlightnetworks.com/greenlight-networks-expands-to-highland-falls-bringing-100-fiber-internet-to-thousands-more-local-homes-and-businesses/ (June 11 2026): Highland Falls build >$2M; >$26M invested in Orange County to date; $3.4M Village of Walden; Washingtonville under construction. → §5 para 2, §5.5, town-by-town (Walden, Highland Falls).
- `Greenlight Walden Washingtonville fiber construction 2026 village` · FC search → https://www.greenlightnetworks.com/faster-more-reliable-fiber-internet-arrives-in-walden-as-greenlight-networks-continues-orange-county-expansion-construction-underway-in-washingtonville/ (excerpt: "Construction in Washingtonville is currently underway, with plans to connect nearly 2,300 homes by the end of 2026") → recorded; page only says construction was under way (number not used).
- `Orange County New York broadband fiber network county government 2025 2026` · WS → results were Orange County **Virginia** (REC partnership) — not used. Orange County NY government fiber network: EMPTY.
- `Orange County NY data center proposal 2025 2026 town fiber` · WS → results are Orangetown (Rockland) / Orange County NC — not used. EMPTY for Orange County NY.
- Times Herald-Record / Mid-Hudson News / News12 Hudson Valley on fiber installation contractors: EMPTY (none retrieved).

### Local licensing / permits
- `Newburgh Architectural Review Commission certificate of appropriateness East End historic district exterior changes` · FC search → https://ecode360.com/30538879 (City of Newburgh Code Art. VI Historic Overlay District, excerpt): "No person shall carry out any exterior alteration, restoration, reconstruction, demolition, new construction, or move of a designated historic landmark or property within a designated historic district without first obtaining a certificate of appropriateness… from the City of Newburgh ARC"; https://www.cityofnewburgh-ny.gov/267/Architectural-Review-Commission (excerpt: ARC empowered by City Code §300-38). → §7 card 2, §8.5 callout 1, §9 facade-terminal Q, §10.5 H3 1, town-by-town.
- `orangecountyny.gov electrician license county-issued license requirement Electrical Licensing Board exemption low voltage` · FC search → https://www.orangecountyny.gov/DocumentCenter/View/317/Electrician-Application-PDF (excerpt: "According to Local Law No. 8 of 2007, any person wishing to work as an electrician in Orange County must possess a county-issued license"); https://www.orangecountyny.gov/DocumentCenter/View/311/Local-Law-No-1-of-2024-Electrical-Licensing-PDF (excerpt). → §8.5 callout 2, §9 licence Q, FAQ 11, §10.5 H3 1. Page does NOT claim the county licence exempts or covers low-voltage work explicitly; it says fiber is low-voltage under the NYS licence and outlets are done by a licensed electrician.
- Orange County home-improvement contractor licence: NOT verified (see soundbar research flag) — page makes no claim.
- 811 / Dig Safely (2–10 working days): silo HV source https://www.cenhud.com/en/my-energy/safety/dig-safely reused → §8.5 callout 5. (Orange & Rockland Utilities' own page not fetched.)
- NEC 770 listings OFNR/OFNP: silo source (cablinginstall) reused → §8.5 callout 4, Equipment.

### Pricing used (blueprint §9 Orange 1.40× on silo base; no new prices)
$35→$49 termination; $40→$56 OTDR/strand; $350→$490 MM drop; $400→$560 SM drop; $4,500–$7,000→$6,300–$9,800; $8,000–$15,000+→$11,200–$21,000+; $2,400→from $3,360; Starter 24×$49 + 12×$56 = $1,848; $195/hr 3-hr min ($585) unchanged. (Same as HV hub table. Live structured-cabling-pricing-orange-county configurator shows $494/$564 drops — discrepancy already flagged by the hub builder.)

### Images (11) — permanent image rule (Drive folder empty, CompanyCam not connected)
Source = `ls images/network`, positions that are multiples of 3 only. All viewed before use.
| File (images/fiber-optic-installation/) | Source (position) |
|---|---|
| fiber-optic-installation-orange-county-finished-rack-yellow-jumpers.webp | network-installation-orange-county-finished-network-rack-firewall-ups.webp (123) |
| fiber-optic-installation-orange-county-core-drill-block-wall-sleeve.webp | network-installation-nyc-core-drill-cmu-wall-penetration.webp (102) |
| fiber-optic-installation-orange-county-emt-conduit-sweep-pull.webp | network-installation-queens-network-drop-conduit-emt-riser.webp (156) |
| fiber-optic-installation-orange-county-two-tech-hallway-cable-pull.webp | network-installation-queens-two-tech-corridor-cable-pull.webp (159) |
| fiber-optic-installation-orange-county-ceiling-tile-cable-feed-ladder.webp | network-installation-bronx-ceiling-tile-cable-drop-occupied-office.webp (3) |
| fiber-optic-installation-orange-county-toner-probe-panel-trace.webp | network-installation-nassau-county-network-cable-toner-tracing.webp (93) |
| fiber-optic-installation-orange-county-switch-mounting-rack.webp | network-installation-westchester-county-managed-poe-switch-rack-install.webp (228) |
| fiber-optic-installation-orange-county-certification-tester-pass-screen.webp | network-installation-nassau-county-fluke-dsx-certification-pass.webp (90) |
| fiber-optic-installation-orange-county-jhook-pathway-open-ceiling.webp | network-installation-orange-county-jhook-ceiling-pathway-bundles.webp (126) |
| fiber-optic-installation-orange-county-closet-before-after-cleanup.webp | network-installation-orange-county-network-rack-cleanup-before-after.webp (129) |
| fiber-optic-installation-orange-county-patch-label-cable-map.webp | network-installation-rockland-county-cable-labeling-port-map.webp (162) |
Note for Anwar: the network library holds only 16 distinct scenes (same photo under many area names), so Westchester/Rockland siblings necessarily show the same scenes from different files. These photos show copper/Cat6 work (alt/captions say so implicitly — no claim of fiber in frame), show technicians' faces and an 844-386-7238 shirt number, and look AI-generated (garbled box text) — same concern as the LI builder raised. DAILY-LOG note: `images: 11 reused from images/network/ (no real fiber-optic-installation photos yet)`.

### Keyword plan (Orange County page)
Service: fiber optic installation Orange County NY, shared building entrance, tenant fiber extension, civic/municipal fiber link, fusion splicing, OTDR testing. Problem: every provider drilling its own hole, terminal on historic facade, rack in attic, party-wall buildings, old institutional pathways, landlord's legacy network, long retail rows over 100 m, leased lines between village buildings. Technology: OS2, OM4, indoor/outdoor, riser/plenum, armoured, wall-mount enclosure, LC/SC, SFP/media converter, sleeves/raceway/conduit. Industry: mixed-use main-street buildings, historic rowhouses, reused schools/hospitals/mills, village halls/police/firehouses, retail/outlets, restaurants, hotels, banks, medical. Geographic: Orange County; Newburgh (East End, Liberty St, Broadway), Middletown, Wallkill (Galleria at Crystal Run, Circleville, Mechanicstown), Goshen, Central Valley/Woodbury, Monroe, Harriman, Chester, Warwick, Greenwood Lake, Florida, Walden, Montgomery, Maybrook, Washingtonville, Cornwall, New Windsor, Highland Falls, Port Jervis, Deerpark, Otisville, Mount Hope; Route 17 / I-86, Route 211.

### Question register additions
fiber-optic-installation-orange-county
§9 Questions Answered (and other question headings):
- Shop or Office Link Dead on an Orange County Main Street? (repair capture heading) — fiber-optic-installation-orange-county
- Each tenant in our Newburgh building orders internet on its own — how do we stop every provider from drilling a new hole through the brick? — fiber-optic-installation-orange-county
- The only place for a rack in our Front Street building is the attic — is that a bad idea for fiber equipment? — fiber-optic-installation-orange-county
- We own two adjoining buildings on a village main street that share a party wall — can one network serve both? — fiber-optic-installation-orange-county
- The provider wants to mount its terminal on our storefront facade — can we ask for it somewhere else? — fiber-optic-installation-orange-county
- Our building used to be a church school — are the old intercom and telephone pathways in its walls usable for fiber? — fiber-optic-installation-orange-county
- Our practice moved into part of a large former hospital building — can we get fiber to our suite without depending on the landlord's old network? — fiber-optic-installation-orange-county
- Our restaurant near a Route 17 interchange is adding a second building on the lot — should it get its own internet service or a fiber link from the first? — fiber-optic-installation-orange-county
- The state plans a third lane on Route 17 — should a business near the highway hold off on buried fiber until the road work is done? — fiber-optic-installation-orange-county
- Our village hall, police desk and highway garage are in separate buildings — can fiber replace the leased lines between them? — fiber-optic-installation-orange-county
- Can fiber keep our firehouse's alerting equipment and cameras separate from the members' Wi-Fi? — fiber-optic-installation-orange-county
- Does Orange County's electrician licence apply to the people installing our fiber? — fiber-optic-installation-orange-county
- Our property in Warwick is a long drive from your Bronx office — how do you keep the job from stretching into extra trips? — fiber-optic-installation-orange-county
- Will a busy Newburgh or Middletown sidewalk have to be closed while the fiber comes in? — fiber-optic-installation-orange-county
§17 FAQ:
- Do you take fiber work in western Orange County — Port Jervis, Otisville and the Deerpark side? — fiber-optic-installation-orange-county
- What should we send so a quote can come back before anyone visits the building? — fiber-optic-installation-orange-county
- Is fiber worth adding to a building we might sell in a few years? — fiber-optic-installation-orange-county
- Can fiber reach a second-floor office over a storefront without running through the shop? — fiber-optic-installation-orange-county
- Will trains on the Port Jervis Line next to our building disturb a fiber link? — fiber-optic-installation-orange-county
- Can fiber be added to a hotel or motel along Route 17 without taking rooms out of service? — fiber-optic-installation-orange-county
- Do outlet-center and shopping-plaza leases usually let a tenant hire its own fiber installer? — fiber-optic-installation-orange-county
- Can new fiber sit alongside an older alarm or fire-alarm panel in the same closet? — fiber-optic-installation-orange-county
- Our landlord lives outside New York — how do approvals work when the owner can't come to the building? — fiber-optic-installation-orange-county
- Do tenants have to be home when fiber is run through an occupied apartment in a two- or three-family house? — fiber-optic-installation-orange-county
- Does each end of a fiber link need a dedicated electrical outlet? — fiber-optic-installation-orange-county
- Can you install fiber in a bank branch or credit union on a village main street? — fiber-optic-installation-orange-county

De-dup notes: checked by meaning against the full register (NYC, Manhattan, Brooklyn, Long Island, Hudson Valley) and the Westchester/Rockland pages on disk at 07:56. Removed during the build: a shared-entrance cost-split Q&A and a "quote broken out per owner" FAQ (overlapped Rockland's "How is the cost of shared fiber divided when a Rockland campus has several owners?"); cost split now appears only as body text in the ownership subsection. Avoided by design: coverage of historic/landmark districts as a question (Manhattan owns it — ARC covered in body/callouts), provider-arrival prep (HV), carrier landing at the wrong end (LI), building permits (NYC), area price difference (LI), flood (Brooklyn/Manhattan), timing/cutover (NYC). Partial-overlap notes for the main run: my firehouse strand-separation Q vs Westchester "tenants sharing a building backbone without sharing a network" (different parties: one organisation's systems vs separate tenants); my former-hospital suite Q vs Westchester office-park medical-suite Q (independence from landlord network vs move-in readiness).

## Staten Island — local research (2026-10-17 batch, fiber-optic-installation-staten-island)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md are reused where noted; only Staten Island research is added here. Page thesis: Staten Island is the city's low-rise, overhead-wired borough — detached and two-family houses, strip retail, west-shore logistics and campus-style institutions — so fiber jobs here are mostly short private links between separate structures on one lot, aerial-versus-buried decisions, flood-elevated houses, and ground that can be protected (Special Natural Area District) or shared (driveways, strip centres), rather than risers.

### Reddit (local)
- Query: `reddit statenisland fiber internet Fios building wiring` · WebSearch → no reddit.com results returned (ISP-comparison pages and Verizon community forum only). r/statenisland: EMPTY.
- Query: `reddit r/statenisland fiber internet house ethernet basement Fios Spectrum` · Firecrawl web search (excerpts only) → no r/statenisland threads; r/Fios excerpts not Staten Island-specific:
  - https://www.reddit.com/r/Fios/comments/pzhs03/renovating_a_basement_with_ethernetfios/ — excerpt: "Renovating a basement, all open foundation currently. Is a Verizon Fios rep need to be called in or an electrician is sufficient." → not quoted; background for §9 elevated-house question (who places equipment where).
  - https://www.reddit.com/r/Fios/comments/1ojj61o/ethernet_to_basement/ — excerpt: "Install router in basement via Ethernet port from ONT. WiFi will be much better throughout home." → background only, not quoted.
  - Same search → https://www.allconnect.com/local/ny/staten-island (excerpt): "The fastest internet option in Staten Island is Verizon Fios, which offers fiber speeds up to 5,300 Mbps for $100.00/mo." → §10.5 H3 6 (quoted claim). https://broadbandnow.com/New-York/Staten-Island (excerpt): Fios "downloads up to 2 Gbps for $49.99 per month" → not used. https://www.spectrum.com/locations/internet-wifi-service/staten-island-ny-i325 (excerpt) "Spectrum Fiber-Powered Internet in Staten Island" → §5 para 4 (both national providers advertise service; owner-side wiring still needed); FAQ coax question.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitutes for the §10.5 reality check — claims quoted from published cost guides/listings (each quoted as published):
- Query: `fiber optic installation Staten Island contractor cost` · Firecrawl web search (excerpts):
  - https://ringandping.com/how-much-does-fiber-optic-cable-installation-cost-in-2026/ — "Residential projects typically range from $1,500 to $6,000, while commercial fiber optic cabling services can scale into six figures for complex builds." → §10.5 H3 1.
  - https://www.gokinetic.com/blog/fiber-internet-cost-guide — "new fiber installation can cost anywhere from $1,500 to $7000" … "activation fee of roughly $99" → §10.5 H3 2 (consumer ISP connection cost confused with private cabling).
  - https://www.reddit.com/r/FiberOptics/comments/v43z6d/study_of_costs_of_aerial_fiber_optic_installs/ — "a typical install will be around $30K per mile for overlash" (commenter opinion) → §10.5 H3 4 (quoted as a forum comment).
  - https://www.quora.com/How-much-would-it-cost-to-install-fiber-at-a-residential-address — "The cost to install a fiber optic network in an apartment building typically ranges from $500 to $1,500 per unit" → §10.5 H3 7 (quoted as a Q&A-site answer).
  - https://www.abstractenterprisessecuritysystems.com/structured-cabling-installation-staten-island (own site) — not used as a claim.
  - https://www.facebook.com/groups/canandaiguachronicles/... (upstate Facebook group, Spectrum drop length anecdote) → not used (not local, anecdote).
- Silo source reused: thenetworkinstallers.com (FBA 2025: aerial median $8.00/ft, underground $18.00/ft) → §10.5 H3 3.
- Silo source reused: Verizon NYC fiber page (https://espanol2.verizon.com/about/node/141763), premises passed at end of 2013, "Staten Island virtually all" → §5.5 facts, §10.5 H3 5.
- Yelp 1–3★ for Staten Island fiber/cabling contractors: no yelp.com result in any query. EMPTY.

### Utility lines / storms (local data)
- Query: `Staten Island overhead utility poles telephone cable aerial lines more than other boroughs` · WebSearch → https://www.nyc.gov/html/planyc2030/downloads/pdf/power_lines_study_2013.pdf (WebFetch): Mayor's Office of Long-Term Planning and Sustainability, "Utilization of Underground and Overhead Power Lines in the City of New York", December 2013, Table 1: Staten Island 7,140 miles of overhead wire, 72% of installed wire overhead (Bronx 20%, Brooklyn 12%, Queens 22%, Manhattan 0%). → §5 para 2, §5.5 facts, aerial-vs-buried section, §10.5 H3 3/4, landmark intro.
- Same query → https://www.cbsnews.com/newyork/news/staten-island-residents-frustrated-with-new-utility-pole-placement/ (WebFetch, Apr 9 2014): Con Edison pole placed mid-sidewalk in Grymes Hill/West Fingerboard Rd area — NOT used (not relevant to private fiber).
- Query: `Tropical Storm Isaias Con Edison Staten Island customers lost power 2020 overhead` · WebSearch → https://coned.com/about-us/media-center/news/2020/08-04/storm-isaias-outage-is-second-largest-in-con-edisons-long-history (WebFetch): 257,000 customers out, "second largest" in Con Edison's history; 29,000 on Staten Island; damage to the "overhead electric-delivery system", trees and branches brought down lines; Sandy + following nor'easter record 1.1 million. → §5.5 facts, aerial-vs-buried section.

### Flooding
- Query: `Hurricane Sandy Staten Island deaths Midland Beach Oakwood Beach flooding homes damaged statistics` · WebSearch → https://www.nyc.gov/site/sirr/rebuilding/east-and-south-shore-staten-island.page (WebFetch, NYC SIRR): 23 storm-related deaths on Staten Island, all but one on the East and South Shores; more than 11,700 buildings in areas that experienced inundation; Hylan Boulevard and Oakwood Beach WWTP named as affected assets. No neighbourhood list, no flood height. → §5 para 3, §5.5, flood/elevated-house section, §9 elevated-house question.

### Land use / natural areas / permits
- Query: `Special Natural Area District Staten Island excavation restrictions trees rock outcrops NYC Planning` · WebSearch → https://www.nyc.gov/assets/planning/download/pdf/plans/special-natural-area-district/snad.pdf (WebFetch, SNAD update; CPC approval Jan 5 2005, Council Feb 2 2005): Staten Island portion covers the Greenbelt (NA-1) and Shore Acres (NA-3), "more than 3,500 acres (2420 lots)", Community Districts 1 and 2; protected features "rock outcroppings, trees and forests, wetlands and water features, and steep slopes"; CPC authorization required to modify a significant natural feature such as steep slope topography or rock outcroppings; tree removal and topography change reviewed. Document does not use the word "excavation". → §8.5 compliance, §9 SNAD question, trench section, §9 tree question.
- Query: `St. George Historic District New Brighton Staten Island Landmarks Preservation Commission designated` · WebSearch → https://hdc.org/?p=11672 (WebFetch): St. George/New Brighton Historic District designated 1994, "only the second designated district in the entire borough"; suburban residences 1830s–1930s; Colonial Revival, Queen Anne, Shingle Style. → §7 building card, §8.5, §13 coverage.
- Query: `Staten Island housing stock one- and two-family detached homes share percent NYC Furman Center` · WebSearch → https://chpcny.org/visualization/housing-stock-visualization/ (WebFetch, CHPC, Oct 2024, 2023 NYC HVS data): "in Staten Island, 83 percent of units are in one- or two-family homes"; Staten Island ~5% of the city's housing units. → §5 para 2, §5.5, §7.
- Query: `Bay Street Corridor rezoning approved 2019 Staten Island North Shore Stapleton Tompkinsville` · WebSearch → https://citylimits.org/2019/06/26/council-approves-bay-street-rezoning-the-sixth-under-de-blasios-housing-plan/ (WebFetch): Council approved June 26 2019, 44–2; ~1,800 new units incl. 1,300 income-targeted; 20 blocks centred on Stapleton and Tompkinsville. → §8 North Shore card, §5.5.

### Commercial, logistics, campuses, landmarks
- Query: `Staten Island Teleport fiber optic Bloomfield history` · WebSearch → https://en.wikipedia.org/wiki/Teleport_(Staten_Island) (WebFetch): 100-acre business park east of Route 440, west of Bulls Head; developed mid-1980s by NYC and the Port Authority; five buildings, 700,000 sq ft; satellite and fiber connectivity; AT&T moved 4,000 employees out in 2001; buildings sold 2009 to Nicotra Group (Corporate Commons). → §8 Teleport card, §13 card.
  - https://clui.org/ludb/site/staten-island-teleport (WebFetch): satellite antennas removed; redeveloped for data processing/storage; NYIIX has one of five NYC connection points there. → §8, §13.
  - https://knowledge.digitaledge.net/white-papers/redundant-access-to-telehouse-facility/ (WebFetch, dated Oct 19 2007): Telehouse Center at 7 Teleport Drive; OCG added a diverse underground dark-fiber entry path; carriers reach 25 Broadway, 60 Hudson St and 111 Eighth Ave. → §8 Teleport card (stated as a 2007 report), §10 equipment context.
- Query: `Matrix Global Logistics Park Staten Island Bloomfield square feet warehouse` · WebSearch → https://commercialobserver.com/2020/01/amazon-expands-its-staten-island-distribution-center-to-1-3m-sf (WebFetch, Jan 28 2020): Amazon 855,000 sq ft facility opened 2018 in the 200-acre Bloomfield industrial complex, Gulf Avenue near the Goethals Bridge, 2,000+ workers; additional 450,000 sq ft lease; IKEA 975,000 sq ft fulfilment centre in the same Matrix complex. → §5, §5.5, §8 West Shore card, §13 card.
- Query: `GCT New York Howland Hook Marine Terminal Staten Island acres container terminal` · WebSearch → https://www.bisnow.com/news/new-york/land/nyc-acquires-122-acre-waterfront-sites-eyeing-port-redevelopment-124262 (WebFetch, May 14 2024): city's 225 acres at Howland Hook Marine Terminal transferred to the Port Authority in a land swap for Red Hook (not final at publication). → §8 West Shore card.
- Query: `College of Staten Island Willowbrook campus 204 acres buildings former Willowbrook State School` · WebSearch → https://en.wikipedia.org/wiki/College_of_Staten_Island (WebFetch): 204-acre Willowbrook campus, largest campus by area in NYC; on part of former Willowbrook State School site (closed 1987); at Willowbrook since 1993; Innovation Hub at Lighthouse Point, St. George. → §7 campus card, §13 card.
- Query: `Snug Harbor Cultural Center 83 acres buildings Staten Island historic` · WebSearch → https://en.wikipedia.org/wiki/Snug_Harbor (WebFetch): 83 acres at 1000 Richmond Terrace, Randall Manor, facing the Kill Van Kull; more than two dozen architecturally significant buildings; Building C completed August 1833 (Greek Revival); NYC landmarks 1965 (A–E and chapel); National Historic Landmark District 1976. → §13 card, §7.5.
- Query: `Staten Island University Hospital campuses Ocean Breeze Prince's Bay beds Northwell` · WebSearch → https://en.wikipedia.org/wiki/Staten_Island_University_Hospital (WebFetch): North Campus 475 Seaview Ave (South Beach/Ocean Breeze); South Campus renamed SIUH Prince's Bay (Aug 2021); 668 beds; Northwell Health; founded 1861. → §8 medical card, §13 card.
- Query: `Staten Island Mall square feet Richmond Avenue New Springville redevelopment` · WebSearch → https://en.wikipedia.org/wiki/Staten_Island_Mall (WebFetch): opened August 9 1973; 1,370,000 sq ft; New Springville; owner GGP/Brookfield; second-largest shopping centre in NYC. → §8 retail card, §13 card.
- Query: `Lighthouse Point St. George Staten Island Empire Outlets opened development` · WebSearch → https://www.triangleequities.com/real-estate-development-press/lighthouse-point-phase-one-completes-construction-in-st-george-staten-island (WebFetch, June 6 2025): Lighthouse Point Phase One complete at 5 Bay Street, steps from the ferry terminal; 115 units; 60,000 sq ft commercial; CSI Tech Incubator tenant. https://rebusinessonline.com/bfc-partners-breaks-ground-on-empire-outlets-on-staten-island/ (WebFetch, Apr 17 2015): Empire Outlets 340,000 sq ft, 100 outlet stores, near the ferry terminal. → §8 St. George card, §13 card.
- Query: `Freshkills Park 2,200 acres former landfill Staten Island NYC Parks` · WebSearch → https://en.wikipedia.org/wiki/Freshkills_Park (WebFetch): ~2,200 acres; landfill closed March 22 2001; North Park Phase 1 opened October 15 2023; full build-out 2035–2037; almost three times Central Park. → §13 card.
- Not researched / EMPTY: Hylan Boulevard, Richmond Avenue, Forest Avenue, Victory Boulevard and Arthur Kill Road are named only as corridors/streets (real streets, no statistics attached); Staten Island community-district broadband-subscription figures not retrieved (EMPTY); Staten Island fiber-installation local news (SI Advance/silive) — no article retrieved, EMPTY.

### Local licensing / permits
- Silo sources reused: DOB low-voltage permit statement (site's own structured-cabling-pricing page), firestopping (nyflnerds/unifinerds), street-opening permit claim (lowvoltagenewyork), LPC permit guidebook. → §8.5.
- SNAD and St. George/New Brighton HD above. → §8.5.
- 811 one-call: New York 811 serves NYC + Nassau/Suffolk (silo HV source https://newyork-811.com/excavators/) → trench section, process step 3 ("call 811 before digging").

### Pricing used (existing approved prices × blueprint §9; no new prices)
Base (Brooklyn 1.00×, research/fiber-optic-installation.md Pricing; fiber-optic-installation-brooklyn.html): $35 termination, $40 OTDR/strand, $350 MM drop, $400 SM drop, $4,500–$7,000 12-strand OM4, $8,000–$15,000+ 24-strand OS2, from $2,400 second telecom room; $195/hr 3-hr min ($585) protected, unchanged.
Staten Island 1.10× (round half-up): $39 termination, $44 OTDR/strand, $385 MM drop, $440 SM drop, $4,950–$7,700 OM4 backbone, $8,800–$16,500+ OS2 link, from $2,640 second room. Packages (built only from these lines, same structure as the Brooklyn page): Starter 2 × $440 = $880; Standard $4,950–$7,700; Premium $8,800–$16,500+.
CONFLICT for review: live structured-cabling-pricing-staten-island.html configurator lists fiber drops at $411 multimode / $470 single-mode (≈1.175×, not §9's 1.10×); that page's meta description also says "Brooklyn" and shows (718) 957-1295. This page follows blueprint §9 as the LI/HV fiber hubs did. Needs Anwar's call.

### Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected
All copied into images/fiber-optic-installation/ as WebP (q80). Printed phone numbers on technicians' shirts/caps were blurred (pixelate + blur) because the page rule forbids visible phone numbers; the storefront photo was cropped above the store-hours sign. No other edits.
| New file | Source |
|---|---|
| fiber-optic-installation-staten-island-exterior-wall-enclosure-conduit.webp | low-voltage/low-voltage-installation-staten-island-exterior-enclosure-install.jpg |
| fiber-optic-installation-staten-island-sfp-switch-rack-mount.webp | network/network-installation-staten-island-managed-poe-switch-rack-install.webp |
| fiber-optic-installation-staten-island-link-tester-rack-and-jack.webp | network/network-installation-staten-island-fluke-dsx-certification-pass.webp |
| fiber-optic-installation-staten-island-ceiling-tile-cable-feed.webp | network/network-installation-staten-island-ceiling-tile-cable-drop-occupied-office.webp |
| fiber-optic-installation-staten-island-corridor-riser-bundle-dress.webp | network/network-installation-long-island-idf-riser-cable-bundle.webp |
| fiber-optic-installation-staten-island-block-wall-conduit-box-pull.webp | low-voltage/low-voltage-installation-staten-island-riser-conduit-pull.jpg |
| fiber-optic-installation-staten-island-retail-fitout-ceiling-pull.webp | low-voltage/low-voltage-installation-staten-island-retail-store-ceiling-pull.jpg |
| fiber-optic-installation-staten-island-metal-stud-cable-routing.webp | low-voltage/low-voltage-installation-hudson-valley-stud-rough-in-boxes.jpg |
| fiber-optic-installation-staten-island-storefront-canopy-camera-mount.webp | low-voltage/low-voltage-installation-nassau-county-storefront-camera-install.jpg (cropped) |
| fiber-optic-installation-staten-island-wall-fish-tape-retrofit.webp | network/network-installation-staten-island-retrofit-wall-fish-data-drop.webp |
| fiber-optic-installation-staten-island-ceiling-access-point-mount.webp | network/network-installation-staten-island-wireless-access-point-ceiling-install.webp |
Overlap note: retail ceiling pull, metal-stud routing and storefront camera scenes were not on any fiber page; the other 8 scenes appear once or twice elsewhere in the fiber silo (no fiber-specific scene was left unused). The library photos look AI-rendered (garbled text on boxes/logos) — flagged again for Anwar.

### Keyword plan (Staten Island page)
Service: fiber optic installation Staten Island, building-to-building fiber, outdoor/aerial vs buried fiber, house-to-outbuilding fiber, strip-centre fiber, fusion splicing, OTDR testing. Problem: overhead lines and storms, flood-elevated houses, SNAD trees/slopes/rock, shared driveways, HOA approvals, landlord demarc at one end of a strip, moving office trailers, corporate cabling specs, party walls. Technology: OS2, OM4, armored indoor/outdoor, all-dielectric self-supporting aerial, innerduct, HDPE conduit, pull boxes, media converters, SFP. Industry: logistics/warehousing, retail strips and malls, medical offices, schools/churches, contractors' yards, home offices, townhouse communities. Geographic: Staten Island, St. George, Stapleton, Tompkinsville, Bay Street, New Brighton, Port Richmond, Bloomfield, Travis, Bulls Head, New Springville, Willowbrook, Todt Hill, Grymes Hill, South Beach, Midland Beach, New Dorp, Great Kills, Eltingville, Annadale, Prince's Bay, Charleston, Rossville, Tottenville, Hylan Blvd, Richmond Ave, Forest Ave, Victory Blvd.

### Question register additions
fiber-optic-installation-staten-island
§9 Questions Answered:
- Our house was raised above the flood line after Sandy — where should the incoming fiber and the network equipment go now?
- Our townhouse community's HOA controls the outside walls and the grounds — how do we get a fiber run approved?
- Who has to sign off before fiber work on a lot in the Special Natural Area District?
- A mature tree stands between our two buildings — can fiber get past it without harming the roots?
- The route to our back building crosses a driveway we share with the neighbour — whose permission do we need?
- Our strip unit's fiber would have to pass through the next tenant's ceiling — how is that handled without disrupting their business?
- Our contractor's yard runs from an office trailer that may be moved — can fiber still reach it?
- A national logistics tenant has sent its own cabling specification — can a local installer build to it?
- The warehouse racking will be rearranged next year — how should the fiber be routed so it isn't in the way?
- Our pad-site restaurant on Richmond Avenue needs its drive-through order point and menu boards online — is fiber worth it out there?
- Will city sidewalk or curb work in front of the property disturb fiber we own?
§17 FAQ:
- Does your Staten Island coverage include Tottenville, Charleston and the rest of the South Shore?
- Does adding fiber raise what a Staten Island home is worth?
- Can a fiber link reach a detached building that has no electricity yet?
- Can fiber pass through the fire-rated wall between an attached garage and the house?
- Will a fiber job need Con Edison to shut off our power?
- Does the heat in an uninsulated attic harm fiber cable?
- Can the old satellite-dish cable route into the house be reused for fiber?
- What warranty applies to the fiber you install?
- Can exterior conduit be matched to vinyl or aluminium siding?
- Our building is wired only with cable-company coax — does fiber replace it or run alongside?
- If we build an addition later, can the fiber be extended without starting over?
- What should we do to get the property ready for installation day?

De-dup notes: after comparing with the batch siblings (Nassau, Suffolk) five questions were replaced — the SNAD trench question reworded to an approvals question (Suffolk asks about trenching in the Central Pine Barrens); strip-tenant shared run (Nassau/Suffolk shared-link intents), party-wall link between two owners (Nassau "two neighbouring buildings with different owners"), fire alarm over fiber (Nassau Fire Marshal question), lawn restoration (Suffolk), rodents (Suffolk burrowing animals) and third-party fiber testing (Nassau) were all removed. Remaining closest intents for the main run to judge: elevated-house equipment placement vs Suffolk "splice enclosure height on a bayfront lot"; SNAD sign-off vs Suffolk "who licenses and permits fiber work"; no-electricity outbuilding vs HV "what equipment sits at each end".
Pricing/content notes: masked paragraph similarity (difflib, ≥12-word paragraphs, exempt NAP/warranty/stamp/pricing cells/form text) max 0.588 vs Brooklyn and Suffolk; file 203,438 B.

### Question register additions (final, as shipped — main run 2026-10-17)
fiber-optic-installation-staten-island
§9 Questions Answered:
- Our house was raised above the flood line after Sandy — where should the incoming fiber and the network equipment go now?
- Our townhouse community's HOA controls the outside walls and the grounds — how do we get a fiber run approved?
- Who has to sign off before fiber work on a lot in the Special Natural Area District?
- A mature tree stands between our two buildings — can fiber get past it without harming the roots?
- The route to our back building crosses a driveway we share with the neighbour — whose permission do we need?
- Our strip unit's fiber would have to pass through the next tenant's ceiling — how is that handled without disrupting their business?
- Our contractor's yard runs from an office trailer that may be moved — can fiber still reach it?
- A national logistics tenant has sent its own cabling specification — can a local installer build to it?
- The warehouse racking will be rearranged next year — how should the fiber be routed so it isn't in the way?
- Our pad-site restaurant on Richmond Avenue needs its drive-through order point and menu boards online — is fiber worth it out there?
- Will city sidewalk or curb work in front of the property disturb fiber we own?
§17 FAQ:
- Does your Staten Island coverage include Tottenville, Charleston and the rest of the South Shore?
- Does adding fiber raise what a Staten Island home is worth?
- Can a fiber link reach a detached building that has no electricity yet?
- Can fiber pass through the fire-rated wall between an attached garage and the house?
- Will a fiber job need Con Edison to shut off our power?
- Does the heat in an uninsulated attic harm fiber cable?
- Can the old satellite-dish cable route into the house be reused for fiber?
- What warranty applies to the fiber you install?
- Can exterior conduit be matched to vinyl or aluminium siding?
- Our building is wired only with cable-company coax — does fiber replace it or run alongside?
- If we build an addition later, can the fiber be extended without starting over?
- What should we do to get the property ready for installation day?

## Nassau County — local research (2026-10-17 batch, fiber-optic-installation-nassau-county)

Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources and the Long Island hub section are reused only where noted; nothing below is inferred to fill a gap. Page thesis: **carrier fiber already reaches almost every Nassau address (and Verizon's Town of Hempstead build dates from 2006–2007), so the Nassau problem is not getting fiber to the property — it is the owner-side gap inside older, built-out, often re-tenanted buildings (1950s–1970s office stock, village Main Street mixed-use, school districts, medical and retail), plus legacy fiber and copper already in the ceilings.** The LI hub's thesis (crossing open ground between buildings) is deliberately not repeated.

### Reddit (local)
- `reddit r/longisland Nassau fiber internet office building Garden City Mineola Lake Success` · Firecrawl web search (excerpts only; Firecrawl does not scrape reddit.com):
  - https://www.reddit.com/r/longisland/comments/1jba48u/best_internet_only_providers/ — excerpt: "In Nassau county what internet only providers do you guys like to use? What's the going rate these days for gig up/gig down?" → §5 Neighborhood para 2 (residents compare providers, not whether fiber exists). Quoted as a resident question only.
  - https://www.reddit.com/r/longisland/comments/1t32xvr/what_are_the_proscons_to_live_in_mineola_garden/ — excerpt about Mineola/Garden City/Hempstead living; NOT used (not about wiring).
  - https://www.verizon.com/home/internet/near-me/long-island-new-york/ (same search, excerpt): "Central Nassau: Hempstead, Garden City, Mineola" listed under where Verizon home internet is available → §5 para 1 (context only).
  - r/longisland threads on Nassau office fiber or building wiring: EMPTY (none returned).

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitutes for §10.5 (claims quoted as published):
- bestneighborhood.org (below) "Verizon Fiber: 99.32%" → H3 1.
- unio.digital (silo source) "$300 to $800 per fiber drop" → H3 2.
- lowvoltagenewyork.com (silo source, Manhattan section) "nobody publishes a flat per-strand rate" → H3 3; "singlemode glass is now cheaper than OM4" / SM optics 1.5–5× → H3 4; "Plenum rating adds 15–25%" → H3 5.
- quantumfiber multifamily timeline (silo source) 30 + 30 + 40–60 days → H3 6.
- Verizon Town of Hempstead release (below) "Full town coverage within five years" → H3 7.
- Yelp: no yelp.com result in any query. EMPTY.

### Carrier fiber availability and history (core of thesis)
- `Verizon Fios Nassau County availability where available Central Nassau Hempstead Garden City Mineola` · WebSearch → https://bestneighborhood.org/fiber-tv-and-internet-nassau-county-ny/ (WebFetch): Optimum Fiber 96.57% (~1,347,927 people), EarthLink Fiber 99.32%, Verizon Fiber 99.32% (~1,386,296 people); FCC update dated Sept 3 2026 reflecting Broadband Data Collection as of Dec 31 2025. → §5 para 1, §5.5 facts, §10.5 H3 1. (Third-party aggregator of FCC data; attributed as such. EarthLink resells — not named on page.)
- Same search → https://verizon.com/about/node/117859 (WebFetch): Verizon release (undated; references "end of 2007" targets, so ~2006): ~65% of Town of Hempstead by year-end, up to 87% by end of 2007, full coverage within five years under the franchise; already served Lakeview, Valley Stream, Hicksville, Plainview; 2006 build Freeport, Roosevelt, Baldwin, Merrick, Elmont, Franklin Square; 2007 build Village of Hempstead, Uniondale, West Hempstead, Long Beach. → §5 para 2 (early-generation installs now ~20 years old), §5.5, §9 Q1, §10.5 H3 7. Stated as "Verizon said at the time".

### Building stock, corridors, landmarks
- `Lake Success Marcus Avenue office market 2026 vacancy Nassau County office` · WebSearch → https://2001marcusavenue.sharplaunch.com (WebFetch): 2001 Marcus Avenue, Lake Success — ~212,000 RSF (fact sheet; overview says 214,000), 3 floors, typical floor 70,621 RSF, completed 1979 (overview says 1978), steel frame/curtain wall, recent upgrades incl. energy management system, elevator modernisation, fire alarm; near LIE, Cross Island and Northern State. → §7 office card, §8 Lake Success card, §13 landmark card, FAQ building-controls. (Range given as "about 212,000"; year "1978–79".)
- Same search → https://rebusinessonline.com/northwell-health-signs-lease-renewals-totaling-32413-sf-in-lake-success-new-york (title only, not fetched): Northwell lease renewals 32,413 SF in Lake Success → NOT used (not fetched).
- `Roosevelt Field mall square feet Garden City largest mall Long Island` · WebSearch → https://en.wikipedia.org/wiki/Roosevelt_Field_(shopping_mall) (WebFetch): 2,372,053 sq ft; 630 Old Country Road, East Garden City section of Uniondale; opened 1956; Simon since 1998; built on Roosevelt Field airfield where Lindbergh's 1927 transatlantic flight took off; airfield closed 1951. → §8 Old Country Road card, §13 card.
- `Nassau Community College campus acres Mitchel Field Garden City buildings` · WebSearch → https://www.ncc.edu/aboutncc/fastfacts.shtml (WebFetch): founded 1959, opened 1960 with 632 students in the old county courthouse in Mineola; 1962 moved to 135 acres of former Mitchel Air Force Base; now 225 acres and 50 buildings; 17,000+ students. → §7 campus card, §13 card.
- `NYU Langone Hospital Long Island Mineola beds campus` · WebSearch → https://en.wikipedia.org/wiki/NYU_Langone_Hospital_%E2%80%93_Long_Island (WebFetch): 259 First Street, Mineola; 591 beds; founded 1896 as Nassau Hospital; Winthrop-University Hospital name 1985; NYU affiliation 2017, merger 2019, renamed Nov 2020. → §8 Mineola card, §13 card.
- `Grumman Bethpage plant history acres former aerospace site redevelopment` · WebSearch → https://en.wikipedia.org/wiki/Naval_Weapons_Industrial_Reserve_Plant,_Bethpage (WebFetch): 605 acres, Town of Oyster Bay, Bethpage; Navy plant est. 1941; Grumman founded 1936; manufacturing stopped 1996; groundwater plumes (shallow 1986, deeper 2009); state Superfund cleanup plans. → §8 Bethpage card, §13 card, (restricted-ground Q&A later removed for overlap with Suffolk; Bethpage now used in §8 card and §13 landmark only).
- `LIRR Third Track completed Floral Park Hicksville` · WebSearch → https://www.cbsnews.com/newyork/news/long-island-rail-road-completes-long-awaited-3rd-track-project-increasing-service-by-40/ (WebFetch, updated Oct 3 2022): 10 miles Floral Park–Hicksville; ~5 years construction; officials cite 40% more service. → §5.5 facts, §8 Main Line villages card. (No claim made about TOD apartment counts — not sourced.)
- `Nassau County number of school districts` · WebSearch → https://www.nassauboces.org/fs/pages/3706 (WebFetch): "across all 56 school districts" (Nassau). → §5.5, §7 schools card, §9 Q6.
- `Nassau County fiber optic network news 2025 2026 village school district fiber` · WebSearch → https://patch.com/new-york/mineola/mineola-board-of-ed-notebook-nov-3 (WebFetch, Patch Dec 6 2011): Mineola board approved a five-year agreement with Nassau BOCES "for fiber optic connectivity" (WAN, internet and voice), $176,905. → §9 Q6 (example of the BOCES-provided WAN model; dated as 2011).
- Nassau municipal structure (2 cities, 3 towns, 64 villages) and population: LI hub source https://www.ny.gov/counties/nassau reused → §5 para 3 (short reference only).
- `Nassau County housing stock median year built homes census` · WebSearch → no primary census page returned (tophap/redfin/HUD archive listings only). EMPTY — page gives no median-year figure.
- `Nassau Hub Coliseum redevelopment 2026 plan after casino` · WebSearch → news12/bisnow/CBS/YIMBY results about the Las Vegas Sands proposal; outcome not verified. NOT used (status unclear).

### Storms / flood (South Shore)
- `Superstorm Sandy Nassau County homes damaged number South Shore Long Beach Island Park Freeport` · WebSearch → https://www.cbsnews.com/newyork/news/more-than-2000-long-island-homes-uninhabitable-after-sandy (WebFetch, Dec 11 2012, AP): more than 2,000 Long Island homes destroyed or uninhabitable; Town of Hempstead "more than 1,000 residences destroyed"; Nassau "hit harder than Suffolk"; 71,000+ Nassau households applied for FEMA help. → §5.5, South Shore section.

### Licensing / permits / regulation (local)
- `Nassau County Office of Consumer Affairs home improvement license who needs license trades` · WebSearch → https://archive.nassaucountyny.gov/agencies/OCA/Licensing/FAQ.html (WebFetch): licence needed by "Contractors who perform remodeling on RESIDENTIAL homes in Nassau County"; "Anyone who works only on COMMERCIAL buildings does NOT need a license"; licensed electricians/plumbers etc. exempt in their field. No mention of low voltage or cabling. → §8.5 callout, §9 Q4. Page states the commercial exemption and that the FAQ is silent on low-voltage; says homeowners can ask OCA and that AESS holds NYS licence #12000287431. **Does not claim AESS holds a Nassau HIC licence — needs Anwar's confirmation.**
- Same search → https://nassaucountyny.gov/1563/Licensing (WebFetch): OCA licence list (home improvement 21-11, home services, locksmiths, electronic/home appliance repair, etc.); no low-voltage, alarm or cabling category. → §8.5 callout.
- `Nassau County Fire Marshal permit plans required commercial occupancy fire alarm low voltage plan review` · WebSearch → https://northhempsteadny.gov/filestorage/16281/32216/32218/Commercial_Plan_Review_Checklist.pdf (WebFetch): Town of North Hempstead commercial checklist — modifying/installing a fire alarm "requires the filing of a Fire Alarm application with the Nassau County Fire Marshal"; sprinkler changes likewise; no mention of data/telecom cabling. → §8.5 callout, §9 Q5. Stated as one town's checklist.
- `New York Industrial Code Rule 56 asbestos survey required before renovation building owner` · WebSearch → https://dol.ny.gov/new-york-state-asbestos-survey-requirements (WebFetch): owner must obtain a survey by a certified NYS Asbestos Inspector before demolition, renovation, remodel or repair; post-1973 buildings exempt under 56-5.1(b) from that section but page says "surveys are required for all demolitions, renovations, remodels, or repairs regardless of construction date". → FAQ asbestos question, §8.5. **Wording for Anwar's skim.**
- Village/town low-voltage permit rules: EMPTY (no village page retrieved); page says to check per address, consistent with LI hub.

### Technical (new for this page)
- `OM1 OM2 10GBASE-SR maximum distance 33 m 82 m` · WebSearch → https://foa.org/tech/Linkspec.htm (WebFetch): 10GBASE-S: OM1 33 m, OM2 82 m, OM3 300 m, OM4 450 m; 1000BASE-SX: OM1 275 m, OM2 550 m, OM3 800 m, OM4 880 m. → §7.5 methods, FAQ legacy multimode question, §10 equipment, §10.5 H3 4.
- Silo sources reused: FOA install guide (bend radius), cablinginstall OFNR/OFNP listings, ampcom SM/MM.

### Local news / hyperlocal (Newsday, Herald, Patch, News12) on Nassau fiber installation contractors — EMPTY beyond the 2011 Mineola Patch item.

### Pricing used (existing approved prices only — mirrors the LI hub Nassau column; no new prices)
Base Brooklyn 1.00× × blueprint §9 Nassau 1.15×, rounded half-up, exactly as live on fiber-optic-installation-long-island: $40/termination, $46/strand OTDR, $403 multimode drop, $460 single-mode drop, 12-strand OM4 backbone $5,175–$8,050, 24-strand OS2 $9,200–$17,250+, second telecom room from $2,760; $195/hr 3-hr minimum ($585) unchanged (protected). Worked packages are arithmetic on those lines only: two SM drops $920; 24 terminations + 12 OTDR = $1,512.
CONFLICT (carried from LI hub): live structured-cabling-pricing-nassau-county configurator shows fiber drops $411/$470 — not used.

### Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected
All images/network/ scenes are already used on a live fiber page and every network/ photo shows a printed phone number (844-386-7238) on the technician's shirt, so all 11 come from images/low-voltage/ Nassau-named files with no visible phone number. 5 of the 11 scenes are on no other fiber page; 6 repeat scenes used on the HV/Manhattan fiber pages from different source files.
| File (images/fiber-optic-installation/) | Source (images/low-voltage/) |
|---|---|
| fiber-optic-installation-nassau-county-idf-rack-patching.webp (hero, eager) | low-voltage-installation-nassau-county-06-idf-rack-patching.jpg |
| fiber-optic-installation-nassau-county-jhook-bundles-open-office.webp | low-voltage-installation-nassau-county-04-jhook-pathway-bundle.jpg |
| fiber-optic-installation-nassau-county-certification-tester-wall-jack.webp | low-voltage-installation-nassau-county-07-fluke-certification-pass.jpg |
| fiber-optic-installation-nassau-county-wall-plate-termination-office.webp | low-voltage-installation-nassau-county-hero-keystone-wall-plate.jpg |
| fiber-optic-installation-nassau-county-ceiling-access-point-cable.webp | low-voltage-installation-nassau-county-08-ceiling-access-point-drop.jpg |
| fiber-optic-installation-nassau-county-school-corridor-ceiling-pull.webp | low-voltage-installation-nassau-county-school-corridor-ceiling-tile.jpg |
| fiber-optic-installation-nassau-county-crew-fitout-cable-reels.webp | low-voltage-installation-nassau-county-03-crew-cable-pull.jpg |
| fiber-optic-installation-nassau-county-hardhat-stud-wall-pull.webp | low-voltage-installation-nassau-county-09-metal-stud-rough-in.jpg |
| fiber-optic-installation-nassau-county-patch-panel-punchdown-hands.webp | low-voltage-installation-nassau-county-02-cat6-patch-panel-punchdown.jpg |
| fiber-optic-installation-nassau-county-ceiling-grid-bundle-feed.webp | low-voltage-installation-nassau-county-04-ceiling-grid-bundle-pull.jpg |
| fiber-optic-installation-nassau-county-conference-room-cable-box.webp | low-voltage-installation-nassau-county-11-conference-room-display-cabling.jpg |
Note: the photos show copper (blue Cat6) work, not fiber; captions describe only that. Several look AI-rendered (garbled tester screen text) — for Anwar's review.

### Keyword plan (Nassau page)
Service: fiber optic installation Nassau County, fiber backbone, fiber riser, legacy fiber re-termination, OTDR testing, fusion splicing, demarc extension. Problem: carrier fiber at the curb but old copper inside, 2006-era carrier install, OM1/OM2 legacy multimode, return-air plenum ceilings, asbestos-era ceilings, split suites, shared closets, fire alarm on fiber, flood-rebuilt South Shore. Technology: OS2, OM4, OM1/OM2, LC/SC, OFNP/OFNR, splice enclosures, media converters. Industry: 1970s office parks, medical, schools (BOCES), retail/malls, village Main Street mixed-use, home-based businesses. Geographic: Nassau County, Lake Success, Garden City, Mineola, Uniondale, Hicksville, Bethpage, Valley Stream, Freeport, Long Beach, Great Neck, Port Washington, Glen Cove, Rockville Centre, Massapequa, Westbury, Syosset, Oyster Bay, Hempstead, North Hempstead.

### Question register additions — fiber-optic-installation-nassau-county
fiber-optic-installation-nassau-county
§9 Questions Answered:
- The Fios equipment in our basement went in around 2007 — should anything on our side of it be replaced now?
- Our building has fiber service at the wall, but the wiring to the desks is decades-old phone cable — where should the money go first?
- Can a shop and the apartments above it share one fiber cable while keeping their networks completely separate?
- We're handing back half our floor to the landlord — what happens to the fiber that crosses the space we're giving up?
- Does Nassau County's home improvement licence cover fiber work in a private house?
- If our fire alarm panel will report over the new fiber, does the Nassau County Fire Marshal get involved?
- Our school district's internet arrives over a BOCES connection — where does district-owned fiber take over?
- Our office is upstairs from a restaurant kitchen — does the heat and grease in the shared ceiling affect fiber?
- I run a business from my house — can my office get its own wired, documented connection separate from the family network?
- The space above our ceiling tiles carries the building's return air — what fiber is allowed up there?
§17 FAQ:
- Do you cover the North Shore, the South Shore and the incorporated villages in between?
- Can multimode fiber installed in the 1990s carry today's network speeds?
- Is it safe to install fiber in an older building that may contain asbestos?
- What happens to our fiber when the landlord replaces the drop ceiling?
- Will you test fiber another company installed before we accept their work?
- How is payment handled on a Nassau fiber job?
- Can a fiber link carry a separate network for our building's heating, cooling and energy controls?
- Will a new fiber backbone work with the network switches we already own?
- Can the phone company's dead boxes and old cables on our wall be removed during the fiber job?

De-dup notes: compared by meaning with the NYC/Manhattan/Brooklyn/LI/HV register and the concurrent Staten Island and Suffolk pages. Replaced: neighbour-owned-buildings FAQ (overlap with SI shared-driveway permission Q) and former-industrial-site digging Q (overlap with Suffolk Pine Barrens trench Q). Judged different: Nassau HIC-licence Q vs Suffolk permit Q (contractor licence vs work permit); existing-switches FAQ vs NYC 'Do you supply the switches and optics' and HV 'What equipment sits at each end' (compatibility of owned switches) — main run to confirm. No question-form repair headings used.

### Question register additions (final, as shipped — main run 2026-10-17)
fiber-optic-installation-nassau-county
§9 Questions Answered:
- The Fios equipment in our basement went in around 2007 — should anything on our side of it be replaced now?
- Our building has fiber service at the wall, but the wiring to the desks is decades-old phone cable — where should the money go first?
- We own two attached storefronts and are merging them into one business — can fiber join the two networks through the shared wall?
- We're handing back half our floor to the landlord — what happens to the fiber that crosses the space we're giving up?
- Does Nassau County's home improvement licence cover fiber work in a private house?
- If our fire alarm panel will report over the new fiber, does the Nassau County Fire Marshal get involved?
- Our school district's internet arrives over a BOCES connection — where does district-owned fiber take over?
- Our office is upstairs from a restaurant kitchen — does the heat and grease in the shared ceiling affect fiber?
- I run a business from my house — can my office get its own wired, documented connection separate from the family network?
- The space above our ceiling tiles carries the building's return air — what fiber is allowed up there?
§17 FAQ:
- Do you cover the North Shore, the South Shore and the incorporated villages in between?
- Can our Wi-Fi access points run straight off the new fiber backbone?
- Can fiber be added to a finished office without opening the walls?
- What happens to our fiber when the landlord replaces the drop ceiling?
- Will you test fiber another company installed before we accept their work?
- How much downtime should we plan for when the new backbone goes live?
- Can a fiber link carry a separate network for our building's heating, cooling and energy controls?
- Will a new fiber backbone work with the network switches we already own?
- Can the phone company's dead boxes and old cables on our wall be removed during the fiber job?

## Suffolk County — local research (2026-10-17 batch, fiber-optic-installation-suffolk-county)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources and the Long Island hub section are reused where noted and are NOT repeated on the page (hub already uses Hauppauge 1,350 businesses, Route 110/Melville, Stony Brook 1,454 acres, BNL 5,265 acres, Optimum ~900k passings, Brookhaven Verizon franchise, Isaias, Long Beach Sandy, ny.gov 2,373 sq mi / 1.52M / 10 towns). Page thesis: Suffolk is a long county where the fiber job changes with the ground and the calendar — sandy outwash and septic systems in the west, the Central Pine Barrens in the middle, farms, vineyards and seasonal/rented houses on the East End, and flood-exposed South Shore canal lots — and much of the East End has had one wired provider, so private owner-side fiber has to be built to last through provider changes.

### Reddit (local)
- Query: `reddit r/longisland Suffolk barn OR outbuilding OR detached garage ethernet fiber run internet` · Firecrawl web search (excerpts only; reddit.com not scraped). Results were r/HomeNetworking threads, not r/longisland → r/longisland local: EMPTY. Topical excerpts already in the HV register (barn) were not reused on this page.
  - https://www.reddit.com/r/HomeNetworking/comments/1p0wdhv/should_i_run_fiber_cable_networking_to_a_separate/ — excerpt: "If they're on different grounds you really need to run fiber or current between the two can be a problem." → background only (not quoted; HV page owns this intent).
- Query: `reddit longisland Suffolk fiber internet Optimum only option East End North Fork` · WebSearch → no reddit.com results. EMPTY.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitutes for §10.5 reality check: claims as published by silo sources already in research/fiber-optic-installation.md (thenetworkinstallers.com FBA 2025 medians; unio.digital trenching $15–$35/ft, boring $20–$30/ft, aerial $8–$12/ft; lowvoltagenewyork "Plenum rating adds 15–25%"; newtechcabling "Small projects can take a day or two"; ampcom OS2 10 km+) plus the Verizon East End item below. Each H3 on the page quotes the claim as published and corrects it with Suffolk field conditions.

### Carriers / provider history
- Query: `Verizon Fios East End Southampton East Hampton fiber expansion 2025 2026 North Fork internet` · WebSearch → https://suffolktimes.timesreview.com/?p=53616 (WebFetch; undated Suffolk Times item about a rally at Riverhead Town Hall): Verizon spokesperson John Bonomo — "It's a simple no"; no new FiOS build-outs on the East End; preliminary talks with eastern Suffolk towns in the mid-2000s; towns named Riverhead and Southold; PSC cannot require Verizon to build in a particular area; CWA Local 1108's Michael Gendron: "Having one provider in this area is not working out"; Supervisor Sean Walter: "competition is always better." → §5 para 3 (stated as an older, undated report; page notes Brookhaven's 2026 franchise vote from the hub is a separate later development), §10.5 H3 1, §9 seasonal/rental Q context.

### Development, corridors, landmarks
- Query: `Ronkonkoma Hub transit-oriented development apartments square feet Brookhaven 2025` · WebSearch → https://www.governor.ny.gov/news/governor-hochul-unveils-next-phase-12-billion-transit-oriented-hub-station-yards-creating-more (WebFetch, Oct 22 2024): Station Yards, 53 acres around Ronkonkoma LIRR; 1,450 units at completion; 360,000 sq ft office; 195,000 sq ft retail; Phase 1 489 units (2020), Phase 2 388 units; $1.2B; near LIE Exit 60 and MacArthur Airport; Ronkonkoma station Suffolk's busiest, ~17,000 daily commuters. → §5.5 facts, §8 Ronkonkoma card, §13 landmark card.
- Query: `Long Island MacArthur Airport acres Islip town owned terminal 2025` · WebSearch → https://politicsny.com/2026/07/20/town-of-islip-names-developer-for-long-island-macarthur-airport-terminal-project/ (WebFetch, July 20 2026): Town of Islip named Fly Long Island (RXR + Avports JV) to build a new terminal and link to the Ronkonkoma LIRR station; RFQ issued 2025. → §8 Ronkonkoma card, §13 card (no acreage/passenger figures used — not in source).
- Query: `Enterprise Park at Calverton EPCAL acres Riverhead 2025` / `EPCAL Calverton Enterprise Park subdivision 2025 Riverhead Town Board acres industrial lots` · WebSearch → https://riverheadnewsreview.timesreview.com/?p=94143 (WebFetch; undated, Riverhead News-Review): Planning Board approved a preliminary plat dividing ~2,107 acres at EPCAL into eight lots; lets Calverton Aviation & Technology buy 1,643 acres for ~$40M; ~292 acres protected Pine Barrens; Grumman memorial; Calverton Sewer District recharge area. → §8 Calverton card, §13 card (stated as "preliminary plat", no completion claim).
- Query: `Gabreski Airport Westhampton business park fiber OR Shirley Brookhaven Calabro airport industrial park` · WebSearch → https://www.27east.com/southampton-press/new-business-park-continues-to-take-shape-in-westhampton-1406404 (WebFetch, Aug 26 2016): Hampton Business District (Rechler) at Francis S. Gabreski Airport, 55 acres of county-owned land, 40-year lease signed 2009, 10 buildings planned; Building 1 60,000 sq ft; Building 2 67,000 sq ft offices/medical; tenants incl. Tate's Bake Shop 37,141 sq ft. → §8 Westhampton card, §13 card (dated 2016 on page).
- Query: `Brookhaven National Laboratory Electron-Ion Collider construction 2025 Upton` · WebSearch → https://www.bnl.gov/newsroom/news.php?a=221812 (WebFetch, Apr 2 2024): EIC with Jefferson Lab; CD-3A long-lead procurements; cost $1.7–2.8B; 2.4-mile circumference; most components fit in existing RHIC tunnel. → §8 research card (different from hub's BNL acreage/staff), §13 card.
- Query: `Suffolk County Community College campuses Selden Brentwood Riverhead ...` · WebSearch → https://sunysuffolk.edu/about-suffolk/campus-information/ (WebFetch): Ammerman Campus Selden 156 wooded acres, 13,000+ students; Grant Campus Brentwood 10,000+ students; Eastern Campus 121 Speonk-Riverhead Road, Riverhead. → §7 campus card, §13 card.
- Query: `Patchogue downtown revitalization apartments ...` · WebSearch → results only (nyrej, patch, ny.gov NYF4 application PDF) — not fetched. NOT used.
- Query: `Republic Airport Farmingdale Route 110 ...` · WebSearch → Wikipedia NY 110 etc. Not fetched; NOT used (hub owns Route 110).
- Query: `Suffolk County New York 10 towns 33 incorporated villages hamlets` · WebSearch → https://www.newyorkfamilyhistory.org/knowledgebase/suffolk-county-new-york-cities-towns-and%C2%A0villages (WebFetch): ten towns named — Babylon, Brookhaven, East Hampton, Huntington, Islip, Riverhead, Shelter Island, Smithtown, Southampton, Southold. Village count not given → page does not state a village count. → §5, Ten towns table, FAQ coverage.

### Agriculture, wineries, land
- Query: `Suffolk County 2022 Census of Agriculture number of farms acres market value` · WebSearch → https://shelterislandreporter.timesreview.com/2025/02/02/suffolk-closeup-the-farming-county/ (WebFetch; column citing the NYS Comptroller's "A Profile of Agriculture in New York State"): 578 farms in 2022, up 18 (3%) from 2017 while the state lost 8%; 33,821 acres of farmland; 79 wineries in Suffolk (Long Island 85); Suffolk first in state aquaculture sales; Farmland Preservation Program approved 1974, 11,000+ acres preserved. → §5.5 facts, §7 farm/vineyard card, Farms & vineyards section, §9 farmland Q.
- Query: `Central Pine Barrens Long Island 105,000 acres core preservation area towns ...` · WebSearch → https://pb.state.ny.us/public-information/faqs/ (WebFetch, Central Pine Barrens Commission FAQ): ~105,000 acres; eastern Brookhaven, western Southampton, southern Riverhead; Long Island Pine Barrens Protection Act 1993; in the Core Preservation Area "new construction or development" prohibited/redirected; clearing or material alteration of vegetation counts as development; Core development requires a Commission hardship waiver with public hearing. → §9 Pine Barrens Q, §8.5 callout, Pine Barrens section.

### Flood / coast
- Query: `Suffolk County Long Island hurricane Sandy Fire Island Mastic Beach Lindenhurst flooding homes damaged numbers` · WebSearch →
  - https://www.weather.gov/media/okx/coastalflood/Lindenhurst%20impacts.pdf (WebFetch, NWS Upton impact table): peak 7.7 ft NGVD on 10/29/2012 10 pm; "much of the area south of Montauk Highway" fully inundated with 2 to 5 feet of water in Lindenhurst, Amityville and Babylon; repeated moderate flooding at ~4 ft (2016, 2017, 2018 events). → §5 para 4, §5.5, §9 enclosure-height Q, South Shore section.
  - https://amp.claimsjournal.com/news/east/2012/11/01/216552.htm (WebFetch, AP, Nov 1 2012): 12 Fire Island houses swept out to sea; Fire Island National Seashore superintendent Chris Soller: 80% of remaining houses damaged; worst since 1938. → South Shore section.

### Seasonal population
- Query: `East Hampton OR Southampton seasonal homes percent housing units vacant seasonal use census` and a second variant · WebSearch → https://www.census.gov/library/stories/2023/05/vacant-seasonal-housing.html (WebFetch): no Suffolk figures. https://www.danspapers.com/2021/09/2020-census-east-end-population-shift (WebFetch, ~2021): 2010→2020 East Hampton +6,928 (32%), Shelter Island +861 (36%), Southampton +21.5%, Riverhead +2,396 (7.2%); Suffolk +2.2% to 1.5M; Southampton supervisor's estimate of off-season effective population "probably over 100,000" (an estimate, not used). Seasonal housing-unit share: EMPTY (no source retrieved) — page gives no seasonal-housing percentage. → §5.5 (East End growth figures), seasonal section.

### Licensing / permits
- Query: `Suffolk County Chapter 563 license low voltage electrician home improvement Consumer Affairs requirement` · WebSearch →
  - https://suffolkcountyny.gov/Departments/Consumer-Affairs/Licensing (WebFetch): Master Electricians and Restricted Electricians, continuing education under "Suffolk County Code, Chapter 563, Article XI"; Home Improvement License Law; no mention of low-voltage/alarm/telecom.
  - https://ecode360.com/14947436 (WebFetch): Chapter 563 Article II Home Improvement Contractors; §563-16 definition of home improvement contracting excludes "work in the electrical and plumbing fields as defined by § 563-126"; residential property = one- or two-family houses; §563-23 exemptions. No low-voltage/communications exemption text.
  → §8.5 callout, §9 licensing Q. Page states what Chapter 563 contains and that we confirm county/town requirements per job; it does NOT claim fiber is exempt or covered. FLAG for Anwar: confirm AESS's Suffolk County license position for residential work.
- Query: `Town of Southampton building permit required low voltage wiring OR "data cabling" OR "communications cable" permit` · WebSearch →
  - https://ePermits.southamptontownny.gov/eElectrical (WebFetch): Town of Southampton "Electrical ePermits Portal"; no low-voltage rule stated.
  - https://www.westhamptonbeach.gov/frequently-asked-questions-faq (WebFetch): "you must obtain a permit when you change any structural, electrical, plumbing, gas in your dwelling"; village answer that an Electrical Permit "from the Town of Southampton as well" is needed (question not shown).
  → §8.5, §9 licensing Q (stated as: towns and villages run their own permit desks; Southampton has its own electrical e-permit system; we check per address). Low-voltage permit rules per town: EMPTY.
- Broadband/municipal: `Suffolk County broadband fiber initiative 2025 county government fiber network` · WebSearch → only UK Suffolk results. EMPTY. `Shelter Island OR Southold OR East Hampton town broadband committee fiber internet 2025 2026` · WebSearch → no relevant NY results. EMPTY.
- `North Fork winery tasting room wifi point of sale internet outage ...` · WebSearch → travel listings only. EMPTY.

### Local news / hyperlocal on fiber installation contractors in Suffolk — EMPTY (none retrieved beyond the items above).

### Pricing used (existing approved prices × blueprint §9 Suffolk 1.20×; identical to the LI hub's Suffolk column)
$42 termination · $48 OTDR/strand · $420 MM drop · $480 SM drop · $5,400–$8,400 12-strand OM4 · $9,600–$18,000+ 24-strand OS2 · from $2,880 second room · $195/hr 3-hr min ($585) unchanged (protected). Package arithmetic on this page: Starter = 2 SM drops (2 × $480 = $960); Standard = OM4 backbone $5,400–$8,400; Premium = OS2 link $9,600–$18,000+; "re-terminate an existing 12-strand cable" example = 24 × $42 + 12 × $48 = $1,584 (same arithmetic as hub, used in body text only).
CONFLICT (unchanged, for Anwar): live structured-cabling-pricing-suffolk-county.html shows fiber drops $453 MM / $517 SM; this page follows blueprint §9 like the LI hub.

### Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected
Every images/network/ scene is already on a live fiber page (average-hash comparison against all files in images/fiber-optic-installation/), so all 11 come from images/low-voltage/. Photos showing a phone number (shirts, caps, van) or a street address were rejected or CROPPED so the number is out of frame (crop = framing only, no other edit). Six first-choice photos were swapped out mid-build because the parallel Nassau builder had already copied the same source photos (identical bytes).
| File (images/fiber-optic-installation/) | Source (crop box if cropped) |
|---|---|
| fiber-optic-installation-suffolk-county-recessed-wall-box-patching.webp (hero, eager) | low-voltage/low-voltage-installation-suffolk-county-display-recessed-box.jpg, crop 600,150,1400,1120 |
| fiber-optic-installation-suffolk-county-van-cable-reels-ladders.webp | low-voltage/low-voltage-installation-orange-county-10-van-load-out.jpg, crop 470,140,1000,880 |
| fiber-optic-installation-suffolk-county-conference-camera-mount.webp | low-voltage/low-voltage-installation-suffolk-county-ptz-camera-mount.jpg, crop 520,40,1400,1120 |
| fiber-optic-installation-suffolk-county-storefront-bullet-camera-mount.webp | low-voltage/low-voltage-installation-suffolk-county-storefront-camera-install.jpg |
| fiber-optic-installation-suffolk-county-video-wall-panel-alignment.webp | low-voltage/low-voltage-installation-suffolk-county-video-wall-install.jpg |
| fiber-optic-installation-suffolk-county-door-reader-mounting.webp | low-voltage/low-voltage-installation-suffolk-county-12-access-control-reader-wiring.jpg |
| fiber-optic-installation-suffolk-county-electric-strike-terminal-wiring.webp | low-voltage/low-voltage-installation-nassau-county-electric-strike-wiring.jpg |
| fiber-optic-installation-suffolk-county-video-intercom-entry-wiring.webp | low-voltage/low-voltage-installation-suffolk-county-13-video-intercom-entry-wiring.jpg |
| fiber-optic-installation-suffolk-county-ceiling-speaker-conference-room.webp | low-voltage/low-voltage-installation-suffolk-county-ceiling-speaker-conference.jpg, crop 380,0,1400,1120 |
| fiber-optic-installation-suffolk-county-restaurant-ceiling-speaker.webp | low-voltage/low-voltage-installation-suffolk-county-14-restaurant-ceiling-speaker.jpg |
| fiber-optic-installation-suffolk-county-maglock-terminal-wiring.webp | low-voltage/low-voltage-installation-bronx-12-door-lock-wiring-detail.jpg |
None of these show fiber; the library's only fiber scenes (fusion splicer, splice tray) are each on 4 fiber pages already. Captions describe only what is visible and the page frames them as devices at the end of a fiber-fed network. The set leans heavily toward AV/door hardware — weak fit; replace with real Suffolk fiber photos when available. Library looks AI-rendered (flagged by earlier builders) — for Anwar to review.

### Keyword plan (Suffolk page)
Service: fiber optic installation Suffolk County, buried fiber, farm/vineyard fiber, estate fiber, campus/business-park fiber, fusion splicing, OTDR testing. Problem: Pine Barrens clearing limits, septic/leaching pools and wells, sandy trench walls, plows and posts, rodents, flood-prone canal lots, empty seasonal houses, summer renters on the owner's network, single wired provider. Technology: OS2 loose-tube, armoured/rodent-resistant cable, HDPE conduit, tracer wire, warning tape, hardened enclosures, VLANs on separate strands, remote power cycling. Industry: vineyards/farms, estates and rental houses, marinas, business parks (Ronkonkoma, Calverton, Westhampton), research campuses, colleges, retail. Geographic: Suffolk County, ten towns, Ronkonkoma, Islip/MacArthur, Calverton/EPCAL, Riverhead, Westhampton/Gabreski, Upton, Selden, Brentwood, Lindenhurst/Babylon/Amityville, Fire Island, North Fork, South Fork, Shelter Island.

### Question register additions
fiber-optic-installation-suffolk-county
§9 Questions Answered (and other question headings):
- Fiber Link Down Somewhere in Suffolk? (repair capture heading)
- Our land is inside the Central Pine Barrens — can a fiber trench still be dug?
- How is buried fiber kept away from plows, trellis posts and drainage on land we farm?
- How does a fiber trench get past a septic tank, leaching pools and a private well?
- Does Suffolk's sandy ground make a fiber trench easier or harder?
- Do mice, voles or other burrowing animals chew buried fiber, and how is it protected?
- How long can one fiber run across a big property be before it needs a splice or electronics partway?
- The house is empty from fall until late spring — how does the link between buildings stay healthy with nobody there?
- Guests change every week all summer — how do we stop them unplugging or resetting the network out at the pool house?
- Our marina's gates, fuel dock and boat sheds sit on ground that floods — how does fiber reach them without the connections ending up underwater?
- Does fiber work on a Suffolk property need a permit from the town, the village or the county?
- Cameras Dark at the Far Building Today? (final repair heading)
§17 FAQ:
- Can you take on jobs that need a ferry, such as Shelter Island?
- How can I tell whether a cable in my yard or basement is fiber, coax or old phone wire?
- Who puts the lawn, irrigation and plantings back after a fiber trench?
- Can your crew work under a research or industrial site's own safety and badge rules?
- Can you look at a property before we close on it?
- What happens to the fiber records if we sell the property?
- Will a fiber trench interfere with our dog's buried electric fence?
- Is there a charge for a site walk on the North or South Fork?
De-dup notes: intents checked against the full register (NYC, Manhattan, Brooklyn, LI hub, HV hub) and against the in-progress batch siblings (Nassau, Staten Island). Dropped or re-angled because a sibling owns the intent: neighbours sharing a link (Nassau), testing another company's fiber (Nassau), owner/guest network separation (Nassau shop/apartments → re-angled to guest tampering), raised-house flood equipment placement (Staten Island → re-angled to marina facilities that cannot be raised), county licence question (Nassau → re-angled to permits), second provider/diverse path (Manhattan), provider arriving soon (HV), gatehouse/outbuilding worth it (LI), boathouse/dock (HV), seasonal scheduling and owner-on-site (HV), area pricing (LI), shared trench (LI), frost (HV), one feed for many units (Brooklyn).

### Build checks (this builder)
check_page --no-registration: only "live sibling X doesn't link back" lines remain (NYC, Manhattan, Brooklyn, LI, HV — main-run wiring). Full run adds sitemap, _redirects and hub-link-down lines. 12,491 rendered words; 181,034 bytes (≥3.1 KB from every fiber sibling incl. Nassau 204,444 / SI 202,088 at time of check). Masked block similarity max 0.620 (Staten Island), Brooklyn 0.608, NYC 0.599, Nassau 0.595 (difflib on geo-masked p/li/td/h3/figcaption blocks ≥12 words; stamp/warranty/consent/NAP excluded).

### Question register additions (final, as shipped — main run 2026-10-17)
fiber-optic-installation-suffolk-county
§9 Questions Answered:
- Our land is inside the Central Pine Barrens — can a fiber trench still be dug?
- How is buried fiber kept away from plows, trellis posts and drainage on land we farm?
- How does a fiber trench get past a septic tank, leaching pools and a private well?
- Does Suffolk's sandy ground make a fiber trench easier or harder?
- Do mice, voles or other burrowing animals chew buried fiber, and how is it protected?
- How long can one fiber run across a big property be before it needs a splice or electronics partway?
- The house is empty from fall until late spring — how does the link between buildings stay healthy with nobody there?
- Guests change every week all summer — how do we stop them unplugging or resetting the network out at the pool house?
- Our marina’s gates, fuel dock and boat sheds sit on ground that floods — how does fiber reach them without the connections ending up underwater?
- Does fiber work on a Suffolk property need a permit from the town, the village or the county?
§17 FAQ:
- Can you take on jobs that need a ferry, such as Shelter Island?
- How can I tell whether a cable in my yard or basement is fiber, coax or old phone wire?
- Who puts the lawn, irrigation and plantings back after a fiber trench?
- Can your crew work under a research or industrial site's own safety and badge rules?
- Can fiber serve a greenhouse where the air stays hot and humid?
- What happens to the fiber records if we sell the property?
- Will a fiber trench interfere with our dog's buried electric fence?
- Is there a charge for a site walk on the North or South Fork?

Main-run de-dup notes (2026-10-17 batch staten-island/nassau/suffolk): replaced after collisions with pages shipped concurrently — Nassau "1990s multimode" (Queens/Rockland), "shop and apartments share one cable" (Queens), "payment handled" (Bronx deposit), "asbestos in older building" (Westchester/Bronx); Suffolk "look at a property before closing" (Bronx audit before buy/lease, Rockland pre-close test). Several captions/paragraphs rewritten to keep masked similarity < 0.65 vs Queens/Bronx/Westchester/Rockland/Orange.


## Putnam County — local research (2026-10-17 batch, fiber-optic-installation-putnam-county)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources and the HV hub section are reused where noted. Page thesis: in Putnam the fiber problem is land and licence — trees (two-thirds forest), Highlands rock (9/10 of land), NYC watershed (3/4 of county) and a county-level low-voltage licence that names fiber optics — on a building stock that is ~80% detached houses with outbuildings, plus small Route 6/22/312 commercial sites and civic buildings.

### County profile (primary source)
- `Putnam County New York percent of county in New York City watershed reservoirs Croton` · Firecrawl search → https://www.putnamcountyny.gov/images/Departments/Emergency_Services/mitigation/Section-4-County-Profile-021815.pdf (Firecrawl scrape/query): >240 sq mi; six towns (Carmel, Kent, Patterson, Philipstown, Putnam Valley, Southeast) + villages Brewster, Cold Spring, Nelsonville; ~three-quarters in NYC watershed; >nine-tenths Hudson Highlands, gneiss/schist/granite; forest 67.9% (2006) / 66.9% (2011); 79.2% single-family detached (30,215 units, 2012 ACS); reservoirs Bog Brook 4.4, Croton Falls 14.2, Diverting 0.9, East Branch 5.2, Middle Branch 4.1, Boyds Corner 1.7, West Branch 8 billion gal (sum ≈38.5); rail stops Brewster, Brewster North, Patterson, Cold Spring, Garrison, Breakneck Ridge, Manitou; one hospital in Carmel; 2,829 establishments / 20,519 employees; lakes list incl. Lake Mahopac, Lake Carmel, Lake Gleneida, Putnam Lake, Lake Peekskill, Oscawana Lake, Roaring Brook. → §5 paras 1–2 + facts list; §7 lake-community card; §8 intro; §13 Croton Falls & Brewster cards; Town by Town; hero subhead.
- Note: page calls Brewster North the "Southeast Metro-North station" (renamed; builder's knowledge, not from the PDF) — flag if a citation is wanted.

### Licensing / permits
- `Putnam County Department of Consumer Affairs home improvement license electrician license requirement` · Firecrawl search → https://www.putnamcountyny.gov/consumer-affairs (scrape/query): licenses Master, Special & Reciprocal Electricians, "Limited Data Communication Technicians", Journeymen, Helpers; publishes "List of Licensed Low Voltage Technicians (as of August 11, 2026)"; "Electrical permit applications for locations in the Towns of Carmel, Patterson, and Putnam Valley must be filed directly with those Building Departments." → §8.5 callouts 1–3; §9 Q1, Q3; Town by Town (Carmel, Patterson, Putnam Valley).
- Same search → https://ecode360.com/6607815 (Chapter 145 Electricians, scrape/query): low-voltage/limited-data communications technician = 8,000 hours + exam; covers computer networking, telecom, CATV, intercom, A/V, fiber optics, video surveillance, ≤90 V and ≤5 A, "where such work commences at an outlet receptacle or connection previously installed by a person holding the proper electrical license"; master electrician qualifies; no one may carry on the trade in the county unless licensed/registered; exemptions incl. utilities and telecom companies up to demarcation; continuing education from 2019. → §5 para 4; §8.5; §9 Q1–Q2; §10.5 H3 1; FAQ "electrician/generator".
- Same search → https://adaptdigitalsolutions.com/articles/new-york-contractor-license-requirements/ (excerpt; title "New York Contractor License Requirements: None Statewide") → §10.5 H3 1 (quoted claim).
- NOT claimed on page: that AESS holds a Putnam county low-voltage licence (not verified) — page tells owners to ask installers, "including us", and to check the county list. FOR ANWAR TO CONFIRM.

### Watershed / stormwater / City land
- `NYC DEP watershed regulations stormwater pollution prevention plan land disturbance threshold square feet East of Hudson Putnam` · Firecrawl search → https://www.townofkentny.gov/DocumentCenter/View/2280/Stormwater-Management-Plan (scrape/query): ≥1 acre generally, ≥5,000 sq ft in East of Hudson watershed; Town of Kent reviews SWPPPs. → §8.5 callout 4; §9 Q4; Town by Town (Kent).
- Same search → https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-27250 (excerpt: NYC Ch. 19.1 "covered development project" 20,000 sq ft / 5,000 sq ft impervious — NYC sewer-system rule) → NOT used (NYC-only).
- `NYC DEP land use permit crossing City-owned watershed land utility cable Putnam` · Firecrawl search → https://www.nyc.gov/site/dep/environment/opportunities-on-city-lands.page (excerpt: "Land Use Permits to applicants who request the temporary use of City-owned water-supply lands for specific proposed activities") → §8.5 callout 5; §9 Q5.
- https://www.nyc.gov/site/dep/water/diverting-reservoir.page (excerpt: Diverting connected to Croton Falls via channel and dividing weir) → §13 Croton Falls card.
- `NYC DEP owns acres of land in Putnam County` · Firecrawl → only Kensico (Westchester) purchase news. EMPTY for Putnam acreage (no figure on page).

### Weather / outages
- Lightning: HV hub source reused (Earth Networks 2020: Putnam 75,093 pulses, 35 thunder days) → §5 facts; Storm Season section.
- `Putnam County power outages storm NYSEG Central Hudson percent customers without power trees` · Firecrawl search → https://www.lohud.com/story/weather/2018/03/05/storm-monday-power-outage/394304002/ (search excerpt: "NYSEG: 18,525 customers without power in Putnam County"; scrape returned page metadata only, figure not in scraped body) → §5 facts; §10.5 H3 3. Stated as the Journal News's March 5, 2018 report.

### Providers / broadband
- `Highlands Current Philipstown internet broadband fiber Garrison Optimum Verizon` · Firecrawl → https://highlandscurrent.org/2023/05/05/fiber-optic-coming-to-highlands/ (scrape/query, May 5 2023): Optimum installing fiber throughout Philipstown (up to 5 Gbps, later 8); Verizon building in Beacon; Verizon "reviewing a FiOS build in Cold Spring but cannot commit to a timeframe." → §10.5 H3 2; Town by Town (Philipstown).
- Same search → https://broadbandnow.com/New-York/Garrison (excerpt: Verizon Fios "covers 40.5% of the area") → §10.5 H3 2 (quoted as aggregator claim).
- `reddit Putnam Valley OR Patterson OR Kent NY internet options home office slow` · Firecrawl → https://broadbandnow.com/New-York/Putnam-Valley (search content): "most widely available internet in Putnam-Valley … is EarthLink Fiber"; Viasat "spans 100.0%"; Mint Mobile 5G "57.6%". → §10.5 H3 2 (aggregator claims, shown as contradictory).
- `Putnam County NY broadband fiber expansion 2025 unserved homes Philipstown Putnam Valley` · Firecrawl → no Putnam-specific programme found (Sullivan/Madison/WV results). EMPTY.
- Optimum Mahopac page (excerpt: "speeds up to 8 Gig in Mahopac") → not used (marketing).

### Landmarks / corridors
- `Putnam County Historic Courthouse Carmel built 1814` · Firecrawl → https://en.wikipedia.org/wiki/Putnam_County_Courthouse_(New_York) (excerpt: built 1814, renovated 1847, hamlet of Carmel, county seat); https://www.hmdb.org/m.asp?m=37288 (excerpt: "second oldest working court house") → §13 card ("one of the oldest working courthouses in the state"); Civic section; §5 para 3.
- `Tilly Foster Farm Brewster county-owned acres buildings` · Firecrawl → https://www.putnamcountyny.gov/images/Departments/Legislature/Meetings/2022/August/minutes/Phys-08-25-22-Presentation-Tilly-Foster-Overview-2022.pdf (excerpt: county-owned, ~199 acres, Town of Southeast, originally dairy); https://www.tpl.org/media-room/tilly-foster-farm-protected-environmental-resource (excerpt: dairy and thoroughbred farm) → §13 card; Town by Town (Southeast).
- `Putnam Hospital Carmel NY beds Stoneleigh Avenue Nuvance Northwell` · Firecrawl → https://www.northwell.edu/locations/putnam-hospital (excerpt: 670 Stoneleigh Avenue, Carmel) → §8 card; §13 card. Bed count: EMPTY (not stated).
- `Clarence Fahnestock Memorial State Park acres` · Firecrawl → https://parks.ny.gov/visit/state-parks/fahnestock-state-park-clarence-fahnestock (excerpt: 15,000-acre park in Putnam and Dutchess); reserveamerica excerpt (Route 301) → §13 card.
- `Mt Ebo Corporate Center Brewster Southeast NY office park Route 312` · Firecrawl → https://southeast-ny.gov/DocumentCenter/View/2436/1b (excerpt: Route 312, "3-story, 50,000 sq. ft. medical facility"); https://www.c21alliancegroup.com/... (excerpt: 15 Mount Ebo Road S, office/medical/educational space); brewsterchamber.com (excerpt: 16 Mount Ebo Road South address) → §8 card 1; §9 Q10; Typical Designs #3.
- `Putnam County Brewster Carmel Route 6 22 business corridor` (HV hub run) → EMPTY; corridor cards for Route 6/22/52/311/Route 9 describe road names only (from county profile road list), no business facts claimed.

### Reddit / PAA / PASF / ATP / AI Overview / Bing & DDG / Yelp
- `reddit Putnam County NY internet Optimum only fiber Mahopac Carmel` · Firecrawl → only r/longisland, r/OPTIMUM, r/Rockland, r/Westchester threads; no Putnam thread. Reddit (Putnam): EMPTY.
- PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp: EMPTY (not accessible in build env). §10.5 uses published claims instead: adaptdigitalsolutions (H3 1), BroadbandNow (H3 2), unio.digital aerial $8–$12/ft and trenching $15–$35/ft, boring $20–$30/ft, drop $300–$800 (silo/HV source; H3 3–5), thenetworkinstallers FBA 2025 $18.00/ft median (silo; H3 4), T-Mobile "up to 4 hours" (silo; H3 6), Central Hudson/Dig Safely NY 811 2–10 days, utilities mark their lines (HV source; H3 7, §8.5 callout 6).

### Pricing used (blueprint §9, Putnam 1.45× — HV hub table row, no new prices)
$51 termination · $58 OTDR/strand · $508 MM drop · $580 SM drop · $6,525–$10,150 12-strand OM4 · $11,600–$21,750+ 24-strand OS2 · from $3,480 second room · Starter $1,920 (24×$51 + 12×$58) · $195/hr 3-hr min ($585) protected.
DISCREPANCY (already logged by HV hub): structured-cabling-pricing-putnam-county configurator shows fiber drops $494 / $564.

### Images (11) — permanent image rule, pool = images/network/ sorted lines 1–117
All source photos show staff faces and an 844-386-7238 number on shirts/signs; each was CROPPED so no face and no phone number is in frame (checked visually). Subjects in the pool are all also used on other fiber pages from other source files; least-used subjects (idf bundle, core-drill rough-in, rack before/after) preferred.
| File (images/fiber-optic-installation/) | Source (images/network/) | Crop |
|---|---|---|
| fiber-optic-installation-putnam-county-tester-pass-wall-outlet.webp | network-installation-bronx-fluke-dsx-certification-pass.webp | x0–960 |
| fiber-optic-installation-putnam-county-rack-before-after-rebuild.webp | network-installation-bronx-network-rack-cleanup-before-after.webp | none |
| fiber-optic-installation-putnam-county-emt-sweep-cable-pull.webp | network-installation-bronx-network-drop-conduit-emt-riser.webp | x560–1448 |
| fiber-optic-installation-putnam-county-hammer-drill-block-entry.webp | network-installation-nyc-core-drill-conduit-rough-in.webp | x590–1448 |
| fiber-optic-installation-putnam-county-jhook-bundles-above-grid.webp | network-installation-bronx-jhook-ceiling-pathway-bundles.webp | x500–1448 |
| fiber-optic-installation-putnam-county-tone-probe-panel-trace.webp | network-installation-bronx-network-cable-toner-tracing.webp | x0–800 |
| fiber-optic-installation-putnam-county-sfp-switch-seated-rack.webp | network-installation-bronx-managed-poe-switch-rack-install.webp | x0–840 |
| fiber-optic-installation-putnam-county-patch-cord-label-applied.webp | network-installation-bronx-cable-labeling-port-map.webp | x0–900, y0–860 (cable-map sheet cropped out) |
| fiber-optic-installation-putnam-county-punchdown-panel-hands.webp | network-installation-nyc-patch-panel-punchdown-rack.webp | x815–1448 |
| fiber-optic-installation-putnam-county-bundle-lift-open-ceiling.webp | network-installation-nyc-idf-riser-cable-bundle.webp | x600–1448 |
| fiber-optic-installation-putnam-county-rack-yellow-patch-ups.webp | network-installation-bronx-finished-network-rack-firewall-ups.webp | x0–630 |
DAILY-LOG note: `images: 11 reused from images/network/ (no real fiber-optic-installation photos yet; cropped to remove faces and shirt phone numbers)`. Captions describe copper network gear honestly (no claim the cable shown is fiber).

### Keyword plan (Putnam page)
Service: fiber optic installation Putnam County, house-to-garage fiber, outbuilding fiber, conduit-only, fusion splicing, OTDR testing, provider extension. Problem: cable strung through trees, storm/branch damage, wireless bridge blocked by leaves, rock near surface, tree roots, watershed erosion rules, City reservoir land, shared private lanes, missing outlet at far building. Technology: indoor/outdoor OS2, all-dielectric loose-tube, rodent-resistant jacket, OM4, HDPE conduit, tracer wire, splice enclosures, SFP switches/media converters, UPS. Industry: commuter homes/home offices, lake communities, estates/farms, medical suites, village main streets, town halls/libraries/fire companies/schools. Geographic: Putnam County; Carmel, Mahopac, Southeast, Brewster, Patterson, Kent, Lake Carmel, Putnam Valley, Lake Peekskill, Philipstown, Cold Spring, Nelsonville, Garrison, Putnam Lake; Routes 6, 9, 22, 52, 301, 311, 312; Croton Falls Reservoir; Tilly Foster Farm; Stoneleigh Avenue; Fahnestock.

### Question register additions
fiber-optic-installation-putnam-county
§9 Questions Answered (and other question headings):
- Putnam Fiber Link Cut or Dark? (repair capture heading) (fiber-optic-installation-putnam-county)
- Our house is inside the New York City watershed — does a short fiber trench need a stormwater plan? (fiber-optic-installation-putnam-county)
- Our property backs onto reservoir land owned by New York City — can the cable cross it? (fiber-optic-installation-putnam-county)
- The ground between our buildings slopes down toward a lake or a brook — what keeps a fresh fiber trench from washing out? (fiber-optic-installation-putnam-county)
- The only spot with a clear view of the sky for our satellite dish or wireless antenna is far from the house — can fiber bring that signal in? (fiber-optic-installation-putnam-county)
- Can fiber join a historic main building to a newer annex without changing the old facade? (fiber-optic-installation-putnam-county)
- Branch Down on the Line to the Studio? (final repair heading) (fiber-optic-installation-putnam-county)
(Statement sub-headings, not questions, in the same section: How Putnam's county low-voltage licence works · Where the cabling licence ends and the electrician's work begins · Electrical permits: Carmel, Patterson and Putnam Valley file with the town · Protecting the big oaks and maples between the buildings · Crossing a lake community's private lane · A garage office that holds a video call · A tenant's own path in a shared Route 312 building · Buying a house with a link already in the yard)
§17 FAQ:
- Do you work in the river hamlets of Philipstown as well as the Route 6 towns? (fiber-optic-installation-putnam-county)
- Will our private fiber interfere with the provider's own fiber terminal on the house? (fiber-optic-installation-putnam-county)
- Can a fiber link cross a gravel driveway that gets plowed all winter? (fiber-optic-installation-putnam-county)
- Will any trees have to be cut down or trimmed for the fiber route? (fiber-optic-installation-putnam-county)
- Can you install just the conduit now and pull the fiber later? (fiber-optic-installation-putnam-county)
- Can a fiber link serve a detached workshop full of power tools and sawdust? (fiber-optic-installation-putnam-county)
- Can the trench be dug by hand where a lot is too steep for a machine? (fiber-optic-installation-putnam-county)
- Can fiber reach a gate or camera at the bottom of a long Putnam driveway? (fiber-optic-installation-putnam-county)
- Do we need the property line staked before you dig near it? (fiber-optic-installation-putnam-county)
- Is there anything to do to a fiber link before a big storm is forecast? (fiber-optic-installation-putnam-county)
- Is there a distance below which fiber isn't worth it for an outbuilding? (fiber-optic-installation-putnam-county)
- Can you photograph the open trench for our records before it is backfilled? (fiber-optic-installation-putnam-county)

Second-pass de-dup (vs queens, bronx, staten-island, nassau, suffolk, westchester, rockland, orange): turned into statement headings — county licence (≈ Orange "Does Orange County's electrician licence apply…"), electrician outlet (≈ Bronx "Do we need an electrician as well as you?", Orange/SI outlet questions), permit office (≈ Suffolk town/village/county permit), tree roots (≈ SI mature tree), lake lane permission (≈ SI shared driveway), garage home office (≈ Nassau home business), tenant suite path (≈ Orange former-hospital suite, Queens tenant service), buying a house with a link (≈ Rockland/Bronx pre-purchase test/audit). Replaced FAQs — landline/alarm (≈ Queens phone system), guest-apartment network (≈ Nassau separate network), rodents (≈ Suffolk/Bronx rodents), neighbour sharing (≈ Rockland Ramapo houses), electrician/generator (≈ Bronx electrician), separate internet account (≈ Orange second building). Added Q: slope washout toward lake/brook.
### Second-pass additions (main-run request, 2026-10-17)
- New visible section "Seven Reservoirs, Dozens of Lakes and Two Rail Lines" — sources: county profile PDF (reservoir capacities, lake list, Harlem/Hudson line stops) already logged above; no new facts.
- JSON-LD enriched only with content visible on the page: areaServed towns (Town-by-Town text) and hamlets named; WebPage.mentions = landmark and corridor cards; OfferCatalog = full Putnam price table + 3 packages + $195/hr service rate; HowTo supplies, step images (page figures) and directions.
- Result: 225,478 bytes, 13,939 words; full check_page PASS; max masked paragraph similarity 0.59 (hudson-valley / ulster-county) across all 15 fiber siblings.

De-dup notes: avoided register intents already used — utility poles, shared trench, power-outage campus, frost/ledge rock, stream crossing, boathouse, stone-wall route, old copper disposal, finding buried fiber, public-job paperwork, new subdivision house, second-home presence, area-pricing, cutover downtime, duration. Masked word-level paragraph similarity vs every fiber page (incl. new Dutchess/Ulster drafts): max 0.59 (HV hub), page-level ≤0.13.


## Dutchess County — local research (2026-10-17 batch, fiber-optic-installation-dutchess-county)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "FC search" = mcp__Fire_Crawl__firecrawl_search (excerpts only); "FC scrape" = mcp__Fire_Crawl__firecrawl_scrape (directQuote query mode). Silo-wide sources in research/fiber-optic-installation.md reused where noted.

Thesis: Dutchess fiber is *inherited* fiber. IBM-era single-owner campuses (Poughkeepsie, East Fishkill → iPark 84) are now multi-tenant; Fishkill Creek mills and the Nabisco plant (Dia Beacon) have been converted; hospitals/colleges grew in layers. Jobs = audit legacy glass (OM1 reach limits, ST connectors, abandoned cable), tenant separation on re-let campuses, exposed-route mill backbones, new-wing tie-ins, last-hundred-feet from new BEAD fiber. Deliberately distinct from the HV hub (distance / ground potential / lightning between scattered buildings) — no lightning, frost, barns or stream crossings on this page.

### Reddit (local)
- `reddit Poughkeepsie fiber internet Beacon Fios Optimum Spectrum only` · FC search → https://www.reddit.com/r/hudsonvalley/comments/qh9rat/who_has_the_best_high_speed_internet_in_the/ (excerpt "Verizon Fios is the best, Spectrum is...") → not used (opinion).
- `site:reddit.com Poughkeepsie OR Beacon OR Fishkill OR Rhinebeck fiber internet Verizon not available` · FC search →
  - https://www.reddit.com/r/hudsonvalley/comments/1g3u51x/verizon_fios_down/ (excerpt: "FiOS unavailable at my address, but available directly behind me and across the street.") → §10.5 H3 1.
  - https://www.reddit.com/r/hudsonvalley/comments/cgv6gr/moving_to_beacon_next_month_any_recommendations/ (excerpt: "When I lived in Beacon, … I lived in a corner of town without fiberoptic service.") → §10.5 H3 1.
  (Threads not opened; Firecrawl excerpts only.)

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Angi / HomeAdvisor / Fixr fiber cost pages: EMPTY (not retrieved; page says so). §10.5 substitutes, quoted as published:
- https://broadbandnow.com/New-York/Poughkeepsie (FC search excerpt, same query as Reddit above): "Fiber internet is 83.3% available in Poughkeepsie." → §10.5 H3 1.
- Silo: streamlinetelecom.com "$1-6 per linear foot"; lowvoltagenewyork.com ($1–$6 indoor; "singlemode glass is now cheaper than OM4"; SM optics "roughly 1.5–5×"; "Plenum rating adds 15–25%") → §10.5 H3 2, 4, 7.
- `OM1 62.5 micron multimode fiber 10GBASE-SR maximum distance 33 meters 1000BASE-SX 275 meters` · FC search → https://www.hello-signal.com/is-om1-fiber-obsolete-speed-distance-wavelength-specs-comparison/ (excerpt: "Can I run 10G on OM1 fiber? A: Only up to 33 meters with 10GBASE-SR. Beyond that, links fail.") → §10.5 H3 3; https://www.fiber-mart.com/news/understanding-distance-limits-with-multimode-fiber-a-6008.html (excerpt: OM1 275 m 1000BASE-SX, 33 m 10GBASE-SR) → "Reading the fiber" section table, §9 OM1 Q; https://blog.fluxlight.com/2017/05/25/... (33 m ≈108 ft) → corroboration.
- Silo: unio.digital "$300 to $800 per fiber drop" → §10.5 H3 5; T-Mobile "can take up to 4 hours" → §10.5 H3 6; ampcom OM3/OM4 ~300/400 m at 10G → table.

### Building stock, campuses, landmarks
- `iPark 84 East Fishkill former IBM campus Hopewell Junction tenants square feet` · FC search →
  - http://ipark84.com/ (excerpt: "former IBM East Campus … 300-acres … over two million square feet") → recorded; page uses the newer trade-press figure.
  - https://cicbca.org/450m-re-trade-includes-ipark-84-complex-in-dutchess-county/ (FC scrape, published Aug 25–26 2026): Lincoln Property Co./Waterfall Asset Management/Saber-Hightower JV acquired portfolio incl. iPark 84 from National Resources for $450M; "270-acre business park comprising approximately 1.8 million square feet originally built for IBM's flagship semiconductor manufacturing plant"; tenants "IBM and Samsung subsidiary eMagin, as well as agricultural firm Cal-Maine"; room for 1.5M+ sq ft more. → §5 para 2, facts list, §8 card, §13 card, WebPage schema.
  - https://extapps.dec.ny.gov/data/DecDocs/314054/Report.HW.314054.2025-07-31.IAQ%20Testing%20Plan%20B220(B310).pdf (excerpt): B220 owned by iPark East Fishkill LLC; OGS leasing ~305,000 sq ft as warehouse. → §5 para 2.
- `IBM Poughkeepsie z17 mainframe built Poughkeepsie plant 2025` · FC search → https://clui.org/ludb/site/ibm-poughkeepsie (FC scrape): main plant begun 1948, wings 1952; "more than fifty buildings on 423 acres"; East Fishkill made semiconductors Poughkeepsie assembled; "many of the buildings are unused"; employment now <3,000. → §5 para 1–2, facts, §13 card. https://www.facebook.com/PoughkeepsieJournal/posts/... (excerpt: "IBM's Poughkeepsie site is where the z16 mainframe is tested and manufactured") → §8 card, §13 card ("still tests and builds its mainframes").
- IBM head count 30,700 (1985) → 13,800 (1993): https://www.latimes.com/archives/la-xpm-1993-09-06-mn-32215-story.html — REUSED from research/soundbar-installation.md Dutchess section (search excerpt, not re-fetched this run). → §5 para 2, facts.
- `Vassar Brothers Medical Center new patient pavilion opened 2021 square feet Poughkeepsie` · FC search → https://www.walshgroup.com/news/2021/walshconsiglicompletes545millionpatientpavilionatvassarbrothersmedicalcenter.html (excerpt: 752,610 sq ft; ED opened Jan 9 2021, rest Jan 11); WAMC excerpt "752,000 square-foot, eight-level addition". → §5 para 4, facts, §13 card.
- `Dia Beacon former Nabisco box printing factory 1929 square feet Beacon NY` · FC search → https://diaart.org/about/press/dia-art-foundation-opens-new-museum-to-house-renowned-collection (excerpt: three buildings and a train shed, nearly 300,000 sq ft, built 1929 for Nabisco, donated 1999 by International Paper). → §5 para 3, facts, §13 card.
- `Beacon NY former factory mill converted lofts Matteawan Groveville Mill Roundhouse Fishkill Creek` · FC search + FC scrape https://www.loftsatbeacon.com/about/history.html: Groveville Carpet Mill employed 700+ in the 1880s, closed on the eve of the Panic of 1893 and relocated to Yonkers; owners bought 2012; hydroelectric dam "tallest on Fishkill Creek"; management building now Beacon Lofts & Storage with gallery/community space; 18 Front Street. → §5 para 3, §13 card. Roundhouse excerpts (https://www.roundhousebeacon.com/about/, Archello "9,000 square foot mill building") → background only ("a hotel and event spaces" in §7 card).
- `Marist College IBM partnership data center Hancock Center Poughkeepsie campus` · FC search + FC scrape https://www.marist.edu/data-center-operations: data centre "in the lower part of Donnelly Hall … the primary hub for the campus computer network"; institution now "Marist University". → §5 para 4, "we also cover".
- `Bard College Annandale-on-Hudson campus acres buildings historic estates Blithewood Montgomery Place` · FC search → https://en.wikipedia.org/wiki/Bard_College (excerpt: 70+ buildings; Montgomery Place 380 acres bought Jan 2016, mansion + ~20 smaller buildings; 260 acres Barrytown bought late 2023); https://www.bard.edu/montgomeryplace/ (380+ acre site, mansion, houses, cottages, barns; Livingston family 1805–1986). → §5 para 4 ("absorbed two historic estates in a decade"), §7 colleges card, §13 card.
- `Culinary Institute of America Hyde Park campus acres former St. Andrew-on-Hudson Jesuit Roth Hall` · FC search → https://www.ciachef.edu/cia-new-york/ ("170-acre riverside main campus"); Wikipedia says 70 acres — CONFLICT, no acreage used; https://www.ciachef.edu/blog/ghost-hunters-... (Roth Hall = former St. Andrew-on-Hudson Jesuit seminary; moved 1972) → "we also cover" line only.
- `Fishkill office park Westage Business Center Route 9 I-84 office building square feet` · FC search → https://www.bottiniproperties.com/commercial-dynamic/300-westage-llc (excerpt: 4-story, 122,038 SF Class A at Route 9 and I-84). → §7 Route 9 card, §8 Fishkill card.
- `Metro-North Hudson Line Harlem Line stations Dutchess County …` · FC search → https://destinationdutchess.com/listingsv/metro-north-railroad (excerpt: Hudson Line Beacon, New Hamburg, Poughkeepsie; Harlem Line Wassaic, Tenmile River …); https://en.wikipedia.org/wiki/Harlem_Line (excerpt: Wassaic "northernmost station in the system"). → §8 northern/eastern card, §9 railroad Q.

### Broadband / providers / local news
- `Dutchess County broadband fiber expansion 2025 2026 unserved ConnectALL` · FC search + FC scrape https://www.governor.ny.gov/news/governor-hochul-us-senators-schumer-and-gillibrand-and-us-representative-tonko-announce-more (April 27, 2026): $542M BEAD implementation; "$11,437,665 to Reasnor Telephone Company, LLC … to serve 795 locations in Dutchess County"; "$23,728,734 to Archtop Fiber, LLC … 1,638 locations in four counties (Columbia, Dutchess, Orange and Sullivan)". → §5 para 6, facts, §6 provider card.
- `Poughkeepsie Journal fiber optic network installed Dutchess 2026 town fiber line Central Hudson` · FC search + FC scrape (pdf) https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7BEC2DC9E8-D582-4406-95A4-39BAEE6C61DD%7D: Dutchess County Central Labor Council resolution (undated in filed copy): "Verizon is refusing to complete and expand the installation of its fiber-optic cable in remaining portions of Dutchess County…". → §5 para 6 ("years earlier" — date not stated on page).
  - Same search: westfaironline Archtop Kingston (Ulster — left for the Ulster page); cityofpoughkeepsie.gov newsflash on July 4 2026 storm restoration → not used.
- Local news (Poughkeepsie Journal / Mid-Hudson News / Highlands Current) on fiber installation contractors: EMPTY.

### Licensing / permits / code
- https://www.dutchessny.gov/Departments/Aging/Docs/OFA-Aging-News-May-11-2026.pdf (FC scrape, pdf; first found in soundbar research, re-verified this run): "New York State does not license home improvement contractors. Check with your town, city, and/or village government as to what licensing and permits may be required…" → §8.5 bullet 1.
- `Dutchess County Department of Public Works highway work permit utility installation county road right-of-way` · FC search → https://www.dutchessny.gov/Departments/Public-Works/Public-Works-Forms.htm (excerpt: Highway Work Permit Application "whenever work is being performed within the County right-of-way"); https://www.dutchessny.gov/Departments/Public-Works/Policies-Applications.htm (excerpt: permit review covers "access and utility construction work on County highways"; FC scrape returned no body text). https://www.dot.ny.gov/divisions/operating/oom/transportation-systems/traffic-operations-section/highway-permits (excerpt: "Beginning in September 2025 … apply online through the PermiTrack HWP System"). → §8.5 bullets 2–3, §9 road-crossing Q.
- `NEC 770.25 abandoned optical fiber cables accessible portion shall be removed` · FC search → https://www.mikeholt.com/newsletters.php?action=display&letterID=219 (excerpt: remove accessible portion of optical fiber cable not terminated and not tagged for future use); Quizlet NEC 770 excerpt corroborates. → §8.5 bullet 5, §9 unlabelled-cable Q, cutover section.
- 811 one-call: stated generically (silo/HV hub sources: cenhud Dig Safely). Asbestos caution: general practice statement, no statistic or rule cited. Railroad-crossing: general statement that railroad agreement is needed; no MTA source retrieved — EMPTY for a specific MTA permit process.
- Jacket colour conventions (orange OM1/OM2, aqua OM3/OM4, violet OM4 sometimes, yellow single-mode) and ST/SC/LC connector history: stated as industry convention, no source fetched — flag for review if a citation is wanted.

### Pricing used (blueprint §9 / HV-hub table, Dutchess 1.53× row only — no new prices)
$54 termination · $61 OTDR/strand · $536 MM drop · $612 SM drop · $6,885–$10,710 12-strand OM4 · $12,240–$22,950+ 24-strand OS2 · from $3,672 second room · $195/hr 3-hr min ($585). Worked sums: 12 × $61 = $732; 24 × $54 = $1,296; Starter $2,028 (= hub's D/U starter).

### Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected
Every photo viewed; photos showing the 800-486-0943 number on a shirt (several dutchess-county/hudson-valley files incl. 05 fusion splice, 08 tone generator, 10 AP lift, hero rack-switch, splice tray, van) were skipped.
| images/fiber-optic-installation/ | source (images/low-voltage/) |
|---|---|
| fiber-optic-installation-dutchess-county-idf-rack-patch-cord-dressing.webp | low-voltage-installation-hudson-valley-hero-idf-rack.jpg |
| fiber-optic-installation-dutchess-county-crew-reel-pull-open-floor.webp | low-voltage-installation-dutchess-county-03-crew-cable-pull.jpg |
| fiber-optic-installation-dutchess-county-high-bay-tray-lift-work.webp | low-voltage-installation-dutchess-county-09-warehouse-cable-tray.jpg |
| fiber-optic-installation-dutchess-county-stud-wall-rough-in-crew.webp | low-voltage-installation-hudson-valley-02-metal-stud-rough-in.jpg |
| fiber-optic-installation-dutchess-county-jhook-bundle-open-office.webp | low-voltage-installation-dutchess-county-14-jhook-pathway-bundle.jpg |
| fiber-optic-installation-dutchess-county-handheld-tester-wall-jack-pass.webp | low-voltage-installation-dutchess-county-02-fluke-certification-pass.jpg |
| fiber-optic-installation-dutchess-county-patch-panel-punchdown-closeup.webp | low-voltage-installation-hudson-valley-07-cat6-patch-panel-punchdown.jpg |
| fiber-optic-installation-dutchess-county-corridor-ceiling-cable-feed.webp | low-voltage-installation-long-island-02-school-ceiling-pathway.jpg |
| fiber-optic-installation-dutchess-county-ceiling-grid-cable-feed.webp | low-voltage-installation-dutchess-county-07-ceiling-grid-bundle-pull.jpg |
| fiber-optic-installation-dutchess-county-wall-plate-termination.webp | low-voltage-installation-dutchess-county-06-keystone-wall-plate.jpg |
| fiber-optic-installation-dutchess-county-ceiling-access-point-drop.webp | low-voltage-installation-hudson-valley-06-ceiling-access-point-drop.jpg |
Overlap note: crew pull, high-bay tray, metal stud, ceiling grid, patch-panel punchdown and ceiling AP are the same scenes as images on the HV hub (different source files). Library photos look AI-generated (for Anwar to review).

### Keyword plan (Dutchess page)
Service: fiber optic installation Dutchess County, fiber backbone, existing fiber audit, OTDR testing, fusion splicing, re-termination, abandoned cable removal. Problem: OM1 10G reach, ST connectors, unlabelled cable, landlord-owned campus fiber, tenant separation, spin-off, new wing tie-in, special-construction charges, railroad/county-road crossing. Technology: OS2, OM4, OM1/OM2, LC/ST/SC, interlocking armour, OFNR/OFNP, splice enclosures, optics/media converters. Industry: re-tenanted corporate campuses, mills/lofts, Route 9 offices, hospitals, colleges, Main Street mixed-use. Geographic: Dutchess County, Poughkeepsie, Beacon, Fishkill, East Fishkill/Hopewell Junction, Wappinger, Hyde Park, Rhinebeck, Red Hook, Annandale-on-Hudson, Millbrook, Pawling, Amenia, Wassaic.

### Question register additions
fiber-optic-installation-dutchess-county
§9 Questions Answered (and other question headings):
- Dutchess Backbone Down Since This Morning? (fiber-optic-installation-dutchess-county)
- What can an OTDR trace show about an old cable that a simple light test cannot? (fiber-optic-installation-dutchess-county)
- Do long-reach multimode optics make sense instead of pulling new cable past an OM1 riser? (fiber-optic-installation-dutchess-county)
- Our old fiber uses round ST connectors — do we have to replace the cable to use modern switches? (fiber-optic-installation-dutchess-county)
- Our backbone dates from the 1990s — which parts of it have actually aged, and which are still fine? (fiber-optic-installation-dutchess-county)
- Our 62.5-micron and 50-micron cables end up in the same rack — does it matter if someone patches one to the other? (fiber-optic-installation-dutchess-county)
- A fire-alarm or building-control network still runs on the old campus fiber to our building — can we take the building over without disturbing it? (fiber-optic-installation-dutchess-county)
- Our lab tenant on a former semiconductor campus needs fiber into a cleanroom — what changes inside a controlled environment? (fiber-optic-installation-dutchess-county)
- Can old line-shaft openings or freight-chute shafts in a mill carry new fiber between floors? (fiber-optic-installation-dutchess-county)
- How does fiber travel through a converted mill where every floor is open timber and nothing can be hidden? (fiber-optic-installation-dutchess-county)
- How does a hospital or school keep a new wing connected if the one link back to the old building is cut? (fiber-optic-installation-dutchess-county)
- A provider has quoted us special-construction charges to reach our building — what part of that work can we do ourselves? (fiber-optic-installation-dutchess-county)
- The railroad tracks split our property in two — is there any lawful way to link the halves with our own cable? (fiber-optic-installation-dutchess-county)
- How do ten-gigabit and faster links change the loss budget an old cable has to meet? (fiber-optic-installation-dutchess-county)
- Old Fiber Failing in Your Dutchess Building Today? (fiber-optic-installation-dutchess-county)
§17 FAQ:
- Do you cover the Harlem Valley towns as well as the river towns? (fiber-optic-installation-dutchess-county)
- How long does an audit of existing fiber take in a typical office building? (fiber-optic-installation-dutchess-county)
- Will you give us the audit report even if we decide not to hire you for the upgrade? (fiber-optic-installation-dutchess-county)
- Can the audit results go straight to our landlord or campus IT office? (fiber-optic-installation-dutchess-county)
- Can old multimode and new single-mode fiber live in the same building? (fiber-optic-installation-dutchess-county)
- Can a broken strand be found without opening every panel in the building? (fiber-optic-installation-dutchess-county)
- Do you clean and inspect the connectors on links you are keeping but not otherwise touching? (fiber-optic-installation-dutchess-county)
- Can spare strands in an old backbone be given a new job, such as a separate camera or door-control link? (fiber-optic-installation-dutchess-county)
- Can you test fiber that passes through a room we cannot get into? (fiber-optic-installation-dutchess-county)
- Do you haul away the abandoned cable you pull out of ceilings and risers? (fiber-optic-installation-dutchess-county)
- Can you supply patch cords and labels to our own IT standard? (fiber-optic-installation-dutchess-county)
- Are the old test printouts a previous installer left in the telecom room worth keeping? (fiber-optic-installation-dutchess-county)

De-dup notes (revised 2026-10-17 after 8 more fiber pages went LIVE): replaced overlaps with Queens/Rockland (old multimode carrying today's speeds; strands in use; label existing plant; inherited fiber usable), Westchester (tenants sharing a backbone without sharing a network; who owns fiber after sale; repair heading), Rockland (county-road crossing; seller-kept building separation), Queens (mixed-use backbone), Bronx/Rockland (pre-purchase audit), Staten Island/Putnam/Rockland (neighbour permission/easement), Bronx (rodents; asbestos), Suffolk (badge rules). Earlier: avoided Brooklyn campus conduit, HV grant-provider prep and campus department fiber, LI Route 110 move-in, Manhattan landmark and smallest job, NYC termination lifespan and shared sleeve.


## Ulster County — local research (2026-10-17 batch, fiber-optic-installation-ulster-county)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md reused where noted; only Ulster research added here.
**Page thesis:** provider fiber has reached the curb in Ulster (Archtop, Planet Networks, MTC, Spectrum, Verizon BEAD), so Ulster jobs are owner-side work — demarc extensions, dual-provider entrances, risers in reused/old buildings (iPark 87, Kingston's three districts, Lace Mill) and segmented networks for rental/inn/retreat compounds — distinct from the HV hub's outdoor/ground-potential thesis.

### Reddit (local)
- `reddit Kingston NY Ulster County internet fiber Spectrum only Woodstock Saugerties` · Firecrawl web search (excerpts only; reddit threads not opened).
  - https://www.reddit.com/r/hudsonvalley/comments/11tsdnz/archtop_fiber_coming_to_kingston_saugerties/ — "Archtop Fiber is starting to connect homes in Kingston and Saugerties to fiber" → §5 para 1 context; dual-provider Q (overlap of providers).
  - https://www.reddit.com/r/Spectrum/comments/16fifqe/is_there_any_hope_for_fiber_service_in_ulster/ — "Archtop (archtopfiber.com) is deploying to many areas… Planet Networks in Saugerties is another one." → §6 Dual-Provider card; dual-provider Q.
  - https://www.reddit.com/r/hudsonvalley/comments/1d6c7m7/other_internet_service_providers_besides_spectrum/ — "Using Planet Networks in & around the Saugerties/Kingston area. Archtop Fiber is also up & running." → same.
  - https://www.reddit.com/r/hudsonvalley/comments/1unfmxq/kingston_internet_options/ — excerpt on symmetrical gigabit in Saugerties (price) → not used (consumer pricing).
- `fiber internet installation to house long driveway cost who pays drop from road private property provider charges per foot` · Firecrawl → https://www.reddit.com/r/HomeNetworking/comments/1eng3n3/ (excerpt "ISP quoted $10k to run fiber down driveway") → background only, not quoted.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG — EMPTY (not accessible in build env)
Substitutes for §10.5 (claims quoted as published):
- `fiber internet installation … provider charges per foot` · Firecrawl → https://www.gokinetic.com/blog/fiber-internet-cost-guide (Firecrawl query scrape): cites Angi "$1,500 to $7000"; "many providers offer free or discounted installation for a new fiber order… activation fee of roughly $99" → §10.5 H3 6.
- Angi (followed from Kinetic): https://www.angi.com/articles/fiber-optic-cable-installation-cost.htm (Firecrawl directQuote scrape, "[2026 Data]"): "Fiber optic cable installation costs between $1,500 and $7,000"; "$1 to $12 per linear foot"; aerial $1,000–$5,000 / underground $2,000–$10,000; "Aerial installations are less expensive because they require less digging"; "Labor costs can range from $50 to $150 per hour"; "Most fiber optic installations require permits… Permit fees… $50 to $500"; DIY "Materials cost $1 to $3 per linear foot" → §10.5 H3 1–5. (First Angi page retrieved for the silo; earlier pages recorded Angi as EMPTY.)
- Archtop quote in Hudson Valley One (below): "Long gone are the days of frequent outages or spotty connections." → §10.5 H3 7.
- Yelp: `fiber optic cabling contractor Kingston NY Ulster County business fiber installation` · Firecrawl → https://www.yelp.com/search?find_desc=Network+Cabling&find_loc=Kingston%2C+NY+12401 (listing excerpt only, no 1–3★ text) → EMPTY.

### Providers / broadband
- `Ulster County broadband fiber Margaretville Telephone MTC Phoenicia Shandaken fiber 2025 2026` · Firecrawl → https://broadbandnow.com/New-York/Phoenicia (excerpt: MTC fiber plans in Phoenicia); Town of Shandaken FB post on MTC fiber coverage map → §5 para 1, Town-by-town (Shandaken). https://mtctelcom.com/mtc-announces-new-broadband-expansion-projects/ → 404, EMPTY.
- Same search family → https://hudsonvalleyone.com/2024/05/15/spectrum-planet-networks-and-archtop-fiber-explain-their-local-operations/ (Firecrawl scrape, May 16 2024, Crispin Kott): Village of Saugerties renewed 15-yr Spectrum franchise; Planet Networks (Newton NJ) "Our construction uses existing utility poles"; "expanding across the county from Saugerties and Kingston to smaller, underserved communities"; member of Saugerties Chamber; Archtop: HQ in Kingston, "14 MOUs with communities in Ulster County", "In March 2024, we turned on… Kingston area… speeds up to 10 Gig. In April 2024… town and village of Saugerties… official tech partner"; Spectrum: multi-gig "expected… across our entire service area in 2026". → §5 para 1 + facts; §8 Providers section; §9 dual-provider Q; §10.5 H3 2 & 7; Town-by-town.
- `Archtop Fiber Ulster County homes passed …` · Firecrawl → https://archtopfiber.com/blog/2024/10/01/archtop-fiber-begins-construction-on-state-of-the-art-fiber-network-in-woodstock/ (Firecrawl query scrape, Oct 1 2024): construction started in Woodstock; Kingston, Saugerties named → §5 para 1; Town-by-town. https://www.sullivanny.gov/news/new-website-shares-info-map-major-broadband-expansion (excerpt: Archtop Sullivan build "220+ miles… nearly 100% of which will be buried") → Providers section para 2.
- `fiber optic cabling contractor Kingston NY Ulster County business fiber installation` · Firecrawl → https://www.ulstercountyny.gov/Government/News/Newsroom/2026/05/2026-05-01-Federal-Approval-Clears-Way-for-Countywide-Fiber-Optic-Broadband-Buildout-in-Ulster-County (Firecrawl scrape, May 1 2026): BEAD approved; all 1,293 unserved locations to get fiber; Verizon BEAD ISP; $17.3M federal to Ulster + $41.7M Verizon = $59M; 29%/71%; Ulster 31% of Verizon BEAD total across 14 counties; next steps: state contracts, environmental review, disbursement. → hero; §5 para 1; facts list; Providers section last para; Town-by-town. (Hub used the Sept 2025 ConnectALL figure; this page uses the newer May 2026 BEAD figures.)

### Building stock, campuses, landmarks
- `iPark 87 former IBM Kingston Tech City Town of Ulster redevelopment 2025` · Firecrawl →
  - https://www.ulstercountyny.gov/Government/News/Newsroom/2026/02/2026-02-27-UCEDA-iPark-Foreclosure (scrape, Feb 27 2026): UCEDA foreclosure on two West Campus parcels (former Bank of America bldg, 101-899 Enterprise Dr; vacant lot 605-695 Boices Ln); East Campus has Ulster BOCES CTC and Archtop Fiber; county acquired complex by foreclosure 2019; $10M Restore NY grant; East Campus remediation complete. → facts list; §8 iPark card; §9 conduit Q; §13 card.
  - https://spectrumlocalnews.com/nys/hudson-valley/news/2026/02/27/ulster-county-moves-to-foreclose-on-2-ipark-87-west-parcels (excerpt): "200 acres with over 1 million square feet of buildings… Enterprise Drive" → §7 card, facts.
  - https://www.ipark87.com/think-about.html (excerpt): former IBM Kingston facility; 200 acres; >1M sq ft; East Campus four buildings incl. warehouses, manufacturing, a data center, an office building → §7 card.
  - https://www.townofulster.ny.gov/…DSEIS… (excerpt: 128.47-acre East Campus, 880 multifamily units proposed) → NOT used (proposal-stage).
- `Ulster BOCES Career and Technical Center iPark 87 …` · Firecrawl → https://www.ulsterboces.org/…/ulster-boces-cuts-ribbon-on-career-academies-at-ipark-87… (scrape, Oct 20 2025): opened Sept 2025 to >1,400 juniors/seniors; ribbon-cutting Oct 3; Archtop "scaled to 130 employees"; partners SUNY New Paltz, SUNY Ulster. → facts; §8 card; §7 institutions card.
- `IBM Kingston plant history …` · Firecrawl → https://nyheritage.org/collections/kingston-ibm-years (excerpt: main plant dedicated Nov 2 1956 on 200 acres, Town of Ulster); https://omeka.hrvh.org/exhibits/show/kingston-the-ibm-years/ibm-in-kingston-timeline (query scrape: 1954 construction; 1955 typewriter assembly; 1959 >5,000 employees; 1995 closes) → §13 iPark card; §7 card.
- `Hutton Brickyards Kingston …` · Firecrawl → https://www.huttonbrickyards.com/ (excerpt: riverfront hotel + venue, 100 riverfront acres, private cabins, historic mansion); https://careers.waterfordhotelgroup.com/… (excerpt: 132 Lindsley Ave Kingston, 43 rooms) → §5 para 3; §7 hotels card.
- `Mohonk Mountain House acres guest rooms …` · Firecrawl → https://en.wikipedia.org/wiki/Mohonk_Mountain_House (query scrape): 1869; 259 rooms; 1,325 acres; towns New Paltz/Marbletown/Rochester; NRHP + NHL; built 1869–1910 → §7 card; §13 card.
- Kingston: https://en.wikipedia.org/wiki/Kingston,_New_York (query scrape): pop 24,069 (2020); first capital 1777; burned Oct 16 1777; Stockade/Midtown Broadway/Rondout-West Strand NRHP districts; Midtown early-20th-c industries, UPAC, City Hall, Kingston HS, HealthAlliance; Rondout = D&H Canal tidewater terminus, artists' community → §5 para 3; Kingston Up Close section; §13 cards.
- `Kingston Rondout waterfront flooding …` · Firecrawl → https://www.timesunion.com/hudsonvalley/news/article/kingston-waterfront-flooding-grant-19373867.php (query scrape, Mar 29 2024): $1.5M federal DOT to raise East Strand/North Street; frequent tidal flooding; 2022 waterfront plan. https://www.kingston-ny.gov/…East_Strans_Street_Flooding… (excerpt: "redevelopment… hindered by intermittent floodwater inundation") → Kingston Up Close (Rondout); §13 card.
- `Lace Mill Kingston RUPCO …` · Firecrawl → https://rupco.org/property/the-lace-mill/ (excerpt: 55 affordable apartments, artist preference); https://thelacemillarts.com/about-the-lace-mill/ (excerpt: 100+-year-old lace curtain mill); FB post (165 Cornell St) → §5 para 3; Kingston Up Close (Midtown).
- `Kingston Midtown Arts District Broadway UPAC 1927` · Firecrawl → https://www.vividseats.com/… (excerpt: 601 Broadway, Midtown Arts District, restored 1927 theater); https://hudsonvalleyone.com/2017/11/30/renovated-upac-reopens-under-new-ownership/ (excerpt: 1,500 seats, built 1927) → Kingston Up Close; §13 card.
- `HealthAlliance Hospital Mary's Avenue …` · Firecrawl → https://www.wmchealth.org/press-releases/wmchealth-announces-continued-investment-in-healthalliance-hospital (query scrape, Nov 19 2025): new HealthAlliance Hospital at 105 Mary's Ave opened 2022; >32,000 patients/yr; Medical Village next phase; https://www.wmchealth.org/locations/healthalliance-hospital-mary-s-avenue (excerpt: Medical Village on Broadway) → §7 card; §8 card; Kingston Up Close.
- `SUNY New Paltz campus acres …` · Firecrawl → https://www.suny.edu/campuses/newpaltz/ (257 acres); https://www.usnews.com/best-colleges/suny-new-paltz-2846 (6,113 undergrads fall 2025) → §8 card; §13 card; §7 card.
- https://www.ny.gov/counties/ulster (Firecrawl scrape): 1,161 sq mi; founded 1683; pop 182,333 (2023); Catskill Park & Forest Preserve >¼ million acres forever-wild; SUNY Ulster in Stone Ridge; list of city, 20 towns, 3 villages → facts; §8.5; Forest Preserve Q&A section; Town-by-town.
- `Ashokan Reservoir capacity …` · Firecrawl → https://www.nyc.gov/site/dep/water/ashokan-reservoir.page (excerpt: two basins, 122.9B gallons, in service 1915) → facts; §13 card; Forest Preserve section.
- `Tropical Storm Irene 2011 Esopus Creek Phoenicia …` · Firecrawl → http://catskillstreams.org/wp-content/uploads/2018/02/SA_LFA_Report_Final.pdf (excerpt: Irene "extensive flooding and devastation in the upper Esopus Creek watershed") → background only (repair capture mentions "a wet spring in the Esopus valley" generically; no Irene figure on page).

### Short-term rentals / lodging
- `Ulster County short-term rental study …` · Firecrawl → https://comptroller.ulstercountyny.gov/wp-content/uploads/2025/09/FINAL-STR-Report-2025.pdf (PDF query scrape): 942 (2015) → 3,013 avg (2024), +220%; peak Oct 2023 3,310 (3.84%); May 2025 2,827 = 3.28% of 86,178 units; 98% entire homes; town table (Shandaken 267/9.98% [report also cites 261/9.76%], Woodstock 378/8.81%, Gardiner 136/7.96%, Denning 7.64%, Rochester 238/5.61%, Saugerties town 384, Marbletown 4.67%, Olive 4.62%, New Paltz town 4.01%, Kingston city 150 of 11,049, Lloyd/Marlborough/Plattekill/Shawangunk all <2%) → §5 para 4; facts; Q&A (guest network); Hospitality section; Town-by-town. Page says "nearly one in ten" for Shandaken to avoid the 261/267 inconsistency.
- https://www.ulstercountyny.gov/Departments/Finance/Tax-Information/Occupancy-Tax/HotelMotelSTR-Registration (Firecrawl scrape): register within 3 days; no cost; 4% occupancy tax → §8.5 callout 3.
- `Ulster County short-term rental registry … Woodstock …` · Firecrawl → wonderguest.app / str.haus / bnbcalc (secondary excerpts: Woodstock annual permit, 180-day cap) → only "several towns, Woodstock among them, run their own permit systems" used.

### Licensing / permits
- `Ulster County electrical license board low voltage contractor licensing requirement` · Firecrawl → https://ecode360.com/35131702 (Ulster County Code Ch. 185, L.L. 3-2019, amended 10-21-2025; Firecrawl directQuote scrapes): "Electrical work" includes wiring "for… signaling, communication, alarm or data transmission"; no person may engage in the business of electrical work unless licensed or supervised by a licensee; exemptions A–G (appliance sales, elevators, heating repair, manufacturers, public service company employees, homeowners in own single-family home, municipal employees) — no low-voltage/data exemption listed. https://www.wawarsingny.gov/DocumentCenter/View/274/Electrical-Licensing-Board-PDF (PDF scrape): Board at 317 Shamrock Lane, Kingston; Master Electrician license required to obtain building permits for electrical work (L.L. 3 & 8 of 2019), enforced from Jan 1 2022. → facts list; §8.5 callout 1; Q&A licensing section; §10.5 H3 4. Page states fiber itself carries no current and that line-voltage parts are done/permitted by a county-licensed master electrician; whether low-voltage-only work needs a county license is NOT asserted (the law's text is broad; flagged for Anwar's review).
- Town/village building permits for low-voltage work: EMPTY (not researched per town); page says the municipality's building department decides.
- 811: silo/hub source (Central Hudson Dig Safely) reused → §8.5 callout 6, process step 3.

### Local news / hyperlocal
- Hudson Valley One, Times Union, Spectrum News (above). Daily Freeman: https://www.dailyfreeman.com/2025/09/22/ulster-county-short-term-rentals-eating-up-housing-market-comptrollers-report-shows/ (excerpt only) → corroborates STR report, not cited separately. Other Ulster fiber-contractor news: EMPTY.

### Pricing used (blueprint §9, Ulster 1.53× — row copied from research/fiber-optic-installation.md HV table; no new prices)
$54 termination · $61 OTDR/strand · $536 MM drop · $612 SM drop · $6,885–$10,710 12-strand OM4 · $12,240–$22,950+ 24-strand OS2 · from $3,672 second room · Starter (24 term + 12 OTDR) $2,028 · $195/hr 3-hr min ($585) protected. Same discrepancy as hub note: live structured-cabling-pricing-ulster-county configurator shows $535/$611 drops; this page follows §9.

### Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected
| File (images/fiber-optic-installation/) | Source |
|---|---|
| fiber-optic-installation-ulster-county-fusion-splicer-patch-cabinet.webp | low-voltage/low-voltage-installation-ulster-county-05-fiber-splice-tray.jpg |
| fiber-optic-installation-ulster-county-exterior-enclosure-brick-wall.webp | low-voltage/low-voltage-installation-ulster-county-02-exterior-enclosure-install.jpg |
| fiber-optic-installation-ulster-county-retail-shop-open-ceiling-pull.webp | low-voltage/low-voltage-installation-ulster-county-13-retail-store-ceiling-pull.jpg |
| fiber-optic-installation-ulster-county-conduit-box-pull-block-wall.webp | low-voltage/low-voltage-installation-ulster-county-hero-riser-conduit-pull.jpg |
| fiber-optic-installation-ulster-county-high-bay-tray-dome-camera.webp | low-voltage/low-voltage-installation-orange-county-hero-warehouse-cable-tray.jpg |
| fiber-optic-installation-ulster-county-door-strike-terminal-wiring.webp | low-voltage/low-voltage-installation-ulster-county-12-electric-strike-wiring.jpg |
| fiber-optic-installation-ulster-county-rack-switch-laptop-setup.webp | low-voltage/low-voltage-installation-ulster-county-11-rack-switch-config.jpg |
| fiber-optic-installation-ulster-county-service-van-cable-reels.webp | low-voltage/low-voltage-installation-nyc-van-load-out.jpg |
| fiber-optic-installation-ulster-county-conference-camera-above-display.webp | low-voltage/low-voltage-installation-orange-county-hero-ptz-camera-mount.jpg |
| fiber-optic-installation-ulster-county-wall-jack-certification-tester.webp | low-voltage/low-voltage-installation-ulster-county-06-fluke-certification-pass.jpg |
| fiber-optic-installation-ulster-county-keystone-wall-plate-termination.webp | low-voltage/low-voltage-installation-nyc-04-keystone-wall-plate-termination.jpg |
Note: every photo in the assigned pool shows technicians (side/rear views) and most show the AESS (800) 486-0943 number on shirts/van; none chosen shows the 844-386-7238 number, a plate, house number or readable document. Several look AI-generated — for Anwar to review.

### Keyword plan (Ulster page)
Service: fiber optic installation Ulster County, demarc extension, fiber riser, dual-provider entrance, fusion splicing, OTDR testing. Problem: multi-gig not reaching rooms, no riser in old buildings, tangle of provider drops, dead cable in reused plants, guest/owner network separation, Wi-Fi mesh bottlenecks, outages at remote rentals. Technology: bend-insensitive OS2, OFNR/OFNP, indoor/outdoor drop, hybrid fiber-power, LC panels, SFP+, VLAN switches, dual-WAN firewall, UPS. Industry: short-term rentals, inns/retreats, Main Street mixed-use, reused industrial (iPark 87), campuses/BOCES/hospital, studios. Geographic: Ulster County, Kingston (Stockade/Uptown, Midtown/Broadway, Rondout/East Strand), Town of Ulster/Enterprise Drive, Saugerties, Woodstock, New Paltz, Gardiner, Shandaken/Phoenicia/Pine Hill/Big Indian, Olive/Ashokan, Stone Ridge, Ellenville, Highland/Marlboro, Route 9W/28/32/209.

### Question register additions
fiber-optic-installation-ulster-county
§9 Questions Answered:
- Can a building in Kingston take service from two different internet providers for backup, and how should both be wired? (fiber-optic-installation-ulster-county)
- Is a cellular backup still worth having once a property has fiber service? (fiber-optic-installation-ulster-county)
- After you leave, can our own staff or a BOCES-trained technician look after the fiber, and what do they get from you? (fiber-optic-installation-ulster-county)
- Groups at our retreat all stream and video call at once — is the bottleneck the internet line or the wiring between the lodge and the cabins? (fiber-optic-installation-ulster-county)
(Statement headings, not questions: "What has to change inside before a multi-gig plan shows up in the rooms"; "Reusing the steel conduit and cable tray in former IBM-era buildings"; "Untangling years of separate provider drops in an Uptown cellar"; "A cellar-level link through the common wall of two attached buildings"; "Walling off locks, cameras and thermostats from guest devices"; "Hybrid fiber-and-power cable on Ulster properties"; "Properties next to Forest Preserve land in the Catskill Park"; "How Ulster County's electrical licensing law treats a fiber job"; repair headings "Same-Day Fiber Repair Across Ulster County", "Network Down at the Cottages Tonight".)
§17 FAQ:
- Do you travel to the Catskill hamlets west of the Ashokan, such as Pine Hill and Big Indian? (fiber-optic-installation-ulster-county)
- Will the new network work with the smart TVs and streaming boxes already in our cabins? (fiber-optic-installation-ulster-county)
- Can fiber be installed in a log home or a cabin with exposed log walls? (fiber-optic-installation-ulster-county)
- Will a stone patio or slate walkway have to come up for a fiber trench? (fiber-optic-installation-ulster-county)
- Can you give us a speed report for each cabin or tenant space when the work is done? (fiber-optic-installation-ulster-county)
- How long will the network keep running in a power cut, and can it run from our generator? (fiber-optic-installation-ulster-county)
- What happens if a tree comes down on an overhead fiber run across our property? (fiber-optic-installation-ulster-county)
- Can the same crew install keypad or smart locks for rental check-in while the fiber goes in? (fiber-optic-installation-ulster-county)
- Can guest Wi-Fi show a welcome page with our house rules before guests connect? (fiber-optic-installation-ulster-county)
- Can fiber feed outdoor Wi-Fi for an event lawn, orchard or campground? (fiber-optic-installation-ulster-county)

De-dup notes: first pass (vs Putnam/Dutchess) dropped rodent, private-road, county-licensing, adjoining-public-land and old-fiber-reuse questions. Second pass (vs queens, bronx, staten-island, nassau, suffolk, westchester, rockland, orange): converted to statement headings the multi-gig (≈ Nassau "fiber at the wall, old phone wiring — where should money go first"), old-pathway reuse (≈ Orange church-school pathways), tenant-drop cleanup (≈ Orange/Queens per-tenant provider holes), shared-wall (≈ Orange party wall, Nassau attached storefronts), guest/lock segmentation (≈ Orange firehouse alerting vs members' Wi-Fi) and hybrid cable (≈ Staten Island detached building with no electricity); replaced FAQ "Does the power have to be shut off…" (≈ Staten Island Con Edison shutoff) and "Can our property manager… see from home…" (≈ Suffolk empty-house monitoring); added the staff-handover question. Page "Larger inns, camps and retreat centers" paragraph and one Field Notes paragraph removed for word count.

## Bloomfield, Staten Island — local research (2026-10-17 batch, fiber-optic-installation-bloomfield-staten-island-ny)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources and the Staten Island section are reused only where noted. Page thesis: **Bloomfield is the West Shore's commercial/industrial district — very large single-storey distribution buildings on former oil-terminal land, 1980s office complexes and the Teleport campus on South Avenue, and hotels near I-278/the Goethals — so the fiber problem is distance inside one building (zone cabinets beyond the 100 m copper limit), links out to gates/yard poles across truck courts and engineered fill, and office/hotel risers.** The Staten Island borough page's thesis (short links between buildings on residential/strip lots, aerial vs buried, SNAD, flood-raised houses) is deliberately not repeated; the SI page's Teleport/Amazon/IKEA facts are re-stated only briefly with different sources.

### Reddit (local)
- Query: `reddit statenisland Bloomfield Amazon warehouse Gulf Avenue traffic` · WebSearch → no reddit.com results (CBS, YIMBY, warehouse.ninja only). EMPTY.
- Query: `reddit statenisland Bloomfield Teleport office internet fiber` · Firecrawl web search (excerpts only) → https://www.reddit.com/r/statenisland/comments/1m1cmz2/staten_island_internet_service_providers/ — excerpt: "glofiber is non existent, and Verizon is hit or miss." → §10.5 H3 7 (quoted as a resident's comment). No Bloomfield-specific thread. Same search → https://broadbandnow.com/New-York/Staten-Island excerpt "Fiber internet is 94.4% available in Staten Island" → §10.5 H3 5. https://ispreports.org/business-internet-providers-bloomfield-staten-island-ny/ (excerpt only, ratings table) → not used.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitutes for §10.5 (claims quoted as published, from excerpts):
- Query: `fiber optic cabling warehouse distribution center installation cost how long does it take` · Firecrawl web search:
  - https://www.parksidetech.com/network-cabling/fiber-optic-installation/ — "Most fiber installations are retrofits and do not require major construction." → §10.5 H3 1.
  - https://www.reddit.com/r/FiberOptics/comments/1ipq8ca/how_long_does_construction_take/ — "Construction is usually 6-12 weeks. Cable placement is a week, splicing is 1-2 weeks including testing." (commenter, provider construction) → §10.5 H3 2.
  - https://ztechcommunications.com/2025/12/10/how-much-does-structured-cabling-installation-cost-in-dallas/ — "Fiber Optic Cabling (Backbone) $3,000-$5,000+ (varies by strand count)" → §10.5 H3 3.
  - https://community.hubitat.com/t/underground-fiber-optic-cable-installation-cost/139202 — "According to the installer, the directional boring cost is $15K." → §10.5 H3 6 (forum post).
- Query: `business park fiber "dark fiber" vs "lit" office tenant claim cheaper faster` · Firecrawl web search → https://lightpathfiber.com/articles/what-dark-fiber-dark-fiber-vs-lit-fiber-explained/ — "Dark Fiber: Higher upfront cost, lower ongoing costs" → §10.5 H3 4.
- Yelp 1–3★ for Bloomfield/West Shore fiber or cabling contractors: no yelp.com result in any query. EMPTY.
- Bing & DuckDuckGo: EMPTY (not accessible in build env).

### Neighbourhood history, land use, transit
- Query: `Bloomfield Staten Island neighborhood industrial Gulf Avenue Chelsea Road history` · WebSearch → https://en.wikipedia.org/wiki/Bloomfield,_Staten_Island (WebFetch): West Shore; north of Travis-Chelsea, west of Bulls Head; Prall's Island offshore; formerly Daniell's Neck / Merrell Town, name on a map 1874; few residents in the 20th century, land used to store construction equipment; Gulf Oil terminal 440 acres, built 1936, 82 tanks, 215 million US gallons, closed 1998; Gulf Avenue (West Shore Expressway service road) named after it; commercial (not residential) development accelerated late 1980s with large office buildings; Hilton Garden Inn opened 2001 and Hampton Inn & Suites 2007, both on South Avenue; NASCAR proposal failed; Matrix Global Logistics Park opened fall 2018 for companies incl. Amazon and IKEA, "more than 2,000 jobs"; S46/S96 on South Avenue, S40/S90 serve Matrix on Gulf Avenue. → §5 paras 1–2, §5.5 fact 2, §8 cards (Gulf Ave, South Ave hotels), §13 Hilton card. (1973 TETCo explosion noted, not used.)
- Query: `silive Bloomfield Staten Island warehouse new development 2025 West Shore` · WebSearch → https://en.wikipedia.org/wiki/West_Shore,_Staten_Island (WebFetch): Travis "only residential neighborhood on the West Shore"; Teleport a high-tech industrial park built early 1980s mostly for communications-industry companies; South Avenue begins in Mariners Harbor, ends in Travis, string of large office complexes built along it in the 1980s; West Shore Expressway principal north–south road; Amazon announced Jan 2020 a 450,000 sq ft lease next to its 855,000 sq ft centre. → §2b offices section para 1, "On the Island" section para 2.
- Same search → https://www.nyc.gov/assets/planning/download/pdf/plans-studies/west-shore/wsfinalreportchap4_46to49.pdf (WebFetch, DCP "Working West Shore 2030" implementation tables; date not visible): Bloomfield/Teleport zone — EDC to pursue modern industrial/distribution development on vacant Bloomfield sites; expand uses at Staten Island Corporate Park and Teleport campus; truck connections from the Goethals Bridge to industrial sites; drainage plan for the northern West Shore. → "On the Island" section para 3.
- Same search → https://newyorkyimby.com/2016/05/450000-square-foot-warehouse-filed-at-566-gulf-avenue-bloomfield-staten-island.html (WebFetch, May 4 2016): 566 and 586 Gulf Avenue; vacant tract west of the West Shore Expressway and north of Bloomfield Avenue; ~252 acres permanently preserved as wetlands, ~330 acres industrial; remediation began 2013; development area raised to at least 10 feet above sea level (Emergency Watershed Protection programme); NYS DEC involved in wetland preservation; warehouses 46 ft high. → §5 para 4, §5.5 fact 3, §8 Bloomfield Ave card, "Tank Farm to Truck Court" section, §9 remediated-site Q and fill Q. (Tract acreage 676 here vs 671 in DNAinfo — not stated on page.)

### Logistics park
- Query: `Matrix Global Logistics Park Staten Island Bloomfield buildings Gulf Avenue` · WebSearch → https://njbiz.com/matrix-breaks-ground-on-staten-island-logistics-park/ (WebFetch, Oct 13 2016): Matrix Development Group broke ground on first two of four buildings, 975,000 and 450,000 sq ft; >3,000 jobs projected. → §5 para 2, §5.5 fact 1.
  - https://www.dnainfo.com/new-york/20161011/bloomfield/nascar-matric-development-group-distribution (WebFetch, Oct 11 2016): former oil tank storage site off Gulf Avenue; Matrix bought 200 acres in 2016; ISC bought 2004 ($100M) for an 82,500-seat track, sold 2007. → §5 para 2 (200 acres). NASCAR detail not used.
  - https://www.pincusco.com/matrix-finishes-7-3m-rehab-of-staten-island-warehouse/ — paywalled. EMPTY.
- Silo/SI-section sources reused: Commercial Observer (Amazon 855,000 sq ft, IKEA 975,000 sq ft) — not repeated as a fact on this page beyond "Amazon and IKEA among tenants".
- Page-own calculation (no source needed, arithmetic): 975,000 sq ft ≈ 90,580 m²; a square footprint of that area ≈ 301 m a side vs the 100 m copper channel limit → §5 para 2. Stated conditionally ("spread over one level").

### Teleport, offices, data centre
- Query: `Corporate Commons Three Staten Island Teleport Nicotra building` · WebSearch →
  - https://forgotten-ny.com/2023/08/teleport-calling-bloomfield/amp (WebFetch): Teleport opened 1983 (article also says 1970s); 17 dishes, 25 ft diameter, 18-acre walled compound, once the world's largest satellite dish farm; AT&T 4,000 jobs, left 2001; satellite/fiber advances made it obsolete; now offices for doctors, lawyers, small businesses, schools; Corporate Commons One–Three (Richard and Lois Nicotra), rooftop farm on Three; Teleport Drive reached only from South Avenue; South Avenue runs 3.5 miles Mariners Harbor–Chelsea; 900 and 1000 South Avenue built in the forest before parcels were restricted; Lois Lane named after Lois Nicotra; Staten Island Industrial Park mapped 1962, now a fenced nature preserve. → §5 para 3, §5.5 fact 5, §8 cards (South Ave, Teleport, Corporate Park/Lois Lane), offices section.
  - https://www.untappedcities.com/330000-square-foot-office-building-on-staten-islands-teleport-campus-breaks-ground-in-nyc/ (WebFetch, Oct 2017): Corporate Commons Three 330,000 sq ft, LEED-certified, NYCEDC + Nicotra Group, groundbreaking announced Oct 4 2017; ~20% medical tenants, charter school, adult education planned; rooftop farm. No fiber/connectivity details. → §7 card, §13 card.
- Query: `Telehouse New York Teleport 7 Teleport Drive Staten Island data center` · WebSearch → https://www.datacenterknowledge.com/colocation/telehouse-space-available-at-ny-nj-powered-staten-island-facility (WebFetch, June 24 2021): 7 Teleport Drive, 162,000 sq ft, completed 1989, KDDI-owned; yards from NYIIX; fiber entry points increased to three in 2007 via underground paths. → §5.5 fact 4, §13 card. (Silo source Wikipedia Teleport reused for "Nicotra" context only.)

### Hotels
- Query: `Hilton Garden Inn Staten Island 1100 South Avenue Hampton Inn 1120 South Avenue` · WebSearch → https://www.timeout.com/newyork/hotels/hilton-garden-inn-new-york-staten-island (WebFetch): 1100 South Ave at Lois Ln; 198 rooms/suites; indoor pool; Lorenzo's restaurant with cabaret; Above Rooftop Lounge; in the Corporate Park within "415 acres of preserved woodland"; minutes from I-278; S46/S96; shuttles to the ferry and Newark Airport. Hampton Inn address NOT confirmed (query's 1120 South Avenue not verified — not used). → §8 hotels card, §13 card, hotels section.

### Bridge, wetlands
- Query: `new Goethals Bridge opened 2017 cable-stayed Port Authority second span 2018 Staten Island Elizabeth` · WebSearch → https://www.cbsnews.com/newyork/news/new-goethals-bridge-opens/ (WebFetch, June 10 2017): first twin span opened to NY-bound traffic; cable-stayed; $1.5 billion; replaced an 89-year-old bridge; Elizabeth NJ–Staten Island. → §13 card.
- Query: `Saw Mill Creek wetland mitigation bank Staten Island Chelsea Bloomfield NYCEDC acres` · WebSearch → https://www.stormwater.com/home/news/33045765/new-york-citys-first-mitigation-bank-restores-54-acres-of-wetlands (WebFetch, Oct 10 2019): NYCEDC; 54 acres tidal wetlands, marsh, mudflat in Saw Mill Creek watershed, west shore; >40,000 cubic yards of debris removed; NYC's first mitigation bank. → §5 para 4, §5.5 fact 6, ground section, §13 card.

### Local licensing / permits / technical
- Silo sources reused: OFNR/OFNP listings (cablinginstall), DOB <50 V statement (site's own structured-cabling-pricing page), firestopping (nyflnerds/unifinerds), New York 811 (newyork-811.com). → §8.5 compliance list, process step 3.
- Not separately researched (stated as general practice, no figures): sprinkler clearance under high-bay roofs, cable minimum installation temperature (data-sheet value), passive optical LAN, service loops, remote-IT handover. No standard numbers quoted.
- Local news (SI Advance/silive) on Bloomfield fiber/cabling: none retrieved. EMPTY. Chelsea Road: no source retrieved — not named on the page.

### Pricing used (copied from fiber-optic-installation-staten-island.html; no new prices)
$39 termination · $44 OTDR/strand · $385 MM drop · $440 SM drop · $4,950–$7,700 12-strand OM4 backbone · $8,800–$16,500+ 24-strand OS2 link · from $2,640 second telecom room · $195/hr, 3-hr min ($585). Packages: Starter 2 × $440 = $880; Standard $4,950–$7,700; Premium $8,800–$16,500+ (same lines as the SI page). The open SI configurator conflict ($411/$470) flagged in the Staten Island section still applies.

### Images (11) — permanent image rule; Drive folder `AESS Website Photos/Fiber Optic Installation` empty (checked this run), CompanyCam not connected
WebP q80 in images/fiber-optic-installation/. Printed phone numbers on shirts/caps/van side (incl. a non-company "444-386-7238") and the van's printed web address were pixelated + blurred; a wall sign reading "COMMUNITY CENTER" (AP photo) and a whiteboard with handwritten rack notes (rack-patching photo) were blurred. No other edits. Source scenes chosen to avoid the 11 used on the Staten Island fiber page.
| New file | Source |
|---|---|
| fiber-optic-installation-bloomfield-high-bay-lift-tray-dome-camera.webp | low-voltage/low-voltage-installation-bronx-hero-warehouse-cable-tray.jpg |
| fiber-optic-installation-bloomfield-crew-reels-open-ceiling.webp | low-voltage/low-voltage-installation-bronx-03-crew-cable-pull.jpg |
| fiber-optic-installation-bloomfield-fusion-splicer-yellow-jumpers.webp | low-voltage/low-voltage-installation-brooklyn-fiber-fusion-splice.jpg |
| fiber-optic-installation-bloomfield-scissor-lift-access-point.webp | low-voltage/low-voltage-installation-bronx-access-point-lift-install.jpg |
| fiber-optic-installation-bloomfield-emt-conduit-block-wall-pull.webp | network/network-installation-bronx-network-drop-conduit-emt-riser.webp |
| fiber-optic-installation-bloomfield-rack-patching-panduit.webp | low-voltage/low-voltage-installation-bronx-05-idf-rack-patching.jpg |
| fiber-optic-installation-bloomfield-splicer-blue-adapter-panel.webp | low-voltage/low-voltage-installation-brooklyn-fiber-splice-tray.jpg |
| fiber-optic-installation-bloomfield-van-cable-reels-ladders.webp | low-voltage/low-voltage-installation-brooklyn-van-load-out.jpg |
| fiber-optic-installation-bloomfield-hammer-drill-block-wall-pull-line.webp | network/network-installation-bronx-core-drill-cmu-wall-penetration.webp |
| fiber-optic-installation-bloomfield-rack-switch-laptop-config.webp | low-voltage/low-voltage-installation-dutchess-county-hero-rack-switch-config.jpg |
| fiber-optic-installation-bloomfield-rack-before-after.webp | network/network-installation-bronx-network-rack-cleanup-before-after.webp |
Note: area-named source files are byte-identical copies of ~20 base scenes, so every scene already appears elsewhere in the fiber silo; the library photos still look AI-rendered (garbled small text) — flagged again for Anwar.

### Keyword plan (Bloomfield page)
Service: fiber optic installation Bloomfield Staten Island, warehouse/distribution-centre fiber backbone, zone cabinets, dock-wall fiber, gate/guard-booth fiber, yard-pole fiber, office suite riser fiber, hotel fiber backbone, fusion splicing, OTDR testing. Problem: 100 m copper limit in big buildings, scanner dropouts at the far end, remediated land, settling fill, truck traffic over conduit, operating buildings/peak weeks, multi-tenant splits. Technology: OS2, OM4, armored, aerial on messenger, conduit/innerduct, zone cabinets, splice trays, SFP/media converters, passive optical LAN. Industry: logistics/distribution, office parks, medical suites, schools, hotels, data-centre tenants, contractors' yards. Geographic: Bloomfield, West Shore, Gulf Avenue, South Avenue, Teleport Drive, Lois Lane, Bloomfield Avenue, West Shore Expressway, Goethals Bridge, Travis, Chelsea, Bulls Head, Mariners Harbor, Arlington, New Springville.

### Question register additions
fiber-optic-installation-bloomfield-staten-island-ny
§9 Questions Answered:
- Our main network room is in the front office but most of our devices are at the back of the building — should the room move rather than run fiber all that way?
- The automation vendor installing our conveyors and sorters wants its own network — should it get dedicated strands, and who answers for them?
- Handheld scanners drop out at the far end of the floor while the office Wi-Fi is fine — is this a wiring problem?
- Our IT team works from headquarters in another state — what do they need from you to support the fiber without visiting?
- Can fiber run up our yard light poles to reach cameras mounted high above the trailer lot?
- Our site was part of a remediated former oil terminal — can we dig through the ground for fiber, and who has to agree?
- Our building pad sits on deep new fill — will settling ground damage fiber buried between the warehouse and the outbuildings?
- We're moving our servers into a nearby data centre — what changes for the fiber inside our office?
- Our hotel's ballroom and meeting rooms host events that need live streaming — can they get capacity separate from guest Wi-Fi?
- Is passive optical LAN a sensible choice for a hotel's guest floors?
§17 FAQ:
- Do you cover Travis, Chelsea, Bulls Head and the rest of the West Shore near Bloomfield?
- Do you carry out wireless surveys, or only the cabling?
- How does fiber cross an expansion joint in a large warehouse floor or roof?
- Can fiber run through a forklift battery-charging room?
- Will you coordinate with our sprinkler contractor before hanging tray under the roof?
- Is there a temperature below which fiber cable should not be pulled?
- Can fiber, cameras and door access be quoted as one project?
- Can a zone network cabinet go on a mezzanine instead of the warehouse floor?
- Who takes away the empty reels, boxes and offcuts at the end of the job?
- Can you work above running conveyors without stopping them?
- Can fiber reach the staff entrance where time clocks, turnstiles and badge readers sit?
- How much spare fiber should be left coiled at each zone cabinet?

De-dup notes (checked by meaning against all 17 fiber pages incl. the in-progress Hunts Point page's headings at build time). Five drafted questions were replaced because the concurrent Hunts Point page asks the same intent: dock-door run design, EV truck chargers, own-lift-or-rent, insulated-metal-panel penetrations, slab scanning before coring. Also avoided SI "national logistics tenant spec" and "racking rearranged", LI "gatehouse"/"parking-lot depth"/"repaving", Brooklyn "truck-yard cameras"/"camera distance from rack", Bronx "high column-free ceiling", Queens "train vibration"/"freezer room", Manhattan "carrier hotel"/"second diverse path"/"cellar flood room", HV "busy-season scheduling", Orange "hotel rooms in service", Rockland "Bergen County cross-state", Suffolk "industrial site safety rules"/"run length before splice", Nassau "separate network for building controls". Closest remaining intents for the main run to judge: automation-vendor strands vs Nassau "separate network for heating/cooling controls"; staff-entrance time clocks vs Bronx "laundry/package room card readers"; mezzanine cabinet vs Bronx "rack in the super's office".
Build checks (this builder): rendered words 12,319; file 170,237 B (siblings 178,211–225,478; Hunts Point in progress 210,275 at check time); masked paragraph similarity (difflib on ≥12-word p/li/h3, boilerplate NAP/warranty/stamp/consent exempt) max 0.617 (vs Hudson Valley intro line); all others < 0.61.

## Hunts Point, Bronx — local research (2026-10-17 batch, fiber-optic-installation-hunts-point-bronx-ny)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources above are reused where noted (AI reality-check claims: streamlinetelecom $1–6/ft, thenetworkinstallers/FBA $18/ft underground median, AT&T 4–6 h + T-Mobile 4 h, Quantum Fiber multifamily stages, Atlantech 15-month wait, r/AskNYC "Its on the ISP to wire your building/apartment", CUF 99.8%). Page thesis: the peninsula is a 24-hour, refrigerated, truck-dominated food hub beside a small residential core — fiber here is dock-row spines, sealed cooler/washdown entries, truck-lane crossings, converted-factory suites and new-building pathways; distinct from the Bronx area page (multi-building complexes/courtyard risers). Up-link /fiber-optic-installation-bronx; phone (646) 490-0629; Bronx GBP.

### Reddit (local) — EMPTY
- Query: `reddit Hunts Point Bronx warehouse internet OR fiber OR Fios` · WebSearch → no reddit.com result returned (results were myshyft, Bronx Times, The POINT, a listing). EMPTY (not accessible in build env / no results).

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG — EMPTY (not accessible in build env)
Substituted for §10.5 with the silo-level published claims listed above (each re-worded/attributed; headings paraphrased so they do not repeat the Bronx/Orange headings).

### Yelp 1–3★ — EMPTY
- Query: `yelp low voltage cabling contractor Bronx Hunts Point reviews` · WebSearch → no yelp.com results (Bronx Chamber, Thumbtack, BlueBook, directories). EMPTY.

### Traffic, highway, trucks
- Query: `Hunts Point Interstate Access Improvement Project Bruckner Expressway Oak Point Avenue ramps NYSDOT` · WebSearch → https://dewberry.com/projects/hunts-point-interstate-access-improvement (WebFetch): NYSDOT project, Dewberry/AECOM JV; widens Bruckner, adds interstate access ramps to Hunts Point Market, shifts trucks off local streets; safety work at 20+ Bruckner Blvd intersections; $1.7 billion; three design-build contracts. → §5.5 facts list, Trucks section para 3, Commercial card "Bruckner Boulevard and Edgewater Road".
- Query: `Hunts Point peninsula industrial business zone truck trips per day Bronx diesel asthma` · WebSearch → https://amny.com/new-york/bronx/hochul-announces-bruckner-expressway-expansion-key-step-to-ease-south-bronx-truck-traffic-right-wrongs-of-robert-moses-era (WebFetch, Aug 21 2023): nearly 80,000 trucks/day to and from the peninsula, ~13,000 on residential side streets; Phase 1 two-way ramp Edgewater Rd–Sheridan Blvd + Bruckner→Edgewater ramp; Phase 2 $518M widening 1.25 mi of Bruckner E 141st St–Barretto St with ramps at Leggett Ave; Phase 3 Bruckner–Sheridan interchange + third lane; Oak Point exit rejected (rail yard, Amtrak/CSX). → hero subhead, §5.5, Trucks section paras 1 & 3.
- Same query → https://www.governor.ny.gov/news/governor-hochul-announces-significant-congestion-pricing-funded-air-quality-improvement (WebFetch, Apr 1 2026): 20 diesel TRUs at the Hunts Point Produce Market replaced, 75 more in pipeline, $15M for the measure; $20M listed for electric truck charging infrastructure (no location given). → Trucks section para 2 (stated with "without naming where").

### Food Distribution Center, markets, flood/power
- Query: `Hunts Point peninsula flood zone FEMA 100-year floodplain food distribution center sea level rise study` · WebSearch → https://citylimits.org/2022/10/27/spared-by-sandy-hunts-point-food-market-slow-to-address-flood-risk/ (WebFetch): nearly a third of FDC in current 100-yr floodplain; future floodplain nearly entire hub; Sandy at low tide, water into New Fulton Fish Market parking lot; 2016 feasibility study: power outages main threat to produce and fish markets; produce market's ground-level power stations vulnerable to Bronx River surge; FDC 329 acres, ~4.5bn lb/yr; NYCEDC estimate 25% produce / 35% meat / 45% fish; meat wholesaler quote "almost 700,000 square feet of refrigerated space". → §5 para 1, §5.5, Flood & Power section, §13 FDC card.
- Query: `Hunts Point Cooperative Market meat buildings square feet merchants Bronx` · WebSearch → https://en.wikipedia.org/wiki/Hunts_Point_Cooperative_Market (WebFetch): opened 1962; ~60 acres; seven refrigerated/freezer buildings; 50+ wholesale businesses. → §5.5. https://newyorkyimby.com/2025/07/renovations-begin-on-building-c-at-hunts-point-cooperative-market-in-hunts-point-the-bronx.html (WebFetch, Jul 24 2025): $18M recladding of Building C (built 1972) with sealed insulated metal façade. → §7 cards, §9 Q "reclad in insulated metal panels".
- Query: `New Fulton Fish Market Hunts Point building square feet opened 2005` · WebSearch → https://www.nbcnews.com/id/wbna8131908 (WebFetch, 2005): ~400,000 sq ft, building more than four football fields long, climate-controlled at 41°F. https://therealdeal.com/2005/09/01/new-fulton-fish-market-to-open-after-delays/ (WebFetch): 450,000 sq ft — CONFLICT on size, so page states only "more than four football fields long" and "mid-2000s". → §13 FDC card.
- Query: `Hunts Point Produce Market redevelopment new building square feet Aurora Primus design-build 2026` · WebSearch → https://newyorkyimby.com/?p=1984924 (WebFetch): $405M, Aurora-Primus JV, all-electric intermodal facility on rail-yard site along the Bronx River, more refrigerated space, construction expected late 2026. → §5 para 4, New Construction section.
- Query: `Hunts Point Wastewater Resource Recovery Facility DEP Ryawa Avenue gallons per day` · WebSearch → https://www.waterandwastewater.com/hunts-point-wastewater-treatment-plant (WebFetch): "600 MGD" — NOT used (implausible/unverified).

### Buildings, streets, landmarks
- Query: `BankNote building 1201 Lafayette Avenue Hunts Point American Bank Note Company landmark` · WebSearch → https://en.wikipedia.org/wiki/American_Bank_Note_Company_Printing_Plant (WebFetch): 1201 Lafayette Ave; 1909–1911; Kirby, Petit & Green; 405,000 sq ft; nine-storey tower on Lafayette wing; brick on steel frame, glazed arches, concrete floors; LPC 2008; The BankNote (Madison Marquette); Wildcat Academy Charter School floors 4–6; HRA 20-year lease 2013. → §5.5, §7 card, Converted Factories section, §13 card.
- Query: `Hunts Point Avenue commercial corridor Bronx shops residential blocks Hunts Point Avenue Bruckner Boulevard 6 train station` · WebSearch → https://www.forgotten-ny.com/2009/03/hunts-point-bronx/ (WebFetch, 2009): Hunts Point Ave runs Southern Blvd/E 163rd St to East Bay Ave & Halleck St; auto-glass shops at Hunts Point & Garrison Aves; Lafayette Ave Bridge 1906; Bruckner Expressway built 1956–61 along the railroad; Barry St brick factory c.1900–1910; Oak Point Ave: Midland Steel warehouse at Worthen St, NYCTA Tiffany Street shops; Corpus Christi Monastery 1890; Gilbert Place bowed-front attached houses; Hunts Point station by Cass Gilbert 1908 housing small businesses. → §5 para 1, §7 cards, §8 corridor cards, §13 station card. (2009 source — stated with attribution where it may be dated.)
- Same query → https://www.newyorkyimby.com/2015/07/construction-begins-on-hunts-point-mall-925-hunts-point-avenue.html (WebFetch): 40,000 sq ft retail centre (The Crossings) at 925 Hunts Point Ave. → §8 Hunts Point Avenue card.
- Query: `Hunts Point Avenue station Cass Gilbert New Haven Railroad landmark Metro-North Penn Station Access Hunts Point` · WebSearch → https://en.wikipedia.org/wiki/Hunts_Point_station (WebFetch): Cass Gilbert station; new Metro-North station north of Hunts Point Ave, below street level behind the old building; planned 2027; design-build Dec 2021, groundbreaking Dec 2022. Silo/Bronx source reused: cityandstateny.com (July 2025) "won't be completed until at least 2028". → §5 para 4, New Construction section, §13 card.
- Query: `The Peninsula Spofford juvenile detention redevelopment Hunts Point 1221 Spofford Avenue light industrial affordable housing` · WebSearch → https://edc.nyc/press-release/mayor-opens-affordable-homes-former-site-spofford-juvenile-detention-center-where-he (WebFetch, Jun 22 2022): The Peninsula; 183 homes in first building; ~740 affordable homes planned on five acres; light-industrial building (bakers, coffee roasters, food producers) completed the year before; Gilbane/Hudson/MHANY; WXY + Body Lawson. → §5 para 4, §7 card, New Construction section.
- Query: `Barretto Point Park Hunts Point Riverside Park Bronx River acres opened` · WebSearch → https://en.wikipedia.org/wiki/Barretto_Point_Park (WebFetch): opened 2006; former sand/gravel and asphalt plant; Floating Pool Lady since 2008. Acreage CONFLICT (12.22 ac vs ~5 ac in Forgotten NY) — acreage not used. → §13 card.
- Query: `Hunts Point Riverside Park Lafayette Avenue Bronx River Edgewater Road opened 2006` · WebSearch → https://php-cms.nycgovparks.org/parks/X336 (WebFetch): Lafayette Ave between Edgewater Rd and the Bronx River; former illegal dumping ground; fishing pier, kayak/canoe launch; Bronx River Greenway. → §13 card, §8 card.
- Query: `Longwood Historic District Bronx designated row houses Hunts Point` · WebSearch → https://www.nypap.org/preservation-history/longwood-historic-district/ (WebFetch): designated July 1980, extended 1983, NRHP 1983; mostly two-/three-family houses by Warren C. Dickerson, bay-front twins. → §13 card.
- Query: `THE POINT CDC 940 Garrison Avenue Bronx 10474` · WebSearch → https://en.wikipedia.org/wiki/The_POINT_Community_Development_Corporation (WebFetch): 940 Garrison Ave, founded 1993. Building origin CONFLICT (bagel factory vs bank-note storage) — not used.
- Query: `Hunts Point Bronx broadband internet fiber businesses connectivity market wholesalers` · WebSearch → https://www.untappedcities.com/a-green-roof-atop-the-point-in-the-bronx-is-providing-free-internet-to-hunts-point/ (WebFetch, Nov 14 2019): Free Hunts Point Community WiFi, mesh with routers placed by volunteer businesses/residents, launched 2015, base on The POINT's green roof. → §5.5, §9 Q "host a node of the neighbourhood's free Wi-Fi".

### Technical / code (new for this page)
- Query: `NYC noise code construction hours weekdays 7 a.m. 6 p.m. after hours variance DOB DEP` · WebSearch → https://www.nyc.gov/assets/dep/downloads/pdf/environment/education/nyc-noise-code-fact-sheet.pdf (WebFetch): approved construction hours weekdays 7:00 a.m.–6:00 p.m.; after-hours with permit for listed reasons; noise mitigation plan required. → §8.5 callout, §9 Q "noisy drilling at night", scheduling table.
- Query: `FOA fiber optic safety fiber scraps disposal container cleaved fiber shards eye skin` · WebSearch → https://www.thefoa.org/tech/safety.htm (WebFetch): scraps "very dangerous", dispose in a dedicated container, keep food and drink out of the work area. → §8.5, Cold Rooms section para 4, §9 Q "cleaved fiber scraps".
- Query: `NEMA 4X enclosure washdown corrosion resistant stainless polycarbonate food processing definition` · WebSearch → https://www.se.com/us/en/faqs/FA350115/ (WebFetch): Type 4 gasketed/clamped for washdowns and directed water; 4X adds corrosion resistance for food processing with caustic cleaners. → Cold Rooms para 3, §9 washdown Q, §10.
- Query: `insulated metal panel cold storage walls block Wi-Fi signal warehouse freezer wireless coverage` · WebSearch → https://unifinerds.com/warehouse-wifi-dead-zones-top-10/ (WebFetch): "Freezer panels and insulated walls can block signal"; coverage outside ≠ inside; metal racking blocks/reflects. → Cold Rooms para 1, §9 cooler Wi-Fi Q.
- Query: `copper cable theft telecom fiber no scrap value thieves mistake fiber for copper` · WebSearch → https://fox4kc.com/business/kansas-city-thieves-suspected-of-cutting-more-fiber-cables-looking-for-copper/amp/ (WebFetch, May 16 2023): "The fiber lines do not contain copper and have no scrap metal resell value." → §9 Q "cable thieves".

### Local news / hyperlocal on Hunts Point fiber-installation contractors — EMPTY (none retrieved).

### Pricing used (copied from fiber-optic-installation-bronx.html only — no new prices)
$35/termination; $40/strand OTDR; $391 MM drop; $447 SM drop; 12-strand OM4 $4,500–$7,000; 24-strand OS2 $8,000–$15,000+; second telecom room from $2,400; $195/hr 3-hr min ($585); packages $894 (2 × $447) / $4,500–$7,000 / $8,000–$15,000+. Same Bronx 1.00× vs $391/$447 configurator conflict as the Bronx page (inherited, flagged there).

### Images (11) — permanent image rule; Drive folder `AESS Website Photos/Fiber Optic Installation` empty (per main run), CompanyCam not connected
Converted to WebP q80 (≤1600 px) in images/fiber-optic-installation/. Chosen by visual-hash clustering to avoid scenes already on fiber-optic-installation-bronx.html; 9 of 11 scenes are not on the Bronx page (splicer and warehouse-tray scenes overlap Bronx because the library has few fiber/warehouse scenes). Rejected: frames with frontal faces (two-tech corridor pull, cable-box staging, wall-fish, AP-on-ladder, core-drill) and the port-map frame with a readable cable map.
| File | Source | What it shows |
|---|---|---|
| fiber-optic-installation-hunts-point-fusion-splicer-adapter-rack.webp (hero) | low-voltage/low-voltage-installation-brooklyn-fiber-splice-tray.jpg | splicer (READY screen) under blue adapters/yellow jumpers, cleaver, IPA |
| fiber-optic-installation-hunts-point-switch-seated-in-rack.webp | network/network-installation-westchester-county-managed-poe-switch-rack-install.webp | switch being seated in rack under blue patch cords, firewall, UPS |
| fiber-optic-installation-hunts-point-jhook-bundles-open-ceiling.webp | network/network-installation-westchester-county-jhook-ceiling-pathway-bundles.webp | blue bundles in J-hooks above open grid |
| fiber-optic-installation-hunts-point-warehouse-basket-tray-lift.webp | low-voltage/low-voltage-installation-nyc-20-warehouse-cable-tray-highbay.jpg | scissor lift, basket tray, dome camera, racking |
| fiber-optic-installation-hunts-point-access-point-lift-ceiling.webp | low-voltage/low-voltage-installation-rockland-county-10-access-point-lift-install.jpg | AP pressed into ceiling from lift (back view) |
| fiber-optic-installation-hunts-point-rack-laptop-switch-setup.webp | low-voltage/low-voltage-installation-nassau-county-rack-switch-config.jpg | laptop on rack shelf, switches |
| fiber-optic-installation-hunts-point-idf-patch-panel-stud-wall.webp | low-voltage/low-voltage-installation-bronx-idf-patch-panel-build.jpg | wall-mount patch panel on stud wall, reels |
| fiber-optic-installation-hunts-point-toner-probe-patch-panel.webp | network/network-installation-orange-county-network-cable-toner-tracing.webp | probe + tester at labelled panel |
| fiber-optic-installation-hunts-point-certification-tester-wall-jack.webp | network/network-installation-rockland-county-fluke-dsx-certification-pass.webp | handheld certifier PASS at wall outlet |
| fiber-optic-installation-hunts-point-rack-before-after-cleanup.webp | network/network-installation-long-island-network-rack-cleanup-before-after.webp | before/after closet cleanup |
| fiber-optic-installation-hunts-point-tone-generator-wall-box.webp | low-voltage/low-voltage-installation-westchester-county-08-tone-generator-trace.jpg | tone generator + probe at wall box |
Flags (same as earlier builders): technicians visible in profile; shirts/hard hats print 800-486-0943 or 844-386-7238; several frames look AI-rendered (garbled small text) — for Anwar's review. Captions describe only what is visible; no customer, named building or local project is claimed.

### Keyword plan (Hunts Point page)
Service: fiber optic installation Hunts Point, dock-row fiber spine, cooler/freezer fiber entry, washdown enclosure, yard/building-to-building fiber, fusion splicing, OTDR testing. Problem: scanners drop in coolers, copper beyond 100 m on long docks, trailers/forklifts hitting cable, washdown spray, condensation, flood/power loss, cable theft, highway construction, noise-code hours. Technology: OS2, OM4, interlocking armor, aerial messenger, NEMA 4X, hardened switches, cold-rated APs, sealed sleeves, firestop. Industry: food wholesale/distribution, cold storage, meat processing, converted-factory offices/schools, light-industrial food producers, residential/mixed-use. Geographic: Hunts Point, Food Distribution Center, Food Center Drive, Halleck St, Oak Point Ave, Barry St, Tiffany St, Lafayette Ave, Garrison Ave, Hunts Point Ave, Bruckner Blvd, Edgewater Rd, Barretto Point, Longwood, Foxhurst, Soundview, Port Morris, Mott Haven.

### Question register additions
fiber-optic-installation-hunts-point-bronx-ny
§9 Questions Answered (and other question headings):
- Hunts Point Link Down Mid-Shift? (repair capture heading)
- Fiber is glass — how do you keep cleaved fiber scraps out of a food-handling area?
- Our processing room is hosed down and sanitised every shift — what fiber hardware survives that?
- Handheld scanners lose Wi-Fi inside our coolers — how do we get reliable coverage in there?
- We have a long row of dock doors — is one fiber run with small switches along the dock better than a cable from every door back to the office?
- Our building is being reclad in insulated metal panels — how should new fiber come through the new wall?
- If fiber has to cross a truck lane overhead between two of our buildings, how high must it be and what holds it up?
- Our new electric truck chargers need a network connection — can that come off our fiber?
- Is fiber a target for cable thieves the way copper is?
- Which parts of a fiber installation can we take with us when our market unit moves to a new building?
- Our suite in a converted printing plant has bare concrete ceilings — how is fiber run so it looks deliberate?
- The floors in our old industrial building are thick reinforced concrete — do you scan before coring?
- Our warehouse backs onto apartment houses — can the noisy drilling be done at night while the market is quiet?
- Can a business host a node of the neighbourhood's free Wi-Fi network on its roof and feed it from our fiber?
- Peninsula Network Down Right Now? (final repair heading)
§17 FAQ:
- Do you cover the rest of the peninsula and the blocks north of the Bruckner — Longwood, Foxhurst and Soundview?
- Is there an industrial or market surcharge on Hunts Point fiber work?
- How will our warehouse staff recognise the fiber so nobody cuts or reroutes it?
- Our camera company is separate — can you install the fiber their system rides on?
- Do we need our refrigeration contractor on site when cable goes into a cold room?
- Can you run fiber for card terminals and order-entry stations on a wholesale sales floor?
- How is drilling dust kept off product and packaging?
- Our provider says its circuit is fine but our far building is still offline — can you find which side the fault is on?
- Can you give us a written scope and quote to attach to a grant, loan or insurance claim?
- Do you bring your own lift for high warehouse ceilings, or should we rent one?
- What does a fiber repair visit to a Hunts Point business cost?
- How does your crew stay safe and out of the way on a floor where forklifts are running?

De-dup notes: checked by meaning against all 16 area pages and the concurrent Bloomfield page. Deliberately avoided intents already in the register: freezer-room entry (Queens), forklift/pallet-jack cable protection, rats, sidewalk shed, BMS link, high-ceiling support (Bronx), truck-yard cameras, wireless-vs-fiber, flood survival (Brooklyn), flood-prone cellar room, lease wording, non-adjacent floors, landmark entry (Manhattan), trench sharing, overhead-vs-underground choice, gatehouse (Long Island), Route 17 road work (Orange), train vibration/noise (Queens), warranty, COI, nights/weekends, single- vs multimode, strand count. A drafted FAQ on Spanish-language labels was dropped because AESS's language capability is unverified. Closest calls for a human read: my cooler Wi-Fi Q vs Bloomfield "scanners drop out at the far end of the floor" (cause differs: insulated panels vs distance); my overhead truck-lane clearance Q vs Long Island "under the parking lot or overhead?" (clearance/support vs route choice); my "camera company is separate" FAQ vs Bloomfield "fiber, cameras and door access quoted as one project".
Build checks (this builder): rendered words 13,811; file 236,653 B (deliberately above the 178,211–225,478 sibling band per the size rule; Bloomfield in progress ~170 KB at check time); masked paragraph similarity (difflib, ≥8-word p/li/td/h3, geo + neighbourhood names masked) max < 0.65 against all 17 fiber pages except the standard pricing-line name "24-strand OS2 backbone or building-to-building link" and the protected NAP/warranty/licence/form lines.

## Chelsea, Manhattan — local research (2026-10-17 batch, fiber-optic-installation-chelsea-manhattan-ny)
Neighbourhood page under /fiber-optic-installation-manhattan. Bronx GBP (460 E Fordham Rd, #bronx), Manhattan line (929) 560-0737. Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md are reused only where noted.

Thesis: Chelsea holds some of New York's most interconnected buildings (111 Eighth Ave, 85 Tenth Ave / Chelsea Market) yet its freight-era terminals, gallery garages, historic-district rowhouses, big co-ops, new High Line condos and NYCHA campuses each block fiber at a different point between the carrier's entrance room and the rooms that need it.

### Reddit (local / NYC)
- Query: `reddit Chelsea Manhattan apartment building fiber internet Verizon Fios not available only Spectrum` · Firecrawl web search (excerpts only; reddit threads not opened).
  - https://www.reddit.com/r/AskNYC/comments/1uhxwu9/why_is_it_so_hard_to_get_fios_on_the_uws_im/ — excerpt: "Verizon tends to want 70% of households in a building to request FIOS before they will wire a building." (UWS thread, a commenter's claim, unverified) → §10.5 H3 #2 (quoted as an unverified Reddit claim and corrected).
  - https://www.reddit.com/r/NYCapartments/comments/14plsdj/advice_no_fios_available_in_apt_after_ll_told_me/ — excerpt: landlord said Fios available; Verizon said "there wasn't any fiber optic cable there at all" → §5 THE NEIGHBORHOOD (resident gap paragraph); §9 Q on checking carriers before a lease.
  - https://www.reddit.com/r/AskNYC/comments/19arudx/verizon_claims_my_building_is_wired_for_fios_but/ — title/excerpt: Verizon and landlord disagree on whether building is wired → §5.
- Query: `Chelsea art galleries West 20s how many galleries open Tuesday through Saturday closed Monday` · Firecrawl web search → https://www.reddit.com/r/AskNYC/comments/zmp3s4/can_i_just_walk_into_the_art_galleries_in_chelsea/ — excerpt: "a ton of art galleries in Chelsea, mainly west of the highline. They all seem to be 'open' during the day from tue-sat." → §5.5 fact list, FAQ (Mondays), Gallery Blocks section.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
- Substitute claims for §10.5 Reality Check: https://ispreports.org/internet-service-providers-chelsea-manhattan-ny/ (search excerpt, query `Chelsea Manhattan news 2026 fiber internet broadband buildings tenants Verizon Spectrum Community Board 4`, Firecrawl): "Verizon offers Fiber service to 86.2% of Chelsea homes" → §10.5 H3 #1. https://www.verizon.com/home/internet/near-me/new-york-ny/ (same search, excerpt): Fios listed as available in Chelsea → §10.5 H3 #1. Remaining five §10.5 claims reuse silo-wide sources already in research/fiber-optic-installation.md (T-Mobile/AT&T install hours; thenetworkinstallers.com citing FBA $18/$8 per ft, Ring and Ping $30–$75 splices, Automation World ~5% testing; atlantech.net 15-month wait; Quantum Fiber multifamily stages).
- Yelp 1–3★ for Chelsea fiber contractors: EMPTY (not searched separately; silo search returned no yelp.com results).

### Landmarks, buildings, corridors
- Query: `111 Eighth Avenue carrier hotel Google purchase Port Authority Commerce Building` · Firecrawl search → https://en.wikipedia.org/wiki/111_Eighth_Avenue (scrape, query mode): completed 1932 as Union Inland Terminal #1; full block Eighth–Ninth Aves, W 15th–16th Sts; 15 storeys, 2.9M sq ft; floors ~165,000 sq ft; four truck elevators 40,000 lb; last railroad company left 1963; Port Authority moved to WTC 1973; Taconic marketed it as a carrier hotel (high ceilings, large floor plates, multiple fiber connections, 5× electrical capacity); stopped accepting new telecom tenants by late 1999; adjacent to trunk fiber from Hudson St up Ninth Ave (Lexent → Lightower); meet-me room one of the main interconnections as of 2006; Google bought 2010 (~$1.8B; other sources $1.9B); Google bought Chelsea Market 2018. Also https://www.datacenterknowledge.com/hyperscalers/google-confirms-purchase-of-111-8th-avenue (excerpt, $1.9B) → §5, §5.5, Carrier Blocks section, §9 Q1, §13 card, Freight-to-Fiber section.
- Query: Firecrawl scrape https://en.wikipedia.org/wiki/Chelsea_Market (query mode): full block, bridge over Tenth Ave to 85 Tenth Ave; High Line passes through the 10th Ave side; Nabisco, Oreo invented there; 19 separate structures; Nabisco left 1958; redeveloped 1990s; Alphabet bought 2018 for >$2.4B; within Gansevoort Market Historic District → §5, §5.5, §7 cards, §13 card, Joined Blocks section, §9 High Line Q.
- Query: Firecrawl scrape https://en.wikipedia.org/wiki/High_Line (query mode): 1.45 miles; West Side Improvement agreed 1929; first train 1933; dedicated 1934; last street-level track removed from Eleventh Ave 1941; 1978 two carloads/week; closed 1980; CSX ownership 1999; spurs at 16th St to Nabisco building and Merchants Refrigerating warehouse; park sections opened June 2009, June 2011, Sept 2014 → §13 card, Freight-to-Fiber section, §9 High Line Q.
- Query: `High Line owned by City of New York CSX donated 2005 Friends of the High Line license agreement NYC Parks` · Firecrawl search → https://www.thehighline.org/faq/ (excerpt): owned by the City, under NYC Parks jurisdiction, donated by CSX; "The land beneath the High Line is owned in parcels by New York State, New York City, and more than 20 private property owners." https://edc.nyc/project/high-line (excerpt): Nov 2005 CSX donates structure south of 30th St. → §5.5, §9 High Line Q, Freight-to-Fiber section.
- Query: `Special West Chelsea District 2005 rezoning High Line transfer corridor NYC Planning` · Firecrawl search → https://cbmanhattan.cityofnewyork.us/cb4/all-committees/special-west-chelsea/ (excerpt: City Council approved West Chelsea/High Line rezoning June 2005); https://zr.planning.nyc.gov/article-ix/chapter-8 (High Line Transfer Corridor) → §5, §7 card, §9 condo Q, Residential section.
- Query: `West Chelsea Historic District designated 2008 warehouses Landmarks Preservation Commission buildings Tenth Eleventh Avenue` · Firecrawl search → https://therealdeal.com/new-york/2008/07/16/west-chelsea-gets-landmark-status/ (excerpt: designated, W 25th–28th); https://www.citylandnyc.org/landmarks-considers-west-chelsea-district/ (excerpt: July 15 2008, seven blocks, West Side Highway to Tenth Ave); https://s-media.nyc.gov/agencies/lpc/lp/2302.pdf (designation report, not opened) → §5, §8.5 landmarks callout.
- Query: `Chelsea Historic District designated 1970 extension 1981 rowhouses Landmarks Preservation Commission` · Firecrawl search → https://hdc.org/buildings/chelsea-historic-district-extension/ (excerpt: designated Sept 15 1970, extended Feb 3 1981; Cushman Row Greek Revival town houses); https://chelseacommunitynews.com/2020/07/03/save-chelsea-plan-proceeding-determines-to-extend-the-chelsea-historic-district/ (excerpt: Greek Revival/Federal rowhouses; W 20th & 21st Sts, 9th–10th Aves landmarked since 1970) → §5, §7 rowhouse card, §9 rowhouse Q, Residential section.
- Query: `Starrett-Lehigh Building 601 West 26th Street truck elevators railroad freight 1931 landmark` · Firecrawl search + scrape https://en.wikipedia.org/wiki/Starrett%E2%80%93Lehigh_Building (metadata description): 601 W 26th St, full block 11th–12th Aves, W 26th–27th; built 1930–31 by Starrett Corp and Lehigh Valley Railroad; completed Dec 1931; 1.8M sq ft rentable; three freight elevators carried trucks to upper delivery bays; 40% vacant early 1970s; investor syndicate bought 1998, attracted dot-com then fashion firms; RXR since 2011. RXR brochure https://starrett-lehigh.com/wp-content/uploads/sites/25/2025/07/RXR_CRE_25028_Starrett-Lehigh_Generic-Brochure-V12.pdf (excerpt: 20' columns, 12'8" ceilings, 150–200 lb/sq ft floor load; not used on page) → §5, §5.5, §7, §13 card, Freight-to-Fiber, Studios section.
- Query: `Terminal Warehouse 261 Eleventh Avenue conversion offices railroad tunnel through building Chelsea` · Firecrawl search → https://terminalwarehouse.nyc/whats-happening/ (excerpt: built 1891; Tunnel nightclub 1986–2001); https://cookfox.com/projects/terminal-warehouse/ (excerpt: rail tunnel runs the length of the building); https://terminalwarehouse.nyc/ (excerpt: office and retail in the West Chelsea Historic District) → §5, §13 card.
- Query: `85 Tenth Avenue telecom carriers colocation data center fiber Chelsea building` · Firecrawl search → https://www.telehouse.com/global-data-centers/america/new-york-datacenters/telehouse-new-york-chelsea/ (excerpt: 85 10th Ave, 60,000 sq ft Tier 3 colocation); https://metanethosting.com/data-center-locations/new-york/85-tenth-avenue-manhattan/ (excerpt: connectivity to NYIIX peering exchange) → §5, Carrier Blocks section, §13 card.
- Query: `London Terrace Chelsea 1930 apartment complex number of apartments; Penn South cooperative 2,820 apartments 1962 Chelsea` · Firecrawl search → https://londonterracetowers.com/about/ (excerpt: 1,665 apartments within a single block); https://en.wikipedia.org/wiki/Penn_South (excerpt: 2,820 units in ten 22-story buildings, founded 1962); https://www.pennsouth.coop/faq-general-information-about-penn-south.html (excerpt: 2,820 units, close to 5,000 residents); https://streeteasy.com/complex/london-terrace-towers (excerpt: W 23rd and W 24th Sts) → §5.5, §7 co-op card, §13 card, Residential section, FAQ (shareholder Q).
- Gallery hours: https://agora-gallery.com/chelsea-galleries-itinerary/ (excerpt: "Tuesday through Saturday, 10am–6pm (most galleries)"); https://www.davidzwirner.com/galleries/new-york (excerpt: Sunday and Monday closed) → §5.5, Gallery Blocks section, FAQ Mondays.

### Local news / hyperlocal
- Query: `Fulton Elliott-Chelsea Houses redevelopment demolition new apartments Related Essence 2025 NYCHA` · Firecrawl search →
  - https://www.nyc.gov/site/nycha/about/pact/chelsea-fulton.page (excerpt): PACT partners Essence Development and Related; all 2,056 existing apartments to be replaced; ~3,500 new homes; >4,500 residents.
  - https://therealdeal.com/new-york/2026/07/10/related-essence-get-court-nod-for-nycha-chelsea-redev/ (excerpt, July 10 2026): state appellate court ruling lifted a pause; ~$2B overhaul; opponents sued.
  - https://www.thecityreporter.nyc/2026/09/21/nycha-fulton-elliott-chelsea-holdouts-manhattan/ (excerpt, Sept 2026): lease-termination notices to holdouts at Fulton 11 and Chelsea Addition. Not quoted on page.
  - https://newyorkyimby.com/2026/08/hud-approves-redevelopment-of-fulton-and-elliott-chelsea-houses-in-chelsea-manhattan.html (excerpt; disputed in comments) — NOT used on page because HUD approval is contested in the comments.
  → §5 (neutral one-line mention), §9 NYCHA Q, Residential section. Presented as contested; no position taken.
- https://www.nyc.gov/content/oti/pages/big-apple-connect (search excerpt): free internet to NYCHA developments; providers Spectrum and Optimum (silo research) → §9 NYCHA Q (worded "participating developments" because coverage of Fulton/Elliott-Chelsea specifically was not verified).
- Local news on Chelsea fiber-installation contractors 2026: EMPTY (none retrieved).

### Local codes / rules
- Query: `NYC Building Code 1023.5 penetrations interior exit stairway prohibited except electrical raceway serving stairway` · Firecrawl search → https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-174119 (excerpt: "Penetrations into or through interior exit stairways and ramps are prohibited except for equipment and ductwork necessary for independent ventilation or ..."); https://www.reddit.com/r/BuildingCodes/comments/1o7rl5q/egress_stairway_penetrations_nyc_bc_2022_10235/ (same text, NYC BC 2022) → FAQ (stairwell Q).
- LPC exterior-work permits: silo Manhattan research (LPC Permit Guidebook) reused → §8.5, §9 rowhouse Q.
- DOB / sub-50 V: existing site position (silo research) → §8.5.

### Pricing used (existing Manhattan prices only — copied from fiber-optic-installation-manhattan.html; nothing new)
$44 termination · $50 OTDR/strand · $453 MM drop · $517 SM drop · $5,625–$8,750 12-strand OM4 backbone · $10,000–$18,750+ 24-strand OS2 backbone · from $3,000 second telecom room · $195/hr, 3-hr min ($585). Packages are sums of these lines: Starter 2 × $517 = $1,034; Standard = the 12-strand OM4 line; Premium = 24-strand OS2 line + second room = $13,000–$21,750+.

### Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected; pool = library files containing `-westchester-county-` or `-rockland-county-` (distinct scenes only)
- fiber-optic-installation-chelsea-finished-rack-firewall-ups.webp ← fiber-optic-installation-westchester-county-finished-rack-ups.webp (hero)
- fiber-optic-installation-chelsea-corridor-cable-bundle-open-ceiling.webp ← fiber-optic-installation-rockland-county-corridor-bundle-idf.webp (§5)
- fiber-optic-installation-chelsea-patch-panel-termination-rack.webp ← fiber-optic-installation-rockland-county-patch-panel-punchdown.webp (§6)
- fiber-optic-installation-chelsea-hammer-drill-masonry-wall-penetration.webp ← fiber-optic-installation-rockland-county-hammer-drill-block-wall.webp (§7)
- fiber-optic-installation-chelsea-emt-conduit-loft-pull.webp ← fiber-optic-installation-westchester-county-emt-conduit-riser-pull.webp (Carrier Blocks)
- fiber-optic-installation-chelsea-inherited-closet-before-after.webp ← fiber-optic-installation-rockland-county-inherited-closet-before-after.webp (§9)
- fiber-optic-installation-chelsea-switch-rack-mounting.webp ← fiber-optic-installation-rockland-county-switch-sfp-rack-mount.webp (§10)
- fiber-optic-installation-chelsea-handheld-tester-pass-wall-jack.webp ← fiber-optic-installation-rockland-county-certification-tester-pass.webp (§12)
- fiber-optic-installation-chelsea-jhook-bundles-open-ceiling.webp ← fiber-optic-installation-westchester-county-jhook-open-ceiling-pathway.webp (§13)
- fiber-optic-installation-chelsea-ceiling-tile-cable-feed-office.webp ← fiber-optic-installation-westchester-county-ceiling-tile-cable-feed.webp (Gallery Blocks)
- fiber-optic-installation-chelsea-cable-boxes-staged-fitout-floor.webp ← fiber-optic-installation-rockland-county-reel-boxes-fitout-staging.webp (Lease checklist)
Skipped: port-labels-cable-map (readable printed document). All library photos show AESS technicians in branded shirts (faces visible on most) — same practice as the parent and area pages; no customer faces, house numbers, plates or documents.

### Keyword plan (Chelsea page)
Service: fiber optic installation Chelsea, fiber backbone, fusion splicing, OTDR testing, fiber audit. Problem: carrier stops at the dock, sublease separation, exhibition walls, landmark exterior, developer-controlled telecom room, inherited dot-com cable, block-long floors. Technology: OS2, OM4, armoured, OFNP/OFNR, micro cable, LC/SC, innerduct. Industry: galleries, studios/showrooms, media/tech tenants, co-ops/condos, storefront clinics/restaurants, theatres. Geographic: Chelsea, West Chelsea, High Line, 111 Eighth Ave, Chelsea Market, 85 Tenth Ave, Starrett–Lehigh, Terminal Warehouse, London Terrace, Penn South, Eighth Ave, W 23rd St, Hudson Yards edge.

### Question register additions — fiber-optic-installation-chelsea-manhattan-ny
§9 Questions Answered:
- Does being a few blocks from 111 Eighth Avenue make it easier to get fiber into our building?
- How can a tenant find out which carriers are already inside a Chelsea building before signing the lease?
- We sublet part of a floor from a larger tech tenant — can we have our own fiber, or do we have to ride theirs?
- Our suites sit at opposite ends of one huge terminal floor — should they share one telecom room or have two?
- How does new fiber get through the thick concrete floors of a former freight terminal?
- The old High Line viaduct runs through or right beside our building — can fiber be fixed to it or carried across it?
- Art handlers book the freight elevator for every show change — how does fiber work fit around installs and de-installs?
- Can fiber reach a gallery's office, viewing room and storage without crossing walls that are rebuilt for every exhibition?
- Where should fiber enter a Chelsea Historic District rowhouse with a stoop and an areaway?
- Our condominium's developer still controls the telecom room — what should the board ask for before it takes over?
- Our tenant association wants better internet at Fulton or Elliott-Chelsea Houses — what can an outside contractor actually do?
Other question headings: Chelsea Link Dark Before an Opening? (repair capture) · West Chelsea Fiber Down Right Now? (final repair)
§17 FAQ:
- Do you also work in the Meatpacking District, the Flatiron and Hell's Kitchen next door?
- How do you protect artwork, white walls and finished concrete floors while fiber goes in?
- Can fiber work be scheduled on Mondays, when most West Chelsea galleries are closed?
- Will drilling dust set off the building's smoke detectors?
- Can fiber run up through the stairwell to save time?
- Can you work inside a theatre or performance space without interrupting shows?
- What happens to the plan if the landlord rejects our first route?
- Can a Penn South or London Terrace shareholder hire you for work inside their own apartment?

## Brooklyn Navy Yard — local research (2026-10-17 batch, fiber-optic-installation-brooklyn-navy-yard-brooklyn-ny)

Neighbourhood page under /fiber-optic-installation-brooklyn (Brooklyn GBP, 1282 Troy Ave; phone (347) 934-8335; Brooklyn base 1.00x). Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md are reused; only Navy Yard research is added here. Thesis: the Yard is a gated, city-owned, single-landlord industrial campus, so tenant fiber is shaped by BNYDC's written rules (plan approval, gate credentials, freight hours, waste, roof, hallways), by four on-campus providers' handoffs, by 1940s concrete and 19th-century brick, and by the Sandy flood history (4–6 ft).

### Primary source — BNYDC Tenant Manual (2026)
- Query: `Brooklyn Navy Yard Development Corporation tenant contractor requirements work permit insurance construction` · Firecrawl search → https://www.brooklynnavyyard.org/wp-content/uploads/2026/06/Updated_Tenant-Manual-2026.pdf (Firecrawl scrape, PDF parser, 34 pages, read in full). Findings used:
  - Est. 1801; 165 years of shipbuilding; USS Maine, Arizona, Missouri; 70,000+ workers in WWII; decommissioned 1966 and bought by the City. 300 acres, NW Brooklyn, three miles of East River; 6.3 million sq ft (19th-century brick warehouses, waterfront, modern office/light industrial). → §5, §5.5.
  - Gates (table): Building 77 Flushing Ave entrance 24/7 peds/bikes (swipe 10 PM–6 AM); Building 3 Flushing Ave entrance 24/7 peds; Clinton Avenue Gate "Closed May 2026 — closed for critical repairs"; Sands Street Gate 24/7 cars/bikes/peds; Cumberland St varied; Clymer St varied. → FAQ "Clinton Avenue gate" answer.
  - BNYDC HQ Building 77, 141 Flushing Ave, Suite 801; Yard divided into three zones, each with its own property manager (names/emails NOT published on page). → §8 card, Rules section.
  - All tenant employees need BNYDC-issued ID; visitors via Eptura Visitor (formerly Proxyclick) QR single-day entry; "Recurring visitors or consultants working on long-term projects should NOT be registered via Eptura Visitor (Proxyclick). They should be given temporary ID cards, which are issued by BNYDC Security." Proxyclick visitor daily parking pass mentioned. → §9 Q "one-day registered visitors or temporary Yard ID cards", Rules section.
  - Electricity: plans for any work on tenant electrical equipment submitted to BNYDC and approved; licensed electrician required. → §8.5 callout.
  - Internet/Telecom: "The Yard is currently serviced by four internet/telecom providers" — Brooklyn Fiber, Crown Castle, Spectrum, Verizon; BNYDC grants access and facilitates a route into tenant spaces; coordinate with Property Manager on installation scope and telecom-closet access; other providers allowed; listed providers may not be in every building. → §5.5, Who Does What, §9 Q "four providers", Seven Things list.
  - Waste: contractor waste per Tenant Alteration Guidelines; penalties if left. → Rules section.
  - Packages must go to tenant spaces/mailboxes, not hallways; address formats (1 Brooklyn Navy Yard, Building #, Suite #, 11205; Building 77 = 141 Flushing Ave). → FAQ "materials shipped".
  - Freight cars shut 8 PM–5 AM weekdays, none weekends/federal holidays; after-hours $50/hr per car 8–11 PM weeknights, 4-hr minimum ($200) 11 PM–5 AM and weekends; request two business days ahead with building, date, time frame, car #. → Rules section, pricing driver (stated as BNYDC's charge, not an AESS price).
  - Ferry stop north side of Dock 72; B67 stops at Sands St gate near Wegmans, Market St, Clymer/Kent; speed limit 25 mph streets, 5 mph lots; no overnight parking except commercial vehicles. → §10.5 H3 3, landmarks.
  - Insurance COIs tracked by Jones (compliance company). Sublets need BNYDC written approval; approved subtenants may not sublet. → Rules section, Growing section.
  - Construction: plans submitted/approved before alterations; licensees may not make any alteration without approval; "Non-Material Alterations" (e.g. painting) exception — confirm with Property Management; obtain and close all permits; unapproved construction / unclosed permits = default. → §9 Q1, Q2, Q "paperwork closes out", §8.5.
  - Hallway storage prohibited (NYS Fire Code violation); roof use prohibited except emergencies unless lease grants roof. → §8.5.
  - Events: small ≤74 attendees, 14 days' notice; large 75+, 45 days; film/photo shoots outside premises 14 days. → Rules section.
  - Market @ 77 runs full length of Building 77 ground floor (Russ & Daughters among vendors); Brooklyn STEAM Center (NYCPS CTE, grades 11–12) in Building 77. Building 92 = welcome centre with workforce development and exhibitions. → §8 card, Industries section.
  - Multi-tenant buildings named in waste programme: 3, 5, 77, 131, 152, 212, 275, 280, 292, 303. → §7 card.

### Flood / resilience
- Query: `Brooklyn Navy Yard Hurricane Sandy flooding damage buildings tenants 2012 resiliency` · Firecrawl search → https://www.brooklynnavyyard.org/brooklyn-navy-yard-resilience-strategy/ (scrape, modified 2024-10-30): 550+ businesses, ~13,000 workers; 300 acres, 3.2 miles of waterfront; Sandy 14-ft surges, 80 mph winds; Yard inundated 4–6 ft; $100M damage; Dec 1992 nor'easter and Hurricane Ida (Sept 2021) also flooded; strategy with Ramboll Engineering, elevations up to 12–13 ft NAVD88; long-term measures (backflow preventers/pumps, deployable flood gates, flood-resilient structures, raised paths, planter seawall, elevated promenade); Resilience Tenant Toolkit five categories; image caption "Mezzanine levels to protect workstations and servers". → §5, §5.5, flood section, §10.5 H3 6, FAQ mezzanine.
- Same query → https://www.bkreader.com/policy-government/brooklyn-navy-yard-secures-287m-for-sandy-repairs-and-climate-resilience-10077818 (scrape, Jan 18 2025): $28.7M FEMA funding announced Jan 10 2025 to replace boilers and fuel oil tanks and elevate steam-generating structure; Building 41A took 48 inches of brackish water; electrical motors, wiring, plumbing, control systems damaged. → §5.5, §10.5 H3 6.
- Same query → https://www.seagrant.sunysb.edu/media/sandy12/TheLocal-Fort-Greene-Sandy121412.pdf (search excerpt only: Steiner Studios "did not suffer storm" damage). Not used.

### Buildings / landmarks
- Query: `Building 77 Brooklyn Navy Yard million square feet windowless warehouse converted history` · Firecrawl → https://urbannext.net/building-77/ (scrape, Marvel Architects project, 2018): built 1942, 16-storey reinforced concrete; windowless lower 11 floors; upper floors offices for Commandant and Navy oversight of North Atlantic Fleet; in National Register Brooklyn Navy Yard Historic District; new MEP/sprinkler/fire alarm; 4 refurbished + 4 new passenger elevators, four freight elevators, two 260-ft loading docks; 1 million sq ft; reopened 2017; ground floor designed for food production tenants. → §7, §8, §9 concrete Q, food-unit Q, landmarks. Also https://www.beyerblinderbelle.com/work/view/brooklyn-navy-yard-building-77/ (excerpt: new window wall into concrete envelope).
- Query: `Dock 72 Brooklyn Navy Yard 675,000 square feet office building completed 2018 16 stories` · Firecrawl → https://s9architecture.com/dock-72 and https://archello.com/project/dock-72 (excerpts: 16-storey, 675,000 sq ft); silo source (Brooklyn research) "built on the site of a former drydock". → §7, §8, landmarks.
- Query: `reddit Brooklyn Navy Yard internet office tenant Building 77 Dock 72 wifi` · Firecrawl → https://dock72.com/the-building/ (excerpt: "wired for broadband, WiFi, and a building-wide operating system; and designed for maximum resiliency"). → §8 card, §9 Q "advertised as wired for broadband".
- Query: `Steiner Studios Brooklyn Navy Yard sound stages number square feet largest film studio` · Firecrawl → https://www.steinerstudios.com/about/ (excerpt: opened Nov 2004; 780,000 sq ft; thirty soundstages incl. largest 27,000 sq ft on East Coast); https://en.wikipedia.org/wiki/Steiner_Studios (excerpt: "New York's largest production facility"). https://www.nyccip.com/projects/steiner-studios-phase-iii/ (Stages 31/32, 58-ft clear height) recorded, not used. → §7, §8, landmarks.
- Query: `Green Manufacturing Center Brooklyn Navy Yard Building 128 square feet manufacturing tenants` · Firecrawl → https://www.brooklynnavyyard.org/tenants/crye-precision/ (excerpt: "Crye employs over 200 people and is expanding into 85,000 square feet at the Yard's new Green Manufacturing Center, Building 128"). Brownstoner excerpt "250,000" ambiguous — not used. → §8, landmarks.
- Query: `Brooklyn Navy Yard Historic District National Register listed buildings Admiral's Row Wegmans Sands Street` · Firecrawl → https://en.wikipedia.org/wiki/Brooklyn_Navy_Yard (excerpt: whole yard NRHP historic district 2014; Quarters A 1807 federal-style commandant's house in Vinegar Hill, National Historic Landmark; 2016 nine of ten Admiral's Row houses torn down for 399 Sands St, Wegmans and parking; Wegmans opened 2019; Building 280 (1942) eight-storey former ordnance machine shop at Morris Ave & Sixth St near Cumberland entrance); https://www.brownstoner.com/development/admirals-row-brooklyn-wegmans-navy-yard-development/ (excerpt: Admiral's Row houses built 1860s–1901); https://www.brooklynnavyyard.org/wp-content/uploads/2024/03/BNY-BLDG-212_2023-Flyer-Final-302.pdf (excerpt: Building 212, anchored by Wegmans, "heart of the Navy Yard's new 500,000 SF multi-building retail, manufacturing, and creative office development"). → §7, §8, landmarks.
- Query: `BLDG 92 Brooklyn Navy Yard museum opened 2011 Marine Commandant's residence Flushing Avenue Carlton Avenue` · Firecrawl → https://www.brooklynnavyyard.org/public-spaces/ (excerpt: Building 92, 63 Flushing Ave at Carlton Ave; built 1858 as Marine Corps Commandant's Residence; opened to public 2011; Yard's first LEED Platinum building). → §8, landmarks.
- Query: `Brooklyn Navy Yard master plan 2018 5.1 million square feet new jobs WXY` · Firecrawl → https://www.brooklynnavyyard.org/developments-master-plan/ (scrape): $2.5B investment, 30,000 jobs, 5.1M sq ft vertical manufacturing; https://architizer.com/projects/brooklyn-navy-yard-master-plan/ (excerpt: WXY, 2018). → §5.5, Growing section.
- Query: `Vinegar Hill Historic District designated Landmarks Preservation Commission 1997 Hudson Avenue Front Street` · Firecrawl → https://www.nyc.gov/assets/lpc/downloads/pdf/maps/HistoricDistrictMaps/Brooklyn/vinegar_hill.pdf (excerpt: designated January 14, 1997, LP-1952); https://hdc.org/hdc-across-nyc/brooklyn/brooklyn-landmarked/dil-vinegar-hill/ (excerpt: early-20th-century industrial buildings also in district); Instagram LPC post excerpt (brick Greek Revival row houses, early 19th c.). → Outside the Gates section, FAQ.

### Providers
- Query: `Brooklyn Fiber Navy Yard buildings on-net tenants internet` · Firecrawl → https://bkfiber.com/campuses/brooklyn-navy-yard (scrape): "on-net operator across Brooklyn Navy Yard", "a new suite is usually live within days"; installs router inside the space; served addresses 299 Sands St, 141 Flushing, 60/62/63/70 Flushing, Building 293 Assembly Rd, 399 Sands St; business service only. Provider's monthly prices NOT used on the page. → Who Does What, §8 card, Move-in timeline (all attributed as provider claims).

### Reddit (local)
- Query: `reddit Brooklyn Navy Yard internet office tenant Building 77 Dock 72 wifi` · Firecrawl search → only https://www.reddit.com/r/NYCbike/comments/qby34x/brooklyn_navy_yard_between_kent_and_flushing_aves/ (excerpt about building security/biking; not about connectivity). Not used. Reddit on Yard connectivity: EMPTY (no relevant threads; reddit.com not scrapeable).

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitute for §10.5 reality check (claims quoted as published):
- Query: `campus fiber backbone between buildings industrial park installation guide armored cable direct burial conduit claims` · Firecrawl → https://www.ttifiber.com/blog/structured-cabling/campus-fiber-network-design (scrape, directQuote, published 2026-07-29): "Direct-burial cable exists but is rarely the right choice on an active campus — future excavation will find it, and repairs require digging"; conduit "sized at least 50% larger than current needs"; "Armored cable where conduit runs under roadways or parking lots". → §10.5 H3 1–3.
- Same query → https://www.csemag.com/fiber-optics-a-backbone-for-advanced-building-design/ (scrape, directQuote, 2015): armored cable "takes less space in a conduit or cable tray … gets pulled in once, whereas using fiber in innerduct typically requires separate placement". → §10.5 H3 4.
- Same query → https://getacg.com/blog/outside-plant-fiber-optic-installation-chicago-guide/ (search excerpt): NEC requires outdoor cables "to splice over to fire-rated indoor cables (like OFNP plenum lines) within 50 feet of entering a building"; extra conduit "protecting your real estate investment for the next 15 to 20 years". → §10.5 H3 5, 7.
- Query: `"fiber optic" cable saltwater flood damage connectors … Verizon replaced copper with fiber` · Firecrawl → https://www.cbsnews.com/newyork/news/verizon-upgrading-to-all-fiber-optics-after-copper-wiring-was-destroyed-in-sandy-storm-surge/ (excerpt: Broad Street vault; "All of the new fiber optic cables survived unharmed by the flooding"). → §10.5 H3 6.
- Yelp 1–3★ for Navy Yard fiber contractors: EMPTY (no query returned yelp.com results).

### Local news / hyperlocal
- BK Reader (Jan 2025 FEMA funding) above. Local news on Navy Yard fiber-installation contractors 2025–2026: EMPTY.

### Local licensing / permits
- BNYDC Tenant Manual (above): plan approval, licensee rule, permit close-out, electrical by licensed electrician, roof/hallway rules. Silo source: sub-50 V low-voltage cabling generally needs no DOB work permit (existing site statement). LPC for exterior work in Vinegar Hill and nearby historic districts. NEC bonding of metallic armor at building entry and the 50-ft OSP rule stated from general code knowledge (§10.5 H3 4–5) — flag for Anwar to confirm wording.

### Pricing used (existing published lines only, Brooklyn base 1.00x — copied from fiber-optic-installation-brooklyn.html)
$35/termination; $40/strand OTDR; $350 MM drop; $400 SM drop; 12-strand OM4 backbone $4,500–$7,000; 24-strand OS2 $8,000–$15,000+; second telecom room from $2,400; $195/hr, 3-hr min ($585). Worked examples: Starter $1,050 = 3 × $350; Standard $4,500–$7,000 = backbone line; Premium $8,000–$15,000+ = OS2 line; inherited-cable example $1,320 = 24 × $35 + 12 × $40. BNYDC after-hours freight fees quoted as the Yard's charges, not AESS prices.

### Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected; pool = library files with `-nassau-county-` / `-suffolk-county-`
crew-fitout-reels ← nassau-county-crew-fitout-cable-reels; ceiling-grid-bundle-feed ← nassau-county-ceiling-grid-bundle-feed; panel-termination-hands ← nassau-county-patch-panel-punchdown-hands; hardhat-stud-wall-pull ← nassau-county-hardhat-stud-wall-pull; floor-rack-patching ← nassau-county-idf-rack-patching; jhook-cable-pathway ← nassau-county-jhook-bundles-open-office; certification-tester ← nassau-county-certification-tester-wall-jack; wall-outlet-termination ← nassau-county-wall-plate-termination-office; van-reels-ladders ← suffolk-county-van-cable-reels-ladders; ceiling-access-point ← nassau-county-ceiling-access-point-cable; door-reader-wiring ← suffolk-county-door-reader-mounting (all prefixed fiber-optic-installation-brooklyn-navy-yard-). Skipped: nassau school-corridor (face in profile), suffolk storefront camera (readable store-hours sign), conference/video-wall/AV shots (not relevant).

### Keyword plan (Navy Yard page)
Service: fiber optic installation Brooklyn Navy Yard, tenant fiber, suite fiber, building-to-building fiber, fusion splicing, OTDR testing. Problem: BNYDC plan approval, gate credentials, freight hours, concrete coring, flood (Sandy 4–6 ft), wash-down units, provider handoff gap. Technology: OS2, OM4, armored indoor/outdoor, OFNR/OFNP, sealed enclosures, innerduct, SFP optics. Industry: manufacturers, design studios, food makers, media/production, schools/training, food-hall vendors. Geographic: Brooklyn Navy Yard, Building 77, Dock 72, Building 92, Building 128, Building 212, Building 280, Steiner Studios, Sands Street, Flushing Avenue, Cumberland Street, Clymer Street, Wallabout Bay, Vinegar Hill, Fort Greene, Clinton Hill, Wallabout.

### Question register additions — fiber-optic-installation-brooklyn-navy-yard-brooklyn-ny
§9 Questions Answered:
- Does low-voltage cabling inside our own Navy Yard suite still need BNYDC plan approval?
- We hold a BNYDC licence rather than a lease — does that change what fiber work we're allowed to do?
- Should our installers come in as one-day registered visitors or with temporary Yard ID cards?
- BNYDC lists four providers already on the Yard — does the one we pick change the fiber we need inside our space?
- Is a second internet subscription cheaper than linking our two Yard spaces with private fiber?
- Before coring a 1940s concrete floor in a Yard building, how do you avoid hitting rebar or buried conduit?
- Our new Yard office was advertised as wired for broadband — what fiber work is still left for us as the tenant?
- Our Building 77 food unit is washed down every night — where can the fiber equipment safely live?
- What paperwork closes out a fiber job at the Yard so it never becomes a lease problem?
§17 FAQ:
- Our business is across Flushing Avenue from the Yard, not inside it — do the Yard's rules apply to us?
- Do you also take fiber work in Vinegar Hill, Clinton Hill and Fort Greene, just outside the Yard?
- Can fiber materials be shipped to our Yard suite ahead of the install?
- If something needs adjusting after handover, how is a return visit to the Yard billed?
- Do you work directly for BNYDC, or only for tenants?
- With the Clinton Avenue gate closed for repairs, which entrance do your crews use?
- We're adding a mezzanine inside our unit, partly for flood protection — how does fiber get up to it?
- How do you keep noise and dust from bothering the tenant next door in a shared Yard building?
- Can a company in a coworking office at the Yard get its own fiber?
(No other headings end in "?"; repair/CTA headings are statements.)

## Jamaica, Queens — local research (2026-10-17 batch, fiber-optic-installation-jamaica-queens-ny)

Neighbourhood page under /fiber-optic-installation-queens (Bronx GBP, Queens line (347) 434-6392). Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md are reused where noted.
Page thesis: Downtown Jamaica is a railroad hub that grew a skyline — turn-of-the-century and inter-war buildings on Jamaica Avenue, courts and federal offices, post-2007 towers by the station, a 2025 rezoning about to add more — all sitting on Southeast Queens' rising groundwater. Fiber work here = sealed provider entrances, passive fiber in the cellar with active equipment lifted to a dry floor, owner risers in old masonry buildings, separate routes for tower podium/condo units, and documented strands.

### Reddit / forums (local)
- `reddit Jamaica Queens internet fiber building Fios not available Jamaica Ave apartment` · Firecrawl search (excerpts only; reddit.com not scraped).
  - https://www.reddit.com/r/verizon/comments/1u083m9/how_do_i_get_fiber_in_my_building_nyc/ — excerpt: "Fios service is available in your neighborhood just not in your building right now. Equipping your building with Fios may take up to 6-12 ..." (truncated in excerpt; only the visible words quoted) → §10.5 H3 2.
  - https://www.reddit.com/r/AskNYC/comments/1uhxwu9/why_is_it_so_hard_to_get_fios_on_the_uws_im/ — excerpt: "FIOS is in the streets - it's individual landlords/building owners which are not giving permission to Verizon to wire the building." → §10.5 H3 3.
  - https://www.broadbandsearch.net/service/new-york/jamaica — excerpt: "Is fiber internet available in Jamaica? Yes, fiber internet is available in Jamaica." → §10.5 H3 1.
  - No Jamaica-specific Reddit thread found. Local Reddit for Jamaica: EMPTY.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitutes for §10.5 (claims quoted as published): BroadbandSearch, r/verizon, r/AskNYC (above); silo sources thenetworkinstallers.com (FBA 2025 underground median $18.00/ft, aerial $8.00/ft; fusion splice $30–$75 and mechanical $15–$40 citing Ring and Ping; testing/documentation ≈5% citing Automation World) → §10.5 H3 4, 5, 6; atlantech.net timeline (distance to nearest fiber, building access, 15-month wait) → §10.5 H3 7. Angi/HomeAdvisor/Fixr: no fiber cost page (silo finding) — stated on page, not quoted.

### Landmarks, transit, buildings, corridors
- `Jamaica Station LIRR AirTrain JFK opened 2003 daily riders hub` · Firecrawl search → https://www.governor.ny.gov/news/governor-hochul-launches-customer-survey-shape-project-reimagine-jamaica-station (scraped; April 10, 2026): ~200,000 daily riders on LIRR, AirTrain, subways, buses; "fourth busiest commuter rail station in North America"; >1,000 subway and LIRR trains every weekday; 790 trains stop, +54% from 481 before Grand Central Madison; last upgraded 2003 with AirTrain; $50M in FY2027 Executive Budget for redesign planning (PANYNJ + MTA); survey April 10–May 8 2026; "Sutphin Archer Subway Station". → §5 para 1, §5.5, §13 card, Station Area section.
  - Same query → https://en.wikipedia.org/wiki/AirTrain_JFK (excerpt): opened December 17, 2003. Not used beyond "2003".
- `Jamaica station` Wikipedia (scraped with query) → https://en.wikipedia.org/wiki/Jamaica_station: junction of Main Line, Atlantic Branch, Montauk Branch; built 1912–1913; six platforms, ten tracks; AirTrain two tracks one platform; weekday ridership >200,000; Feb 2023 Brooklyn service converted to shuttle using new Platform F south of existing platforms; address 93-02 Sutphin Boulevard. → §5 para 1, §13 card, Station Area section.
- `Jamaica Center–Parsons/Archer station` Wikipedia (scraped) → https://en.wikipedia.org/wiki/Jamaica_Center%E2%80%93Parsons/Archer_station: opened December 11, 1988; E and J all times, Z rush hours; Archer Avenue Lines. → §5 para 1, §8 card (165th Street).
- `Jamaica Neighborhood Plan rezoning City Council approved homes Downtown Jamaica` · Firecrawl search →
  - https://www.cozen.com/news-resources/publications/2025/new-york-city-council-approves-jamaica-neighborhood-plan (scraped; Nov 3, 2025): approved Oct 29, 2025; ~230 blocks; largest MIH area; >2M sq ft commercial/community facility; ~11,800 units, ~4,200 affordable; five sub-areas (Downtown Core high-density commercial/towers; North Core between Jamaica Ave and Hillside Ave medium-density mixed use with community facilities on lower floors; Southern Corridors on Merrick, Guy R. Brewer, Sutphin; South Core south of LIRR east of Sutphin mixed residential/light manufacturing; Industrial Areas along Liberty Ave kept industrial at higher density); expands Special Downtown Jamaica District with school height/floor-area bonuses and open-space bonuses; $413M area-wide funding; largest neighbourhood rezoning in 20+ years. → §5 para 3, §5.5, §7 cards, Q&A (Liberty Ave question), Rezoning Timeline section, Terms section.
  - https://council.nyc.gov/press/2025/10/09/2986/ (scraped; Oct 9, 2025): committee approval; $413M investments; $78M Jamaica Avenue renovation Sutphin Blvd–168th Place; $13M 165th Street shared street; $17.9M plaza at western end of Archer Ave bus terminal; $5.75M canopy removal; $47M Station Plaza; $315M sewer upgrades; $16M CUNY for York College groundwater intrusion; $7M community-facility basement reconstruction for flood prevention; $9.4M JCAL elevators; >$8M King Manor restoration, $17.5M Rufus King Park; DHS commitment to review whether Jamaica-area commercial hotel contracts can return to tourism; technical assistance for faith-based organisations' affordable housing; relocation of Allen AME Theodora Jackson Older Adult Center; DOHMH building on Parsons Blvd; NYC H+H/Queens Claire Shulman Pavilion $70M. → §5.5, §8 cards, groundwater section, Q&A (Jamaica Ave rebuild; hotel; free Wi-Fi context), Station Area, coverage cards, "Beyond the Downtown" section.
  - https://queenseagle.com/all/2025/10/10/... and https://www.jamaicaplan.nyc/ (excerpts only). Not used.
- `Jamaica Now Action Plan 2015 Downtown Jamaica $153 million` · Firecrawl search → https://edc.nyc/project/Jamaica-Planning-Initiative (excerpt: "$153 million strategic economic development investment"); https://www.nyc.gov/html/dot/html/pr2018/pr18-033.shtml (excerpt: "$153 million dollar neighborhood revitalization initiative announced in 2015"); https://qns.com/2015/04/downtown-jamaica-development-plan-unveiled/ (excerpt: 21 strategic actions, $153M). → §5.5, Rezoning Timeline 2015.
- 2007 Downtown Jamaica rezoning: silo source https://citylandnyc.org/jamaica-rezoning-approved-with-modifications (Council approved Aug 22 2007; upzone core/shopping district; near AirTrain/LIRR). → §5 para 3, Rezoning Timeline 2007.
- `The Crossing at Jamaica Station BRP towers apartments ... completed` · Firecrawl search → https://www.fxcollaborative.com/projects/155/the-crossing-at-jamaica-station (scraped): "One of the first major construction projects following the neighborhood's rezoning"; corner of Archer Ave and Sutphin Blvd across from LIRR; 600,000 sf 28-storey, 539 units on three-storey retail/parking podium; 170,000 sf 14-storey, 130 units with community facility space; completion 2021; client BRP. (CityRealty/StreetEasy excerpts conflict — 669 units/25 storeys/2019 vs 539/28/30 storeys; architect's figures used.) → §5 para 3, Rezoning Timeline 2007.
- `Joseph P. Addabbo Federal Building ... SSA Northeastern Program Service Center` · Firecrawl search → https://www.ssa.gov/ny/services-nepsc.htm (scraped): NEPSC in Addabbo Federal Building, 155-10 Jamaica Ave, Jamaica NY 11432; ~9.4 million RSDI beneficiaries; ~1.5 million actions FY2021. → §8 card, §13 card, Civic Neighbours section.
- `Queens County Supreme Court civil 88-11 Sutphin ... Civil Court 89-17 Sutphin` · Firecrawl search → https://www.nycourts.gov/courts/11th-judicial-district (excerpt: Civil Court 89-17 Sutphin Blvd; Supreme Civil 88-11 Sutphin Blvd); https://www.nyc.gov/site/dcas/business/dcasmanagedbuildings/queens-civil-courthouse.page (scraped): built 1997, Perkins Eastman, limestone/granite/glass, two wings, glass lobby, plaza unifying it with older Supreme Courthouse across the street; Civil, Small Claims, Landlord/Tenant courts; 230-seat jury auditorium. → §7 card, §8 card, §13 card, Civic Neighbours section.
- `Jamaica Center Business Improvement District 165th Street Mall Jamaica Avenue retail corridor` · Firecrawl search → https://jamaicacenter.org/ (scraped): "Jamaica Avenue, with over 400 businesses"; three performing arts centres, landmarked historic buildings, Rufus King Park, two colleges, transport hub. https://www.downtownjamaica.org/about-the-bid/what-we-do (excerpt: Downtown Jamaica Partnership BID covers former 165th St Mall, Jamaica Center and Sutphin BIDs) — not used. → §5.5, §8 card.
- `Jamaica Savings Bank Sutphin Boulevard landmark ...` · Firecrawl search →
  - https://en.wikipedia.org/wiki/Jamaica_Savings_Bank_Building_(Sutphin_Boulevard) (scraped): 146-21 Jamaica Ave; Art Deco, built 1938–39; opened April 22, 1939; architect Morrell Smith; carved eagle over entrance, bronze doors; NYC landmark designated Oct 26, 2010; main office at 161-02 Jamaica Ave NRHP 1983 and NYC landmark 2008. → §7 card, §8.5 landmarks, §13 card.
  - https://archive.nytimes.com/cityroom.blogs.nytimes.com/2008/02/12/at-last-1898-jamaica-bank-building-is-a-landmark/ — excerpt only (scrape refused by Firecrawl): "The Jamaica Savings Bank, a Beaux Arts building completed in 1898, was designated a landmark. Mid-block at 161-02 Jamaica Avenue". → §7 card.
- `Jamaica Center for Arts & Learning` Wikipedia (scraped with query) → 161-04 Jamaica Ave; former Office of the Register (Queens Register of Titles and Deeds); Neo-Italian Renaissance; NYC landmark and NRHP; galleries, studios, 99-seat theatre. (Build year given as 1904 / 1895–1913 — no year used on page.) → §8.5, §13 card.
- `King Manor` Wikipedia (scraped with query) → 150-03 Jamaica Ave; Rufus King acquired 1805, expanded to 17-room mansion; Rufus King Park 11.5 acres; NHL, NRHP, NYC landmark. → §8.5, §13 card.
- `York College CUNY Jamaica campus acres FDA Northeast regional laboratory building` · Firecrawl search → https://www.york.cuny.edu/about/buildings (scraped; revised Sept 24, 2026): Academic Core 94-20 Guy R. Brewer Blvd; Performing Arts Center 94-45 Guy R. Brewer; FDA Building 158-15 Liberty Ave (New York Human and Animal Food Laboratory); campus near Jamaica Center station and LIRR. https://www.hines.com/properties/food-and-drug-administration-facility-jamaica (excerpt: 224,000 sf FDA office/lab at Liberty Ave & 158th St) — not used. → §7 card, §8 card, §13 card.
- `Jamaica Hospital Medical Center ... NYC Health + Hospitals Queens` · Firecrawl search → https://www.health.ny.gov/professionals/ems/state_trauma/trauma2.htm (excerpt: Jamaica Hospital Medical Center Level I, 8900 Van Wyck Expy); https://www.nychealthandhospitals.org/locations/queens/ (excerpt: 82-68 164th Street). Not used on page beyond FAQ generality ("courthouses and hospitals").

### Local news / hyperlocal (groundwater)
- `Southeast Queens rising groundwater basements flooding Jamaica York College groundwater intrusion` · Firecrawl search →
  - https://www.sqrejc.org/blog/46ww7yjqibto0zza37uiljp2agur8a (scraped; Bill Scarborough, Jan 10 2024, Southeast Queens Residents Environmental Justice Coalition): Jamaica Water Supply Co. pumped ~60M gallons/day from 69 wells for 100+ years; DEP bought JWS and phased out wells, connecting the area to upstate reservoirs; "Former DEP Commissioner Emily Lloyd testified in 2007 that since 1996, the groundwater level in Southeast Queens had risen by 35 feet." → §5 para 4, §5.5, Groundwater section.
  - https://www.qchron.com/editions/queenswide/york-college-still-hit-by-heavy-flooding/article_3472f8ea-9bc3-5e24-a144-d889e2e279a2.html (scraped metadata; Richard Heaton, Queens Chronicle, Sept 26 2019): "When entering the York College boiler room, you have to trek around puddles of water that are scattered throughout the sub-basement of the Academic Core building." → Groundwater section.
- Silo source re-used: NYC Council internet-access data, CD12 Jamaica–St. Albans–Hollis 41% no broadband subscription → §5.5, Q&A (free Wi-Fi question).
- Queens Chronicle / QNS / Patch items on fiber-installation contractors in Jamaica 2026: EMPTY (none retrieved).

### Local licensing / permits
- No Jamaica-specific permit source. Silo sources reused: sub-50 V cabling generally no DOB permit (site's structured-cabling-pricing statement) + firestopping (unifinerds/nyflnerds) → §8.5; LPC concern limited to exterior work (silo LPC sources) + designations above → §8.5. Street/sidewalk work stated as provider/city territory; page claims no street permits. Condominium declarations/bylaws governing common elements: general statement, no source quoted.

### Pricing used (existing AESS prices — no new prices)
All lines copied from the parent page fiber-optic-installation-queens.html (table in §14): $37/termination; $42/strand OTDR; $391 MM drop; $447 SM drop (Queens configurator); $4,725–$7,350 12-strand OM4 backbone; $8,400–$15,750+ 24-strand OS2; from $2,520 second telecom room; $195/hr, 3-hr min ($585).
Packages (sums of published lines only): Starter $1,062 = 2 × $447 + 4 × $42; Standard $7,245–$9,870+ = $4,725–$7,350 + $2,520; Premium $9,294–$16,644+ = $8,400–$15,750+ + 2 × $447. BYOE = $195/hr, 3-hr min. (Parent-page CONFLICT note on $391/$447 vs §9 1.05× still applies.)

### Images (11) — permanent image rule; Drive folder empty, CompanyCam not connected
images: 11 reused from images/fiber-optic-installation/ pool (putnam-county files, originally borrowed from earlier silos — no real Fiber Optic Installation photos yet). All 11 chosen because they show no face (hands/arms only); the orange-county and ulster-county pool files were skipped because they show faces in profile. Caveat as on earlier fiber pages: library photos look AI-generated (Cat6 boxes, branded tees); none shows fiber glass except yellow jumpers in one rack.
| New file (images/fiber-optic-installation/) | Source | Shows |
|---|---|---|
| fiber-optic-installation-jamaica-sfp-switch-rack-mount.webp | fiber-optic-installation-putnam-county-sfp-switch-seated-rack.webp | hands seating a 24-port switch with SFP slots in a rack |
| fiber-optic-installation-jamaica-hammer-drill-wall-entry.webp | fiber-optic-installation-putnam-county-hammer-drill-block-entry.webp | hammer drill with dust hose boring block wall beside conduit |
| fiber-optic-installation-jamaica-conduit-sweep-block-wall.webp | fiber-optic-installation-putnam-county-emt-sweep-cable-pull.webp | gloved hands feeding cable into EMT sweep on block wall |
| fiber-optic-installation-jamaica-corridor-cable-bundle-lift.webp | fiber-optic-installation-putnam-county-bundle-lift-open-ceiling.webp | strapped cable bundle lifted to corridor ceiling grid |
| fiber-optic-installation-jamaica-jhook-bundles-ceiling-grid.webp | fiber-optic-installation-putnam-county-jhook-bundles-above-grid.webp | bundles laid into J-hooks above ceiling grid |
| fiber-optic-installation-jamaica-rack-before-after.webp | fiber-optic-installation-putnam-county-rack-before-after-rebuild.webp | before/after closet rebuild |
| fiber-optic-installation-jamaica-tone-probe-trace.webp | fiber-optic-installation-putnam-county-tone-probe-panel-trace.webp | tone probe and toner at a patch panel |
| fiber-optic-installation-jamaica-rack-yellow-jumpers.webp | fiber-optic-installation-putnam-county-rack-yellow-patch-ups.webp | finished rack with yellow fiber jumpers |
| fiber-optic-installation-jamaica-tester-pass-outlet.webp | fiber-optic-installation-putnam-county-tester-pass-wall-outlet.webp | certification tester PASS at wall outlet |
| fiber-optic-installation-jamaica-patch-cord-label.webp | fiber-optic-installation-putnam-county-patch-cord-label-applied.webp | label wrapped on patch cord |
| fiber-optic-installation-jamaica-patch-panel-punch-tool.webp | fiber-optic-installation-putnam-county-punchdown-panel-hands.webp | punch-down tool at Cat6 patch panel |

### Keyword plan (Jamaica page)
Service: fiber optic installation Jamaica Queens, building fiber backbone, owner riser, sealed building entrance, fusion splicing, OTDR testing, strand map. Problem: groundwater/damp cellar, open entrance ducts, abandoned provider drops, unsealed floor holes, neighbouring redevelopment, street reconstruction, hotel re-opening, no home internet (CD12). Technology: OS2, OM4, indoor/outdoor water-blocked cable, armoured fiber, OFNP/OFNR, gasketed enclosures, duct plugs, SFP optics, LC/SC/MPO. Industry: avenue retail and upstairs offices, law/professional offices near courts, schools/training centres/clinics, towers and commercial condos, hotels, houses of worship, Liberty Avenue industrial. Geographic: Jamaica, Downtown Jamaica, Jamaica Center, Jamaica Avenue, Sutphin Boulevard, Archer Avenue, 165th Street, Parsons Blvd, Merrick Blvd, Guy R. Brewer Blvd, Liberty Avenue, Hillside Avenue, Jamaica Estates, Jamaica Hills, Briarwood, Hollis, St. Albans, South Jamaica, Rochdale Village, Springfield Gardens, Richmond Hill, Kew Gardens.

### Question register additions
fiber-optic-installation-jamaica-queens-ny
§9 Questions Answered (and other question headings):
- Fiber Down Between Sutphin and 168th Street? (repair capture heading)
- Groundwater keeps rising through our cellar floor — can it follow the provider's conduit into the building, and how is that stopped?
- Our cellar is damp every day of the year rather than flooding now and then — which cable, enclosures and patch cords stand up to that?
- The city is rebuilding Jamaica Avenue in front of our building — should we use the moment to prepare a better way in for providers' fiber?
- A neighbouring lot is about to be cleared for a new building, and our internet arrives through it — how do we protect the service before demolition starts?
- Our hotel near the AirTrain is going back to welcoming travellers after years of other use — what should be checked in its network before guests return?
- Many of our tenants have no home internet — can the building's backbone feed a free Wi-Fi spot in a lobby or community room?
- We bought a commercial condominium at the base of a new Jamaica tower — does our fiber have to come through the residential building's telecom room?
- Our Liberty Avenue industrial building is adding a floor of offices above the shop — how should fiber reach the new floor while the work floor keeps running?
- Want the Entrance Sealed and the Riser Drawn Before You Sign a Lease? (mid-page CTA heading)
§17 FAQ:
- Do you cover Jamaica Estates, Hollis, St. Albans and South Jamaica as well as the downtown blocks?
- Will you leave spare innerduct so a second provider can come in later without new drilling?
- Can you move the provider's terminal out of our wet cellar, or does the provider have to do that?
- Does the room that holds the fiber enclosure need a dehumidifier or a fan?
- Should our building's backbone be finished before or after the provider turns on its service?
- What size of conduit should a developer leave between floors for future fiber?
- How long does a walkthrough of a Jamaica building take, and who should be there?
- Do you keep a copy of our strand map and test results after the job?
- Will your crew sign a confidentiality agreement before working in an office that holds client files?
- How is the shop on the ground floor protected while the riser goes in above it?

De-dup notes: checked by meaning against every question heading/FAQ on the 16 live fiber pages (not only the register, which lags) and the parallel Chelsea / Brooklyn Navy Yard files as they stood mid-build. Deliberately avoided: Manhattan "main fiber room in a flood-prone cellar" (my cellar questions are about duct sealing and chronic humidity materials), Brooklyn "fiber underwater / what to replace after a flood", Orange "second-floor office over a storefront without running through the shop" (my FAQ is about protecting the shop during work), Orange "hotel without taking rooms out of service" (mine is post-other-use inspection), Westchester "New Rochelle developer timing" and Bronx "items on architect's drawings" (my conduit-size FAQ is a specific sizing answer), Staten Island "city sidewalk work disturbing owned fiber" (mine is using a street rebuild to prepare an entrance), Rockland "two buildings across a county road" / Dutchess railroad, Queens "free provider wiring offer", Queens "7 train vibration". Closest calls for a human read: my neighbour-redevelopment question vs Staten Island shared-driveway permission; my free-Wi-Fi question vs Brooklyn "will a backbone lower what tenants pay"; my backbone-before-provider FAQ vs Brooklyn "coordinate with the internet provider".

### Facts for Anwar to verify
- Groundwater "35 feet since 1996" is the SQREJC blog's report of 2007 DEP testimony (secondary source).
- Jamaica Plan figures (230 blocks, ~11,800 homes, $413M, $78M Jamaica Ave etc.) are from the Council's Oct 9 2025 committee release and Cozen's summary of the Oct 29 vote; final adopted numbers may differ slightly.
- The Crossing unit/storey counts follow FXCollaborative (539 + 130 units; 28 + 14 storeys; 2021); listing sites disagree.
- 1898 date for the 161-02 Jamaica Savings Bank is from a NYT City Room excerpt (page not scraped).

## Financial District, Manhattan — neighbourhood research (2026-10-17 batch, fiber-optic-installation-financial-district-manhattan-ny; includes this page's question-register additions)

### Financial District, Manhattan — local research (2026-10-17 batch, fiber-optic-installation-financial-district-manhattan-ny)
Neighbourhood spoke under /fiber-optic-installation-manhattan. Phone (929) 560-0737, Bronx GBP. Silo-wide findings and the Manhattan section above are reused (Empire City Subway 1891, carrier hotels, Verizon end-2013 premises-passed figures, cost-guide claims, comptroller conversion counts, CBS Verizon/Sandy, structured-cabling prices). Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. Platform for every entry below: WebSearch (result list) then WebFetch (page read) unless marked otherwise.

**Thesis:** a Financial District backbone has to be designed to be separated, moved and kept dry — towers change occupancy (two conversion waves), cellars sit behind post-Sandy flood barriers, and the street grid/security perimeter controls access. Not a geo-swap of the Manhattan page (that page's thesis is building rules/riser paperwork).

#### Reddit (local) — EMPTY (not accessible in build env)
No new Reddit thread was opened for FiDi. Silo-level r/AskNYC excerpt ("It's on the ISP to wire your building…", https://www.reddit.com/r/AskNYC/comments/1tez8o2/incorrectly_wired_internet_cables_in_building/) reused → §10.5 H3 5.

#### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
§10.5 substitutes: claims published by cost guides / carrier pages already recorded in the silo file (thenetworkinstallers FBA medians $18/ft underground, $8 aerial, ~5% testing; lowvoltagenewyork fusion splices $50–$150; AT&T 4–6 h / T-Mobile up to 4 h; Quantum Fiber multifamily 30/30/40–60 days; Atlantech 15-month wait). Angi/HomeAdvisor/Fixr: EMPTY (silo query returned none; stated on page).

#### Neighbourhood data
- Query `Downtown Alliance Lower Manhattan real estate market overview 2025 residents office inventory` · https://downtownny.com/research/2025-lower-manhattan-real-estate-year-in-review/ — 2025 leasing 4.75M sf ("most active year since 2019"); vacancy 22.2% (Class A 21.1%); residents passed 70,000 for the first time; Q4 hotel occupancy 90% and record ADR $384.93; 90 retail openings in 2025. → §5 para 4 + §5.5 facts; Mixed-use section (hotel ADR/occupancy, 90 retail openings).
- Same query · https://downtownny.com/research/lower-manhattan-real-estate-overview-q2-2025/ — largest Q2 2025 deal 193,000 sf at 1 World Trade Center (financial services tenant); vacancy 22.8%. → §8 WTC card; Battery Park City/WTC section.
- Query `1995 Lower Manhattan revitalization plan 421-g tax incentive office to residential conversions number of units` · https://cbcny.org/research/potential-office-residential-conversions — 1994 Giuliani plan + 1995 state package; 98 office buildings, 12.8M sf, 12,865 units; 28 buildings in first 3 years; permits before June 2006, construction by 2013. → §5 para 1, §5.5, Two Conversion Waves section, FAQ 7.
- Query `City of Yes for Housing Opportunity office conversions buildings built before 1991 expanded eligibility` · https://www.cozen.com/news-resources/publications/2024/city-of-yes-for-housing-opportunity-approved-by-the-city-council — approved Dec 5 2024; conversion provisions now apply to buildings built before 1991 in most areas (previously pre-1961, parts of Manhattan/Brooklyn/Queens). Also https://www.nyc.gov/assets/planning/download/pdf/plans-studies/city-of-yes/housing-opportunity/housing-opportunity-guide-conversions.pdf (DCP guide). → §5 para 1, Two Conversion Waves section.
- Query `Financial District office to residential conversion 2025 2026 Broad Street Wall Street Maiden Lane conversion units 467-m` · https://newyorkyimby.com/2026/03/61-broadway-readies-for-796-unit-office-to-residential-conversion-in-financial-district-manhattan.html — 61 Broadway, 33 storeys, 1913 Adams Express (Francis Kimball), National Register; 796 rentals, ~200 affordable under 467-m; work to start March 2026, first units H1 2028. → §5.5, §7 card, §13 landmark card, conversion section.
- Same query · https://www.6sqft.com/former-home-of-new-york-stock-exchange-in-fidi-to-become-nearly-400-apartments/ — 40 Exchange Place (1893, 20 storeys) 382 apartments; permit filed July 9 2025; still office, vacating date unclear. → §7 card, §9 Q "floors above converted while we stay".

#### Flooding / resilience
- Query `One New York Plaza Hurricane Sandy flooded basement telecom equipment relocated` · https://therealdeal.com/new-york/2012/11/01/trd-survey-more-than-17-million-sf-of-downtown-office-space-shuttered-in-sandys-wake/ — at least 17.3M sf in at least 15 east-side buildings closed with flooded basements: 55 Water (3.6M sf), 1 NY Plaza, 2 Broadway, 4 NY Plaza, 90 Broad, 60 Broad, 120 Wall, 180 Maiden Lane; water pumped from tunnels under Pearl Street where communications lines flooded. → §5 para 2, §5.5, Floodline section.
- Query `Lower Manhattan building flood barriers installed after Sandy Water Street office tower deployable flood wall` · https://www.constructiondive.com/news/54-story-nyc-tower-installs-bathtub-flood-protection-system/245538/ — 55 Water St, 54 storeys, 3.8M sf; removable posts-and-panels "bathtub" for 8 ft of water; stored in basement; 30 workers, 8 hours (2014). → §5.5, Floodline section, §13 card. (Page says ">3.5 million sf" in §7 to reconcile 3.6M/3.8M sources.)
- Same query · https://en.wikipedia.org/wiki/Lower_Manhattan_Coastal_Resiliency — FiDi–Seaport master plan 2021; 15–20 years, $5–7B, funding not secured as of late 2025; BPC resiliency $1.6B; South BPC/Wagner Park reopened July 2025 ($300M); North/West BPC site work late 2025, completion 2031. → Floodline section, BPC/WTC section.
- Query `dry floodproofing wall penetrations conduit sealing FEMA floodproofing utilities penetrations seals` · https://www.cedengineering.com/userfiles/S06-005%20-%20A%20Guide%20to%20Dry%20Floodproofing%20Homes%20-%20US.pdf — measures "only as good as their weakest link"; identify number/size/location of penetrations below DFE; sealants/membranes reduce seepage. FEMA EMI page https://emilms.fema.gov/is_0280/groups/152.html → EMPTY (file not found). → Floodline section, §9 flood-barrier Q.
- Query `NYC Building Code Appendix G flood-resistant construction utilities equipment above design flood elevation substantial improvement` · https://www.nyc.gov/assets/buildings/pdf/presentations/bsls22-flood_resistant_construction.pdf — Item 10.2.2.3: new equipment in existing non-residential spaces below DFE must be designed/isolated so as not to affect building components if submerged; no mention of telecom. → §8.5 compliance, §9 entry-room relocation Q.
- CBS New York Verizon/Broad Street vault quote (silo Manhattan section) reused → Floodline section closing paragraph.

#### Streets, access, landmarks
- Query `Wall Street security zone NYSE vehicle barriers sally ports restricted vehicle access streets` · https://tribecatrib.com/content/downtown-alliance-targets-street-mess-around-ny-stock-exchange (Jan 31 2017) — fence along Wall St between Broad and Broadway; checkpoints incl. Broad St; installed after 9/11; Downtown Alliance failed to shrink zone; vehicle access rules not described. → §5 para 3, §9 Q1, §13 card. (Page says checkpoint rules are set by police and change — no procedures invented.)
- Query `Stone Street Financial District one of oldest streets first paved narrow colonial street grid` · https://en.wikipedia.org/wiki/Stone_Street_(Manhattan) — cobbled 1658, first in New Amsterdam; renamed 1794; LPC historic district 1996, NRHP 1999; eastern block pedestrian, closed to vehicles in summer for dining; Greek Revival 1830s buildings after Great Fire of 1835; 1 Hanover Square NHL; 85 Broad St (1983) lobby preserves street path. → §5, §5.5, §7, Oldest Blocks section, §13 card.
- Query `Equitable Building 120 Broadway 1915 led to 1916 zoning resolution floor area` · https://en.wikipedia.org/wiki/120_Broadway — completed 1915, ~1.2M sf, helped spur 1916 Zoning Resolution. → §7, §13 card.
- Query `South Street Seaport Historic District designated 1977 blocks buildings Landmarks Preservation Commission` · nyclandmarks.lunaimaging.com result list only — confirms district name; designation year NOT verified, so page names the district without a year.
- Query `75 Broad Street data center carrier hotel Lower Manhattan colocation` · https://baxtel.com/data-center/epsilon-ny-75-broad — historic ITT carrier hotel; NYI "Broad Street Connect" launched Q4 2023 with JEMB Realty; Verizon colocation on 7th floor. → §9 latency Q, §13 card.

#### Building construction / technical
- Query `terra cotta flat arch floor construction early New York skyscrapers hollow clay tile coring` · https://en.wikipedia.org/wiki/Structural_clay_tile — flat arches between steel/iron beams; declined after 1910 as reinforced concrete and metal deck spread; no longer manufactured, not replaced. Nothing on drilling. → §7 card + methods, §9 clay-tile Q (page says "many" towers "before about 1910" and that we confirm by inspection; not claimed for any named building).
- Query `underfloor duct system cellular steel floor deck telephone power 1960s office buildings` · https://www.econline.com/doc/cellular-underfloor-duct-system-0001 — cellular underfloor duct for data, voice, power in separate compartments, hatches. Era not sourced → page does not date it. → §7, §9 underfloor Q.
- Query `raised access floor cabling NEC Article 645 information technology equipment room underfloor cable requirements` · https://cablinginstall.com/design-install/cabling-installation/article/16468180/raised-floor-cabling-standards — if room meets NEC 645-2, other cable types allowed; otherwise plenum listing rules (800-51/770-51) apply. → §9 raised-floor Q, §10 table.
- Query `NYC building code auxiliary radio communication system ARCS FDNY requirement high-rise buildings` · https://www.ny-engineers.com/auxiliary-radio-communication-system-design — BC requires in-building radio in all new high-rise buildings since 2015; radiating cable in stairways/corridors/shafts; DAS over fiber; riser diagram to FDNY; licensed master electrician installs; FCC licence for commissioning. → §8.5, §9 ARCS Q.
- Query `distributed antenna system DAS fiber backbone in-building cellular coverage office tower how it works head-end remote units` · https://www.belden.com/blog/how-in-building-das-works — 600–2700 MHz signals don't travel well through building materials; head-end combines carriers onto single-mode fiber to a remote unit per floor; coax to antennas. → §6 card, §9 (statement H3, not a question — LIC page asks the cellular question).
- Query `speed of light in optical fiber about 5 microseconds per kilometer latency` · https://www.commscope.com/globalassets/digizuite/2799-latency-in-optical-fiber-systems-wp-111432-en.pdf — 5 µs/km; equipment latency independent of distance; colocation operators equalise link latency. → §9 latency Q.
- Query `23 NYCRR 500.13 asset inventory requirement November 1 2025 DFS cybersecurity regulation` · https://www.hlc.com/en/publications/nydfs-final-set-of-cybersecurity-requirements-under-amended-part-500-take-effect-november-1-2025 — from Nov 1 2025 written inventory procedures; track owner, location, classification, support expiration date, RTO; kept in one place. → §9 DFS Q (stated as not legal advice).

#### Local news / hyperlocal on fiber contractors in FiDi — EMPTY (none retrieved beyond the items above).

#### Pricing used (existing Manhattan page lines only — no new prices)
$44 termination · $50 OTDR/strand · $453 MM drop · $517 SM drop · 12-strand OM4 backbone $5,625–$8,750 · 24-strand OS2 $10,000–$18,750+ · second telecom room from $3,000 · $195/hr, 3-hr min ($585). Worked totals on page: Starter $776 = 12×$50 + 4×$44; Standard $6,225–$9,350 = backbone $5,625–$8,750 + 12×$50; Premium from $13,000 (to $21,750+) = OS2 backbone $10,000–$18,750+ + second room from $3,000. Caveat: the Manhattan page's OS2 line already says "OTDR on every strand"; Premium does not add OTDR again.

#### Images (11) — Step C library; Drive folder empty, CompanyCam not connected
Copied (new names) from existing `/images/fiber-optic-installation/` files; none shares content with the DUMBO or LIC copies. Source files look AI-rendered, not real photos (garbled box text, invented shirt phone numbers such as 844-386-7238, uniform lighting). Most show technicians' faces in profile/three-quarter view (staff, not customers); none shows house numbers, licence plates or readable documents.
1. fiber-optic-installation-financial-district-corridor-cable-bundle-idf.webp ← staten-island-corridor-riser-bundle-dress (hero)
2. …-van-shelving-reels-ladders.webp ← suffolk-county-van-cable-reels-ladders (§5)
3. …-switch-seated-rack.webp ← staten-island-sfp-switch-rack-mount (§6)
4. …-metal-stud-cable-routing.webp ← staten-island-metal-stud-cable-routing (§7)
5. …-conduit-pull-box-block-wall.webp ← staten-island-block-wall-conduit-box-pull (Floodline)
6. …-ceiling-tile-ladder-feed.webp ← staten-island-ceiling-tile-cable-feed (§9)
7. …-link-tester-pass-screen.webp ← staten-island-link-tester-rack-and-jack (§10)
8. …-tone-probe-wall-opening.webp ← hudson-valley-tone-probe-wall-jack-trace (§12)
9. …-retail-ceiling-cable-pull.webp ← staten-island-retail-fitout-ceiling-pull (§13)
10. …-recessed-wall-box-patching.webp ← suffolk-county-recessed-wall-box-patching (Conversion waves)
11. …-rack-laptop-switch-setup.webp ← ulster-county-rack-switch-laptop-setup (§16)
DAILY-LOG note: `images: 11 reused from images/fiber-optic-installation/ (no real Fiber Optic Installation photos yet; library images appear AI-rendered)`.

#### Keyword plan (FiDi page)
Service: fiber optic installation Financial District, fiber backbone Lower Manhattan, riser fiber Wall Street, fusion splicing, OTDR testing. Problem: flood-proofed cellar, entry room relocation, conversion demolition, restricted delivery/security zone, clay-tile floors, raised floor clean-out, cell dead zones. Technology: OS2, OM4, OFNP/OFNR, armoured, microduct, sealed enclosures, MPO, DAS. Industry: financial firms/trading desks, DFS-regulated firms, law, hotels, conversions/residential, Seaport restaurants, retail. Geographic: Financial District, Wall Street, Broad Street, Water Street, Maiden Lane, Broadway, Stone Street, Seaport, World Trade Center, Battery Park City, Lower Manhattan.

#### Question register additions (fiber-optic-installation-financial-district-manhattan-ny)
§9 Questions Answered:
- Our building sits inside the barricaded blocks around the Stock Exchange — how do installers get vans, reels and ladders to the door?
- Our cellar was rebuilt with a flood wall and drop-in barrier panels — where can new fiber run so it never gets in their way?
- The landlord is moving the carriers' entry room up out of the cellar — what happens to our circuits and our fiber during the move?
- Can new risers be cored through the clay-tile floor arches of an early Broadway or Broad Street skyscraper?
- Our post-war tower has an underfloor duct system — can fiber use it instead of the ceiling?
- Our old trading floor has a raised access floor — can fiber run underneath it, and what cable is allowed there?
- The floors above us are being converted to apartments while we stay — how do we keep our riser fiber alive through the demolition?
- Our building has to add a Fire Department radio system — does it compete with our fiber for riser space?
- Our trading desk counts microseconds — does the length of the fiber path inside the building matter?
- We're covered by New York's DFS cybersecurity rules — does a documented fiber plant help with the asset inventory they now require?
(In-building cellular is covered under a statement heading, "A note on in-building cellular systems", not a question, because the LIC page asks it.)
§17 FAQ:
- Do you work in Battery Park City, the Seaport and the World Trade Center blocks as well as the streets around Wall Street?
- Will you work on the apartment floors of a converted tower, or only the office floors?
- We sublease part of a floor downtown — can we have our own fiber back to the building's entry room?
- Is fiber work in the Financial District priced differently from Midtown?
- How long do you need the freight elevator for a typical downtown riser pull?
- Can fiber reach the lobby security desk and turnstiles in a downtown tower?
- Were the towers converted under the 1990s downtown incentive left with usable telecom risers?
- If our firm moves to a different floor in the same tower, can our backbone move with us?
- Some downtown towers require union labour — can you work in those buildings?
Other question headings: Fiber Link Down Between Wall Street and the Battery? · Conversion Starting Above You? · Downtown Link Dark After a Storm Warning?

## DUMBO, Brooklyn — neighbourhood research (2026-10-17 batch, fiber-optic-installation-dumbo-brooklyn-ny; includes this page's question-register additions)

### DUMBO, Brooklyn — local research (2026-10-17 batch, fiber-optic-installation-dumbo-brooklyn-ny)

Neighbourhood spoke under `fiber-optic-installation-brooklyn`. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in `research/fiber-optic-installation.md` are reused where noted (no silo research redone). To be merged into `research/fiber-optic-installation.md` by the main run.

**Thesis:** in DUMBO the cable is cheap and the building is the constraint — century-old Gair reinforced-concrete slabs, brick-and-timber warehouses, a landmark district with newly rebuilt Belgian block streets, Manhattan Bridge trains overhead and a Sandy-flooded river edge decide the route, the enclosure placement and the price.

#### Reddit (local)
- Query: `Manhattan Bridge subway trains noise vibration DUMBO residents buildings` · Firecrawl web search (excerpt only; Firecrawl does not scrape reddit.com) → https://www.reddit.com/r/DUMBO/comments/1plt5ma/front_streetbridge_street_nonstop_noise_closed/ — excerpt: "Our triple paned windows make the trains crossing sound like a mild, relaxing sigh compared to this ongoing street construction." → §"The Manhattan Bridge Overhead" para 1 (resident voice, quoted as a forum post).
- Query: `reddit Dumbo internet fiber building office loft provider` · Firecrawl web search → https://www.reddit.com/r/sysadmin/comments/1oni8uz/pilot_fiber_in_nyc/ — excerpt: "The building fiber remains a single point of failure with Pilot/Fios…" → §"Two Carriers, One Cellar Wall" para 2 (presented as a commenter's general NYC opinion, not DUMBO fact). Other results (r/verizon, r/telecom, r/nyc, r/networking) generic NYC — not used.
- DUMBO-specific Reddit threads about fiber/internet: EMPTY (none returned).

#### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitute for §10.5 reality check — claims published by competitor/provider pages, quoted as published:
- Query: `reddit Dumbo internet fiber building office loft provider` · Firecrawl → https://www.buildinghealthx.com/services/internet-providers/dumbo (search excerpt): "Many converted warehouse lofts have Fios where the landlord granted Verizon access for fiber installation, though coverage is patchier here than in new…" → §10.5 H3 2.
- Silo sources reused (not re-researched): streamlinetelecom.com "$1-6 per linear foot" → §10.5 H3 1; thenetworkinstallers.com fusion splice $30–$75 (citing Ring and Ping) → H3 3; lowvoltagenewyork.com "OTDR $75–$150/hour; nobody publishes a flat per-strand rate" → H3 4; "Plenum rating adds 15–25%" → H3 5; "singlemode glass is now cheaper than OM4" / transceivers "roughly 1.5–5×" → H3 6; "a 2,000-foot OM4 riser run between IDFs, terminated and tested — lands around $3,000–$5,000" → H3 7.
- Angi/HomeAdvisor/Fixr DUMBO pages: EMPTY (not searched again; silo search returned none).
- Query: `business internet providers Dumbo Brooklyn` — https://ispreports.org/business-internet-providers-dumbo-brooklyn-ny/ appeared in results (excerpt only: "Compare 10 business internet providers in Dumbo") — not used.

#### Landmarks, buildings, historic district
- Query: `DUMBO Historic District designation 2007 Landmarks Preservation Commission buildings warehouses` · Firecrawl search → https://s-media.nyc.gov/agencies/lpc/lp/2279.pdf (Firecrawl scrape, query mode): designated December 18, 2007; "approximately 91 buildings"; bounded by John, Adams, Plymouth, Main, Water Streets, Howard Alley, Front, York, Washington, Pearl, Jay and Bridge Streets; "slow-burning mill construction" / "massive wooden columns, beams"; reinforced concrete; brick; "granite Belgian block paving"; "network of train tracks, running along the streets and in some cases extending into individual buildings, laid out by the Jay Street Connecting Railroad"; "The Manhattan Bridge, which soars over the area"; Robert Gair, Arbuckle Brothers named. → §5 paras 1 & 3, §5.5 fact 1, §8.5 Landmarks callout, "Fiber in a Landmark District" section, glossary.
- Same search → https://www.citylandnyc.org/landmarks-designates-new-dumbo-historic-district/ (excerpt: Dec 18 2007 vote) and https://www.brownstoner.com/history/breaking-dumbo/ (excerpt: voted 8-0) — corroboration only.
- Query: same · Firecrawl → https://dumbo.nyc/buildings/ (DUMBO Improvement District, search excerpt): 45 Water St built 1870, 5-storey brick and timber tobacco inspection warehouse, truncated by New Dock Street, "now a city landmark, houses … St. Ann's Warehouse"; Empire Stores 53–83 Water St, western warehouses 1870, eastern 1885, seven brick warehouses; 16 Main St 1906 stable for the Gair Company; 1 Main St reinforced concrete, "tallest reinforced concrete building in the world when it was built in 1914", leased in 1920s to Charles William Stores; 45 Main St 1919, Gair's third and final, designed by William Higginson, erected by Turner; 55 Washington St 1905, "first reinforced concrete building for Gair and the largest of its kind at the time"; 10 Jay St 1897–98 sugar refinery; 68 Jay St 1915, "Brick; steel frame with reinforced concrete floors", tea warehouse; 1 Front St "brought back to life in the late 2000s"; 11 & 15 Old Fulton St. → §5.5, §7 cards, §8 cards, §13 cards, Building Reference table, Q&A Q1.
- Query: `Gair buildings DUMBO Robert Gair reinforced concrete factory history "Gair"` · Firecrawl → https://www.brownstoner.com/history/robert-gair-dumbo-brooklyn-inventor-gairville-boxes-packaging/ (scrape, Oct 23 2024): "Gairville"; "eight Gair buildings"; Turner Construction; "1904 and 1916"; 1 Main St "tallest reinforced concrete building in the world"; "The Gair name incised on the buildings". https://old.skyscraper.org/EXHIBITIONS/VERTICAL_URBAN_FACTORY/gair.php (excerpt: brick slow-burning 1887–91, "from 1904 on built, with Turner Construction, much larger…"). → §5 para 1, §7 Gair card, landmark section, glossary.
- Query: `Empire Stores DUMBO redevelopment 2017 office square feet Water Street warehouse restoration` · Firecrawl → https://developingresilience.uli.org/case/empire-stores/ (scrape): "400,000 –square-foot raw space"; "AquaFence, a retractable flood wall that staff can store when the building doesn't need it"; "tuck in a generator on the fifth floor"; Brooklyn Bridge Park redevelops "1.3 miles of former industrial waterfront". https://brooklynbridgepark.org/press-releases/empire-stores-… (excerpt: "500,000-square-foot multipurpose facility") — not used (ULI figure used instead). → §13 Empire Stores card, Q&A flood/mechanicals Q, flood section bullet, Building Reference table.
- Query: `Dumbo Heights Watchtower buildings 55 Prospect 77 Sands 81 Prospect 117 Adams office conversion Etsy WeWork` · Firecrawl → https://gothamist.com/news/jehovahs-witness-watchtower-buildings-will-become-dumbo-heights-tech-temple (excerpt: 175 Pearl, 77 Sands, 117 Adams, 81 and 55 Prospect); https://www.bizjournals.com/newyork/news/2016/08/05/… (excerpt: "Etsy, which moved its headquarters to 117 Adams St. earlier this summer"); https://www.jrmcm.com/project/dumbo-heights/ (excerpt: "The 1,200,000 SF, $93 Million LEED certified project"); https://www.wework.com/buildings/dumbo-heights-77-sands--new-york-city--NY (excerpt: "a 1962 industrial landmark"; "three WeWork floors"). → §7 Dumbo Heights card, §8 card, §13 card, Building Reference table, Coworking section.

#### Local data (DUMBO Improvement District)
- Query: `DUMBO Improvement District annual report tech companies employees office square feet` · Firecrawl → https://dumbo.nyc/data/ (scrape): commercial sq ft (2022) 6 million; employees (2022) 11,266; office buildings 15; creative and tech companies 1,000+; retail storefronts 125+; residents (2023) 10,200; residential units (2023) 3,338; F train York St 2024 ridership 3.47 million; Brooklyn Bridge Park 85 acres, avg 613,698 visitors/week, Pier 1 Old Fulton most used entrance; 20+ galleries; 152 artist studios; 107 video art exhibits projected onto the Manhattan Bridge; 13th Annual Photoville (2024); 2 pedestrian plazas; 2,700 hours of open streets; 152,313.5 sq ft Belgian block. (Page notes 2021 data unless indicated.) → §5 para 1, §5.5 fact 2, §8 Front/York card, Tech Triangle section, Lofts section, Arts section, "Working Around" section, Q&A landlord Q.
- Same search → https://technical.ly/civic-news/dumbo-has-500-tech-firms-10k-employees-in-10-block-radius/ (older excerpt: 500 tech firms) — not used (superseded by BID figure).

#### Local news / hyperlocal
- Query: `Manhattan Bridge subway trains noise vibration DUMBO residents buildings` · Firecrawl → https://www.mta.info/document/138061 (scrape, "New York City Transit Noise Reduction Report"; DUMBO memo transmitted January 18, 2024): measured homes incl. 135 Plymouth St (357 trains, max Lmax 94.76 dB(A)), 56 Adams St (520, 94.66), 68 Jay St (503, 90.37), 98 Front St (323, 83.93), 133 Water St (472, 80.36); Front St & Pine St at anchorage 94.4 dB(A) vs 68.2 dB(A) background (30-min sample); rail-joint modification judged "infeasible". → §5.5 fact 4, Bridge section table and paras, Q&A rack Q.
- Same search → https://www.brooklynpaper.com/deaf-in-dumbo/ (scrape, Sept 25 2008): DUMBO Neighborhood Association president moved away over noise; B, D, N, Q trains and truck traffic on the Manhattan Bridge; 33-story J and 23-story Beacon Tower named. → Bridge section para 1, §7 towers card.
- Query: `DUMBO Hurricane Sandy flooding Water Street basements Brooklyn 2012` · Firecrawl → https://www.nhregister.com/news/article/Hurricane-Sandy-floods-New-York-City-11496317.php (excerpt, AP caption: "Streets are flooded under the Manhattan Bridge in the Dumbo section of Brooklyn, N.Y., Monday, Oct. 29"); https://www.cbsnews.com/pictures/superstorm-floods-new-york-city/ (excerpt: flooded street in Dumbo). → Flood section para 1.
- Query: `Dumbo Sandy flood businesses Two Trees buildings basement damage Jane's Carousel water` · Firecrawl → https://www.cbsnews.com/newyork/news/janes-carousel-spared-but-electronics-damaged-in-brooklyn-bridge-park/ (scrape): "The basement that houses all the electronics was totally flooded – 5 feet of water" (article undated on page; 2012 storm coverage). → §5.5 fact 6, §13 carousel card, Flood section.
- Silo source reused: NYC SIRR report — Brooklyn flooded area more than twice the floodplain → Flood section para 1.
- Query: `NYC DDC DUMBO street reconstruction Belgian block water main sewer Front Street Bridge Street project` · Firecrawl → https://www.nyc.gov/html/dot/html/pr2025/city-completes-historic-street-restoration-dumbo.shtml (search excerpt, full press text): $108 million; 26 blocks; began 2019; Pearl Street Plaza; restored archway; 2,735 ft new storm sewers; 1,300+ ft sanitary sewers replaced; 6,600 ft water mains upgraded; 3,140 ft new; 114 ADA ramps; "additional funding coming from private utilities"; LPC approved restoration "in the DUMBO and Vinegar Hill Historic Districts". https://dumbo.nyc/construction/ (excerpt: "broke ground in April 2019, and was completed in December 2025"). → §5.5 fact 5, Landmark section para 3, Q&A streets Q, §13 archway card.
- Local news on DUMBO fiber-installation contractors 2025–2026: EMPTY.
- FEMA flood zone designation for DUMBO blocks: EMPTY (search returned only generic FEMA/First Street pages; no zone claim made on the page).

#### Local licensing / permits / building rules
- LPC: designation report above → exterior work in the district is LPC territory; routes kept indoors. (Silo LPC sources reused.)
- DOB sub-50 V permit statement, firestop, cable ratings: silo sources reused (unifinerds, cablinginstall NEC 770).
- NYC Mesh (silo source, https://www.nycmesh.net/building): works with management companies, helps with lease/insurance paperwork; fiber connections require a fiber lease → Q&A community-network Q.

#### Pricing used (existing approved prices only — no new prices)
DUMBO = Brooklyn base 1.00× (blueprint §9). Lines copied from `fiber-optic-installation-brooklyn.html`: $35/termination; $40/strand OTDR; $350 MM drop; $400 SM drop; 12-strand OM4 backbone $4,500–$7,000; 24-strand OS2 $8,000–$15,000+; second telecom room with fiber link from $2,400; $195/hr, 3-hr minimum ($585). Worked packages are sums of those lines only: Starter $400+$400+4×$40 = $960; Standard ($4,500–$7,000)+12×$40 = $4,980–$7,480; Premium ($8,000–$15,000+)+(from $2,400) = $10,400–$17,400+.

#### Images (11) — Step C library reuse
Drive folder `AESS Website Photos/Fiber Optic Installation` empty (main run); CompanyCam not connected. 11 copied from `/images/fiber-optic-installation/` (all library photos are already used on sibling pages; chose single-use, face-free crops; none shared by hash with the FiDi/LIC batch pages). Each viewed before use; alt/title/caption describe only what is visible.
| New file | Copied from |
|---|---|
| fiber-optic-installation-dumbo-hammer-drill-masonry-penetration.webp | …-putnam-county-hammer-drill-block-entry.webp |
| fiber-optic-installation-dumbo-emt-conduit-sweep-feed.webp (hero) | …-putnam-county-emt-sweep-cable-pull.webp |
| fiber-optic-installation-dumbo-switch-seated-in-rack.webp | …-putnam-county-sfp-switch-seated-rack.webp |
| fiber-optic-installation-dumbo-rack-yellow-jumpers-ups.webp | …-putnam-county-rack-yellow-patch-ups.webp |
| fiber-optic-installation-dumbo-patch-cord-labelling.webp | …-putnam-county-patch-cord-label-applied.webp |
| fiber-optic-installation-dumbo-tone-probe-panel-trace.webp | …-putnam-county-tone-probe-panel-trace.webp |
| fiber-optic-installation-dumbo-jhook-bundles-open-deck.webp | …-putnam-county-jhook-bundles-above-grid.webp |
| fiber-optic-installation-dumbo-corridor-bundle-open-ceiling.webp | …-putnam-county-bundle-lift-open-ceiling.webp |
| fiber-optic-installation-dumbo-panel-punchdown-hands.webp | …-putnam-county-punchdown-panel-hands.webp |
| fiber-optic-installation-dumbo-idf-rack-patching-rear-view.webp | …-manhattan-idf-rack-patching.webp |
| fiber-optic-installation-dumbo-link-tester-pass-wall-jack.webp | …-putnam-county-tester-pass-wall-outlet.webp |
**Flag:** the library photos appear AI-rendered (garbled small text on equipment and shirts, inconsistent "Abstract Enterprise LLC" logos, blurred patches, a 844-386-7238 number on some uncropped originals). None of the 11 shows a fiber splicer; most show copper/rack work. DAILY-LOG note: `images: 11 reused from images/fiber-optic-installation/ (no real Fiber Optic photos yet; library looks rendered)`.

#### Keyword plan (DUMBO page)
Service: fiber optic installation DUMBO, fiber backbone DUMBO Brooklyn, loft fiber, slab coring, fusion splicing, OTDR testing. Problem: century-old concrete slabs, timber beams, landmark facade, bridge vibration, waterfront cellar entry, subtenant/coworking access, carrier redundancy through one entry. Technology: OS2, OM4, OFNR small-diameter riser, OFNP, armored indoor/outdoor, duct seal, latched enclosures, OTDR baseline. Industry: tech/creative offices, studios, galleries/venues, residential loft condos, coworking operators, landlords. Geographic: DUMBO, Water St, Front St, York St, Main St, Washington St, Jay St, Adams St, Plymouth St, Pearl St, Sands St, Prospect St, Old Fulton St, Dumbo Heights, Empire Stores, Brooklyn Bridge Park, Manhattan Bridge, Vinegar Hill, Fulton Ferry.

#### Question register additions (fiber-optic-installation-dumbo-brooklyn-ny)
§9 Questions Answered:
- Our Gair-era factory floor still has openings left by old freight lifts, chutes and pipes — can new fiber use those instead of fresh cores through the slab?
- Can fiber follow the heavy timber beams of a Water Street warehouse without being fastened into the wood?
- How is cable protected where it has to cross rough brick and stone in a Civil War–era warehouse?
- Where should the rack and splice enclosures go in a loft that shakes every time a train crosses the Manhattan Bridge?
- After Sandy our building moved its generator and mechanical gear up high — should the network equipment go up to the roof with it?
- What should we do with our fiber equipment when a coastal storm warning goes up for the DUMBO waterfront?
- The cobblestone streets around our building were just rebuilt — can a new carrier still bring fiber in?
- We own a DUMBO loft building and are leasing floors to tech tenants — what should we be able to show prospective tenants about the building's fiber?
- Our gallery wants a video work on a far wall with no visible cable — can fiber carry the signal from a back room?
- Can our DUMBO loft building connect to a community network such as NYC Mesh, and what wiring would that take?
§17 FAQ:
- Do you need to go through other tenants' spaces to run our fiber?
- Do you also cover Vinegar Hill, Fulton Ferry and the Dumbo Heights buildings up on Sands Street?
- Will trains crossing the Manhattan Bridge affect when you can splice or test?
- Is there any extra charge for working inside the DUMBO Historic District?
- Will new cable holes weaken the soundproofing our bridge-side office paid for?
- Can you work inside a gallery or showroom without putting the pieces on the walls at risk?
- Can one backbone in our loft building carry the lobby cameras, door readers and intercom as well as residents' internet?
- Can fiber let a recording or podcast studio move noisy computers and storage out of the live room?
- If our internet plan is the bottleneck, will new fiber inside the office make any difference?
- How much noise and dust does coring a concrete floor make in an occupied loft building?
Non-question headings (for reference): "DUMBO Fiber Link Dropped Today" (repair capture), "Studio Offline Between Water Street and Sands Street" (final repair).
Checked against the silo register and the parallel FiDi / LIC pages: subletting, freight-elevator, pricing-rate, flood-wall entry and "does the building's fiber reach my space" questions were dropped from this page because FiDi/LIC ask them.

## Long Island City, Queens — neighbourhood research (2026-10-17 batch, fiber-optic-installation-long-island-city-queens-ny; includes this page's question-register additions)

### Long Island City, Queens — local research (2026-10-17 batch, fiber-optic-installation-long-island-city-queens-ny)

Neighbourhood spoke of fiber-optic-installation-queens (Bronx GBP, (347) 434-6392). Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md and the Queens section are reused where noted; only LIC-specific research is added here.

**Page thesis:** Long Island City is a neighbourhood people live and work in while it is still being built (2001 rezoning towers, OneLIC 2025 rezoning starting a second cycle). Fiber here has to go in while a building is unfinished (TCO floors, loft re-lets, retail condos) and still be provable after the neighbours finish excavating — phased risers, scanned cores, sealed entrances, dated baselines and a building file.

**Name handling:** the page says early in §5 (and in FAQ 1) that Long Island City is a neighbourhood of western Queens inside NYC, not Nassau or Suffolk, priced as Queens. The silo cross-link block labels the LI group "Long Island (Nassau and Suffolk)". tools/check_page.py: no geo check trips on "Long Island City" (title/alt aliases for queens = "Queens", satisfied; no wrong-area phrase check exists). Only side effect: `mask()` strips "Long Island" from "Long Island City" (leaves "City") in the duplicate-question comparison — harmless.

#### Reddit / forums (local)
- `reddit LongIslandCity internet building Verizon Fios Spectrum only option apartment` · Firecrawl search (excerpts only; reddit.com not opened)
  - https://www.reddit.com/r/longislandcity/comments/1pt8ihp/spectrum_astound_or_fios/ — "Not sure where you live but if it is an option for your building, you may want to consider Honest Internet. I pay $50 flat/mo for 1 Gbps" → §5 para 4; §10.5 H3 7.
  - https://www.reddit.com/r/AskNYC/comments/go1pjg/nyc_apartment_building_only_allowing_one_cable/ — "You can own a building in a FiOS neighborhood and still not be able to convince Verizon to install FiOS in it." → §5 para 4.
  - https://www.reddit.com/r/AskNYC/comments/1uhxwu9/why_is_it_so_hard_to_get_fios_on_the_uws_im/ — "Verizon tends to want 70% of households in a building to request FIOS before they will wire a building." (UWS thread; quoted as a commenter's claim, page says no published Verizon policy found) → §10.5 H3 4.
  - https://www.reddit.com/r/AskNYC/comments/155v4gi/moving_into_a_new_apartment_with_spectrum_how_bad/ — "I ended up opting for Verizons 5G home internet instead. It has been 95 percent as good as the wired Verizon connect" → §10.5 H3 5.
- `reddit Long Island City apartment internet fiber building Verizon Fios not available tower` · WebSearch → community.verizon.com/discussion/1747457 ("impossible to get fios at new construction condominium") — WebFetch redirected to Verizon support (community sunset). EMPTY (not accessible in build env). Not used.
- Silo source reused: Verizon forum Astoria tenant, moderator "owner to sign an easement form" → §10.5 H3 4.

#### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
Substitutes for §10.5 (claims quoted as published):
- `Long Island City NY internet providers fiber availability percent coverage 11101` · Firecrawl search (excerpts)
  - https://broadbandnow.com/New-York/Long-Island-City — "Fiber internet is 69.7% available in Long Island City. Cable is available to 85.6%" → §5.5, §10.5 H3 1.
  - https://www.broadbandsearch.net/service/new-york/long-island-city — "Fiber 61.8%" → §5.5, §10.5 H3 1.
  - https://www.inmyarea.com/internet/new-york/long-island-city — "Verizon Fios … cover a whopping 78.5% of the area" → §10.5 H3 1.
  - https://www.spectrum.com/locations/internet-wifi-service/long-island-city-ny-i3215 — "Get Spectrum Fiber-Powered Internet in Long Island City, NY with reliable speeds up to 1 Gig" → §10.5 H3 2.
- `"fiber optic" cables "not affected by water" flooding advantage` · Firecrawl search (excerpt) → https://blog.frontier.com/2020/07/5-reasons-you-want-fiber-internet-service-right-now/ — "It is not affected by water, including flooding" → §10.5 H3 3.
- `low-E glass blocks cellular signal buildings distributed antenna system attenuation dB` · WebSearch →
  - https://www.waveform.com/pages/das-in-leed-buildings-with-low-e-glass (WebFetch): low-E glass causes "high signal attenuation"; DAS donor antenna supplies indoor antennas "through media such as optical fiber"; no dB figure → §9 Q3, §10 table.
  - https://powerfulsignal.com/support/kb/how-much-cell-signal-is-lost-passing-through-building-materials/ (WebFetch): low-e glass "−30 to −34 dB"; concrete 6″ "−10 to −19 dB" → §9 Q3, §10.5 H3 6.
- Angi / HomeAdvisor / Fixr: no fiber cost page (silo finding) — stated on page, not quoted.

#### Landmarks, buildings, corridors
- `OneLIC neighborhood plan City Council approved Long Island City rezoning homes jobs` · WebSearch → https://www.6sqft.com/14700-homes-long-island-city-rezoning-approved/ (WebFetch, Nov 13 2025): unanimous Council approval; 14,700 homes, 4,350 permanently affordable; 54 blocks; East River to Crescent St, Queens Plaza North to 47th Ave; 3.5M+ sq ft commercial/industrial; continuous waterfront Gantry Plaza SP → Queensbridge Park; two elementary schools (Hunters Point, Court Square) 1,094 seats; IBZ studies → §5 para 2, §5.5, "Rezoned Twice" section, block-by-block (Ravenswood).
- `Long Island City Partnership neighborhood snapshot residential units businesses jobs 2025` · WebSearch →
  - https://www.osc.ny.gov/press/releases/2025/09/dinapoli-lic-sunnyside-and-woodside-are-drivers-economic-growth-queens (WebFetch, Sept 25 2025): LIC–Hunters Point housing units quadrupled 2010–2024 to 26,177; region private-sector jobs +9.3% to 74,972 (2023) led by business services, security services, social assistance, health care, retail → §5 para 2, §5.5.
  - https://www.nyrej.com/lic-partnership-releases-lic-neighborhood-snapshot (WebFetch; snapshot released 2018): LIC "NYC's fourth-largest central business district"; co-working "five locations" → §8 intro, §9 Q6.
- Silo/Queens sources reused: DCP 2001 rezoning summary (37 blocks, 23rd St/41st Ave/Sunnyside Yards, large floor plates as of right) → §5 para 2, "Rezoned Twice" para 1; One Court Square (Wikipedia: 673 ft, 50 storeys, 1989, Citigroup, 25-01 Jackson Ave, tallest until Skyline Tower 2019) → §7 card, §13 card; Silvercup Studios (Wikipedia: 42-25 21st St, bakery 1929–30 Gordon Baking Co., studio 1983, Sopranos/Mad Men) → §8 card, §13 card; inflect.com 23-10 43rd Ave data-centre listing, Zayo and Lumen in building → §8 card, §9 Q9; Hunters Point South Center Blvd towers → §7/§8.
- `Falchi Building 31-00 47th Avenue Long Island City history office conversion` · WebSearch → https://commercialobserver.com/2019/01/under-construction-the-falchi-building-in-long-island-city (WebFetch): built 1922 as Gimbels warehouse; 736,000 sq ft, full block, six storeys; Jamestown bought 2012 ($81.2M) and converted to offices; Savanna bought Dec 2016; tenants TLC, Uber, Lyft etc.; "floor plates of a large warehouse" → §7 card, §8 card, §13 card.
- `Standard Motor Products building 37-18 Northern Boulevard Long Island City office conversion square feet` · WebSearch → https://6tocelebrate.org/site/standard-motor-products-building/ (WebFetch): built 1921 as S. Karpen & Brothers furniture factory; SMP engine parts 1936–2008; 150,000+ sq ft, six storeys; converted 2010–2014 for small commercial tenants → §7 card, §8 card, block-by-block.
- `JetBlue headquarters Brewster Building 27-01 Queens Plaza North Long Island City moved 2012` · WebSearch → https://therealdeal.com/new-york/2012/04/04/jetblue-headquarters-opens-today-in-lic/ (WebFetch; URL dated 2012-04-04): Brewster Building, 27-01 Queens Plaza North, 200,000 sq ft, ~970 staff from Forest Hills and Darien → §8 card, block-by-block. (milrose.com page fetched: no building content — not used.)
- `LaGuardia Community College Thomson Avenue campus former Ford factory buildings students` · WebSearch → https://en.wikipedia.org/wiki/LaGuardia_Community_College (WebFetch): opened Sept 22 1971; campus Thomson Ave–47th Ave, 28th St–Van Dam St; White Motor truck factory (1920), Equitable Paper Bag building, Sunshine Biscuits bakery (1912) etc.; fall 2025 enrollment 25,877 → §7 card, §8 card, §13 card, campus section.
- `Court Square–23rd Street station complex E M G 7 lines transfer opened` · WebSearch → https://secondavenuesagas.com/2011/06/03/months-late-court-square-entrance-finally-opens (WebFetch): 7–G covered transfer opened June 3 2011, complex renamed Court Square → §8 card.
- `Sunnyside Yard acres largest rail yard Amtrak Long Island City` · WebSearch → https://en.wikipedia.org/wiki/Sunnyside_Yard (WebFetch): completed 1910; Amtrak owns/operates, NJ Transit and LIRR use; NYCEDC working footprint 180 acres; Skillman Ave (S) to Northern Blvd (N); 2020 master plan deck 12,000 affordable units + 60 acres parks; Feb 2026 revival seeking ~$21B federal funds → §5.5, §13 card, "Sunnyside Yard" section.
- `Hunters Point Historic District 45th Avenue rowhouses designated 1968 Landmarks` · WebSearch → https://6tocelebrate.org/site/hunters-point-historic-district/ (WebFetch): designated 1968; S/NR 1973; 45th Ave between 21st and 23rd Sts; late-19th-c. stone houses, many subdivided → §7 card, §8.5, §13 card.
- `Long Island City data center colocation building carrier fiber Queens` · WebSearch → Con Edison Communications lease (undated) — not used; other results are Long Island (Nassau/Suffolk) data centres — not used.
- Building-type share / tower counts for LIC: EMPTY (no source retrieved; page gives no counts).

#### Local news / hyperlocal
- `Hurricane Sandy flooding Long Island City Hunters Point Newtown Creek basements 2012` · WebSearch → https://www.dnainfo.com/new-york/20121031/long-island-city/hunters-point-residents-clean-up-after-sandy (WebFetch, Oct 31 2012): parts of LIC flooded up to 11th St; PowerHouse (2-17 51st Ave, 11 storeys) lobby ~5 ft of water, garage lower level submerged, no power; The Foundry (2-40 51st Ave) basement still flooded; CityLights co-op (4-74 48th Ave) water entered, 4 of 5 elevators running Wed → §5.5, §9 Q7, §10.5 H3 3, "What Sandy Taught" section (building names/addresses not used beyond street names).
- Queens Chronicle / QNS / LIC Post items on fiber installation in LIC: EMPTY (none retrieved).

#### Local licensing / permits / building rules
- `NYC Local Law 196 Site Safety Training SST card required workers construction sites 40 hours` · WebSearch → https://www.nyc.gov/site/buildings/safety/sst-worker-information.page (WebFetch): SST required on sites needing a Site Safety Plan and designated Construction Superintendent; worker card min. 40 hours → §8.5, §9 Q1, FAQ 3.
- `post-tensioned concrete slab coring tendons GPR scanning before drilling New York residential towers` · WebSearch → https://www.cmc.com/en-us/what-we-do/america/cable-articles/the-importance-of-understanding-the-depth-of-post (WebFetch; vendor marketing): must know location and depth of PT cables; depth not standardised; accidental cuts risk injury/"catastrophic slab and structure failures"; GPR for tendon depth → §8.5, §9 Q2. (No source for the share of LIC towers that are post-tensioned — page does not claim one.)
- Silo sources reused: sub-50 V no DOB permit + firestopping; OFNR/OFNP (cablinginstall) → §8.5.

#### Pricing used (existing AESS Queens prices — no new prices)
Copied from fiber-optic-installation-queens.html: $37/termination; $42/strand OTDR; $391 MM drop; $447 SM drop; $4,725–$7,350 12-strand OM4 backbone; $8,400–$15,750+ 24-strand OS2; second room from $2,520; $195/hr, 3-hr min ($585).
Worked totals on page: Starter $1,452 = 24×$42 ($1,008) + 12×$37 ($444). Standard $5,619–$8,244 = $4,725–$7,350 + 2×$447 ($894). Premium $10,920–$18,270+ = $8,400–$15,750+ + $2,520.
Caveat carried from Queens section: the $391/$447 drop prices come from the live Queens configurator (≈1.12×), not §9's 1.05×.

#### Images (11) — Step C library reuse; Drive folder empty, CompanyCam not connected
All copied from /images/fiber-optic-installation/ (themselves copies of images/low-voltage originals). Every source scene was checked by eye. The photos look AI-generated / rendered (uniform branding, garbled small text, shirts printed with "844-386-7238" or "800-486-0943"), and most show a technician's face in profile — the whole library is like this; back-view/hands-only scenes were preferred. Byte-identical files used by the parallel DUMBO and Financial District pages were avoided (the first pick, an SFP-switch scene, matched the FiDi file and was replaced).
| File | Source | Shows |
|---|---|---|
| …-long-island-city-fusion-splicer-ready-screen.webp | …-bronx-splicer-screen-yellow-patch-cords.webp | fusion splicer READY, cleaver, IPA, yellow patch rack |
| …-long-island-city-glass-floor-crew-open-ceiling.webp | …-bronx-crew-open-ceiling-fitout.webp | 4-person crew from behind, open ceiling, glass-walled floor |
| …-long-island-city-splicer-bench-sc-patch-cabinet.webp | …-ulster-county-fusion-splicer-patch-cabinet.webp | splicer bench beside SC adapter cabinet |
| …-long-island-city-hammer-drill-block-wall-dust-hose.webp | …-brooklyn-hardhat-core-drill.webp | rotary hammer with dust hose on block wall |
| …-long-island-city-warehouse-basket-tray-lift.webp | …-hudson-valley-warehouse-high-bay-cable-tray.webp | scissor lift, basket tray, warehouse racking |
| …-long-island-city-meeting-room-display-recessed-box.webp | …-nassau-county-conference-room-cable-box.webp | 3 techs from behind, display + recessed cable box |
| …-long-island-city-patch-panel-punchdown-hands.webp | …-hudson-valley-patch-panel-termination-hands.webp | hands only, punch-down on numbered panel |
| …-long-island-city-exterior-enclosure-brick-conduit.webp | …-staten-island-exterior-wall-enclosure-conduit.webp | weatherproof enclosure + conduits on brick |
| …-long-island-city-conduit-pull-box-block-wall.webp | …-ulster-county-conduit-box-pull-block-wall.webp | cable from conduit pull box beside rack |
| …-long-island-city-closet-rack-before-after.webp | …-rockland-county-inherited-closet-before-after.webp | before/after closet, no people |
| …-long-island-city-ceiling-tile-cable-feed.webp | …-westchester-county-ceiling-tile-cable-feed.webp | tech from behind feeding cable through ceiling tile |
DAILY-LOG note: `images: 11 reused from images/fiber-optic-installation/ (library copies of images/low-voltage/; no real Fiber Optic Installation photos yet)`.

#### Keyword plan (LIC page)
Service: fiber optic installation Long Island City, tower riser fiber, phased fit-out fiber, retail condo fiber, DAS fiber strands, entrance conduit sealing, baseline OTDR testing. Problem: TCO / unfinished floors, post-tensioned slab coring, low-E glass cellular dead zones, adjacent excavation damage, waterfront flooding (Sandy), carrier "fiber-powered" vs glass to unit, provider blaming inside wiring. Technology: OS2, OM4, OFNR/OFNP, innerduct, armoured, duct seals, LC/SC/MPO, SFP, GPR scanning. Industry: condo/rental towers, office towers, warehouse-to-office conversions, coworking, retail condos, college campus, film studio area. Geographic: Long Island City, Court Square, Jackson Ave, Queens Plaza, Hunters Point, Center Blvd, Vernon Blvd, Dutch Kills, Northern Blvd, Thomson Ave, 47th Ave, 21st St, 43rd Ave, Ravenswood, Queensbridge, Blissville, Newtown Creek, Sunnyside Yard, Skillman Ave.

#### Question register additions
fiber-optic-installation-long-island-city-queens-ny
§9 Questions Answered (and other question headings):
- Fiber Down in a Long Island City Building? (repair capture heading)
- Our Court Square or Hunters Point tower only has a temporary certificate of occupancy and some floors are still under construction — can tenant or resident fiber go in now?
- Our tower has post-tensioned concrete floors — how does fiber get between floors without endangering a tendon?
- Cell signal dies inside our glass-walled tower — can the building's fiber carry an in-building cellular system?
- We bought the retail condominium at the base of a residential tower — does the residential board control how our fiber gets in?
- Can I have fiber run to a home office inside my own Long Island City condo, and what will the board ask for?
- We run a coworking floor in a converted Long Island City factory — should each member company get its own strands, or is that just a network-settings job?
- Water came in around the provider's conduit where it enters our waterfront basement — how is a fiber entrance sealed so it stays dry?
- A tower is going up on the lot next door — should we test our fiber before excavation starts, so any damage can be proven?
- There is a data centre a few blocks away — does that make internet service to our Long Island City building faster or cheaper?
- Want the Baseline Before the Excavator Arrives? (mid-page CTA heading)
§17 FAQ:
- Long Island City is in Queens, not in Nassau or Suffolk — which rates apply to a fiber job here?
- Which parts of Long Island City do you work in?
- Do your installers carry SST cards for a tower that is still an active construction site?
- How do you protect a new building's lobby, elevators and corridors while fiber is being pulled?
- Our rental listing says the building has fiber — how do we find out whether it actually reaches the apartment?
- The provider blames our inside wiring for outages — can your test results settle it?
- Can fiber work start before a new building's telecom rooms have permanent power?
- Could drilling for the fiber set off our building's fire alarm?

De-dup notes: checked against the full silo register and the parallel FiDi and DUMBO drafts. Removed during build: "What does the installation warranty cover?" (Queens/Staten Island exact intent) and "Do you work alongside the carrier's own technicians on installation day?" (= Brooklyn "Will you coordinate with the internet provider…"). Closest calls for a human read: post-tension coring (mine) vs FiDi "core risers through clay-tile floor arches" (different structural hazard, same coring family); DAS strands (mine) vs FiDi "Fire Department radio system competes for riser space" (cellular vs public-safety radio); fire-alarm/drilling-dust FAQ (mine) vs DUMBO "noise and dust coring in occupied loft"; LIC-vs-Nassau rates FAQ vs FiDi "priced differently from Midtown"; coworking strands vs FiDi "sublease part of a floor — own fiber to entry room". Masked-geo paragraph similarity (difflib, ≥12-word blocks, constants excluded) is < 0.65 against every fiber sibling incl. the two drafts; max 0.644 (ADT/Ring paragraph vs Queens).

## Port Morris, Bronx — local research (2026-10-17 batch, fiber-optic-installation-port-morris-bronx-ny)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources (top of research/fiber-optic-installation.md) and the Bronx section are reused where noted; only Port Morris research is added here. Up-link /fiber-optic-installation-bronx · phone (646) 490-0629 · Bronx GBP (460 E Fordham Rd, #bronx).

Page thesis: almost every Port Morris building is on its second or third life (piano factories → lofts, a 1916 bakery warehouse → creative offices, a warehouse → sound stages, rail-yard land → distribution, lots → towers and a last-mile depot). Fiber here follows the change of use: the carrier entrance moves, ownership splits among many occupants, and inherited cable has to be traced and either salvaged or removed. Distinct from the Bronx page (scale / multi-building complexes).

### Reddit (local)
- Query: `reddit Port Morris Bronx internet OR fiber OR Fios OR warehouse loft` · Firecrawl web search (excerpts only; reddit.com threads not opened).
  - https://www.reddit.com/r/bronx/comments/14poru5/are_port_morris_and_mott_haven_actually/ — title "Are Port Morris and Mott Haven actually gentrifying or is it just locals renovating the area?"; excerpt mentions "abandoned industrial or commercial buildings". → §5 THE NEIGHBORHOOD para 2; Sources table.
  - https://www.reddit.com/r/nyc/comments/1bco3hh/so_this_is_the_south_bronx_now_is_this_the_new/ — excerpt: "The appeal is that it offers luxury apartments at a lower price compared to say, Manhattan or LIC." → §5 para 2 (paraphrased, attributed to r/nyc).
  - https://www.reddit.com/r/Fios/comments/1oz9xcz/1_gb_fios_installion_in_a_5thfloor_apt_bronx_nyc/ and /r/Fios/comments/1rkb228/ — already logged in the Bronx section. Not used again.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG — EMPTY (not accessible in build env)
Substitute for §10.5 reality check — claims quoted from published sources:
- Silo/Bronx sources reused: Angi ($4,500 average, $1,500–$7,000), Ring and Ping (residential $1,500–$6,000; commercial "six figures"), Unio (single-mode $0.09–$1.49/ft; OM3/OM4 $1.50–$6.00/ft), AT&T "four to six hours", T-Mobile "up to 4 hours", CUF 99.8% wired + "individual buildings not yet wired", buildinghealthx 5G "no landlord or co-op board approval required" → §10.5 Claims 1, 2, 3, 5, 6, 7.
- Query: `Port Morris Bronx data center OR fiber network OR broadband` · Firecrawl web search → https://lightyear.ai/tips/dark-fiber-the-bronx (Firecrawl scrape, dated Feb 5, 2026): "an estimated 31 available" dark fiber providers in the Bronx; connectivity score "High"; availability "depends on fiber infrastructure near a specific address"; names Verizon, Windstream, Optimum, Spectrum, Lightpath, Zayo, Crown Castle, etc. → §10.5 Claim 4.
- Same query → https://council.nyc.gov/data/internet-access/ (excerpt): "Melrose-Mott Haven-Port Morris: 44% (The Bronx – CD01)" households without broadband (silo source re-confirmed). → §5 para 3, §5.5 facts, §10.5 Claim 5.
- Fixr: no Fixr fiber page found (silo record). Stated on page as "our research turned up no comparable Fixr page".

### Yelp 1–3★ — EMPTY
- Query: `yelp fiber optic cabling contractor Bronx reviews` · Firecrawl web search → only Yelp search-result pages and one 4.0★ single-review listing ("New York Network Cabling & Fiber Optic Wiring"); no 1–3★ fiber-contractor reviews for the Bronx/Port Morris. Not used.

### Building stock, zoning, history
- Query: `Port Morris Bronx industrial buildings warehouses conversion lofts Bruckner Boulevard rezoning` · Firecrawl web search → https://www.nyc.gov/assets/planning/download/pdf/plans/port-morris/port_morris.pdf (Firecrawl scrape, DCP, 7 pp.): 1997 CPC created the city's first mixed-use district (Port Morris Special Mixed Use District), five blocks along Bruckner Blvd, CD1; 2005 extension to eleven blocks bounded by Park Ave, Willow Ave, E 134th St and the Harlem River/Harlem River Yards; CPC approval Jan 31, 2005, Council adoption Mar 9, 2005; 129 lots: industrial 38 (29%), residential 44 (34%), more than one-third vacant or underutilized; industrial/commercial uses in "large brick and concrete industrial buildings ranging from one to six stories", mainly along Bruckner; two- and three-story rowhouses on E 133rd/134th near Willow Ave, three- to five-story multifamily on Bruckner; ~42 rowhouses rehabilitated; 50 lofts in the former Estey Piano Factory converted, 100 more expected by end-2004; history: Gouverneur Morris II seaport plan, piano and furniture manufacturing, Third Avenue Bridge 1898, Willis Avenue Bridge three years later, Harlem River train yards 1906, 1950s clearance for the Triborough Bridge and Bruckner/Major Deegan expressways; "Antique Row" on Bruckner; former New Haven passenger station building on Willis Ave south of 132nd St. → hero, §5 paras 1–2, §5.5, §7 cards, §8 Bruckner card, Change-of-use table, Streets table.
- Query: `reddit Port Morris Bronx internet OR fiber OR Fios OR warehouse loft` (same search) → https://en.wikipedia.org/wiki/Port_Morris,_Bronx (Firecrawl scrape): boundaries (Major Deegan/Bruckner, E 149th St, East River, Bronx Kill, Harlem River), ZIPs 10451/10454, 40th Precinct, CB1; Oak Point Yard; Hell Gate Bridge northern approach concrete arches (1917) north from E 132nd St between Willow & Walnut Aves; Randall's Island Connector opened Nov 2015; Dec 2017 Special Harlem River Waterfront District expansion; Union Crossing (825 E 141st St); The Arches at 224–228 E 135th St, "first market-rate high-rise rental development in Port Morris" (renting 2020); 101 Bruckner (55 units, 2021); Bankside (>1,350 units); Maven 2413 Third Ave (27 storeys, 200 apts); 188 E 135th St in brownfield cleanup; Port Morris IBZ in the eastern half; Alexander Ave–Bruckner Blvd main commercial corridor; Estey factory ("Clock Tower") at Lincoln & Bruckner; Bronx Grit Chamber (1937, McKim, Mead & White, E 132nd St & St. Ann's Ave, DEP, protected landmark); Per Scholas at 804 E 138th St; 6 train at Cypress Ave and E 143rd St–St. Mary's St; Bx17/Bx33/M125; 2010 census Mott Haven + Port Morris 52,413 residents, 72.3% Hispanic or Latino. NOT used: NY Post printing-plant dates (conflict between Wikipedia articles: 1998 vs 2001–2021), the Revolutionary War gold-ship story, Bluestone's $44M 2016 price (conflicts with The Real Deal's $39M). → §5, §7, §8, Change of use, Streets table, Landmarks, FAQ (Spanish labels: census figure), schema `mentions`.
- Query: `Harlem River Yard Port Morris FreshDirect rail yard warehouse distribution` · Firecrawl web search → https://en.wikipedia.org/wiki/Harlem_River_Yards (Firecrawl scrape): 96 acres total, 28-acre intermodal portion, rail limited to municipal solid waste; 99-year state lease (1991) to Harlem River Yard Ventures (Galesi Group); FedEx distribution centre (2007); FreshDirect construction began Dec 2014; Oak Point Link opened 1998. → §5.5, §7 rail-yard card, §8 Harlem River Yards card, Q&A sublease question, Landmarks, Streets table.
- Query: `Port Morris Bronx new rental towers waterfront Bankside Third Avenue Bridge 2025` · Firecrawl web search →
  - https://www.6sqft.com/new-rental-buildings-in-the-bronx/ (excerpt): Bankside $950M, seven towers, Brookfield, spans the Third Avenue Bridge; Bankside Park opened 2024; Third at Bankside 2401 Third Ave, three towers 17–25 storeys, 458 units; Maven 2413 Third Ave, 200 units, CetraRuddy. → §7 towers card, §8 Third Ave card, Streets table.
  - https://www.brickunderground.com/rent/what-renters-can-get-mott-haven-bronx-new-rental-developments (excerpt): Third at Bankside 324 market + 134 affordable (opened March 2022); Lincoln at Bankside four towers, 644 market + 277 affordable; Maven 60 rent-stabilized middle-income units. → Sources table only.
  - https://rent.brookfieldproperties.com/property/third-at-bankside/ (excerpt): 2385 3rd Ave, Bronx NY 10451. Not used (marketing/rents).
- Query: (first search) → https://newyorkyimby.com/2026/08/construction-nears-completion-on-307-bruckner-boulevard-in-port-morris-the-bronx.html (Firecrawl scrape, Aug 9, 2026): 307 Bruckner Blvd, two-storey last-mile logistics facility, ~100,000 sq ft, 59 ft tall, ~46,000 sq ft covered fleet parking/storage at ground level, 46,000 sq ft high-bay warehouse with 36-ft clear heights, 8,200 sq ft mezzanine, four loading docks, two drive-in doors, ESFR, 4,000 amps; scheduled to open Q3 2026; Sterling Organization / AO Architects; Cypress Ave 6 station two blocks south; under a mile from RFK, Willis and Third Ave bridges. Related-article titles: permits filed for 132 Brown Place (Oct 2025), 20 Brook Ave (Apr 2026), 521 E 132nd St (May 2026); housing lottery 132 Brown Place (Aug 2026). → §5 para 2, §5.5, §7 logistics card, Studios & Depots section, Streets table, Siting (bridges).
- Query: `Union Crossing 825 East 141st Street Bronx office studios tenants` · Firecrawl web search → https://therealdeal.com/new-york/2023/03/22/maddd-equities-sobro-buy-empty-bronx-office-building-for-44m/ (Firecrawl scrape, Mar 22, 2023): seven-storey former warehouse built 1916 as an A&P baking facility; bought 2016 for $39M, ~$45M renovation into flex offices, retail and studio space; sold 2023 to Maddd Equities and SoBro for $44M (with adjacent lot at 804/825 E 141st); Westhab 8,000 sq ft lease (2019); banner advertising 300,000 sq ft available. Excerpts: 6sqft/CityRealty "275,000 square feet of office and studio space" — NOT used (conflicting size). → hero, §5, §7 warehouse card, §8 E 138th–141st card, Change of use, Streets table.
- Query: `Silvercup North 295 Locust Avenue Bronx studio Port Morris` · Firecrawl web search →
  - https://www.silvercupstudios.com/north/ (Firecrawl scrape): North Lot, 295 Locust Ave; four sound stages 8,030–16,220 sq ft, "52-Foot Ceilings" (stage spec tables list 50 ft height); 33,900 sq ft office, 63,940 sq ft support; North Lot totals 148,140 sq ft; on-lot parking for 60+ vehicles; 4,800 amps per stage. → §5.5, Studios & Depots section, §8 Locust card, Landmarks card, Streets table.
  - https://www.nyc.gov/site/mome/news/070115_silvercup_bronx_expansion.page (excerpt, July 6, 2015): expansion to 295 Locust Ave. → Landmarks card.
- Query: `Estey Piano Company Factory landmark designation Lincoln Avenue Bruckner Boulevard clock tower lofts` · Firecrawl web search → https://hdc.org/buildings/estey-piano-company-factory/ (excerpt: brick facades, corner clock tower); https://urbanarchive.org/... (excerpt: 112–128 Lincoln Ave, A. B. Ogden & Sons, 1885, oldest known piano factory still standing in the borough); https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=446255&GUID=E21ED519-1DAB-41FF-B7E5-89EA2A435952 (Res 0484-2006 affirming LPC designation); https://www.citylandnyc.org/... (excerpt: "The 1886 Estey Piano Factory, at 112 Lincoln Avenue"). → §5.5 (1885–86), §8, Landmarks card.
- Query: `Per Scholas Bronx 804 East 138th Street tech training campus` · Firecrawl web search → https://www.perscholas.org/locations/new-york/ (excerpt: 804 E 138th St #2, Bronx 10454). → §8 E 138th–141st card, Streets table.
- Query: `Port Morris Industrial Business Zone IBZ Bronx businesses` · Firecrawl web search → https://www.sobro.org/industrial (excerpt: SoBro is the Industrial Business Solutions Provider for all five Bronx IBZs: Bathgate, Port Morris, Eastchester, Zerega, Hunts Point); https://edc.nyc/industry/industrial-and-manufacturing (excerpt: Bronx IBZs list); City Record "Port Morris Industrial Business Zone Ratified Boundaries September 2013" (PDF, excerpt only). → §8 Locust card, Q&A IBZ question.
- Query: `Bronx Brewery East 136th Street Port Morris taproom OR "Port Morris Distillery"` · Firecrawl web search → Facebook group excerpt about Port Morris Distillery closing after 12 years; unioncrossingbronx "Your Neighbors" excerpt (brewery at 856 E 136th St). NOT used (unverified status).
- Query: `Port Morris Bronx last-mile warehouse Amazon delivery station Oak Point Bruckner 2025` · Firecrawl web search → results were Hunts Point (Viele Ave) and 1055 Bronx River Ave, not Port Morris. EMPTY for Port Morris; not used.

### Flooding, waterfront, air quality
- Query: `Port Morris Bronx flooding Hurricane Sandy flood zone waterfront industrial resiliency` · Firecrawl web search →
  - https://www.southbronxunite.org/community-managed-waterfront (Firecrawl scrape): after Sandy the waterfront was "upwards of 3.5 feet underwater"; waterfront uses: waste transfer stations (5,000 and 2,000 tons/day), peaker power plants, abandoned WSJ/NY Post printing presses, FreshDirect ~1,000 daily diesel truck trips; 96-acre NYSDOT land leased 1991 to Harlem River Yard Ventures; Phase 1 sites Lincoln Ave street end and E 132nd St Pier. → Siting section paras 1 & 3, §5.5, Streets table (Lincoln Ave street end).
  - https://www.motthavenherald.com/2023/03/26/federal-coastal-resiliency-plan-south-bronx-flooding-climate-change/ (Firecrawl scrape, Mar 26, 2023): USACE $52B NY & NJ HATS study; tentatively selected plan with flood walls and deployable gates roughly from Yankee Stadium to the RFK Bridge; Port Morris walls are an "induced" measure; final proposal likely not built until at least 2044; heavy rainfall (Hurricane Ida) noted as a separate risk. → Siting section para 1.

### Local codes / technical (new for this page)
- Query: `NFPA 13 sprinkler piping shall not be used to support non-system components cables hangers` · Firecrawl web search → https://www.meyerfire.com/daily/any-contact-allowed-with-sprinkler-pipe (excerpt quoting NFPA 13: "Sprinkler piping or hangers shall not be used to support non-system components."); https://up.codes/s/support-of-non-system-components; https://www.nfpa.org/news-blogs-and-articles/blogs/2022/04/18/hangers-and-support-of-sprinkler-system-piping. → §8.5 bullet, §10.5 Claim 3, Process step 5.
- Query: `building code interior exit stairway penetrations limited to items serving the stairway 1023.5` · Firecrawl web search → https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-174119 (excerpt, 2022 NYC BC 1023.5: "Penetrations into or through interior exit stairways and ramps are prohibited except for equipment and ductwork necessary for independent ventilation or…"). → §8.5 bullet.
- Silo sources reused: OFNR/OFNP (cablinginstall), FOA bend radius/pulling, DOB sub-50 V statement (site content), NEC 620.37 hoistway (Bronx section). → §8.5, §10, Process.
- General practice, no citation (flag for Anwar if a citation is wanted): post-tensioned slab GPR scanning before coring; brownfield vapour-barrier/sub-slab penetration sealing per environmental engineer; minimum installation temperature of cable; pigeon-dropping clean-up before work; electrical-room working clearances.
- Local news on Port Morris fiber-installation contractors 2026: EMPTY (none retrieved).

### Pricing used (existing AESS prices only — no new prices; same lines as /fiber-optic-installation-bronx)
- $35/termination · $40/strand OTDR · $391 MM drop · $447 SM drop (Bronx structured-cabling configurator) · 12-strand OM4 $4,500–$7,000 · 24-strand OS2 $8,000–$15,000+ · second telecom room with fiber link from $2,400 · $195/hr, 3-hr min ($585).
- Worked examples (sums of published lines only): Starter $527 = $447 + 2×$40; Standard from $3,741 = $2,400 + 3×$447; Premium $6,300–$8,800 = $4,500–$7,000 + 24×$35 ($840) + 24×$40 ($960); hypothetical warehouse-floor example $4,128 = 48×$40 + 12×$35 + 4×$447 (+ optional room from $2,400).
- Same open conflict as the Bronx section: §9 says Bronx 1.00× but the live Bronx configurator publishes $391/$447.

### Images (11) — Step C; Drive folder `AESS Website Photos/Fiber Optic Installation` empty this run, CompanyCam not connected
All copied from images/fiber-optic-installation/ and cropped (to exclude faces and shirt/van phone numbers), saved as WebP q80 under new names. Each viewed before captioning; alt/title/caption describe only what is visible.
| File (images/fiber-optic-installation/) | Source file | Crop | Shows |
|---|---|---|---|
| fiber-optic-installation-port-morris-fusion-splicer-bench-fiber-panel.webp (hero) | …-manhattan-fusion-splicer-patch-rack.webp | right side | splicer, SC panel, IPA, cleaver, tray |
| fiber-optic-installation-port-morris-tangled-closet-before-cleanup.webp | …-rockland-county-inherited-closet-before-after.webp | "before" half | tangled closet |
| fiber-optic-installation-port-morris-ceiling-grid-bundle-feed.webp | …-dutchess-county-ceiling-grid-cable-feed.webp | right side | hands feeding bundle into grid |
| fiber-optic-installation-port-morris-core-bit-block-wall-penetration.webp | …-westchester-county-block-wall-drill-penetration.webp | right side | core bit, cable through hole, Cat 6 box |
| fiber-optic-installation-port-morris-emt-pull-box-cable-feed.webp | …-ulster-county-conduit-box-pull-block-wall.webp | right side | hands at EMT pull box |
| fiber-optic-installation-port-morris-high-bay-basket-tray-dome-camera.webp | …-ulster-county-high-bay-tray-dome-camera.webp | right/top | basket tray, dome camera, racking |
| fiber-optic-installation-port-morris-crew-open-ceiling-cable-reels.webp | …-dutchess-county-crew-reel-pull-open-floor.webp | none (backs only) | crew, reels, rack |
| fiber-optic-installation-port-morris-sc-adapter-panel-yellow-jumpers.webp | …-nyc-splice-tray-patching.webp | panel only | SC adapters, yellow jumpers |
| fiber-optic-installation-port-morris-brick-wall-outdoor-enclosure-conduit.webp | …-ulster-county-exterior-enclosure-brick-wall.webp | right side | enclosure, EMT, brick |
| fiber-optic-installation-port-morris-shop-open-ceiling-cable-drop.webp | …-ulster-county-retail-shop-open-ceiling-pull.webp | right side | open-ceiling shop, cable drop |
| fiber-optic-installation-port-morris-van-shelves-cable-reels-ladders.webp | …-ulster-county-service-van-cable-reels.webp | van interior | reels, ladders, tool cases |
Note: same scenes appear (uncropped) on sibling pages; library photos look AI-rendered (garbled small text, repeated faces across "different" jobs) — flagged for Anwar as on every earlier fiber page. Log line: `images: 11 reused from images/fiber-optic-installation/ (cropped; no real fiber photos yet)`.

### Keyword plan (Port Morris page)
Service: fiber optic installation Port Morris, fiber riser converted loft, warehouse fiber link, studio fiber backbone, fiber audit/inherited fiber, fusion splicing, OTDR testing. Problem: change of use, entrance in sidewalk vault, no riser in factory building, tenant split, abandoned cable, vehicles/forklifts, hot work, scrap theft, brownfield vapour barrier, post-tensioned slabs, flooding, dust/soot. Technology: OS2, OM4, armored, indoor/outdoor loose-tube, OFNP/OFNR, MPO, enclosures, media converters/SFP. Industry: lofts/live-work, creative offices, film/TV studios, last-mile logistics/fleet depots, distribution (Harlem River Yards), fabrication shops, new rental towers, rowhouses, training campuses. Geographic: Port Morris, Bruckner Boulevard, Alexander Ave, Lincoln Ave, Third Ave, E 132nd–E 141st Streets, Locust/Willow/Walnut Aves, Harlem River Yards, Bronx Kill, Randall's Island, Mott Haven, Hunts Point, Bronx.

### Question register additions
fiber-optic-installation-port-morris-bronx-ny
§9 Questions Answered (and other question headings):
- Port Morris Fiber Link Down This Morning? (repair capture heading)
- The provider's cable reaches our building through an old sidewalk vault that takes on water — can the entrance be moved?
- Before we sign a lease on an older industrial building, how can we find out which carriers can already serve it?
- Our lease may end when the owner redevelops the site — which parts of a fiber installation can a tenant take along when it moves?
- Can the fiber equipment share the main electrical room in a building with very large power service?
- Our stage has to stay silent during takes — will fiber enclosures and switches add noise the microphones pick up?
- We rent our loft for events a few nights a month — can visiting vendors get a network connection without touching ours?
- Our delivery fleet parks on the ground floor and the warehouse is upstairs — how does fiber get from dispatch to the upper bay?
- The electric-van chargers in our fleet garage need a network connection — is fiber worth running to them?
- Can fiber run through a metal fabrication or welding shop where sparks and hot slag fly?
- Does fiber get stolen for scrap the way copper cable does?
- We sublease from a company that itself leases the land from the State — how many sign-offs does a new fiber entrance need?
- Will exterior conduit on our street wall get tagged or broken, and how is it protected?
- Is there any help for industrial businesses in the Port Morris Industrial Business Zone that are planning a network upgrade?
- Our new building sits on a cleaned-up brownfield with a vapour barrier under the slab — can fiber conduit pass through it?
- Our new tower has post-tensioned concrete floors — how do you core through them without hitting a tendon?
- Our rental building has a resident co-working lounge — should it run on the building's own fiber or on a resident's internet account?
- Port Morris Studio, Loft or Warehouse Offline? (final repair heading)
§17 FAQ:
- Do you also take fiber jobs on Randall's Island, across the Bronx Kill?
- Can the labels and the closeout paperwork be in Spanish as well as English?
- What happens if the ceiling or attic space we need is fouled with pigeon droppings?
- Can fiber work go ahead while the building is still on temporary construction power?
- Our loft building has no working elevator — does carrying materials up the stairs change the price?
- Our construction lender pays out in draws — can your proposal be broken into the line items its inspector checks?
- Can fiber carry the monitoring link for rooftop solar panels or a battery system?
- Can fiber be pulled in an unheated building during a cold snap?
- Do you supply the hybrid fiber cables that broadcast cameras plug into?
- Can we see a sample test report before we hire you?
- Can the old fiber enclosures and patch panels a previous tenant left behind be reused?
- Do we need to tell our property insurer before fiber work starts?

De-dup notes: checked by meaning against the full register and the 16 live fiber pages plus the concurrent Midtown and St. George neighbourhood drafts. Two FAQs were replaced after the concurrent pages appeared (dust control while drilling — St. George; digital signage over fiber — Midtown). Sprinkler-pipe supports and exit-stair penetrations appear only as §8.5 compliance bullets, not as questions (Midtown asks both as questions). Post-tensioned-slab and brownfield items are answered once, in §9 only.

## St. George, Staten Island — local research (2026-10-17 batch, fiber-optic-installation-st-george-staten-island-ny)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md are reused where noted; only St. George research is added here. Up-link /fiber-optic-installation-staten-island; phone (347) 934-8335; Brooklyn GBP.

Page thesis: St. George is the one part of Staten Island where fiber goes **up and through** rather than across a yard — hillside Queen Anne/Shingle houses in the St. George/New Brighton Historic District (cellar at grade on the downhill side), houses divided into two- and three-family homes with no common hallway, pre-war co-ops and a 20-storey tower, a 1930s poured-concrete factory turned lofts, new mixed-use buildings at the terminal, and small offices around Borough Hall and the courts. So the work is vertical routes in old finishes, board/landlord/LPC paperwork, inherited wiring from earlier conversions, and scheduling around a neighbourhood that runs on the ferry. (Parent Staten Island page = lateral yard/aerial/buried links; not repeated.)

### Reddit (local)
- Query: `reddit statenisland St. George internet fiber apartment building Fios` · Firecrawl web search (excerpts only; Firecrawl does not scrape reddit.com) → no r/statenisland thread returned. r/statenisland: EMPTY.
  - https://www.reddit.com/r/Fios/comments/lfhywy/if_an_apartment_complex_says_theyre_wired_for/ — excerpt: "The term "wired for fios" means the infrastructure is in the building. The apartments are wired per order." → §10.5 H3 3 (quoted as a Reddit answer; not St. George-specific).
  - https://www.reddit.com/r/Fios/comments/1u2ndd4/getting_fios_installed_at_a_brooklyn_apartment/ — excerpt "the building still has to be setup… FAST ticket for engineering" → background only, not quoted.
  - https://www.verizon.com/home/internet/near-me/new-york-ny/ (same search, excerpt): "In apartment buildings or homes not yet wired for Fios: Verizon coordinates with the property manager/owner to wire and install the service." → §10.5 H3 2 (paraphrased + "not yet wired for Fios" quoted).
  - https://www.broadbandsearch.net/service/new-york/staten-island (same search; WebFetch): "Fiber service is concentrated in St. George, Tompkinsville and parts of the North Shore," "while the South Shore and many inland suburban blocks remain served primarily by cable." No source cited by the site. → §10.5 H3 1 (quoted claim, flagged as unsourced).

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitutes for §10.5 (claims quoted/summarised as published): broadbandsearch and Verizon FAQ (above); Reddit r/Fios (above); silo sources reused — streamlinetelecom.com "$1-6 per linear foot" (H3 4), thenetworkinstallers.com citing FBA 2025 underground median $18/ft, aerial $8/ft (H3 5), multifamilyresources.quantumfiber.com stages 30 days off-site / 30 on-site / 40–60 days activation (H3 6, summarised, not quoted), t-mobile.com "can take up to 4 hours" and att.com four to six hours (H3 7). Yelp 1–3★ for St. George fiber/cabling: no query returned yelp.com results. EMPTY.

### Landmarks, civic buildings, transit
- Query: `St. George Historic District Staten Island Landmarks Preservation Commission designation report boundaries St. Marks Place` · WebSearch → https://s-media.nyc.gov/agencies/lpc/lp/1883.pdf (WebFetch): St. George/New Brighton Historic District, designated July 19, 1994 (LP-1883); "some 78 buildings"; portions of St. Marks Place, Carroll Place, Westervelt Ave, Hamilton Ave, Phelps Place cul-de-sac, short stretches of Richmond Terrace; earliest house 404 Richmond Terrace c.1835, peak 1880s–90s, last house 1926–28; styles Greek Revival → Queen Anne/Shingle (predominant) → Colonial Revival, Craftsman, Art Deco; "three crescent-shaped streets ascending a steep hillside"; "taking advantage of the hilly topography"; "Most houses are larger than they appear from the street due to the sloping terrain"; "terraced landscape". → §5 para 3, §5.5 facts 1–2, §7 cards, "On the Hill" section, Sources.
- Query: `St. George Staten Island Borough Hall 10 Richmond Terrace built 1906 Carrère and Hastings` · WebSearch → https://en.wikipedia.org/wiki/Staten_Island_Borough_Hall (WebFetch): 1906, Carrère and Hastings, 10 Richmond Terrace, brick and limestone, Beaux-Arts/French Renaissance, NYC landmark March 23, 1982, NRHP 1983, 13 WPA murals by Frederick Charles Stahr. → §5 para 1, §8 Richmond Terrace card, §13 card.
- Query: `Richmond County Supreme Court new courthouse 26 Central Avenue St. George opened` · WebSearch → https://en.wikipedia.org/wiki/Richmond_County_Courthouse_(Staten_Island) (WebFetch): 18 Richmond Terrace, opened Nov 3 1919, Carrère and Hastings, NYC landmark 1982; most Supreme Court parts moved to 26 Central Avenue, opened Sept 28 2015; Matrimonial Parts and Surrogate's Court remain. → §5 para 1, §8 Central Ave card, §13 card, civic-centre section.
- Query: `St. George Ferry Terminal Staten Island ferry annual riders terminal renovation` · WebSearch → https://en.wikipedia.org/wiki/St._George_Terminal (WebFetch): ferry terminal opened 1886; 1946 fire; city-built facility opened June 8 1951; four bus ramps A–D; 22 NYCT routes listed; northern terminus of Staten Island Railway. → §5 para 1, Ferry Time section, §13 card.
  - https://malliotakis.house.gov/media/press-releases/malliotakis-announces-575-million-st-george-ferry-terminal-upgrades (WebFetch): June 9 2025 release, $5,750,000 FTA Passenger Ferry Grant for replacing bus ramp passageways and terminal chillers (headline "575 million" is a typo for $5.75M). → §13 terminal card.
- Query: `Staten Island Ferry daily riders trips per day NYC DOT facts 5.2 miles 25 minutes` · WebSearch → https://en.wikipedia.org/wiki/Staten_Island_Ferry (WebFetch): 16,692,900 riders in calendar 2025; 5.2 miles; ~25 minutes; 24/7; nine boats. → §5.5 fact 3, Ferry Time section. (NYC DOT's own facts page not fetched.)
- Query: `St. George Theatre 35 Hyatt Street opened 1929 seats Staten Island` · WebSearch → https://en.wikipedia.org/wiki/St._George_Theatre (WebFetch): 35 Hyatt St, opened Dec 4 1929, 1,903 seats today, architect Eugene De Rosa (with James Whitford), interiors Nestor Castro; landmark status not stated. → §8 Hyatt St card, §13 card.
- Query: `Curtis High School Hamilton Avenue St. George landmark 1904 C.B.J. Snyder` · WebSearch → https://hdc.org/buildings/curtis-high-school/ (WebFetch): 105 St. Marks Pl, 1902–04 with additions 1922/1925/1937, C.B.J. Snyder, Collegiate Gothic, "Designated Individual Landmarks" (year not stated). → §13 card.
- Query: `SIUH Community Park 75 Richmond Terrace FerryHawks ballpark St. George opened 2001` · WebSearch → https://en.wikipedia.org/wiki/SIUH_Community_Park (WebFetch): 75 Richmond Terrace, opened June 24 2001, capacity 7,171, Staten Island FerryHawks, formerly Richmond County Bank Ballpark. → §8 Richmond Terrace card, §13 card, Ferry Time para 3.
- Query: `Empire Outlets Staten Island opened 2019 square feet St. George ferry terminal` · WebSearch → https://en.wikipedia.org/wiki/Empire_Outlets (WebFetch): grand opening May 15 2019; ~350,000 sq ft; next to St. George Terminal; built by BFC Partners, SHoP Architects; Goldman Sachs acquired at Sept 2023 foreclosure auction (not used); garage figure conflicting 1,200/1,250 (not used); hotel component not confirmed built (not used). → §8 waterfront card, waterfront section.
- Query: `St. George Library Center 5 Central Avenue Staten Island NYPL` · WebSearch → https://gopher.nypl.org/locations/st-george-library-center (search result title/URL only: "5 Central Avenue … Staten Island, NY 10301"). → §8 Central Ave card.
- Query: `National Lighthouse Museum St. George Staten Island address 200 The Promenade Lighthouse Service depot` · WebSearch → https://ohny.org/place/national-lighthouse-museum-and-us-lighthouse-service-super-depot/ (WebFetch returned only a loading shell). EMPTY — museum not used on the page.

### Building stock / housing
- Query: `St. George Staten Island neighborhood guide renters housing types Victorian homes converted apartments` · Firecrawl web search → https://www.defalcorealty.com/neighborhood-guide/st-george-staten-island/ (excerpt, 2026 guide): ~8,600 residents (20,500 incl. New Brighton); ~70% of housing units renter-occupied (St. George–New Brighton area); two- and three-family properties common on the streets climbing south of Richmond Terrace; historic homes on streets above Fort Hill and along Daniel Low Terrace; "The 20-story Castleton Park Apartments on St. Marks Place ranks among the tallest structures on Staten Island." → §5 para 1/3, §5.5 facts 4–5, §7 cards, FAQ 1 (Fort Hill).
  - https://ranolarealestate.com/living-in-st-george-staten-island-2026/ (Firecrawl scrape, May 16 2026): four housing tiers — condo/co-op towers near the ferry, pre-war loft and apartment conversions near Bay Street, brownstones/multi-family townhouses (many legal 2–3 family), restored Victorian/Queen Anne houses on the hill (St. Marks Pl, Westervelt, Carroll Pl, Hamilton Ave); "Bay Street and Stuyvesant Place are full-on walkable retail corridors with bars, coffee shops, restaurants … galleries". Real-estate prices NOT used. → §7, §8 Bay St / Stuyvesant Pl cards.
  - Same search → apartments.com local guide (excerpt "2,800 seat St. George Theatre") — NOT used (conflicts with Wikipedia's 1,903 current seats).
- Query: `Castleton Park St. George Staten Island towers Hamilton Avenue apartments CAMBA` · WebSearch → https://rebusinessonline.com/stellar-management-camba-housing-ventures-acquire-castleton-park-on-staten-island/ (WebFetch, July 24 2015): 454 apartment units, "40-year-old development"; storeys not stated (20-storey from DeFalco). → §5.5 fact 5, §7 tower card.
- Query: `Bay Street Landing St. George Staten Island warehouse conversion condos history` · WebSearch → https://scaranoarchitect.com/project/bay-street-landing/ (WebFetch): 1930s waterfront factory building of poured-in-place concrete, converted to residential lofts with new addition; unit count not stated. → §5 para 3, §7 loft card, §9 concrete-loft Q.
- Lighthouse Point: Query `Lighthouse Point St. George 2026 phase two tower hotel YIMBY` · WebSearch → https://newyorkyimby.com/2025/06/lighthouse-point-phase-one-finishes-construction-at-5-bay-street-in-st-george-staten-island.html (WebFetch): 5 Bay Street, 115 units, ~60,000 sq ft commercial; tenants CSI Tech Incubator, The Learning Experience, Club Pilates; Cooper Carry / Triangle Equities; site of U.S. Lighthouse Service General Depot 1863–1966. Future phases not mentioned. (Silo SI research also has Triangle Equities June 6 2025 release.) → §5 para 3, §5.5 fact 6, §7 new-building card, waterfront section.

### Local news / hyperlocal / planning
- Query: `silive St. George 2026 new apartment towers waterfront development Staten Island` · WebSearch →
  - https://www.defalcorealty.com/blog/staten-island-multifamily-development-pipeline/ (WebFetch; Jan 27 2026, mod. Apr 29 2026): North Shore Action Plan ~2,400 potential homes; Lighthouse Point 115 units 2025; other projects in Stapleton (not used). → waterfront section para 1.
  - https://www.nyc.gov/assets/statenislandcb1/downloads/pdf/2026/Land-Use-Meeting-Agenda-March-3-j2026.pdf (WebFetch): CB1 Land Use agenda Mar 3 2026 — 198-208 Richmond Terrace, zoning amendments sought for a 14-storey mixed-use building. → waterfront section para 1 (described as "on Richmond Terrace", no outcome claimed).
  - YIMBY "Liberty Towers" (2020) and Bisnow results — not opened, not used.
- Query: `silive St. George Staten Island internet outage fiber Verizon Spectrum 2025 2026` · Firecrawl web search → irrelevant results. Query `silive St. George Staten Island news October 2026` · WebSearch → no relevant SI Advance item. SI Advance/silive fiber or internet news for St. George: EMPTY.
- Broadband statistics by community district: https://council.nyc.gov/data/internet-access/ (WebFetch) gives no Staten Island CD figures on the page. EMPTY (not used).

### Local licensing / permits / building rules
- Query: `Landmarks Preservation Commission permit guidebook historic district interior work no permit unless exterior conduit wiring visible` · WebSearch → https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Introduction.pdf (WebFetch): permit generally needed for work affecting the exterior "including parts not visible from the street" (paraphrased on page, not quoted), and work in front/side/rear yards; interior work needs an LPC permit when it needs a DOB permit; HVAC louvers/vents count as exterior; PMW (exterior work not needing DOB permit), CNE, Certificate of Appropriateness. → §8.5 Landmarks bullet, §9 LPC rear-wall Q, nonprofit Q, renovation section, Sources.
  - https://www.nyc.gov/site/lpc/applications/permits-and-making-alterations.page — WebFetch blocked (permission request not answered in build env). EMPTY (not accessible in build env); guidebook used instead.
- Silo sources reused: DOB sub-50 V statement (site's structured-cabling-pricing page), firestopping (nyflnerds/unifinerds), OFNR/OFNP (cablinginstall.com), FOA bend radius 10×/20×, NEC 770 abandoned optical cable (mikeholt.com). → §8.5, §10, FAQ bend question, inherited-wiring section.
- Fios footprint: silo source https://espanol2.verizon.com/about/node/141763 — Staten Island "virtually all" premises passed at end-2013. → §5 para 4, §10.5 H3 1.

### Pricing used (existing approved prices × blueprint §9 Staten Island 1.10×; identical to the live Staten Island fiber page table — no new prices)
$39 termination · $44 OTDR/strand · $385 MM drop · $440 SM drop · $4,950–$7,700 12-strand OM4 backbone · $8,800–$16,500+ 24-strand OS2 · from $2,640 second telecom room · $195/hr, 3-hr min ($585) protected.
Worked examples (sums of published lines only): 2 × $440 = $880; 3 × $385 = $1,155; 24 × $39 + 12 × $44 = $936 + $528 = $1,464; $4,950–$7,700 + from $2,640 = from $7,590.
Packages: Starter $1,464 (re-terminate + OTDR a 12-strand riser) · Standard $4,950–$7,700 · Premium from $7,590 (backbone + second closet) · BYOE $195/hr, 3-hr min. (Open CONFLICT from SI research still applies: structured-cabling-pricing-staten-island.html shows $411/$470 drops ≈1.175×.)

### Images (11) — Step C library; Drive folder `AESS Website Photos/Fiber Optic Installation` empty this run, CompanyCam not connected
Copied within images/fiber-optic-installation/ as WebP q80. Looked at each before choosing; skipped every image with a frontal/readable face, a readable document (cable map sheet, IDF floor-plan sheet) or a visible street number. Printed phone numbers on shirts/caps were pixelated + blurred (844-386-7238 is not an approved number; 800 also blurred for consistency). Back-turned or cropped-profile shots only.
| New file | Source | Edit |
|---|---|---|
| fiber-optic-installation-st-george-fusion-splicer-sc-panel.webp | fiber-optic-installation-brooklyn-splice-tray-enclosure.webp | shirt number blurred |
| fiber-optic-installation-st-george-brick-wall-enclosure-conduit.webp | fiber-optic-installation-staten-island-exterior-wall-enclosure-conduit.webp | (already blurred) |
| fiber-optic-installation-st-george-ceiling-tile-coil-feed.webp | fiber-optic-installation-staten-island-ceiling-tile-cable-feed.webp | (already blurred) |
| fiber-optic-installation-st-george-rack-patch-cord-dressing.webp | fiber-optic-installation-manhattan-idf-rack-patching.webp | none |
| fiber-optic-installation-st-george-jhook-bundles-above-ceiling.webp | fiber-optic-installation-orange-county-jhook-pathway-open-ceiling.webp | shirt number blurred |
| fiber-optic-installation-st-george-recessed-media-box-tester.webp | fiber-optic-installation-suffolk-county-recessed-wall-box-patching.webp | none |
| fiber-optic-installation-st-george-rack-laptop-switch-setup.webp | fiber-optic-installation-ulster-county-rack-switch-laptop-setup.webp | hoodie + cap numbers blurred |
| fiber-optic-installation-st-george-lift-ceiling-access-point.webp | fiber-optic-installation-long-island-scissor-lift-ceiling-access.webp | shirt number blurred |
| fiber-optic-installation-st-george-soffit-camera-drill-mount.webp | fiber-optic-installation-staten-island-storefront-canopy-camera-mount.webp | none |
| fiber-optic-installation-st-george-conference-display-recessed-box.webp | fiber-optic-installation-nassau-county-conference-room-cable-box.webp | none |
| fiber-optic-installation-st-george-van-reels-ladders-tool-bag.webp | fiber-optic-installation-suffolk-county-van-cable-reels-ladders.webp | none |
Flag for Anwar: the whole library still looks AI-rendered (garbled box text, invented logos, a fake "844-386-7238" number on shirts). Rule says real photos only; these were the only fiber-folder images available. Several scenes now appear on 2–4 fiber pages.

### Keyword plan (St. George page)
Service: fiber optic installation St. George, fiber riser, building backbone, house fiber riser, co-op fiber backbone, fusion splicing, OTDR testing, fiber termination. Problem: Wi-Fi fades upstairs, no common hallway, locked telephone closet, inherited/abandoned wiring, landmark permits, concrete slabs, alteration agreements. Technology: OS2 bend-insensitive, OM4, OFNR/OFNP, micro-cable, wall enclosures, splice panels, SFP/media converters, surface raceway. Industry: hillside houses, two/three-family conversions, co-ops/condos, lofts, law offices/nonprofits, new-building tenants. Geographic: St. George, Staten Island, Bay Street, Richmond Terrace, Stuyvesant Place, Central Avenue, Hyatt Street, St. Marks Place, Hamilton Avenue, Westervelt Avenue, Carroll Place, Tompkinsville, New Brighton, Fort Hill, Randall Manor, Stapleton, West Brighton.

### Question register additions
fiber-optic-installation-st-george-staten-island-ny
§9 Questions Answered:
- Our house is built into the hillside, with the cellar at street level on one side and underground on the other — which level should the network start from?
- Does the Landmarks Preservation Commission care about conduit on the back of a historic-district house, where nobody on the street can see it?
- Can fiber follow the old radiator pipe chases up through a Victorian house?
- Would fiber to the top floor fix Wi-Fi that fades on the stairs of a four-storey house, or is a mesh kit enough?
- Our converted Victorian has no common hallway — every stair belongs to one apartment — so where can a building-wide fiber riser run?
- We're turning a three-family house back into a single home — what happens to the three sets of provider wiring, and where should the new fiber go?
- Our condo is in a 1930s poured-concrete factory building on the waterfront — how does fiber get through slabs and columns like that?
- Our co-op's alteration agreement asks for a scope of work — how much detail should the fiber section contain?
- The old telephone closet in our co-op is locked and nobody on the board knows who has the key — can fiber work start without it?
- We're a small law office near the courthouses with a records room in the basement — can scanning stations down there run over fiber without putting a server in the cellar?
- We're fitting out a shop or studio unit in a brand-new building by the ferry — what does the developer's telecom room give us, and what do we have to build ourselves?
- Our nonprofit shares an older building on Richmond Terrace with other tenants — can we have fiber of our own without paying for a whole-building system?
§17 FAQ:
- Do you work in the neighbourhoods next to St. George — Tompkinsville, New Brighton, Fort Hill and Randall Manor?
- How do you keep dust down when drilling through old plaster in a lived-in house?
- Can the small fiber box at each end be painted to match period woodwork?
- How tight can fiber bend around the corners of a narrow Victorian stair?
- Can the building's video intercom use the same fiber as the internet?
- Does fiber give off any radiation or signal that could bother people living next to it?
- If we change internet providers, does the fiber you installed still work?
- How are the strands labelled when each one serves a different apartment?
- Do we have to warn the neighbours in the attached house before you drill near the shared wall?
- Can fiber reach a turret room or attic studio at the very top of the house?
Other headings: none end in "?" (repair headings worded as statements).

De-dup notes: two draft questions were replaced after comparing with the concurrent Port Morris and Midtown drafts — "only entrance up a long flight of outdoor steps" (≈ Port Morris "no working elevator — carrying materials up the stairs") and "nonprofit … who has to sign off" (≈ Port Morris State-sublease sign-offs and SI SNAD sign-off). Closest remaining intents for the main run to judge: radiator-chase route vs Midtown "Con Edison steam beside the telecom entrance — will the heat harm fiber" (mine = route, theirs = heat proximity); FAQ bend radius vs Midtown "Is bend-insensitive single-mode worth paying for" (mine = limit, theirs = value); co-op scope-of-work vs Manhattan "drawings the landlord's engineer can review"; video intercom vs NYC-hub-family "phone system over the same fiber".

### Build checks (this builder)
- `python3 tools/check_page.py fiber-optic-installation-st-george-staten-island-ny --no-registration --stats`: 12,343 words, title 52, meta 157, 11 figures, 6 JSON-LD blocks, FAQ 10 = schema 10, 2 forms, tel 347 + 800 (header only), 168,924 bytes. Only remaining failures: 16 × "live sibling … doesn't link back" (area pages must link down — main-run wiring; not touched by this builder).
- Masked paragraph similarity (difflib, word level, ≥12-word paragraphs, exempt warranty/NAP/licence line/freshness stamp/consent text/quoted source claims): max 0.623 vs fiber-optic-installation-staten-island (final repair paragraph); all other siblings ≤ 0.571.
- Cross-link block contains the comment `<!-- NEIGHBOURHOOD SIBLINGS: … -->` where the main run adds neighbourhood sibling links.
- Rendered at 1440 and 390 px (Playwright): no horizontal scroll.

## Midtown, Manhattan — local research (2026-10-17 batch, fiber-optic-installation-midtown-manhattan-ny)
Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources (top of research/fiber-optic-installation.md) and the Manhattan section are reused where noted; only Midtown-specific research is new here. Thesis: Midtown fiber is a vertical-stack problem — elevator-bank changes, mechanical floors and pre-war setbacks (not distance) decide the route — with sub-district rules layered on (East Midtown rezoning towers, Plaza District, Sixth Ave slabs, Times Square signage, landmarked theatre interiors, Diamond District security, Garment District lofts under the 2025 MSMX rezoning, Con Ed steam in the cellars). Kept clear of FiDi and Chelsea topics (no carrier hotels, no Sandy/flood material, no 111 Eighth Ave).

### Reddit (local / topical)
- Query: `reddit Midtown Manhattan office building internet fiber riser landlord slow` · Firecrawl web search (excerpts only; reddit.com threads not opened).
  - https://www.reddit.com/r/networking/comments/26uymj/i_own_an_office_building_how_can_i_provide_my/ — excerpt: owner of an office property wants "to install a system where I can provide my tenants with internet access through fiber." → §5 THE NEIGHBORHOOD (paraphrased, not Midtown-specific).
  - https://www.reddit.com/r/sysadmin/comments/1k5et51/do_you_cut_all_your_cabling_when_moving_office/ — excerpt: "We've had to tear out tons of copper and fiber, otherwise the landlord will charge to remove it." → §5 (quoted).
  - https://www.reddit.com/r/verizon/comments/1u083m9/how_do_i_get_fiber_in_my_building_nyc/ — already in silo research; not reused.
- No Midtown-specific Reddit thread retrieved: EMPTY beyond the above.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitute for §10.5 reality check: claims published by carrier pages and cost guides already in the silo research, quoted as published (none of these seven claims is an H3 on the Manhattan page):
- AT&T "four to six hours" (https://www.att.com/support/article/internet/KM1066216/) and T-Mobile "up to 4 hours" (https://www.t-mobile.com/home-internet/fiber/fiber-optic-installation) → §10.5 H3 1.
- Ampcom OM4 ~400–550 m at 10G, ~150 m at 40/100G SR4; OS2 10 km+ (https://www.ampcom.com/blogs/industry-insights/how-to-choose-the-right-fiber-type-singlemode-vs-multimode) → §10.5 H3 2 and the "Reading the Stack" note (with One Vanderbilt 1,401 ft ≈ 427 m from the Manhattan section).
- Low Voltage New York cost guide (July 2026) fusion splices "$50–$150 each" (https://lowvoltagenewyork.com/resources/fiber-optic-cabling-cost-new-york/); The Network Installers $30–$75 citing Ring and Ping (https://thenetworkinstallers.com/blog/fiber-optic-installation-cost/) → §10.5 H3 3.
- The Network Installers citing FBA 2025: underground median $18.00/ft, aerial $8.00/ft → §10.5 H3 4; testing/documentation ≈5% citing Automation World → §10.5 H3 5.
- Quantum Fiber multifamily stages 30 / 30 / 40–60 days (https://multifamilyresources.quantumfiber.com/fiber-installation-journey/) → §10.5 H3 6.
- Atlantech commercial timeline, one customer waited 15 months (https://www.atlantech.net/blog/install-fiber-optic-internet-timeline) → §10.5 H3 7, with Verizon 94% Manhattan premises passed end-2013 (https://espanol2.verizon.com/about/node/141763, silo source).

### Office market / building stock
- Query: `Midtown Manhattan office availability rate 2026 report Avison Young OR CBRE OR Colliers Midtown submarket` · Firecrawl web search (PDF excerpts).
  - https://www.colliers.com/-/media/files/unitedstates/markets/new-york-city/research/new-york-city/2026/q2-2026-manhattan-office-market-quarterly-report_v2.ashx — Q2 2026: Midtown inventory 233,215,500 sf, availability 12.3%; Plaza District 84,670,506 sf, 11.0%; Times Square 58,221,381 sf, 13.2%; U.N. Plaza 4,059,924 sf, 2.1%; Manhattan 13.0%. → §5 para 1, §5.5 facts, District section (Plaza 11.0%).
  - https://www.avisonyoung.us/documents/d/new-york/manhattan-office-report-2q-2026 — Midtown 41.90% of the conversion pipeline (sf); Midtown South 8.20%; Midtown Total inventory 308.7 msf at 13.3% (AY definition, not used). → §5.5 facts.
- Query: `East Midtown rezoning 2017 adopted blocks new office space transit improvements` · Firecrawl web search → https://www.nyc.gov/content/planning/pages/our-work/plans/manhattan/greater-east-midtown (Firecrawl scrape): adopted by City Council August 9, 2017; area generally bounded by Fifth Ave, Third Ave, E 39th, E 57th; >60 million sf office, >quarter million jobs; iconic buildings named: Lever House, Seagram Building, 550 Madison, 601 Lexington, Chrysler Building; many older buildings built under pre-1961 rules with more floor area than now permitted; Vanderbilt Corridor 2015 text amendment; One Vanderbilt 30 FAR, 1.3 msf, ~$225 million of Grand Central improvements; LPC designated 12 buildings as individual landmarks; FAR 18–27 near Grand Central/Park Ave. → §5 para 3, §5.5, §7 cards, §13 landmark cards (Grand Central, One Vanderbilt, Chrysler, Seagram/Lever House), District section (pre-1961 note). Also excerpt https://www.skyscraper.org/programs/assessing-east-midtown-rezoning/ ("78-block district", not used).
- Query: `270 Park Avenue JPMorgan Chase headquarters opened 2025 height floors employees` · Firecrawl web search →
  - https://www.jpmorganchase.com/newsroom/press-releases/2025/grand-opening-270-park — opened October 21, 2025; 60 storeys; 10,000 employees; 2.5 million sf. → §5, §5.5, §13 card.
  - https://www.fosterandpartners.com/projects/270-park-avenue — lifted ~80 ft off the ground; eight trading floors. → §5.5, §13 card.
  - https://en.wikipedia.org/wiki/270_Park_Avenue_(2025%E2%80%93present) — HQ since October 21, 2025 (confirms date; schema mention).
- Query: `Midtown South Mixed-Use Plan approved City Council 2025 Garment District homes blocks` · Firecrawl web search →
  - https://council.nyc.gov/press/2025/08/14/2940/ (Firecrawl scrape): approved August 14, 2025; "largest neighborhood, residential rezoning plan in two decades"; 9,500+ units, 2,800+ permanently affordable; >$448 million community/infrastructure; >$120 million for Garment District fashion/garment businesses. → §5, §5.5, "What the Midtown South Plan Means" section, §10.5 H3 6.
  - https://www.midtownsouthplan.nyc/ (excerpt): 42 blocks of Midtown South. → same sections.
- Query: `Garment District loft buildings 1920s built for garment manufacturing converted offices history Seventh Avenue` · Firecrawl web search → https://garmentdistrict.nyc/history (excerpt): district settled between 9th Avenue and Broadway, 34th–42nd Street; Co-Operative Garment Center Buildings at 494 and 500 Seventh Ave built 1920; fastest-growing construction site by 1926; Ely Jacques Kahn designed ten district buildings, first the Arsenal Building on Seventh Ave at 35th. → §7 Garment card, District section, §13 card.
- Query: `Diamond District West 47th Street between Fifth and Sixth Avenues number of businesses jewelry` · Firecrawl web search → https://en.wikipedia.org/wiki/47th_Street_(Manhattan) (excerpt): Diamond District between Fifth and Sixth Avenues ("Diamond Jewelry Way"). → §8 card, §9 vault question, §13 card. (A jeweller's blog claim of "over 2,600 businesses" was NOT used — weak source.)
- Query: `Grand Central Madison LIRR terminal opened January 2023` · Firecrawl → https://www.mta.info/press-release/icymi-governor-hochul-celebrates-grand-central-madisons-inaugural-year — opened to the public January 25, 2023. → §13 card.

### Codes / rules used for Q&A
- Query: `NYC Building Code interior exit stairway penetrations prohibited except equipment serving the stairway 1023.5` · Firecrawl → https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-174119 (excerpt): "Penetrations into or through interior exit stairways and ramps are prohibited except for equipment and ductwork necessary for independent ventilation or…". → §8.5 callout, §9 fire-stair question.
- Query: `FDNY auxiliary radio communication system ARCS required high-rise building fire code section 510 in-building` · Firecrawl → https://nyc-business.nyc.gov/nycbusiness/description/auxiliary-radio-communication-system-application (scrape summary): ARCS for FDNY use; required in all new high-rise buildings and those undergoing major changes per BC 403.4.4 and 907.2.13.2; licensed design professional; $585 fee (fee not used). → §9 ARCS/DAS question.
- Query: `Local Law 26 of 2004 sprinklers office buildings 100 feet or higher deadline July 2019 NYC` · Firecrawl → https://www.nyc.gov/assets/buildings/pdf/ll26of2004_reminder.pdf (excerpt): full sprinklers in office buildings over 100 ft, completed by July 1, 2019. → §8.5, §9 sprinkler question.
- Query: `NFPA 13 sprinkler piping shall not be used to support nonsystem components cables` · Firecrawl → https://up.codes/s/support-of-non-system-components (excerpt: non-system components must not be supported by sprinkler piping or hangers); https://www.fhca.org/focusonflorida/entry/cabling_on_sprinkler_piping (NFPA 25 5.2.2.2 wording). → §8.5, §9 sprinkler question.
- Query: `Times Square zoning signage requirement Special Midtown District illuminated signs minimum LUTS` · Firecrawl → https://zr.planning.nyc.gov/article-viii/chapter-1/81-732 and https://zr.planning.nyc.gov/article-viii/chapter-1 (excerpts): Special Times Square signage requirements in the Theater Subdistrict; illuminated signs required on Seventh Ave/Broadway frontages; "All required illuminated signs shall at a minimum remain lit from dusk until 1:00 a.m. daily." → §9 Times Square question, District section.
- Query: `Landmarks Preservation Commission Broadway theater interiors designated 1987 number of theaters` · Firecrawl → https://www.nypap.org/preservation-history/theater-district/ (excerpt: "By 1987, 25 Broadway theaters had been designated New York City Landmarks"); http://s-media.nyc.gov/agencies/lpc/lp/1343.pdf (excerpt: Imperial Theater first-floor interior, designated November 17, 1987); https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCrules/0-0-0-90685 (scrape summary of RCNY LPC § 4-01: production-related work on designated theatre interiors needs no application if guidelines followed and reversible; permanent alterations go to LPC). → §8.5, §9 theatre question, §13 card.
- NEC listing hierarchy (OFNP may substitute for OFNR): silo source cablinginstall.com → §8.5 callout.

### Steam / street infrastructure
- Query: `Con Edison steam system Manhattan miles of mains buildings served 2007 Lexington Avenue 41st Street steam pipe explosion` · Firecrawl →
  - https://en.wikipedia.org/wiki/2007_New_York_City_steam_explosion (excerpt): July 18, 2007; 24-inch steam pipe installed 1924; 41st St and Lexington Ave near Grand Central. → §5.5, §9 steam question, §13 Chrysler/Lexington card.
- Query: `Con Edison steam system customers Manhattan miles of pipe coned.com steam operations` · Firecrawl → https://www.coned.com/en/commercial-industrial/steam (excerpt: southern tip of Manhattan to 96th Street); https://www.coned.com/en/about-us/media-center/news/2022/03-23/con-edisons-steam-system-will-become-nycs-hottest-new-clean-energy-solution (excerpt: 105 miles of steam mains, six generating stations). → §5.5, §9 steam question.
- Query: `congestion pricing began January 5 2025 Manhattan below 60th Street toll trucks` · Firecrawl → https://portal.311.nyc.gov/article/?kanumber=KA-03612 (excerpt: toll for vehicles entering Manhattan south of and including 60 Street); https://en.wikipedia.org/wiki/Congestion_pricing_in_New_York_City (began January 5, 2025). → District section (Sixth Avenue para: deliveries consolidated). No pricing consequence stated.

### Local news / hyperlocal on Midtown fiber-installation contractors 2026 — EMPTY (none retrieved).

### Pricing used (published lines from fiber-optic-installation-manhattan.html only — no new prices)
$44/termination · $50/strand OTDR · $453 MM drop · $517 SM drop · $5,625–$8,750 12-strand OM4 backbone · $10,000–$18,750+ 24-strand OS2 · from $3,000 second telecom room · $195/hr 3-hr min ($585). Worked examples are sums only: Starter $828 = 12×$44 + 6×$50; Standard $6,225–$9,350 = OM4 backbone + 12×$50; Premium $13,000–$21,750+ = OS2 backbone + second room; sign link 2×$517 = $1,034; re-terminate 24-strand both ends + trace = 48×$44 + 24×$50 = $3,312.

### Images (11) — Step C (Drive folder `AESS Website Photos/Fiber Optic Installation` empty this run, CompanyCam not connected)
Copied from images/fiber-optic-installation/ (each a single-use file in that folder; 10 are the face-free crops first used on the Putnam page, 1 is a new crop of fiber-optic-installation-long-island-scissor-lift-ceiling-access.webp cut to 800×600 to remove the technician's face and the printed phone number): midtown-rack-yellow-uplinks-ups, midtown-corridor-bundle-open-ceiling, midtown-switch-seated-in-rack, midtown-emt-sweep-block-wall, midtown-hammer-drill-dust-extraction, midtown-jhooks-above-ceiling-grid, midtown-tone-probe-trace, midtown-patch-panel-punchdown, midtown-certifier-pass-outlet, midtown-ceiling-access-point-tile, midtown-patch-cord-label. Alt/title/caption describe only what is visible (mostly copper Cat6 panels, racks, conduit, J-hooks); no building, customer or project claimed. Candidates skipped for readable faces: westchester two-tech corridor pull, staten-island corridor bundle, staten-island link tester, orange finished rack, orange J-hook, rockland reel boxes, westchester port labels, staten-island block-wall conduit, rockland switch, rockland punchdown, hudson-valley access point; suffolk video wall skipped (shows a Lower Manhattan skyline on screen).
REVIEW: several library photos show tell-tale rendering artefacts (garbled patch-panel numbering such as "1 12 13 4 16 12 8", box text "H50 MHz", logo variations) — Anwar should confirm these are real AESS photos.

### Keyword plan (Midtown page)
Service: fiber optic installation Midtown Manhattan, tower riser backbone, fusion splicing, OTDR. Problem: elevator-bank change, mechanical floor, setback offset, full sleeve, sprinkler-pipe support, steam heat, sign uptime. Technology: OS2, OM4/OM5, bend-insensitive, armoured, high-count distribution cable, MPO. Industry: banks/trading floors, law firms, theatres, Times Square signage, jewellers, missions, Garment showrooms, condo towers. Geographic: Midtown, East Midtown, Grand Central, Plaza District, Sixth Avenue, Rockefeller Center, Times Square, Theater District, Diamond District, Garment District, Penn Plaza, Turtle Bay, Murray Hill, Koreatown, Hell's Kitchen.

### Question register additions (fiber-optic-installation-midtown-manhattan-ny)
§9 Questions Answered:
- Our floors are served by a different elevator bank from the building's telecom room, with a mechanical floor in between — what route does fiber take?
- The riser closets in our pre-war tower stop lining up above the setback floors — how does a backbone jog sideways to stay in a shaft?
- Can a backbone run up a fire stair when the riser closets are full?
- Can cable be hung from the sprinkler pipes that Local Law 26 added above our office ceiling?
- What should we check about a brand-new Midtown tower's telecom rooms before our fit-out drawings are final?
- The building's FDNY radio system or a carrier's in-building cellular system needs fiber to every floor — can that share our backbone?
- Two tenants on our stack want the last spare sleeve — how do buildings decide, and how do we avoid losing out?
- Does a trading floor need its fiber routed for low latency, or is that a myth inside one building?
- Our building's freight elevator is out of service for modernisation this year — can a riser job still go ahead?
- Our Times Square frontage has to keep its signs lit — can fiber feed the sign controllers and media players from the building's network room?
- Can fiber be installed in a Broadway theatre without disturbing a landmarked interior?
- Our jewellery business on 47th Street keeps its stock in a vault room — how does fiber reach the back office without creating a new way in?
- Con Edison steam enters our cellar right beside the telecom entrance — will the heat harm fiber, and how far away should it run?
- Riser cable or distribution cable: which suits a Midtown tower? (§10 EQUIPMENT table heading)
- Fiber Down Between Two Midtown Floors? (repair capture heading)
- Want the Transfer Floor Found Before Pricing? (mid-page CTA heading)
- Midtown Backbone Dark Before the Morning Rush? (final repair heading)
§17 FAQ:
- Does your Midtown coverage include Turtle Bay, Murray Hill, Koreatown and Hell's Kitchen as well as the office core?
- How is a long vertical fiber run supported so it does not hang on its own weight over dozens of floors?
- Do we need OM5 multimode for a new Midtown fit-out?
- Is bend-insensitive single-mode worth paying for in shallow Midtown closets?
- Can private fiber link the rooms of a full-floor condominium in a 57th Street residential tower?
- Do you work inside Grand Central or other transit-owned property?
- Does the building's chief engineer have to be with you for the whole job?
- Can our suite get a fiber path with no splice points or patch panels in any shared closet?
- Is armoured fiber required in a Midtown riser?
- Can the backbone go in before the landlord finishes its base-building work on our floor?
## Stapleton, Staten Island — local research (2026-10-17 batch, fiber-optic-installation-stapleton-staten-island-ny)

Neighbourhood page under /fiber-optic-installation-staten-island (Brooklyn GBP #brooklyn, 1282 Troy Ave; phone (347) 934-8335). Format per v2.3 §12.4: exact query · platform · URL · finding · page section used. Silo-wide and Staten Island borough sources are reused only where noted.

**Thesis:** Stapleton stacks three building generations inside a ten-minute walk — 1830s–1930 hillside houses (St. Paul's Avenue–Stapleton Heights HD), two-to-four-storey stores-with-apartments around Tappen Park on Bay/Canal/Water Streets, and post-2016 waterfront rentals plus 2019-rezoning mid-rises with required ground-floor retail — on a slope that runs down to a waterfront Sandy flooded. So Stapleton fiber is vertical and inside-out: get the line from a low, sometimes wet cellar entry to the first dry floor unspliced, run small risers through single stair halls, and secure building pathways in store ceilings before fit-outs close them. (Borough page = lot-to-lot outdoor links/aerial vs buried; St. George sibling expected civic/ferry; Bloomfield sibling expected West Shore industrial.)

### Reddit (local)
- Query: `reddit statenisland Stapleton internet Fios Spectrum apartment Bay Street` · Firecrawl search (excerpts only; reddit not scraped):
  - https://www.reddit.com/r/statenisland/comments/1gnpbct/1st_building_completed_since_the_bay_street/ — title "1st building completed since the Bay Street Rezoning" (excerpt only, building not identified) → background for §8 rezoned-Bay-Street card; not quoted.
  - https://www.reddit.com/r/statenisland/comments/1glwm5e/spectrum/ — "my Fios service is pretty awful" (excerpt, not Stapleton-specific) → not used.
- Stapleton-specific resident threads on in-building wiring: EMPTY.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitutes for §10.5 (all new claims, none used on the borough page):
- Query: `cost to run fiber optic cable to a retail store or small business building per drop` · Firecrawl search (excerpts):
  - https://unio.digital/blog/fiber-optic-installation-cost — "Fiber optic installation costs $1 to $6 per foot and $300 to $800 per drop for commercial buildings." → §10.5 H3 1.
  - https://www.clawcomm.com/fiber-optic-installation-cost-in-the-bay-area-what-commercial-projects-actually-pay-and-what-impacts-price — "For a small office build-out under 5,000 square feet, budget at least $10,000–$15,000." → §10.5 H3 2.
  - https://tssusa.net/blog/commercial-data-cabling/ — "Eyewear retail rollout (36 Cat6 drops per store): $8K–$12K per location" → §10.5 H3 7.
- Query: `fiber optic cable lifespan years fragile myth bend installation small business` · Firecrawl search:
  - https://www.lindenphotonics.com/debunking-common-myths-about-fiber-optic-cables — "Fiber optic installation is straightforward and efficient"; most providers offer professional installation; bend-insensitive fibers "allow the cable to bend around corners or fit into tight spaces without causing signal loss or damage" (article also says bend radius should not be exceeded) → §10.5 H3 3 and 4.
  - https://www.facebook.com/Cailabs/videos/myth-the-lifespan-of-fiber-optic-cables-is-10-to-25-years-false-the-lifespan-of-/393152399604171/ — "can exceed 150 years" (excerpt) → §10.5 H3 5.
  - https://www.quora.com/What-is-the-lifespan-of-fiber-optic-cable-when-laid-in-the-ground — "typically around 20-25 years" (excerpt) → §10.5 H3 5.
- Query: `fiber internet installation how long does it take mixed-use building landlord permission tenant` · Firecrawl search:
  - https://fcconnexion.com/upgrade-your-rental-to-fiber-internet-in-fort-collins-colorado/ — "The total timeline is typically 2–4 weeks from sign-up to activation"; "Does fiber installation damage the property? No." (excerpt) → §10.5 H3 6.

### Neighbourhood facts, streets, landmarks
- Query: `Urby Staten Island Stapleton former Navy homeport units opened Front Street` · WebSearch → https://en.wikipedia.org/wiki/Stapleton,_Staten_Island (WebFetch): bounds Tompkinsville at Grant St, Clifton at Vanderbilt Ave, west St. Paul's Ave/Van Duzer St (Grymes Hill); ZIP 10304; laid out 1830s by William J. Staples and Minthorne Tompkins; German breweries (last closed 1963); Seaman's Retreat 1832 (later Bayley Seton); incorporated as village of Edgewater 1884; SIR stop 1884; Navy homeport selected 1983, cancelled 1993; Urby opened 2016; Sandy (Oct 29 2012) threw tanker John B. Caddell onto Front St; 132 Canal St Carnegie library (1907, renovated 2011–13); NTA SI0102 2020 pop 19,027 (+17.5% from 16,192), 71.2% renter-occupied. → §5 paras 1/4, §5.5 (renter share, growth), §13 cards, block-by-block bounds, FAQ 1.
- Same search → https://edc.nyc/project/new-stapleton-waterfront (WebFetch): 35-acre stretch; Phase 1 (Ironstate, fall 2011) opened 2016 with six-acre park; "nearly $200 million" public improvements; bioswales, tidal wetlands cove; esplanade; Bay Street Corridor rezoning approved 2019. → §5.5, §13 waterfront card, flood section.
- Same search → https://www.fieldcondition.com/blog/2016/8/23/urby-staten-island (WebFetch): two buildings, "four and five story", 571 apartments, 115 affordable, Ironstate, completed 2016. → §5 para 3, §5.5, §7 card.
- Query: `St. Paul's Avenue–Stapleton Heights Historic District designated Landmarks Preservation Commission` · WebSearch → https://6tocelebrate.org/site/st-pauls-avenue-stapleton-heights-historic-district/ (WebFetch): designated 2004; 92 freestanding houses; St. Paul's, Cebra, Marion Aves, Beach St; mid-1830s Greek Revival to 1906–1930 (about a third); styles Italianate, Second Empire, Queen Anne, Shingle, Colonial Revival; St. Paul's Memorial Church 1866–70. → §5.5, §7 card, §8.5, §13 card, historic-interiors section, block-by-block.
- Query: `Tappen Park Stapleton Staten Island village hall Edgewater Hall history` · WebSearch → https://en.wikipedia.org/wiki/Edgewater_Village_Hall_and_Tappen_Park (WebFetch): built 1889, Paul Kuhne, Romanesque Revival; bounded by Wright, Water, Bay and Canal Sts; NRHP May 19 1980. → §5 para 1, §13 card, schema mentions.
- Query: `Stapleton Houses NYCHA Staten Island buildings apartments completed` · WebSearch → https://en.wikipedia.org/wiki/Stapleton_Houses (WebFetch): six buildings, eight storeys, 693 units, 16.87 acres, completed May 31 1962; Tompkins Ave, Broad, Hill, Warren, Gordon Sts. → §5.5, §7 card, §13 card. https://www.nyc.gov/site/nycha/about/pact/stapleton.page (WebFetch): selected for PACT/RAD, first resident meeting Oct 20 2025; no unit count or timeline. → §5.5, §13.
- Query: `Stapleton Staten Island Railway station Prospect Street ...` · WebSearch → https://en.wikipedia.org/wiki/Stapleton_station (WebFetch): Bay St & Prospect St; opened July 31 1884; elevated; rebuilt 1936 grade-crossing elimination; exits Prospect St and Water/Bay Sts. → §13 card.
- Query: `John B. Caddell tanker Front Street Stapleton Sandy storm surge` · WebSearch → https://en.wikipedia.org/wiki/John_B._Caddell (WebFetch): 184.6 ft, driven onto Front Street, Stapleton, Oct 29 2012. → hero subhead, §5 para 4, flood section.
- Query: `Stapleton Staten Island flood zone Bay Street Front Street Hurricane Sandy flooding waterfront` · WebSearch → https://www.dnainfo.com/new-york/20160502/stapleton/35m-waterfront-park-opens-stapleton (WebFetch): $35M, 6-acre park, bioswales and drainage to reduce neighbourhood flooding; on former Navy Homeport; next to Urby on Front St. → §5 para 4, flood section.
- Query: `North Shore Action Plan Staten Island 2023 ...` · WebSearch → https://www.6sqft.com/nyc-releases-staten-island-north-shore-revitalization-plan-for-waterfront-access-and-housing/ (WebFetch): Sept 2023, $400M, 2,400 units, two-mile esplanade St. George–Stapleton by 2027. → background only (esplanade "under construction" wording); figures not quoted.

### Bay Street Corridor rezoning / new buildings
- Query: `Bay Street Corridor rezoning Stapleton Tompkinsville Canal Street Van Duzer Street mixed-use special district` · WebSearch → https://citylandnyc.org/major-staten-island-project-approved-by-city-planning-despite-significant-opposition-city-council-up-next (WebFetch): ~20 blocks / ~45 acres; 14 blocks of Bay St, two of Canal St; Special Bay Street Corridor District; Bay St was M1-1 (no residential); R6/C2-3, C2-4, R6B on Van Duzer; "required non-residential uses on ground floors within 50 feet of Bay Street"; ground-floor commercial optional on parts of Van Duzer St; some sites 12 storeys. Council approval June 26 2019 (citylimits, silo source). → §5 para 3, §5.5, §8 cards, fit-out section, block-by-block.
- Same search → https://commercialobserver.com/2019/04/the-bay-street-rezoning-could-be-a-boon-to-the-area-or-a-migraine-for-residents (WebFetch): "half-mile stretch"; empty lots, auto shops, gas stations; buildings mainly one to four storeys; 475 Bay St BFC plan 214 units. → fit-out section para 1.
- Same search → https://www.nyc.gov/assets/planning/download/pdf/applicants/env-review/bay-street-corridor/00-feis.pdf (WebFetch): Stapleton town center uses "generally mixed‐use developments with ground floor retail and residential uses above". → §8 Bay Street card. Floodplain text: EMPTY in this excerpt. Appendix C (block/lot list) has no flood text: EMPTY.
- Query: `silive Stapleton Bay Street new building apartments retail 2025 construction` · WebSearch → https://blog.marketproof.com/new-building-permit-filed-for-541-bay-st-in-stapleton-staten-island/ (WebFetch): seven storeys, 92 units, ~6,589 sq ft commercial, filed June 2, 2025. https://blog.marketproof.com/new-building-permit-filed-for-490-bay-st-in-stapleton-staten-island/ (WebFetch): five storeys, 26 units, filed June 12, 2026. → §5 para 3. (https://www.pincusco.com/... 274-unit BFC filing, paywalled, address not stated → not used.)

### Flood / code
- Query: `NYC Building Code Appendix G flood-resistant construction utilities equipment above design flood elevation` · WebSearch → https://www.nyc.gov/assets/buildings/pdf/presentations/bsls22-flood_resistant_construction.pdf (WebFetch): flood hazard area = 1-percent-or-greater annual chance; installing new equipment below the design flood elevation where not previously present treated as increase in noncompliance (alterations). → §8.5 callout, flood section, building-terms list.
- Stapleton lot-level FEMA/PFIRM zone status: EMPTY (no source retrieved; page tells owners to check the city flood map rather than asserting a zone).

### Carriers / local news
- Query: `Stapleton Staten Island 10304 fiber internet providers Verizon Fios availability` · WebSearch → only national ISP-listing sites, several for other "Stapleton"s; nothing Stapleton-NY-specific usable. EMPTY. Page relies on borough research (Verizon "virtually all" SI premises passed, Spectrum advertising) only as "Fios and cable service reach Bay Street" — FLAG: general, not address-verified.
- SI Advance / silive articles on Stapleton fiber or cabling contractors: EMPTY (none retrieved).
- Yelp 1–3★ Stapleton cabling contractors: EMPTY.

### Pricing used (copied exactly from fiber-optic-installation-staten-island.html; no new prices)
$39 termination; $44 OTDR/strand; $385 MM drop; $440 SM drop; $4,950–$7,700 12-strand OM4; $8,800–$16,500+ 24-strand OS2/building-to-building; from $2,640 second telecom room; $195/hr 3-hr min ($585). Packages: Starter $880 (2 × $440), Standard $4,950–$7,700, Premium $8,800–$16,500+; BYOE labour $195/hr, 3-hr min.

### Images (11) — permanent image rule; Drive folder empty (checked by main run), CompanyCam not connected
Copied to images/fiber-optic-installation/ as WebP q80. Printed phone numbers on shirts/caps/van side and the van's web address were pixelated + blurred; the floor-plan sheet in the patch-panel photo was blurred; the lobby photo was cropped to remove the building directory sign ("123 Main Street", apartment list). Sources chosen by perceptual hash as least-used in the fiber silo (most 0–2 prior fiber uses). Faces are visible (profile or partial) in most — the library has almost no face-free photos; flagged.
| New file | Source |
|---|---|
| fiber-optic-installation-stapleton-fusion-splicer-rack.webp | low-voltage/low-voltage-installation-brooklyn-fiber-fusion-splice.jpg |
| fiber-optic-installation-stapleton-block-wall-core-drill.webp | network/network-installation-nyc-core-drill-conduit-rough-in.webp |
| fiber-optic-installation-stapleton-stud-wall-patch-panel.webp | low-voltage/low-voltage-installation-bronx-idf-patch-panel-build.jpg |
| fiber-optic-installation-stapleton-wall-plate-tone-trace.webp | low-voltage/low-voltage-installation-dutchess-county-08-tone-generator-trace.jpg |
| fiber-optic-installation-stapleton-scissor-lift-access-point.webp | low-voltage/low-voltage-installation-bronx-access-point-lift-install.jpg |
| fiber-optic-installation-stapleton-van-cable-reels.webp | low-voltage/low-voltage-installation-brooklyn-van-load-out.jpg |
| fiber-optic-installation-stapleton-lobby-entry-panel.webp | low-voltage/low-voltage-installation-long-island-lobby-video-intercom.jpg (cropped) |
| fiber-optic-installation-stapleton-rack-laptop-config.webp | low-voltage/low-voltage-installation-dutchess-county-hero-rack-switch-config.jpg |
| fiber-optic-installation-stapleton-gutted-floor-cable-staging.webp | network/network-installation-bronx-cat6-cable-box-staging-fitout.webp |
| fiber-optic-installation-stapleton-entrance-intercom-wiring.webp | low-voltage/low-voltage-installation-bronx-11-video-intercom-entry-wiring.jpg |
| fiber-optic-installation-stapleton-storefront-door-maglock.webp | low-voltage/low-voltage-installation-long-island-maglock-install.jpg |

### Keyword plan (Stapleton page)
Service: fiber optic installation Stapleton, fiber riser, storefront fiber fit-out, cellar-to-upper-floor fiber, fusion splicing, OTDR testing. Problem: wet cellar entry, store ceiling closing over building cables, services through neighbour's cellar, facade cable clutter, vanilla-box retail units, historic plaster, balloon framing, retaining walls, neighbour excavation, weak indoor cell signal, POTS alarm dialers. Technology: OS2, OM4, riser/plenum ratings, indoor/outdoor water-blocked cable, sealed sleeves, listed firestop, media converters/SFP. Industry: storefront retail, restaurants, mixed-use landlords, new rental buildings, churches/halls, NYCHA-area community organisations. Geographic: Stapleton, Stapleton Heights, Tappen Park, Bay St, Canal St, Water St, Wright St, Front St, Van Duzer St, Tompkins Ave, Broad St, St. Paul's Ave, Cebra Ave, Marion Ave, Beach St, Grant St, Vanderbilt Ave, Tompkinsville, Clifton, Grymes Hill, Rosebank, St. George.

### Question register additions — fiber-optic-installation-stapleton-staten-island-ny
§9 Questions Answered:
- The tenant fitting out our ground-floor store wants to close the ceiling — what should be left in it for the floors above?
- Can the fiber come into our storefront through the header above the roll-down gate instead of through the cellar?
- Our retail unit was handed over as a vanilla box with only an empty sleeve to the building's telecom room — what do we still need?
- Our building's phone and cable lines arrive through the cellar of the building next door — can our new fiber get its own way in?
- A new mid-rise is going up next door — how do we protect our fiber entrance while they excavate?
- Our lot is slated for redevelopment in a few years — can fiber installed now be recovered and reused?
- Does the old balloon framing in our house make a cellar-to-attic fiber run easier, and does the cavity need fire-blocking afterwards?
- A stone retaining wall separates our house from the garage below it — can fiber get through or over the wall without weakening it?
- Cell signal is weak inside our new concrete building — can fiber help bring coverage indoors?
§17 FAQ:
- Do you work up in Stapleton Heights and out to the Clifton and Tompkinsville edges, or only near Bay Street?
- How much dust and noise does a core-drilled entrance make inside an open shop?
- Could drilling or cutting set off our building's smoke detectors?
- Can a fiber link serve the network connection for electric-vehicle chargers in our lot or garage?
- Does fiber cable add fire load inside the walls of a wood-frame house?
- Do we see the test results before the final payment is due?
- Can fiber feed a digital menu or sign screen in the shop window?
- Our alarm still dials out over an old phone line — will it keep working once the building moves to fiber?

De-dup notes: checked by meaning against all 16 fiber pages' questions (401 headings/FAQ). Dropped before drafting: historic-district/Landmarks entry (≈ Manhattan "landmarked or historic-district building"), cellar main-room-in-flood (≈ Manhattan), flood-damaged fiber (≈ Brooklyn underwater), reach second floor without passing through shop (≈ Orange), party wall (≈ Orange/Nassau), per-tenant provider holes (≈ Orange/Queens), mixed-use backbone keeping store and apartments apart (≈ Queens), elevated-train (≈ Queens), rack location (≈ Bronx/Orange), warranty (≈ SI/Queens), COI (≈ Queens), nights/weekends (≈ NYC hub). Closest remaining intents for the main run to judge: "vanilla box sleeve" vs Long Island "vacant office building near Route 110 — what fiber before move-in" (unit-level tenant fit-out vs whole-building move-in); "redevelopment — recover fiber" vs Orange "worth adding to a building we might sell" (salvage vs resale value); "test results before final payment" vs NYC hub "how do you prove a new link is good" (payment timing vs test method). Masked paragraph similarity (word-level difflib, ≥12-word body paragraphs, exempt warranty/licence/consent/NAP/stamp and shared nav) below 0.63 after rewrites (was 0.807 vs SI borough "who does what" paragraph; process step 4 rewritten from 0.632).

## Downtown Brooklyn, Brooklyn — local research (2026-10-17 batch, fiber-optic-installation-downtown-brooklyn-ny)
Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources and the Brooklyn section are reused where noted. Thesis: Downtown Brooklyn is the borough's vertical exception — fiber climbs towers and crosses ownership lines (retail podium / commercial unit / condo or rental floors / schools) inside one building, so the job is governed by who controls each riser and closet, not distance.

### Reddit (local) — excerpts only (reddit.com not scrapable)
- Query: `reddit Downtown Brooklyn apartment building internet options Fios not available new tower` · Firecrawl search → https://www.reddit.com/r/Brooklyn/comments/13w39r3/moving_apartments_and_choosing_new_internet/ (excerpt: "Verizon not … hooked up in the building to continue with FiOS") → §5. Same query → https://www.verizon.com/home/internet/near-me/new-york-ny/ (FAQ: in buildings "not yet wired for Fios: Verizon coordinates with the property manager/owner to wire and install the service") → §5, §10.5 H3 5.
- Query: `reddit Downtown Brooklyn building only one internet provider exclusive Spectrum luxury rental bulk` · Firecrawl search → https://www.reddit.com/r/nyc/comments/qxk36v/ (excerpt: "A lot of buildings and neighborhoods in NYC only have one option for internet") → §5; https://www.reddit.com/r/AskNYC/comments/go1pjg/ (excerpt: "There are buildings with exclusive contracts … Legal AFAIK, tons of buildings in NYC do that." — commenter opinion, corrected with silo HPD/FCC source) → §10.5 H3 3; https://www.reddit.com/r/Apartmentliving/comments/1f6og70/ (bulk-billing excerpt) → §9 bulk-internet Q context only.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitute §10.5 claims (quoted as published): lowvoltagenewyork.com ("$7–$12" per foot finished walls/packed risers — silo source); https://www.broadbandsearch.net/service/new-york/brooklyn (Sep 2026 excerpt: fiber "concentrated in DUMBO, Williamsburg and Downtown Brooklyn"); r/AskNYC exclusive-contract comment; quantumfiber multifamily stages (silo source); verizon.com FAQ (above); atlantech 15-month wait (silo source); https://cooperatornews.com/article/get-a-little-fiber-in-your-diet (Firecrawl query scrape: Victor Cruz of Time Warner Cable: "We'll install and upgrade a building at no cost as long as it's a normal installation" — older article, presented as such). Yelp: EMPTY (not searched separately; silo Yelp search returned nothing usable).

### Landmarks, buildings, corridors
- `Brooklyn Tower 9 DeKalb Avenue height stories Dime Savings Bank tallest Brooklyn` · Firecrawl → https://www.shoparc.com/projects/9-dekalb/ (1,066 ft, tallest in borough); https://en.wikipedia.org/wiki/Brooklyn_Tower (first supertall in Brooklyn) → §5.5, §7, §13.
- `MetroTech Center Downtown Brooklyn office campus acres buildings history` · Firecrawl → https://www.6sqft.com/with-50m-redevelopment-metrotech-center-will-become-brooklyn-commons/ (scrape, Feb 8 2022: rebrand to Brooklyn Commons, $50M, 1/2/15 MetroTech renovations, 3.6-acre park, 16-acre 12-building property built in 1980s as office park for data-processing centres and financial back offices, near 13 subway lines, tenants NYU Tandon, Slate Media, JPMorgan Chase). Same page's related items: Brooklyn Tower 93 storeys, condos from 53rd floor (Mar 2022), relaunch as 85 Fleet Street (Jun 2025), Silverstein takeover $672M (Jul 2024), pools around Dime Savings Bank dome; 100 Flatbush 44 storeys, NYC's first all-electric skyscraper, Alloy Block 850 apts/200,000 sf office/two public schools (Jan 2023); The Brook 589 Fulton 600 ft/591 apts; One Boerum Place 22 storeys/138 rentals; BKX at 422 Fulton, 440,000 sf, five floors, "largest block of retail space available in NYC" (Jul 2026); Macy's 422 Fulton sold for $23M (Jan 2025). https://therealdeal.com/new-york/2022/09/14/nyu-buys-3-metrotech-center-office-building-for-122m/ (excerpt: NYU bought 3 MetroTech $122M). → §5.5, §7, §8, §13, Vertical Work, Block by Block, Conversions, Retail Podiums, Institutions.
- `Downtown Brooklyn office to residential conversion 2025 2026 Court Street Montague building` + `Brooklyn office tower completed 2023 never leased $208 million loan…` · Firecrawl → https://www.multihousingnews.com/capstone-bh3-obtain-208m-for-rare-office-to-residential-project-in-brooklyn/ (141 Willoughby: 24 storeys, 355,000 sf, 239 apts floors 8–23, floors 1–7 commercial); https://finance.yahoo.com/real-estate/articles/northwind-group-provides-208-million-140000640.html (delivered 2023, never occupied, Class A spec, commercial rebranded 385 Gold) → §5, §5.5, §7, §8, §13, Conversions, SVG 6.
- `Borough Hall Skyscraper Historic District designated…` · Firecrawl → https://www.citylandnyc.org/borough-hall-skyscraper-historic-district-approved/ (scrape: LPC approved Sept 13 2011; 21 buildings on Court/Montague/Remsen/Joralemon/Livingston; Borough Hall, Temple Bar Building, 32 Court St "Brooklyn's first true skyscraper"; became Brooklyn's commercial core); https://www.nyc.gov/assets/lpc/newsletters/may-2017.html (181 Montague and 185 Montague designated) → §5, §5.5, §7, §8.5, §13, Block by Block.
- `Brooklyn Paper Downtown Brooklyn 2026 construction tower Livingston Street…` · Firecrawl → https://en.wikipedia.org/wiki/List_of_tallest_buildings_in_Brooklyn (75 Livingston 1926, 32 floors, office converted to co-op 1981; 111 Livingston 1969, 22 floors mixed office/residential); https://www.brooklynpaper.com/proposed-downtown-brooklyn-tower-blocks-views-landmark-row/ (Duffield St tower 323 ft, healthcare facility in cellar/1st/2nd floors); https://brooklyneagle.com/58635/downtown-brooklyn-construction-checklist/ (333 Schermerhorn 610 ft) → §7, §8, Block by Block, Conversions, Institutions.
- `City Point Brooklyn Albee Square Dekalb Market Hall…` · Firecrawl → https://en.wikipedia.org/wiki/City_Point_(Brooklyn) (summary: three towers 2015–2020, largest mixed-use project in city by sq ft, City Point III 720 ft second tallest in Brooklyn, Target, Trader Joe's); https://www.citypointbrooklyn.com/ (445 Albee Square West; DeKalb Market Hall, Alamo Drafthouse) → §7, §8, §13.
- `NYU Tandon City Tech Brooklyn Tech Triangle…` · Firecrawl → https://brooklyntechtriangle.com/57000-students-8-colleges-and-universities-1-tech-triangle/ (57,000 students, 8 colleges); https://en.wikipedia.org/wiki/New_York_City_College_of_Technology (seven buildings in Tech Triangle, 14,000+ students) → §5.5, Block by Block, Institutions.
- Silo Brooklyn source reused: Downtown Brooklyn Partnership storymap (32M+ sf, 144 projects since 2004; 1 Willoughby Square first new office tower) → §5, Block by Block.

### Local news / hyperlocal / data
- `Fulton Mall Downtown Brooklyn history pedestrian shopping street…` · Firecrawl → https://therealdeal.com/new-york/2026/10/06/fulton-mall-proposed-for-downtown-brooklyn-mega-bid/ (excerpt, Oct 6 2026: DBP proposes mega-BID merging Fulton with MetroTech, Court-Livingston-Schermerhorn; 25,000+ housing units since 2004 rezoning; retail vacancy ~22% vs 11% citywide; 212 chain stores; upper floors of many Fulton Mall storefronts underutilized; Restler quote "one of the most successful commercial corridors"); https://prattcenter.net/our_work/fulton_street_mall_new_strategies_for_preservation_and_planning (late-19th/early-20th-c department-store buildings, upstairs vacant) → §5, §5.5, §8, Block by Block, Retail Podiums.
- `Downtown Brooklyn Partnership office vacancy 2025 2026 report` · Firecrawl → DBP Q1/Q2 2026 market report pages scraped: Issuu embed only, no figures retrievable = EMPTY (not accessible in build env). Colliers Q1 2026 Brooklyn excerpt not used.
- `Downtown Brooklyn Partnership free public WiFi…` · Firecrawl → technical.ly Fulton Mall Wi-Fi, Brooklyn Eagle LinkNYC items — found, not used.
- `Brooklyn Fiber OR "Downtown Brooklyn" fiber internet provider…` · Firecrawl → https://bkfiber.com/buildings/310-livingston-st (The Guild listed as served) — recorded, not used on page.

### Local licensing / permits / codes
- `FDNY auxiliary radio communication system ARCS required high-rise…` · Firecrawl → https://nyc-business.nyc.gov/nycbusiness/description/auxiliary-radio-communication-system-application (BC §403.4.4, §907.2.13.2: ARCS required in all newly built high-rises and existing buildings with major changes) → §8.5, §9 ARCS Q, glossary, SVG 1.
- `post-tensioned concrete slab coring scanning tendons GPR…` · Firecrawl → https://www.penhall.com/post-tension-vs-rebar/ (GPR "the only reliable method" to confirm PT cable location; typical 24–48 in spacing); https://www.reddit.com/r/StructuralEngineering/comments/13xzm1i/ (excerpt: scan and get engineer approval) → §8.5, §9 PT Q.
- Silo sources reused: HPD broadband guidance/FCC exclusivity ban; LPC exterior-only rule; site statement sub-50 V no DOB permit.

### Pricing used (Brooklyn 1.00× — copied verbatim from fiber-optic-installation-brooklyn.html; no new prices)
$35/termination; $40/strand OTDR; $350 MM drop; $400 SM drop; $4,500–$7,000 12-strand OM4; $8,000–$15,000+ 24-strand OS2; from $2,400 second telecom room; $195/hr 3-hr min ($585). Starter package $700 = 2 × $350 MM drops (arithmetic only).

### Images (11) — permanent image rule; Drive folder empty (main run 11:40Z), CompanyCam not connected
Reused from images/low-voltage/ (10) and images/network/ (1), converted to WebP, chosen for back-of-head/hands-only views with no readable phone numbers: lv nyc-02-ceiling-grid-bundle-pull → tower-floor-ceiling-bundle-pull (eager); lv nyc-01-crew-ceiling-cable-pull → office-fitout-crew-overview; lv nyc-06-idf-rack-patching → floor-closet-rack-patching; lv nyc-05-cat6-patch-panel-punchdown → panel-punchdown-closeup; lv nyc-04-keystone-wall-plate-termination → suite-wall-outlet-termination; lv nyc-10-ceiling-access-point-drop → ceiling-access-point-mount; lv nyc-15-conference-room-display-cabling → conference-display-cabling; lv manhattan-11-video-wall-installation → video-wall-mounting; network nyc-network-rack-cleanup-before-after → closet-rebuild-before-after (same photo as Brooklyn page's telecom-closet-cleanup); lv nyc-07-fluke-certification-pass → link-certification-tester (partial side profile); lv nyc-08-storefront-camera-cabling → storefront-canopy-camera. DAILY-LOG note: images: 11 reused from images/low-voltage/ and images/network/ (no real fiber-optic-installation photos yet).

### Keyword plan (Downtown Brooklyn page)
Service: fiber optic installation Downtown Brooklyn, tower riser fiber, fiber backbone, commercial-unit fiber, OTDR testing, fusion splicing. Problem: riser access, condo board approval, post-tensioned slab coring, amenity-floor coverage, below-grade retail, bulk-internet buildings, conversions. Technology: OS2, OM4, OFNR/OFNP, innerduct, floor enclosures, OTDR. Industry: residential/condo towers, office campus, law/professional offices, retail podiums/food halls, colleges, clinics, schools in mixed-use. Geographic: Downtown Brooklyn, Fulton Mall, Court/Montague/Remsen, MetroTech/Jay St, Albee Square/Flatbush Ave Ext, Livingston/Schermerhorn/Boerum Pl, Willoughby/Gold/Duffield, Brooklyn Heights, DUMBO, Fort Greene, Boerum Hill.

## Flushing, Queens — local research (2026-10-17 batch, fiber-optic-installation-flushing-queens-ny)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources above are reused where noted; only Flushing research is added here.
Page thesis: downtown Flushing is owned in slices — office/medical condominiums, podium-and-tower complexes with retail, hotel and parking sections, indoor malls with basement food halls — so fiber is a condominium common-element decision made by a board of managers, the carrier often lands on a parking level (now in the Local Law 126 inspection window for Queens), and the route has to bypass separately owned retail. Fix: a condo-owned backbone, passive entry room below / active room above, strands labelled by unit number.

### Reddit (local)
- `site:reddit.com/r/Flushing internet Fios building` · Firecrawl search (excerpts only; reddit threads not opened).
  - https://www.reddit.com/r/Flushing/comments/1kn99t8/verizon_fios_available_on_my_street_in_north/ — excerpt: "Some coop building has contracts with optium. Some small commercial buildings are landlocked by other buildings, so Verizon doesn't care." → §5 para 3; §10.5 H3 1.
  - https://www.reddit.com/r/Flushing/comments/1spiap6/experience_with_internet_services_around_flushing/ — excerpt: "Move to a different building." (also in Queens section) → §5 para 3.
  - https://www.reddit.com/r/Flushing/comments/1gamoe7/ (new ISP excerpt, vague) — not used.
- `reddit Flushing Queens building internet only one provider landlord wiring` · Firecrawl search → only non-Flushing threads (r/Apartmentliving, r/nyc, r/Landlord). Not used.

### Forums (co-op / condo boards)
- `reddit r/flushing internet fiber building condo Fios Spectrum` · WebSearch → https://www.habitatmag.com/Board-Talk/Building-wide-internet (WebFetch; posted Dec 15 2018, comments Jan–Mar 2019): "Normally each subscriber has to find a place to put those big boxes that convert the fiber to copper."; "Spectrum will do bulk packages @ 50$ish per participating shareholder." → §10.5 H3 2 and 3.
  - Same query → community.verizon.com "impossible to get fios at new construction condominium" — redirects to Verizon support (community sunset). EMPTY (not accessible in build env).

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
§10.5 substitutes (quoted as published): Reddit and Habitat above; silo sources thenetworkinstallers.com (FBA 2025 underground median $18.00/ft, aerial $8.00/ft; fusion splice $30–$75, mechanical $15–$40 citing Ring and Ping) → H3 4, 5; HPD Broadband in Affordable Housing (broadband required in new construction; basement entry point; FCC bans exclusive / sale-leaseback) → H3 3, 6 and §9 turnover answer; Atlantech (customer waited 15 months, no fiber) → H3 7. Angi/HomeAdvisor/Fixr: none returned (silo finding).
- `Flushing Queens 2025 news broadband internet fiber small businesses Main Street` · WebSearch → no usable local news item (ISP-comparison and unrelated pages). EMPTY.

### Building stock, developments, corridors
- `Special Flushing Waterfront District rezoning approved 2021 towers Flushing Creek units` · WebSearch → https://www.6sqft.com/nyc-rezoning-flushing-waterfront-district/ (WebFetch, Dec 10 2020): Council approval; 13 towers; 29 acres; 1,725 units (up to 90 affordable); 879 hotel keys; ~400,000 sq ft office; ~287,000 sq ft retail; FWRA LLC = F&T Group, United Construction and Development Group, Young Nian Group; bounded by Van Wyck Expwy, College Point Blvd, Roosevelt Ave; new walkway and plaza. → §5 para 4, facts table, waterfront section, schema citation.
- `Tangram Flushing mixed-use towers condo hotel mall opened` · WebSearch → https://www.gmsllp.com/portfolio/tangram-two-fulton-square/ (WebFetch): Prince St & 39th Ave; 1,403,500 sq ft; four towers of 15–16 storeys; two-level retail podium; three below-grade parking levels; hotel/office/residential; F&T Group. → §7 card, garage section.
- `One Fulton Square Flushing Hyatt Place hotel retail building 39th Avenue Prince Street opened` · WebSearch → https://newyorkyimby.com/2014/08/construction-update-one-fulton-square.html (WebFetch): Roosevelt Ave & Prince St; twin 12-storey towers; 168-key Hyatt Place (opened end of May 2014); three-level glass retail podium; 43 residential condos; separate office condominium of 22 professional and medical offices; 300 parking spaces; F&T Group. → §5 para 1, facts table, §7 card, garage section, medical section.
- `Flushing Commons Main Street 39th Avenue former municipal parking lot development completed units` · WebSearch → https://newyorkyimby.com/2026/09/two-tower-second-phase-of-flushing-commons-breaks-ground-in-flushing-queens.html (WebFetch, Sept 17 2026): phase two groundbreaking Sept 16 2026 at 37-10 138th St; 156 condos; ~132,000 sq ft retail; 123,000 sq ft office; 63,000 sq ft YMCA; completion June 2029; phase one 2017 = 148 condos, 90 office condominiums, ~30,000 sq ft retail, 982 parking spaces; phase three pre-development 2027; F&T Group, NYCEDC, YMCA. → §5 paras 1 & 4, facts table, street section, garage section, FAQ phases.
- `Sky View Parc Flushing condominium towers Skyview Center mall parking units` · WebSearch → https://www.multihousingnews.com/30-percent-of-sky-view-parc-sold/ (WebFetch, Mar 25 2008): six towers, 448 condos phase 1, 800,000 sq ft retail, 14-acre site at College Point Blvd & Roosevelt Ave, Muss Development. → §7 card ("announced with 800,000 sq ft").
- `Flushing commercial condominium office units medical condo building downtown Flushing` · WebSearch → https://loopnet.ca/Listing/36-09-Main-St-Flushing-NY/35395439 (WebFetch): Main Street Tower, 36-09 Main St, 10 floors, built 1988, Class B, 33,247 sq ft, typical floor 3,324 sq ft, atrium, elevator; unit 8A 628 sq ft office/medical condo for "investment or owner-user". → §5 para 1, §7 card, medical section.
  - https://www.crexi.com/lease/properties/1209972/new-york-queens-crossing (WebFetch) — no content returned. EMPTY.
- `New World Mall Flushing food court basement stalls Main Street` · WebSearch → https://theinfatuation.com/new-york/reviews/new-world-mall-food-court (WebFetch): 136-20 Roosevelt Ave; basement food court ~30 stalls; "largest Asian indoor mall in New York City". → §7 card, landmarks card.
- `Downtown Flushing Transit Hub Business Improvement District established blocks Main Street Roosevelt` · WebSearch → flushingpost.com redirect → https://qns.com/2020/04/city-council-approves-expansion-of-the-flushing-business-improvement-district/ (WebFetch, Apr 23 2020): Council vote Apr 22 2020; budget ~$380,000 → ~$1M; old and new boundaries (Main St, 40th Rd, Roosevelt Ave, Kissena Blvd, 39th Ave; added 37th Ave, Union St, 138th St, Prince St, 38th Ave, 41st Rd, 41st Ave). → facts table, §8 corridor cards, street-by-street section.
- `Flushing–Main Street station 7 train ridership busiest outside Manhattan` · WebSearch → https://en.wikipedia.org/wiki/Flushing%E2%80%93Main_Street_station_(IRT_Flushing_Line) (WebFetch): opened Jan 21 1928; 14,592,853 riders 2024; 10th of 423; underground; 20+ bus routes; connection to LIRR Port Washington Branch. → facts table, landmarks card. (untappedcities.com 2017 "busiest outside Manhattan (2015)" fetched but not used — dated.)
- `Flushing Creek flood zone downtown Flushing Ida flooding College Point Boulevard 2021` · WebSearch → https://www.nyc.gov/assets/planning/download/pdf/plans-studies/flushing-west/032515_presentation.pdf (WebFetch, DCP, Mar 25 2015): 30+ acre brownfield opportunity area along Flushing Creek; flood zones & wetlands map; airport height limitations; possible soil contamination on nearly all lots; M1-1/M3-1 zoning. → §7 waterfront card, waterfront section.
- Ida: silo/Queens source reused — https://qns.com/2021/09/queens-storm-death-toll-rises-to-11-after-three-bodies-found-in-flooded-flushing-basement-nypd/ (10 of 11 Queens deaths in basement apartments, incl. East Flushing near Kissena Park). → street section (Kissena), waterfront section.

### Landmarks
- `Flushing Town Hall 1862 Northern Boulevard landmark history` · WebSearch → https://en.wikipedia.org/wiki/Flushing_Town_Hall (WebFetch): 137-35 Northern Blvd; 1862; Rundbogenstil; NYC Landmark July 30 1968; performing arts centre run by Flushing Council on Culture and the Arts. → §8.5 callout, landmarks card.
- `Bowne House Flushing 1661 Quaker Meeting House 1694 Northern Boulevard landmark` · WebSearch → https://en.wikipedia.org/wiki/Old_Quaker_Meeting_House_(Queens) (WebFetch): 137-16 Northern Blvd; built 1694, enlarged 1716–1719; NHL Dec 24 1967; NYC Landmark Aug 18 1970. → §8.5, landmarks card. (Bowne House date not obtained — not used.)
- `Queens Botanical Garden Main Street Flushing acres history 1939 World's Fair` · WebSearch → https://planning.org/greatplaces/spaces/2009/queensbotanicalgarden.htm (WebFetch): 39 acres; 43-50 Main St; "Gardens on Parade" at 1939 World's Fair; Visitor & Administration Building opened 2007, first LEED Platinum facility in NYC. → landmarks card.
- `NewYork-Presbyterian Queens hospital Flushing Main Street beds campus` · WebSearch → https://en.wikipedia.org/wiki/NewYork-Presbyterian_Queens (WebFetch): 56-45 Main St; 535 beds; formerly New York Hospital Queens; renamed July 1 2015. → landmarks card, medical section.

### Local licensing / permits / building rules
- `New York Real Property Law 339-e common elements definition condominium board of managers` · WebSearch → https://www.nysenate.gov/legislation/laws/RPP/339-E (WebFetch): common elements (unless declaration provides otherwise) include basements, cellars, yards, parking areas, halls, corridors, "central and appurtenant installations for services such as power, light…", "all apparatus and installations existing for common use"; "wiring" appears in the capital-replacement definition (subd. 1-a(e)). → §5 para 2, §8.5 callout, condo section + table, §9 answers (budget, funding). Stated on page as general description, not legal advice.
- `NYC Local Law 126 of 2021 parking structure periodic inspection requirement Queens deadline` · WebSearch → https://www.thorntontomasetti.com/local-law-126-nyc-parking-structure-inspections (WebFetch): LL126 (2021), DOB Article 323; six-year cycle; QPSI engineer; Queens all CDs Sub-Cycle 1C, Jan 1 2026–Dec 31 2027; SAFE / SREM / UNSAFE (repair within one year). → facts table, §8.5 callout, garage section, FAQ.
- Silo sources reused: sub-50 V no DOB permit + firestopping; OFNR/OFNP listings (cablinginstall); HPD/FCC fair access.
- Local news (Queens Chronicle / QNS / Flushing Post) on fiber-installation contractors in Flushing 2026: EMPTY.

### Pricing used (existing AESS Queens prices, copied verbatim from fiber-optic-installation-queens — no new prices)
$37 termination; $42 OTDR/strand; $391 MM drop; $447 SM drop; $4,725–$7,350 12-strand OM4; $8,400–$15,750+ 24-strand OS2; from $2,520 second room; $195/hr 3-hr min ($585); packages $1,392 / $4,725–$7,350 / $8,400–$15,750+. (Inherits the Queens drop-price conflict already logged.)

### Images (11) — permanent image rule; Drive folder empty (main run 11:40Z), CompanyCam not connected
images: 11 reused from images/low-voltage/ (10) and images/network/ (1) (no real Fiber Optic Installation photos yet). Each cropped (no generation) to exclude faces and the phone numbers printed on shirts, and the lobby crop excludes a "123 Main Street" directory sign. Sources chosen by perceptual hash as least-used on fiber pages (6 scenes never used before).
| File (images/fiber-optic-installation/) | Source | Shows |
|---|---|---|
| fiber-optic-installation-flushing-fusion-splicer-patch-rack.webp (hero) | low-voltage/low-voltage-installation-brooklyn-fiber-splice-tray.jpg | fusion splicer, IPA bottle, strippers, yellow fiber, patch rack |
| fiber-optic-installation-flushing-stud-wall-patch-panel-cables.webp | low-voltage/low-voltage-installation-bronx-idf-patch-panel-build.jpg | patch panel between metal studs |
| fiber-optic-installation-flushing-cable-box-staging-open-floor.webp | network/network-installation-bronx-cat6-cable-box-staging-fitout.webp | cable boxes staged on concrete floor |
| fiber-optic-installation-flushing-lobby-video-intercom-panel.webp | low-voltage/low-voltage-installation-long-island-lobby-video-intercom.jpg | video intercom panel on stone wall |
| fiber-optic-installation-flushing-storefront-entrance-camera-mount.webp | low-voltage/low-voltage-installation-nassau-county-storefront-camera-install.jpg | bullet camera on soffit over glass entrance |
| fiber-optic-installation-flushing-door-strike-keypad-exit-button.webp | low-voltage/low-voltage-installation-long-island-electric-strike-keypad.jpg | electric strike, keypad, push-to-exit |
| fiber-optic-installation-flushing-tone-tracer-wall-jack-rack.webp | low-voltage/low-voltage-installation-dutchess-county-08-tone-generator-trace.jpg | tone probe at wall jack, rack |
| fiber-optic-installation-flushing-recessed-display-box-patch-cable.webp | low-voltage/low-voltage-installation-bronx-display-recessed-box.jpg | recessed box behind display, testers |
| fiber-optic-installation-flushing-ceiling-access-point-scissor-lift.webp | low-voltage/low-voltage-installation-bronx-access-point-lift-install.jpg | access point into ceiling from scissor lift |
| fiber-optic-installation-flushing-corridor-ceiling-cable-bundle.webp | low-voltage/low-voltage-installation-hudson-valley-10-school-corridor-cable-pull.jpg | cable bundle in corridor ceiling over lockers |
| fiber-optic-installation-flushing-conference-display-wall-mount.webp | low-voltage/low-voltage-installation-brooklyn-11-conference-room-display-cabling.jpg | display being mounted in meeting room |
Review note: library photos look AI-generated (same caveat as Queens/Long Island); only the hero shows fiber specifically.

### Keyword plan (Flushing page)
Service: fiber optic installation Flushing, condominium fiber backbone, building fiber riser, fusion splicing, OTDR testing, strand map. Problem: carrier drops through common ceilings, landlocked buildings, carrier entry on parking level, retail podium in the way, sponsor turnover records, LL126 garage repairs, flood-prone cellars. Technology: OS2, OM4, OFNR/OFNP, armoured cable, innerduct, LC/SC/MPO, zone cabinets, media converters. Industry: condo boards/managing agents, office and medical condo owners, malls/food halls, hotels in podiums, developers. Geographic: Flushing, downtown Flushing, Main Street, Roosevelt Ave, 39th Ave, Prince St, 40th Rd, 37th Ave, Union St, 138th St, College Point Blvd, Kissena Blvd, Sanford Ave, Northern Blvd, Murray Hill, Broadway–Flushing, East Flushing, Queensboro Hill, Auburndale, Flushing Creek, Willets Point.

## Fordham, Bronx — local research (2026-10-17 batch, fiber-optic-installation-fordham-bronx-ny)

Neighbourhood page; up = /fiber-optic-installation-bronx; phone (646) 490-0629 (800 only in shared header); GBP Bronx (#bronx, 460 E Fordham Rd — the GBP office is inside this neighbourhood). Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. "FC search" = mcp__Firecrawl__firecrawl_search (excerpts only unless scraped); "FC scrape" = mcp__Firecrawl__firecrawl_scrape. Silo-wide sources already in research/fiber-optic-installation.md are reused only where noted.

Page thesis: Fordham is the Bronx's busiest shopping-and-transit crossroads, where old buildings keep changing jobs (a 1930s bank becomes a supermarket and a dormitory, a 1929 movie palace becomes a 4,000-seat arts centre, storefronts turn over, office floors fill with clinics, schools and agencies). Fiber here is re-planned every time a building's use changes, and the work is scheduled around a curb that never empties (new offset bus lanes, delivery windows, vendors, crowds). Different from the Bronx parent (site-wide backbones for big complexes/cold chain).

### Reddit (local)
- Query: `reddit Fordham Bronx apartment internet fiber Fios building` · FC search → https://www.reddit.com/r/Fios/comments/1oz9xcz/1_gb_fios_installion_in_a_5thfloor_apt_bronx_nyc/ (excerpt: "The technician did, in fact, bring the ONT box"; Bronx, exact neighbourhood not stated) — not used. https://www.reddit.com/r/verizon/comments/1u083m9/how_do_i_get_fiber_in_my_building_nyc/ (excerpt: "Fios service is available in your neighborhood just not in your building right now. Equipping your building with Fios may take up to 6-12 months") → §10.5 H3 2. https://www.reddit.com/r/rva/comments/70xglo/if_you_have_fios_and_live_in_an_apartment/ (excerpt, Richmond VA thread: "Verizon provides fiber to the building, but it is the landlord's responsibility to provide connectivity from the point where Verizon terminates") → §10.5 H3 6 (attributed as an out-of-area forum claim).
- Query: `reddit r/bronx Fordham Road living internet slow building old apartment` · FC search → https://www.reddit.com/r/howislivingthere/comments/1wa3g7e/how_is_life_in_the_bronx/ (excerpt: "Fordham road is probably one of the most chaotic shopping area in the country.") → "Working the Curb" section para 1. Other r/bronx results (lease/safety threads) not about wiring — not used.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG — EMPTY (not accessible in build env)
Substitutes for the §10.5 reality check (claims quoted as the pages state them):
- Query `reddit Fordham Bronx apartment internet fiber Fios building` · FC search → https://www.verizon.com/home/internet/near-me/new-york-ny/ (excerpt: "Bronx Fios is widely available across the Bronx") → §10.5 H3 1. https://www.cnet.com/home/internet/best-internet-providers-in-the-bronx-ny/ (excerpt: "Verizon Fios is the best internet service provider in the Bronx, with speeds up to 2000Mbps and prices starting at $50 per month") → §10.5 H3 3.
- Query `reddit r/bronx Fordham Road living internet slow building old apartment` · FC search → https://newyorkcomputerhelp.com/how-to-fix-slow-wifi-in-your-nyc-apartment-2026-edition/ (excerpt: "Most slow WiFi problems in NYC apartments stem from three culprits: terrible router placement, building interference, and outdated equipment.") → §10.5 H3 4.
- Query `does a small business need fiber optic cabling or is Cat6 enough office 100 meters` · FC search → https://igtech365.com/cat6-vs-cat6a-fiber/ (excerpt: "Cat6 is sufficient for standard office use, fiber is the best choice for connecting multiple sites.") → §10.5 H3 5; https://www.clawcomm.com/... (Cat6 1 Gbps at 100 m, 10 Gbps to ~55 m; Cat6A 10 Gbps at 100 m) → §10 table. https://www.wirednm.com/wired-blog/cat6-vs-cat6a-vs-fiber ("You need fiber when runs stretch past 100 meters or when you connect multiple floors or buildings") → §10.5 H3 5.
- Silo source reused: T-Mobile "can take up to 4 hours" (research/fiber-optic-installation.md §2) → §10.5 H3 7.
- Yelp 1–3★: Query `yelp low voltage cabling contractor Bronx Fordham reviews` · FC search → only Yelp search pages for electricians in Throgs Neck, Norwood, Edenwald, Westchester Square; no fiber/cabling reviews. EMPTY.

### Commercial district, demographics, transit (primary source)
- Query `Fordham Road Business Improvement District businesses shoppers retail corridor Bronx` · FC search → https://www.nyctourism.com/shopping/fordham-road-business-improvement-district/ (excerpt: "almost 300 specialty stores ranging from nationwide chains to locally owned independent shops"); https://fordhamroadbid.org/ (excerpt: BID formed 2005) → §5 para 1, §8 intro.
- Same query → https://www.nyc.gov/assets/sbs/downloads/pdf/neighborhoods/avenyc-cdna-fordham.pdf (FC scrape, SBS Commercial District Needs Assessment, Sept 2021–June 2022, with Fordham Road BID): 756 surveys; 657 storefronts analysed along Fordham Rd (Andrews Ave–Southern Blvd), Jerome Ave and Grand Concourse (E 184th–Kingsbridge Rd), Webster Ave (E 188th–E 194th), E 188th St, Third Ave; 80 vacant storefronts; 40 doctors/dentists/medical, 46 cell-phone/electronics, 20 schools/educational, 26 government/social services/nonprofits/houses of worship, 12 banks; 21% storefronts in poor condition; 43% of merchants have 0–2 full-time employees; 188 street vendors, "largest street vending scene in the Bronx"; 118,076 residents; 86,189 per sq mi; car ownership 23.7%; "fourth busiest Metro-North station"; 4, B, D lines; Fordham Plaza reconstructed 2016 for nearly $34 million; Bronx Night Market on the plaza since 2018 (April–October); Bryan Park opened 1933, renovated 2015, hosts "Sparkling the Heart of Fordham" each December; NYC DOT Oct 2021 pedestrian count E Fordham Rd Valentine–Tiebout 7,296 weekday afternoon; NYS DOT 2019 AADT E Fordham Rd Webster Ave–Bronx River Pkwy 32,103; Bx12-SBS average monthly ridership 875,152 (2021); 46% of jobs located in Fordham are in education, health care and social assistance; St. John's College (Fordham University) opened 1841; "iconic office buildings" housing agencies, healthcare, nonprofits. → hero, §5 paras + §5.5 list, §8 cards, Curb section, Clinics section, §13, regional notes.

### Street redesign (local news + DOT)
- Query `Fordham Road bus lanes DOT redesign 2025 Bronx Times Norwood News merchants` · FC search → https://www.nyc.gov/html/dot/downloads/pdf/fordham-rd-sedgwick-ave-bronx-river-pkwy-cb6-may2026.pdf (FC scrape, DOT to CB6, May 14, 2026): buses as slow as 5 mph, 130,000 average daily riders; top 10% most dangerous Bronx corridors; April 2026 DOT visited 217 businesses, 60% receive deliveries in the curbside bus lane; offset bus lanes + new loading zones; curb rules tailored per block (e.g. 60 ft commercial-vehicle parking); ACE bus cameras since 2022, stationary cameras since 2011; "Fordham Road will remain open" during implementation; lanes operational late summer/fall. → Curb section, §9 curb Q, §12 step 3.
- Same query → https://ny1.com/nyc/all-boroughs/traffic_and_transit/2026/07/22/city-announces-redesign-of-bus-lanes-on-fordham-road (FC scrape, NY1, July 22, 2026): groundbreaking; offset bus lanes Sedgwick Ave to Boston Road; 130,000 daily riders; 62% of households without a car; completion by end of year; Belmont BID concern quoted. → Curb section.
- Norwood News https://www.norwoodnews.org/update-feliz-critical-of-fordham-road-redesign-investment-scope/ (excerpt: redesign underway in Fordham Manor/Kingsbridge Heights, July 27, 2026) → Curb section (date only).

### Broadband
- Query `Bronx Community District 5 OR 7 Fordham households without broadband subscription percent` · FC search → https://www.osc.ny.gov/files/reports/pdf/report-20-2025.pdf (excerpt, Figure 8): PUMA 4207 Fordham, Bedford Park & Norwood — 47.8% of households without broadband, 33.2% cellular data only, 32.9% below poverty (State Comptroller definition). → §5.5 list (attributed, definition noted). https://www.thecityreporter.nyc/2025/07/08/bronx-internet-access-laptop-affordable-broadband/ (excerpt: "In the Fordham, Bedford Park and Norwood neighborhoods… more than 30% of households lack broadband") → §5 para 2.

### Buildings that changed use (thesis)
- Query `Dollar Savings Bank building Grand Concourse Fordham landmark redevelopment` · FC search + FC scrape https://en.wikipedia.org/wiki/Dollar_Savings_Bank_Building: 2516–2530 Grand Concourse, block bounded by Grand Concourse, Fordham Rd, Valentine Ave, E 192nd; built 1932–1952; banking hall with basement safe-deposit lobby and steel vaults; NYC landmark (exterior and interior) July 19, 1994; NRHP; bank closed 2014; banking hall became Fine Fare supermarket 2024; Lehman College 184-bed dorm "Lehman Grand" opened Aug 2026. → "When a Fordham Building Changes Jobs", §13 card, §9 vault Q.
- FC scrape https://www.norwoodnews.org/bedford-park-the-lehman-grand-lehman-colleges-first-dorm-opens/ (Norwood News, Aug 6, 2026): ribbon cutting Aug 5, 2026; "more than 180 beds"; 58 furnished rooms with private bathrooms and free WiFi; Fine Fare on ground floor; 10-story office block and 50-foot clock tower added early 1950s; Lehman campus less than a mile away; MADDD also redeveloping Kingsbridge Armory. → same sections + Residence Halls section.
- Query `Loew's Paradise Theater Grand Concourse 188th Street opened 1929 seats today` · FC search + FC scrape https://secretnyc.co/bronx-historic-paradise-theater-reopening/ (Sept 22–23, 2026): opened 1929, John Eberson; closed nearly 30 years; becoming Paradise Performing Arts Center, 4,000 seats, "second-largest theater in New York City"; new rooftop outdoor stage, restaurant, bar; 2403 Grand Concourse; preview/community event Nov 10. Opening date Sept 7, 1929 from https://en.wikipedia.org/wiki/Paradise_Theater_(Bronx) excerpt. → Changes-Jobs section, §9 theatre Q, §13 card.
- Query `"One Fordham Plaza" office building Bronx square feet tenants` · FC search → https://www.nytimes.com/2007/07/11/realestate/commercial/11bronx.html (excerpt only; FC refuses nytimes.com): "One Fordham Plaza, a 557,000-square-foot office and retail building"; headline "A Bronx Retailing Hub Is Getting Offices, Too". LoopNet/realbird excerpts: suites on 9th and 10th floors (1,700–17,928 SF) listed. → §8 card, Clinics section.
- Query `Webster Avenue Fordham new affordable housing development 2025 2026 Bronx building units` · FC search → https://newyorkyimby.com/2026/07/rendering-revealed-for-2740-webster-avenue-in-fordham-the-bronx.html (excerpt): 2740 Webster Ave, 12-storey dormitory, 215,129 sq ft, 162 units, 600 students, at E 197th St, completion July 2028 for 2029 academic year; next door 2768 Webster Ave planned 13 storeys, 510 residential units. https://thenyhc.org/projects/2850-webster-avenue/ (excerpt: 12-storey, 188 senior affordable units). → Residence Halls section, §5 para 4.

### Campuses, institutions, landmarks
- Query `Monroe College Bronx campus buildings Jerome Avenue Fordham residence halls` · FC search (excerpt: Bronx campus "a fixture since 1967 of the lively Fordham section", commuter campus) + FC scrape https://www.monroeu.edu/sites/default/files/documents/2023/09/13/BXCampusMap_091123.pdf: King Hall 2501 Jerome Ave, Jerome Hall 2468 Jerome Ave, Monroe Hall 29 E Fordham Rd, Ustin Hall 2375 Jerome Ave. → Clinics/schools section, §7 card.
- Query `Fordham University Rose Hill campus acres buildings founded 1841 students` · FC search → https://www.fordham.edu/about/campuses/rose-hill-campus/ (excerpt: 85 acres, Gothic architecture, est. 1841). → §13 card.
- Query `Bronx Library Center Kingsbridge Road square feet opened 2006 largest library Bronx` · FC search → https://www.nypl.org/locations/bronx-library-center (excerpt: opened January 17, 2006; $50 million; 78,000 sq ft; NYPL's first green library). → §13 card.
- Query `Poe Park Visitor Center Grand Concourse Kingsbridge Road Poe Cottage opened` · FC search → https://www.nycgovparks.org/parks/poe-park (excerpt: park opened 1902; cottage opened to public at present site 1913); https://urbanomnibus.net/2012/07/field-trip-poe-park-and-cottage/ (Visitor Center opened May 2012); https://tmarch.com/poe (2,700 sq ft). → §13 card.
- Query `Fordham Hill Owners Corporation co-op buildings apartments Sedgwick Avenue history` · FC scrape https://fordhamhill.com/living-at-fordham-hill/history: built 1950 by Equitable Life as rentals, co-op 1982, nine high-rises, 1,130 apartments. → §7 card.
- Query `St. Barnabas Hospital SBH Health System Bronx Third Avenue 183rd Street beds` · FC search → https://www.sbhny.org/locations/ (excerpt: St. Barnabas Hospital 4422 Third Ave; ambulatory care 4487 Third Ave; wellness 4507 Third Ave). Bed counts from third-party sites NOT used. → Clinics section (named only).

### Codes / rules used in Q&A
- Query `NYC construction noise permitted hours weekdays 7 a.m. 6 p.m. after hours variance DOB DEP` · FC search → https://www.nyc.gov/site/dep/environment/construction-noise-rules-regulations.page (excerpt: construction allowed 7am–6pm weekdays); https://www.nyc.gov/site/buildings/industry/after-hour-variances.page (AHV required before 7 am, after 6 pm, Sat/Sun). → §9 noise Q.
- Query `exit stair enclosure penetrations limited equipment serving the stairway building code 1023.5` · FC search → https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-174119 (NYC BC 1023.5: penetrations into/through interior exit stairways prohibited except listed items). → §9 stairwell Q.
- Query `NFPA 13 sprinkler piping shall not be used to support non-system components cables` · FC search → https://up.codes/s/support-of-non-system-components; https://www.meyerfire.com/daily/any-contact-allowed-with-sprinkler-pipe ("Sprinkler piping or hangers shall not be used to support non-system components") → FAQ sprinkler.
- Query `Landmarks Preservation Commission permit required interior landmark work cabling alterations FAQ` · FC search → https://www.nyc.gov/site/lpc/about/permits-and-making-alterations.page (excerpt: LPC permit for interior work required when the interior is a designated interior landmark, when DOB permit needed, or when interior work affects exterior) → §8.5 callout, Changes-Jobs section.
- Silo sources reused: sub-50 V DOB statement (existing site content), firestopping, OFNR/OFNP, bend radius (FOA) → §8.5, §10.

### Local news on Fordham fiber-installation contractors 2026 — EMPTY (none retrieved).

### Pricing used (existing AESS Bronx prices copied verbatim from fiber-optic-installation-bronx — no new prices)
$35/termination; $40/strand OTDR; $391 MM drop; $447 SM drop; 12-strand OM4 $4,500–$7,000; 24-strand OS2 $8,000–$15,000+; second telecom room from $2,400; $195/hr, 3-hr min ($585). Packages: Starter $894 (2 × $447), Standard $4,500–$7,000, Premium $8,000–$15,000+ (same as parent; Bronx 1.00×).

### Images (11) — permanent image rule; Drive folder empty (checked by main run 11:40Z), CompanyCam not connected
Each photo viewed before use. Where the source showed a face, a shirt/cap/sign with a phone number, or a readable paper document, the photo was CROPPED (PIL, no generation or retouching) so the saved WebP shows none of them; alt/title/caption describe only what is in the crop.
| File | Source | Crop | What it shows |
|---|---|---|---|
| fiber-optic-installation-fordham-bronx-fusion-splicer-bench-rack.webp (hero, eager) | low-voltage/low-voltage-installation-brooklyn-fiber-fusion-splice.jpg | x780–1400 | gloved hands at a lit fusion splicer, yellow jumpers on rack, IPA bottle, cleaver, strippers |
| fiber-optic-installation-fordham-bronx-sc-adapter-panel-jumpers.webp | low-voltage/low-voltage-installation-brooklyn-fiber-splice-tray.jpg | x880–1400, y0–560 | two rows of blue SC adapters with yellow jumpers |
| fiber-optic-installation-fordham-bronx-retail-fitout-ceiling-cable.webp | low-voltage/low-voltage-installation-brooklyn-retail-store-ceiling-pull.jpg | x560–1290 | blue cable dropped from open black ceiling into a clothing store being fitted out |
| fiber-optic-installation-fordham-bronx-inherited-rack-before-after.webp | network/network-installation-bronx-network-rack-cleanup-before-after.webp | none | before/after rack cleanup (no people) |
| fiber-optic-installation-fordham-bronx-jhook-pathway-office-floor.webp | low-voltage/low-voltage-installation-bronx-02-jhook-pathway-bundle.jpg | none | installer from behind seating bundles in J-hooks over an open-plan floor (no phone number) |
| fiber-optic-installation-fordham-bronx-ceiling-grid-drop-pull.webp | low-voltage/low-voltage-installation-bronx-10-ceiling-grid-bundle-pull.jpg | none | installer from behind on a ladder pulling drops through ceiling grid |
| fiber-optic-installation-fordham-bronx-ceiling-access-point-mount.webp | low-voltage/low-voltage-installation-bronx-09-ceiling-access-point-drop.jpg | none | installer from behind mounting a ceiling access point |
| fiber-optic-installation-fordham-bronx-corridor-ceiling-bundle-ap.webp | low-voltage/low-voltage-installation-hudson-valley-10-school-corridor-cable-pull.jpg | x600–1400, y0–820 | gloved hand on a cable bundle above a corridor ceiling, round access point, wall banner |
| fiber-optic-installation-fordham-bronx-tracing-unlabeled-cable.webp | network/network-installation-bronx-network-cable-toner-tracing.webp | x0–770 | tone probe and tester on a labelled patch field (hands only) |
| fiber-optic-installation-fordham-bronx-metal-stud-fitout-spool.webp | low-voltage/low-voltage-installation-bronx-04-metal-stud-rough-in.jpg | x0–640 | metal-stud fit-out, installer on ladder seen from behind at distance, cable spool |
| fiber-optic-installation-fordham-bronx-riser-bundle-corridor.webp | network/network-installation-long-island-idf-riser-cable-bundle.webp | x640–1448 | large blue bundle rising into ceiling beside a corridor, cable box |
Overlap note: the splicer, adapter-panel and riser-bundle scenes also appear (uncropped) on earlier fiber pages; the other eight scenes had no recorded fiber-silo use. FLAG (same as earlier builders): the library photos appear AI-rendered (garbled small text on tools/labels) — Anwar to review; replace with real AESS photos when uploaded.

### Keyword plan (Fordham page)
Service: fiber optic installation Fordham, fiber backbone Fordham Road, storefront fiber, office-floor riser, residence hall fiber, fusion splicing, OTDR testing. Problem: building changing use, inherited unlabeled cabling, curb/bus-lane access, crowds and vendors, noise hours, exit-stair restrictions, sprinkler pipes, landmark interiors. Technology: OS2, OM4, OFNR/OFNP, armored, MPO/LC, splice enclosures, PoE switches/APs. Industry: retail chains and independents, clinics, social-service agencies, colleges/dorms (Lehman Grand, Monroe, Fordham University), theatre/venue (Paradise PAC), supermarkets, banks. Geographic: Fordham, Fordham Road, Grand Concourse, Webster Avenue, Jerome Avenue, Kingsbridge Road, E 188th St, Third Avenue, Fordham Plaza, Fordham Manor, Fordham Heights, University Heights, Belmont, Bedford Park, Kingsbridge Heights.


## Hudson Square, Manhattan — local research (2026-10-17 batch, fiber-optic-installation-hudson-square-manhattan-ny)
Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources above (lowvoltagenewyork.com cost page, unio.digital, Empire City Subway) are reused for the §10.5 reality check; only Hudson Square-specific research is new here.

Thesis: Hudson Square is a few very large, very strong printing/freight-era floors owned by a few very large owners — so the hard part of fiber is horizontal (deep plates past copper's 90 m reach, flat-slab column zones, core on one side, floors re-cut by demising) and the approvals run through portfolio landlords, ground lessors and meet-me-room operators, on blocks shaped by Holland Tunnel traffic. (Distinct from Chelsea = carrier hotels next door / building types stop fiber at different points; Midtown = vertical layout; FiDi = separable/movable/dry backbone.)

### Reddit (local)
- Query: `reddit Hudson Square internet fiber building office apartment` · WebSearch → no reddit.com results (only 325 Hudson / DivcoWest pages). EMPTY. Page §5 states plainly that no neighbourhood-specific Reddit threads were found.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
- §10.5 reality check uses published competitor/listing claims instead: lowvoltagenewyork.com ("$1–$6 per foot", "singlemode glass is now cheaper than OM4" / SM optics "1.5–5×", "Plenum rating adds 15–25%", OTDR "$75–$150/hour; nobody publishes a flat per-strand rate", street-opening permit / Empire City Subway), unio.digital ("$300 to $800 per fiber drop") — all from the existing Manhattan section of this file; DivcoWest 325 Hudson ("atop the fiber-dense Hudson Street corridor") — new, below.

### History, zoning, ownership
- Query: `Hudson Square rezoning 2013 former Printing District Trinity Real Estate` · WebSearch → https://hraadvisors.com/news/new-york-city-council-approves-rezoning-of-hudson-square-neighborhood/ (WebFetch): Council approved March 20 (2013); "18-block area above Canal Street"; more than seven years of planning; >3,000 apartments, 20% affordable; 444-seat elementary school in base of a residential tower (Trinity-funded); prior zoning commercial/manufacturing only, no housing; protection of existing commercial stock. → §5 para 4, Rezoning section.
- Same query → https://www.6sqft.com/?p=79831 (6sqft, Jan 2 2018, WebFetch): printers in big concrete-and-steel factory buildings early 1900s near Wall Street clients; left 1970s–80s, tech/design moved in; Queen Anne granted Trinity 215 acres in 1705; Trinity owned almost 40% of Hudson Square incl. ground leases; rezoning = 18 blocks bounded by Greenwich, W Houston, Varick, Sixth Ave, Canal; "largest privately initiated rezoning in NYC history"; $27M streetscape plan. → §5 paras 1 and 3, Rezoning section, ground-lease Q&A.
- Query: `Hudson Square Properties Trinity Norges Bank Hines joint venture buildings square feet 2015 stake` · WebSearch → https://nbim.no/en/news-and-insights/the-press/press-releases/2016/fund-acquires-larger-share-of-hudson-square-portfolio (WebFetch): 7 June 2016; Norges up to 48%, Trinity 51%, Hines 1%; 11 office buildings; 4.9M sq ft; $142M for 4%, $1.7B total. → §5 para 3, facts list, Owners section.
- Same query → https://www.hines.com/properties/hudson-square-portfolio-new-york (WebFetch): directory index only, no building data. EMPTY (not used).
- Query: `Hudson Square Business Improvement District founded 2009 blocks companies employees` · WebSearch → https://www.hudsonsquarebid.org/2015/wp-content/uploads/2018/10/HSQ_AnnualReport_181015_LoRes.pdf (BID FY2018 annual report, WebFetch): approved Jan 28 2009 as 64th BID; bounded W Houston/Canal/6th Ave/Greenwich, expanding to Clarkson/West; 40,000+ workers in ~1,000 businesses; 71% creative industries; $27M "Hudson Square is Now" streetscape; Spring Street Park $6M renovation opened FY2018; Sam Schwartz study — one-way Verrazzano/Holland tolling routes traffic via Canal St and Hudson Square; pedestrian safety managers −45% blocked intersections/crosswalks. → Commercial section intro (71%), Holland Tunnel section, Spring Street Park landmark card.
- Same query → https://www.ny.gov/sites/default/files/2024-02/Hudson_Square_NYF_2_Application.pdf (Hudson Square NY Forward application, 2024, WebFetch): ~33 blocks Clarkson/6th Ave/Canal/West St; pre-pandemic daytime population ~70,000 (≈60,000 office workers, 3,000 residents, 4,000 students/faculty); >12M sq ft office; Hudson Square Properties manages 7 office buildings, 4.58M sq ft; 1920s West Side Highway, Holland Tunnel and Sixth Ave extension made area logistics/manufacturing hub, printing concentrated, large-floor-plate buildings replaced row houses (some survive in southwest); 345 Hudson built 1931; 2 Hudson Square planned 26 storeys/450,380 sq ft, SHoP, 444-seat school; 388 Hudson HPD fully affordable; vacancy 7.4% pre-2019 → 14.8% post-pandemic; no broadband or flood content. → §5 para 1, facts list, architecture card (walk-ups), Owners section (4.58M sq ft, vacancy), Rezoning section (2 Hudson Square, 388 Hudson).
- Query: `SoHo NoHo rezoning approved December 2021 City Council units joint living work quarters artists` · WebSearch → https://www.6sqft.com/nyc-soho-noho-rezoning-approved/ (WebFetch): approved Dec 15 2021 (article Dec 16); ~3,000 homes, ~900 permanently affordable; 50+ blocks; west edge Sixth Ave & West Broadway. → Rezoning section (context across Sixth Avenue).

### Buildings, landmarks, corridors
- Query: `Google St. John's Terminal 550 Washington Street opened 2024 freight terminal` · WebSearch → https://newyorkyimby.com/2024/02/google-opens-st-johns-terminal-headquarters-at-550-washington-street-in-hudson-square-manhattan.html (WebFetch): ribbon-cutting Feb 2024; 1.3M sq ft; 12 storeys, 232 ft; COOKFOX; "over 3,000 Google employees"; concrete-encased I-beams that once supported elevated railway tracks; spans two blocks (West St, W Houston, Washington, DSNY building); 1.7M sq ft campus incl. 315 & 345 Hudson. → facts list, architecture card, Geometry section (new on old), landmark card.
- Same query → https://www.6sqft.com/google-opens-new-nyc-office-at-historic-st-johns-terminal/ (WebFetch): built 1934 as terminus of NY Central's West Side elevated freight line (High Line); nine floors added atop three; Oxford bought 2017 ($700M); Google bought 2021 for $2.1B. → architecture card, landmark card, Geometry section.
- Query: `Disney headquarters 4 Hudson Square 137 Varick Street completed` · WebSearch → https://newyorkyimby.com/2022/04/disney-headquarters-tops-out-at-4-hudson-square-in-hudson-square-manhattan.html (WebFetch): 4 Hudson Square / 137 Varick; 338 ft, 22 storeys; 1.2M sq ft offices/studios/retail; SOM; Silverstein; Lendlease; full block Varick/Spring/Hudson/Vandam; topped out Apr 2022. → architecture card, landmark card.
- Query: `Disney moves into new New York headquarters 7 Hudson Square 2024 2025 employees` · WebSearch → https://en.wikipedia.org/wiki/7_Hudson_Square (WebFetch): official address 137 Varick, vanity 7 Hudson Square; land owned by Trinity, 99-year lease for $650M; The View moved Sept 2024 … GMA June 2025, ESPN shows after; four underground taping facilities; ESPN facilities connect to Bristol, CT over fiber links. → §5 para 3 (99-year lease), ground-lease Q&A, Media Floors section, landmark card.
- Query: `325 Hudson Street data center carrier hotel Hudson Square` · WebSearch → https://www.datacenterfrontier.com/colo/article/55388769/h5-data-centers-325-hudson-a-manhattan-carrier-hotel-with-soho-dna-dcf-tours (WebFetch): 225,000 sq ft mixed-use (office/lab/data centre); 40+ networks; DE-CIX & NetIX; diverse entries, north and south risers; 13 ft slab-to-slab; 150 psf floor loading. → facts list, floor-load Q&A, architecture card.
- Query: `reddit Hudson Square internet fiber building office apartment` (result) → https://divcowest.com/property/325-hudson/ (WebFetch): 220,000 sq ft, 10 storeys; "atop the fiber-dense Hudson Street corridor"; MMR with 40+ fiber networks and five transatlantic subsea cables; adjacent to Disney HQ, surrounded on three sides by Google; near NY Genome Center and NYU Langone biolab co-working. → meet-me-room Q&A, glass-tower Q&A, lab Q&A, §10.5 H3 "fiber-dense corridor", landmark card. (Note: two sources give 220,000 vs 225,000 sq ft; page avoids the figure.)
- Query: `Hudson Square printing buildings heavy floor loads high ceilings 75 Varick 375 Hudson former printing plant` · WebSearch → https://commercialobserver.com/2019/05/the-plan-hudson-square-loft-buildings-get-a-fresh-look/ (WebFetch): 75 Varick (One Hudson Square), 225 Varick, 155 Avenue of the Americas = 1920s former printing-press buildings near the Holland Tunnel; owned by Hines/Trinity/Norges; lobbies stripped to original concrete columns and floors; 225 Varick lobby 14-ft ceilings; tenants Squarespace, Horizon Media. No floor-load data. → architecture card, landmark card ("printing trio"), Media Floors section.
- Query: `Holland Tunnel opened 1927 Manhattan entrance Broome Street exit rotary Hudson Square St. John's Park` · WebSearch → https://en.wikipedia.org/wiki/Holland_Tunnel (WebFetch): opened Nov 13 1927 (ceremony Nov 12); westbound tube starts at Broome St between Varick and Hudson; eastbound surfaces at rotary on site of former St. John's Park Terminal (block Laight/Varick/Beach/Hudson); 89,792 vehicles/day in 2016; Freeman Plaza West 2013, East/North 2014. → facts list, Holland Tunnel section, landmark card.
- Same query → https://www.hmdb.org/m.asp?m=149495 (WebFetch): 1929 engineers' plaque inside the Broome St entrance (groundbreaking 1920, chief engineers Holland, Freeman, Singstad). Not used on page.
- Query: `Hurricane Sandy flooding Hudson Square Manhattan 2012 basements power outage Varick Street` · WebSearch → general Lower Manhattan Sandy items only, nothing Hudson Square-specific. EMPTY (no flood claim made on page).

### Local news / hyperlocal on Hudson Square fiber contractors — EMPTY (none retrieved).

### Local licensing / permits / building rules
- No new sources. Page reuses the silo position (sub-50 V fiber not filed with DOB on its own; filed alteration covers it), NYC Building Code exit-stair restriction stated generally (no section number), and portfolio-landlord rules described as typical practice, not quoted from any one building. Flat-slab column-zone coring restriction and TIA-568 90 m + 10 m copper limit stated as general engineering/standards knowledge (no URL).

### Pricing used (existing AESS prices only — no new prices)
- fiber-optic-installation-manhattan lines verbatim: $44/termination, $50/strand OTDR, $453 MM drop, $517 SM drop, $5,625–$8,750 12-strand OM4, $10,000–$18,750+ 24-strand OS2, from $3,000 second telecom room, $195/hr 3-hr min ($585). Packages are sums only: $1,128 (12×$44 + 12×$50); $7,437–$10,562 (OM4 backbone + 4×$453); $14,034–$22,784+ (OS2 backbone + $3,000 + 2×$517).

### Images (11) — permanent image rule; Drive folder `AESS Website Photos/Fiber Optic Installation` empty (checked by main run), CompanyCam not connected
Copied, cropped (faces, shirt phone numbers and readable documents removed) and converted to WebP in images/fiber-optic-installation/: from images/low-voltage/ (4): brooklyn-fiber-fusion-splice → hudson-square-fusion-splicer-at-rack; brooklyn-fiber-splice-tray → hudson-square-splicer-below-fiber-panel; nassau-county-riser-conduit-pull → hudson-square-conduit-riser-cable-feed; nassau-county-exterior-enclosure-install → hudson-square-brick-wall-enclosure-conduit. From images/network/ (7): bronx-network-drop-conduit-emt-riser → hudson-square-emt-conduit-riser-pull; bronx-core-drill-cmu-wall-penetration → hudson-square-masonry-wall-core-drill; bronx-jhook-ceiling-pathway-bundles → hudson-square-j-hook-ceiling-pathway; bronx-cable-labeling-port-map → hudson-square-panel-port-labeling (cable-map document cropped out); bronx-ceiling-tile-cable-drop-occupied-office → hudson-square-ceiling-tile-cable-drop; bronx-finished-network-rack-firewall-ups → hudson-square-finished-rack-with-ups (person and sign cropped); bronx-network-rack-cleanup-before-after → hudson-square-rack-before-after-cleanup. Only 2 show fiber (splicer frames); the rest show blue copper and are captioned as such. Source library looks AI-rendered — needs Anwar's review. Note: images/fiber-optic-installation/aess-*.webp (20 "AESS fiber" photos added by commit 93994347 to all live fiber pages) also look AI-generated and show full technician faces, so they were not used.

### Keyword plan (Hudson Square page)
Service: fiber optic installation Hudson Square, fiber backbone, floor spine, meet-me room tie-in, fusion splicing, OTDR testing (+ full service-list keyword set). Problem: floor too deep for copper, column-zone coring, portfolio landlord standard, ground lease consent, cross-connect fees, connector contamination, suite demising. Technology: OS2, OM4, OFNP, zone enclosures, pre-terminated MPO trunks, tray/J-hooks/conduit for exposed ceilings. Industry: agencies, media/production, software, life-science labs, residential towers. Geographic: Hudson Square, Varick St, Hudson St, Avenue of the Americas, Spring/Vandam/Charlton, Canal St, Holland Tunnel, Washington/West Sts, SoHo, Tribeca, West Village.

### Question register additions (fiber-optic-installation-hudson-square-manhattan-ny)
§9 Questions Answered:
- The landlord's engineer won't let us core near the columns of our 1920s concrete floor — why, and where can the hole go?
- These floors were built for printing presses — does that mean we can put racks, battery cabinets and a small server room anywhere on the plate?
- Where should the telecom room sit on a floor that wraps around a central core of elevators and stairs?
- Heavy traffic outside our windows leaves grime on every surface — does that get into fiber connectors in the telecom room?
- Our landlord has one cabling standard for its whole portfolio and our IT team has its own spec — whose rules win?
- Our building stands on ground-leased land — does the ground owner have any say over a new carrier entrance?
- Our building has a meet-me room that charges a monthly cross-connect fee — can private fiber get around it?
- We're moving from a glass tower uptown into a 1920s Hudson Square loft — what will be different about getting our network in?
- We're fitting out a lab suite in a converted office building — what changes for fiber near instruments, freezers and safety cabinets?
- (table heading, no "?") Carrier circuit, meet-me cross-connect or owner riser: which piece does each party pay for in a Hudson Square building
§17 FAQ:
- Do you also work in SoHo, Tribeca and the West Village around Hudson Square?
- Why does our building's insurance certificate have to list several different companies as additional insured?
- Do you time deliveries around Holland Tunnel traffic on Varick and Canal?
- Can the roof terrace our landlord is adding get Wi-Fi and a screen off our fiber?
- Can the old electrical conduit cast into our concrete floor be reused for fiber?
- Can you take instructions from our project manager or owner's representative instead of our own staff?
Repair/CTA headings: Far Side of the Floor Gone Quiet? · Hudson Square Office Offline Right Now?

De-dup notes: checked against all 722 question headings/FAQ items on the 33 fiber pages present at build time (including Sunset Park and Astoria drafts). Avoided on purpose (handled in prose only): unloading/curb logistics (Fordham, FiDi, Orange), two suites on one huge floor (Chelsea), exposed printing-plant ceilings (Hunts Point), old chutes/openings in slabs (DUMBO, Dutchess), carrier hotel across town / nearby data centre (Manhattan, LIC), production video (Brooklyn), cross-street links (Rockland), conversion floors (FiDi, Westchester). Closest calls for a human read: COI-naming FAQ vs Queens "Can you issue a certificate of insurance that our property manager or co-op will accept?"; tunnel-delivery FAQ vs Fordham bus-lane unloading Q; telecom-room placement vs Bloomfield "main room in front office, devices at back — move the room?"; landlord portfolio standard vs Bloomfield "national logistics tenant cabling spec".


## Sunset Park, Brooklyn — local research (2026-10-17 batch, fiber-optic-installation-sunset-park-brooklyn-ny)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources and the Brooklyn section above are reused where noted; only Sunset Park research is added here.

Page thesis: Sunset Park is two neighbourhoods split by the Gowanus Expressway. Below Third Avenue, carriers already reach the block-long 1906–1928 reinforced-concrete factory campuses (Industry City meet-me room, Connect IBZ fiber), so the fiber problem is the *length of the building* — a long horizontal run from the campus/carrier handoff to a suite hundreds of feet away (pull points, slab-soffit supports, campus dark fiber vs own strands, closet into campus data room). Above Third Avenue, runs are short but *owners are many* — rowhouses in four 2019 historic districts, divided houses, Fifth/Eighth Avenue storefronts with apartments above and rear extensions. The expressway itself is crossed only by carrier networks (recommend carrier circuits at each site, not private cable). Distinct from Navy Yard (single landlord/BNYDC rules), DUMBO ("cable is cheap, the building is hard"), Downtown Brooklyn (vertical towers/ownership lines).

### Reddit (local)
- Query: `reddit Sunset Park Brooklyn internet Fios Spectrum building apartment options` · WebSearch → no reddit.com result returned (results were technical.ly, untappedcities, listing pages, ispreports.org). Local Reddit: EMPTY. Silo Reddit excerpt reused: r/AskNYC "Its on the ISP to wire your building/apartment" (silo §1) → §10.5 H3 5.

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitute §10.5 claims (quoted as published): streamlinetelecom "$1-6 per linear foot" (silo §5) → H3 1; thenetworkinstallers FBA 2025 underground median $18.00/ft, aerial $8.00 (silo §5) → H3 2; newtechcabling "Copper stops working reliably beyond about 100 meters" and "Small projects can take a day or two" (Brooklyn section) → H3 3, H3 6; ispreports.org fiber availability 95.16% (below) → H3 4; r/AskNYC comment (silo) → H3 5; lowvoltagenewyork "Plenum rating adds 15–25%" (Brooklyn section) → H3 7. Angi/HomeAdvisor/Fixr: EMPTY (stated on page as not reachable). Yelp: EMPTY (not searched separately; silo Yelp searches returned nothing usable).

### Waterfront campuses, buildings, history
- Query: `Industry City Sunset Park buildings square feet history Bush Terminal` · WebSearch → WebFetch https://www.brownstoner.com/history/industry-city-brooklyn-bush-terminal-sunset-park-history (2015): Irving T. Bush; William Higginson designed reinforced-concrete factories (learned via Gair/Turner; Gair buildings in DUMBO); block-long six-storey factories built 1906–1928; WWII peak largest multi-tenant complex in US, 25,000+ employees, own power plants; WWI Navy took piers/warehouses; Bush built the Army terminal (Cass Gilbert, Turner); 1939 Moses BQE on 3rd Ave El pillars; renamed Industry City mid-1980s. → §5 THE NEIGHBORHOOD, §7 building cards (factory lofts), §13 landmark card (Industry City).
- Query: `Industry City 16 buildings 6 million square feet 35 acres Sunset Park tenants` · WebSearch → WebFetch https://brooklyneagle.com/articles/2025/04/08/industry-city-surpasses-650-businesses/ (Apr 2025): 35-acre, ~6M sq ft, 16 buildings, 650+ businesses; $450M+ infrastructure since 2013; parking at 37th & Second Ave; D/N/R, B35/B37. → §5.5 stats, §8 commercial card, §13 landmark card.
- Silo source re-fetched: WebFetch https://dataverge.com/industry-city/ : 882 3rd Ave; 16 interconnected buildings; 40+ carriers via Meet-Me Room; "Industry City Campus Connect" dark fiber from MMR to tenant suites; tenants can move an existing IT closet into DataVerge's data center. → §5, Below the Expressway section, §9 Q1 and Q2.
- Query: `Brooklyn Army Terminal Cass Gilbert 1919 atrium square feet NYCEDC tenants` · WebSearch → WebFetch https://bklynlibrary.org/blog/2023/06/12/brooklyn-army-terminal : Cass Gilbert, completed 1919, largest military supply base in US, 95 acres (page figure; not used — Mann Report 59 acres used instead), transferred to city 1981, NYCEDC-managed, 100+ small businesses. → §7 card, §13 card.
- Same search → WebFetch https://scoutingny.com/the-secret-of-building-b-scouting-brooklyns-incredible-atrium-train-station/ : Building B 980 ft × 360 ft, eight storeys, two rail tracks inside, loading docks at diagonal intervals, ceiling crane, skylight framing. → §7 card, §9 Q5 (atrium) and Q6 (rail tracks), §13 card.
- Query: `Southwest Brooklyn Industrial Business Zone Sunset Park waterfront` · WebSearch → WebFetch https://www.mannpublications.com/mannreport/2026/01/06/building-brooklyns-future-how-the-nycedcs-public-investment-in-sunset-park-is-creating-a-new-model-for-economic-growth/ (Jan 2026): BAT 59 acres, 4.1M sq ft, $500M+ NYCEDC over decade, 100+ businesses (Jacques Torres, MakerSpace NYC, Rooftop Films, Altronix, Uncommon Goods, FABSCRAP, NY Embroidery Studio); BATWorks ~200,000 sf Building A, $100M, permanent 2028; MADE Bush Terminal 20-acre 8-building campus, Building A 140,000 sf manufacturing; Pier 6 five-acre park due 2027; Bush Terminal Piers Park $38M; SBMT offshore wind (not used); BWMM (not used). → §5.5, §8 cards, §13 cards, Who Uses It section.
- Query: `Liberty View Industrial Plaza 850 Third Avenue Sunset Park building history` · WebSearch → WebFetch https://elevatorworld.com/news/usa-news/new-york/nyc/old-building-new-purpose/ : 850 3rd Ave, built 1916, former U.S. Navy supply warehouse, eight storeys, 1.3M sq ft; Salmar bought 2011; exterior restored March 2013; National Register; 22 elevators replaced (only 3 worked). → §5.5, §7 card, §8 card, §13 card.

### Connectivity / broadband (local)
- Query: `Sunset Park Brooklyn households without broadband internet community district 7 percent` · WebSearch → WebFetch https://technical.ly/brooklyn/2015/01/13/sunset-park-fiber-broadband-alicia-glen (Jan 2015): Deputy Mayor Glen "laying high-speed broadband all throughout the Sunset Park innovation corridor"; Industry City and Liberty View already had fiber; Connect IBZ RFP April 2014. → §5 (background), §10.5 H3 2.
- Query: `NYCEDC "Connect IBZ" RFP 2014 fiber industrial business zones Southwest Brooklyn` · WebSearch → WebFetch https://bbcmag.com/xchange-telecom-and-nyc-edc-to-expand-broadband-in-industrial-zones/ (Jul 2015): $5.3M Connect IBZ; Stealth Communications to build fiber in the Southwest Brooklyn IBZ; build-outs to at least 500 commercial tenants over two years; 10 Mbps–1 Gbps+. → §5, §10.5 H3 2.
- Same search → WebFetch https://technical.ly/diversity-equity-inclusion/brooklyn-fiber-bring-commercial-internet-service-sunset-park.md (Feb 2015): Brooklyn Fiber bringing symmetrical 1 Gbps to Industry City (~$500/mo). → §10.5 H3 4 ("independent fiber company that has served Industry City since at least 2015"; provider not named on page).
- Same search → WebFetch https://WWW.NYULANGONE.ORG/files/data-at-a-glance-sunset-park-2022.pdf : population 146,000 (Census 2020); 84% households with broadband subscription (ACS 2016–2020); 77% speak a language other than English at home. → §5.5 stats.
- Same search → WebFetch https://ispreports.org/internet-service-providers-sunset-park-brooklyn-ny/ (updated Sep 2026, FCC BDC data as of Dec 31 2025): fiber availability 95.16%; Verizon fiber and EarthLink fiber 92.2%; page's provider figures don't reconcile with headline. → §5 (quoted as a provider-comparison site's claim), §10.5 H3 4.

### Uphill: historic districts, avenues, expressway
- Query: `Sunset Park Historic District Landmarks Preservation Commission designated 2019 rowhouses` · WebSearch → WebFetch https://citylandnyc.org/landmarks-designates-sunset-park-historic-districts : LPC vote June 18, 2019; Sunset Park North (56 buildings, 44th St 5th–7th Aves, 1903 William Kay row, 1913–14 apartments), Sunset Park South (~285, 54th–59th Sts between 4th and 5th Aves, mostly 1890s), Central Sunset Park (~148, 47th/48th Sts and 6th Ave, 1897–1906), Sunset Park 50th Street (~50, 1897–1903). → §5.5 (≈540 buildings = sum), §7 card, §8.5, §9 Q7, §13 card.
- Same search → WebFetch https://www.6sqft.com/sunset-park-gains-four-historic-districts/ : campaign began 2013 (Sunset Park Landmarks Committee); rowhouses 1890–1919, neo-Grec/Romanesque/Renaissance Revival, brick/limestone/brownstone; 1988 nearly all neighbourhood listed on National Register. → §7 card, §9 Q7, §13 card.
- Query: `Sunset Park Brooklyn 8th Avenue Chinatown largest Chinatown history` · WebSearch → WebFetch https://en.wikipedia.org/wiki/Chinatowns_in_Brooklyn : settlement along Eighth Ave 42nd–68th St since 1980s; ~30 shops before 1984; Winley Supermarket 5523 Eighth Ave 1986; Brooklyn's largest Chinatown; Buddhist temples, bakeries, groceries, community orgs. → §7 card, §8 card, §13 card.
- Query: `Sunset Park Fifth Avenue BID 5th Avenue commercial corridor businesses` · WebSearch → WebFetch https://brooklyneagle.com/articles/2014/02/05/shoppers-go-forth-on-fifth-in-sunset-park/ (2014): ~500 businesses, 5th Ave 38th–64th St (~2 miles); Dominican, Salvadoran, Mexican, Colombian, Cuban, Ecuadorian; BID director "Fifth Avenue is our Main Street in Sunset Park." → §5.5, §8 card, §13 card.
- Query: `Gowanus Expressway Third Avenue Sunset Park elevated highway history 1941 neighborhood divided` · WebSearch → WebFetch https://www.thedrive.com/vintage/2920/the-slow-and-steady-death-of-the-gowanus-expressway : completed 1941 as Gowanus Parkway on former Third Ave el structure; Moses chose 3rd Ave over residents' 2nd Ave proposal; widened to six lanes in 1960s; "well over 100,000 cars and trucks" daily. → §5, Fiber and the Gowanus Expressway section.

### Flood / resilience
- Query: `Sunset Park waterfront Hurricane Sandy flooding Bush Terminal Industry City 2012` · WebSearch → WebFetch https://brooklyneagle.com/articles/2017/07/24/shelter-from-the-storm-in-sunset-park-flood-proofing-industry-city-and-the-brooklyn-army-terminal/ (Jul 2017): NYT-reported $50M Sandy damage to Industry City buildings on 36th St between 2nd and 3rd Aves; ~$21M FEMA/city resiliency (drainage, flood barriers, storm sewers, elevated substation at IC; barriers protecting 1,200 linear ft of BAT waterfront); BAT in a mapped flood zone. → §8.5, Planning Fiber Where the Harbour Has Come In.

### Local news / hyperlocal on Sunset Park fiber-installation contractors 2026 — EMPTY (none retrieved).

### Local licensing / permits / technical
- Silo sources reused: LPC exterior-only rule; site statement low-voltage <50 V no DOB permit; NEC 770 OFNR/OFNP; FOA pulling-tension/figure-8/bend-radius guidance. National Register vs LPC statement ("listing generally does not restrict private owners using private funds") is general knowledge, framed on page as general guidance, not legal advice — FLAG.

### Pricing used (Brooklyn 1.00× — copied verbatim from fiber-optic-installation-brooklyn.html; no new prices)
$35/termination; $40/strand OTDR; $350 MM drop; $400 SM drop; $4,500–$7,000 12-strand OM4; $8,000–$15,000+ 24-strand OS2; from $2,400 second telecom room; $195/hr 3-hr min ($585). Arithmetic only: Starter $800 = 2 × $400; worked examples $1,320 (24 × $35 + 12 × $40) and $700 (2 × $350).

### Images (11) — permanent image rule; Drive folder empty (per main run), CompanyCam not connected
Reused from images/low-voltage/ (5) and images/network/ (6), cropped to remove faces, shirt phone numbers and logos, converted to WebP: lv brooklyn-fiber-fusion-splice → fiber-optic-installation-sunset-park-fusion-splicer-closeup (hero, eager); lv brooklyn-fiber-splice-tray → splice-bench-fiber-panel; lv bronx-hero-warehouse-cable-tray → warehouse-tray-lift; lv nassau-county-riser-conduit-pull → block-wall-conduit-pull; lv nassau-county-exterior-enclosure-install → brick-wall-enclosure; net bronx-network-drop-conduit-emt-riser → emt-conduit-sweep-feed; net long-island-idf-riser-cable-bundle → corridor-riser-bundle; net bronx-network-rack-cleanup-before-after → closet-before-after (uncropped, no people); net nyc-core-drill-conduit-rough-in → masonry-core-drill; net bronx-fluke-dsx-certification-pass → rack-link-tester; net bronx-finished-network-rack-firewall-ups → finished-rack-elevation. Library photos look AI-rendered — needs Anwar's review. Note: sibling fiber pages currently carry 20 `aess-fiber-optic-installation-*` figures each (commit cce0a6ac/93994347) and fail the 11-figure check; those 20 also look AI-rendered with visible faces, so they were not used here.

### Keyword plan (Sunset Park page)
Service: fiber optic installation Sunset Park, loft fiber backbone, campus suite fiber, unit-to-unit fiber, storefront fiber, rowhouse fiber riser, fusion splicing, OTDR testing. Problem: suite far from meet-me room, copper 100 m limit along block-long floors, inherited unlabelled tenant fiber, flat-slab ceilings with no grid, atrium/rail-track crossings, provider cables on historic facades, rear extensions, waterfront flooding. Technology: OS2, OM4, OFNR/OFNP, armoured, bend-insensitive SM, innerduct, wall enclosures, SFPs. Industry: food production, fabrication/makerspaces, media/events, climate start-ups, offices/showrooms, avenue retail/restaurants, small landlords. Geographic: Sunset Park, Industry City, Brooklyn Army Terminal, Bush Terminal/MADE, Liberty View/850 Third Ave, Third Ave/Gowanus Expressway, Fifth Ave, Eighth Ave Chinatown, 44th/47th–48th/50th/54th–59th St historic districts; Greenwood Heights, Windsor Terrace, Borough Park, Bay Ridge, Gowanus, Red Hook.

### Question register additions — fiber-optic-installation-sunset-park-brooklyn-ny
§9 Questions Answered:
- Our campus offers a dark-fiber connection from its meet-me room to our suite — when is that enough, and when should we pull our own strands?
- Should our server closet move into the campus data centre rather than stay in our suite?
- Our floor has flat concrete slabs with flared column capitals and no ceiling grid — how is fiber supported along it?
- How do you pull fiber several hundred feet down a factory corridor without overstressing the cable?
- Can fiber cross an open atrium or light court between two wings of the same building?
- Disused rail tracks run through our building's ground floor — can fiber conduit follow or cross them?
- Most of Sunset Park is on the National Register of Historic Places — does that listing limit where fiber can be mounted on our building?
- Our shop's back room is a later one-storey extension with its own flat roof — how does fiber get from the front of the building into it?
§17 FAQ:
- Do you also cover Greenwood Heights, Windsor Terrace, Borough Park and Bay Ridge around Sunset Park?
- Can a tenant on the NYCEDC-managed waterfront campuses hire you, and whose rules apply?
- Why might two Sunset Park quotes for runs of similar length differ so much in price?
- Our campus has one street address for several buildings — what location details does a quote need?
- How long does a small storefront fiber job usually take?
- If we may move to a bigger unit elsewhere on the campus in two years, which fiber type keeps our options open?
- Can work be scheduled around weekend markets and events held in our campus courtyard?
- Does a big electrical substation or switchgear room near our unit interfere with fiber?
Other question headings: Fiber Down Somewhere in Sunset Park? · Sunset Park Link Dark Right Now?
Closest in meaning to existing register entries (please judge): NYCEDC-campus FAQ vs Navy Yard "Do you work directly for BNYDC, or only for tenants?"; substation FAQ vs Port Morris "Can the fiber equipment share the main electrical room…?"; courtyard-events FAQ vs Chelsea "Mondays when galleries are closed"; quote-variance FAQ vs Fordham "Why does a quote … list so much more cable than the distance we measured?"


## Astoria, Queens — local research (2026-10-17 batch, fiber-optic-installation-astoria-queens-ny)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources already in this file are reused where noted. Facts that appear on other silos' Astoria pages (sonos/soundbar/cat6-repair/smart-lock) were re-fetched for this page, not copied.
Page thesis: in Astoria the gatekeeper is a small owner (18.5% homeownership; two-families, 3–4-family houses, walk-ups, storefront-and-apartment buildings) — so fiber is a small, owner-controlled plant sized in drops, not storeys: one sealed carrier entry, a passive cellar enclosure, a labelled single-mode pair per apartment and per storefront, carrier-neutral, with a one-page drawing; exceptions covered separately (Kaufman Arts District production businesses, Steinway factory/industrial north, Halletts Point towers + NYCHA Astoria Houses). Distinct from LIC (building-while-occupied), Jamaica (groundwater), Flushing (condo slices).

### Reddit (local) — Firecrawl search excerpts only (threads not opened)
- `site:reddit.com astoria internet building wiring fios spectrum landlord` · Firecrawl search ·
  - https://www.reddit.com/r/astoria/comments/1iimex5/what_is_the_worst_internet_provider_in_astoria/ — "the key is your landlord or co-op board has to let them wire the place up." → §5 para 2.
  - https://www.reddit.com/r/astoria/comments/1p4sn8v/what_do_you_do_for_internet/ — "I'm stuck with Spectrum because my landlord won't allow wiring for another provider." → §5 para 2.
  - https://www.reddit.com/r/astoria/comments/pzy3u2/can_i_ask_ll_to_wire_our_building_for_a_better_isp/ — ISP can run cable with LL's permission "as long as the conduit into the building supports it." → §5 para 2.
  - https://www.reddit.com/r/astoria/comments/1lvsgmm/wifi_options_in_astoria/ — "If the building doesn't have FiOS then you can't have FiOS." → §10.5 H3 1.
  - https://www.reddit.com/r/astoria/comments/gs3sz9/rcn_might_have_just_won_over_a_customer_for_life/ — landlord said building has Fios but online "only shows the basement and top floor" → §10.5 H3 1.
  - https://www.reddit.com/r/astoria/comments/1huccbp/ and /133xmx6/ — similar landlord-approval excerpts. Not used.
- `reddit r/astoria fiber internet building Fios not available landlord` · WebSearch → community.verizon.com thread 1591094 redirects to Verizon support (community sunset). EMPTY (not accessible).

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
- §10.5 reality check reuses silo sources (quoted as published): streamlinetelecom.com "$1-6 per linear foot" (H3 2); ringandping.com "$1,500 to $6,000" (H3 3); unio.digital "$300 to $800 for each fiber drop" (H3 4); T-Mobile "can take up to 4 hours" / AT&T "four to six hours" (H3 5); Quantum Fiber multifamily 30/30/40–60 days (H3 6, paraphrased, not quoted); HPD broadband guidance — FCC ban on exclusive agreements and sale-leaseback of inside wiring (H3 7 and §8.5). H3 7 heading is stated on page as an assumption, not a quotation. Angi/HomeAdvisor/Fixr: no page returned (silo finding) — stated on page.

### Housing / demographics
- `Furman Center Astoria neighborhood profile housing units owner occupied buildings 1-4 units` · WebSearch → https://www.furmancenter.org/neighborhoods/astoria/ (WebFetch): QN CD1 labelled "Astoria"; 2024: population 198,608; housing units 99,819; homeownership 18.5% vs 32.7% citywide; rental vacancy 3.4%; median rent $2,160. Building-type split not on page → §5 para 1, §5.5 table. (Note: CD1 includes part of LIC.)
- `Queens Community District 1 profile building types percent units in buildings 1-2 family walk-up elevator NYC planning` · WebSearch → https://www.nyc.gov/assets/planning/download/pdf/data-maps/nyc-population/census2000/demo_cd_qn.pdf (WebFetch): only total units (80,506 in 2000). Units-in-structure / year-built shares for Astoria: EMPTY. Page describes building types qualitatively.
- `Astoria Queens housing stock two-family rowhouses brick 1920s walk-up apartment buildings Ditmars Steinway history` · WebSearch → https://www.cityneighborhoods.nyc/ditmars-steinway (WebFetch): prewar apartment buildings + modest brick rowhouses and detached homes; early-20th-c. two-storey brick rowhouses, apartment buildings and corner shops south of Ditmars Blvd; Ditmars Blvd civic/commercial spine (bakeries, markets, cafés interwar); Henry Steinway bought 400+ acres in 1870, Steinway Village company town; Italian/Greek/Irish families → §5 para 1, §7 intro + cards, street-by-street (Ditmars–Steinway), §8 Ditmars card.

### Commercial corridors
- `Steinway Street Astoria business improvement district Steinway Astoria Partnership blocks businesses Little Egypt` · WebSearch → https://www.nyc.gov/assets/sbs/downloads/pdf/neighborhoods/Astoria.pdf (WebFetch, SBS Avenue NYC Commercial District Needs Assessment, Sept 2022–June 2023, with Central Astoria LDC + Queens EDC): 1,450 storefronts on 6 corridors — Steinway St 477 (12% vacant), Broadway 342 (10%), 30th Ave 238 (6%), Ditmars 175 (9%), Astoria Blvd 120 (17%), 36th Ave 98 (7%); 288 merchant surveys: 64% rent, 6% own; 69% have a website; no broadband data → §5.5 table, §8 intro + cards, street-by-street.
- Same query → https://qns.com/2023/11/city-announces-12-million-redesign-of-steinway-street-in-astoria-to-boost-business-increase-pedestrian-safety/ (WebFetch, Nov 22 2023): $12M SEED-funded DOT redesign, Steinway St between 30th and 34th Aves; Steinway Astoria Partnership (Marie Torniali) → street-by-street (Steinway Street).
- Same query → https://en.wikipedia.org/wiki/Steinway_Street (WebFetch): 2.4 mi; south of Grand Central Pkwy "major commercial district", primary part of Steinway Astoria Partnership BID → §8 Steinway card. "Little Egypt" not confirmed → not used.

### Landmarks / institutions
- `Kaufman Astoria Studios history 1920 Paramount soundstages 35th Avenue` · WebSearch → https://movingimage.org/feature/the-astoria-studio/ (WebFetch): opened 1920 by Famous Players-Lasky (later Paramount); Paramount left 1932; Army 1942 (Signal Corps Photographic Center, 1942–1970); 1980 management awarded to George S. Kaufman; name KAS from 1982; Stage K 40,000 sq ft 2010; backlot 2013; two more stages 2019 → 12 stages; original building at Pierce St & Sixth Ave = 35th Ave & 35th St; MoMI 36-01 35th Ave, opened 1988, renamed 2005 → §13 card, Studio Blocks section.
- `Museum of the Moving Image 2011 expansion Leeser Architecture 97,000 square feet Astoria` · WebSearch → https://www.nyc.gov/html/film/html/news_2011/010111_museum_moving_image11.shtml (WebFetch): reopened Jan 13/15 2011; nearly doubled to 97,700 sq ft; $67M; Thomas Leeser → §13 card.
- `Kaufman Arts District Astoria designated 2014 ...` · WebSearch → https://www.dnainfo.com/new-york/20140327/astoria/queens-getting-first-official-arts-district-astoria (WebFetch, Mar 27 2014): first arts district in Queens, via City Council; Steinway St to 31st St, 34th to 37th Ave; KAS, MoMI, Frank Sinatra School of the Arts, Queens Council on the Arts → §8 card, street-by-street, Studio Blocks section.
- `Steinway & Sons factory Astoria Queens 19th Avenue built 1870s history` · WebSearch → https://www.timeout.com/newyork/things-to-do/5-things-you-didnt-know-about-nycs-steinway-sons-piano-factory (WebFetch): 19th Ave & Steinway Place; on site "since the 1870s"/"1880s" (article inconsistent); ~225 unionized workers; 1,300 pianos/yr; 11 months per piano → §13 card (attributed to Time Out; date of article not confirmed).
  - Same query → https://queenseagle.com/all/how-some-of-the-worlds-best-pianos-were-built-in-queens (WebFetch): William Steinway bought Astoria farmland early 1870s; company town (school, firehouse, post office); hand-built pianos → §7 intro.
- `Steinway Mansion Astoria 1858 landmark Benjamin Pike 41st Street` · WebSearch → https://en.wikipedia.org/wiki/Steinway_Mansion (WebFetch): built 1857–58 by Benjamin Pike Jr.; 18-33 41st St; bought by William Steinway 1870; NYC Landmark Feb 15 1967 (body text says 1966 — 1967 used, per infobox/LPC report); NRHP Sept 8 1983 → §13 card, §8.5 landmark callout.
- `Hell Gate Bridge 1917 Astoria Park Triborough RFK Bridge 1936 Astoria Park pool history nycgovparks` · WebSearch → https://en.wikipedia.org/wiki/Astoria_Park (WebFetch): 59.96 acres; Hell Gate Bridge opened 1917 (Amtrak NEC); Triborough opened July 11 1936; pool opened July 2 1936, largest of 11 WPA pools of 1936 → §13 card.
- `Bohemian Hall` (from Astoria search results) · WebFetch https://www.bohemianhall.com/about: society formed 1892; cornerstone Oct 1 1910; outdoor bar/park finished 1919; 29-19 24th Ave → §13 card.
- `BMT Astoria Line elevated 31st Street opened 1917 Ditmars Boulevard station N W` · WebSearch → https://en.wikipedia.org/wiki/BMT_Astoria_Line (WebFetch): elevated over 31st St Ditmars Blvd–39th Ave; opened Feb 1 1917; N all times, W weekdays; 2017–19 Enhanced Station Initiative renovations → §5.5, §7 intro, street-by-street (31st St).
  - https://en.wikipedia.org/wiki/Astoria%E2%80%93Ditmars_Boulevard_station (WebFetch): above 31st St between 23rd Ave and Ditmars; opened Feb 1 1917; 3,309,906 riders 2024; renovated 2018–19 ($22M programme) → §5.5, §13 card.
- `Socrates Sculpture Park founded 1986 ...` · WebSearch → https://en.wikipedia.org/wiki/Socrates_Sculpture_Park (WebFetch): 1986, Mark di Suvero, 32-01 Vernon Blvd (LIC address), former landfill → §13 "we also serve" line only.
- `Astoria ferry landing Hallets Point NYC Ferry route Astoria opened 2017` · WebSearch → https://www.dnainfo.com/new-york/20170829/astoria/nyc-ferry-astoria-route-launch-aug-29 (WebFetch): launched Aug 29 2017; landing 3-10 Astoria Blvd next to Astoria Houses → §13 "we also serve" line.

### Waterfront / new construction / public housing
- `Halletts Point Durst Astoria towers units Astoria Houses NYCHA` · WebSearch → https://qns.com/2023/11/durst-organization-tops-out-construction-647-unit-mixed-use-complex/ (WebFetch via redirect from queenspost.com): 20 & 30 Halletts Point Rd, 647 units, 27 and 32 storeys, topped out Oct 26 2023; phase 1 at 10 Halletts Point Rd completed 2019; ~2,000 units across three buildings; affordable building 3-24 27th Ave with 163 homes; Durst investment in Astoria Houses heating plant/public spaces → §5.5, §7 card, Hallets Point section.
- `Astoria Houses NYCHA 1951 buildings apartments Hallets Point peninsula` · WebSearch → https://en.wikipedia.org/wiki/Astoria_Houses (WebFetch): completed Nov 1951; 22 buildings, 6–7 storeys; 26.86 acres; 2,601 residents; $88M FEMA-funded resiliency work from 2016 → §7 card, Hallets Point section.
- `Astoria Cove 4-34 26th Avenue towers units waterfront Astoria` · WebSearch → https://www.newyorkyimby.com/?p=1952250 (WebFetch, May 5 2024): Astoria Cove master plan, Fogarty Finger, 469 apartments + ~14,500 sq ft commercial in four buildings west of 9th St → Hallets Point section.
- Lot-level FEMA/flood-zone data for the peninsula: not researched → page tells owners to check the city flood hazard map; EMPTY.

### Power / outages
- `Astoria Generating Station Ravenswood power plants northwest Queens share of city electricity peaker` · WebSearch → https://citylimits.org/2023/08/15/citys-largest-power-plant-nears-milestone-in-renewable-energy-push/ (WebFetch): Ravenswood ("Big Allis") opened 1963; ~20% of NYC electricity; bordered by Astoria, Ravenswood and Queensbridge Houses; owner Rise Light and Power; plan to retire 1960 steam units for offshore wind/solar via underground cables → §5.5, Power section. Astoria Generating Station (20th Ave) facts: not fetched → not used.
- `2006 Queens blackout Astoria Long Island City network customers days Con Edison` · WebSearch → https://en.wikipedia.org/wiki/2006_Queens_blackout (WebFetch): began July 17 2006 during heat wave; Astoria, LIC, Sunnyside, Woodside; 174,000 people; Con Ed first estimated 1,600 customers, revised tenfold (counts a building as one customer); 10 of 22 feeders failed → Power section.
  - https://www.baruch.cuny.edu/nycdata/disasters/blackouts-queens.html (WebFetch): July 17–25 2006, eight days, est. 175,000 people; LIC network → Power section ("about eight days").

### Not used (checked)
- `City of Yes basement apartments legalization ...` · WebSearch → nyc.gov HPD release (Local Law 126 of 2024 ATR pilot, 1–2 family homes, flood-prone areas excluded) + https://www.thecity.nyc/2024/04/29/basement-apartments-legalization-queens/ (WebFetch): Queens CD1 (Astoria) NOT in the pilot (only QN CD2). Basement-apartment question dropped.
- `NYC Mesh Astoria rooftop node` · WebSearch → no Astoria-specific page fetched. Not used.
- `Verizon Fios Astoria buildings expansion ...` · WebSearch → corporate/press items only, nothing Astoria-specific. EMPTY.
- Local news (Queens Chronicle / QNS / Patch / Astoria Post) on fiber installation contractors in Astoria 2026: EMPTY (none retrieved).

### Pricing used (existing AESS prices only — copied from fiber-optic-installation-queens, no new prices)
- $447 single-mode drop, $391 multimode drop (Queens configurator), $37/termination, $42/strand OTDR, $4,725–$7,350 12-strand OM4, $8,400–$15,750+ 24-strand OS2, from $2,520 second telecom room, $195/hr 3-hr min ($585). Packages shown as sums: Starter 3 × $447 = $1,341; Standard 6 × $447 + 6 × $42 = $2,934; Premium = 24-strand OS2 line $8,400–$15,750+. Carries the logged Queens CONFLICT ($391/$447 configurator drops vs §9 1.05× = $368/$420).

### Images (11) — permanent image rule; Drive folder `AESS Website Photos/Fiber Optic Installation` empty (main run), CompanyCam not connected
images: 11 reused from images/low-voltage/ (6) and images/network/ (5), each cropped to remove faces, shirt/cap phone numbers, a readable cable-map sheet, a label printer and a "123 Main Street" directory sign. Note: images/fiber-optic-installation/ now also holds 20 `aess-fiber-optic-installation-*` photos (commit cce0a6ac) that are on every other fiber page; not used here per the batch instruction (and check_page allows exactly 11 figures).
| File (images/fiber-optic-installation/) | Source | Shows |
|---|---|---|
| fiber-optic-installation-astoria-splicer-bench-sc-rack.webp | low-voltage/low-voltage-installation-brooklyn-fiber-splice-tray.jpg | gloved hands at fusion splicer, SC rack, cleaver, strippers, IPA |
| fiber-optic-installation-astoria-fusion-splice-ready-screen.webp | low-voltage/low-voltage-installation-brooklyn-fiber-fusion-splice.jpg | splicer screen READY, jumper tray, IPA, cleaver |
| fiber-optic-installation-astoria-riser-bundle-corridor-ceiling.webp | network/network-installation-long-island-idf-riser-cable-bundle.webp | blue copper bundle lifted to corridor ceiling |
| fiber-optic-installation-astoria-conduit-pull-box-block-wall.webp | low-voltage/low-voltage-installation-nassau-county-riser-conduit-pull.jpg | cable out of pull box on EMT, block wall |
| fiber-optic-installation-astoria-core-drill-block-wall-entry.webp | network/network-installation-bronx-core-drill-cmu-wall-penetration.webp | rotary hammer coring block wall |
| fiber-optic-installation-astoria-exterior-enclosure-brick-conduit.webp | low-voltage/low-voltage-installation-nassau-county-exterior-enclosure-install.jpg | outdoor enclosure on brick with conduits |
| fiber-optic-installation-astoria-patch-cord-label-marker.webp | network/network-installation-bronx-cable-labeling-port-map.webp | hands labelling patch cord at numbered panels |
| fiber-optic-installation-astoria-rack-ups-battery-closet.webp | network/network-installation-bronx-finished-network-rack-firewall-ups.webp | rack with switches, firewall, UPS |
| fiber-optic-installation-astoria-tone-trace-wall-opening.webp | low-voltage/low-voltage-installation-dutchess-county-08-tone-generator-trace.jpg | tone probe at wall opening, rack |
| fiber-optic-installation-astoria-lobby-entry-panel-wiring.webp | low-voltage/low-voltage-installation-long-island-lobby-video-intercom.jpg | hands at video entry panel, tiled wall |
| fiber-optic-installation-astoria-emt-conduit-sweep-pull.webp | network/network-installation-bronx-network-drop-conduit-emt-riser.webp | cable through EMT sweep, "NETWORK DROP CONDUIT" sign |
Review note: library photos look AI-rendered (uniform branding); only 2 of 11 show fiber specifically — the rest are captioned as copper/pathway/power/labelling scenes.

### Keyword plan (Astoria page)
Service: fiber optic installation Astoria, owner fiber plant, small-building fiber, sealed carrier entry, cellar fiber enclosure, apartment fiber drops, fusion splicing, OTDR testing. Problem: landlord won't allow another provider, building not wired for Fios, cables on the facade/roof, shared internet in a two-family, unlabelled provider jacks, roof cell-site cable, crawlspace entry, blackout resilience. Technology: OS2 single-mode, bend-tolerant indoor cable, OFNR/OFNP, lockable enclosures, apartment outlets, conduit/raceway, SFP/media converters. Industry: small landlords, two- to four-family owners, walk-up owners, storefront/restaurant tenants, studio/post-production businesses, developers. Geographic: Astoria, Ditmars–Steinway, Astoria Heights, Old Astoria, Hallets Point, Kaufman Arts District, Steinway Street, 30th Avenue, Broadway, Ditmars Boulevard, 31st Street, 36th Avenue, Astoria Boulevard.

### Question register additions
fiber-optic-installation-astoria-queens-ny
§9 Questions Answered (and other question headings):
- Astoria Building Offline Since This Morning? (repair capture heading)
- A tenant has asked us to let a second internet provider into our building — what should a small landlord require before saying yes?
- We live downstairs in our two-family house and rent out the upstairs — can both households share one fiber line, or should each have its own?
- We renovate our apartments one at a time as tenants move out — can fiber be added the same way, or does the whole building have to be done at once?
- A tenant who moved out left a provider's fiber box and jack on the apartment wall — who owns it, and can the next tenant use it?
- We manage our own building and aren't technical — once owner fiber is in, what are we actually responsible for?
- A wireless carrier leases space on our roof — does the fiber running up to its antennas change anything in our own plan?
- Our older frame house near Astoria Park has a crawlspace instead of a full cellar — where should fiber come into the building?
- Want a Price Per Apartment Before You Decide? (CTA heading)
§17 FAQ:
- Do you take fiber work in Ditmars–Steinway, Astoria Heights, Old Astoria and out on the Hallets Point peninsula?
- Can your crew work alongside the handyman or super who already looks after our building?
- Can the same visit fix a tenant's dead Ethernet jack or a damaged cable inside one apartment?
- While you're on the roof, can you take down old satellite dishes and the coax that fed them?
- Can you work from a lockbox code or a spare key while we're at our own jobs?
- Can the owner fiber enclosure go on the same cellar wall as the electric meters?
De-dup notes: checked against all 33 fiber pages incl. batch-mates Hudson Square and Sunset Park (check_page mechanical + read by meaning). Deliberately avoided: Queens "provider offered to wire at no charge" (my Q is a tenant-initiated provider request and installation conditions), Queens elevated-7 vibration/EMI (el covered in prose only), Brooklyn "one fiber feed for every apartment in a walk-up", Orange "stop every provider drilling through the brick" and "two adjoining buildings", Stapleton "phone/cable lines through the building next door", Ulster "power cut / generator" (power covered in prose + table), St George "Wi-Fi fades on stairs" and "labelled per apartment", Flushing "unit numbers vs names", Port Morris/Hunts Point "what a tenant can take along", Bronx "laundry room"/"gas meters", NYC "closeout documentation"/"DOB permit", Manhattan "smallest job". Closest calls for a human read: my handyman/super FAQ vs Bronx "Do we need an electrician as well as you?" (coordination vs licensing); my lockbox FAQ vs Orange "landlord lives outside New York — approvals" (site access vs approvals); my satellite-dish FAQ vs Staten Island "reuse the old satellite-dish cable route" (removal vs reuse).

## Williamsburg, Brooklyn — local research (2026-10-17 batch, fiber-optic-installation-williamsburg-brooklyn-ny; includes this page's question-register additions)

Up-link /fiber-optic-installation-brooklyn · direct line (347) 934-8335 · GBP Brooklyn (1282 Troy Ave, #brooklyn) · Brooklyn base pricing 1.00×, lines copied verbatim from fiber-optic-installation-brooklyn.html.
Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: mcp__Firecrawl__firecrawl_search / firecrawl_scrape. Shell curl blocked. "Carried" = fetched by an earlier run (research/cat6-repair.md or research/soundbar-installation.md Williamsburg sections) and not re-fetched.

**Thesis:** Williamsburg keeps its old buildings and builds new structure inside them (Domino Refinery glass insert in a landmarked brick shell), on top of them (Wythe Hotel rooftop addition, Moore Street one-storey to five-storey vertical expansions), beside them (2005-rezoning towers next to a median-1910 walk-up stock) and through them (Loft Law legalisation fire walls). Fiber is easy; the seam between old and new structure is the job — where to cross it, where the main room goes, enclosure on each side, documented crossing. Supporting thread: the rebuilt Canarsie (L train) tunnel put new cables on accessible wall racks instead of encasing them — keep building fiber reachable. Distinct from DUMBO (brick/timber + historic district + bridge vibration), Downtown Brooklyn (vertical ownership in towers), Navy Yard (gated campus, one landlord), Port Morris (change of use).

### Research matrix — local facts
| # | Exact query | Platform | URL | Finding | Page + section |
|---|---|---|---|---|---|
| W1 | `Refinery at Domino office building opened tenants square feet glass box inside brick shell` | Firecrawl search → scrape | https://www.twotreesny.com/about-us/press/at-the-domino-sugar-refinery-a-glass-egg-in-a-brick-shell (Two Trees reprint of NYT, Feb 12 2023) | ~60% of US sugar passed through the refinery in early 1900s; landmarked brick shell hollowed, roof removed; 15-storey glass structure inside, 30-ft glass dome penthouse; "roughly 10- to 12-foot gap" (Lisa Switkin); "practically a machine wrapped in brick", "Every floor was different", "ship within a bottle", façade braced from exterior towers (Al Henriquez); "insert a brand-new building within the existing building" (Ruchika Modi, PAU); ground floor public passage Kent Ave → park; refinery fully commercial; 325 Kent, One South First, Ten Grand Street office open; 3,000 apts + 600,000 sf office, completion then slated 2027; 11-acre site sold 2012 | §5 ¶1–2, §5.5, The Seam, Built Inside, §8 Kent Ave card, §13 Refinery card, §9 Q1 |
| W2 | same | Firecrawl search (excerpts) | https://nypost.com/2023/10/02/the-refinery-at-domino-is-nycs-most-stunning-office-space/ ; Gothamist FB post | glass set back from outer walls; 460,000 sf office (Gothamist excerpt) | background; reopening 2023 (with ArchDaily ref in W5) |
| W3 | `Williamsburg Brooklyn fiber internet buildings provider Brooklyn Fiber OR "NYC Mesh" Williamsburg` | Firecrawl search | https://www.reddit.com/r/williamsburg/comments/1goylhd/internet_providers/ (excerpt only) | "I'm moving into a new apartment on Graham Ave and it seems like the best internet providers are Verizon or Spectrum." | §5 ¶4 |
| W4 | same | Firecrawl scrape | https://bkfiber.com/services/williamsburg/ (redirected to /check-availability) | "Many buildings activate same day"; expands "block by block" | §10.5 H3 2 |
| W5 | same | Firecrawl scrape | https://www.buildinghealthx.com/services/internet-providers/williamsburg | Median Williamsburg apt building built 1910; 46.9% of apts pre-1940; 35.7% in ≤5 floors; 2,035 buildings / 31,792 apts (3+ units), Sept 2026 data; "Order 1 to 2 weeks before move-in"; "For converted warehouses without Fios, T-Mobile 5G Home" (search excerpt) | §5 ¶1, §5.5, §10.5 H3 3–4 |
| W6 | same | Firecrawl search (excerpt) | https://www.broadbandsearch.net/service/new-york/brooklyn | fiber concentrated in DUMBO, Williamsburg, Downtown Brooklyn (also carried from Downtown Brooklyn research) | §5 ¶3, §10.5 H3 1 |
| W7 | `South Williamsburg Hasidic community housing ...` | Firecrawl scrape | https://en.wikipedia.org/wiki/South_Williamsburg,_Brooklyn | Domino opened 1856, largest refinery; Pfizer plant to 2007; Satmar: Joel Teitelbaum arrived 1947, Yetev Lev 1948; 1950s–60s rebuilt housing, yeshivas, mikvahs, synagogues; UJO 1966, new HQ 498 Bedford Ave groundbreaking (Jewish Press Aug 29 2025); Los Sures/Southside United HDFC 1972, 1975 first Brooklyn CBO managing city-owned property; El Puente 1982, Academy 1993; Furman Center: W'burg/Greenpoint most rapidly gentrifying 1990–2014; rezoning May 11 2005, 175 blocks; UJA 2023: 36,000 Jewish adults, 32,000 children, 21,000 households; Lee Ave spine; Graham Ave "Avenue of Puerto Rico"; Williamsburgh Library first Carnegie library in Brooklyn, cornerstone 1903, 26,000 sf, landmark 1999; Moore Street Market 1941, 110 Moore St; BQE bisects | §5 ¶2, §8 Lee Ave & Graham/Moore cards, §13 library card, South Williamsburg section |
| W8 | `Austin Nichols warehouse Kent Avenue Williamsburg ...` | Firecrawl search (Wikipedia + MCNY blog + CityRealty excerpts) | https://en.wikipedia.org/wiki/Austin,_Nichols_and_Company_Warehouse ; https://blog.mcny.org/2012/05/15/the-struggle-to-save-the-austin-nichols-and-co-warehouse/ ; https://www.cityrealty.com/nyc/williamsburg/austin-nichols-house-184-kent-avenue/46551 | Cass Gilbert, built 1914–15, reinforced concrete, 179×440 ft; LPC designated Sept 2005, Council overturned Nov 2005; NRHP 2007 (less restrictive); JMH completed 338 rentals 2010; retail condo 16,000 sf storefronts + 55,000 sf 3-level garage; 2004 proposal to BSA for rooftop addition / 256 condos (MCNY); 7 floors, 338 apts (CityRealty); "largest importing and manufacturing wholesale grocery business in the world" (MCNY) | §5 ¶1–2, §5.5, §7 card, Built On Top ¶1, Street Level, §8.5 landmarks bullet, §10.5 H3 7, §13 card |
| W9 | `Williamsburg Brooklyn rooftop addition vertical enlargement ...` → `"Moore Street" Williamsburg vertical expansion YIMBY stories added` | Firecrawl search → scrape | https://newyorkyimby.com/2025/03/vertical-expansion-project-begins-at-103-105-107-moore-street-in-williamsburg-brooklyn.html | Mar 25 2025: 103-105 & 107 Moore St, one-storey commercial structures gutted, structurally reinforced, expanded to five-storey mixed-use, 8 rental units each, cellar levels; between Humboldt St and Avenue of Puerto Rico; same architect/developer at 96 Moore St | Hero, §5 ¶2, Built On Top ¶2, §9 Q4 |
| W10 | (related article on W9 page) | Firecrawl scrape | https://newyorkyimby.com/2026/10/timberburg-completes-construction-at-179-north-10th-street-in-williamsburg-brooklyn.html | Oct 15 2026: Timberburg, 179 N 10th St between Bedford & Driggs, 7 storeys, 23 condos, mass timber + CLT, Passive House, triple glazing, ERV, Butterfly intercom, EV chargers | Built New ¶1, §9 Q5–Q6 context |
| W11 | (related article) | Firecrawl scrape | https://newyorkyimby.com/2026/10/1262-unit-two-skyscraper-development-rises-at-280-kent-avenue-in-williamsburg-brooklyn.html | Oct 12 2026: 280 Kent Ave, twin 50-storey, 591 ft, 1,262 units, Building B of Domino masterplan, reinforced-concrete superstructure + glass, completion posted fall 2030; reader comment attributing to "Google AI" that the refinery is "90% leased by tech, media & AI startups" (unverified) | §5.5, Built New, §13 Domino Park card, §10.5 H3 5 |
| W12 | `Canarsie Tunnel L train rehabilitation cable racks bench wall Sandy salt water damage cables` | Firecrawl search (excerpts incl. full MTA release text) | https://apps.cio.ny.gov/apps/mediaContact/public/view.cfm?parm=B43E5B26-... (MTA, Mar 17 2017); https://www.hillintl.com/project/canarsie-tunnel/ (excerpt) | 7 million gallons salt water (Hill); damage to tracks, signals, power/signal/communication cables, cable ducts, bench walls along 7,100-ft flooded section (MTA); original plan rebuild duct banks/bench walls, closure | §5.5, Under the River ¶1 |
| W13 | `L train 2019 plan cables racks side of tunnel instead of bench wall Cornell Columbia engineers Canarsie Tunnel` | Firecrawl search → scrape | https://www.newswise.com/articles/cornell-engineers-help-get-nyc-s-l-train-back-on-track (Cornell, Apr 29 2020); https://abc7ny.com/post/why-the-l-train-tunnel-opening-is-so-important-now/6130846/ (excerpt) | Completed Apr 27 2020, six months early, $100M under budget; FRP encasement; cable racking system; fiber-optic monitoring; cables decoupled from walls "so they can remain accessible, instead of buried in cement" | Under the River ¶2–3, §9 Q8 |
| W14 | `Bedford Avenue Williamsburg retail Apple store Whole Foods ...` | Firecrawl search → scrape | https://www.brooklynvegan.com/williamsburgs-whole-foods-and-apple-stores-both-opening-next-week/ (Jul 21 2016) | Whole Foods Bedford & N 4th opens Tue July 26 (site previously Flame Cut Steel); 20,000-sf Apple store, over half the block N 3rd–N 4th, east side, formerly King's Pharmacy and the Bagel Store, opens July 30 | §8 Bedford card, Street Level ¶1 |
| W15 | `Wythe Hotel 1901 cooperage rooftop addition ...` | Firecrawl search (excerpts) | https://ma.com/wythe-hotel.html ; https://archello.com/project/wythe-hotel | 1901 cooperage converted; contemporary addition built on roof of restored brick warehouse (floor count not used) | Hero, §5 ¶2, Built On Top ¶1, §13 card, Street Level ¶4 |
| W16 | `cross-laminated timber floor penetration firestopping cables ...` | Firecrawl search (excerpts) | https://www.woodworks.org/resources/holes-and-penetrations-in-mass-timber-floor-and-roof-panels/ ; https://www.stifirestop.com/news/cross-laminated-timber-clt-and-firestopping (2019) | through-penetrations protected by approved firestop system tested to ASTM E814 / UL 1479; STI: cables "pretty easily handled with firestop sealant and mineral wool"; CLT listings still being developed; longer screws beyond char layer | Built New ¶2, §9 Q5, §10.5 H3 6, §8.5 firestop bullet |

Carried (not re-fetched): Loft Law / Loft Board (nyc.gov/site/loftboard/about — 1982 MDL Art. 7-C, IMDs, 2010/2013/2015/2019 amendments, IBZ exception incl. Greenpoint/Williamsburg) — research/cat6-repair.md W1 → Lofts Made Legal, §9 Q7. Domino landmark 2007 filter/pan/finishing house; Williamsburgh Savings Bank 175 Broadway at Driggs, 1875, exterior 1966, interior 1996, Weylin 2014; Wythe 1901 cooperage by Theobald Engelhardt, textile factory, hotel 2012; Williamsburg Houses landmark 2003; Domino Park June 2018, quarter mile; NFPA 13 sprinkler-pipe support — research/cat6-repair.md W4–W7, W11, W16 and research/soundbar-installation.md Williamsburg §6 → §8, §8.5, §13. Silo technical sources (OFNR/OFNP, FOA, NEC abandoned cable, sub-50 V DOB statement) — research/fiber-optic-installation.md silo section.

### Sources EMPTY
- Google PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG — EMPTY (not accessible in build env). §10.5 states on the page that the AI Overview could not be viewed and works from published claims (W4, W5, W6, W11 comment, W16, W8).
- Yelp 1–3★ — EMPTY (not accessible in build env; not searched separately, silo Yelp search returned nothing usable).
- Local Reddit — excerpt only (W3); reddit.com not scrapable by Firecrawl. Williamsburg-specific fiber/backbone threads: EMPTY.
- Local news / hyperlocal on fiber installation in Williamsburg specifically: EMPTY (news used is construction/landmark news: YIMBY, BrooklynVegan, NYT via Two Trees).
- Kent Avenue lot-level flood zone: not researched; page makes no flood-zone claim.

### Pricing used (Brooklyn 1.00× — verbatim from fiber-optic-installation-brooklyn.html)
$35/termination; $40/strand OTDR; $350 MM drop; $400 SM drop; $4,500–$7,000 12-strand OM4; $8,000–$15,000+ 24-strand OS2 / building-to-building; from $2,400 second telecom room; $195/hr 3-hr min ($585). Packages are sums only: Starter $800 (2 × $400, same as parent's starter); Standard $4,500–$7,000; Premium from $6,900 ($4,500 + $2,400). Worked example $660 (12 × $35 + 6 × $40).

### Images (11) — permanent image rule
Drive "AESS Website Photos/Fiber Optic Installation" empty (main run 17:35Z); CompanyCam not connected. Copied/cropped (Pillow, WebP q80) into images/fiber-optic-installation/fiber-optic-installation-williamsburg-*.webp; every crop removes faces, shirt/cap phone numbers (844-386-7238 / 800-486-0943) and readable documents (cable map sheet, IDF floor plan):
- fusion-splicer-at-rack ← images/low-voltage/low-voltage-installation-brooklyn-fiber-fusion-splice.jpg (hero, eager)
- strands-into-splicer-sc-panel ← images/low-voltage/low-voltage-installation-brooklyn-fiber-splice-tray.jpg
- overhead-tray-dome-camera ← images/low-voltage/low-voltage-installation-brooklyn-05-warehouse-cable-tray-highbay.jpg
- core-drill-block-wall ← images/network/network-installation-brooklyn-core-drill-cmu-wall-penetration.webp (same frame also used by concurrent Parkchester page)
- fish-cable-wall-opening ← images/network/network-installation-brooklyn-retrofit-wall-fish-data-drop.webp
- labeling-patch-cords ← images/network/network-installation-brooklyn-cable-labeling-port-map.webp
- j-hook-bundles-open-ceiling ← images/network/network-installation-brooklyn-jhook-ceiling-pathway-bundles.webp
- emt-conduit-cable-pull ← images/network/network-installation-bronx-network-drop-conduit-emt-riser.webp
- stud-wall-patch-panel ← images/low-voltage/low-voltage-installation-brooklyn-idf-patch-panel-build.jpg
- tracing-cable-at-wall-hole ← images/low-voltage/low-voltage-installation-nyc-tone-generator-trace.jpg
- rack-switch-setup-laptop ← images/low-voltage/low-voltage-installation-nyc-rack-switch-config.jpg
Alt/title/caption describe only what is visible; several show blue copper (Cat6) cable, said as "blue cable" — not called fiber. Page FAQ states the photos are illustrative library images, not Williamsburg jobs. Library looks AI-rendered — Anwar to review.
DAILY-LOG note: images: 11 reused from images/low-voltage/ (6) and images/network/ (5) (no real fiber-optic-installation photos yet).

### Keyword plan (five layers)
Service: fiber optic installation Williamsburg, fiber backbone, riser into rooftop addition, fusion splicing, OTDR testing, backbone upgrade. Problem: seam between old and new structure, main-room placement, vertical expansion entry, CLT firestopping, Passive House envelope, Loft Law legalisation, buried vs accessible cable. Technology: OS2, OM4, armoured indoor/outdoor, flexible conduit, splice enclosures, listed firestop, airtight grommets, J-hooks/tray. Industry: adaptive-reuse offices, converted-warehouse condos, loft buildings, hotels/venues, Bedford Ave retail, housing nonprofits, community institutions, developers. Geographic: Williamsburg, Kent Ave, Bedford Ave, Wythe Ave, Broadway, Lee Ave, Graham Ave, Grand St, Moore St, North 10th St; East/South Williamsburg, Greenpoint, Bushwick, Clinton Hill, Bedford-Stuyvesant.

### Masked similarity (my script: geo-masked per tools/check_page.mask, digits stripped, p/li/td/h2/h3/figcaption ≥8 words, difflib ratio after 3-gram prefilter, constants excluded)
Final 173,887 B / 12,853 rendered words. Max content-block similarity 0.619 (vs St. George: pricing "access" bullet). Only blocks ≥0.65: pricing-table label "24-strand OS2 backbone or building-to-building link" (copied price line, exempt) and the blueprint-fixed H2 "What AI Gets Wrong About Fiber Optic Installation in [Area]" (0.894 vs DUMBO, required pattern). Whole-page 5-gram Jaccard ≤0.023 vs every sibling (incl. Maspeth and Parkchester drafts on disk).

## Question register — fiber-optic-installation-williamsburg-brooklyn-ny
§9 Questions Answered (H3, under non-question H2 clusters "New structure inside old walls" / "Floors added on top" / "New construction" / "Lofts, upkeep and portfolios"):
- Our office floors are a new structure set inside an old brick shell, with an open gap between the two — how does fiber get from the street entry to our suite?
- Should the main network room sit in the old part of the building or the new part?
- A glass addition was built on the roof of our converted factory — how does a backbone climb from the original floors into the new ones?
- Our one-storey building is being raised to five storeys — will the internet entry and the cellar it comes into still work for the bigger building?
- Our building is cross-laminated timber — how are the holes for cable through a timber floor sealed?
- Our new building was built to Passive House standards — will a new fiber entry spoil the airtight envelope?
- Our loft building is still going through Loft Board legalisation — should we wait to put in fiber until the fire-safety work is finished?
- Is it better to hide our new fiber inside walls or leave it on supports where it can be reached later?
- Our housing organisation runs older walk-ups on different blocks — should every building get the same fiber layout?
§17 FAQ (= FAQPage schema, 7):
- Do you also work in Greenpoint, East Williamsburg, Bushwick and Clinton Hill?
- Can noisy work and cutovers be scheduled around Shabbat and Jewish holidays in South Williamsburg buildings?
- Does a mass-timber building need a different type of fiber cable from a concrete one?
- Can a terrace or balcony outside a floor-to-ceiling glass wall get a wired access point?
- Can our fiber share a conduit with the building's fire-alarm wiring?
- Will you cut a chase into the old brick to hide fiber?
- Are the photos on this page from your Williamsburg jobs?
Other headings: none end in "?" (repair headings are statements; §10.5 H3s are claims).

De-dup notes (by meaning against the register and every fiber page on disk, incl. Maspeth/Parkchester drafts): dropped "sidewalk shed / scaffold" (exists on a sibling), "expansion joint between structures" (sibling: expansion joint in warehouse floor — handled in prose only), "leave a pathway for the next addition" (sibling: extend fiber after an addition / developer conduit size), "1915 concrete warehouse slabs" (St. George concrete factory Q), condo-board/commercial-condo approval (Flushing/Downtown), vibration from the elevated J/M/Z (DUMBO/Orange), crossing the BQE (Rockland county-road Q), Yiddish labels (Port Morris Spanish labels). Closest calls for a human read: Q3 (rooftop addition riser) vs sibling "If we build an addition later, can the fiber be extended without starting over?" (mine = existing addition route, theirs = future extension); Q9 (same standard across scattered walk-ups) vs Rockland "start with one building on a split campus"; Q5 (CLT firestop) vs DUMBO "heavy timber beams without fastening into the wood"; FAQ fire-alarm conduit vs Orange "fiber alongside an alarm panel in the same closet".

## Maspeth, Queens — local research (2026-10-17 batch, fiber-optic-installation-maspeth-queens-ny)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources above are reused where noted (AI reality-check claims: streamlinetelecom $1–6/ft; thenetworkinstallers/FBA $18/ft underground median; AT&T 4–6 h and T-Mobile up to 4 h residential installs; Quantum Fiber multifamily 30/30/40–60-day stages; Atlantech 15-month wait; r/AskNYC "Its on the ISP to wire your building/apartment"; Verizon NYC fiber-footage release). Merge this section into research/fiber-optic-installation.md and append the question list below to the register.

**Page thesis (distinct from Hunts Point's refrigerated 24-hour food hub and Port Morris's second-use loft buildings):** Maspeth is built around wheels, not foot traffic. It has no subway station; its industrial lowland now holds two-storey delivery stations with truck ramps, van decks and multi-level docks (55-15/56-19 Grand Ave, 55-90 48th St) beside contractors' and trucking yards, concrete and trade businesses on assembled lots, the MTA's Grand Avenue Bus Depot, and a village of 1910–1930 attached brick two-family houses with driveways and rear garages next to freight tracks. Fiber here is planned along the vehicle path — ramps, decks, dock levels, rolling gates, gravel yards, weighbridges, curb frontages — and kept out of the vehicles' way.

### 1. Reddit (local)
- Query: `reddit Maspeth internet Fios Spectrum building` · Firecrawl search (excerpts only; reddit not scraped) → no Maspeth-specific thread; results were r/AskNYC/r/Upperwestside generic Fios threads (r/AskNYC 1uhxwu9 excerpt: "Verizon tends to want 70% of households in a building to request FIOS before they will wire a building" — commenter claim, not used as fact). Maspeth-specific internet complaints: EMPTY.
- Query: `site:reddit.com Maspeth` · Firecrawl search (excerpts only):
  - https://www.reddit.com/r/newyorkcity/comments/1n0mhtr/ibx_stop_by_stop_maspeth_has_smalltown_charm_in/ — excerpt: "Maspeth is an okay Queens neighborhood but is hard to access without a car so lots of traffic." → §5 The Neighborhood para 3 (quoted as a commenter's view).
  - https://www.reddit.com/r/SunnysideQueens/comments/1f1v1rc/do_you_want_to_move_to_maspeth/ — excerpt: "just on the other side of an incredibly 24/7 industrial area (Less than a block)". → §5 para 3.
  - https://www.reddit.com/r/Bushwick/comments/1f1uyix/do_you_bwant_to_move_to_maspeth/ — excerpt: "4bed 2 family 2800 sq ft with parking and a back yard … if you're living there you're prolly driving". → §5 para 3, "The Village Behind the Warehouses" section.
  - https://www.reddit.com/r/movingtoNYC/comments/1st5uh9/bushwick_vs_maspeth/ — excerpt: "quiet, residential, and industrial neighborhood". Not quoted (political remark in same excerpt not used).

### 2–5, 8. Google PAA / PASF / Answer the Public / AI Overview / Bing & DuckDuckGo — EMPTY (not accessible in build env)
Substituted for §10.5 with the silo-level published claims listed above plus local availability claims:
- Query: `Maspeth Queens warehouse internet fiber business` · Firecrawl search →
  - https://broadbandnow.com/New-York/Maspeth — excerpt: "Fiber internet is 88.4% available in Maspeth. Cable is available to 97.5%". → §10.5 H3 1.
  - https://ispreports.org/business-internet-providers-maspeth-queens-ny/ — excerpt: "Verizon Business offers Fiber service to 97.6% of Maspeth homes". → §10.5 H3 1 (two sites, two different percentages; quoted as claims).
  - https://www.broadbandsearch.net/service/new-york/maspeth — excerpt: "EarthLink Fiber covers 94.61% | Spectrum covers 100% | Verizon covers 98.5%". → §10.5 H3 1.
  - https://business.naturalwireless.com/fiber-internet-queens-ny/ — excerpt: "Quick Installation -- Within 5 Days". → §10.5 H3 7 (quoted as a carrier's marketing claim for a wireless circuit, not building fiber).
  - https://www.qchron.com/editions/queenswide/maspeth-a-possible-spot-for-amazon/article_24567c1d-7684-53ff-a178-2c4918d7ed3e.html — excerpt: Amazon considering 55-15 Grand Ave. → background only.

### 6/7. Landmarks, streets, building stock, use cases
- Query: `Maspeth Industrial Business Zone businesses jobs number` · WebSearch → https://cityneighborhoods.nyc/maspeth (WebFetch): boundaries BQE (N), LIRR freight lines (E), Eliot Ave (SE), Metropolitan Ave (S), Newtown Creek/Brooklyn (W); Grand Street (now Grand Ave) built early 1800s; Maspeth Plank Road Company 1854; attached brick homes many built 1910–1930, brick two-family homes; 58th Ave, 69th St, 58th Rd housing streets; Holy Cross RC Church est. 1848 (German parish), St. Stanislaus Kostka 1891 (Polish); Newtown Creek banks once held refineries, glue works, copper smelters, tanneries, chemical plants; name from Mespeatches ("at the bad water place"). → §5 paras 1–2, §7 Architecture, "Village" section, §13 landmarks.
- Same query → https://www.qchron.com/news/central/west-maspeth-property-owners-form-local-development-corp/article_e4c652d3-d47a-587c-91bb-87223c7fe0b8.html (WebFetch; article undated, references suggest c. 2004): Maspeth Industrial Commercial Owners' LDC, ~300 parcels, 30 members; Phil Galasso (Galasso Trucking) quotes: "It is probably the most valuable industrial property in this city…", "Quite often, we get reports of theft of hundreds of thousands of dollars worth of equipment."; streets often unmarked, sidewalks rare, lighting spotty; eastern portion has a private sewer system; Maurice/Maspeth Ave five-way intersection; rutted rail crossing at Maspeth Ave and Rust St; some businesses not complying with sidewalk-construction rules; UPS facility on 56th Road. → §5 para 4 (theft quote, dated "two decades ago"), §8.5 compliance (sidewalk strip), Q&A sidewalk question, Q&A power-cut cameras question. Article age stated on page.
- Query: `Maspeth Queens wikipedia population rowhouses Grand Avenue Holy Cross` · WebSearch → https://en.wikipedia.org/wiki/Maspeth,_Queens (WebFetch): 2020 NTA population 43,257; ZIP 11378; Community District 5; 104th Precinct at 64-02 Catalpa Ave; 43rd–58th Streets incl. former Furman Island mostly industrial lowland; Phelps Dodge 1920–1983; LIRR Montauk Branch freight, Bushwick Branch (NY&A), Bay Ridge Branch freight-only separating Maspeth from Elmhurst/Middle Village; no subway stations, nearest M at Middle Village–Metropolitan Ave; bus routes B57, Q18, Q39, Q47, Q54, Q58, Q59, Q67 etc.; Grand Avenue Bus Depot; FDNY Squad 288/Hazmat 1 at 56-29 68th St (1914), lost 19 firefighters on 9/11; Maspeth Town Hall community center 72nd St; Maspeth Federal Savings; Queens Public Library Maspeth branch 69-70 Grand Ave; Ridgewood Gardens co-ops on 65th Place; housing mostly single/multi-family. → §5.5 facts table, §5, §13 landmarks, "Village" section, FAQ coverage answer.
- Query: `Maspeth Town Hall landmark 72nd Street history` · WebSearch → https://forgotten-ny.com/?p=9116 (WebFetch; 2002 article with 2006–2011 updates): Maspeth Town Hall, 72nd St north of Grand Ave, built 1897 (not 1802 as its sign states), later police stationhouse then public school; Mathews Company row houses between Grand Ave, 79th St and Calamus Ave built 1930; Metropolitan Oval, 60th St north of 60th Ave, soccer since 1925; Queens County Hotel on Grand Ave built 1851; Grand Street Bridge opened Feb 5, 1903; Rust Street tunnel under LIRR; horsecar barn lost to LIE early 1950s. → §13 landmarks (Town Hall, Metropolitan Oval), §7 Architecture (1930 Mathews rows), "Village" section.
- Query: `Maspeth Plank Road Newtown Creek historic site Kosciuszko Bridge Maspeth` · WebSearch → https://www.newtowncreekalliance.org/?p=3964 (WebFetch): Plank Road street end at 58th Road on Newtown Creek, DSNY Queens Garage 5 next door; remnants of Maspeth Toll Bridge Co. plank road; restored from 2013 by Newtown Creek Alliance; US Concrete (neighbour) donated materials in 2014; SPLASH! event Oct 2024. → §13 landmarks, §8 commercial (concrete, sanitation neighbours), Q&A cement-dust question context.
- Query: `Kosciuszko Bridge new span opened 2017 2019 Maspeth Greenpoint Newtown Creek` · WebSearch → https://en.wikipedia.org/wiki/Kosciuszko_Bridge (WebFetch): eastbound span opened Apr 27, 2017; westbound Aug 29, 2019; $554.77M design-build contract (May 23, 2014), largest single NYSDOT contract; old 1939 approaches demolished Oct 1, 2017 with 944 charges; links Greenpoint and Maspeth; 624-ft main span. → §5.5 facts, §13 landmarks.
- Query: `Elmhurst Park gas tanks site opened park Grand Avenue 57th Avenue` · WebSearch → https://en.wikipedia.org/wiki/Elmhurst_Park (WebFetch): bounded by Grand Ave (N), 57th Ave/LIE (S), CSX Fremont Secondary (W), 80th St (E); 6.22 acres; Elmhurst gas tanks (Newtown Holder Station) built 1910–1921, dismantled 1996–2001; park opened May 24, 2011. → §13 landmarks (stated as on the Maspeth–Elmhurst edge), IBX context.

### Industrial: delivery stations, warehouses, depot
- Query: `Maspeth industrial last-mile warehouse trucks 2025 Queens Chronicle` · WebSearch →
  - https://www.dcvelocity.com/articles/53407-realterm-acquires-final-mile-warehouse-in-queens-new-york (WebFetch): 50-35 56th Road, 130,000 sq ft on 5.2 acres, 15 loading positions, excess parking, announced Jan 7, 2022; Realterm quote "Maspeth is an outstanding warehouse submarket" and Maspeth ranks first for drive time; >11 million people within 15 miles. → §5 para 2, §8 commercial (56th Road), §5.5.
  - https://therealdeal.com/new-york/2021/09/22/everwest-acquired-a-maspeth-warehouse-from-wharton-for-57m/ (WebFetch): 55-30 46th Street, 70,500 sq ft on 2.9 acres, $57.25M, multi-tenant (food distributors per headline), delivery-truck parking; FedEx Ground filed in July 2021 for a two-storey facility. → §8 commercial (46th Street), §7 Architecture ("multi-tenant older warehouse").
  - https://therealdeal.com/2020/12/03/lba-lands-316m-loan-for-amazon-warehouse-in-maspeth (WebFetch): 55-15 Grand Ave, described as 770,000 sq ft five-storey vertical warehouse with truck loading on the first three floors; $316M JPMorgan loans; RXR/LBA bought 54-15, 55-15, 56-19 Grand Ave parcels Jan 2018 for $72M; Amazon lease. → §5 para 2 (stated as reported in 2020), §7.
- Query: `55-15 Grand Avenue Maspeth multi-story warehouse Amazon completed opened` · WebSearch →
  - https://suffolk.com/project/55-15-grand-avenue-queens-last-mile-distribution-facility/ (WebFetch): builder's page: about 1.1 million sq ft; two-storey Class-A logistics centre with three levels of parking above; 15 loading docks; parking for 600+ employees and fleet vehicles incl. EV charging and van launches; Cobiax voided slab, cast-in-place concrete, precast panels; reached TCO (date not stated); owner RXR; architect BL Companies; leased by Amazon. → §5 para 2, §7 card "Stacked delivery stations", §9 Q (deck Wi-Fi, cast-in conduit), worked-example section. Discrepancy with 2018/2020 press (770,000 sq ft, five storeys) stated on page.
  - https://www.pincusco.com/rxr-lba-logistics-permitted-for-770k-sf-grand-logistics-center-for-amazon-in-maspeth/ and https://newyorkyimby.com/?p=1851839 (WebFetch, Dec 1 2018): 56-19 Grand Ave "Grand Logistics Center" 770,000 sq ft, truck ramps to loading docks on multiple levels, nine interior dock positions, 21-ft clear height, 6.5 acres existing fleet parking. → §7, §5.5.
- Query: `FedEx Ground Maspeth two-story facility 159,000 square feet` · WebSearch →
  - https://informedinfrastructure.com/post/skanska-builds-distribution-facility-in-maspeth-new-york-usa-for-usd-110m-about-sek-930m (WebFetch): Skanska $110M contract for FedEx Ground; two-storey, 28,000 m²; demolition of three unoccupied buildings; ground-level offices; precast access ramp to second-level employee parking; 45 truck loading bays; May 2021 – Sept 2023 schedule. → §5.5, §7, §8.
  - https://junipercivic.com/juniper-berry/article/berry-bits-skanska-building-huge-distribution-facility-in-maspeth (WebFetch, Sept 11 2021): address 55-90 48th Street; 301,000 sq ft. → §8 corridor (48th Street). (Pincus 159K sq ft filing headline seen in search only, not used.)
- Query: `UPS Maspeth facility 56th Road largest hub Queens` · WebSearch → https://www.bisnow.com/news/new-york/industrial/ups-lease-red-hook-est4te-four-maspeth-queens-80975 (WebFetch, Oct 31 2017): UPS long-term triple-net lease on a 475K sq ft Maspeth warehouse, formerly Duane Reade's distribution centre. → §5 para 2, §5.5.
- Query: `Grand Avenue Bus Depot Maspeth MTA depot opened compressed natural gas` · WebSearch → https://amny.com/transit/plugged-in-mta-debuts-new-electric-bus-charging-hub-at-queens-depot/embed (WebFetch, May 14 2024): Grand Avenue Bus Depot, 17 overhead pantograph chargers, 60 electric buses, 566 kW chargers; $188M for 200 more overhead chargers at Grand Avenue and four other depots. → §5.5, §13 landmarks. (Page makes no claim that AESS works for the MTA.)
- Query: `Maspeth truck route bypass Grand Avenue trucks residential streets DOT` · WebSearch → https://www.nyc.gov:443/html/dot/html/motorist/maspeth.shtml (WebFetch): Maspeth Bypass and Intersection Normalization study (area bounded by Grand Ave, LIE, BQE); 2007 truck-route study named Grand Ave high priority; one-way conversions from Oct 2011 (Maurice Ave northbound Maspeth Ave–55th Dr; 59th St southbound Maurice–56th Ave; 58th St southbound 55th Dr–Maspeth Ave); five-leg intersection Maurice Ave/58th St/Maspeth Ave. → §8 corridors, §5 para 4, process step on arrival, FAQ day-of prep.
- Query: `Maspeth equipment theft construction yard cargo theft Queens 104th precinct trucks stolen` · WebSearch → results were general Queens police blotter pages (queenspost tag pages, 2018 Juniper precinct report, Fox News backhoe ATM story). Not opened in detail; not used. EMPTY for a recent Maspeth-specific yard-theft figure.

### 9/10. Local news / hyperlocal
- Query: `Interborough Express Maspeth Grand Avenue station 2026 update environmental review` · WebSearch → https://ny1.com/nyc/queens/news/2026/09/17/homeowners-protest-construction-of-interborough-express-station-in-queens (WebFetch, Sept 17 2026): planned IBX station on Grand Ave near 74th St beside Elmhurst Park; residents protested at MTA pop-up; CSX tracks ~80 ft from one resident's back wall, IBX would add two tracks west of CSX; quote "The property is already shifting"; design and environmental review could finish by end of 2027; 18 stations Jackson Heights–Sunset Park. (Article's "$5 million" cost figure looks like an error — not used.) → §5 para 5, "Village" section (freight vibration, prose only; no Q because Orange/Queens already ask about trains).
- Query: `Maspeth Avenue flooding Ida 2021 Maspeth basements sewer` · WebSearch → https://queenspost.com/progress-made-on-long-awaited-sewer-upgrades-in-maspeth-and-woodside-city-ddc-reports (WebFetch, Apr 27 2023): DDC $101M sewer/water-main project on 70th Street; low-lying Maspeth/Woodside flooding since at least 2007; 2020 sinkhole; completion expected spring 2024; COMET Civic Association quote "nightmare". → "Village" section (cellar equipment placement, prose only).
- Query: `Newtown Creek Superfund Maspeth Creek cleanup 2025 EPA` · WebSearch → https://epa.gov/newsreleases/epa-will-take-early-action-clean-east-branch-portion-newtown-creek-superfund-site (WebFetch, Jan 17 2025): EPA interim early action for the East Branch — dredging, capping, in-place stabilisation, sealed bulkheads; nearly $250M; contaminants PAHs, PCBs, dioxins, heavy metals. → §5.5 facts, Q&A historic-fill trench question (stated generally; no claim about any specific lot).
- Query: `Maspeth news 2026 warehouse OR industrial OR Grand Avenue qns` · WebSearch → listings and deal pages (commercialcafe, loopnet, connectcre; Commercial Observer Mar 2022 Davis Companies $51M Maspeth warehouse). Not opened; not used.

### 11. Yelp 1–3★ — EMPTY (not accessible in build env)
No Maspeth-specific low-voltage/fiber contractor reviews searched successfully.

### Local licensing / permits
- Reused silo-wide sources (DOB low-voltage permit scope, NEC 770 riser/plenum ratings, TIA bend radius). No Maspeth-specific permit source found. The page's sidewalk/curb-cut and historic-fill statements are general practice (FLAGGED for Anwar's review), with the city agency named (DOT for sidewalk/street work) and "not legal advice" wording.

### Prices
Copied verbatim from fiber-optic-installation-queens.html (published Queens lines): $37 termination; $42 OTDR/strand; $391 multimode drop; $447 single-mode drop; $4,725–$7,350 12-strand OM4 backbone; $8,400–$15,750+ 24-strand OS2; from $2,520 second telecom room; $195/hr, 3-hr minimum ($585). Packages are sums of those lines only. Parent's open $391/$447 configurator-vs-1.05× caveat carries over.

### Question register additions — fiber-optic-installation-maspeth-queens-ny
§9 Questions Answered:
- Should conduit for fiber be cast into a new delivery station's ramp and deck slabs while they are being poured, or added afterwards on the surface?
- Snowmelt and road salt run off our rooftop van deck — how do you keep that water out of the fiber enclosures on the level below?
- Handheld scanners keep dropping on our covered van deck during the morning load-out — can fiber fix the Wi-Fi up there?
- We are a delivery contractor working out of a large carrier's station — can we bring in our own fiber, or is the building's network off limits?
- A delivery station is busiest overnight and at dawn — when is the quiet window for a fiber cutover?
- Our yard gate rolls open and shut all day — how does fiber reach the keypad and camera on the moving side without being torn?
- How will our loader operator know where buried fiber runs in a gravel yard that gets regraded every spring?
- Our truck scale at the gate has to report weights to the office — can fiber carry that link?
- Can fiber be run along a chain-link fence or a perimeter wall instead of being buried across the yard?
- Cement dust and diesel soot settle on everything in our yard — what does that do to fiber connectors, and how are they protected?
- If someone cuts the power to our yard at night, how do the cameras keep recording over the fiber?
- Our yard office is a converted shipping container — can network equipment survive inside it through a Queens summer?
- The city may make us build a sidewalk along our yard frontage — should buried fiber stay out of that strip?
- Our lot sits on old industrial fill near Newtown Creek — can we still trench for fiber conduit?
- Our attached brick house gets its internet through the neighbour's cellar — can we have our own service entrance instead?
§17 FAQ:
- Do you also work in Middle Village, Ridgewood, Woodside and Elmhurst, next door to Maspeth?
- Who does the trenching and patches the asphalt on a yard job, and is that in your price?
- Our dispatch office runs a wall of screens tracking every van — does that need fiber, or is the internet line enough?
- We own the shop and live in the two-family house next door — can both be done on one visit and one invoice?
- Can fiber carry the feed from a licence-plate camera at our truck gate?
- Our burglar alarm still reports over an old copper phone line — can it move onto fiber?
- Our site is still under construction — can fiber work be scheduled around the concrete pours?
- What should we have ready on the morning your crew arrives at a yard or warehouse?
- How long do outdoor fiber boxes last on a pole or wall in full sun?
Other headings (no "?"): "Maspeth Yard or Dock Link Down" (repair capture), "Send Us the Site Plan and the Truck Route" (CTA), "Maspeth Dock, Deck or Yard Dark Right Now" (final repair).

De-dup notes: checked by meaning against the 722 question headings/FAQ items on all 31 fiber pages on disk (16 area/hub + 15 neighbourhood). Deliberately avoided: EV/electric-van chargers (Port Morris, Downtown Brooklyn, Stapleton, Hunts Point), truck-lane overhead crossing and dock-row switches (Hunts Point), ground-floor fleet to upstairs bay (Port Morris), yard light poles (Bloomfield), trains/vibration (Orange, Queens, DUMBO), hold-off-for-road-project (Orange), parking-lot depth/repaving/boring (Long Island), contractor trailer (Staten Island), gatehouse (Long Island), Spanish labels (Port Morris), rowhouse entry point (Chelsea), shared-wall neighbour warning (St. George), lease-end take-along (Port Morris), tenant vanilla box (Stapleton), two buildings we own (NYC hub), scrap theft (Port Morris). Concurrent batch drafts (Williamsburg, Parkchester, Astoria and others) were not on disk at build time — main run should re-check against them.

## Parkchester, Bronx — local research (2026-10-17 batch, fiber-optic-installation-parkchester-bronx-ny)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources (NEC/OFNR, DOB sub-50 V, pricing) reused from the silo section, not repeated here.

**Thesis:** Parkchester repeats itself — 171 brick buildings in two heights (8 and 13 storeys) built 1938–42 to one plan — so fiber is engineered once on a pilot building, written down as an owner-held standard (route, parts list, M-floor labelling key, two height variants) and copied; cost and risk sit where the pattern breaks (shops built into residential bases on Metropolitan Ave, the five garages, the grounds between entrances, and the unrelated buildings around the complex on Starling/Castle Hill/E Tremont). Distinct from the parent Bronx page (big multi-building site plan: which building hosts the main room / phasing / tunnels) and from Flushing (condo ownership slices).

### Reddit (local)
- Query: `reddit Parkchester internet Fios apartment wiring` · Firecrawl web search (excerpts only; reddit threads not opened). No Parkchester-specific thread returned. Generic results only:
  - https://www.reddit.com/r/Fios/comments/1nzl5q6/nyc_apartment_installations_can_they_be_hidden/ — excerpt: "You would have to get your own installer to prepare spaces for where the equipment and wiring will go." → §10.5 H3 5.
  - https://www.reddit.com/r/Fios/comments/1oz9xcz/1_gb_fios_installion_in_a_5thfloor_apt_bronx_nyc/ — title only. Not used.
- Local Parkchester Reddit: EMPTY (no thread found).

### PAA / PASF / Answer the Public / Google AI Overview / Bing & DDG — EMPTY (not accessible in build env)
Substitute claims for §10.5 (quoted from published pages):
- Engadget 2008 (below) "giving some 12,271 apartments in 171 buildings access to a fiber-based alternative" → H3 1.
- https://www.verizon.com/home/internet/near-me/new-york-ny/ (silo source, excerpt) "Verizon coordinates with the property manager/owner to wire and install the service"; same page table "Optimum (Fiber) | Up to 8 Gbps … Limited boroughs (Bronx and Brooklyn)" → H3 2, H3 3. (Parent Bronx page also quotes the first line — paragraph text rewritten.)
- Query `Parkchester Bronx internet Fios Optimum Spectrum building wiring condominium residents` · Firecrawl → https://ispreports.org/internet-service-providers-parkchester-bronx-ny/ excerpt "Compare 5 internet providers in Parkchester, Bronx, NY. Check availability by address" → H3 4.
- https://www.angi.com/articles/fiber-optic-cable-installation-cost.htm (silo source) "$4,500 … $1,500 to $7,000" → H3 6.
- Query `Parkchester South Condominium alteration agreement contractor insurance certificate unit owner renovation rules` · Firecrawl → https://www.myhomeus.com/blog/2026-nyc-condo-alteration-agreement-what-unit-owners-need-to-know/ (excerpt): 2026 NYC Bar standardized condo alteration agreement; "Pre-vetting all contractors to ensure they meet the new $2M–$10M liability thresholds"; also says requirements vary and form is not a legal mandate → H3 7.
- Same query → https://www.facebook.com/groups/641918253488666/posts/1802334910780322/ (excerpt) "Internet Deals for Parkchester Residents … Optimum" → §5 para 3 ("Optimum markets to residents as well").

### Yelp 1–3★ — EMPTY
- Only incidental Yelp results (Macy's Parkchester 2.3★/48, Bangla Town Supermarket listing, Spectrum Co-op City) — none about cabling/fiber contractors. Not used.

### History, building stock, ownership
- Query: `Parkchester Bronx condominium North South board history Metropolitan Life 171 buildings` · Firecrawl search →
  - https://www.parkchesternyc.com/about-us/history/ (excerpt): July 1938 MetLife announcement; self-contained community; 66 acres open landscaped space; central heating plant; 51 building clusters, 171 building entrances; 129 acres, only 27% built on; Richmond H. Shreve (Empire State Building firm); shopping centre >500,000 sq ft near Hugh Grant Circle "largely integrated into the residential structures"; first Macy's branch outside Herald Square; PNC/PSC offering plans; PPC became Sponsor; NORC (PEP) programme → hero, §5 paras 1, §5.5, Where-the-Pattern-Breaks, Occupied Buildings section.
  - https://en.wikipedia.org/wiki/Parkchester,_Bronx (excerpt): built 1939–42; 171 four-sided brick buildings, 8 or 13 storeys, floors numbered M (Main) through 7 / M through 12; 13-storey buildings have dual side-by-side elevators, 8-storey one; terracotta (WPA-style, Joseph Kiselewski); Metropolitan Ave, Unionport Rd, White Plains Rd main thoroughfares; CD9; ZIP 10462 (+10460/10461); patrolled by Parkchester Department of Public Safety; Ryan Oval formerly Metropolitan Oval; surrounding area "dominated by multi-unit buildings unrelated to Parkchester complex"; Macy's branch 1941 → §5.5, §7 cards, §9 Q3, §13 card, FAQ 5, Building Systems section.
- Firecrawl scrape https://www.parkchesternorth.com/About/History : PNC "consists of 55 buildings in the northern section"; "two condominiums have separate boards and staff but work together on many common issues"; own steam plant; 1972 north conversion (per PNC); 1998 PPC bought remaining unsold apartments; renovation financed windows, expanded electrical wiring (AC), plumbing → §5 para 2, renovation section.
- Firecrawl scrape https://citylimits.org/cityviews-the-lessons-we-learned-from-saving-parkchester/ (Michael Lappin, Aug 22 2018): 12,271 apartments, 171 buildings; >40,000 inhabitants; five garages; 500,000 sq ft commercial; North converted 1978 / South 1984 (per this author); mid-1990s up to 60 plumbing breaks/day, warping casement windows, 15-amp service; 1998 purchase incl. 6,362 unsold units, 432,000 sq ft retail, five garages; renovation: replumbing, asbestos removal, >70,000 casement windows, electrical upgrade enabling AC; completed 2004–05; "all but about 20 apartments provided contractors timely access" → renovation section, Where-the-Pattern-Breaks (garages), Occupied Buildings section.
- Firecrawl scrape (pdf) https://www.parkchesternyc.com/wp-content/uploads/2018/10/Crains-Parkchester-1.pdf (Crain's, Oct 26 2015): two condominium boards and eight committees; Oval with fountain; shops along Metropolitan Ave; 1998 deal incl. five parking garages and half a million sq ft retail; $250M overhaul; 65,000 casement windows (conflicts with City Limits 70,000 — page says "the windows", no number); PSC "encompasses 130 of the complex's buildings" (conflicts with PNC 55 → counts not used) → §13 Oval card, garages paragraph.
- Conflicts NOT resolved on page: conversion dates (1972/1974/1978; 1984/1986) → page says "since the conversion" only; building counts per condominium → not stated.
- Firecrawl scrape https://www.parkchestersouth.com/Services/Facility-Services (via search excerpt): unit owners responsible for most interior repairs except common elements; common-area repairs only through the Service Department; "Private arrangements with members of staff are prohibited" → §8.5 callout 1, §10.5 H3 5, FAQ 3.

### Carriers
- Firecrawl scrape https://www.engadget.com/2008-10-21-verizon-gets-fios-tv-high-speed-internet-into-bronxs-parkches.html (Oct 21 2008): Parkchester "the largest privately owned condominium complex in the US"; FiOS TV/internet to 12,271 apartments in 171 buildings; Verizon's largest urban MDU agreement → §5 para 3, §5.5, Carriers section, §10.5 H3 1.
- https://www.nexttv.com/news/verizon-inks-fios-pact-171-building-bronx-complex-297751 — scrape returned only a newsletter wall (title/date only). Not used beyond corroborating date.

### Transit, rezoning, local news
- Query `Parkchester Macy's Bronx 2025 OR 2026 news Bronx Times` · Firecrawl → https://www.macys.com/stores/ny/bronx/parkchester_22.html (1441 Metropolitan Ave Fl 2) → §8 card, §13 card.
- Firecrawl scrape https://www.bxtimes.com/category/news/neighborhoods/parkchester/ → index of 2025–26 items (station upgrade, Wonder, Bangla Bazaar, 1848 Guerlain St permits, 1353 Castle Hill Ave senior lottery, Castle Hill Library $17M renovation title) → leads below.
- Firecrawl scrape https://www.bxtimes.com/new-accessibility-upgrades-complete-at-parkchester-6-train-station/ (Jan 9 2026): new elevators street/mezzanine/platform; station "sees 7,000 daily riders"; three flights of stairs before → §5 para 4, §8 card, §13 card.
- Firecrawl scrape https://www.bxtimes.com/wonder-popular-digital-food-hall-opens-first-location-in-the-bronx/ (Apr 27 2026): Wonder opened Apr 23 at 1498 Metropolitan Ave, 20+ cuisines → §8 card, Shopping Streets section.
- Firecrawl scrape https://www.bxtimes.com/permits-4-story-residential-building-parkchester/ (Feb 5 2025): 1848 Guerlain St, 4 storeys, 37 ft, 9 units, 6,199 sq ft, cellar, between Leland and Thieriot Aves → §7 card, §9 Q9 context, Around the Complex section.
- Firecrawl scrape https://www.bxtimes.com/our-forgotten-borough-bangla-bazaar-growth-in-the-bronx/ (Apr 10 2026): Starling Ave "Bangla Bazaar" between Castle Hill Ave and Unionport Rd; BBBA estimates ~45 storefronts, up to 80 businesses with shared spaces; grocers, restaurants, clothing, pharmacies, tax offices, driving schools; Parkchester Jame Masjid; Golden Palace Catering and Banquet Hall on Unionport Rd; spreading along 6 line to Castle Hill Ave, Zerega Ave, Westchester Square → §5.5, §8 cards, §9 Q6, §13 card, Shopping Streets section.
- Query `Bangla Bazaar Starling Avenue Parkchester Castle Hill Avenue businesses Bronx Times 2026` · Firecrawl → https://www.bxtimes.com/bangladeshi-community-chaand-raat-bronx/ (excerpt): strip "closed to traffic for the night" on Chaand Raat → FAQ 4. http://www.nycstreets.info/honorStreetc65d.html?b=BX&letter=B (excerpt): Bangla Bazaar honorary name, Starling Ave between Castle Hill Ave and Unionport Rd.
- Query `Parkchester-Van Nest Metro-North station location construction 2026 Penn Station Access` · Firecrawl → https://en.wikipedia.org/wiki/Parkchester/Van_Nest_station (excerpt: east of Unionport Rd, entrance from East Tremont Ave); https://www.mta.info/project/penn-station-access (excerpt: Nov 2025 structural steel at Parkchester-Van Nest); https://www.nyc.gov/content/planning/pages/our-work/plans/bronx/bronx-metro-north-area (excerpt: nearly 7,000 homes, 1,700 income-restricted, 10,000 jobs; increased housing in Parkchester/Van Nest and Morris Park) → §5 para 4, §8 cards, §13 card, Around the Complex, Construction Nearby.
- Firecrawl scrape https://www.thecityreporter.nyc/2026/05/15/metro-north-bronx-partial-service-mta-timeline/ (May 15 2026): hopes for 2027 partial East Bronx service dwindling; Congress members' letter raises service "by early 2029"; overall completion pushed 2027→2030 → Construction Nearby section.
- Query `Unionport Road Westchester Avenue East Tremont Avenue Parkchester Van Nest rezoning …` · Firecrawl → DCP page above; https://zap-api-production.herokuapp.com/…/240015.pdf (excerpt: ~46-block area along East Tremont Ave, White Plains Rd…). Used only as "rezoning" context.
- Query `Parkchester Department of Public Safety cameras CCTV complex security officers` · Firecrawl → https://www.instagram.com/reel/DWgYTKEEWSb/ (excerpt): "intercom SECURITY button connects directly to Parkchester Police dispatch" → Building Systems section ("a 2026 social-media post aimed at residents said…") — FLAG: social-media source only; reel date not confirmed beyond index.
- Query `Parkchester central heating steam plant cogeneration underground tunnels utilities` · Firecrawl → no Parkchester result. EMPTY. (Page makes no tunnel/steam-route claim.)
- Local news on Parkchester fiber/cabling contractors: EMPTY.
- Local licensing/permits specific to Parkchester: none beyond condominium rules above; DOB sub-50 V statement reused from silo.

### Pricing used (copied verbatim from fiber-optic-installation-bronx.html; Bronx 1.00×; no new prices)
$35/termination; $40/strand OTDR; $391 MM drop / $447 SM drop (Bronx configurator — inherits logged §9 1.00× conflict); 12-strand OM4 $4,500–$7,000; 24-strand OS2 $8,000–$15,000+; second telecom room from $2,400; $195/hr 3-hr min ($585). Packages: Starter $894 (2×$447), Standard $4,500–$7,000, Premium $8,000–$15,000+, BYOE $195/hr 3-hr min.

### Images (11) — permanent image rule; Drive folder empty (checked 17:35Z by main run), CompanyCam not connected
All cropped (Pillow) to remove faces, shirt/van phone numbers and the "123 Main Street / ABC Property Management" directory sign; saved WebP q80 ≤1600 px to images/fiber-optic-installation/.
| File | Source | What it shows |
|---|---|---|
| fiber-optic-installation-parkchester-splicer-blue-adapter-rack.webp (hero) | low-voltage/low-voltage-installation-hudson-valley-fiber-splice-tray.jpg | splicer, gloved hands, blue adapter panels, yellow jumpers, IPA |
| fiber-optic-installation-parkchester-fusion-splicer-screen-ipa.webp | low-voltage/low-voltage-installation-dutchess-county-05-fiber-fusion-splice.jpg | splicer screen, IPA bottle, cleaver, yellow jumpers |
| fiber-optic-installation-parkchester-emt-conduit-block-wall.webp | network/network-installation-queens-network-drop-conduit-emt-riser.webp | cable into EMT sweep, block wall, "network drop conduit" sign |
| fiber-optic-installation-parkchester-pull-box-cable-feed.webp | low-voltage/low-voltage-installation-queens-riser-conduit-pull.jpg | cable through riser pull box |
| fiber-optic-installation-parkchester-exterior-enclosure-brick.webp | low-voltage/low-voltage-installation-rockland-county-11-exterior-enclosure-install.jpg | outdoor enclosure, brick, conduits, drill |
| fiber-optic-installation-parkchester-lobby-intercom-panel.webp | low-voltage/low-voltage-installation-queens-lobby-video-intercom.jpg | video intercom panel on marble wall (directory sign cropped out) |
| fiber-optic-installation-parkchester-door-strike-keypad.webp | low-voltage/low-voltage-installation-queens-electric-strike-keypad.jpg | electric strike, keypad, push-to-exit |
| fiber-optic-installation-parkchester-corridor-cable-bundle.webp | network/network-installation-rockland-county-idf-riser-cable-bundle.webp | blue (copper) bundle in corridor |
| fiber-optic-installation-parkchester-rack-before-after.webp | network/network-installation-putnam-county-network-rack-cleanup-before-after.webp | rack before/after (uncropped, no people) |
| fiber-optic-installation-parkchester-core-drill-block-wall.webp | network/network-installation-putnam-county-core-drill-cmu-wall-penetration.webp | rotary hammer into block wall |
| fiber-optic-installation-parkchester-patch-panel-stud-wall.webp | low-voltage/low-voltage-installation-hudson-valley-idf-patch-panel-build.jpg | patch panel on stud wall (IDF paper sign cropped out) |
Notes: lobby intercom and electric-strike clusters had never been used on a fiber page; the other scenes recur in the library. Same-scene overlap with concurrent batch pages: patch-panel (≈ Williamsburg stud-wall-patch-panel), pull box (≈ Maspeth emt-conduit-pull-box), splicer hero (≈ Maspeth splicer-ready-screen). Library photos look AI-rendered (as flagged by earlier builders) — Anwar to confirm.

### Keyword plan (Parkchester page)
Service: fiber optic installation Parkchester, fiber backbone, building standard, pilot building survey, riser, fusion splicing, OTDR. Problem: repeated buildings wired five ways, store under apartments, garage cable damage, grounds between entrances, carrier backboard crowding, condo common elements. Technology: OS2, OM4, OFNR/OFNP, armored fiber, indoor/outdoor in duct, wall-mount enclosures, SFP/media converters. Industry: condominium complex, managing agent, retail/food hall, clinics/tax offices in converted apartments, garages, small new walk-ups. Geographic: Parkchester, Metropolitan Ave, Ryan Oval, Unionport Rd, Starling Ave/Bangla Bazaar, Westchester Ave, East Tremont Ave, Castle Hill Ave, Van Nest, Unionport, Westchester Square, Parkchester/Van Nest station.

### Question register additions — fiber-optic-installation-parkchester-bronx-ny
§9 Questions Answered:
- Parkchester's buildings were built to one plan — can a fiber design worked out in one building be copied to the rest?
- Why open up a pilot building before pricing the whole group?
- Do the eight-storey and thirteen-storey buildings need different fiber designs?
- Did the renovation of 1998 to 2005 leave sleeves or chases that new fiber can reuse?
- Our shop sits in the base of a residential building near the Oval — can its fiber stay inside the store's own ceiling?
- Two businesses split one Starling Avenue storefront — who should own the network equipment in the back?
- Verizon's equipment is already on our cellar backboard — can our own enclosure go beside it?
- Can fiber cross the landscaped grounds between two buildings without trenching the lawn?
- We're putting up a four-storey, nine-unit building off Castle Hill Avenue — is a fiber riser worth it for so few apartments?
- A ground-floor apartment is being converted into a doctor's or tax office — what network wiring is the old apartment missing?
(Repair/CTA headings carry no "?": "Parkchester Store or Office Lost Its Connection", "Send Us One Building and We'll Price the Rest", "Parkchester Link Down Right Now".)
§17 FAQ:
- Do you also work in Castle Hill, Van Nest, Unionport and Westchester Square around Parkchester?
- Can you hand us the building standard as a written document our own super or later contractors can follow?
- Can the building's porters or handymen help our crew to keep the cost down?
- Starling Avenue is closed to traffic for Chaand Raat and other street events — do you schedule around them?
- Can exterior conduit be fixed to a facade that carries the complex's terracotta ornament?
- Once the standard is agreed, how long does each additional building take?
- Does repeating one design lower the price of each building?
- If one building in a group is served by a different provider than its neighbours, does the standard change?
- Will you keep spare enclosures and connectors that match our standard for future repairs?
- If the work pauses between buildings, is anything left exposed in the hallways?
De-dup notes (checked by meaning against all 722 question headings/FAQs on the 33 sibling files): avoided board-approval/unit-owner intents (Flushing), hallway-notice (Bronx), unloading-on-a-curb (Fordham), excavation-baseline (LIC), Spanish labels (Port Morris), phases over budget years (Bronx — mentioned in body only). Closest remaining intents for the main run to judge: Q "Verizon equipment on backboard — own enclosure beside it" vs Jamaica "move the provider's terminal out of our wet cellar" (mine = co-location, theirs = relocation); Q "pilot building" vs Rockland "start with one building on a split campus and reach the others later" (mine = survey before pricing, theirs = phasing); FAQ "pause between buildings" vs Bronx "phases over several budget years" (mine = site left safe, theirs = whether phasing is possible); Q "ground-floor apartment → office" vs Fordham change-of-use theme (body, not a question).

## New Springville, Staten Island — local research (2026-10-17 batch, fiber-optic-installation-new-springville-staten-island-ny)

Thesis: New Springville was built after the 1964 bridge for the car — the 1973 mall on a former airfield, the eight-lane Richmond Avenue strip, pad sites, strip centres, small medical/office buildings and Heartland Village two-family houses. Fiber work here is horizontal and on the ground (across parking fields, along strips, over flat roofs, house to garage), not vertical risers or wet cellars (Stapleton) or warehouses (Bloomfield).

Format: exact query · platform · URL · finding · page + section used.

### 1. Reddit (local) — EMPTY
- Query: `reddit statenisland New Springville internet Verizon Fios Optimum availability` · WebSearch → no reddit.com results (only ISP-comparison and unrelated "Springville NY 14141" pages). EMPTY. Not used.

### 2–5, 8, 11. PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
Substituted for the §10.5 Reality Check with claims published pages actually make (quoted verbatim on the page):
- Query: (silo source, re-fetched) WebFetch https://thenetworkinstallers.com/blog/fiber-optic-installation-cost/ → "the typical underground deployment costs $18.00 per foot and the typical aerial deployment costs $8.00 per foot"; "Laying fiber directly in the ground instead of installing new conduit is about 40% cheaper". → §10.5 H3 1 and H3 2.
- Query: `retail store network fiber not necessary Cat6 100 meters small business "fiber" overkill guide` · WebSearch → https://ifeeltech.com/blog/cat6-vs-fiber-business-guide (WebFetch): "No—business fiber internet does not require internal fiber cabling."; "Cat6A supports 10Gbps over the full 328-foot distance, covering most office requirements."; "Unlike Cat6A, you can't easily add drops or modify fiber runs after installation". → §10.5 H3 3, 4, 6.
- Query: `point-to-point wireless bridge cheaper than fiber between buildings "wireless bridge" business parking lot` · WebSearch → https://bridgeheadit.com/understanding-it/wireless-bridges-for-business-connectivity (WebFetch): bridges "are not affected by weather conditions or other environmental factors"; "often less expensive than running fiber optic cable"; same page later advises a weatherproof bridge if exposed to the elements. → §10.5 H3 5.
- Silo source (already in register research): https://www.t-mobile.com/home-internet/fiber/fiber-optic-installation — in-home install "can take up to 4 hours". → §10.5 H3 7.

### 6/7. Landmarks, building stock, corridors
- Query: `New Springville Staten Island neighborhood history Richmond Avenue Staten Island Mall` · WebSearch → https://en.wikipedia.org/wiki/Richmond_Avenue (WebFetch): Richmond Ave ~7.05 mi, Tennyson Dr (Eltingville) to Forest Ave (Graniteville); passes between the mall and Freshkills Park, intersects Rockland Ave/Draper Pl in New Springville, edge of Willowbrook Park; widened after the mall opened; Rockland Ave–Forest Hill Rd section is eight lanes (four each way). → §5 para 2, §8 cards, block-by-block "eight-lane stretch".
- Same search → https://en.wikipedia.org/wiki/Mid-Island,_Staten_Island (WebFetch): mall opened 1973 on a former airport site; Richmond Ave corridor became "the island's liveliest commercial strip"; farms until the 1960s; bridge 1964 spurred construction. → §5 para 2.
- Query: `Heartland Village New Springville Staten Island history townhouses built` · WebSearch → https://en.wikipedia.org/wiki/Heartland_Village,_Staten_Island (WebFetch): development within New Springville; square bounded by Richmond Ave, Rockland Ave, Richmond Hill Rd, Forest Hill Rd; construction late 1960s to early 1980s; mostly two-family houses; P.S. 69 and I.S. 72 opened 1976; bus routes on Richmond Ave. → §5, §5.5 fact 4, §7 house cards, landmarks card, block-by-block.
- Same search → https://theneighborhoods.substack.com/p/new-springville-staten-island (WebFetch): early name Karle's Neck; Springville after freshwater springs; Lemnos Greek truck farms ~WWI; Decker Farm on Richmond Hill Rd; cul-de-sacs with one/two-family homes and garages; developers built 200–300 buildings at a time after 1964; matching porticos with thin white columns; Staten Island Airport opened 1941 (closed 1964); city's first drive-in opened 1948 next door; Petticoat Lane = Rockland Ave (lore); Freshkills East Mound along Richmond Ave; Latourette Park SE border; Willowbrook Park north border. → §5 para 1, Heartland Village section, block-by-block (Petticoat Lane).
- Query: (follow-up) WebFetch https://en.wikipedia.org/wiki/New_Springville,_Staten_Island: 2020 NTA "New Springville-Willowbrook-Bulls Head-Travis" population 42,871 (+9.1% from 39,310); 33.4% renter-occupied; Yukon depot early 1980s, 380 buses; second-largest transit hub (note: mall article says third-largest — page uses the mall article's "third-largest"); LaTourette House NRHP 1982. → §5.5 facts 5 and 6, block-by-block (Yukon).
- Query: `Staten Island Mall expansion 2019 square feet food district Brookfield redevelopment plan 2025` · WebSearch → https://en.wikipedia.org/wiki/Staten_Island_Mall (WebFetch): opened August 9, 1973 with Macy's and Sears; site of Staten Island Airport (1941), sold 1955; 1,370,000 sq ft; owner GGP/Brookfield; only indoor mall in the borough; 2016–2019 expansion +242,000 sq ft incl. Food District, AMC dine-in, Dave & Buster's; Sears closed, The Container Store opened on an outparcel; third-largest transit hub after St. George and Eltingville. → §5 para 2/4, §8 mall card, landmarks card, schema mentions.
- Same search → https://commercialobserver.com/2024/10/brookfield-staten-island-mall-expansion (WebFetch): Oct 2024 filing with DCP; ~41,000 sq ft in seven one-storey retail buildings of 2,000–8,000 sq ft; removes 246 parking spaces; ULURP; anticipated opening 2030. → §5 para 4, §5.5 fact 3, §10.5 H3 2. Follow-up query `Staten Island Mall seven new retail buildings parking lot City Council approval 2025` · WebSearch → no approval article found; page says only "filed … entering land-use review". Status after 2024: EMPTY.
- Same search → https://www.nyc.gov/assets/planning/download/pdf/applicants/env-review/staten_island_mall/final_scope.pdf (WebFetch): 2655 Richmond Ave, Block 2400; 84.95-acre site bounded by Richmond Hill Rd, Marsh Ave, Platinum Ave, Richmond Ave; C4-1; parking 5,844 → 5,477 with a new three-level 1,413-space garage; Freshkills Park ~2,200 acres across Richmond Ave. → §5.5 facts 1–2, block-by-block "mall and ring road", schema.
- Query: `Decker Farm Richmond Hill Road Historic Richmond Town 1810 farm` · WebSearch → https://www.nyctourism.com/places/decker-farm (WebFetch): 435 Richmond Hill Rd, 10314; ~11 acres; one of four Historic Richmond Town sites; "said to be New York City's oldest continuously working example of its type". → landmarks card, §5 para 1, schema.
- Query: `Asbury Methodist Episcopal Church New Springville Richmond Avenue landmark 1849` · WebSearch → https://forgotten-ny.com/2024/03/ichabods-grave-new-springville/amp (WebFetch): former Asbury Methodist church (now SON Rise Charismatic Interfaith Church), Richmond Ave just south of Signs Rd opposite Willowbrook Park; walls 1849, interior remodelled 1878; Washington Cemetery first interments 1804; grave of Col. Ichabod Crane. → landmarks card, schema.
- Query: `Freshkills Park 2,200 acres East Park Richmond Avenue opening landfill closed 2001` · WebSearch → https://en.wikipedia.org/wiki/Freshkills_Park (WebFetch): ~2,200 acres; landfill 1948–2001; New Springville Greenway along Richmond Ave completed 2015; North Park Phase 1 opened Oct 15, 2023. → landmarks card, schema.
- Silo research (existing entry, Staten Island section): College of Staten Island 204-acre Willowbrook campus, largest by area in NYC. → landmarks card.

### 9/10. Local news / hyperlocal / filings
- Query: `silive New Springville Richmond Avenue new development 2025 2026 shopping center construction` · WebSearch → https://blog.marketproof.com/new-building-permit-filed-for-1358-forest-hill-rd-in-new-springville-staten-island/ (WebFetch): filed March 27, 2026; three-storey mixed-use, residential + commercial floor area. → §8 Forest Hill Road card. Also 51 Sloane Ave (Dec 31, 2023, four-storey mixed-use) and 2086 Richmond Ave, Bulls Head (Mar 17, 2025, one-storey) — read, not used on page.
- SI Advance / silive articles on New Springville fiber or broadband — none retrieved. EMPTY.

### Building stock — medical/office
- Query: `medical office building Richmond Avenue New Springville Staten Island 10314 Northwell OR RUMC OR ambulatory` · WebSearch → https://www.cityfeet.com/cont/10314-staten-island-ny/medical-offices-for-lease (WebFetch): Richmond Ave office/medical listings at 1550 (built 1996), 2066 (2009), 2555 (1977). → §8 "Richmond Avenue north" card, medical suites section (years only; no addresses or tenants named).

### Technical / practice statements (not sourced this run — written from trade practice; flagged for review)
- Lead-lined X-ray room penetrations need the shielding designer/physicist's approval (Q&A).
- PCI DSS: cable type doesn't change obligations; separation and physical access to network jacks/equipment matter (Q&A).
- Fire lanes kept passable; trench crossed in same-day sections or bored (Q&A).
- Provider owns curb pedestal and buried drop to its terminal (Q&A).
- Builder media panels as fiber landing points (Q&A).
- Roofing manufacturer warranties usually require approved roofer for penetrations (Q&A roof route).
- All-dielectric fiber needs no pool bonding; armoured cable armour grounded at entry (FAQ).
- TIA-598 jacket colour code yellow/aqua/orange/lime (FAQ).
- Outdoor cable temperature tolerance under asphalt (FAQ, no figures quoted).

### Pricing used (copied from fiber-optic-installation-staten-island.html, 1.10×; no new prices)
$39 termination · $44 OTDR/strand · $385 MM drop · $440 SM drop · $4,950–$7,700 12-strand OM4 · $8,800–$16,500+ 24-strand OS2 · from $2,640 second telecom room · $195/hr, 3-hr min ($585) · packages $880 / $4,950–$7,700 / $8,800–$16,500+.

### Images (11) — Drive folder `AESS Website Photos/Fiber Optic Installation` empty (main run 17:45Z), CompanyCam not connected; library crops
New files in images/fiber-optic-installation/ (each a re-cropped WebP of a library image not referenced by any fiber page; faces not visible):
fiber-optic-installation-new-springville-fusion-splicer-bench-below-patch-rack (from …-port-morris-fusion-splicer-bench-fiber-panel) · -sc-adapter-panels-yellow-jumpers (…-port-morris-sc-adapter-panel-yellow-jumpers) · -brick-wall-enclosure-conduit-drops (…-port-morris-brick-wall-outdoor-enclosure-conduit) · -core-bit-block-wall-entry (…-port-morris-core-bit-block-wall-penetration) · -retail-unit-open-ceiling-cable-drop (…-port-morris-shop-open-ceiling-cable-drop) · -bullet-camera-bracket-conduit-mount (…-flushing-storefront-entrance-camera-mount) · -emt-pull-box-cable-feed (…-port-morris-emt-pull-box-cable-feed) · -stud-wall-patch-panel-dressing (…-flushing-stud-wall-patch-panel-cables) · -tangled-wiring-closet-before-cleanup (…-port-morris-tangled-closet-before-cleanup) · -tone-probe-wall-jack-trace (…-flushing-tone-tracer-wall-jack-rack) · -metal-stud-fitout-ladder-cable-pull (…-fordham-bronx-metal-stud-fitout-spool).
Seven of the eleven show copper (blue) cable/pathway work; alts describe only what is visible.

### Keyword plan (New Springville page)
Service: fiber optic installation New Springville Staten Island, pad/outparcel fiber, strip-centre backbone, building-to-building fiber, fusion splicing, OTDR testing. Problem: copper 328 ft limit across lots, surge between buildings, tenant turnover, landlord approvals, fire lanes, roof routes, shielded rooms. Technology: OS2, OM4, indoor/outdoor water-blocked, armoured, Schedule 40/80 conduit, traffic-rated pull boxes, media converters/SFP. Industry: mall/retail, restaurants and banks on pads, medical/dental suites, two-family homes, townhouse/condo. Geographic: New Springville, Heartland Village, Staten Island Mall, Richmond Avenue, Forest Hill Road, Richmond Hill Road, Rockland Avenue, Travis Avenue, Bulls Head, Willowbrook, Freshkills.

### Question register additions — fiber-optic-installation-new-springville-staten-island-ny
Q&A (§9):
- Our new pad building will open before the provider has run service to it — can the store start out on a fiber connection from the main building?
- The landlord plans to put a new pad building on top of the spot where our buried fiber crosses the lot — who pays to move it?
- Plowed snow and road salt end up piled over our parking-lot handhole every winter — does that harm the fiber?
- Does trenching across our parking lot mean closing the fire lane, and who has to sign off on that?
- Our strip centre's units are joined only by a flat roof — can fiber run across the roof from one unit to another?
- Our X-ray room has lead-lined walls — can fiber pass through the shielding?
- Does running our card terminals over fiber change anything for PCI compliance?
- Our provider's line comes from a pedestal at the curb rather than a pole — who looks after the stretch from the pedestal to the house?
- Our townhouse came with a builder-installed media panel in a closet — can new fiber land there?
FAQ (§17):
- Do you take jobs in Heartland Village, Bulls Head, Travis and Willowbrook as well as around the mall?
- Our office is in a converted house on Richmond Avenue — which cable ratings apply, house or commercial?
- Can fiber be laid temporarily across a parking lot for a few weeks of seasonal events?
- Will summer heat from the blacktop damage fiber buried under a parking lot?
- Can fiber run to our backyard pool equipment without bonding or grounding problems?
- Does the colour of a fiber cable's jacket mean anything?

## Harlem, Manhattan — local research (2026-10-17 batch, fiber-optic-installation-harlem-manhattan-ny)
Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources (cost guides, AT&T install time, FBA medians, Empire City Subway, FOA, Ampcom) are reused from the silo sections above and not repeated except where the page quotes them.

Thesis: Harlem is owned and used in clusters (churches + community houses, schools/clinics/arts groups in neighbouring rowhouses, owners buying the house next door) on blocks of attached 1870s–1920s masonry, so the fiber job is joining neighbouring buildings — through party walls, along roof lines, across rear yards and gated alleys, or by carrier circuit across streets — under LPC rules, while 125th Street is rebuilt (rezonings, Manhattanville, Second Avenue Subway Phase 2). Different from Midtown (vertical stack), Chelsea (galleries/terminals), FiDi (conversions), and from the smart-lock Harlem page (resident-run buildings).

### 1. Reddit (local) — excerpts only (Firecrawl refuses reddit.com scrapes)
- `reddit r/Harlem internet provider building fiber` · Firecrawl search →
  - https://www.reddit.com/r/Harlem/comments/1ey6vvf/what_internet_is_the_best/ — "Supposedly, fiber isn't available at my house." → §5 para (Reddit), §10.5 H3 "about a third of New York City".
  - https://www.reddit.com/r/Harlem/comments/1n0p6ts/spectrum_or_verizon_better_in_harlem/ — "Not every block/building has Verizon but if you can get it, do. I had spectrum for 8 years until Verizon came to my building around 4 years ago." → §5 para (Reddit), §10.5.
  - https://www.reddit.com/r/nyc/comments/qxk36v/ever_moved_into_a_building_and_realized_you_only/ — "a signal for NYC Mesh at one building in Harlem". → §9 Q "Neighbouring owners … share one internet connection".
  - Firecrawl scrape of the r/Harlem thread: EMPTY (not accessible in build env — "we do not support this site").
- `reddit Harlem internet fiber Verizon Fios not available brownstone building` · WebSearch → only spam/aggregator pages and a 2008 Brownstoner forum archive. EMPTY (nothing usable).

### 2–5, 8. PAA / PASF / Answer the Public / AI Overview / Bing & DDG — EMPTY (not accessible in build env)
Substitutes for the §10.5 reality check (claims as published):
- `Harlem broadband fiber 2025 2026 news building internet East Harlem` · Firecrawl search → https://broadbandnow.com/New-York/New-York (excerpt: "Fiber internet is 37.4% available in New York City (NYC)") → §10.5 H3 1; https://ispreports.org/internet-service-providers-east-harlem-manhattan-ny/ (excerpt: "Spectrum offers Fiber service to 58.1% of East Harlem homes") → §10.5 H3 7. Both excerpts only, not opened.
- Remaining §10.5 claims reuse silo sources: lowvoltagenewyork.com ($1–$6/ft, splices $50–$150), thenetworkinstallers.com (FBA $18/ft underground, $8 aerial; testing ≈5%), AT&T support (4–6 hours).

### 11. Yelp 1–3★ — EMPTY
- `yelp fiber optic cabling contractor Harlem Manhattan reviews` · Firecrawl search → only Yelp search-result pages with aggregate ratings and positive excerpts (East Harlem cable installation 4.5; Harlem internet providers 3.3 aggregate). No 1–3★ fiber-contractor reviews retrieved.

### 6/7. Landmarks, building stock, corridors
- `Mount Morris Park Historic District designated 1971 extension 2015 rowhouses Landmarks Preservation Commission` · WebSearch → WebFetch https://www.nyc.gov/assets/lpc/downloads/pdf/press/archive/2015/092215-mount-morris-park-extension-approved.pdf: approved Sept 22, 2015; 276 buildings (250+ row houses, ~12 apartment buildings) on six blocks west of the 1971 district; row houses built mostly as single-family after rapid transit reached the area around 1880, many later rooming houses/small apartment buildings; oldest = three c.1870 Second Empire houses at 124–128 W 123rd St; Queen Anne row at 133–143 W 122nd St. → §5 paras 1, facts list, §7 cards, landmarks card, sub-districts.
- `St. Nicholas Historic District Strivers' Row …` · WebSearch → WebFetch https://en.wikipedia.org/wiki/St._Nicholas_Historic_District: W 138th & 139th Sts between ACP Jr. Blvd and Frederick Douglass Blvd; built 1891–93 by David H. King Jr.; architects James Brown Lord, Bruce Price & Clarence S. Luce, Stanford White (McKim, Mead & White); designated 1967; gated rear alleys, some "Walk Your Horses" signs. → §5, facts, §9 alley Q, landmarks card, sub-districts.
- `125th Street rezoning 2008 Harlem office space Adam Clayton Powell State Office Building` · WebSearch → WebFetch https://www.nyc.gov/assets/planning/download/pdf/about/press-releases/pr043008.pdf: approved April 30, 2008; >1 million sq ft office, >7,000 jobs expected; first height limits on corridor; arts bonus. → §5 para 4, facts.
- WebFetch https://en.wikipedia.org/wiki/Adam_Clayton_Powell_Jr._State_Office_Building: 163 W 125th St, nineteen storeys, completed 1973. → §7 card, landmarks card.
- `East Harlem rezoning approved November 2017 City Council blocks Park Avenue` · WebSearch → WebFetch https://council.nyc.gov/press/2017/11/21/1549/: $222M commitments; Park Ave north of 118th 275 ft cap; Second Ave 175 ft; Third Ave (122nd–124th) 235 ft; full Council vote scheduled Nov 30, 2017. → §5 para 4, §8 East 116th card, sub-districts.
- `Columbia University Manhattanville campus acres …` · WebSearch → WebFetch https://neighbors.columbia.edu/node/1006 (Oct 2016): 17 acres, 125th–133rd Sts along Broadway; 75,000 sq ft central energy plant; loading below grade; 6.8M sq ft planned; adaptive reuse of Studebaker plant, Sheffield Farms (Prentis Hall). Wikipedia campus page: EMPTY (URL not found). → facts, landmarks card, sub-districts.
- `Columbia Business School Manhattanville Geffen Hall Kravis Hall opened 2022 …` · WebSearch → WebFetch https://dsrny.com/press-release/columbia-business-school-opens-two-new-buildings-completing-the-first-phase-of-the-university-s-17-acre-manhattanville-campus: Feb 2022, Kravis (11 storeys) + Geffen (8), 492,000 sq ft, completes first phase of 17-acre campus. → §5, facts.
- `Studio Museum in Harlem new building opened November 2025 …` · WebSearch → WebFetch https://www.studiomuseum.org/press/studio-museum-in-harlem-opening-date-and-community-day: 144 W 125th St, 82,000 sq ft, seven floors, opened Nov 15, 2025, Adjaye Associates. → §9 arts-org Q, landmarks card.
- `Apollo Theater Victoria Theater Apollo Stages opened 2024 …` · WebSearch → WebFetch https://www.governor.ny.gov/news/governor-hochul-unveils-complete-restoration-and-redevelopment-harlems-historic-victoria (Mar 7, 2024): 211-room hotel, ~200 homes (100+ affordable), two Apollo stages, 27,000 sq ft cultural space. → §9 arts-org Q, landmarks card.
- `National Black Theatre new building 2 East 125th Street opened tower` · WebSearch → WebFetch https://rebusinessonline.com/lmxd-tops-out-21-story-residential-civic-project-in-harlem/ (Oct 11, 2023): 21 storeys, 222 apartments, 27,000 sq ft NBT home, commercial along 125th St; theatre opening planned early 2026. designboom page: EMPTY (fetch error). → §9 arts-org Q.
- `Harlem Hospital Mural Pavilion …` · WebSearch → WebFetch https://www.nychealthandhospitals.org/pressrelease/mayor-bloomberg-deputy-mayor-gibbs-and-hhc-president-alan-d-aviles-open-new-harlem-hospital-patient-pavilion/: six-storey, 195,000 sq ft, $325M pavilion on Lenox Ave; restored murals (Hayes, Crimi, Alston; Seabrooke 1937). Page shows conflicting dates (2012/2016) — no opening year used. → landmarks card, §7 card.
- WebFetch https://en.wikipedia.org/wiki/Harlem: boundaries; CD9/10/11; Central Harlem = CD10; East Harlem 96th–138th. → sub-districts intro, FAQ coverage.
- `Furman Center Central Harlem MN10 …` · WebSearch → WebFetch https://www.furmancenter.org/?p=1571 (updated 05/06/2026): homeownership 15.3% (2024); public housing 13.6% of rental units, 7,766 units (2025); 1,412 properties with subsidized units. → §5 para 2, facts.

### 9/10. Local news / hyperlocal
- `Second Avenue Subway Phase 2 construction 125th Street Harlem 2026 progress` · WebSearch → WebFetch https://www.governor.ny.gov/news/governor-hochul-announces-mta-advances-final-construction-contract-second-avenue-subway-phase (Sept 14, 2026): final (fourth) contract RFQ; stations 106/116/125; Q 96th–125th ~1.5 mi; Park Ave entrance; Contract 2 to Sept 2029; full completion fall 2032; $6.968B; Contract 1 utility relocation at 106 St ~60% complete; 125 St entrance shaft excavation begun, TBM under construction. → facts, §9 subway Q, Construction Watch section.
- WebFetch https://www.amny.com/nyc-transit/second-avenue-subway-extension-east-harlem/ (Aug 18, 2025): $1.97B tunnelling contract to Connect Plus Partners; west on 125th to Park Ave; connection to Lexington line and Metro-North. → Construction Watch.
- `Harlem broadband fiber 2025 2026 news …` (above) → https://edc.nyc/press-release/nycedc-issues-rfp-redevelop-east-125th-street-site-new-housing-project (Firecrawl summary): B-East site, Second Ave between E 125th–126th, ~140 homes. → Construction Watch.
- `Harlem free Wi-Fi 110th to 138th Street …` · WebSearch → WebFetch https://www.nyc.gov/assets/fund/downloads/pdf/press_releases/press-release-harlem-wifi-12-10-2013.pdf (Dec 10, 2013): 95 blocks 110th–138th, Frederick Douglass Blvd–Madison Ave, ~80,000 residents. Listed in sources/citation only (not used in body copy beyond sources). The nyc.gov mayor news URL returned the index page: EMPTY.
- `Big Apple Connect NYCHA free internet developments Harlem St. Nicholas Houses` · WebSearch → WebFetch https://www.cb11m.org/harlem-nycha-complexes-get-free-internet-cable-through-city-program/ (Aug 1, 2023): Jefferson Houses (E 115th), Manhattanville Houses (Broadway–Amsterdam, 129th–133rd), St. Nicholas Houses (FDB–ACP, 127th–131st) added. → landmarks card (St. Nicholas Houses), sub-districts (Jefferson).
- `Link5G kiosks Harlem …` · WebSearch → only CB2/CB8/Brooklyn resolutions, nothing Harlem-specific. EMPTY.
- `Harlem church owns several buildings … Abyssinian Development Corporation` · WebSearch → WebFetch https://citylimits.org/sacred-ground/ (2002): ADC est. 1989; Convent Avenue Baptist Church ~six properties, some on landmarked blocks. https://communitydevelopmentarchive.org/abyssinia-development-corporation/: founded 1989, "rebuild Harlem brick by brick, block by block". → §5 para 2 (labelled 2002 on Sources).
- `GreenThumb community gardens Harlem …` · WebSearch → WebFetch https://www.dnainfo.com/new-york/20130819/west-harlem/volunteer-gardeners-set-sights-on-vacant-harlem-lots (Aug 19, 2013): 69 of Manhattan's 77 City-owned vacant lots in Harlem (HPD); GreenThumb agreements temporary. → §9 community-garden Q (dated 2013 on page).

### Local licensing / permits
- `LPC rules interior work historic district rowhouse permit …` · Firecrawl search → Firecrawl scrape https://www.nyc.gov/site/lpc/applications/permit-types.page: permits required for exterior work "even parts of the building that are not visible from the street"; interior work only if DOB permit needed, affects exterior, or designated interior; 95% of approvals at staff level; filed via Portico; fees for certain work. → §8.5 callouts, §9 LPC Q, roof Q, alley Q, FAQ LPC paperwork, pricing note on fees.
- LPC Permit Guidebook PDF and NYCEDC page via WebFetch: EMPTY (not accessible in build env — permission request timed out); EDC page then read via Firecrawl summary.

### Installer-practice statements without an external source (flag for Anwar)
Party-wall coring/sleeving/firestop both faces and photo; avoid bowed/damp walls; roof route in UV innerduct with non-penetrating supports and roofer's detail; no cable on fire escapes; flue reuse only after confirming sealed/unconnected; joists span party wall to party wall and holes only in middle third; volunteers not allowed to pull; church scheduling; easement advice on sale; roofer-warranty answer; ISP terms usually forbid sharing service; Columbia buildings run to their own contractor rules; "two to five days" physical work for a cluster link; P21D HowTo totalTime.

### Pricing used (parent Manhattan page lines only; no new prices)
$44/termination, $50/OTDR strand, $453 MM drop, $517 SM drop, $5,625–$8,750 12-strand OM4, $10,000–$18,750+ 24-strand OS2, from $3,000 second room, $195/hr 3-hr min ($585). Packages are sums: $552 (8×44+4×50), $1,234 (2×517+4×50), $11,034–$19,784+ (OS2 range + 2×517). Worked examples: $517; $828 (12×44+6×50).

### Images (11) — Drive folder empty (main run 17:45Z), CompanyCam not connected
New crops (faces removed) of the existing real-library set images/fiber-optic-installation/aess-fiber-optic-installation-*:
wall-enclosure-sc-adapters (hero), splicer-open-enclosure-bench, red-light-fault-locator-wall, riser-panel-yellow-cable-stack, sidewalk-handhole-conduit-pull, ceiling-tray-fiber-coil, fusion-splicer-screen-bench, otdr-trace-building-labels, power-meter-light-source-pair, labelled-backbone-panels-floor, inspection-tablet-pass-rack (all `fiber-optic-installation-harlem-*.webp`). The aess-* source set looks AI-rendered — needs Anwar's review. Gowanus (same batch) cropped some of the same source frames.

### Keyword plan (Harlem page)
Service: fiber optic installation Harlem, building-to-building fiber, rowhouse fiber riser, fusion splicing, OTDR testing. Problem: buildings not linked, provider serves one building only, party wall, landmark district, no riser, subway construction. Technology: OS2 indoor/outdoor, bend-insensitive, OFNR/OFNP, armoured, innerduct, wall-mount enclosures, media converters. Industry: churches, cultural institutions, schools, clinics, small landlords, 125th Street mixed-use. Geographic: Harlem, Central Harlem, East Harlem/El Barrio, Manhattanville, Hamilton Heights, Sugar Hill, Mount Morris Park, Strivers' Row, 125th Street, Frederick Douglass Blvd, Lenox/Malcolm X Blvd.

### Question register additions — fiber-optic-installation-harlem-manhattan-ny
Q&A (§9):
- We own both of two attached Harlem rowhouses — can a hole go through the party wall between their cellars, and how is it closed up?
- Can fiber cross from one rowhouse roof to the next instead of going through the cellars?
- Strivers' Row houses back onto shared gated alleys — can fiber run along the alley to link houses on the same row?
- Why does the direction of the floor joists matter when routing fiber across a Harlem rowhouse?
- Is a Landmarks Preservation Commission permit needed for fiber that stays entirely inside a historic-district house? (near Manhattan's landmark Q and St. George's rear-conduit Q — interior-only intent; review)
- Can cable be fixed to the fire escape on the front or back of a Harlem walk-up?
- Can a disused fireplace flue carry fiber between the floors of a brownstone? (related to DUMBO/Dutchess/St. George "reuse old shaft/chase" Qs; review)
- How do you get fiber to camera positions in a church sanctuary or balcony for livestreaming without cable across the nave?
- Our arts organisation is moving into a new building on the same street but keeping the old one — should the two be linked by fiber or run as separate networks? (partial overlap with Navy Yard "second subscription vs linking two spaces"; review)
- Neighbouring owners on our block want to share one internet connection over fiber we would install between the houses — is that allowed?
- Should a fiber project on or near East 125th Street wait until the Second Avenue Subway construction is finished?
- A community garden on a City-owned lot sits between two of our buildings — can fiber cross it?
FAQ (§17):
- Do you cover East Harlem, Manhattanville, Hamilton Heights and Sugar Hill as well as Central Harlem?
- Can installation in a church building be scheduled around services, funerals and weddings?
- Can volunteers from our congregation or block association help pull the cable to keep the cost down?
- If we sell one of the linked buildings, does the buyer have to let our cable keep crossing into the others?
- Do you take work inside Columbia University's Manhattanville buildings?
- Will you prepare the work description and photos our Landmarks Preservation Commission application needs?
- How far apart can two of our Harlem buildings be for a single fiber link?
- Our roof is still under the roofer's warranty — will a fiber crossing on the roof affect it?
CTA headings ending "?": Link Between Your Harlem Buildings Gone Dark? · Want the Route Drawn Before You Ask the Neighbours? · One Harlem Building Online and the Other Not?

## Gowanus, Brooklyn — local research (2026-10-17 batch, fiber-optic-installation-gowanus-brooklyn-ny)

**Page thesis:** Gowanus fiber has to respect three lines — the flood line (2021 rezoning towers in/near the canal floodplain under NYC BC Appendix G: utilities and attendant equipment at/above the DFE, so provider entrance + main room go up, only sealed passive pathway stays low), the slab (brownfield lots with vapour barriers / sub-slab depressurization; fiber comes in through walls and gets its own sleeve beside vent risers), and the property line between old buildings (19th-century factory complexes of joined wings with mismatched floor levels, studios/makers, individual landmarks). Distinct from Downtown Brooklyn (tower ownership lines), DUMBO (Gair concrete/bridge vibration), Navy Yard (BNYDC campus rules).

Up-link: /fiber-optic-installation-brooklyn · phone (347) 934-8335 (800 only in shared header) · GBP Brooklyn (1282 Troy Ave) · prices = Brooklyn parent lines verbatim (1.00×).

### 1. Reddit (local) — EMPTY (not accessible in build env)
- Query `reddit Gowanus apartment internet Verizon Fios Spectrum new building` · WebSearch → no reddit.com result returned (only Verizon community threads about other buildings, not Gowanus). Not used.

### 2–5, 8, 11. Google PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp 1–3★ — EMPTY (not accessible in build env)
- §10.5 substitutes (claims quoted as published, see below).

### 6/7. Landmarks, building stock, corridors (verified)
- `Gowanus rezoning 2021 approved City Council units canal` · WebSearch → https://www.6sqft.com/nyc-council-approves-sweeping-gowanus-rezoning/ (WebFetch, article Nov 24, 2021): upzones 82 blocks; "nearly 8,500 units of housing", "roughly 3,000" affordable; towers up to 30 storeys around canal, 17 on 4th Ave; $174M sewer upgrades; $200M nearby NYCHA; four acres waterfront open space → §5 para 2, §5.5 facts (8,500; 30/17), hero subhead.
- `Gowanus Canal Superfund cleanup dredging status 2025` · WebSearch → https://www.epa.gov/newsreleases/epa-reaches-new-milestone-cleanup-gowanus-canal-superfund-site-cleanup (WebFetch, July 1, 2024): RTA1 dredging/capping started late 2020; RTA2 initial work late June 2024, full-scale est. $369M over several years; RTA3 after; overall plan "over $2 billion" incl. CSO controls; two CSO tanks being built by the City → §5.5 ($2B+), "Working Over Cleaned-Up Ground", "Fiber Work Next to an Active Canal Cleanup".
- `Gowanus canal 2026 dredging middle segment RTA2 update EPA` · WebSearch → https://gowanussuperfund.com/ (WebFetch): latest update week of July 6, 2026 — RTA2 (3rd St to Hamilton Ave) bulkhead support system installation; Huntington St east of Smith St closed for GRT staging; bridge openings can close roadways/detours → brownfield section para 1, block-by-block (crossings, south end), cleanup section.
- `Gowanus flood zone resiliency rezoning requirements elevated ground floor waterfront esplanade` · WebSearch → https://www.nyc.gov/assets/planning/download/pdf/plans-studies/gowanus/canal-corridor-flood-resiliency.pdf (WebFetch, DCP): floodplain buildings must meet FEMA/BC Appendix G; residential above flood elevation; non-residential at-grade dry-floodproofed or elevated; mechanical/critical systems allowed on roofs; waterfront access plan raises waterfront yards toward future daily tide; bi-level esplanade encouraged → §5 para 3, "Keeping Gowanus Fiber Above the Water", Q&A A1/A3.
- `NYC Building Code Appendix G flood-resistant construction utilities and equipment above design flood elevation telecommunications` · WebSearch → https://www.nyc.gov/assets/buildings/codes-pdf/cons_codes_2022/2022BC_AppendixG_FloodResistantWBwm.pdf (WebFetch): G102.1 applies in SFHAs and shaded X-zones; G304.1.1 item 5 "Utilities and attendant equipment shall be located at or above the design flood elevation specified in ASCE 24, Table 7-1" (or built to keep water out) → §5, compliance callouts, Q&A A1, Terms. NOTE: Appendix G does not name telecom specifically; the page states our conservative reading as practice.
- `"Special Gowanus Mixed Use District" zoning resolution article XIII chapter 9` · WebSearch → https://zr.planning.nyc.gov/node/22003 (WebFetch): purposes (mixed use, canal access); 139-212 "Gowanus mix" FAR bonus with Notice of Restrictions + annual reports by June 30; 139-51 shore public walkway min 10-ft clear path, 20% of lot as waterfront public access; 139-52 30-ft walkways on some parcels; 139-43 sidewalks 17 ft Third Ave, 15 ft Nevins, 13 ft Fifth St → corridors (Third Ave), Q&A A3, Studios and Makers section, Terms.
- `Gowanus new rental tower 2025 opens Bond Street canal units leasing` · WebSearch → https://hoodline.com/2026/07/brick-beauty-on-the-canal-maison-bond-wraps-up-in-gowanus/ (WebFetch): Maison Bond, 335 Bond St at Carroll, 14 storeys, 73 rentals, ~10,911 sf ground-floor commercial + ~4,644 sf manufacturing; Brownfield Cleanup Program incl. sub-slab depressurization system → §5 para 4, block-by-block (canal blocks).
- `365 Bond Street Lightstone Gowanus units opened flood Hurricane Sandy` · WebSearch → https://www.6sqft.com/?p=123692 (WebFetch, Mar 1, 2016): 363–365 Bond total 700 rentals; buildings sit higher than post-Sandy floodplain; only new residential developments under way due to restrictive zoning; canal 1.8 miles, Superfund 2010 → §5 para 1, §10.5 H3 6.
- `Gowanus rezoning pipeline units under construction 2026 cityrealty buildings list` · WebSearch → https://www.6sqft.com/best-new-apartments-gowanus-brooklyn/ (WebFetch, Feb 9, 2026): Society Brooklyn 500 Degraw/504 Sackett, 517 units, two 21-storey towers, SCAPE esplanade, 57,000 sf retail, plants to withstand flooding; 420 Carroll 360 units (two towers joined by underground tunnel); 175 Third St 1,100 units / 27 storeys (planned) → §5 para 2, landmarks card (Society Brooklyn), corridors.
- `Old American Can Factory 232 Third Street Gowanus artists studios` · WebSearch → https://www.nyc.gov/site/lpc/about/pr2019/lpc_designates_five_historic_buildings_in_gowanus_as_individual_landmarks.page (WebFetch): designated Oct 29, 2019 — Somers Brothers Tinware Factory (later American Can) 238–246 3rd St 1884; BRT Central Power Station Engine House 153 2nd St 1901–03; Gowanus Canal Flushing Tunnel Pumping Station & Gate House 196 Butler St 1911; Montauk Paint 170 2nd Ave 1908; ASPCA 233 Butler St 1913 → §5 para 5, building types, landmarks cards, compliance callouts.
- `Carroll Street Bridge Gowanus retractile 1889 oldest landmark` · WebSearch → https://en.wikipedia.org/wiki/Carroll_Street_Bridge (WebFetch): opened 1889; landmark 1987; oldest of four remaining US retractile bridges; closed 2020/21 for cleanup damage; reopened June 15, 2026 to pedestrians, bikes, emergency vehicles → §5.5 fact, landmarks card.
- `Gowanus Canal bridges Union Street Third Street Ninth Street bascule bridge list` · WebSearch → https://www.nyc.gov/html/dot/html/infrastructure/bridges-gowanus.shtml (WebFetch): Union St bascule 1905; Carroll St retractile 1889; Third St bascule 1905; Ninth St vertical lift 1999; Hamilton Ave bascule 1942 → corridors (crossings).
- Same search → https://en.wikipedia.org/wiki/Gowanus_Canal (WebFetch): 1.8 mi, ~100 ft wide; Superfund announced March 4, 2010; flushing tunnel 1911, reactivated 2014 after $177M upgrade; Fourth Street Basin branches east at Fourth St → §5.5 fact, landmarks (pumping station), block-by-block (south end).
- `Gowanus CSO retention tank Butler Street Nevins 8 million gallon DEP construction Thomas Greene Park` · WebSearch → https://citylimits.org/gowanus-sewage-cleanup-will-clear-out-several-businesses/ (WebFetch, Dec 7, 2017): 8M-gallon tank at head of canal on 234 Butler, 242 & 270 Nevins; 19 businesses displaced; 4M-gallon second tank at DSNY facility 2nd Ave & 5th St → §5.5 fact, corridors, block-by-block.
- `Gowanus Hurricane Sandy flooding canal overflow basements 2012` · WebSearch → https://brooklyneagle.com/articles/2012/12/05/sandy-pushed-gowanus-delivered-noxious-toxic-punch/ (WebFetch): canal "gushed over its banks", flooding streets and basements; landlords hadn't pumped basements; bacteria and industrial toxins concern → "Keeping Gowanus Fiber Above the Water" para 1.
- `Gowanus Green Public Place former gas plant site construction affordable housing 2025` · WebSearch → https://www.brownstoner.com/development/gowanus-green-public-place-development-2026/ (WebFetch, Mar 20, 2026): city-owned former Citizens MGP; 950 all-affordable homes, school, park; cleanup stalled since 2024 (National Grid vs DEC dispute) → corridors (south end), brownfield section.
- `Powerhouse Arts Gowanus 322 Union Street opened 2023 former power station` · WebSearch → https://www.aiany.org/architecture/featured-projects/view/powerhouse-arts/ (WebFetch): 1903 BRT power station; 170,000 sf; fabrication workshops (metal, wood, ceramic, textiles, print) + performance/exhibition; PBDW / Herzog & de Meuron; year 2023 → §5 para 5, landmarks card. (Street address 322 Union St appears only in a search-result title; page uses LPC's 153 Second Street for the engine house.)
- `Whole Foods Third Street Third Avenue Gowanus opened 2013 rooftop greenhouse Gotham Greens` · WebSearch → https://bkreader.com/2013/12/19/10-things-you-should-know-about-the-new-brooklyn-whole-foods-store/ (WebFetch): 214 3rd St at 3rd Ave; 56,000 sf; 20,000 sf Gotham Greens greenhouse. December 2013 opening per search results (Commercial Observer "Whole Foods Announces December Opening in Gowanus", dnainfo 2013-12-17) → corridors (Third Ave), landmarks card.
- `Fourth Avenue Park Slope Gowanus 2003 rezoning residential buildings corridor` · WebSearch → https://brooklyneagle.com/articles/2014/09/11/fourth-avenue-undergoes-transformation/ (WebFetch, Sept 11, 2014): 2003 rezoning Warren–15th St, residential to 120 ft; extended to 24th St two years later; 11–13-storey projects; blank ground floors criticised; Special Fourth Avenue Enhanced Commercial District 2011 → building types, corridors, block-by-block.
- `Gowanus Open Studios artists studios buildings number 2025` · WebSearch → https://www.artsgowanus.org/gowanus-open-studios-2026 (WebFetch): Oct 17–18, 2026; 30th year; "more than 400 artists, businesses, and venues"; organiser Arts Gowanus → §5 para 5.
- `HPD broadband in affordable housing design guidelines requirements entry point new construction` · WebSearch → https://www.nyc.gov/site/hpd/services-and-information/broadband-development-projects.page (WebFetch): "Fiber is trenched from the nearest telecommunications vault in the street to the building's basement"; risers to each floor; ≥100 Mbps up/down per apartment; no additional cost to tenant; applies to HPD-assisted projects (MIH/VIH-only and 421-a-only excluded) → §10.5 H3 5, FAQ 4.
- `Gowanus rezoning E-designation hazardous materials OER vapor barrier sub-slab depressurization` · WebSearch → only generic EIS PDFs (a002-epic.nyc.gov) returned; not opened. Page mentions E-designations only generically in compliance callouts.

### 9/10. Local news / hyperlocal on fiber contractors in Gowanus — EMPTY (none retrieved).

### §10.5 substitutes (quoted as published)
- https://www.angi.com/articles/fiber-optic-cable-installation-cost.htm (WebFetch this run, "Updated May 3, 2026"): "$1,500 and $7,000 for your home"; "$1 to $12 per linear foot"; aerial $1,000–$5,000 vs underground $2,000–$10,000; labour "$50 to $150 per hour", "$1 to $7 per foot" → H3 1–4. ("Aerial installations are less expensive because they require less digging" re-verified by a second WebFetch this run.)
- HPD broadband page (above) → H3 5. 6sqft 365 Bond (above) → H3 6.
- thenetworkinstallers.com FBA 2025 underground median $18/ft, aerial $8/ft — silo research entry (line 29), not re-fetched this run → H3 7.

### Pricing used (Brooklyn parent page lines verbatim, 1.00×)
$35/termination · $40/strand OTDR · $350 MM drop · $400 SM drop · $4,500–$7,000 12-strand OM4 · $8,000–$15,000+ 24-strand OS2 · from $2,400 second telecom room · $195/hr 3-hr min ($585). Packages $800 / $4,500–$7,000 / $8,000–$15,000+ (parent package prices).

### Images (11) — Drive folder `AESS Website Photos/Fiber Optic Installation` empty (main run, 17:45Z), CompanyCam not connected
Cropped (faces removed) from the 20 `images/fiber-optic-installation/aess-fiber-optic-installation-*` library photos (the set every current fiber page uses; these look AI-rendered — Anwar to review), saved as `fiber-optic-installation-gowanus-<what>.webp`: riser-panel-yellow-jumpers, armored-cable-into-handhole, wall-enclosure-pigtails, splice-enclosure-breakout-strands, fusion-splicer-loading-fiber, red-fault-locator-on-strand, cleaver-and-splicer-bench, distribution-panel-numbered-ports, otdr-trace-building-uplinks, end-face-pass-screen, loss-test-meters-at-rack. Captions/changelog state photos were not taken at a Gowanus site.

### Keyword plan (Gowanus page)
Service: fiber optic installation Gowanus, fiber backbone Gowanus, riser fiber new building, factory building fiber link, studio fiber drop, fusion splicing, OTDR testing. Problem: flood zone, design flood elevation, flooded cellar, brownfield slab, vapour barrier, vent chase, mismatched floors, crane bay, kiln room, airtight envelope, roof membrane. Technology: OS2, OM4, OFNR/OFNP, armoured cable, duct seals, innerduct, splice enclosures. Industry: developers/GCs, studio landlords, makers, venues, retail on Third Ave, Fourth Ave residential. Geographic: Gowanus, Gowanus Canal, Bond/Nevins Streets, Third Avenue, Fourth Avenue, Union/Carroll/Third St bridges, Butler/Douglass/Degraw, Second–Hamilton Aves, Carroll Gardens, Park Slope, Boerum Hill, Red Hook.

### Question register additions (fiber-optic-installation-gowanus-brooklyn-ny)
- Which parts of a fiber system can stay below the design flood elevation in a new canal-side building, and which have to go up?
- Our lot runs from a higher avenue down to a lower street near the canal — which frontage should the provider's fiber come in on?
- The shore walkway on our lot has to stay open to the public — can conduit for its lights and cameras run underneath it?
- The vapour-mitigation vent pipe runs up the only chase to our roof — can fiber share that shaft?
- Can cellar flood sensors, sump-pump alarms and the vapour-mitigation fan alarm report to the super over the building's fiber?
- Our complex is several old factory buildings joined together and the floors don't line up — how does a backbone cross from one section to the next?
- Where should fiber run in a fabrication shop with an overhead crane?
- Our ceramics studio fires kilns for hours at a time — can fiber or network gear go in the kiln room?
- Our new building is going for Passive House certification — how are cable holes kept from spoiling the airtightness test?
- Can conduit for rooftop equipment cross a green or blue roof without voiding the membrane warranty?
- FAQ: Do you also work in Carroll Gardens, Park Slope’s Fourth Avenue blocks, Boerum Hill and Red Hook?
- FAQ: Does fiber work inside a building beside the Superfund canal need any sign-off from the EPA or the state?
- FAQ: Our shop ceiling is packed with fume-extraction ducts — where does the fiber go?
- FAQ: Our affordable building is HPD-assisted — does the city’s broadband guidance decide where the fiber enters?
- FAQ: Can a fiber link carry DMX lighting control or show control for a performance or event space?

Closest existing intents (judged distinct, please review): A1 vs Manhattan "main fiber room stay in cellar of flood-prone building" / DUMBO "network equipment up to the roof" (ours = what the code lets stay below the DFE); B1 vs Port Morris "vapour barrier under the slab — can conduit pass through it" (ours = sharing the vent-riser chase); B2 vs Bronx/Nassau BMS-over-fiber questions (ours = flood/pump/vapour-fan alarms); FAQ DMX vs Brooklyn "production video and audio between stages".


<!-- batch 2026-10-17T17:27Z: fiber-optic-installation-mott-haven-bronx-ny -->
## Mott Haven, Bronx — local research (2026-10-17 batch, fiber-optic-installation-mott-haven-bronx-ny)

Thesis (distinct from Port Morris' "second-and-third-use industrial buildings" and Fordham's "buildings keep changing jobs"): Mott Haven is residential — three landmark row-house districts, walk-up tenements, NYCHA campuses, new HPD-assisted affordable buildings with clinics/pharmacies below, and old institutions (churches, Carnegie library, schools). Fiber is about getting glass from the provider's box to the rooms without marking a landmark front, cluttering an exit stair or disrupting occupied homes; approvals (owner/board, LPC, HPD, neighbours, tenants) and occupied-home practice (notice, lead-safe thresholds) are the core.

### Sources (exact query · platform · URL · finding · page + section used)

- Query: (direct page) `https://en.wikipedia.org/wiki/Mott_Haven,_Bronx` · Firecrawl scrape → https://en.wikipedia.org/wiki/Mott_Haven,_Bronx : primarily residential; bounded roughly by E 149th St (N), Bruckner Expwy (E/S), Harlem River (W), boundaries imprecise; E 138th St primary E–W street; CB1; ZIPs 10451/10454/10455; 6 train along E 138th; 2020 pop. 54,163; area 1.18 sq mi; Alexander Ave brownstones "Doctors' Row / Irish Fifth Avenue"; land use "dominated by tenement-style apartment buildings and large public-housing complexes", three historic districts of brownstone rowhouses, new 2–3-unit rowhouses; one of the highest NYCHA concentrations in the Bronx; 17 NYCHA developments listed (Mott Haven Houses 8 bldgs 20/22 st; Mitchel 10 bldgs 17–20 st; Patterson 15 bldgs 6/13 st; Millbrook nine 16-st; several Betances developments = rehabilitated 5–6-storey tenements); Mott Haven HD on Alexander Ave E 138th–E 141st (4–5-storey row houses, 40th Precinct station house, 1905 library, St. Jerome's), NRHP 1980; Mott Haven East (E 139th/140th, Brook–Willis, 1883, O'Gorman & Hornum); Bertine Block (E 136th, Brook–Willis, 1891–95); St. Ann's Episcopal Church (St. Ann's Ave E 139th–141st, 1841, Bronx's oldest church, Lewis & Gouverneur Morris buried); redevelopment on E 138th: The Joinery (first luxury mid-rise condo), Borinquen Court, Tres Puentes; schools list (P.S. 30, 40, 49, 154, Mott Haven Academy CS, South Bronx Classical II, Hostos CC etc.); library 321 E 140th (Carnegie, 1905, City landmark); Lincoln Hospital 234 E 149th, FDNY EMS Station 14; Hub Station P.O. 633 St. Ann's Ave; NYC Health 2018 profile: 25 bodegas per supermarket. → §Why (paras 1–2, facts list), Architecture cards, Business corridors, Walk-up section, Institutions, Public Housing, Landmarks cards, Sources table.
- Query: `Mott Haven Historic District Alexander Avenue Landmarks Preservation Commission designation report row houses` · WebSearch → https://hdc.org/hdc-across-nyc/bronx/hd-map/bronx-landmarks-mott-haven/ (WebFetch): designated July 29, 1969; "Irish 5th Avenue"/"Politicians' Row"; one of the earliest (possibly the earliest) row-house series in the Bronx built 1863–1865. → hero, facts list, Landmark Row Houses para 1, Landmarks card, Sources.
- Query: `Bertine Block Historic District East 136th Street Bronx landmark` · WebSearch → https://hdc.org/hdc-across-nyc/bronx/hd-map/bronx-landmarks-bertine-block/ (WebFetch): designated April 5, 1994; Edward D. Bertine's ten Queen Anne row houses 1891–1895; three two-storey brick row houses 1877–1878. → Landmark Row Houses para 1, Landmarks card.
- Query: `"Mott Haven East Historic District" designated 1994 Landmarks Preservation Commission East 139th East 140th Street` · WebSearch → https://hdc.org/hdc-across-nyc/bronx/hd-map/bronx-landmarks-mott-haven-east/ (WebFetch): designated April 5, 1994; last-quarter-19th-c. town houses with Dutch/Flemish detailing. → facts list, Landmark Row Houses para 1, Landmarks card.
- Query: `Landmarks Preservation Commission rules installation of conduit cable telecommunications equipment facade historic district permit` · WebSearch → https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf (WebFetch): Ch. 11 Health, Safety and Utility Equipment — conduit concealed through plain masonry behind installation; staff may approve ~10 in. visible conduit; surface conduit painted to match, secured into mortar joints; not through cast iron or on decorative surfaces; ordinary maintenance needs no permit. Does NOT address telecom equipment specifically (stated on page as "chapter on utility equipment"). → Landmark Row Houses para 2.
- Query: `LPC permit interior work historic district building "interior" alterations do not require LPC permit unless affects exterior FAQ nyc.gov` · WebSearch → https://home4.nyc.gov/site/lpc/about/permits-and-making-alterations.page (WebFetch): "Most exterior changes to the front and rear facades of buildings in historic districts require review by LPC"; interior LPC permit only when DOB permit required, interior work affects exterior, or designated interior landmark. → Landmark para 2 & 4, code callouts, FAQ 2 & 3, Approvals table.
- Same search → https://www.nyc.gov/site/lpc/applications/permit-types.page (WebFetch): staff-level permits (Permit for Minor Work, Certificate of No Effect, Master Plans, FasTrack/Expedited CNE) for work conforming to LPC Rules; Certificate of Appropriateness = Commission public hearing. → Landmark para 3, Q&A (façade application).
- Query: `Mott Haven Bronx internet fiber broadband building residents` · Firecrawl search → https://www.nyc.gov/site/hpd/services-and-information/broadband-development-projects.page (Firecrawl scrape): guidelines updated March 2026; apply to HPD-assisted new construction, supportive, senior and preservation projects; ≥100 Mbps up/down per unit; 99.9% uptime; no added cost to tenant; unique secured profile; owner retains in-building network ownership; pathways accessible with room for more cable; standard option fiber from street vault to basement switch then risers; <50 units alternatives; Neighborhood Internet (NYPL-operated, HPD-funded) for HPD projects in Bronx west of White Plains Rd and Manhattan north of 96th St; sponsors may admit other ISPs for paid service. → code callouts, Affordable Housing section, Q&A (HPD, Neighborhood Internet), Approvals table.
- Same search → https://thebronxisbuffering.nycitynewsservice.com/bridge/ (Firecrawl scrape; NYCity News Service 2021): Bronx has major conduit system from Manhattan via Verizon's Empire City Subway, expense is connecting the last mile; School District 7 (parts of Mott Haven, Melrose, Hunts Point) only 77% households with broadband (CCC data); Neture/Nos Quedamos Melrose (760 Melrose Ave, nine storeys, 120 apts). Used: conduit/last-mile point. NOT used: 77% figure, Neture details. → §Why para 3, AI claim 4.
- Same search → https://ispreports.org/internet-service-providers-mott-haven-bronx-ny/ (search excerpt only): "Optimum offers Fiber service to 76.6% of Mott Haven homes"; "Astound Broadband offers Fiber service to 7.4% of Mott Haven homes". → AI claim 1.
- Same search → https://bestneighborhood.org/tv-and-internet-mott-haven-bronx-ny/ (search excerpt only): "About 87.56%, or 67,509 people, have EarthLink fiber internet available". → AI claim 2 (contrasted with 2020 pop. 54,163).
- Same search → https://thebronx.org/understanding-and-overcoming-the-bronx-digital-divide/ (excerpt): "22.4 percent of households lack broadband at home". → AI claim 3.
- Query: `reddit r/bronx Mott Haven internet provider Fios Optimum apartment` · Firecrawl search → https://www.reddit.com/r/bronx/comments/15bxozc/any_alternative_to_optimum/ (excerpt): "My Optimum internet goes down and is extremely slow almost every morning until around 11:30" (Bronx-wide, not Mott Haven-specific). → AI claim 5.
- Query: `The Hub Bronx East 149th Street Third Avenue Willis Melrose BID "The Hub" retail district history` · WebSearch → https://en.wikipedia.org/wiki/The_Hub,_Bronx (WebFetch): convergence of E 149th, Willis, Melrose, Third; mostly in Melrose lining Mott Haven's northern border; "Broadway of the Bronx"; oldest major shopping district in the Bronx; HUB Third Avenue BID est. 1990, first BID in Bronx; Bronx Opera House now boutique hotel; Hub Retail and Office Center (2007), Triangle Plaza Hub (2016); crowded sidewalks. → Hub section, Business card, FAQ 1.
- Query: `NYC Health + Hospitals Lincoln 234 East 149th Street beds history opened 1976 building` · WebSearch → https://en.wikipedia.org/wiki/Lincoln_Hospital_(Bronx) (WebFetch): 234 E 149th St, Mott Haven; NYC H+H; current building dedicated 1976; Adult Level I trauma; >144,000 ED visits/yr; busiest single-site ED in NYC, third-busiest in nation; founded 1839. NOT used: bed counts (362 vs 347 conflict). → facts list, Health section, Business card, Landmarks card.
- Query: `Tres Puentes Mott Haven affordable housing 6sqft Brook Avenue apartments Borinquen Court` · WebSearch → https://thenyhc.org/projects/tres-puentes/ (WebFetch): WSFSSH; two new buildings, 175 affordable senior apartments; campus with Borinquen Court 320 units; 4,500 sq ft FQHC by Urban Health Plan; 1,300 sq ft pharmacy; social services suite; ground-floor retail on Third Ave; 162,000 sq ft. → Affordable Housing para 4, Health para 1, Business card (E 138th).
- Query: `Mott Haven Library 321 East 140th Street Carnegie 1905 landmark NYPL` · WebSearch → https://6tocelebrate.org/site/mott-haven-branch-nypl-the-bronx (WebFetch): 321 E 140th; 1905; Babb, Cook & Willard; Classical Revival. NOT used: its "1967" district date (conflicts with HDC 1969). → Institutions para 3, Landmarks card.
- Query: `EPA Renovation Repair and Painting rule pre-1978 housing 6 square feet interior 20 square feet exterior certified firm` · WebSearch → https://www.dshs.texas.gov/environmental-lead-program/laws-rules-environmental-lead-program/summary-epas-renovation-repair (WebFetch): federal RRP 6 sq ft interior / 20 sq ft exterior. Not used directly (NYC rule stricter).
- Query: `NYC Local Law 1 of 2004 lead paint pre-1960 multiple dwelling child under 6 work disturbing 100 square feet safe work practices` · WebSearch → https://www.nyc.gov/site/hpd/services-and-information/safe-work-practices.page (WebFetch): safe work practices apply to pre-1978 housing when disturbing ≥2 sq ft paint in a room (or 10% of small component), exterior ≥20 sq ft; EPA-certified RRP firm; independent dust-clearance testing; LL1 child-under-6 >100 sq ft abatement. → code callouts, Occupied Homes section, FAQ 5, Walk-up para 3.
- Silo sources reused: https://council.nyc.gov/data/internet-access/ (Melrose–Mott Haven–Port Morris 44% without broadband subscription, highest district) → §Why para 3, facts list, AI claim 3. nyc.gov Big Apple Connect (Sept 2025, ~220 NYCHA developments, through June 2028) → Public Housing para 1. Bronx Times May 4, 2026 (https://www.bxtimes.com/mayor-mamdani-ritchie-torres-high-speed-internet/: $2M Neighborhood Internet expansion; microtrenching, rooftop equipment, in-unit connectivity, ~50 buildings) → Affordable Housing para 3.
- Prices: Bronx parent page lines verbatim ($35 termination, $40 OTDR/strand, $391 MM drop, $447 SM drop, $4,500–$7,000 12-strand OM4 backbone, $8,000–$15,000+ 24-strand OS2, from $2,400 second telecom room, $195/hr 3-hr min $585). Packages are sums: 3 × $447 = $1,341; backbone $4,500–$7,000; backbone + second room = $6,900–$9,400; labour-only $195/hr.
- EMPTY (not accessible in build env): Google People Also Ask, People Also Search For, Answer the Public, Google AI Overview, Bing, DuckDuckGo, Yelp 1–3★ for Mott Haven fiber/cabling. Local Reddit: only Bronx-wide r/bronx Optimum thread found (excerpt only); no Mott Haven-specific fiber thread.

### Keyword layers (Mott Haven)
Service: fiber optic installation Mott Haven, row house fiber entry, brownstone fiber, walk-up fiber riser, tenement riser, affordable housing fiber backbone, clinic network fiber, church campus fiber, fusion splicing, OTDR testing. Problem: landmark façade restrictions, no riser closet, single exit stair, occupied apartments, tenant access refused, pre-1978 lead paint, shared light wells/party walls, store-controlled cellar, provider stops at its box, separate clinic/residential networks. Technology: bend-insensitive OS2, slim drop cable, OFNR/OFNP, paintable surface raceway, small wall enclosures, media converters/SFP. Industry: row-house owners, small multifamily landlords, HPD-assisted/senior/supportive housing, FQHCs/pharmacies, charter & parochial schools, churches, nonprofits, bodegas/storefronts. Geographic: Mott Haven, Alexander Ave, Bertine Block, Mott Haven East, E 138th St, Willis Ave, Third Ave, St. Ann's Ave, Brook Ave, E 149th St, The Hub, Melrose, Port Morris, Lincoln Hospital, St. Mary's Park.

### Question register additions (fiber-optic-installation-mott-haven-bronx-ny)
FAQ (visible + FAQPage schema):
- Do you also take fiber work in Melrose, the Hub and the Grand Concourse blocks next to Mott Haven?
- Does the Landmarks Commission have to approve fiber work that stays entirely inside a historic-district house?
- Our house is in the historic district but is not one of the notable buildings — do the landmark rules still cover it?
- What happens if one tenant along the planned route won't let us into their apartment?
- Our building is older than 1978 — do lead-paint rules affect drilling for fiber?
- How many fiber drops does a typical three-storey row house need?
- Does a single-family row house pay the same fiber rates as a commercial building?
- Our bodega's cameras record to a box in the cellar and the picture keeps freezing — is it the cable or the recorder?
- The store on our ground floor controls the cellar where the provider's line comes in — how do the upstairs owners get access for fiber work?
- The provider will run its line to my house for free — when does a homeowner need a private installer as well?
- How many days will a crew be working inside a lived-in walk-up?
- Will the new cable be visible in our building's public hallway, and what will it look like?
Q&A (H3):
- Our row house already has a Landmarks permit application in for façade restoration — can the fiber entry be added to it?
- Our row house has a rented garden apartment that takes up most of the cellar level — where can the fiber equipment go?
- Can the old gas-light pipes inside the walls of an 1880s house be used as conduit for fiber?
- Our tenement shares a light well with the building next door — whose permission does a cable up that well need?
- Our building is HPD-financed — what do the City's broadband guidelines require of the cabling itself?
- If we choose the Library-run Neighborhood Internet option for an HPD project, is there any cabling left for us to do?
- Some of our senior residents depend on medical-alert units at home — how is a cutover handled so those keep working?
- Our church's buildings are separated by an old churchyard — can fiber cross it?
- Our charter school shares a city-owned school building with a district school — who approves new cabling?
CTA headings ending "?": Mott Haven Building Lost Its Connection Overnight? · Apartments Lost Service on One Line of the Building?

### Images (11, permanent image rule — no real fiber photos; Drive folder empty per main run 17:28Z, CompanyCam not connected)
All cropped to remove faces, shirt/hat/van phone numbers, a building directory and a readable floor-plan sheet; saved as WebP q80 in images/fiber-optic-installation/:
fiber-optic-installation-mott-haven-fusion-splicer-adapter-panel.webp ← images/low-voltage/low-voltage-installation-brooklyn-fiber-splice-tray.jpg · …-brick-wall-enclosure-conduit.webp ← low-voltage-installation-nassau-county-exterior-enclosure-install.jpg · …-core-bit-block-wall-pull-line.webp ← images/network/network-installation-bronx-core-drill-cmu-wall-penetration.webp · …-finished-wall-opening-fish-line.webp ← network-installation-bronx-retrofit-wall-fish-data-drop.webp · …-pull-box-riser-conduit.webp ← low-voltage-installation-nassau-county-riser-conduit-pull.jpg · …-stud-wall-panel-termination.webp ← low-voltage-installation-bronx-idf-patch-panel-build.jpg · …-cable-label-marking-rack.webp ← network-installation-bronx-cable-labeling-port-map.webp · …-tone-probe-wall-outlet-trace.webp ← low-voltage-installation-dutchess-county-08-tone-generator-trace.jpg · …-van-shelf-reels-ladder.webp ← low-voltage-installation-brooklyn-van-load-out.jpg · …-school-hall-ceiling-bundle.webp ← low-voltage-installation-hudson-valley-10-school-corridor-cable-pull.jpg · …-hallway-riser-bundle-lift.webp ← network-installation-long-island-idf-riser-cable-bundle.webp


<!-- batch 2026-10-17T17:27Z: fiber-optic-installation-port-richmond-staten-island-ny -->
## Port Richmond, Staten Island — local research (2026-10-17 batch, fiber-optic-installation-port-richmond-staten-island-ny)

Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Silo-wide sources in research/fiber-optic-installation.md are reused where noted. Page thesis: Port Richmond is three economies on one avenue — a main street of small storefronts where two of three merchants rent (so fiber is designed around landlord approval, fixture-vs-equipment ownership and routes that stay in the merchant's own space), an M3-1 waterfront of yards rather than buildings inside the expected Flood Zone A (links between office, scale house, sheds and masts with electronics above the flood line and no digging on capped/contaminated ground), and village-era frame houses with no riser (one cavity, one thin cable, Landmarks only for the individual landmarks — no historic district). Distinct from St. George (vertical hillside/co-ops), Stapleton (three building generations, cellar-to-dry-floor risers, rezoning fit-outs) and Bloomfield (logistics/warehouses).

### Reddit (local)
- Query: `reddit statenisland "Port Richmond" internet OR Fios OR wiring OR landlord` · Firecrawl search (excerpts only; scrape of reddit.com refused by Firecrawl "we do not support this site") →
  - https://www.reddit.com/r/statenisland/comments/d8m10k/advice_port_richmond_house/ — excerpt: "My wife and I found a house we like in Port Richmond just north of Post Avenue. Reading about the area, it seems it isn't the best neighborhood." → not quoted; background only (house buyers north of Post Ave).
  - https://www.reddit.com/r/statenisland/comments/gtdgy1/... (Ralph's Ices memorial post), /comments/1s92u2k/ (Popeyes on Forest Ave closed) → not relevant, not used.
  - No r/statenisland thread on Port Richmond internet/wiring found. Reddit local for the service: EMPTY.
- https://www.reddit.com/r/HomeNetworking/comments/8qcawt/fiber_optic_cable_foot_spectrum_quote_6000_for/ (title via Firecrawl search) "Fiber optic cable $/foot, Spectrum quote $6000 for ~450ft of cable on pre-installed poles" → §10.5 H3 5 (quoted as a forum thread title).

### PAA / PASF / Answer the Public / AI Overview / Bing & DDG / Yelp — EMPTY (not accessible in build env)
Substitutes for §10.5 (claims quoted exactly as published; query `fiber optic cable installation cost per foot business building 2025 HomeAdvisor OR Angi OR Fixr` · Firecrawl search excerpts):
- https://www.angi.com/articles/fiber-optic-cable-installation-cost.htm — "costs average $4,500 for most homeowners, with most installations ranging from $1,500 to $7,000"; DIY "Materials cost $1 to $3 per linear foot" → §10.5 H3 1 and H3 2.
- https://unio.digital/blog/fiber-optic-installation-cost — "$300 to $800 per fiber drop installed for a typical office run"; "Drop count and run distance are the primary cost drivers"; underground "$15 to $35 per foot" → §10.5 H3 3 (and H3 6 range).
- https://www.clawcomm.com/fiber-optic-installation-cost-in-the-bay-area-... — "Commercial fiber optic installation cost in the Bay Area typically runs between $10,000 and $100,000+ per project"; "For a small office build-out under 5,000 square feet, budget at least $10,000–$15,000"; "Underground trenching costs $15–$35 per linear foot" → §10.5 H3 4 and H3 6.
- https://www.quora.com/How-much-does-it-cost-to-install-fiber-optic-cable — "24 Count Fiber = 70,000 ft at $0.68 per foot" → §10.5 H3 7 (quoted as a Q&A-site answer).
- Not used: thenetworkinstallers ($8/$18) and ringandping (already used on SI parent); Facebook lowvoltagenation "$29,000" comment (anecdote).
- Note: the Clawcomm "$10,000–$15,000" line also appears as an H3 on Stapleton and the Unio "$300 to $800" / "100 to 200 drops" lines as H3s on Orange / Hudson Valley; this page's H3s quote different sentences from those sources.
- Yelp 1–3★ for Port Richmond / Staten Island fiber or cabling contractors: no yelp.com result. EMPTY.

### Landmarks, history, demographics
- Query: `Port Richmond Staten Island neighborhood history Port Richmond Avenue commercial Kill Van Kull` · WebSearch → https://en.wikipedia.org/wiki/Port_Richmond,_Staten_Island (WebFetch): boundaries Kill Van Kull / Clove Rd / Forest Ave / Bayonne Bridge; CD1, ZIP 10302; 2020 Census 22,609 (+8.9% from 20,754); 56.0% renter-occupied; Hispanic 49.1%; village incorporated 1866; oyster captains' houses on Richmond Terrace 1840s–1850s; North Shore branch built 1880s, closed 1953; Ritz Theater 1924 by Sol Brill, 2,126 seats, Pedulla family tile showroom from 1985, surviving murals; Temple Emanu-El domed building 1907; Carnegie library 1905, Chimes Playhouse 1939; "Port Richmond 7" exchange 1930–1948; Old PS 20 (Heberton Ave, building 1891, landmark 1988); 121 Heberton Ave c.1859–61 (landmark 2002); Reformed Church NRHP 2005; ferries to Bergen Point; Castleton Bus Depot; Bayonne Bridge 1931. → §5 paras 1–4, §5.5 (56% renters, population), §7 cards, §13 cards, "What We Find" (Port Richmond 7), Congregations section, LocalBusiness/WebPage schema mentions.
- Same search → https://hdc.org/borough/port-richmond/ (WebFetch): "one of the oldest neighborhoods on the island"; coach route NYC–Philadelphia; ferries until shortly after the 1931 bridge; landmarks 121 Heberton Ave (designated Dec 17, 2002, c.1859–61, carpenter-builder James G. Burger), Reformed Church 54 Port Richmond Ave (Greek Revival, 1844, Burger), NYPL Port Richmond 75 Bennett St (opened Mar 18, 1905, Carnegie), 29 Cottage Place (two-storey Greek Revival frame saltbox); no historic district named. → §5 para 1, §7, §8.5 Landmarks callout, Old Houses section, §13, schema mentions.
- Same search → https://forgotten-ny.com/?p=31963 (WebFetch, Dec 2006 + reader comments): Griffith Block 1874 (shoe dealer Charles Griffith, Burr plaque); Farrell Lumber in former Empire Theater (1916–1978), moved out early 2009; Faber Park land granted to Jenny Faber 1869, pool 1932 largest on SI at the time; SIRT Port Richmond section raised on viaduct 1935 by B&O; tug yards (Moran, Reinauer, McAllister) on the Terrace (location along the Terrace not pinned to Port Richmond — NOT used). → §7 big-rooms card, §13 Faber card, "Up the Avenue" lower-avenue para, Bridge-and-Rails section.
- Query: `Bayonne Bridge raised roadway 2017 2019 Port Richmond Staten Island` · WebSearch → https://en.wikipedia.org/wiki/Bayonne_Bridge (WebFetch): opened Nov 15, 1931; main span 1,675 ft; Raise the Roadway contract Apr 24, 2013; northbound roadway Feb 20, 2017; southbound completed Feb 11, 2019; completion May 2019; ~$1.7 billion; clearance 151 → 215 ft; path opened May 24, 2019; SI end lands in Port Richmond. → §5.5, §13 card, Bridge-and-Rails section, schema mentions.

### Commercial corridor (core of thesis)
- Query: same first query → https://www.nyc.gov/assets/sbs/downloads/pdf/neighborhoods/n360-cdna-portrichmond.pdf (WebFetch; NYC SBS Neighborhood 360° Commercial District Needs Assessment, La Colmena, July 2023–June 2024): corridors Port Richmond Ave (Richmond Terrace–Forest Ave) and Forest Ave (Manor Rd–Port Richmond Ave); 392 storefronts; vacancy 7.9% (June 2024) vs 12.8% BID average (75 BIDs); 201 merchant surveys: 67% rent, 16% own; median 8 years in business; median 3 full-time employees; 52% have a website; 52% minority/woman-owned; business categories list (full/limited-service restaurants, delis/bodegas & smoke shops, salons/barbers, medical, professional services, nonprofits/houses of worship, automotive, check cashing/money transfer, laundromats, schools/day cares…); Port Richmond Ave "significantly darker at night"; 2023 AADT Forest Ave 19,638 (MLK Expwy–Jewett Ave), Richmond Terrace 13,067, Port Richmond Ave 10,320 (Trantor Pl–Richmond Terrace); internet/connectivity concerns NOT discussed (only website/social use). → §5 para 2, §5.5 facts 1–2, §8 corridor cards, §10.5 H3 4, Renting section, Restaurants section, schema mention.
- Query: `Port Richmond Staten Island North Shore rezoning OR "Port Richmond Avenue" storefronts 2024 2025` · WebSearch → https://www.nyc.gov/assets/planning/download/pdf/plans-studies/port-richmond-boa/presentation_0613.pdf (WebFetch; DCP Port Richmond Brownfield Opportunity Area presentation, 2012–13 meetings): avenue once the "5th Avenue of Staten Island"; Subarea A 37 sites / 12.5 acres open land on the waterfront (fleet storage, auto repair, junk storage, vacant); waterfront uses incl. Faber Park, bus parking, auto repair, C&D waste transfer, maritime support; M3-1 waterfront, M1-1 pockets; updated FEMA maps likely put most land north of Richmond Terrace in Flood Zone A; buildings may need elevation up to 7 ft; Richmond Terrace mapped width far wider than built road, historic buildings in mapped bed, narrow sidewalks; ~152 on-street spaces on Port Richmond Ave; strategic sites incl. former Standard Boat, EPA Superfund/former Jewett Lead–Sedutto's, former Sherwin Williams; prominent nonprofit/social-services presence; recommended BRT environmental review on former rail ROW; reconnect avenue to bulkhead. Dated (2012–13) — stated as "the study" / "was expected". → §5 para 1 & 3, §5.5 fact 4, §7 waterfront card, §8 cards, §8.5 flood/zoning callout, Waterfront section, Flood-proofing Q, Up the Avenue, Bridge-and-Rails, Congregations, FAQ parking.
- https://www.nyc.gov/site/planning/plans/port-richmond-boa/port-richmond-boa.page (WebFetch) → "page has moved" only. EMPTY.
- Query: `silive Port Richmond Avenue business 2025 OR 2026` · WebSearch → https://www.nyc.gov/assets/districting/downloads/pdf/20220817-Port-Richmond-Strong.pdf (WebFetch; testimony of Port Richmond Strong Civic Association president, Aug 17, 2022): 77 restaurants registered with NYC (self-reported advocacy claim). → Restaurants section (attributed to the civic association). No silive article retrieved: local news EMPTY.
- https://www.nyc.gov/assets/bic/downloads/pdf/flag-container-customer-list.pdf (Firecrawl excerpt; BIC customer list) → shows taquerias, delis, grocery on Port Richmond Ave; used only to support the "Taquerias, Pizzerias, Delis and Bodegas" heading (Denino's Pizza Tavern named in the BOA presentation). Phone numbers in it NOT used.
- https://newyorkyimby.com/2018/08/permits-filed-for-41-port-richmond-avenue-elm-park-staten-island.html (WebFetch): 15-unit building, YIMBY labels it Elm Park → NOT used (neighborhood attribution ambiguous).

### Flooding / storms
- Query: `Port Richmond Staten Island Hurricane Sandy flooding Richmond Terrace waterfront businesses` · WebSearch → https://www.dnainfo.com/new-york/20121220/mariners-harbor/staten-islands-north-shore-businesses-feel-forgotten-after-sandy/slideshow/320470 (WebFetch, Dec 20, 2012): Richmond Terrace in Mariners Harbor (west of Port Richmond); Margarella: surge topped his 8-foot seawall; Villa Marin building gutted. → Waterfront section (stated as Mariners Harbor, "a few minutes west").
- Silo sources reused: 2013 power-lines study (SI 72% overhead; Queens 22%, Brooklyn 12%) → §5.5, §10.5 H3 5, Storms section; Con Edison Isaias 2020 (29,000 SI customers) → Storms section.

### Local licensing / permits
- Silo sources reused: DOB low-voltage permit statement, firestopping, LPC permits, New York 811 (https://newyork-811.com/excavators/) → §8.5 callouts, process step 2, Waterfront section.
- Port Richmond has individual landmarks but no historic district (HDC page; Wikipedia) → §8.5 Landmarks callout.
- Broadband subscription by CD1: query `Staten Island Community District 1 broadband internet subscription percent households without home internet` · WebSearch → only citywide reports (OSC, Comptroller 2015); no CD1 figure retrieved. EMPTY, not used.

### Pricing used (copied verbatim from fiber-optic-installation-staten-island.html; no new prices)
$39 termination · $44 OTDR/strand · $385 MM drop · $440 SM drop · $4,950–$7,700 12-strand OM4 · $8,800–$16,500+ 24-strand OS2 / building-to-building · from $2,640 second telecom room · $195/hr, 3-hr min ($585). Packages = sums of lines: Starter 2 × $440 = $880; Standard = OM4 line; Premium = OS2 line; BYOE = $195/hr. Inherits the parent's open $411/$470 configurator conflict.

### Images (11) — permanent image rule (Drive folder `AESS Website Photos/Fiber Optic Installation` empty per main run 17:28Z; CompanyCam not connected)
All cropped (faces, shirt/cap phone numbers, a cable-map document removed) and saved as WebP q80, ≤1600 px. Every borrowed library copy in images/fiber-optic-installation/ is currently unused by live pages (all 31 live pages show the 20 aess-* photos), so none of these scenes is on a live sibling; batch siblings Flatiron and Mott Haven use some of the same source scenes (fusion splice, splice tray, conduit, before/after, brick enclosure, fish line, J-hooks) under their own crops.
| New file (images/fiber-optic-installation/) | Source |
|---|---|
| fiber-optic-installation-port-richmond-fusion-splicer-rack-jumpers.webp | low-voltage/low-voltage-installation-brooklyn-fiber-fusion-splice.jpg (crop 640,330–1400,1120) |
| fiber-optic-installation-port-richmond-storefront-ceiling-pull.webp | low-voltage/low-voltage-installation-brooklyn-retail-store-ceiling-pull.jpg (crop 560,0–1180,1120) |
| fiber-optic-installation-port-richmond-exterior-brick-enclosure-conduit.webp | low-voltage/low-voltage-installation-nassau-county-exterior-enclosure-install.jpg (crop 720,0–1400,1120) |
| fiber-optic-installation-port-richmond-link-tester-pass-rack.webp | network/network-installation-bronx-fluke-dsx-certification-pass.webp (crop 0,0–950,1086) |
| fiber-optic-installation-port-richmond-wall-opening-fish-rod.webp | network/network-installation-bronx-retrofit-wall-fish-data-drop.webp (crop 780,0–1448,1086) |
| fiber-optic-installation-port-richmond-high-bay-wire-basket-tray.webp | low-voltage/low-voltage-installation-bronx-hero-warehouse-cable-tray.jpg (crop 600,0–1400,1120) |
| fiber-optic-installation-port-richmond-emt-conduit-block-wall-pull.webp | network/network-installation-bronx-network-drop-conduit-emt-riser.webp (crop 560,0–1448,1086) |
| fiber-optic-installation-port-richmond-splicer-adapter-panel.webp | low-voltage/low-voltage-installation-brooklyn-fiber-splice-tray.jpg (crop 720,0–1400,1000) |
| fiber-optic-installation-port-richmond-hammer-drill-block-wall-sleeve.webp | network/network-installation-bronx-core-drill-cmu-wall-penetration.webp (crop 600,0–1448,1086) |
| fiber-optic-installation-port-richmond-closet-before-after.webp | network/network-installation-bronx-network-rack-cleanup-before-after.webp (uncropped) |
| fiber-optic-installation-port-richmond-j-hook-ceiling-bundles.webp | network/network-installation-bronx-jhook-ceiling-pathway-bundles.webp (crop 480,0–1448,900) |
Library photos look AI-rendered (garbled small text on screens/labels) — flagged again for Anwar. Copper certifier, Cat6 boxes and a dome camera are visible in some frames; captions say so and call them library photos.

### Keyword plan (Port Richmond page)
Service: fiber optic installation Port Richmond, storefront fiber, yard fiber link, building-to-building fiber, fusion splicing, OTDR testing, fiber repair. Problem: renting merchant/landlord approval, shared cellar, pressed-metal ceiling, slab store with no cellar, flood zone A yard, contaminated ground/no-dig, storm-downed aerial drops, shop and family apartment on one account. Technology: OS2, OM4, water-blocked indoor/outdoor, armored, all-dielectric, media converter, SFP, wall enclosure, fish rod, expansion fitting. Industry: restaurants/delis, auto and body shops, scale houses/C&D yards, maritime support, day cares, churches/community groups, showrooms. Geographic: Port Richmond, Port Richmond Avenue, Richmond Terrace, Forest Avenue, Castleton Avenue, Heberton Avenue, Bennett Street, Cottage Place, Post Avenue, Kill Van Kull, Bayonne Bridge, Elm Park, Mariners Harbor, West Brighton, Westerleigh, North Shore.

### Question register additions
fiber-optic-installation-port-richmond-staten-island-ny
§9 Questions Answered:
- Our storefront still has its old pressed-metal ceiling — can fiber get to the back of the shop without cutting into it?
- Our family's shop and our apartment upstairs share one internet account — how do we split them onto separate, separately billed lines?
- Our one-storey store is built on a slab with no cellar — where does the provider's line come in, and where does our equipment go?
- Our showroom fills one big hall with a finished ceiling we can't open — how does fiber reach a sales desk standing in the middle of the floor?
- Our yard's truck scale and scale house sit by the gate, a long way from the office — can fiber connect the scale terminal to the office computer?
- Can a fiber run go into an auto-body paint booth, or does it have to stop outside?
- Our building north of Richmond Terrace is due to be flood-proofed in the next few years — what fiber work should go in now, and what should wait?
- We run a licensed day care on the ground floor — how is fiber run so children can't reach the cable or the equipment?
§17 FAQ:
- Do you also cover Elm Park, Mariners Harbor, West Brighton and Westerleigh, next door to Port Richmond?
- Does armored fiber have to be grounded, and who does that?
- Will the router and switch we already have plug into the new fiber, or do we need new hardware?
- How do you keep a new fiber run from being cut by the next electrician or contractor who opens the wall?
- Will plastic conduit on a sunny brick wall expand and pull apart in summer?
- Does fiber need routine maintenance after it's installed?
- Will your crew need to park in front of our store, and for how long?
- Does fiber make our card terminals process payments faster?

De-dup notes: checked by keyword grep against all 722 questions on the 33 fiber pages on disk (incl. batch siblings at 17:48). Dropped during planning because the intent already exists: provider line through a cellar rented to another store (DUMBO "through other tenants' spaces", Flushing podium, SI strip-unit ceiling), private fiber across a city street (Rockland "across a county road"), knob-and-tube/old wiring (Brooklyn "next to electrical wiring in an old house"), previous tenant's leftover fiber (Port Morris), lease-end ownership (Port Morris/NYC/Manhattan), salt air (Long Island), poles (Long Island), rear wing crawlspace (Long Island attic/crawlspace), wall space for enclosure (Queens), site-walk charge (Suffolk), phases over budget years (Bronx — budget staging kept as body text only), restaurant kitchen heat (Nassau — kept as body text only). Closest remaining intents for the main run to judge: showroom mid-floor desk vs Bronx "hall with a very high, column-free ceiling" (support overhead vs reaching a mid-floor point with no ceiling access); flood-proofing sequencing vs SI parent "house raised after Sandy — where should equipment go now" (before vs after elevation); shop/apartment split vs Westchester "tenants share a backbone without sharing a network" (one family's business vs household accounts); maintenance vs Dutchess "clean and inspect connectors on links you are keeping" (owner care vs audit service); router compatibility vs Dutchess ST-connector/modern-switch question (existing hardware vs legacy connectors).
Content notes: masked paragraph similarity (difflib on ≥12-word p/li/td/h3/figcaption, protected NAP/warranty/stamp/price cells excluded) max 0.620 vs Fordham hero caption (same source photo described); file 236,696 B (JSON-LD indent 15 + 16-source citation array to reach the reserved slot).


<!-- batch 2026-10-17T17:27Z: fiber-optic-installation-flatiron-manhattan-ny -->
## Flatiron, Manhattan — local research (2026-10-17 batch, fiber-optic-installation-flatiron-manhattan-ny)

Up-link /fiber-optic-installation-manhattan · direct line (929) 560-0737 · GBP Bronx · prices = Manhattan parent lines verbatim (1.25×).

**Thesis (distinct from Midtown = vertical stack, Chelsea = carrier hotels/freight terminals/galleries, FiDi = flood/conversion/perimeter):** Flatiron companies grow in jumps inside pre-WWI store-and-loft buildings — spec suites on short leases, expansion onto the floor above, re-demising and sublets, a premium AI corridor (Park Ave South / Madison Square) beside a value loft district (Sixth Ave / side streets) — so fiber is planned per suite with spare strands for the next floor; plus Ladies' Mile facade rules, plaza-fronting curbs, the 2018 steam-pipe closure and office-to-condo conversions (Flatiron Building).

### Research matrix (query · platform · URL · finding · page + section used)

1. `Ladies' Mile Historic District designated 1989 buildings Flatiron` · WebSearch → Firecrawl scrape (summary) · https://en.wikipedia.org/wiki/Ladies%27_Mile_Historic_District · designated May 1989 by LPC; 440 buildings on 28 blocks/parts of blocks, roughly 15th–24th St, Park Ave South to west of Sixth Ave; campaign by Drive to Protect the Ladies' Mile District and Historic Districts Council; mostly multi-storey store and loft buildings; carriage-trade shopping Civil War–WWI · Neighbourhood §5 + figures list; "Fiber Behind 440 Protected Facades"; Coverage card.
2. `Flatiron Building residential conversion condos 2026` · WebSearch → Firecrawl scrape · https://therealdeal.com/new-york/2025/06/26/flatiron-building-conversion-takes-shape · plans filed with AG: 38 condos, 2 commercial units, 40 storage units; Brodsky Organization + Sorgente Group (SLCE, Studio Sofield); earlier reports said ~60 units; Gural-led group won 2023 auction at $160M; completion estimated 2026 · figures list; Conversions section; Coverage card.
3. `Flatiron NoMad Partnership district office square feet tech companies report` · WebSearch → Firecrawl scrape (PDF) · https://www.flatironnomad.nyc/wp-content/uploads/2025/02/2022-Annual-Trending-Report_Flatiron_NoMad_Partnership.pdf · BID since 2006, renamed Flatiron NoMad Partnership 2022; 36M sq ft commercial ("on par with Miami"), 7,000+ office tenants, 1,100+ ground-floor businesses; TAMI largest sector, "Silicon Alley"; major tenants IBM, Mastercard, New York Life, Nike, Credit Suisse, Tiffany, Sony, Capital One, SeatGeek, FanDuel, Betterment, Dropbox; plazas since 2008, upwards of 100,000 people stop daily; Broadway 21st–23rd shared street 2021 (city's largest); 6.2-acre Madison Square Park (Conservancy); 3 historic districts (Ladies' Mile, Madison Square North, Gramercy Park); Toy Center 200 Fifth + 1107 Broadway repurposed to retail/office/residential; conversions 212 & 225 Fifth, 1107 Broadway (10 Madison Square West); 35,000+ residents; 400+ F&B (over 1 in 3 businesses); 70+ furniture/design stores, ~40% of retail shops furniture/interior design; Porcelanosa US flagship at 202 Fifth; Eataly US debut 2010, LEGO 2014; Harry Potter NY, FRIENDS Experience; 2018 steam pipe explosion named as a crisis · Neighbourhood §5; Commercial; Street; July 2018; Ground Floors; Engineering Floors; Conversions; Coverage.
4. `Flatiron NoMad Partnership 2025 annual report office leasing vacancy pre-built suites` · WebSearch → Firecrawl scrape · https://flatironnomad.nyc/newsletter/february-5-2026-flatiron-nomad-economic-development-snapshot-q4-2025/ · 2025 office leasing >3.8M sq ft; employee visits 81% of pre-pandemic; vacancy fell 15% → 12% · Neighbourhood §5 + figures; Street section.
5. `Flatiron office buildings small floor plates loft tech tenants Midtown South sublease availability 2025` · WebSearch → Firecrawl scrape · https://www.metro-manhattan.com/neighborhoods/midtown-south/flatiron/ (market data Q1 2026, citing Newmark/Colliers/Savills) · Flatiron/Union Sq availability 13.9% vs Midtown South 16.9% (Newmark 1Q26); Ramp 285,300 SF at 28-40 W 23rd (largest Midtown South Q1 2026 lease); Clay 163,000 SF at 11 Madison, building 100% leased; Harvey AI expanded ~185,000 SF at One Madison; "two markets wearing one name"; Savills Flatiron $64.66/SF vs Park Ave South $77.50/SF (Q4 2025); spec suites "with furniture and cabling already in place so you can move in fast"; "Sign one month, move in the next"; "Class describes the building. Rent tier describes what tenants pay."; "the loft floor plates suit fast-growing engineering teams"; side streets W 18th–22nd 1,500–15,000 SF inventory; Manhattan sublet availability down nearly 30% (Colliers Q1 2026); Microsoft at 122 Fifth; 225 Park Ave South = 19-storey American Woolen Building; 11 Madison = former Metropolitan Life North Building · Neighbourhood §5; Building cards; Commercial; Growth Spurts; Spec Suites; Two Markets; Engineering Floors; AI Reality Check H3 1, 4, 6, 7; Coverage.
6. `2018 steam pipe explosion Fifth Avenue 21st Street Flatiron buildings evacuated asbestos` · WebSearch → Firecrawl scrape (summary) · https://api-demo.gothamist.com/news/steam-pipe-explosion-spewed-asbestos-into-flatiron-district (Gothamist mirror) · July 19, 2018 steam pipe burst at Fifth Ave & 21st St; >25 buildings evacuated; pipe insulation contained asbestos; people told to bag clothes and shower; Fifth Ave 19th–22nd St closed several days · "The Day Fifth Avenue Closed".
7. `Broadway Vision Flatiron plazas permanent reconstruction 2025 2026 construction Broadway 21st to 23rd` · WebSearch → Firecrawl scrape (PDF) · https://www.nyc.gov/html/dot/downloads/pdf/broadway-vision-cb5-sept2026.pdf · DDC/AECOM/DOT "Reconstruction of Flatiron Plazas and Worth Square", CB5 Sept 2026: interim plazas 2008; $375M public space funding 2023; final design 2025–; construction to commence FY28; Broadway 25th–27th converted to plaza blocks 2021–25; block Broadway 22nd–23rd: ~70 vehicles AM / 90 PM, no major property entrances, loading docks or driveways, access via Fifth Ave and 22nd St; "NYC DOT can work with property owners to maintain critical access for repairs, move ins/outs"; plaza workshops Oct 14–15 · Street section; Q&A (plaza reconstruction 2028); Coverage card.
8. `Silicon Alley history Flatiron District 1990s internet startups origin name` · WebSearch → Firecrawl scrape (summary) · https://flatironnomad.nyc/history/the-launch-of-silicon-alley/ · Silicon Alley emerged in the 1990s dot-com boom around Flatiron with internet/media start-ups and VCs (Flatiron Partners); bust after 2001; revival late 2000s · Neighbourhood §5 para 1.
9. `Madison Square Park Conservancy 6.2 acres founded park history 1847` · WebSearch → Firecrawl scrape (summary) · https://en.wikipedia.org/wiki/Madison_Square_and_Madison_Square_Park · 6.2-acre park at Fifth Ave/Broadway/23rd St; Flatiron Building adjacent · Coverage card.
10. `LPC permit not required interior work historic district building rooftop equipment visible Landmarks rules mechanical equipment` · WebSearch → Firecrawl scrape (PDF, directQuote) · https://home4.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter3_Storefronts.pdf · "an LPC permit is required for any elements of the outdoor dining setup that attach to the building, storefront, or sidewalk paving (including awnings, light fixtures, signage, conduit, etc.)"; "Conduit or other wiring that is extended from a building to an outdoor dining area at the sidewalk or roadway requires a permit from LPC" · Compliance callouts; Ladies' Mile section; Ground Floors; Q&A (outdoor seating terminals).
11. `prebuilt spec suite "plug and play" office New York cabling included move in tenants article` · WebSearch → Firecrawl scrape (directQuote) · https://www.loopnet.com/cre-explained/getting-started/spec-suites-a-powerful-tool-in-the-battle-to-fill-office-space/ (2023, national) · "the ability to be up and operating in 30 to 60 days"; "some landlords provide cabling, which is a true value" (Dallas broker); spec suites expedite lease-up; landlords "open to shorter-term leases of three to five years"; tenants avoid "designing, building and having somebody on staff coordinate with contractors" · Spec Suites section; AI Reality Check H3 2, 3, 5.
12. `fiber optic installation cost per foot commercial Angi OR Fixr OR HomeAdvisor 2025` · WebSearch → Firecrawl scrape · https://unio.digital/blog/fiber-optic-installation-cost · $1–$6/ft, $300–$800/drop, $15k–$30k whole building — NOT USED (already quoted on Stapleton, Orange, NYC, Manhattan, Hudson Valley pages; dropped to avoid repeating a sibling's reality-check claim).
13. Reddit: `site:reddit.com Flatiron office building internet outage fiber` · Firecrawl search · results were other cities / unrelated (r/crownheights, r/AskOldPeople Flatiron Building 1993 anecdote) — **EMPTY** for Flatiron fiber concerns; nothing used.
14. `reddit Flatiron office internet fiber building wired startup` · WebSearch · listing sites only (LoopNet, Showcase) — EMPTY for resident/tenant concerns.

### Sources EMPTY (not accessible in build env)
Google PAA · Google PASF · Answer the Public · Google AI Overview · Bing & DuckDuckGo PAA/autocomplete · Yelp 1–3★ — **EMPTY (not accessible in build env)**. Local Reddit — EMPTY (no relevant results). Hyperlocal news beyond the 2018 steam-pipe reports — not searched further (news.google.com blocked by proxy).

### Unsourced practice statements on the page (AESS working routine, flag for Anwar)
Walk "under an hour" for one floor; proposal "within a few business days"; label by suite not company; photograph every sealed opening; one booked freight trip early morning; reserve spare strands for expansion floor and price optional link; light-source check on BYOE reels; strand table as CSV on request; "we stop and report" suspect asbestos material; TI-allowance applicability stated generally ("check with your broker or attorney").

### Pricing used (Manhattan parent, verbatim)
$44 termination · $50 OTDR/strand · $453 MM drop · $517 SM drop · $5,625–$8,750 12-strand OM4 · $10,000–$18,750+ 24-strand OS2 · from $3,000 second telecom room · $195/hr, 3-hr min ($585). Packages = sums: Starter 2×$517 + 2×$50 = $1,134; Standard $5,625–$8,750 + 12×$50 = $6,225–$9,350; Premium $10,000–$18,750+ + from $3,000 = from $13,000.

### Images (11) — permanent image rule (Drive folder empty at 17:28Z per main run; CompanyCam not connected)
All copied/cropped to WebP q80 into images/fiber-optic-installation/; faces, shirt phone numbers and wall poster number cropped out; library photos look AI-rendered (uniform logo shirts) — Anwar to review. None of these source frames are used on the Manhattan/Chelsea/Midtown/FiDi fiber pages (those use the aess-* set).
| New file | Source | Crop |
|---|---|---|
| fiber-optic-installation-flatiron-fusion-splicer-bench.webp (hero) | images/low-voltage/low-voltage-installation-brooklyn-fiber-fusion-splice.jpg | right/lower 50%×70% (face + shirt number removed) |
| fiber-optic-installation-flatiron-splice-tray-panel.webp | images/low-voltage/low-voltage-installation-brooklyn-fiber-splice-tray.jpg | right 48% |
| fiber-optic-installation-flatiron-floor-closet-panel-build.webp | images/low-voltage/low-voltage-installation-brooklyn-idf-patch-panel-build.jpg | right half, top 62% (floor-plan sheet removed) |
| fiber-optic-installation-flatiron-riser-conduit-pull.webp | images/low-voltage/low-voltage-installation-nyc-riser-conduit-pull.jpg | right half, lower 75% |
| fiber-optic-installation-flatiron-emt-conduit-riser.webp | images/network/network-installation-bronx-network-drop-conduit-emt-riser.webp | right 55% |
| fiber-optic-installation-flatiron-jhook-ceiling-pathway.webp | images/network/network-installation-manhattan-jhook-ceiling-pathway-bundles.webp | right 64%, top 72% |
| fiber-optic-installation-flatiron-rack-cleanup-before-after.webp | images/network/network-installation-manhattan-network-rack-cleanup-before-after.webp | full frame (no person) |
| fiber-optic-installation-flatiron-finished-suite-rack.webp | images/network/network-installation-manhattan-finished-network-rack-firewall-ups.webp | left 55% (person + poster removed) |
| fiber-optic-installation-flatiron-core-drill-penetration.webp | images/network/network-installation-manhattan-core-drill-cmu-wall-penetration.webp | right 60% |
| fiber-optic-installation-flatiron-fit-out-floor-staging.webp | images/network/network-installation-manhattan-cat6-cable-box-staging-fitout.webp | left 60%, lower 74% |
| fiber-optic-installation-flatiron-inherited-cable-tracing.webp | images/network/network-installation-manhattan-network-cable-toner-tracing.webp | left 55% |
Note: most frames show copper/Cat6 pathway work, not fiber; alt/captions describe only what is visible (hero, splice-tray are fiber).

### Similarity
Masked paragraph similarity (difflib on geo-masked word lists, paragraphs ≥12 words, required constants excluded): max 0.597 vs fiber-optic-installation-jamaica-queens-ny (home-page link sentence); everything else < 0.59. Only 1.0 match is the required freshness/author stamp.

### Question register additions — fiber-optic-installation-flatiron-manhattan-ny
Q&A (H3):
- We signed a three-year lease on a pre-built suite — how much fiber is worth paying for in space we may outgrow?
- Our headcount could double within a year — can the fiber be planned now for a floor we have not leased yet?
- We own the building and want to split a full floor into two spec suites — how should the fiber be divided?
- We are leaving a coworking membership for our first floor of our own — what fiber did the coworking operator handle that we now need?
- Our loft floor is open, with brick walls and an exposed ceiling — where does the network cabinet go when there is no closet?
- Our building has one elevator for people and freight — how is a fiber pull scheduled around a single car?
- Our AI team runs GPU workstations in the office — does that change the fiber between our floors?
- Our hardware lab needs a network that never touches the office network — can fiber give it a separate path?
- Our restaurant faces the Broadway plaza — can a cable be run out to terminals at our outdoor seating?
- The city plans to rebuild the Flatiron plazas from 2028 — will that work affect the fiber entering buildings along Broadway?
- We are buying a condominium in a converted Flatiron office building — what should we ask about how internet reaches the unit?
FAQ:
- Do you also take fiber work in NoMad, Gramercy, Union Square and the blocks north of Madison Square Park?
- Can our landlord's tenant-improvement allowance pay for the fiber?
- Can fiber link our floor to the building's shared amenity floor or conference centre?
- If our company is acquired and moves out mid-lease, can the fiber stay for the subtenant or assignee who takes over?
- Can the strand map come as a spreadsheet our office-management software can import?
Question-form headings: Flatiron Floor Offline Before a Client Demo? · Planning the Next Floor Before You Need It? · Signing for Space in Flatiron This Quarter? · Two Flatiron Floors Not Talking Right Now?
Closest register neighbours checked by meaning and judged distinct: LIC/BNY "advertised as wired" (ours = spec-suite investment sizing for a short lease); Westchester "reassign strands when a tenant expands" (ours = reserve capacity before the floor is leased); DUMBO/Downtown Brooklyn/LIC coworking-floor layout (ours = tenant leaving coworking); Bloomfield/Bronx rack location (ours = open loft with no closet); FiDi freight-elevator duration (ours = single shared car); Manhattan lease/work-letter (ours = TI allowance funding); Port Morris/Hunts Point "take fiber with us" (ours = leave it for an assignee).
