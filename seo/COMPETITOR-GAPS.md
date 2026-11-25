# Competitor gaps queue (weekly competitor sitemap watch)

Weekly scheduled task. Pulls each competitor's sitemap (list and snapshot in `seo/COMPETITOR-SITEMAPS.json`), diffs it against last week, and matches every new or changed competitor page to our site. This file holds the GAPS: intents a competitor has a page for and we don't.

**Rules (Anwar, HARD):**
- A page for a NEW service, brand or topic is never built until Anwar supplies its keyword list in `keywords/<slug>.md`. Those gaps are marked **NEEDS KEYWORD LIST**. Once the file exists, the next run moves the gap into PAGE-QUEUE.md (hubs/boroughs/counties before neighborhoods) the way DAILY-RUN.md describes.
- Never build a page that competes with one of our existing pages. Never delete or rename pages. Never "AESS" on the site. No Anwar byline. Only prices Anwar has set.
- Never copy competitor wording. Beat them with first-hand job proof under the ranking-principles skill.
- COVERED pages where the competitor's version is newer or deeper go to `seo/PAGE-DECAY-LOG.md` (competitor-watch candidates) for the weekly decay refresh. This task does not rewrite them.

Priority: P1 money service / brand / audience pages, P2 cost, law and troubleshooting guides (AI-citation content per BLUEPRINT), P3 blogs.
Demand evidence: our Search Console (sc-domain property, Composio, openeyesales@gmail.com), 90 days Aug 24 – Nov 22 2026, shown as impressions @ average position. Ahrefs keywords-explorer not used (free plan, 0 units).

---

## 2026-11-24 — run 1 (full baseline)

