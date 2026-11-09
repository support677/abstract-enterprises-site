# Research — Wireless Camera Installation (silo)

Created 2026-10-18 (batch 15, scheduled run) while rebuilding `wireless-camera-installation-hudson-valley` (REBUILD, was crawled-not-indexed). Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Sources that could not be reached are written EMPTY (not accessible in build env). "CARRIED" = fact and URL reused from another research file in this repo (file named), not re-fetched this run.

## 1. Research matrix (v2.3 §3, all 11 sources)

| # | Source | Status this run |
|---|---|---|
| 1 | Google People Also Ask | EMPTY (not accessible in build env) — no SERP feature capture available |
| 2 | People Also Search For | EMPTY (not accessible in build env) |
| 3 | Answer the Public | EMPTY (not accessible in build env) |
| 4 | Google AI Overview claims | EMPTY (not accessible in build env) — page section "What AI Gets Wrong" tests recurring claims from cost guides/product marketing instead, and says so on the page |
| 5 | Reddit | Partial — search excerpts only (see §3) |
| 6 | Yelp 1–3★ reviews | EMPTY (not accessible in build env) — Yelp search page surfaced only as a listing excerpt (https://m.yelp.com/search?cflt=securitysystems&find_loc=Hudson+Valley%2C+NY, "3.8 (874)"), no reviews readable; not used |
| 7 | Bing / DuckDuckGo SERPs | EMPTY (not accessible in build env) |
| 8 | Keyword layers | Built from queries and page needs (§4) — no keyword-volume tool used |
| 9 | Manufacturer / standards documents | Done (§2) |
| 10 | Government / regulatory | Done (§2, §5) |
| 11 | Local news / hyperlocal | Done (§5) |

## 2. Technology and rules facts (silo-wide)

- Query `Wi-Fi HaLow security camera long range kilometer farm Reolink HaLow` · Firecrawl search · https://www.lorex.com/pages/halow (excerpt) · "Wi-Fi HaLow's long distance range up to 500ft (150m) vs. the average Wi-Fi range of 100ft (30m)" · HV hub: Why §5 para 2; Q&A "How far…"; Q&A "Is Wi-Fi HaLow worth…". Same search: https://www.showmo365.com/2026/05/25/wi-fi-halow-security-camera-the-complete-2026-guide-802-11ah-range-explained/ (excerpt) "up to 1 mile (1.6 km) in open terrain" · used only as "other makers quote longer figures".
- Query `Ubiquiti UniFi Building-to-Building Bridge UBB range 500 m 60 GHz` · Firecrawl search · https://store.ui.com/us/en/products/ubb (excerpt "500 m (0.31 mi) Link Range"); https://www.streakwave.com/ubiquiti-networks-ubb-us-unifi-building-to-building-60ghz-us ("500 m (1,640 ft) maximum range") · HV hub: Services card "Point-to-point bridges"; Q&A "The barn is in plain sight…".
- Query `tree foliage leaves attenuate 2.4 GHz Wi-Fi signal outdoor wet leaves` · Firecrawl search · https://auf.isa-arbor.com/content/35/4/203 (excerpt, Arboriculture & Urban Forestry 35(4)): "Dalley and colleagues (1999) … a wet tree attenuated the signal considerably more (loss of 18 dB)" · HV hub: Why para 2; Q&A "Will the leaves coming out in May…"; Field Notes (season reasoning).
- Query `Ring battery camera cold weather will not charge below 32 degrees` · Firecrawl search · https://ring.com/support/articles/6nmmg/ring-devices-and-extreme-temperatures (excerpt): "Your device is designed to stop charging if the temperature is below freezing." · HV hub: Why para 4; AI section claim 1.
- Query `Arlo camera operating temperature battery cold -4F specifications` · Firecrawl search · https://www.arlo.com/en_gb/support/faq/arlo-app-and-automations/what-do-my-arlo-camera-s-battery-level-icons-and-notifications-mean (excerpt): "Batteries cannot charge safely in temperatures below 32°F (0°C) or above 113°F (45°C)." · HV hub: Why para 4; AI claim 1.
- Query `Ring solar panel how many hours of direct sunlight needed` · Firecrawl search · https://ring.com/support/articles/1h6ko/solar-panels-battery-doorbells ("three to four hours of direct sunlight a day"); https://ring.com/support/articles/7cjx4/Installing-a-solar-panel-with-your-security-camera ("minimum of four to six hours a day") · HV hub: Services card "Solar and battery"; Q&A "Which way should a camera's solar panel face…"; AI claim 2.
- Query `Reolink 4G LTE camera requirements SIM card signal strength Go Plus` · Firecrawl search · https://reolink.com/blog/reolink-sim-card-guide/ ("require a nano SIM card and an active cellular data plan"); https://support.reolink.com/articles/360009756673-How-to-Choose-SIM-Card-for-Reolink-4G-Cameras/ ("Each Reolink 4G camera requires one SIM card. A SIM card cannot be shared by multiple cameras.") · HV hub: Services card "Cellular"; Q&A "The phone gets one bar…".
- Query `Airbnb policy ban indoor security cameras 2024` · Firecrawl search · https://www.airbnb.com/help/article/3061 (excerpt: no cameras monitoring "any part of a home's interior, such as the hallway, bedroom, bathroom, living room…even if they're turned off"; outdoor cameras not allowed where greater privacy expected "such as the inside of an enclosed outdoor shower or in a sauna"); https://news.airbnb.com/an-update-on-our-policy-on-security-cameras (ban on indoor cameras globally) · HV hub: Business "Short-term rentals"; Q&A "The house is rented out on weekends…".
- Query `Ring ends Request for Assistance police video requests January 2024 Neighbors app` + `Consumer Reports Ring Community Requests police Axon 2025` · Firecrawl search + scrape · https://www.consumerreports.org/electronics/privacy/ring-community-requests-lets-police-ask-for-user-videos-a2437818485/ (Sept 8 2025: Ring resumed letting police request footage via Community Requests; resembles program canceled in 2024; sharing voluntary; opt-out path in Neighbors feed settings); https://ring.com/support/articles/uds27/Community-request ("never automatically shared"; "Verified and Axon Evidence users") · HV hub: Q&A "If the police ask for footage…"; AI claim 5.
- Query `FCC covered list Hikvision Dahua new equipment authorization ban 2022 video surveillance` · Firecrawl search · https://www.fcc.gov/laboratory-division/equipment-authorization-approval-guide/equipment-authorization-system (excerpt: rules effective February 6, 2023; prohibition on authorization of covered video surveillance equipment by Hikvision, Dahua … "for the purpose of public safety, security of government facilities, physical security surveillance of critical infrastructure, and other national security purposes") · HV hub: Q&A "Are any camera brands restricted…".
- Query `FCC Cyber Trust Mark smart home cameras launched` · Firecrawl search · https://www.fcc.gov/CyberTrustMark ("Examples of eligible products include internet-connected home security cameras…"); https://www.netgear.com/hub/network/security/us-cyber-trust-mark/ (launched January 7 [2025]) · HV hub: Q&A "Are any camera brands restricted…" para 2.
- Query `New York eavesdropping law one-party consent audio recording security camera Penal Law 250.05` · Firecrawl search · https://www.rcfp.org/reporters-recording-guide/new-york/ ; https://www.nysenate.gov/legislation/laws/PEN/250.05 · NOT USED on HV hub (audio question already on NYC/LI hub FAQ — intent reserved there).
- Query `Angi cost to install wireless security cameras per camera 2025` · Firecrawl search · https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera.htm (2026 data: wireless cameras "$25 to $35 per camera"; professional installation "$100 and $200 per camera on top of the camera's purchase price") · HV hub: AI claim 3.

## 3. Market, Reddit and forum findings

- Query `reddit Hudson Valley security camera no internet rural property cellular trail camera` · Firecrawl search · https://www.reddit.com/r/SecurityCamera/comments/1kfb8gs/security_cameras_in_very_ruralremote_regions/ ("Most rural camera setups rely on either LTE trail cams. No internet needed…"); https://www.reddit.com/r/homesecurity/comments/1vu38al/security_cam_for_rural_cabin_no_wifi_or_4g_signal/ ("Get a Starlink dish…") · opinions only; informed Q&A "Our weekend house has no cable or fiber…" (satellite as an option, no Starlink facts stated).
- Query `reddit hudsonvalley security cameras recommendations house upstate` · Firecrawl search · https://www.reddit.com/r/Ubiquiti/comments/sr6f9s/looking_for_an_installer_in_the_hudson_valley_ny/ (owner asking for a Hudson Valley installer who uses Ubiquiti gear) · not quoted; supports bridge/Ubiquiti emphasis.
- r/hudsonvalley threads specifically about wireless cameras: EMPTY (none returned).

## 4. Keyword layers (five)

- **Service:** wireless camera installation, wireless security camera install, Wi-Fi camera installer, solar camera installation, 4G LTE camera install, video doorbell installation, floodlight camera installation.
- **Problem:** camera too far from router, barn camera no Wi-Fi, battery camera not charging in cold, camera offline after power outage, no internet security camera, deer motion alerts.
- **Technology:** point-to-point wireless bridge, Wi-Fi HaLow 802.11ah, outdoor access point, nano SIM LTE camera, solar panel for battery camera, base station local storage, UPS battery backup for router.
- **Industry/property:** farm, orchard, winery, horse barn, equipment yard, construction site, weekend house, short-term rental, lake house, village storefront, house of worship, camp.
- **Geographic:** Hudson Valley, Westchester, Rockland, Orange, Putnam, Dutchess, Ulster; towns named on page (Yonkers, White Plains, Bedford, Nyack, New City, Newburgh, Warwick, Mahopac, Cold Spring, Poughkeepsie, Beacon, Rhinebeck, Millbrook, Kingston, New Paltz, Woodstock …).

## 5. Hudson Valley

Thesis: north of the city "wireless" is a design problem of distance, internet availability, winter power and storms. Each camera's link (Wi-Fi / AP / bridge / HaLow / LTE), power (outlet / battery / solar for December) and storage (local + cloud) is planned and tested at the mounting spot; the system must survive a power cut.

- Query `Central Hudson Gas & Electric serves electric customers Mid-Hudson Valley square miles` · Firecrawl search · https://www.cenhud.com/en/about-us/our-service-territory/ ("approximately 315,000 electric customers … from the northern suburbs of New York City to the Capital District near Albany") · Why facts list bullet 1.
- Query `Orange and Rockland Utilities serves customers Rockland Orange Sullivan counties` · Firecrawl search · https://www.oru.com/en/about-us/media-center/corporate-facts ("approximately 300,000 electric customers in New York and northern New Jersey"; Orange, Rockland, Sullivan) · Why facts bullet 1.
- Query `Con Edison provides electric service New York City and Westchester County customers` · Firecrawl search · https://en.wikipedia.org/wiki/Consolidated_Edison (CECONY electric service in NYC and Westchester) · Why facts bullet 1; Counties "Westchester".
- CARRIED (research/video-wall-installation.md, Putnam section): Isaias 2020 — 34,150 of 38,693 NYSEG Putnam customers out · Why facts bullet 2; Counties "Putnam".
- CARRIED (research/parking-lot-camera-installation.md / sonos research, Rockland): https://rocklandtimes.com/2012/11/02/the-impact-of-hurricane-sandy/ — O&R "worst storm in company history", 230,000 outages · Why facts bullet 2.
- CARRIED: https://www.dailyfreeman.com/2026/07/05/nearly-50000-central-hudson-customers-without-power-after-storms-hit-region/ — nearly 50,000 Central Hudson customers out (July 2026) · Why para 5; Q&A battery backup.
- CARRIED: https://www.oru.com/en/about-us/media-center/news/2026/07-06/storm-outage-update-restored-power-to-more-than-45k — "more than 47,000 customers have been impacted" since July 1; Clarkstown and Ramapo among towns still out · Why para 5; Counties "Rockland".
- CARRIED: https://www.dailyfreeman.com/2026/09/27/noreaster-day-two-over-4000-central-hudson-customers-still-have-no-service/ — Central Hudson serves 93,209 Ulster customers; peak >14,000 out · Counties "Ulster".
- CARRIED: https://www.ulstercountyny.gov/Government/News/Newsroom/2025/09/2025-09-25-Funding-for-Broadband-Expansion — $20.8M ConnectALL; nearly 1,300 unserved households, businesses and community facilities; $61,799,320 total incl. $40,938,790 Verizon match · Why para 3; facts bullet 3.
- Query `New York Public Service Commission mobile cellular coverage study dead zones upstate 2024 drive test` · Firecrawl search + scrape · https://www.nyc.gov/site/dep/news/24-044/nyc-dep-intent-expand-wireless-communications-across-upstate-water-supply-region-and (Nov 25 2024; counties Delaware, Ulster, Schoharie, Orange, Greene, Sullivan, Putnam, Westchester, Dutchess; quote "Far too much of the watershed region remains a broadband and cellular black hole…") · Why para 3; AI claim 4. Same search: Schumer upstate dead-zone release (undated excerpt) — not used.
- CARRIED (Census QuickFacts, from research files for Westchester/Rockland/Dutchess/Orange): Westchester pop. 1,015,743; Rockland 357,397, 3.22 persons/household, owner-occupied 67.9%; Dutchess 300,708, owner-occupied 69.2%, broadband 93.5%; Orange broadband 89.3% · Why facts bullet 4; Counties sections.
- Query `NYSDEC deer population Hudson Valley Westchester deer density per square mile` · Firecrawl search · https://engage.ryeny.gov/32884/widgets/116581/documents/82980 (excerpt: overwinter deer density "estimated via pellet surveys at 50.1 deer/square mile, nearly 3 times the density required to ensure forest [health]") · Why facts bullet 5. https://www.irvingtongreen.org/land/deer (141.5/sq mi, advocacy site) — not used.
- Query `Hudson Valley package theft porch pirates police warning 2025` · Firecrawl search + scrape · https://hudsonvalley.news12.com/2025/10/10/carmel-police-warn-residents-about-porch-pirates-ahead-of-holiday-season-sales/4iCeCbof90EaTdTznQM2qs (Oct 10 2025; no mention of cameras) · not used.
- Query `Ulster County seasonal recreational occasional use housing units second homes Census` · Firecrawl search · no Hudson Valley county figure returned → EMPTY; page describes weekend houses without a statistic.
- Local licensing for low-voltage camera work by county: not researched this run (hub defers to county pages) — EMPTY.
- Landmarks/towns in "Near Hudson Valley Landmarks" are place and road names only (no claims).

## 6. Prices used (rule + source)

- HV hub keeps its own existing approved table unchanged (old wireless-camera-installation-hudson-valley.html, "Build / Use case / Installed price range"): doorbell $450–$850; 2-cam $850–$1,600; 4-cam $1,600–$3,200; 6-cam $2,400–$4,500; 8-cam $3,200–$6,400; 16-cam hybrid $6,500–$13,500; 32-cam $13,000–$27,000; solar +$150–$300 each; LTE +$200 + data plan; hub +$99–$299; service $195/hr 3-hr min ($585). Use-case text rewritten.
- FLAG: this table is ~1.33× the NYC hub table (4-cam $1,200–$2,400) and is not a §9 per-county multiplier; HV county pages quote a "typical 4-cam" of $1,870 (Westchester) and $2,020 (Dutchess). Old page's "$150–$300/camera labor", "1-year parts on labor", ADT/Ring/Vivint comparison and "Most NYC clients save $1,500 to $4,000" claims dropped (unsourced / conflicting wording).

## 7. Images (11) — permanent image rule

Drive "AESS Website Photos" has no wireless-camera subfolder (only Soundbar, Smart Lock, Fiber Optic, Cat6 Repair, Sonos); CompanyCam not connected. No real AESS wireless photos exist, so 11 manufacturer product photos of Wi-Fi/battery devices were converted to WebP in images/wireless-camera-installation/ (captions say "Manufacturer product photo, not an AESS job photo"):
- images/floodlight-eufy-e340.png → …-eufy-pan-tilt-floodlight-camera-product-photo.webp (hero)
- images/ring-video-doorbell.webp → …-ring-video-doorbell-satin-faceplate-product-photo.webp
- images/floodlight-google-nest.png → …-google-nest-floodlight-camera-product-photo.webp
- images/floodlight-ring-cam-plus.png → …-ring-twin-lamp-floodlight-camera-with-cord-product-photo.webp
- images/floodlight-wyze-pro.png → …-wyze-black-three-panel-floodlight-camera-product-photo.webp
- images/floodlight-lorex.png → …-lorex-twin-panel-floodlight-camera-product-photo.webp
- images/floodlight-blink-wired.png → …-blink-white-twin-lamp-floodlight-camera-product-photo.webp
- images/arlo-2k-video-doorbell.jpg → …-arlo-white-video-doorbell-product-photo.webp
- images/eufy-video-doorbell-2k.jpg → …-eufy-black-video-doorbell-product-photo.webp
- images/floodlight-tapo-c720.png → …-tapo-twin-lamp-floodlight-camera-product-photo.webp
- images/nest-doorbell-grey.webp → …-google-nest-green-video-doorbell-product-photo.webp
Excluded: images/wireless-camera-*.png (unbranded 1254×1254 renders — possibly AI-generated); AESS van/bucket-truck/trailer images (AI-generated); images/reolink-video-doorbell.webp (shows a Speco logo, filename mismatch); root job photos rockland-toyota/manhattan-deli/nassau-window-depot (used by today's Manhattan warehouse page, 300 px).

## 8. Unsourced practices (written as AESS method, not facts)

Analyser survey at mounting height; access point on the far side of stone houses; bridge-first then cameras; boot-order/power-cut test at handover; surge protection and grounding per manufacturer with electrician; camera under eaves away from roof-slide line; IR glare/floodlight advice; wildlife camera kept separate; privacy masks for neighbours; data-plan tuning after two weeks; seasonal brackets; theft-resistant pole mounts; remote pre-survey by video call; storm checklist; shared caretaker logins; handover sheet; openingHours not set in schema.

## 9. Question register

### wireless-camera-installation-hudson-valley (2026-10-18)
- Q&A: How far from the house can a camera go before ordinary Wi-Fi stops being the right way to connect it?
- Q&A: The barn is in plain sight of the house but about 600 feet away. What actually carries the video?
- Q&A: Will the leaves coming out in May change how a camera link behaves?
- Q&A: Is Wi-Fi HaLow worth considering for a gate at the end of a long driveway?
- Q&A: Our weekend house has no cable or fiber. Can cameras run over satellite internet instead?
- Q&A: The phone gets one bar at the house. Will a cellular camera work there?
- Q&A: How do cellular cameras avoid running up a large data bill?
- Q&A: Which way should a camera’s solar panel face, and what do we do about the trees?
- Q&A: After a power cut that lasts two days, will the cameras come back on by themselves?
- Q&A: What should go on battery backup so the cameras keep recording when the power goes?
- Q&A: Does lightning put outdoor cameras and bridges at risk?
- Q&A: Where should cameras go so snow, ice and driving rain don’t blind them?
- Q&A: Can one of the cameras watch the bird feeder or the wildlife without counting as a security camera?
- Q&A: The house is rented out on weekends. Where can the cameras go?
- Q&A: A camera at our gate would also see the neighbour’s driveway across the road. What should we do?
- Q&A: If the police ask for footage, do they get it automatically?
- Q&A: Are any camera brands restricted by the federal government?
- FAQ: Can you take cameras down for the winter and put them back up in spring for a seasonal business?
- FAQ: Can a camera at the mailbox tell us when the mail or a delivery arrives?
- FAQ: Can a caretaker or a neighbour who checks the house get access to some cameras but not others?
- FAQ: We are closing on a valley house next month. Can you plan the cameras before we move in?
- FAQ: Can the cameras warn us if a pipe freezes or the basement floods in an empty house?
- FAQ: What happens to the cameras and the accounts if we sell the house?
- FAQ: How do you keep a camera on a remote gate or pole from being stolen?
- FAQ: Can the driveway camera work with our electric gate?
- FAQ: Can you look at the property remotely before driving up?
- FAQ: What should we do with the cameras when a big storm is forecast?

### Existing questions on other wireless-camera pages (old template, as of 2026-10-18 — new pages must not repeat these intents)

    == wireless-camera-installation-bronx-ny.html 22
       Who installs wireless cameras in the Bronx?
       What is the best wireless camera for the Bronx?
       Where do I install a wireless camera on a Riverdale or Throgs Neck home?
       When should I replace a wireless camera battery in the Bronx?
       Why is my wireless camera offline in the Bronx?
       How long does wireless camera install take in the Bronx?
       Can I record audio on a Bronx wireless camera?
       Do Bronx wireless cameras work without Wi-Fi?
       Wireless Camera DIY vs Pro Install in the Bronx — What's Worth Hiring Out?
       How much does wireless camera installation cost in the Bronx?
       What brand of wireless camera do you recommend for a Riverdale Tudor or Throgs Neck detached home?
       Can a Bronx renter install a wireless camera without landlord permission?
       How long do wireless camera batteries last in Bronx winters?
       Do you install wireless cameras in Bronx NYCHA buildings — Mott Haven, Patterson, Castle Hill, Bronx River, Soundview?
       Can I view my Bronx wireless cameras from my phone?
       Do wireless cameras work in the Bronx during a Spectrum or Verizon Fios outage?
       Do you install wireless cameras for Bronx commercial properties?
       Can I record audio on a Bronx wireless camera?
       What if I already have wired cameras — can I add wireless cameras to my existing Bronx system?
       Do you install wireless camera systems for Bronx houses of worship — Catholic churches, synagogues, mosques, Hindu mandirs?
       Are you licensed and insured for wireless camera installation in the Bronx?
       🚨 Wireless Camera Down in the Bronx?
    == wireless-camera-installation-brooklyn-ny.html 22
       Who installs wireless cameras in Brooklyn?
       What is the best wireless camera for Brooklyn?
       Where do I install a wireless camera in a Brooklyn brownstone?
       When should I replace a wireless camera battery in Brooklyn?
       Why is my wireless camera offline in Brooklyn?
       How long does wireless camera install take in Brooklyn?
       Can I record audio on a Brooklyn wireless camera?
       Do Brooklyn wireless cameras work without Wi-Fi?
       Wireless Camera DIY vs Pro Install in Brooklyn — What's Worth Hiring Out?
       How much does wireless camera installation cost in Brooklyn?
       What brand of wireless camera do you recommend for a Brooklyn brownstone?
       Can a Brooklyn renter install a wireless camera without landlord permission?
       How long do wireless camera batteries last in Brooklyn?
       Do you install wireless cameras in NYCHA buildings?
       Can I view my Brooklyn wireless cameras from my phone?
       Do wireless cameras work in Brooklyn during a Spectrum or Verizon Fios outage?
       Do you install wireless cameras for Brooklyn commercial properties?
       Can I record audio on a Brooklyn wireless camera?
       What if I already have wired cameras — can I add wireless cameras to my existing Brooklyn system?
       Do you install wireless camera systems for Brooklyn houses of worship?
       Are you licensed and insured for wireless camera installation in Brooklyn?
       🚨 Wireless Camera Down in Brooklyn?
    == wireless-camera-installation-brooklyn.html 0
    == wireless-camera-installation-dutchess-county.html 20
       Ready to talk through your Dutchess County install?
       Best wireless camera for Dutchess County?
       How much for wireless camera install Dutchess County?
       Wireless or wired cameras for Dutchess County?
       Wireless camera no monthly fee Dutchess County?
       Solar wireless camera Dutchess County?
       4G LTE camera install Dutchess County?
       Wireless camera installer near me Dutchess County?
       Wireless Camera DIY vs Pro Install in Dutchess County — What's Worth Hiring Out?
       Ready to talk through your Dutchess County install?
       How much does wireless camera install cost in Dutchess County?
       What brands do you install in Dutchess County?
       Do I need monthly fees for Dutchess County wireless cameras?
       How long does install take?
       Can Dutchess County renters install wireless cameras?
       Do you handle Dutchess County HOA / co-op approval?
       Same-day install in Dutchess County?
       Will my Wi-Fi handle 4 cameras?
       4G LTE camera install in Dutchess County?
       What's the 3-year warranty cover in Dutchess County?
    == wireless-camera-installation-long-island.html 30
       Q1: What's a fair price for wireless camera install in NYC, and where does the money actually go?
       Q2: What hidden fees should I watch for on a wireless camera quote?
       Q3: Do the no-subscription cameras really skip monthly fees forever?
       Q4: How do I tell a real licensed NYC wireless installer from a Craigslist guy with a drill?
       Q5: What wireless camera brands do actual installers trust, versus what the reviews push?
       Q6: Wireless cameras are sold as plug-and-play. Why pay an installer at all?
       Q7: What are the biggest mistakes NYC DIYers make installing wireless cameras themselves?
       Q8: How do wireless cameras hold up in a NYC apartment building with 40+ competing Wi-Fi networks?
       Q9: Will my wireless camera battery survive a NYC winter on the side of the house?
       Q10: What happens to my wireless camera when the internet goes down?
       Q11: I own a single-family home on Long Island with a pool and a 2-car garage. What's the right wireless camera setup?
       Q12: I run a small business in downtown Patchogue, Sayville, Huntington, or Sag Harbor. Do I need a different wireless camera setup than for a home?
       Q13: Why do my wireless cameras keep dropping offline, and is it the camera or the Wi-Fi?
       Q14: Why do my wireless cameras alert constantly on nothing, and can it be fixed?
       Ready for a real wireless camera plan, not a national average?
       🚨 Need wireless camera repair on Long Island today?
       1. Does Abstract Enterprises install all wireless camera brands or only certain ones?
       2. Do you offer wireless cameras with no monthly fees at all?
       3. How long does a wireless camera install take in NYC?
       4. Do wireless cameras work in pre-war NYC buildings with thick walls?
       5. Are wireless cameras reliable enough for commercial properties?
       6. Will my landlord, co-op, or condo board allow a wireless camera install?
       7. Can you install wireless cameras without drilling holes?
       8. What's the warranty on wireless camera installations from Abstract Enterprises?
       9. Do you install solar-powered wireless cameras?
       10. Can wireless cameras integrate with my existing alarm or intercom system?
       11. Will my wireless cameras record audio, and is that legal in New York?
       12. Do I need a license to install wireless cameras in NYC as the property owner?
       Have a wireless camera question we didn't cover?
       🚨 Existing wireless system not working on Long Island?
    == wireless-camera-installation-manhattan.html 5
       🔧 Wireless Camera Not Working in Manhattan?
       Ready to Schedule Your Manhattan Install?
       Still Have Questions?
       Ready to Get Started?
       🔧 Wireless Camera Already Installed and Failing in Manhattan?
    == wireless-camera-installation-nassau-county.html 20
       Ready to talk through your Nassau County install?
       Best wireless camera for Nassau County?
       How much for wireless camera install Nassau County?
       Wireless or wired cameras for Nassau County?
       Wireless camera no monthly fee Nassau County?
       Solar wireless camera Nassau County?
       4G LTE camera install Nassau County?
       Wireless camera installer near me Nassau County?
       Wireless Camera DIY vs Pro Install in Nassau County — What's Worth Hiring Out?
       Ready to talk through your Nassau County install?
       How much does wireless camera install cost in Nassau County?
       What brands do you install in Nassau County?
       Do I need monthly fees for Nassau County wireless cameras?
       How long does install take?
       Can Nassau County renters install wireless cameras?
       Do you handle Nassau County HOA / co-op approval?
       Same-day install in Nassau County?
       Will my Wi-Fi handle 4 cameras?
       4G LTE camera install in Nassau County?
       What's the 3-year warranty cover in Nassau County?
    == wireless-camera-installation-nyc.html 30
       Q1: What's a fair price for wireless camera install in NYC, and where does the money actually go?
       Q2: What hidden fees should I watch for on a wireless camera quote?
       Q3: Do the no-subscription cameras really skip monthly fees forever?
       Q4: How do I tell a real licensed NYC wireless installer from a Craigslist guy with a drill?
       Q5: What wireless camera brands do actual installers trust, versus what the reviews push?
       Q6: Wireless cameras are sold as plug-and-play. Why pay an installer at all?
       Q7: What are the biggest mistakes NYC DIYers make installing wireless cameras themselves?
       Q8: How do wireless cameras hold up in a NYC apartment building with 40+ competing Wi-Fi networks?
       Q9: Will my wireless camera battery survive a NYC winter on the side of the house?
       Q10: What happens to my wireless camera when the internet goes down?
       Q11: I rent an apartment in NYC. Can I install wireless cameras without my landlord's permission?
       Q12: As a landlord, can I install wireless cameras in the hallways and lobby of my NYC building?
       Q13: Why do my wireless cameras keep dropping offline, and is it the camera or the Wi-Fi?
       Q14: Why do my wireless cameras alert constantly on nothing, and can it be fixed?
       Ready for a real wireless camera plan, not a national average?
       🚨 Need wireless camera repair in NYC today?
       1. Does Abstract Enterprises install all wireless camera brands or only certain ones?
       2. Do you offer wireless cameras with no monthly fees at all?
       3. How long does a wireless camera install take in NYC?
       4. Do wireless cameras work in pre-war NYC buildings with thick walls?
       5. Are wireless cameras reliable enough for commercial properties?
       6. Will my landlord, co-op, or condo board allow a wireless camera install?
       7. Can you install wireless cameras without drilling holes?
       8. What's the warranty on wireless camera installations from Abstract Enterprises?
       9. Do you install solar-powered wireless cameras?
       10. Can wireless cameras integrate with my existing alarm or intercom system?
       11. Will my wireless cameras record audio, and is that legal in New York?
       12. Do I need a license to install wireless cameras in NYC as the property owner?
       Have a wireless camera question we didn't cover?
       🚨 Existing wireless system not working in NYC?
    == wireless-camera-installation-orange-county.html 20
       Ready to talk through your Orange County NY install?
       Best wireless camera for Orange County NY?
       How much for wireless camera install Orange County NY?
       Wireless or wired cameras for Orange County NY?
       Wireless camera no monthly fee Orange County NY?
       Solar wireless camera Orange County NY?
       4G LTE camera install Orange County NY?
       Wireless camera installer near me Orange County NY?
       Wireless Camera DIY vs Pro Install in Orange County NY — What's Worth Hiring Out?
       Ready to talk through your Orange County NY install?
       How much does wireless camera install cost in Orange County NY?
       What brands do you install in Orange County NY?
       Do I need monthly fees for Orange County NY wireless cameras?
       How long does install take?
       Can Orange County NY renters install wireless cameras?
       Do you handle Orange County NY HOA / co-op approval?
       Same-day install in Orange County NY?
       Will my Wi-Fi handle 4 cameras?
       4G LTE camera install in Orange County NY?
       What's the 3-year warranty cover in Orange County NY?
    == wireless-camera-installation-putnam-county.html 20
       Ready to talk through your Putnam County install?
       Best wireless camera for Putnam County?
       How much for wireless camera install Putnam County?
       Wireless or wired cameras for Putnam County?
       Wireless camera no monthly fee Putnam County?
       Solar wireless camera Putnam County?
       4G LTE camera install Putnam County?
       Wireless camera installer near me Putnam County?
       Wireless Camera DIY vs Pro Install in Putnam County — What's Worth Hiring Out?
       Ready to talk through your Putnam County install?
       How much does wireless camera install cost in Putnam County?
       What brands do you install in Putnam County?
       Do I need monthly fees for Putnam County wireless cameras?
       How long does install take?
       Can Putnam County renters install wireless cameras?
       Do you handle Putnam County HOA / co-op approval?
       Same-day install in Putnam County?
       Will my Wi-Fi handle 4 cameras?
       4G LTE camera install in Putnam County?
       What's the 3-year warranty cover in Putnam County?
    == wireless-camera-installation-queens-ny.html 22
       Who installs wireless cameras in Queens?
       What is the best wireless camera for Queens?
       Where do I install a wireless camera on a Bayside or Whitestone home?
       When should I replace a wireless camera battery in Queens?
       Why is my wireless camera offline in Queens?
       How long does wireless camera install take in Queens?
       Can I record audio on a Queens wireless camera?
       Do Queens wireless cameras work without Wi-Fi?
       Wireless Camera DIY vs Pro Install in Queens — What's Worth Hiring Out?
       How much does wireless camera installation cost in Queens?
       What brand of wireless camera do you recommend for a Forest Hills Tudor or Bayside detached home?
       Can a Queens renter install a wireless camera without landlord permission?
       How long do wireless camera batteries last in Queens winters?
       Do you install wireless cameras in NYCHA buildings — Queensbridge, Astoria Houses, Pomonok, Ravenswood?
       Can I view my Queens wireless cameras from my phone?
       Do wireless cameras work in Queens during a Spectrum or Verizon Fios outage?
       Do you install wireless cameras for Queens commercial properties?
       Can I record audio on a Queens wireless camera?
       What if I already have wired cameras — can I add wireless cameras to my existing Queens system?
       Do you install wireless camera systems for Queens houses of worship — churches, synagogues, mosques, mandirs, gurdwaras?
       Are you licensed and insured for wireless camera installation in Queens?
       🚨 Wireless Camera Down in Queens?
    == wireless-camera-installation-rockland-county.html 20
       Ready to talk through your Rockland County install?
       Best wireless camera for Rockland County?
       How much for wireless camera install Rockland County?
       Wireless or wired cameras for Rockland County?
       Wireless camera no monthly fee Rockland County?
       Solar wireless camera Rockland County?
       4G LTE camera install Rockland County?
       Wireless camera installer near me Rockland County?
       Wireless Camera DIY vs Pro Install in Rockland County — What's Worth Hiring Out?
       Ready to talk through your Rockland County install?
       How much does wireless camera install cost in Rockland County?
       What brands do you install in Rockland County?
       Do I need monthly fees for Rockland County wireless cameras?
       How long does install take?
       Can Rockland County renters install wireless cameras?
       Do you handle Rockland County HOA / co-op approval?
       Same-day install in Rockland County?
       Will my Wi-Fi handle 4 cameras?
       4G LTE camera install in Rockland County?
       What's the 3-year warranty cover in Rockland County?
    == wireless-camera-installation-staten-island.html 20
       Ready to talk through your Staten Island install?
       Best wireless camera for Staten Island?
       How much for wireless camera install Staten Island?
       Wireless or wired cameras for Staten Island?
       Wireless camera no monthly fee Staten Island?
       Solar wireless camera Staten Island?
       4G LTE camera install Staten Island?
       Wireless camera installer near me Staten Island?
       Wireless Camera DIY vs Pro Install in Staten Island — What's Worth Hiring Out?
       Ready to talk through your Staten Island install?
       How much does wireless camera install cost in Staten Island?
       What brands do you install in Staten Island?
       Do I need monthly fees for Staten Island wireless cameras?
       How long does install take?
       Can Staten Island renters install wireless cameras?
       Do you handle Staten Island HOA / co-op approval?
       Same-day install in Staten Island?
       Will my Wi-Fi handle 4 cameras?
       4G LTE camera install in Staten Island?
       What's the 3-year warranty cover in Staten Island?
    == wireless-camera-installation-suffolk-county.html 20
       Ready to talk through your Suffolk County install?
       Best wireless camera for Suffolk County?
       How much for wireless camera install Suffolk County?
       Wireless or wired cameras for Suffolk County?
       Wireless camera no monthly fee Suffolk County?
       Solar wireless camera Suffolk County?
       4G LTE camera install Suffolk County?
       Wireless camera installer near me Suffolk County?
       Wireless Camera DIY vs Pro Install in Suffolk County — What's Worth Hiring Out?
       Ready to talk through your Suffolk County install?
       How much does wireless camera install cost in Suffolk County?
       What brands do you install in Suffolk County?
       Do I need monthly fees for Suffolk County wireless cameras?
       How long does install take?
       Can Suffolk County renters install wireless cameras?
       Do you handle Suffolk County HOA / co-op approval?
       Same-day install in Suffolk County?
       Will my Wi-Fi handle 4 cameras?
       4G LTE camera install in Suffolk County?
       What's the 3-year warranty cover in Suffolk County?
    == wireless-camera-installation-ulster-county.html 20
       Ready to talk through your Ulster County install?
       Best wireless camera for Ulster County?
       How much for wireless camera install Ulster County?
       Wireless or wired cameras for Ulster County?
       Wireless camera no monthly fee Ulster County?
       Solar wireless camera Ulster County?
       4G LTE camera install Ulster County?
       Wireless camera installer near me Ulster County?
       Wireless Camera DIY vs Pro Install in Ulster County — What's Worth Hiring Out?
       Ready to talk through your Ulster County install?
       How much does wireless camera install cost in Ulster County?
       What brands do you install in Ulster County?
       Do I need monthly fees for Ulster County wireless cameras?
       How long does install take?
       Can Ulster County renters install wireless cameras?
       Do you handle Ulster County HOA / co-op approval?
       Same-day install in Ulster County?
       Will my Wi-Fi handle 4 cameras?
       4G LTE camera install in Ulster County?
       What's the 3-year warranty cover in Ulster County?
    == wireless-camera-installation-westchester-county.html 20
       Ready to talk through your Westchester County install?
       Best wireless camera for Westchester County?
       How much for wireless camera install Westchester County?
       Wireless or wired cameras for Westchester County?
       Wireless camera no monthly fee Westchester County?
       Solar wireless camera Westchester County?
       4G LTE camera install Westchester County?
       Wireless camera installer near me Westchester County?
       Wireless Camera DIY vs Pro Install in Westchester County — What's Worth Hiring Out?
       Ready to talk through your Westchester County install?
       How much does wireless camera install cost in Westchester County?
       What brands do you install in Westchester County?
       Do I need monthly fees for Westchester County wireless cameras?
       How long does install take?
       Can Westchester County renters install wireless cameras?
       Do you handle Westchester County HOA / co-op approval?
       Same-day install in Westchester County?
       Will my Wi-Fi handle 4 cameras?
       4G LTE camera install in Westchester County?
       What's the 3-year warranty cover in Westchester County?

## NYC (hub) — /wireless-camera-installation-nyc (batch 2026-10-18, includes its silo findings and its question register)

## Research — wireless-camera-installation-nyc (REBUILD, NYC hub)

Built 2026-10-18. Thesis: in NYC a wireless camera is a radio-and-power problem in dense buildings, plus permission (landlord/board/LPC) and NY audio law. Format per entry: exact query · platform · URL · finding · page+section used.

### Silo-wide findings

#### Google PAA / PASF / AnswerThePublic / AI Overview / Bing / DDG / Yelp 1–3★
- PAA: EMPTY (not accessible in build env)
- PASF: EMPTY (not accessible in build env)
- AnswerThePublic: EMPTY (not accessible in build env)
- Google AI Overview: EMPTY (not accessible in build env). Reality Check uses cost-site claims below instead.
- Bing / DuckDuckGo autocomplete & related: EMPTY (not accessible in build env)
- Yelp 1–3★: EMPTY (not accessible in build env)

#### Cost-site claims (stand-in for AI Overview claims)
- "wireless security camera installation cost per camera Angi HomeAdvisor 2025" · Firecrawl search · https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera.htm · wireless cameras $25–$35 each; DIY install $50–$100/camera; "save up to $150 per camera" · AI Reality Check H3 "$50 to $100 per camera".
- same query · Firecrawl · https://www.homeadvisor.com/cost/safety-and-security/security-camera-installation-cost/ · professional install $593–$2,040 complete home setup · same H3.

#### Reddit (search excerpts only; reddit scrape blocked by Firecrawl)
- "reddit NYC apartment wireless security camera landlord hallway door camera" · Firecrawl search · https://www.reddit.com/r/AskNYC/comments/1959k2t/ring_camera_in_apartment_building_opinions/ · NYC tenant with Ring on apartment door facing neighbour's door · The City (renter paragraph); Sources.
- same · https://www.reddit.com/r/newyorkcity/comments/crbfu0/can_i_legally_install_a_surveillance_camera_on_my/ · tenant asking whether a door camera is legal, packages going missing · The City renter paragraph; Sources.
- same · https://www.reddit.com/r/AskNYC/comments/1gjf846/can_you_recommend_a_camera_to_go_on_your/ · "You may not be allowed to install a camera in the hallway" · background (renter paragraph).
- "site:reddit.com brownstone wifi camera signal brick wall backyard Brooklyn" · Firecrawl · https://www.reddit.com/r/EufyCam/comments/1ncbxp1/disappointed_in_my_eufy_cams/ · Brooklyn brownstone owner disappointed with Eufy cams, router-to-camera distance · brownstone Q&A; Sources.
- Full thread scrapes: EMPTY (not accessible in build env — Firecrawl does not support reddit.com).

#### Primary / technical sources
- "New York eavesdropping law one-party consent Penal Law 250.00" · WebSearch→WebFetch · https://nysenate.gov/legislation/laws/PEN/250.00 · "mechanical overhearing" = recording a conversation without consent of at least one party, by a person not present, by device · Commercial rules; Q&A hallway voices; AI Reality Check audio H3.
- NY Penal Law 250.05 · Firecrawl scrape · https://www.nysenate.gov/legislation/laws/PEN/250.05 · eavesdropping is a class E felony · same sections. (WebFetch blocked — permission timeout; Firecrawl reached it.)
- NY Labor Law 203-c · Firecrawl scrape · https://www.nysenate.gov/legislation/laws/LAB/203-C · employers may not video record employees in restrooms, locker rooms, changing rooms without court order · Commercial rules; AI Reality Check.
- "NIST electromagnetic signal attenuation construction materials" · WebSearch→WebFetch · https://nist.gov/publications/electromagnetic-signal-attenuation-construction-materials · NISTIR 6055 (Stone, 1997): brick, masonry block, 8 concrete mixes, reinforced concrete, rebar grids etc., 0.5–2 GHz & 3–8 GHz · The City; Building Specialists materials. (Full PDF numeric results not extracted — no dB figures used.)
- "2.4 GHz three non-overlapping channels" · WebSearch→WebFetch · https://www.acrylicwifi.com/en/blog/why-are-wifi-channels-1-6-and-11-used-on-2-4ghz/ · ch 1–11 legal in North America; 1/6/11 non-overlapping at 20 MHz · The City; facts list; Q&A evening slowdown.
- "5 GHz shorter range less able to penetrate walls" · WebSearch→WebFetch · https://arris.force.com/consumers/articles/General_FAQs/Differences-Between-2-4-and-5-GHz-Wi-Fi-Network · 5 GHz penetrates walls less well; 23 channels vs 11 · facts list; AI Reality Check "5 GHz always better".
- "FCC opens 6 GHz band unlicensed Wi-Fi 1,200 megahertz April 2020" · WebSearch→WebFetch · https://www.telecomtv.com/content/wi-fi/fcc-opens-6ghz-band-to-wi-fi-and-other-unlicensed-uses-38453 · adopted Apr 23, 2020; 1,200 MHz 5.925–7.125 GHz; LPI across full band · facts list; Q&A 6 GHz router.
- "FCC November 2022 order ... Hikvision Dahua" · WebSearch→WebFetch · https://urgentcomm.com/2022/11/30/fcc-bans-authorization-of-new-covered-products-from-five-chinese-vendors/ · no new authorizations for Huawei, ZTE, Hikvision, Dahua, Hytera; past authorizations not immediately revoked · Q&A Hikvision/Dahua; equipment caption.
- "Ring battery will not charge below 32 degrees" · WebSearch→WebFetch · https://ring.com/support/articles/0ot3t/Battery-Powered-Ring-Cameras-and-Cold-Weather · designed to stop charging below freezing; operating −4°F to 122°F; battery life shortens near freezing · The City; Q&A battery/solar; AI Reality Check solar.
- "IEEE 802.3af 15.4 watts 802.3at 30 watts PoE 100 meters" · WebSearch→WebFetch · https://support.cyberdata.net/portal/en/kb/articles/poe-standards-and-the-poe-switch-distance-limit · af 15.4 W, at 30 W, bt 60/100 W, 328 ft/100 m · Q&A "why a cable".
- "NYC DOB electrical permit licensed electrician" · WebSearch→WebFetch · https://www.nyc.gov/site/buildings/property-or-business-owner/project-requirements-owner-electrical.page · "No installation and modification to any electrical systems can be performed without a permit and a Licensed Master Electrician." · The City; Commercial rules; Q&A light-fixture power; AI Reality Check.
- "Con Edison June 2025 heat wave outages voltage reduction" · WebSearch→WebFetch · https://ny1.com/nyc/all-boroughs/news/2025/06/25/power-outages-across-nyc-stretch-into-third-day · peak >12,000 customers out from Jun 23; 8% voltage reduction SE Queens, then Staten Island and SW Brooklyn; one customer can be a whole building · Q&A voltage reduction.
- "Citizens Housing and Planning Council housing stock" · WebSearch→WebFetch · https://chpcny.org/visualization/housing-stock-visualization/ · 3.7M units; 54% pre-1947; 62% in 6+ unit buildings; Manhattan 97% in 6+; Staten Island 83% one/two-family; Brooklyn+Queens = half of units · The City; Five Boroughs.
- "Landmarks Preservation Commission security cameras permit" · WebSearch→WebFetch · https://www.nyc.gov/assets/lpc/downloads/pdf/LPCPermitGuidebook_Chapter11_HealthSafety.pdf · staff-level permit; cut sheets; ≤2 cameras/25 ft frontage small bldgs, ≤3 large; off primary façade unless no option; attach at mortar joints/plain masonry/wood/metal, not through cast iron or decorative surfaces; ~10 in visible conduit max · Q&A historic district; materials (cast iron); equipment table; AI Reality Check.
- "NYC LPC number of protected buildings" · WebSearch→WebFetch · https://www.nyc.gov/assets/operations/downloads/pdf/mmr2025/lpc.pdf · 38,113 buildings and sites; 1,464 individual landmarks; 157 historic districts & extensions; 11,748 permit applications FY25 · The City; facts list; AI Reality Check.
- "HPD fire escape obstructed" · WebSearch→WebFetch · https://www.nyc.gov/assets/hpd/downloads/pdfs/services/fire-safety-graphic.pdf · "Exits must be clear of obstacles on fire escapes, in hallways & by all building entrance doors, including roof doors." · Q&A fire escape.
- (secondary) https://nyhabitat.com/blog/2015/11/23/5-things-know-fire-escapes-renting-apartment-nyc · storing anything on fire escape illegal (no code cited) · not used on page (HPD used instead).
- "co-op alteration agreement security camera board approval" · WebSearch→WebFetch · https://www.brickunderground.com/improve/what-are-alteration-agreements · alteration agreements protect building-wide services/structures; insurance language, e.g. $1M general liability · Q&A board.
- "connextivity NYC apartment security camera laws" · Firecrawl search · https://www.connextivity.com/insights/nyc-apartment-security-safety-camera-laws · "No New York statute bans door cameras that view a hallway"; co-ops/condos may require board approval · Q&A board.
- same · https://www.fsresidential.com/new-york/news-events/articles-and-news/security-cameras-best-practices-nyc-condos-co-ops/ · audio in common areas = eavesdropping risk (§250.05); personal door-camera policies common; links NYT 2023-02-18 Ring doorbell article · Q&A board; Q&A hallway voices.
- https://cctvblog.mataroa.blog/blog/wifi-interference-from-neighbours-plagues-cctv/ · neighbour Wi-Fi congestion claims (unsourced) · NOT used for facts.

#### Five keyword layers (as placed)
- Service: wireless camera installation NYC; Wi-Fi camera install; battery camera; solar camera; 4G LTE camera; PoE camera; floodlight camera; doorbell camera.
- Problem: camera drops in the evening; camera can't reach router; battery won't charge in cold; no outlet; board approval; landmark permit; audio legality.
- Technology: 2.4/5/6 GHz, channels 1/6/11, Wi-Fi 6E/7, mesh/wired backhaul, access point, point-to-point bridge, PoE 802.3af/at, WPA2/WPA3, NVR/base station/microSD/cloud.
- Industry: apartments/co-ops/condos, row houses, storefronts under els, office suites, restaurants, pop-ups, small warehouses, houses of worship.
- Geographic: NYC, five boroughs, Brooklyn Heights, Grand Concourse, Jackson Heights, Roosevelt Ave/7, Jamaica Ave/J, Hudson Yards, St. George, Park Slope, Upper West Side, Tottenville.

### NYC (hub) — local section
- Borough building stock (CHPC above) drives the "Five Boroughs" section; Manhattan vertical/managed, Brooklyn rows, Queens mixed, Bronx large apartment buildings, Staten Island houses (83%).
- Landmarks named in Coverage (Brooklyn Heights, Grand Concourse, Jackson Heights, Roosevelt Ave under the 7, Hudson Yards, St. George) — general knowledge, described by building conditions only; no source fetched for each this run (flag for skim).
- LPC and HPD, DOB, Con Ed sources as above.

### Question register — wireless-camera-installation-nyc
Q&A (H3):
1. Why does my camera stream perfectly at noon and stutter or freeze most evenings?
2. Can a camera on the back of a brownstone reach a router at the front of the parlor floor?
3. Can a neighbour on the same channel see our camera video, or only slow it down?
4. Will a new 6 GHz Wi-Fi 6E or Wi-Fi 7 router fix our camera problems?
5. If the camera is “wireless,” why does the quote include running a cable?
6. Is a battery camera realistic over a courtyard or façade that gets almost no direct sun?
7. What does a Con Edison voltage reduction or a short block outage do to Wi-Fi cameras?
8. Can a camera be mounted on the fire escape outside my window?
9. Our building is in a historic district — do we need Landmarks approval for a camera on the front?
10. What does a co-op or condo board usually want to see before a camera goes on a common wall?
11. Can a camera take its power from the existing light fixture over our door instead of a new outlet?
12. My door camera picks up voices in the shared hallway — is that a problem under New York law?
13. Can a wireless camera go inside our building’s elevator cab? (replaced HV-overlapping FCC/brand question; general AESS practice)
14. Can one app show cameras from three different apartments or buildings we own?
15. Our storage cage or bike room in the cellar has no Wi-Fi — can a camera still watch it? (replaced; overlapped HV 'cameras and accounts if we sell'; general AESS practice)
FAQ (= FAQPage schema):
16. Why does the hub quote in Brooklyn dollars when I live in Manhattan or Queens?
17. Do you survey the signal before quoting, or quote from photos?
18. Can you work inside a doorman building’s contractor hours?
19. Will you use our existing router or bring new network equipment?
20. Do you keep the admin login, or do we get it?
21. Can we start with two cameras and add more later?
22. How quickly can you send a certificate of insurance naming our building?
23. Will you install cameras we bought online ourselves?
24. Can a camera see the street through our window glass at night?
25. How is payment handled for a wireless camera job?
Other "?" heading: "Wireless Camera Down Somewhere in the Five Boroughs?" (repair CTA).

## Nassau County — /wireless-camera-installation-nassau-county (batch 2026-10-18, includes its silo findings and its question register)

## Research — wireless-camera-installation-nassau-county (REBUILD, 2026-10-18)

Format: exact query · platform · URL · finding · page+section used.

### Silo-wide findings (wireless-camera-installation)

- Google PAA "wireless camera installation nassau county" · Google · EMPTY (not accessible in build env)
- Google PASF · Google · EMPTY (not accessible in build env)
- AnswerThePublic "wireless camera" · ATP · EMPTY (not accessible in build env)
- Google AI Overview "wireless camera installation cost" · Google SGE · EMPTY (not accessible in build env). The Reality Check section is written as commonly repeated generic claims, not quoted AI Overview text.
- Bing / DuckDuckGo autocomplete · EMPTY (not accessible in build env)
- Yelp 1–3★ camera installers Nassau · Yelp · EMPTY (not accessible in build env)
- "site:reddit.com r/longisland security cameras wifi backyard detached garage" · Firecrawl search · https://www.reddit.com/r/Landlord/comments/1t0ef4d/landlord_usny_can_i_have_cameras_in_the_outside/ · snippet (opinion): "Any common areas cameras are permitted as long as the tenants know about them." · informed the tone of Building Specialists > "Two-family houses and basement apartments" (not quoted; no fact relies on it). Other hits (r/EufyCam shared garage, r/homedefense detached garage, r/homesecurity) were general, not Nassau; not used.
- Five keyword layers used on page: Service (wireless camera installation, Wi-Fi camera, video doorbell, floodlight camera, solar camera, LTE camera) · Problem (camera keeps buffering/offline, battery dies, power outage, package theft, car break-ins, neighbour privacy) · Technology (mesh node, outdoor access point, 2.4 GHz, base station/NVR, UPS, privacy mask, separate camera network) · Industry (homeowners, two-family landlords, storefront strip tenants, flood-zone homes) · Geographic (Nassau County, Hempstead, North Hempstead, Oyster Bay, Glen Cove, Long Beach, Levittown, Massapequa, Wantagh, Elmont, Hicksville, Baldwin, Lawrence, Flower Hill).

### Pricing basis
- wireless-camera-installation-brooklyn.html shows NO prices. Silo price base taken from the in-page price widget ITEMS on the old Nassau/SI/Suffolk wireless pages (Brooklyn base m=1.0): 295/445/345/1295/1495/2795/145/345/545/695. Old widget used Nassau multiplier 1.2 (text showed $355 etc.); rebuilt page uses §9 ×1.15, round half-up: 339/512/397/1489/1719/3214/167/397/627/799; $195/hr, 3-hr min ($585). Old page also showed inconsistent figures ($295–$3,795 ranges, $1,295/$1,555 4-cam, "3-year warranty", fabricated "illustrative" projects) — all dropped.

### Nassau County

| Query | Platform | URL | Finding | Used |
|---|---|---|---|---|
| Nassau County New York three towns two cities 64 incorporated villages | WebSearch → WebFetch | https://nassaucountyny.gov/3406/Cities-Towns-Villages | "2 cities, 3 towns, 64 incorporated villages and over 100 unincorporated areas"; cities Glen Cove, Long Beach; towns Hempstead, North Hempstead, Oyster Bay | Why section ¶6 + facts list; Q&A neighbour-yard; FAQ 1; AI check H3 6; sources |
| Nassau County QuickFacts owner-occupied | WebFetch | https://www.census.gov/quickfacts/nassaucountynewyork | Pop 1,398,939 (V2025); owner-occ 81.9% (2020–24); median value $684,700; 2.99 persons/household; broadband 94.8%; 480,591 housing units | Why ¶1; facts list |
| PSEG Long Island Tropical Storm Isaias outages | WebSearch → WebFetch | https://abc7ny.com/weather/widespread-damage-and-power-outages-across-long-island/6353608/ | Almost half of PSEG's 1.1M customers out at peak; 105,000 still out (Aug 7, 2020); half of Glen Cove residents without power | Why ¶4; facts; Q&A PSEG outage; AI check H3 3 |
| PSEG Long Island storm outages 2025 Nassau | WebFetch | https://longisland.news12.com/thousands-without-power-due-to-noreaster-across-long-island | Oct 13, 2025 nor'easter, ~3,000 out on LI; pockets in Port Washington, Glen Cove, Levittown | Why ¶4 |
| Hurricane Sandy Long Beach | WebFetch | https://liherald.com/longbeach/stories/superstorm-sandy-10-years-later,149164 | "basically a dirty brown river"; 3–5 ft water in yards; FEMA >1,000 homes substantially damaged; 2.2-mile boardwalk rebuilt ~$40M | Why ¶4; Q&A flood zone; landmarks card |
| Nassau County police package theft porch pirates | WebSearch → WebFetch | https://www.fox5ny.com/news/long-island-porch-pirates-nassau-county | Nov 7, 2023: FedEx packages stolen from ≥6 homes, Massapequa Park/Massapequa/Wantagh, Oct 5–16; suspect walks up, takes package, leaves on foot; Crime Stoppers 1-800-244-TIPS | Why ¶5; Q&A porch camera; FAQ police footage |
| Nassau County police car thefts key fob | WebSearch → WebFetch | https://www.cbsnews.com/amp/newyork/news/nassau-police-making-push-for-residents-to-stop-leaving-key-fobs-in-cars-amid-surging-thefts | Apr 15, 2022: thefts 100→341; 95% unlocked with fobs inside (police); Commissioner Ryder, Lt. LeBrun quotes | Why ¶5; facts; Q&A driveway |
| Nassau village code security cameras neighbor privacy | WebSearch → WebFetch | https://www.cbsnews.com/amp/newyork/news/flower-hill-security-cameras | Oct 12, 2017 Flower Hill proposed local law banning imaging devices with "no legitimate purpose other than viewing or recording another"; hearing postponed | Why ¶6; Q&A neighbour-yard; AI check H3 6 |
| (same search) | WebFetch | https://longisland.news12.com/2026/04/29/lawrence-to-add-more-than-100-cameras-as-part-of-newly-approved-comprehensive-outdoor-surveillance-camera-system/4YrqdHL7d9vos0DokdpJbu | Lawrence board unanimously approved (Feb 19, 2026) >100 cameras with LPRs on ~800 upgraded light fixtures, linked to NCPD command center; $250,000 | Why ¶6; Q&A LPR |
| Levittown 17,447 houses Cape Cod ranch | WebSearch → WebFetch | https://www.foxnews.com/story/levittown-americas-first-suburb-turns-60.print | 17,544 Cape Cod and ranch houses; first opened Oct 1947; four rooms, bath, unfinished attic, no basements; nearly all renovated, "almost McMansions" | Why ¶2; facts; landmarks |
| Nassau downtown revitalization grants | WebFetch | https://www.nysenate.gov/newsroom/in-the-news/2021/todd-kaminsky/10m-state-grant-bring-new-projects-downtown-baldwin | May 2021 Baldwin $10M DRI, train station area & Grand Ave; Merrick Rd rebuild Harrison Ave–Pershing Blvd | Commercial section ¶3 |
| (same) | WebFetch | https://longislandpress.com/2017/08/02/hicksville-gets-10m-downtown-revitalization-grant | Hicksville $10M DRI; station where Port Jefferson and Ronkonkoma branches meet near Rts 106/107; Westbury won prior year | Commercial ¶3; landmarks |
| Hempstead Turnpike route | WebFetch | https://en.wikipedia.org/wiki/New_York_State_Route_24 | Route through Elmont, Franklin Square, W. Hempstead, Hempstead, Uniondale, East Meadow, Levittown, Plainedge to Farmingdale; long commercial strip in Elmont/Franklin Square; passes Belmont Park/UBS Arena, Hofstra, Nassau Coliseum lots, Eisenhower Park | Commercial ¶1; landmarks cards |
| NY Penal Law 250.45 | WebSearch | https://www.nysenate.gov/legislation/laws/PEN/250.45 | Unlawful surveillance (recording in bedrooms, bathrooms etc. without consent) | Two-family block; equipment table; AI check H3 6 |
| Nassau PD camera registration program | WebSearch | (results were Nassau County, Florida) | Not applicable | not used |
| Town of Hempstead outdoor lighting ordinance | WebSearch | (no Nassau code returned) | EMPTY — no village/town lighting rule cited; page only advises checking village code | — |

Hyperlocal (Herald etc.) beyond the above: liherald Isaias pieces seen in results, not fetched. Local Reddit for Nassau: EMPTY (no Nassau-specific camera thread found).

### Unsourced statements (general AESS practice, marked as such in context)
Wi-Fi range/attenuation through walls, foil-faced insulation & aluminium siding, 2.4 GHz congestion, mesh/outdoor AP fixes, UPS sizing, storm-door IR glare, winter solar shading, separate camera SSID, siding mounting — presented as installer practice, not as Nassau statistics.

### Question register (this page)
Q&A (H2):
1. Our router is in the front room and the garage is at the back of the lot. Why does the garage camera keep buffering?
2. Our side yard is only a few feet wide and the neighbour's windows face it. Where should that camera point?
3. The neighbours say our floodlight camera lights up their bedroom. How do we keep the night picture without the glare?
4. What does a driveway camera need to show if someone tries the car doors at night?
5. Can the cameras tell us the kids got home from school without recording them all day?
6. Where should a porch camera go so it shows the face of someone taking a package?
7. Will a video doorbell work if we have a glass storm door in front of the front door?
8. Our shop is in a strip with a shared lot behind it. Can one Wi-Fi system cover the front counter and the back door?
9. We live in a flood zone near the water. Does that change where cameras and equipment go?
10. Our village just put licence plate readers on the street lights. Do we still need a camera facing the street?
11. Should the cameras be on our main Wi-Fi or a network of their own?
12. If we can only afford two cameras this year, which two should they be on a Nassau house?
FAQ:
1. My mailing address says one town but I live in an incorporated village. Whose rules apply to cameras on my house?
2. Does mounting a plug-in or battery camera on my own house in Nassau need a building permit?
3. We are switching internet providers next month. Should we wait before installing the cameras?
4. Can cameras go on vinyl or aluminium siding without letting water in behind it?
5. Can a camera on our detached garage run off the same outlet as the garage door opener?
6. What happens to the recording if someone pulls a wireless camera off the wall?
7. How soon can a technician get to a house in Nassau County?
8. We already have two Ring cameras. Can they stay if we add a local-recording system?
9. Can a camera go on the utility pole or the street tree in front of our house?
10. We are getting new gutters and a new roof next spring. Should the cameras wait?
11. Can we put cameras on a parent's house in Nassau when we live somewhere else?
12. Roughly how many wireless cameras does a typical Cape or ranch on a quarter-acre need?

### Revision (coordinator follow-up, 2026-10-18)
- Four questions replaced for meaning overlap with the shipped wireless-camera-installation-hudson-valley page (selling the house, police footage, power-outage backup, neighbour in view); replacements are general AESS practice (no new local facts).
- Added the four-camera package table from the Brooklyn wireless page pricing-bar data (AP.brooklyn a 950, f 998, e 1157, c 1392, d 1392, b 1659) ×1.15 → $1,093 / $1,148 / $1,331 / $1,601 / $1,601 / $1,908, alongside the wireless list (widget base ×1.15). Note: the Brooklyn pricing bar's own nassau entry uses ~1.176 (a 1117 …); not used.

## Westchester County — /wireless-camera-installation-westchester-county (batch 2026-10-18, includes its silo findings and its question register)

## Research — wireless-camera-installation-westchester-county (REBUILD, 2026-10-18)

Format: exact query · platform · URL · finding · page+section used.
Research tools: Firecrawl search/scrape (MCP). Shell web access blocked.

### Silo-wide findings (wireless-camera-installation)

| Source | Exact query | Platform | URL | Finding | Used |
|---|---|---|---|---|---|
| Google PAA | — | Google | — | EMPTY (not accessible in build env) | — |
| Google PASF | — | Google | — | EMPTY (not accessible in build env) | — |
| Answer the Public | — | ATP | — | EMPTY (not accessible in build env) | — |
| Google AI Overview | — | Google | — | EMPTY (not accessible in build env); AI Reality Check section written from common AI-summary claims answered with sourced local facts, no AI claim quoted verbatim | AI Overview Reality Check (framed as generic summaries) |
| Bing / DDG autocomplete | — | Bing/DDG | — | EMPTY (not accessible in build env) | — |
| Yelp 1–3★ | "wireless security camera installation Westchester NY" | Firecrawl search | https://m.yelp.com/search?find_desc=Security+Camera+Installation&find_loc=Westchester+County%2C+NY | Only a listing snippet (Queens-based installers ranking for Westchester); no 1–3★ review text retrievable → EMPTY for reviews | Not used |
| Reddit (r/homeautomation, r/HomeNetworking, r/smarthome, r/homedefense, r/Starlink) | "point to point wifi bridge to detached garage barn security camera how far reddit" | Firecrawl search | https://www.reddit.com/r/homeautomation/comments/su3iz9/how_to_add_a_wifi_camera_1000_ft_from_my_house/ ; https://www.reddit.com/r/HomeNetworking/comments/oc1vme/best_way_to_get_wireless_in_detached_garage_far/ ; https://www.reddit.com/r/homedefense/comments/p64ry1/options_for_a_camera_down_by_my_barn_about_800/ ; https://www.reddit.com/r/Starlink/comments/1rehosm/wireless_bridge_to_barn/ | Snippets only (Reddit scrape unsupported): owners asking how to reach barns/garages 175–1,000 ft away; consensus = point-to-point bridge with line of sight, not mesh/extender | Questions Answered › Distance, Bridges (Q: 400-ft garage bridge vs mesh); AI check "Wi-Fi extender" myth |
| Competitor landscape | "wireless security camera installation Westchester NY" | Firecrawl search | knightprotect.com, datawiresolutions.com, nyconnsecurity.com, westchestersecuritysystems.com, wirefly.com | Competitors pitch generic "wireless camera systems"; none address bridges/LTE/solar/outage backup | Positioning only; no competitor named or quoted |
| Wi-Fi jammer news | "Westchester burglary crews Wi-Fi jammers security cameras police warning" | Firecrawl search + scrape | https://westchester.news12.com/police-in-new-jersey-say-burglars-are-using-wi-fi-jammers-to-target-homes-heres-what-you-need-to-know | News 12 Westchester, June 14, 2024: Florham Park NJ police say a burglar used a Wi-Fi jammer to knock out cameras and phone; devices under $300; police urge hardwiring, not relying on Wi-Fi | Neighborhood ¶5; Q "burglars use Wi-Fi jammers"; Sources |

#### Five keyword layers (planned, natural placement)
- Service: wireless camera installation Westchester County; wireless security camera install; outdoor Wi-Fi camera installation
- Problem: camera keeps disconnecting detached garage; camera offline after power outage; no Wi-Fi at gate; cameras jammed
- Technology: point-to-point wireless bridge; outdoor mesh; LTE cellular camera; solar camera; PoE; NVR local recording; battery backup/UPS; 2.4 vs 5 GHz; 4K bitrate
- Industry/property: estate with outbuildings; barn/stable; pool house; two-/three-family house; apartment parking court; village storefront rear lot
- Geographic: Westchester County; Yonkers; Mount Vernon; New Rochelle; White Plains; Scarsdale; Rye; Mamaroneck; Pelham Manor; Greenburgh; Dobbs Ferry; Irvington; Mount Kisco; Bedford; Pound Ridge; Lewisboro; North Salem; Somers; Yorktown; Armonk; Chappaqua; Katonah; Cross River; Valhalla

### Westchester

| Exact query | Platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| "northern Westchester cell phone dead zones Pound Ridge North Salem cell tower coverage" | Firecrawl search → scrape | https://bedfordny.gov/DocumentCenter/View/3832/Cellular-Presentation-5625 | Town of Bedford wireless presentation to Town Board, May 7, 2025: "Hilly Terrain obstructs signals"; pocket gaps even near a facility; Seminary Ridge shadows coverage; Indian Hill blocks Bedford Post site from Middle Patent Rd, upper Long Ridge Rd, parts of Route 172; Bedford Post initially Verizon only, antennas carrier-specific; Northern Westchester Wireless Masterplan; recommends signal apps (LTE Discovery) | Hero subhead; Neighborhood ¶3; facts list; Q barn line-of-sight; Q cellular test; AI "300 feet"; Landmarks (Indian Hill/Route 172); Sources |
| same query | Firecrawl search (snippet only) | https://www.reddit.com/r/Westchester/comments/16rsx6t/cellular_provider_recommendations/ | Snippet: "Much of Bedford to the east of 684 is a dead zone for everyone" (scrape unsupported) | Not quoted; noted in Sources paragraph as excerpt-only |
| "NYSEG service territory Westchester County towns northern Westchester" | Firecrawl search | https://www.nyseg.com/documents/d/nyseg/psc120_section-1 | NYSEG tariff PSC 120 §1 snippet: "WESTCHESTER COUNTY: Towns: Bedford. Lewisboro. North Salem. Poundridge. Somers. Yorktown." | Neighborhood ¶4; facts list; Q Con Ed vs NYSEG; Sources |
| same | Firecrawl scrape | https://www.nyseg.com/w/nyseg-making-steady-progress-restoring-service-in-westchester-putnam-and-dutchess-counties-final | NYSEG Brewster Division = parts of Westchester, Putnam, Dutchess; 86,000 customers; peak >15,000 out in one (undated) storm; restoration priorities | Neighborhood ¶4; Q Con Ed vs NYSEG; Sources |
| same | Firecrawl search | https://www.coned.com/en/business-partners/service-territories | Con Ed service area includes all NYC and Westchester County | Q Con Ed vs NYSEG; Sources |
| "Westchester County power outages storm Con Edison customers without power lohud 2025" | Firecrawl scrape | https://www.coned.com/en/about-us/media-center/news/2026/07-04/con-edison-restoring-power-to-customers-impacted-by-severe-storms | July 5, 2026: >20,000 customers still out; Westchester greatest impact; Greenburgh, Yonkers, Elmsford, Dobbs Ferry, Rye; gusts to 60 mph | Hero; Neighborhood ¶4; facts list; Across the County (central); Sources |
| same | Firecrawl scrape | https://www.coned.com/en/about-us/media-center/news/2026/06-06/con-edison-restoring-power--to-customers-affected-by-storm | June 7, 2026 release: >5,000 Westchester customers out; Bronxville, Mount Vernon, New Rochelle, Pelham Village, Scarsdale, White Plains, Yonkers | Across the County (central); Sources |
| "Tropical Storm Isaias Con Edison Westchester customers lost power 2020 PSC" | Firecrawl search + scrape | https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7BB7BCDA40-2075-4231-A208-702C436893C0%7D | PSC interim Isaias report: peak ~290,000 Con Ed, 95,000 NYSEG; most NYSEG outages in Brewster Division; full restoration Aug 12 | Neighborhood ¶4; facts list; Q outage duration; Sources |
| same | Firecrawl search | https://www.lohud.com/story/weather/2020/08/12/eight-days-after-isaias-many-without-power-wednesday-morning-hudson-valley/3352805001/ | Aug 12, 2020: 8 days after Isaias, Con Ed said ~350 storm outages in Westchester | Q outage duration; Sources |
| "New York State Police targeted residential burglaries Dutchess Westchester Putnam counties alert" | Firecrawl scrape | https://troopers.ny.gov/news/public-safety-alert-targeted-residential-burglaries-hudson-valley-region | Jan 29, 2025 NYSP alert: targeted residential burglaries in Dutchess, Westchester, Putnam; recommends installing/activating security systems and cameras, motion lighting | Neighborhood ¶5; Sources |
| "Westchester police warn residents burglaries homes South American theft groups 2025" | Firecrawl search | https://abc7ny.com/post/police-warning-residents-westchester-county-after-rash-home-break-ins-including-family-was-sleeping/15315908/ | ABC7: Pelham Manor police warn after rash of break-ins; Chief Thomas Atkins: intruders seek key fobs to take vehicles (article date not shown in text; NOT dated on page) | Neighborhood ¶5; Across the County (Sound Shore); Sources |
| "Westchester County population 2024 census land area square miles Yonkers population" + Census Reporter scrapes | Firecrawl | https://censusreporter.org/profiles/05000US36119-westchester-county-ny/ ; https://censusreporter.org/profiles/16000US3649121-mount-vernon-ny/ ; http://censusreporter.org/profiles/06000US3611984000-yonkers-city-westchester-county-ny/ | ACS 2024 1-yr: county 1,006,447; 430.8 sq mi land; 2,336.1/sq mi; 50% multi-unit; median owner value $691,100 (not used). Mount Vernon 71,982; 4.4 sq mi; 16,388.8/sq mi; 70% multi-unit. Yonkers 211,062; 18 sq mi; 11,722/sq mi | Hero; Neighborhood ¶1; facts list; Q Mount Vernon; Q Yonkers; Landmarks; Sources |
| "Westchester County 6 cities 19 towns 23 villages municipalities" | Firecrawl search | https://www.ny.gov/counties/westchester ; https://en.wikipedia.org/wiki/Westchester_County,_New_York | 6 cities, 19 towns, 23 villages (48 municipalities) | Facts list; Q pole permit; Sources |
| "Pound Ridge OR North Salem four-acre zoning minimum lot size residential" | Firecrawl search | https://www.bedfordny.gov/AgendaCenter/ViewFile/Item/3028?fileID=9252 ; https://ginnel.com/blog/understanding-bedfords-unique-four-acre-residential-zoning | "4 acres is required in the R-4 Acre District" (Bedford ZBA doc); Bedford four-acre zoning | Hero; Neighborhood ¶2; Across the County (north); Sources |
| "Westchester County Department of Consumer Protection home improvement license required contractors" | Firecrawl scrape | https://consumer.westchestercountyny.gov/home-contractors-and-trades/home-improvement-contractors | County law requires home improvement contractors to hold a county license; public license search; plumbers/electricians separately licensed | Commercial › compliance callouts; Sources |
| "Westchester building permit required gate pillars driveway gate electrical permit village code" | Firecrawl search | https://www.dobbsferry.gov/building-department/pages/building-department-info ; https://www.irvingtonny.gov/295/What-Requires-a-Permit ; https://cms6.revize.com/revize/mountkisco/departments/building_department/docs/Building%20Permit%20Application%20Instructions%20revised%206-24-25.pdf | Dobbs Ferry: only Westchester County Master license holders may apply for electrical permit; Irvington: electrical work filed by Westchester County licensed contractor; Mount Kisco: all electricians licensed by Westchester County; driveway/curb cut/street opening permit from State, County or Village | Compliance callouts; Q pole permit; Q who wires outlet; Sources |
| "ecode360 Westchester town exterior lighting law glare light trespass…" | Firecrawl search | https://www.irvingtonny.gov/DocumentCenter/View/9785/2020-03---Lighting-Standards | Irvington Local Law #3 of 2020 lighting standards; defines light trespass | Compliance callouts (exterior lighting); Sources |
| "ecode360 Westchester village code security camera…" | Firecrawl search | (no relevant residential camera ordinance found; only Ossining pawnbroker camera rule) | EMPTY for residential camera ordinances | Not used |
| "Ward Pound Ridge Reservation acres largest park Westchester County parks" | Firecrawl search | https://parks.westchestercountyny.gov/ward-pound-ridge-reservation | 4,315 acres, county's largest park (Pound Ridge/Lewisboro per Wikipedia) | Landmarks |
| "Muscoot Farm Somers Westchester County park acres…" | Firecrawl search | https://parks.westchestercountyny.gov/muscootfarm | 777 acres; early-20th-century farm near Katonah | Landmarks |
| "Kensico Dam Plaza Valhalla…; Playland Rye…" | Firecrawl search | https://en.wikipedia.org/wiki/Playland_(New_York) ; https://npgallery.nps.gov/GetAsset/4b8e2d7e-4c98-4de8-b57d-076a47f61853 ; Westchester Parks Facebook snippet listing Kensico Dam Plaza | Playland: 280 acres, county-owned, built 1928, on Long Island Sound in Rye; Kensico Dam Plaza is a county park location | Landmarks |
| Local news (Patch/Lohud hyperlocal for wireless cameras) | covered by queries above | — | No Westchester-specific wireless-camera news beyond the above | — |

### Question register (this page)
Questions Answered (H3):
1. We have a garage, a barn and a guest cottage in different directions from the house. Does each building need its own pair of radios? (general AESS practice)
2. The barn sits below the house, behind a stone wall and a row of old oaks. Can a wireless link reach it without a straight line of sight?
3. Will a bridge radio on our roof interfere with the neighbors’ Wi‑Fi, or need some kind of license? (general AESS practice)
4. Our barn is across a town road from the house. Can the camera link go over the road instead of trenching under it? (Mount Kisco permit instructions)
5. Bedford has new cell sites planned near us. Should we wait for them before choosing a gate camera? (Bedford May 2025 report: Rt 35 Katonah, Bedford Hills WTP site, Bedford Post carriers)
6. A falling limb took down the wires to our garage in the last storm. How do you keep a tree from cutting the camera link? (Con Ed July 5, 2026 release: trees pushed into overhead lines)
7. Does it matter to the camera design whether our house is on Con Edison or NYSEG?
8. We live on the water in Rye. Does salt air shorten the life of outdoor cameras and radios? (general AESS practice; Playland landmark)
9. We read that burglars use Wi‑Fi jammers to knock cameras offline. Should we avoid wireless cameras entirely?
10. Can the cameras run on a network separate from the one the family, guests and smart-home gadgets use?
11. We own a three-family house in Mount Vernon with a rear parking pad. Can the owner and the tenants share one camera system without sharing one password?
12. Our Yonkers building’s parking court is around the back and downhill from the office where the internet comes in. Can one wireless link cover it?
13. Do we need a building permit to put a camera on a pole at the gate?
14. Who wires a new outlet for a camera on the garage — your crew or an electrician?
15. House staff live in the apartment over our garage. How do we cover the garage without recording their home? (NY Labor Law §203-c)
16. We spend winters in Florida. Can we watch the property all season without the bridges or recorder needing a visit?
17. The previous owner left battery cameras and a base station we have no login for. Can you reuse them?
FAQ (visible + FAQPage, 9):
18. Will deer, branches and wind set off alerts all night on cameras watching a wooded lot?
19. Can we get an alert only when someone opens the pool gate, not every time a person walks past it?
20. Can a camera read the plate of a car coming up a long, dark driveway?
21. Where should the recorder go in a large house so a burglar cannot simply carry it out?
22. What happens to the footage if someone pulls a camera off the wall and takes it?
23. Can you do the installation while we are away, with our caretaker letting you in?
24. Our north-county internet is slow on upload. Will remote viewing still work?
25. Police in Pelham Manor warned about intruders hunting for car key fobs. Which cameras matter most if the worry is the car in the driveway? (ABC7 Pelham Manor report)
26. How soon can you come out, and what do you need from us first?
(Non-question H2: "Westchester Wireless Camera Down? Same-Day Repair" — contains "?" mid-string only.)

### Unsourced = general AESS practice (not stated as local fact)
Bridge vs mesh guidance, leaf-on signal loss, relay design, solar sizing rules, 2.4 vs 5 GHz, 4K bitrate on shared links, generator gap/auto-restart test, network segmentation, recorder placement, user-permission design, plate-camera placement.

### Revision 2026-10-18 (later): 8 questions replaced to avoid meaning-duplicates with the shipped Hudson Valley hub (hv-questions.txt). Cluster H2 'When Con Ed or NYSEG Goes Dark' renamed 'Storms, Salt Air and the Grid'.
