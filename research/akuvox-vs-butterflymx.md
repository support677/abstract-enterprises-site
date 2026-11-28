# akuvox-vs-butterflymx — research and spec source log (2026-11-16)

## Demand check
- Live Firecrawl SERP "akuvox vs butterflymx" (2026-11-16), dedicated results:
  - reddit.com/r/sanfrancisco/comments/1jadb5q/butterfly_mx_vs_akuvox/ — thread titled "Butterfly MX vs. Akuvox" (ButterflyMX pros: customer service, reviews, app; cons: "susceptibility to vandalism, Windows-based" — quoted on page as a forum claim, OS NOT confirmed by butterflymx.com)
  - butterflymx.com/blog/akuvox-intercom-review/ — ButterflyMX's own Akuvox review with an "Akuvox vs. ButterflyMX" section
  - academyintercom.com/comparing-intercom-system-manufacturers-butterflymx-and-akuvox/ — "ButterflyMX ... cloud-based technology only, while Akuvox ... on-premise, cloud-based and Plug-and-Play" (paraphrased on page)
  - globalvisionsinc.com/a-comparison-akuvox-butterflymx-2/ — "A Comparison: Akuvox & ButterflyMX"
  - beelocksmith.com/guide-butterflymx-vs-akuvox-vs-comelit.html — NYC co-op/condo guide ("ButterflyMX is app-first; Akuvox can add in-apartment monitors")
  - doorvi.co ButterflyMX alternatives (lists Akuvox), ipvm.com ButterflyMX discussion, Facebook fb-answers comparisons