**Not done this run:**
- 0 gaps went into PAGE-QUEUE.md. Every gap below is a new brand, audience or topic with no keyword list in `keywords/` yet, so all are **NEEDS KEYWORD LIST** (or held). The only related list, `keywords/door-buzzer-repair.md`, covers a service we already have pages for.
- momentumsecuritysystems.com: both sitemap URLs return a parked-domain ad 404. No baseline. Check its homepage next run and drop it if the domain is parked.
- Three new local installers found in the top 10 for "intercom installation NYC apartment building" were added to the list (now 15, the cap): parkercustomsecurity.com (#3), dtv-installations.com (#7), intercomrepairny.com (#8). Their sitemaps were not pulled this run; next run takes their baseline (`baseline_pending`).
- jacobintercom.com's sitemap has no lastmod dates, so its pages can only be diffed by URL (new/removed), never "changed".
- Depth was checked on 2 competitor pages only (Impera door buzzer repair NYC, Impera building intercom installation NYC) to keep Firecrawl lean. The other COVERED matches were compared by lastmod only.
- Google autocomplete / People Also Ask were not pulled; Search Console impressions were enough to rank the gaps.

**Baseline:** 2,330 competitor URLs across 11 sitemaps (product, tag, category, attachment and login URLs skipped).
**New or changed in the last 7 days (Nov 17–24):** 58 pages from 3 competitors: Impera Security 31, Vertex Security 23, EZ Switch 4. The other 8 had nothing new this week (Total Security, Security Camera NY, Sabre, ASM, NYC Intercom, UA Security, Rolo; Jacob Intercom's sitemap has no dates, so it can't be read for changes).
**Seed check (Nov 24 note):** verified. Impera published 11 brand-installer pages Nov 16–18 (Comelit, ButterflyMX, Aiphone, 2N, Akuvox, DoorBird, Swiftlane, Siedle, UniFi on Nov 16, Brivo Nov 17, Avigilon Alta Nov 18) and audience pages co-op/condo security and property management security (Nov 18) plus apartment buildings (Nov 16). Vertex refreshed its ButterflyMX and Comelit dealer pages Nov 20.

### Gaps

| Date | Competitor URL | Their lastmod | Intent | Suggested page / slug | Demand evidence (GSC 90d) | Priority | Status |
|---|---|---|---|---|---|---|---|
| 2026-11-24 | imperasecurity.com/co-op-condo-security · jacobintercom.com/co-op-condo-intercom/ | 2026-11-18 · n/a | Audience: co-op and condo boards (intercom, access, cameras) | Audience hub `/co-op-security-systems-nyc` (intercom-led; condo list pending) | "coop intercom system nyc" 159 @8.1 · "coop intercom system" 141 @12.8 · "condo intercom system nyc" 111 @17.3 · "condo access control nyc" 49 @8.4 | P1 (highest demand gap) | QUEUED Nov 25 at the FRONT of the queue, HELD: keywords/co-op-security-systems.md is PARTIAL (Anwar's upload cut off); build the moment the full list arrives |
| 2026-11-24 | imperasecurity.com/comelit-installer-nyc · vertexsecurity.com/brand/comelit-dealer/ · jacobintercom.com/brands/comelit/ | 2026-11-16 · 2026-11-20 · n/a | Brand: Comelit intercom install/upgrade | `/comelit-intercom-installation-nyc` | "comelit intercom nyc" 129 @40.8 · "comelit video intercom nyc" 28 @30.2 · "comelit intercom system nyc" 13 @28.1 | P1 | QUEUED Nov 25 (keywords/comelit.md; 16 lines in PAGE-QUEUE.md) |
| 2026-11-24 | imperasecurity.com/butterflymx-installer-nyc · vertexsecurity.com/brand/butterflymx-dealer/ · jacobintercom.com/brands/butterflymx/ | 2026-11-16 · 2026-11-20 · n/a | Brand: ButterflyMX installer | `/butterflymx-installation-nyc` (link to /akuvox-vs-butterflymx) | "butterflymx installer nyc" 39 @9.5 · "butterflymx repair" 24 @37.7 · "butterflymx repairs near me" 4 @6 | P1 | QUEUED Nov 24 (keywords/butterflymx.md; 16 lines in PAGE-QUEUE.md, NYC hub rebuilt in place) |
| 2026-11-24 | imperasecurity.com/akuvox-installer-nyc · jacobintercom.com/brands/akuvox/ | 2026-11-16 · n/a | Brand: Akuvox intercom (we install it) | `/akuvox-intercom-nyc` (link to /akuvox-vs-butterflymx) | "akuvox intercom installation nyc" 32 @15.8 | P1 | QUEUED Nov 25 (keywords/akuvox.md; 16 lines in PAGE-QUEUE.md) |
| 2026-11-24 | imperasecurity.com/aiphone-intercom-installer-nyc · jacobintercom.com/brands/aiphone/ | 2026-11-16 · n/a | Brand: Aiphone install (repair intent also shows) | `/aiphone-intercom-nyc` (one page per area, repair-led) | "aiphone intercom repair" 26 @28.0 · "aiphone repair nyc" 17 @6.2 · "aiphone installer orange county" 11 @19.7 | P1 | QUEUED Nov 25 (keywords/aiphone.md drafted at Anwar's request; 16 lines in PAGE-QUEUE.md) |
| 2026-11-24 | imperasecurity.com/property-management-security · jacobintercom.com/property-managers/ · jacobintercom.com/superintendents/ | 2026-11-18 · n/a | Audience: property managers / supers (also the cold-email target) | Audience hub `/property-management-security-nyc` | Thin so far ("bronx locksmith for property managers" 4 @10.5); money audience | P1 | NEEDS KEYWORD LIST |
| 2026-11-24 | imperasecurity.com/doorbird-installer-nyc · jacobintercom.com/brands/doorbird/ | 2026-11-16 · n/a | Brand: DoorBird (special-order brand we install) | `/doorbird-intercom-nyc` (link to /doorbird-vs-2n) | "doorbird intercom repair" 25 @34.4 · "doorbird intercom system repair" 10 @28 | P2 | QUEUED Nov 25, HELD: keywords/doorbird.md is PARTIAL (Anwar's upload cut off); build once the full list arrives |
| 2026-11-24 | imperasecurity.com/brivo-installer-nyc · vertexsecurity.com/brand/brivo-dealer-nyc/ | 2026-11-17 · 2026-02-25 | Brand: Brivo access control | `/brivo-access-control-nyc` | "brivo access control installer nyc" 13 @12.8 · "brivo authorized dealers" 4 @9 | P2 | QUEUED Nov 25, HELD: keywords/brivo.md is PARTIAL (Anwar's upload cut off); build once the full list arrives |
| 2026-11-24 | uasecurity.com/blog1/2026/08/25/nyc-intercom-law-apartment-building-requirements/ · jacobintercom.com/guides/nyc-landlord-intercom-requirements/ · imperasecurity.com/blog/nyc-building-security-requirements-landlords | 2026-09-14 · n/a · 2026-11-20 | Guide: NYC intercom law, Multiple Dwelling Law §50-a | Guide `/nyc-intercom-law-multiple-dwelling-law-50-a` | No query yet; three competitors and AI answers cite it | P2 | NEEDS KEYWORD LIST |
| 2026-11-24 | imperasecurity.com/blog/security-camera-laws-nyc-property-owners · vertexsecurity.com/our-blog/security-camera-laws/ | 2026-11-21 · 2026-10-19 | Guide: security camera laws for NYC property owners | Guide `/security-camera-laws-nyc` | None yet | P2 | NEEDS KEYWORD LIST |
| 2026-11-24 | roloelectronics.com/blog/verizon-copper-landline-retirement-alarm-systems | 2026-11-09 | Guide: Verizon copper landline retirement and alarm communicators | Guide `/verizon-copper-landline-retirement-alarm-systems-ny` | None yet | P2 | NEEDS KEYWORD LIST |
| 2026-11-24 | uasecurity.com/blog1/2026/09/10/how-to-check-if-dvr-is-recording/ · uasecurity.com/dvr-nvr-troubleshooting-nyc.htm | 2026-10-26 · 2026-10-11 | Troubleshooting guide: is my DVR/NVR recording | Guide `/how-to-check-if-dvr-is-recording` (link to dvr-upgrade / nvr-installation, no DIY wiring) | "24hr recording camera" 1 · "cctv recording system" 1 (thin) | P2 | NEEDS KEYWORD LIST |
| 2026-11-25 | imperasecurity.com/ubiquiti-unifi-installer-nyc | 2026-11-16 | Brand: UniFi Access (door access; our UniFi camera silo already covers Protect) | `/unifi-access-control-nyc` | none yet | P3 | QUEUED Nov 25, HELD: keywords/unifi-access.md is PARTIAL (Anwar's upload cut off); build once the full list arrives |
| 2026-11-24 | imperasecurity.com/2n-installer-nyc · jacobintercom.com/brands/2n/ | 2026-11-16 · n/a | Brand: 2N | `/2n-intercom-installation-nyc` | "2n on elevators" 1 (thin) | P3 | QUEUED Nov 25, HELD: keywords/2n.md is PARTIAL (Anwar's upload cut off); build once the full list arrives |
| 2026-11-24 | imperasecurity.com/avigilon-alta-installer-nyc | 2026-11-18 | Brand: Avigilon Alta access/cameras | `/avigilon-intercom-nyc` (intercom only) | "avigilon dealer" 4 @1 · "avigilon camera(s)" 6 @6–10 | P3 | QUEUED Nov 25 (keywords/avigilon-intercom.md complete; 16 lines in PAGE-QUEUE.md, ahead of the held brands) |
| 2026-11-24 | imperasecurity.com/swiftlane-installer-nyc | 2026-11-16 | Brand: Swiftlane | `/swiftlane-access-control-nyc` | None | P3 | QUEUED Nov 25, HELD: keywords/swiftlane.md is PARTIAL (Anwar's upload cut off); build once the full list arrives |
| 2026-11-24 | imperasecurity.com/siedle-installer-nyc · jacobintercom.com/brands/siedle/ | 2026-11-16 · n/a | Brand: Siedle | `/siedle-intercom-nyc` | None | P3 | QUEUED Nov 25, HELD: keywords/siedle.md is PARTIAL (Anwar's upload cut off); build once the full list arrives |
| 2026-11-24 | jacobintercom.com/lee-dan-intercom-systems/ (+ IR-203/204/205, PK-543, wiring, troubleshooting, parts) | n/a | Brand: Lee Dan apartment intercom repair/replacement | `/lee-dan-intercom-repair-nyc` (repair page) | "lee dan intercom troubleshooting" 1 @11 | P3 | NEEDS KEYWORD LIST |
| 2026-11-24 | imperasecurity.com/blog/butterflymx-vs-2n-intercom-nyc | 2026-11-20 | Comparison: ButterflyMX vs 2N (§12.5) | `/butterflymx-vs-2n` | None; confirm demand before building | P3 | NEEDS KEYWORD LIST |
| 2026-11-24 | uasecurity.com/downloads/comelit-app-reconnect-guide.pdf | 2026-09-22 | Resource: Comelit app reconnect | Fold into the Comelit brand page + customer how-to video library, not its own page | None | P3 | Folded into Comelit pages (keywords/comelit.md) |
| 2026-11-24 | imperasecurity.com/blog/false-alarms-nyc-causes-and-fixes | 2026-11-21 | Blog: false alarms causes/fixes | Blog | "fire alarm false alarm putnam county ny" 28 @29.7 | P3 | NEEDS KEYWORD LIST |
| 2026-11-24 | imperasecurity.com/blog/intercom-upgrade-unitone-butterflymx-nyc | 2026-11-20 | Blog: upgrading an old (Unitone) system | Blog | None | P3 | NEEDS KEYWORD LIST |
| 2026-11-24 | jacobintercom.com/intercom-maintenance-contract/ | n/a | Service: intercom maintenance contract | Blog or section on intercom repair pages | None for intercom (fire alarm maintenance contract queries exist, separate service) | P3 | NEEDS KEYWORD LIST |
| 2026-11-24 | vertexsecurity.com/our-blog/what-is-a-fire-alarm-interlock/ | 2026-11-18 | Blog: fire alarm interlocks | Blog (fire alarm list exists: keywords/fire-alarm-installation.md) | None | P3 | Held: no demand yet, not queued |
| 2026-11-24 | vertexsecurity.com/our-blog/the-nyc-security-compliance-checklist/ | 2026-11-18 | Blog: NYC security compliance checklist | Blog | None | P3 | NEEDS KEYWORD LIST |
| 2026-11-24 | vertexsecurity.com/our-blog/how-to-place-office-security-cameras/ · /how-to-choose-between-2-8mm-4mm-8mm-and-12mm-lenses/ · /power-over-ethernet/ | 2026-11-23 · 2026-11-11 · 2026-11-11 | Blogs: office camera placement, lens choice, PoE | Blogs | None | P3 | NEEDS KEYWORD LIST |
| 2026-11-24 | ezswitchli.com: video intercoms + existing access control (11-20), wired vs wireless cameras (11-19), alarm loses cellular/internet (11-18), monitoring detects equipment failure (11-17) | 2026-11-17 – 11-20 | Blogs | Blogs | None | P3 | NEEDS KEYWORD LIST |

### Matched as COVERED (no new page; would compete with ours)

- Impera /ubiquiti-unifi-installer-nyc (11-16) → our /ubiquiti-camera-installation-nyc (+31 area pages).
- Impera /door-buzzer-repair-nyc (11-16) → our /door-buzzer-repair-nyc. Theirs is newer. Decay candidate.
- Impera /building-intercom-installation-nyc, /video-intercom-systems-nyc, /security-systems/intercom (11-16/21) → our /intercom-installation-nyc. Theirs is newer. Decay candidate.
- Impera /intercom-repair, blog /intercom-replacement-nyc, Jacob /intercom-replacement/ → our /intercom-repair-nyc (refreshed Nov 23 by the decay task; "intercom replacement nyc" 296 @25.0 is already tracked there).
- Impera blog /intercom-installation-cost-nyc (11-21), Jacob cost guides → we already show at 4.0 for "intercom installation cost nyc" (89 impr). Don't build a competing cost page.
- Impera /security-camera-repair-{brooklyn,manhattan,queens} (11-14) → our /security-camera-repair-* pages (sitemap lastmod Apr 27). Decay candidate.
- Impera /industries/apartment-buildings (11-16) → our /apartment-building-security-camera-installation-* (cameras only).
- Vertex /security-systems-long-island/, /-nassau-county/, /-suffolk-county/, /security-systems-long-island/{intercom,access-control,security-camera-installation}/, /access-control-suffolk-county/ (11-17 to 11-20) → our Long Island / Nassau / Suffolk service hubs (sitemap lastmod May 3). Decay candidates.
- Vertex blog /school-security-systems-requirements-nyc-guide/ → our /school-security-camera-installation-* pages.
- Hanwha and Axis brand dealer pages (Vertex, Feb) → our hanwha-camera-installation-* and axis price pages; not changed this week.

### Skipped (out of scope)

- Impera /locksmith-services, /locksmith-services-brooklyn, -manhattan (11-21): lock work isn't our scope.
- Vertex enterprise brand pages (Genetec, Lenel S2, Salto, Milestone, Genea): enterprise VMS/access platforms we don't install or price.
- Vertex /industries/{offices,business-and-commercial,residential-buildings,hospitals-and-health-institutions}, /process/, /testimonials/, /about/ (11-20 to 11-24): industry and company pages, not service intents. Revisit if Anwar wants industry pages.
- Impera /homepage, /about, /brands, /blog, /contact, /service-areas: index pages.
