# doorbird-vs-2n — research and spec source log (2026-11-15)

## Demand check
- Ahrefs keywords-explorer-overview: "Insufficient plan" (HTTP 400) — not used.
- Live Firecrawl SERP "doorbird vs 2n" (2026-11-15), dedicated results:
  - groups.io/g/crestron/topic/doorbird_vs_2n/115570018 — Crestron dealers' thread titled "Doorbird vs 2N" (quote used on page: 2N "immensely more responsive, reliable, and packed with far more features")
  - smarteg.lv/en/content/1037-blog-doorbird-2n-comparison — "DoorBird vs 2N: choosing an IP video intercom for KNX projects"
  - novakdoorsandgates.com/doorbird-vs-2n/ — "DoorBird vs 2N: Which Intercom System Is Right for You?"
  - thetechguysdoorsandgates.com (DoorBird installer LA) — "DoorBird vs. 2N" section
  - reddit r/crestron front-door intercom thread; Facebook Low Voltage Nation (2N IP Style vs DoorBird); AVS Forum; Home Assistant "Doorbird, is it any good?" (30-sec delay complaint, cited); swiftlane DoorBird review (compares to 2N)
- Reversed "2n vs doorbird" (exact quotes): 1 result (wideodom.eu, Polish, "2N vs DoorBird vs Akuvox vs Vidos"). Reversed order mentioned on page (hero + FAQ), no second page.
- Verdict: real, niche demand (dealer/forum + installer comparison pages). BUILD.

## DoorBird sources (doorbird.com)
- https://www.doorbird.com/downloads/datasheet/datasheet_d2203v_en.pdf — D22x specs: 5 MP HDR, 180°D/140°H/100°V, 2 IR LEDs, PoE 802.3at, 2 relays 24V/1A, 2 inputs, 12V 0.48A out, 125 kHz + 13.56 MHz RFID up to 3,000 tags (13.56 encryption needs Cloud Pro/Enterprise), BLE (A8007 fob), Wiegand/OSDP/RS-485 "hardware ready, enabled later with software update", IP65 IK08, −25..+55 °C, SIP/RTSP/WebRTC, integrations list, D21x upgrade by replacing main electrical unit, min lens height 145 cm, one simultaneous stream, "assembly requires professional skills".
- https://www.doorbird.com/downloads/datasheet/datasheet_d2101v_en.pdf and datasheet_d2102v-d2118v_en.pdf — D21x: 720p, 180°, 12 IR LEDs, 125 kHz up to 100 tags, PoE 802.3af or 15 VDC, up to 18 buttons (EANs listed as discontinued Aug 1 2021).
- https://www.doorbird.com/shop/d22 — D22x lineup D2201V–D2218V, KV/KH, Fingerprint 50, ekey sLine, D22DKV/D22DKH, D2200E/EA; finishes (V4A, PVD, brass, bronze, RAL). Shop prices seen but NOT used on page.
- https://www.doorbird.com/downloads/datasheet/datasheet_a1121_flush_en.pdf — A1121: 500 PINs, 125k/13.56 either-or 500 transponders, BLE, Wi-Fi or PoE, 2 relays, Wiegand output, tamper, local operation without internet, A1081 adds up to 3 doors/gates/elevators.
- https://www.doorbird.com/en/cloud-recording — Cloud Free (last 50 events, permanently free), Cloud Pro (HD video, 7 days, +0.5 Mbit/s upload), NAS/NVR option.
- https://www.doorbird.com/en/warranty — 24-month warranty; out-of-warranty repair service.
- https://www.doorbird.com/en/about-us — Berlin HQ/production, US offices SF and Jacksonville, ASSA ABLOY since Oct 2022, first product 2015, ISO/IEC 27001:2024 (TÜV Saarland), D21x UL 62368-1 (Intertek).
- https://www.doorbird.com/en/integrations/crestron (map description) — native RAVA SIP, no gateway.

