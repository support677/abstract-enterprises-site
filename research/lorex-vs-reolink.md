# Research: lorex-vs-reolink (comparison page, BLUEPRINT §12.5)

Built 2026-11-03 by the max-daily run (Anwar's Max plan, no API spend). Every fact on the page traces to a line here.
Fetched with Firecrawl search/scrape on 2026-11-03. "NOT CONFIRMED" = not confirmed on a manufacturer page, so the page does not state it.

## Search demand check (§12.5: confirm real demand first)
- query "lorex vs reolink" (Firecrawl web search): dedicated results from security.org/security-cameras/lorex-vs-reolink/ ("Lorex cameras offer superior video quality and night vision, while Reolink's Argus PT is wire-free"), safehome.org/compare/lorex-vs-reolink/ ("Lorex ... our top choice over Reolink"), lorex.com/pages/lorex-vs (Lorex's own vs page quoting security.org 9.6 vs 7.2), vueville.com Reolink vs Lorex, a YouTube "Reolink vs Lorex (2025)" video, ipcamtalk.com thread "Which system is better, Reolink or Lorex", trustyjoe.com, Facebook group Low Voltage Nation thread, reddit r/reolinkcam "Help me decide between Reolink and Lorex?". → demand confirmed.
- query "reolink vs lorex reddit which is better nvr": r/homedefense "Your Experiences, Recommendations - LOREX, REOLINK, EUFY and ARLO" (poor reviews of the Lorex app), r/reolinkcam "Is a Reolink NVR a good upgrade for my Lorex system?", r/homeowners + r/Lorex "SECURITY CAMERAS - LOREX OR REOLINK" (relative recommends Lorex night video), r/reolinkcam PoE shopping thread ("The Lorex system will outperform it imo"). Used as FAQ stand-ins (reworded); People Also Ask panel: EMPTY (not returned in build env).
- Gap: every ranking page is a reviewer or a manufacturer; none is an installer who wires both. → page angle (§12.5 installer angle).
- Reversed order "Reolink vs Lorex" appears in the same SERP (vueville, YouTube, trustyjoe) → mentioned on this page; no second page.

## Lorex (manufacturer pages)
- Fusion 4K+ 12MP 16-camera-capable NVR N910A62 https://www.lorex.com/products/n910a62-fusion-4k-12mp-16-channel-nvr : 16 camera capable (8 wired + 8 Fusion Wi-Fi); supports 12MP (16:9) and 4K+ (11.3MP 16:9); 2 TB included, up to 16 TB (SATA); 1 bay; PoE max 25.5 W single port, 72 W total; detection Person, Vehicle, Face, Mask, Package (missing/left behind), Animal; Lorex Home app (also Lorex Classic app, Lorex Cloud client); Alexa, Google Assistant, Chromecast, Echo Show, Google Home Hub; "No Monthly Fees. Own it. No subscriptions required." ONVIF/third-party and warranty not on that page.
- E910AB 4K+ 12MP IP wired bullet with Smart Security Lighting https://www.lorex.com/products/e910ab-4k-plus-12mp-smart-security-lighting-bullet-ip-camera : 12MP CMOS 4640×2624; 15 fps at 4K+ (all resolutions 15 fps); 139° FOV; 2.8 mm F1.6 fixed; IR 98 ft / 30 m; Color Night Vision yes; Smart Security Lighting yes; Active Deterrence warning light + siren + pre-recorded message; mic + speaker; PoE 802.3af or 12 V DC, max 9.5 W; IP67; −22 °F to 140 °F; detection vehicle, person, face, face mask, animal, package; compatible: N910 series NVR, RNU01P Lorex Connect XC NVR (limited via ONVIF), ONVIF conformant products (Profiles G, S, T). microSD and warranty not on page.
- ONVIF: "Lorex cameras are ONVIF G, S, and T compliant" https://www.lorex.com/blogs/news/why-lorex-onvif-security-cameras-are-the-perfect-replacement-for-banned-brands ; Lorex PRO FAQ "Do Lorex NVRs support third-party ONVIF cameras? Lorex NVRs are designed to work best with Lorex cameras" https://pro.lorex.com/collections/onvif-security-cameras-and-recorders ; X Series NVR help article on connecting ONVIF-conformant cameras https://www.lorex.com/blogs/help/how-to-connect-onvif-confirmant-ip-cameras-to-a-lorex-x-series-nvr
- Warranty: "The Lorex warranty covers the Product for one (1) year from the documented date of purchase. Some exceptions apply." https://www.lorex.com/pages/warranty ; Lorex PRO: "three (3) years ... through the Lorex for Business Partner Program" https://pro.lorex.com/pages/warranty
- Subscription: "Lorex security cameras and systems do not require a subscription"; Connect Cloud+ up to 60 days cloud retention for supported smart motion events https://www.lorex.com/blogs/news/own-your-security-own-your-footage-no-required-monthly-fees-with-lorex ; Connect Cloud+ Single Camera $5.99/mo, Multi-Camera $16.99/mo https://www.lorex.com/pages/connect-cloud (from research/best-security-camera-brands.md, 2026-11-02)
- Ownership: Dahua Technology press release "DAHUA TECHNOLOGY TO SELL LOREX TO SKYWATCH", around $72 million USD, Skywatch = privately held cloud services company headquartered in Taiwan https://www.dahuasecurity.com/mena/newsEvents/pressRelease/7717 ; Security World Market "Dahua to sell Lorex to Skywatch for USD $72 million" (Hangzhou / Taipei / Ontario, Canada) https://www.securityworldmarket.com/int/News/Business-News/dahua-to-sell-lorex-to-skywatch-for-usd-72-million ; Wikipedia Dahua refs dated Dec 2022 / Mar 2023. Exact closing date NOT CONFIRMED → page states only "Dahua announced it was selling Lorex to Skywatch ... for about $72 million" and gives no year.
- Reddit/ipcamtalk claim that Lorex cameras were Dahua OEM: forum opinion only → page says "for years Lorex was owned by Dahua" (fact from press release) and does not claim current hardware origin.

## Reolink (manufacturer pages)
- RLN16-410 16-channel PoE NVR https://reolink.com/product/rln16-410/ : up to 24 IP cameras (max 16 wired); up to 16MP; 2 × SATA, up to 16 TB (max 8 TB per HDD); ships with 3 TB HDD; 16 PoE ports, max 25 W per port, IEEE 802.3af/at; total PoE budget NOT CONFIRMED on page; person/vehicle/animal detection (depends on hardware version); Reolink App + Reolink Client; 2-year limited warranty. ONVIF, subscription, smart home: not on that page.
- Duo 3 PoE https://reolink.com/product/reolink-duo-3-poe/ : 7680×2160 (16MP) at 20 fps; f=2.8 mm F1.6; 180° H / 55° V; IR 30 m; color night vision with spotlight (8 pcs, 5 W, 6500 K, 560 lumens); IEEE 802.3af; microSD up to 512 GB; two-way audio; person/vehicle/animal detection; IP67; ONVIF yes; Google Assistant; Reolink App; 2-year limited warranty.
- RLC-810A https://reolink.com/product/rlc-810a/ : 3840×2160 (8MP) at 25 fps; lens options 2.8 mm (101° H), 4 mm (87° H), 6 mm (53° H), F2.0; IR 30 m (100 ft); 802.3af, <12 W; built-in mic (audio recording); person/vehicle/animal detection; microSD up to 512 GB; IP67; −10 °C to +55 °C (14 °F to 131 °F); RTSP & ONVIF; 2-year limited warranty.
- ONVIF store page https://store.reolink.com/onvif-camera/ : PoE and plug-in Wi-Fi models (RLC, E1 Outdoor, Duo series) support ONVIF on their own; battery models (Argus, Altas) need a Reolink Home Hub; NVR kit cameras need a Reolink NVR; "A Reolink NVR can also pull in third-party ONVIF cameras"; Blue Iris, Synology Surveillance Station, QNAP; default ONVIF port 8000.
- Third-party compatibility table https://reolink.com/3rd-party-compatibility/ : Blue Iris, Milestone, iSpy, Digital WatchDog listed "Yes".
- Subscription: no subscription required https://reolink.com/blog/reolink-subscription-cost/ (hub research 2026-11-02); cloud plan price NOT CONFIRMED (cloud.reolink.com shows LTE plans) → page states no Reolink cloud price.
- Company: "Founded in 2009" https://m.reolink.com/us/about-us/ ; US office 13668 Valley Blvd Unit C1, City of Industry, CA https://m.reolink.com/us/contact-us/ .

## FCC Covered List (checked 2026-11-03)
- https://www.fcc.gov/supplychain/coveredlist , page dated Friday, October 23, 2026: companies named include Dahua Technology Company and Hangzhou Hikvision Digital Technology Company; Lorex and Reolink are not named.

## AESS installed prices used (own pages only, NYC rate; never next to a store price)
- /lorex-camera-installation-prices-nyc (title on 2026-11-03): 4 cameras from $1,827; cameras installed from $272 each; recorders with setup from $510; 4 × 8MP H12 bullet (E863SB) $1,903; 4 × 12MP E910AB $2,243; packages include Lorex Connect VC 4K 8-channel NVR, "2+ weeks of recording", wire runs up to 100 ft per camera, phone app setup. (Hub listed $1,939 on 2026-11-02: price pages move with equipment cost, page says "at the time of writing" and links to the live page.)
- /reolink-camera-installation-prices-nyc (2026-11-03): 4 cameras from $1,579; cameras installed from $266; recorders with setup from $290; 4 × RLC-810A $1,719; 4 × 12MP RLC-1212A / RLC-1224A $1,839; packages include Reolink RLN4E, 2+ weeks of recording, wire runs up to 100 ft, phone app setup.
- Both price pages: hidden in-wall wiring in hollow drywall $200 more per camera, up to 100 ft; spray foam, plaster, brick and exterior walls checked on site.
- Non-branded default: /security-camera-installation-nyc residential from $950 (hub research). §12.5: quotes still default to the non-branded system.

## Images (11)
- 4 Lorex product photos from our library (images/lorex-camera-installation/, images/floodlight-lorex.png), 2 Reolink product photos (images/nvr-reolink-nvs8.png, images/floodlight-reolink.png — Reolink logo visible on both, checked by eye), 5 AESS job-library photos (recorder monitors, dome in drop-ceiling corner, camera above bulkhead, dome under eave). images/reolink-video-doorbell.webp NOT used: it shows a Speco Technologies doorbell (mislabeled file). images/reolink-camera-installation/*network-installation* NOT used: crew photos look AI-generated. Reolink manufacturer CDN download blocked in build env (proxy 403), so no Duo 3 PoE photo.

## Question register (lorex-vs-reolink)
- Is Lorex or Reolink better for a house in New York City?
- Is Reolink vs Lorex the same comparison?
- Do Lorex or Reolink need a monthly subscription?
- Can a Reolink NVR record Lorex cameras, or the other way around?
- Which has better night video, Lorex or Reolink?
- Which brand has the longer manufacturer warranty?
- Is Lorex still owned by Dahua?
- Are Lorex or Reolink on the FCC Covered List?
- Which works with Alexa or Google?
- Can I install Lorex or Reolink myself instead of hiring an installer?
- How much does it cost to have a 4-camera Lorex or Reolink system installed in NYC?
- Will you install a Lorex or Reolink kit I already bought?
