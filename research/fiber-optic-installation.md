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