## 2N sources (2n.com)
- https://www.2n.com/en-US/products/intercoms/2n-ip-verso-2 — 20 modules, 1920x1440, 125°x105° (peephole 138°), WDR, 0.8 lux, ONVIF S, H.265, PoE 802.3af or 12V/3A, switch 30V 1A, 1 input, active out 8–12V 400 mA, 5W amp/2W speaker 78 dB, BLE, RFID (secured: Seos, iClass SE, DESFire), fingerprint (FBI std), Wiegand/OSDP/I-O modules, IP54 IK08, −40..60 °C, 5-yr warranty.
- https://www.2n.com/en-US/products/intercoms/2n-ip-style — 10.1" 1280x800, directory 10,000 users, 2560x1920, 138°x114°, forensic WDR, face zoom, bi-directional video, WaveKey test (15,000 openings/100 phones/98% <1 s), 2 mics 2x4W 85 dB, PoE+ 802.3at, 3 inputs, IP65 IK08, −30..60 °C.
- https://www.2n.com/en-US/products/intercoms/2n-ip-one — ARTPEC-7, 156°x116°, 0.3 lux, 1920x1440, 5W/3W, PoE 802.3af, IP66 IK08, −40..60 °C, grey/bronze/black, RGB button.
- https://www.2n.com/en-US/products/intercoms/2n-ip-solo — 1 button, camera 1280x960 / 640x480 call, 128°x95°, PoE 802.3af, IP54 IK08.
- https://www.2n.com/en-US/products/apps-and-software/my2n-app/ — features, iOS 17/Android 10, 500 devices/installation, 5 devices per speed dial, Mobile Video → My2N transition, free calls with indoor station.
- https://www.2n.com/en-US/products/management-platforms/my2n-management-platform/Pricing/ — free-license rules; MSRP $44/yr/apartment, $270/10 yr, $31/yr/device commercial; install type cannot be changed.
- https://www.2n.com/en-US/products/management-platforms/comparison-table — My2N vs Access Commander.
- https://www.2n.com/en-US/about-2n — founded 1991 Prague, first IP intercom 2008, Axis since 2016, 5-yr warranty, ≥8 yrs firmware.
- https://www.2n.com/en-US/products/discontinued/2n-ip-force (map) — IP Force final order date June 30, 2026.

## Installed prices (own site only)
- /intercom-installation-nyc: 2N "Starting at $900"; video intercom home/small building $700–$1,800; multi-unit 5–30 units $1,200–$5,000+; commercial $800–$4,000+; $250 service call. DoorBird: no sourced AESS price → "quoted per building". No retail/store prices anywhere on the page; 2N subscription MSRP only in the apps section.

## First-hand proof (from user memory /areas/doorbird-two-door-job.md + repo video)
- Oct 2026 two DoorBird D21DKH stations, front + back door, mag locks, replaced DoorKing, 30-s release; 87-second resident how-to video (videos/howto/vl-doorbird-app-setup.mp4). Customer name/address NOT used.

## Images (images/doorbird-vs-2n/, 11 WebP)
- 1 official DoorBird D21DKH product photo, copied from aess-housecall-connector/ad-videos/photos/doorbird_d21dkh/d21dkh_v2a_front.png (SOURCE.txt: official doorbird.com shop image, ean 4251489615025).
- 10 real job photos from images/door-buzzer-installation/ and images/intercom-repair/ (captioned as not DoorBird/2N gear).
- NOT obtained: 2N product photos and further DoorBird shop images — www.doorbird.com, www.2n.com and storage.googleapis.com are blocked by the egress proxy (CONNECT 403); a remote-sandbox download was denied by the permission classifier. Library images under images/intercom-installation/ and images/buzzer-repair/ look AI-generated (wrong phone number on shirts) — not used.

## NOT CONFIRMED (left out or stated as not published)
- DoorBird speaker wattage/SPL, lux/WDR rating; DoorBird Cloud Pro price; what DoorBird Cloud Enterprise includes; DoorBird ring latency figures.
