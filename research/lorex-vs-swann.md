# Research: lorex-vs-swann (comparison page, BLUEPRINT §12.5)

Built 2026-11-05 by the max-daily run (Anwar's Max plan, no API spend). Every fact on the page traces to a line here.
Fetched with Firecrawl search/scrape on 2026-11-05. "NOT CONFIRMED" = not confirmed on a manufacturer page, so the page does not state it (or says "not stated").

## Search demand check (§12.5: confirm real demand first)
- query "lorex vs swann" (Firecrawl web search): dedicated results from security.org/security-cameras/lorex-vs-swann/ ("Lorex beats Swann with better app usability and versatility ... Swann excels in heat-sensing tech"), lorex.com/pages/lorex-vs ("security.org scores Lorex at 9.6 rating, compared to Swann's 8.1"), lorex.com/blogs/news/lorex-vs-swann-home-security-cameras-1, vueville.com "Lorex vs. Swann - The Most Popular IP Cameras Compared" ("Lorex supports ONVIF, Swann doesn't"), YouTube "Lorex vs Swann Security – How Do They Compare", cctvforum.com "Swann vs. Lorex vs. Q-See vs. Night Owl", trustyjoe.com/lorex-vs-swann/, Facebook fb-answers/lorex-vs-swann, reddit r/homedefense "Lorex or Swann? Or neither?". → demand confirmed (also listed in research/best-security-camera-brands.md vs-pair spot check, 2026-11-02).
- query "swann vs lorex reddit which is better": r/homedefense 1e64o4q ("The Swann kit was better, but only really because it came pre-configured as a kit"), r/homedefense 6nvvp7 ("Both Lorex and Swann are good ... Lorex has less cameras but higher resolution(4K) than Swann"), r/homesecurity ht07rd "Reolink vs Lorex vs Swann?" ("Just stay far far away from lorex ... customer service ... horror stories"), r/videosurveillance 1mjm7rh "Swan or Lorex Doorbell" ("Swann is OK. Just beware that they are currently changing over their ecosystem and older models may not be supported in the near future"), r/homedefense kcrwe5, r/homesecurity u79ngd ("Lorex and Swann seem to be disappointing according to reviews"). Used in "What Owners on Reddit and Camera Forums Report" (paraphrased, labeled as owner opinion) and as FAQ stand-ins. People Also Ask panel: EMPTY (not returned in build env).
- Gap: ranking pages are reviewers, Lorex itself and forums; none is an installer that wires both → page angle.
- Reversed order "Swann vs Lorex" in the same SERP (cctvforum, reddit) → mentioned on this page; no second page.

## Swann (manufacturer pages)
- EliteX 6K/12MP NVR system with 4 bullets SWNVK-8EX412MPB https://us.swann.com/products/swnvk-8ex412mpb-us : NVR display up to 4K; recording up to 16MP (depending on camera); camera video 6K/12MP; frame rate NOT STATED; viewing angle 90°; lens NOT STATED; night vision 82 ft/25 m (total darkness); color night vision up to 82 ft/25 m (color with sensor light); sensor lights yes; 2-way audio & siren; mic yes; IP66; −22 °F ~ 131 °F; "8 Channels on NVR + 8 Cameras via Network (Up to 16 cameras)"; 2 TB included, up to 8 TB; PoE, 8 PoE ports; PIR Thermal / Motion Sensor: No; Smart analytics: video-based motion, people & perimeter intrusion detection; AI detects people, vehicles and motion; Swann Security App; cloud backup optional via subscription; "no subscriptions or surprises"; smart home, ONVIF, warranty NOT STATED on page. Swann CDN image download blocked in build env (proxy 403).
- AdvancedX Wired 4K NVR system SWNVK-8ADVANX4B https://us.swann.com/products/swnvk-8advanx4b-us : 4K; frame rate NOT STATED; 90°; IR 100 ft/30 m; color up to 50 ft/15 m with sensor light; lights yes; siren No; audio one way (mics); IP66; −22 °F ~ 131 °F; 8 channels; 1 TB included, up to 8 TB; wired PoE; detection video-based motion, people, vehicle, line crossing, perimeter intrusion, sound detection; Swann Security App; 24/7 recording; cloud via Secure+; smart home / ONVIF / warranty NOT STATED. (us.swann.com/products/swnhd-advancxb returned 404.)
- Secure+ plans https://us.swann.com/pages/secure-plans : Free (no subscription; cloud: Evo range none, all others 1 day); Extra USD $4.99/mo or $49.99/yr, 1 device, 60 days, alerts for people/vehicles/pets/packages, dynamic notifications, lifetime extended warranty, insurance coverage, priority support; Unlimited USD $12.99/mo or $129.99/yr, unlimited devices, 60 days, same benefits.
- Warranty https://support.swann.com/hc/en-us/articles/45069252673177-What-is-Lifetime-Warranty : "24-month manufacturer's warranty on all devices purchased from swann.com website in Australia, United States, Canada and United Kingdom in 2025 ... Devices sold prior to 2025 may only have 12-month"; extended to 36 months or more with active subscription activated within 6 months; ends if subscription cancelled; device must never be unpaired/removed; "Lifetime Support" ≠ lifetime warranty. (us.swann.com/pages/warranty returned 404.) Also support article 40119773071513 snippet: brand-new units bought on swann.com in 2025 have a 2-year standard warranty.
- Google Home https://support.swann.com/hc/en-us/articles/49401506825625 : "Google Home Integration Discontinued August 2025 ... All existing and new account links are now disabled, and streaming via Google Home devices is not supported ... please use the Swann Security app". Alexa: NOT CONFIRMED → page says "other assistants not stated".
- ONVIF: NOT STATED on either Swann system page. Search: JustAnswer / VisioForge / IP Cam Talk user reports that some Swann NHD models and firmware accept ONVIF; IPVM discussion "Why do Swann and Q-See deny ONVIF"; Swann refund policy "cannot support third party software" https://us.swann.com/policies/refund-policy → page treats Swann as Swann-only unless the model's docs say otherwise.
- Camera compatibility chart https://cdn.swann.com/media/wysiwyg/docs/swann-camera-compatibility.pdf (search result) → "Swann publishes a camera compatibility chart".
- Company: "Founded in 1987 in Melbourne, Australia" https://us.swann.com/pages/about-swann ; Swann Communications Pty. Ltd., Port Melbourne https://au.swann.com/ ; LinkedIn "basement of David Swann's family home ... pioneered the category of Do-it-Yourself security" https://www.linkedin.com/company/swann-communications-usa . protectfind.com.au says Infinova bought Swann in 2014 — third party only, NOT used.

## Lorex (manufacturer pages, from research/lorex-vs-reolink.md 2026-11-03, re-used)
- N910A62 Fusion NVR: 16 cameras (8 wired + 8 Fusion Wi-Fi); 2 TB, up to 16 TB, 1 bay; PoE 25.5 W/port, 72 W total; detection person, vehicle, face, mask, package, animal; Lorex Home (+ Lorex Classic, Lorex Cloud client); Alexa, Google Assistant, Chromecast, Echo Show, Google Home Hub; no monthly fees.
- E910AB 12MP bullet: 4640×2624, 15 fps all resolutions; 139°; 2.8 mm F1.6; IR 98 ft/30 m; Color Night Vision; Smart Security Lighting; warning light + siren + pre-recorded message; mic + speaker; PoE 802.3af; IP67; −22 °F to 140 °F; ONVIF G/S/T.
- ONVIF G/S/T compliant; "Lorex NVRs are designed to work best with Lorex cameras"; X Series ONVIF help article.
- Warranty 1 year; Lorex PRO 3 years via Lorex for Business Partner Program.
- Connect Cloud+ $5.99/mo single, $16.99/mo multi, up to 60 days.
- Dahua press release: sale of Lorex to Skywatch (Taiwan, privately held cloud services) ~US$72 million; no year stated on page.

## FCC Covered List (checked 2026-11-05)
- https://www.fcc.gov/supplychain/coveredlist , last updated Friday, October 30, 2026: names Digitalsystem Technology, Kaspersky (x2), China Unicom Americas, Pacific Networks, ComNet, China Telecom Americas, China Mobile International USA, Dahua Technology, Hangzhou Hikvision, Hytera, ZTE, Huawei. Lorex, Swann, Infinova, Skywatch: not named.

## AESS installed prices used (own pages only, NYC rate; never next to a store price)
- /lorex-camera-installation-prices-nyc (2026-11-05): title "4 Cameras from $1,899"; cameras installed from $290 ($290 to $1,450); recorders with setup from $510; 4 × E910AB $2,243. (Was $1,827 on 2026-11-03 — price pages move.)
- /swann-camera-installation-prices-nyc (2026-11-05): title "4 Cameras from $1,779"; cameras $290 to $400 installed; SWNVK-8EX412MPB $1,799; SWNVK-8ADVANX4B $1,819; list includes analog DVR kits (SWDVK-*) and EVO Wireless Video Doorbell SWIFI-EVOVDB.
- Both: hidden in-wall wiring in hollow drywall $200/camera up to 100 ft; at least 2 weeks recording; wire runs up to 100 ft; phone setup; plus sales tax.

## Images (11)
- 3 Lorex product photos (images/lorex-camera-installation/: black bullet with red/blue warning LEDs, white turret with spotlight, black floodlight two white panels), 2 Swann product photos (images/alarm-installation/…swann-floodlight-with-motion-sensor-product-photo.webp — Swann logo visible; images/nvr-swann-advancedx-4k.png — "swann AX" recorder front/rear, 8 PoE ports), 6 AESS job-library photos (ceiling dome facing glass entrance, recorder per-channel bitrate screen, network cable bundles, dome on wall arm over stone facade, bullet on pole mount in drop ceiling, turret in storage-room corner). All checked by eye; none used on lorex-vs-reolink. Duplicates noted: images/nvr-installation/*swann-recorder* = same photo as nvr-swann-advancedx-4k.png; floodlight-camera-installation/*white-swann-floodlight* = same photo as the alarm-installation Swann floodlight. images/floodlight-swann-4k.png NOT used (mislabeled, per hub log).

## Question register (lorex-vs-swann)
- Which is better for most New York homes, Lorex or Swann?
- Is Swann vs Lorex a different comparison from Lorex vs Swann?
- Do Swann or Lorex systems charge a monthly fee?
- Does Swann still work with Google Home?
- How long is the Swann warranty compared with Lorex?
- Can I add Lorex cameras to a Swann recorder, or Swann cameras to a Lorex recorder?
- Do current Swann cameras still use heat sensing?
- Which brand covers a wider area with one camera?
- Are Swann or Lorex cameras banned by the FCC?
- What does a 4-camera Lorex or Swann system cost installed in NYC?
- My old Swann or Lorex system stopped connecting to the app. Should I replace it?
- What should I send you before you install a Swann or Lorex kit I bought?
- (headings) 1. How many cameras will this property need in three years? 2. Will anyone use a voice assistant or a TV to watch the cameras? 3. Is the goal to record what happened, or to stop it? 4. How long must the video last? 5. How much do you care about the manufacturer warranty? 6. Could you ever want a camera from another brand?; Who Makes Lorex and Swann, and Does It Matter?; Lorex or Swann ... headings.