- Reversed "butterflymx vs akuvox" (exact quotes): beelocksmith.com guide + its guide index pages, Facebook fb-answers "ButterflyMX vs Akuvox vs Doorbird for multi-tenant buildings". Reversed order mentioned on page (hero + FAQ 2), no second page.
- Verdict: real demand (forum thread, maker's own vs-section, several installer comparison pages, NYC locksmith guide). BUILD.

## Akuvox sources (akuvox.com / knowledge.akuvox.com)
- https://www.akuvox.com/productsDisp?pid=53 and productsDispParameter?pid=53 — X912: 4" touchscreen, dual cameras (main starlight), keypad, QR, face, IC/ID/NFC/BT; X912S stainless IP65 IK10; X912K aluminium IP65 IK08, HID iCLASS version; PoE+ or external; Linux; surface/flush. Related-products list gives the model range (S539, S538, S535, S532 "2.8” SIP Video Door Phone", X916, X915, X912, X910, R29, R28, R25K, R20K, R20K-L, R20B, E21, R25A, R20A, E18, E16, E13S, E12, E20S).
- https://www.akuvox.com/productsDisp?pid=104 — X910: single-button, package detection, dual cameras, 13.56 MHz NFC, Linux, surface mount, IP66 IK08, "designed for high-end homes".
- https://www.akuvox.com/productsDispParameter?pid=17 — R29: 7" IPS 1280x800, Android, R29S 3 MP, R29C dual camera, IP65 IK06, PoE 802.3af, Wiegand, 13.56/125 kHz, face recognition, R29C-L LTE.
- https://www.akuvox.com/productsDispParameter?pid=81 — S539: Android 12, 10", HDR + starlight main camera, dual cameras anti-spoofing, extra QR camera, PoE+ or external. (Page icons: IP66, IK08, ONVIF, Wiegand.)
- https://www.akuvox.com/productsDispParameter?pid=113 — S535: 5" IPS, Linux, 2 MP 1/2.9" CMOS, up to 1920x1080 30 fps, HDR, 0.1 lux, viewing angle 110°H/62°V in video spec but 116°H/62°V in "At a Glance" (both noted on page), face/card/PIN/BLE/QR, 13.56 MHz/125 kHz/NFC, Wiegand, RS-485, 1 relay, 2 inputs, LTE/fingerprint/induction-loop modules, 802.3at PoE, 12V/4A, IP66 IK08, 210x100x27 mm, -40..+55 °C, RTSP, NVR compatible.
- https://www.akuvox.com/productsDispParameter?pid=91 — S532: aluminium die-cast, display listed as 8" LCD on key-spec page while the related-products list calls it a 2.8" door phone (inconsistency stated on page), 130°H x 90°V, PIN/IC/ID/NFC/BT, 2 relays, PoE+ or external, IP66 IK08; IP, hybrid (analog handset) and induction-loop versions.
- https://www.akuvox.com/productsDispParameter?pid=54 — E18: 7" 600x1024, 2 MP WDR, IP65, PoE 802.3af, Wiegand, RS-485, 125 kHz & 13.56 MHz, LTE optional, face recognition.
- https://www.akuvox.com/productsDispParameter?pid=46 — A02: touch keypad, 13.56/125 kHz & NFC, 20,000 cards, 100,000 logs, tamper, PIN/RFID/2FA, IP65, 802.3af PoE or 12 V DC.
- https://www.akuvox.com/productsSoftwareForIntercom — SmartPlus app (cloud intercom service, virtual keys), My MobileKey (wave-to-unlock, AES256, ACMS integration), Installer Kit Tool (S563W hardware, PoE + Wi-Fi), ACMS, ACMS Pro, SDMC (on-premise community intercom software).
- https://knowledge.akuvox.com/docs/power-supply-for-intercom-devices — PoE class per model (802.3af: R20/R25/E12/E16C/E18C/E21/E20S; 802.3at: S532/S535/S538/S539/X912S/X915S/X916S; no PoE: R29C-L, R20A-2/R20K-2 2-wire 48 V), indoor monitors list (X937, S567, S565, S563, S562, S560, IT88, C319, C316, C315, C313, C313-2 2-wire, C310), EC33 elevator controller, A094, A095, A15, A08, A01-A05, WR01.
- https://knowledge.akuvox.com/docs/devices-supporting-12v-power-output — 12 V output via relay: X912S/X912K/S539/S535 12V/1A; S532 and R29 V1.1 12V/500mA; A094 4 ports 12V/800mA; A095 8 ports.
- https://knowledge.akuvox.com/docs/which-door-phones-and-access-control-devices-support-unified-http-apis — unified HTTP API model list.
- https://knowledge.akuvox.com/docs/akuvox-smartplus-installer-guide-community — feature plan per community, "indoor monitors with SmartPlus as backup" call type (premium), indoor-monitor requirement setting, Apple Wallet = paid feature, Landline Service premium, extra family accounts need activation fees, PIN / APT+PIN modes, akubela smart home.
- Press releases (search snippets, titles only): companyPressReleaseDisp?aid=12 Genetec integration (dateline "Xiamen, China"), aid=16 Tuya integration, aid=43 SmartPlus + Rent Manager, aid=17 A01/A02/A03/A05 launch.
- akuvox.com privacy text: "akuvox.com is the official website of Akuvox, targeting enterprise users."

## ButterflyMX sources (butterflymx.com)
- https://butterflymx.com/products/video-intercoms/ — 8"/12" surface/recessed; cast aluminium alloy, IP65, -40 °F..+140 °F, Wi-Fi & RFID, wide-angle 156° FOV, adaptive bitrate up to 1080p, IR proximity sensors, 2x USB 3, four dry-contact relays (2 A, 62.5 VA), NEMA 5-15 socket, 9-24 VDC input, 12.7 W standard / 34 W max at 24 VDC, dedicated circuit on UPS, dimensions (8" surface 11.5x5.6x2.4 in; 8" recessed 15.3x8.7x2.4; 12" surface 12.4x11.6x2.4; 12" recessed 13.3x13.6x2.4), capacitive multi-touch, up to 1,500 nits, 720x1280 (8") / 1280x800 (12"), DHCP or static IP, wired & wireless, UL/FCC/CE; FAQ: app opens doors/gates/garages/elevators; installed by local low-voltage installer; needs internet, power, door strike; updates pushed to all users; polycarbonate vandal-resistant screen.
- https://butterflymx.com/products/video-intercoms/7-surface/ — 8" surface: "It's wireless! ... won't have to wire the entire building or install expensive in-unit hardware".
- https://butterflymx.com/pricing/ (redirects to /cost/) — one-time hardware fee + annual software fee per apartment unit; $30–$42 per unit per year; app, new features, live phone/email support included; two-year hardware warranty, not against vandalism or incorrect installation. STORE PRICES SEEN ($3,995, "regular price" $6,995 / $5,495) — NOT used on page.
- https://butterflymx.com/products/keypad/ — 6-digit PIN, 2" read range, mobile/fob/keycard, entry photo stored 365 days, Alexa/Siri unlock, elevator control compatible, 5-16 VDC, IP55, -31..150 °F, EAL6+, OSDP secure channel, UL 294, powered and networked via Access Controller.
- https://butterflymx.com/products/access-control-system/ — Mullion/Keypad/Single Gang readers; installs over most existing systems, needs internet + power; controller 12-24 VDC 60 W; REX, emergency unlock, fire exit switch, push-to-exit, door state sensor; outputs strike, mag lock, push/crash bars, elevator panels, gate/garage controllers, dry relay; FCC, IEC 62599, UL 294, UL 62368; 2-year warranty.
- https://butterflymx.com/about/ — founded 2014 by Cyrus Claffey; 20,000+ properties; HQ New York City, Toronto, Croatia.
- https://butterflymx.com/resources/installers/documentation/ (search snippet) — headings for recessed intercom quick start, wiring guides, "Cellular connectivity".
- https://butterflymx.com/video-intercom/ — old noindex AdWords page ("same wiring" claim) — NOT used.

## Installed prices (own site only)
- /intercom-installation-nyc: AKUVOX Smart IP Intercom "Starting at $950"; BUTTERFLYMX Smartphone-Based Intercom "Starting at $1,500"; multi-unit 5–30 units $1,200–$5,000+; commercial $800–$4,000+; elevator access control $1,500–$6,000+; $250 book & pay / service call.
- /butterflymx-installation-nyc: installation = written quote after site visit; hardware & subscription "Set by ButterflyMX"; $250 service call; "We price a no-subscription alternative alongside every ButterflyMX quote."
- /intercom-pricing: $250 service call. No retail/store prices anywhere on the page. ButterflyMX's $30–$42/unit/yr software fee appears only in the running-costs section and FAQ, never next to our prices.
- NOTE for Anwar: /intercom-installation-nyc says "Starting at $1,500" for ButterflyMX while /butterflymx-installation-nyc says hardware and subscription are set by ButterflyMX and installation is quoted after a site visit; the page states both as written.

## First-hand facts used (from user memory, no names/addresses on page)
- Brooklyn school elevator access project: Akuvox A02 readers (landings + cabs), A094S door controllers (5th-floor closet), EC33 elevator controllers (machine room), reused old keypad cabling; elevator company dry contacts/diagram (memory /areas/williamsburg-charter.md).
- Mag lock + Akuvox A02 keypad packages for stores/restaurants/offices (memory /areas/aess-pricing.md; price NOT used).
- Oct 2026 recommendation of Akuvox X915S in a surface box with rain hood for a driveway gate (housecall-connector outbox email, customer not named).

## Images (images/akuvox-vs-butterflymx/, 11 WebP)
- 7 Akuvox product photos (X915S, E18C, A02, A094S from aess-housecall-connector/webhooks/docs/photos — the cut-sheet library that only holds real manufacturer/retailer photos; keypad door station, white indoor monitor, single-button station from existing repo product-photo images). Not re-downloaded from akuvox.com: www.akuvox.com and butterflymx.com image downloads blocked by the egress proxy (CONNECT 403) on 2026-11-16.
- 1 real job photo: back of an Akuvox reader with terminal wiring, Brooklyn, Nov 13 2026 (images/job-photos/access-control-installation/).
- 3 job photos from our library (cable rack, cables over beam, tiled corridor) captioned as not Akuvox/ButterflyMX gear.
- NO ButterflyMX photo: none in the repo and butterflymx.com blocked.

## NOT CONFIRMED (left out or stated as not published)
- Akuvox warranty terms; Akuvox SmartPlus prices; ButterflyMX panel OS (Reddit says Windows); ButterflyMX camera sensor/lux/IR; ButterflyMX behaviour when internet is down; Akuvox founding year/headcount (companyProfile/companyAboutUs 404).

- 2026-11-16 (max-daily): removed from the page before shipping — references to the Brooklyn school elevator job (silo rule: never name the school job) and a customer driveway-gate recommendation taken from an outbox email.
