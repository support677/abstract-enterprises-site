==============================================================
FULL SITE DEPLOY — site-rebuild-66
Deploy Date: July 17, 2026
Previous deployment: site-rebuild-65 (delivered as site-rebuild-65-complete.zip)
==============================================================

SITE-REBUILD-66 — SURGICAL WARRANTY + REVIEWCOUNT CORRECTION
(8 warehouse pages + this readme; source = site-rebuild-65-complete)

FIX 1 — LAST OLD WARRANTY DURATIONS REMOVED:
- Suffolk County Included Standard: "twelve months of parts warranty"
  -> "three-year warranty on AESS-supplied products (exclusions apply;
  see FAQ)."
- Westchester County: visible warranty FAQ answer replaced with the
  exact standard three-year policy paragraph (AESS-supplied products,
  full exclusion list, $195/hr + three-hour minimum $585); FAQPage
  schema regenerated from the visible FAQ — answer matches exactly;
  Included Standard reference updated to the same three-year line.
- Audit across all 16 pages: zero warranty references using one year /
  one-year / 1 year / 1-year / twelve months / twelve-month /
  12 months / 12-month. The single remaining "within twelve months"
  phrase (Rockland) is the unrelated access-control cross-sell stat
  and is intentionally preserved.

FIX 2 — REVIEWCOUNT 178 -> 201:
- AggregateRating reviewCount corrected to "201" on Bronx, Hudson
  Valley, Manhattan, Queens and Westchester County (ratingValue stays
  4.7). Stale 4.7/178 changelog-comment references corrected to
  4.7/201 on those pages plus Orange County and Rockland County.
- Final sweep: zero occurrences of 178 across all 16 pages; exactly
  one AggregateRating reviewCount "201" per page; visible badge
  remains "4.7 / 201 Google Reviews".

PRESERVED (verified byte-identical or count-identical vs 65): hero
forms and lower forms (32 total), Web3Forms keys and hidden values,
AJAX, hero/mobile layout, all 192 photographs with filenames, alts,
titles, figcaptions and ImageObject entries, no-crop CSS (zero
object-fit:cover), logo, favicons, phone routing, sitemap (1,838),
_redirects, navigation. All 7 JSON-LD blocks parse on every page;
FAQ visible == schema on all 16; zero broken internal links.
==============================================================

SITE-REBUILD-65 — HERO QUOTE FORM + WARRANTY STANDARDIZATION
(16 warehouse pages + this readme only; source = site-rebuild-64)

REPAIR 1 — HERO FORM ON ALL 16 PAGES:
- Hero rebuilt as a responsive two-column grid (>=861px):
  left = eyebrow, H1, intro copy, CTA buttons, trust badges, hub link;
  right = existing hero photograph + compact "Get a Free Warehouse
  Security Quote" form card. Mobile (<=860px) stacks in the required
  order: heading/copy -> call/quote buttons -> hero form -> hero
  photograph -> trust badges (form ordered above photo via CSS order).
- Real form controls in every hero: Full Name*, Phone*, Email*,
  Warehouse Size* (select), Project Need* (select), Brief Project
  Details (textarea), required contact-consent checkbox linking to
  /privacy-policy.html (extensionless /privacy-policy has no 200
  rewrite in _redirects, which is out of scope, so the link targets
  the file directly). Two-column fields on desktop, one column mobile.
- Page-specific hidden fields verified on all 16: access_key
  (88890030-1770-483e-a622-0e054d8e14b1), service, target_area,
  landing_page (== canonical path), form_location=Hero,
  subject = "Warehouse Security Camera Quote - [AREA] - Hero",
  from_name = AESS Warehouse Website, botcheck honeypot.
- Page-specific IDs (wh-hero-[slug]-*); every label references its ID;
  zero duplicate IDs page-wide.
- AJAX via fetch + FormData: accessible status line
  (role="status", aria-live="polite"), submit button disabled during
  send and restored on failure; native action/method preserved so the
  form still submits without JavaScript; access key lives only in the
  hidden input.
- Each page now carries exactly 2 forms (hero + existing detailed
  form): 32 forms across the silo.
- Hero photo in-column CSS: width:100%, height:auto,
  object-fit:contain (no crop, no stretch); the 4 portrait heroes
  (Dutchess, Hudson Valley, Queens, Staten Island) capped at 340px
  wide and centered. Zero object-fit:cover site-silo-wide.

REPAIR 3 — WARRANTY STANDARDIZED (71 old refs -> 0):
- Every one-year/1-year reference removed across trust bullets,
  pricing/quote-includes lists, DIY comparison tables, stack table,
  Included Standard features, CTA copy, HowTo step 6 (visible +
  HowTo schema), and FAQ answers.
- Standard policy now used: three-year warranty on AESS-supplied
  products for normal wear and tear; excludes existing/customer
  wiring, customer-supplied equipment, lightning/acts of God, power
  outages or surges, physical damage or unplugging,
  internet/router/phone changes, and post-completion camera
  readjustments; $195/hr with a three-hour minimum ($585) afterward.
  No claim that labor, existing wiring or customer equipment is
  covered.
- FAQPage JSON-LD regenerated from the visible FAQ on all 16 pages;
  visible answers and schema answers match exactly. Final sweep:
  zero one-year/1-year/1yr occurrences on all 16 pages.

QA (all 16 pages): 2 forms/page (32 total), hero form present inside
<section class="hero"> with required fields + consent + privacy link,
page-specific hidden values verified against canonicals, no duplicate
IDs, Web3Forms key in both forms, AJAX success/error + button-state
logic present, 12 photographs/page, 192 unique sources / alts /
titles / figcaptions / ImageObjects (byte-identical to 64), 1 eager
hero + 11 lazy per page, og/twitter/Service images unchanged, zero
object-fit:cover, zero broken internal links, phone routing and
4.7/201 and NYS license counts unchanged vs 64, 7 JSON-LD blocks
parse per page, strict parser balance, 28 H2 per page, sitemap valid
at 1,838 URLs.
==============================================================

SITE-REBUILD-64 — HERO IMAGE GEOMETRY REFINEMENT (CSS-ONLY)
- Re-inspection with a rendering engine + pixel measurement showed the
  63 hero rule (width:100% + fixed clamp height + contain) painted the
  photo inside a full-wrap 1020px navy element: landscape heroes sat
  between ~195px navy bars per side; the 4 portrait-hero pages painted
  a ~336px photo inside a 1020px navy field — violating the "small
  amount of navy" acceptance line.
- New hero rule (all 16 pages): element hugs the contained photo and
  centers itself. .wimg-hero{margin:20px auto 0;text-align:center};
  .wimg-hero img{height:clamp(260px,32vw,420px);width:auto;
  max-width:100%;object-fit:contain;object-position:center;
  background:#0B1F3A;border-radius:12px;display:inline-block}.
  Mobile (<=860px): height:auto, width:100%, contain. clamp heights,
  contain, navy background and radius all preserved; object-fit:cover
  still absent everywhere; entire hero photo always visible.
- GEOMETRY QA (deterministic, per final CSS): all 576 placements
  (16 pages x 1440/1024/390 x 12 figures) verified — painted aspect ==
  intrinsic within 0.5% (no stretch), photo fully inside its element
  (no crop), portrait bodies <=720px centered, hero internal navy 0px
  (element hugs photo), captions inside figures directly below images.
  Real-photo contact sheets composited for all 16 heroes at each
  viewport.
- IMAGE SEO: every <img> tag, figcaption and ImageObject @graph
  re-verified byte-identical. Parser balance + JSON-LD validity pass
  on all 16 pages.
- Scope: 16 warehouse pages only; nothing else touched.
==============================================================

SITE-REBUILD-63 — WAREHOUSE IMAGE CROPPING CORRECTION (CSS-ONLY)
- Root cause fixed: .wimg img max-height:620px + object-fit:cover was
  cropping portrait/vertical photographs. Source files were correct and
  are untouched.
- New body rules: .wimg img -> width:100%, height:auto, max-height:none,
  object-fit:contain, object-position:center (no crop possible).
  Orientation classes added from real dimensions:
  portrait (1024x1536, 1122x1402) -> .wimg-portrait (max-width:720px,
  centered); landscape (1536x1024, 1402x1122) -> .wimg-landscape.
  176 body figures classified: 44 portrait / 132 landscape.
- Hero rule: .wimg-hero img -> height:clamp(260px,32vw,420px),
  object-fit:contain, navy #0B1F3A letterbox, border-radius 12px;
  mobile (max-width:860px): height:auto, object-fit:contain. Full hero
  photo always visible on all 16 rotations (4 portrait heroes included).
- IMAGE SEO PRESERVED BYTE-FOR-BYTE: every <img> tag, filename, alt,
  title, width/height, loading attrs, figcaption, and the 12-entry
  ImageObject @graph verified identical pre/post on all 16 pages.
  No photograph regenerated, renamed, cropped, resized or recompressed.
- QA: rendered-size math verified at 1440/1024/390 (full subject visible,
  true aspect, portrait centered <=720px, hero letterboxed on navy);
  structural renders pass (captions directly below figures, 12 images
  per page, no horizontal overflow introduced — pre/post renders
  byte-equal in width at all three viewports); strict parser balance
  and JSON-LD validity re-verified on all 16 pages.
- Scope: 16 warehouse pages only. Sitemap (1,838), _redirects (871),
  navigation, phones, ratings, copy — untouched.
==============================================================

SITE-REBUILD-62 — WAREHOUSE BRANDING: LOGO + FAVICON CLEANUP
- images/logo.png cleaned (same design, no redesign): converted to RGBA,
  exterior white removed by edge-connected flood fill only; all interior
  whites preserved (ABSTRACT lettering, camera body, shield details);
  edge halo decontaminated; subtle light-blue outer edge added for
  visibility on navy; content-cropped with transparent padding; verified
  on navy and white composites; corners alpha 0; high-res master (500px).
- Warehouse header logo: height 46 -> 54 desktop, 38 -> 42 mobile
  (max-width:860px), width auto, vertically centered; footer logo
  unchanged at 52. Applied on all 16 warehouse pages.
- Favicon set REPLACED (old set squeezed the full detailed logo into
  16x16). New simplified symbol for small sizes: navy #0B1F3A background,
  bold white "A" with bright-blue crossbar accent + blue inset ring,
  recognizable at 16x16. favicon.ico now contains 16/32/48.
  favicon-192.png and apple-touch-icon.png (180x180) carry the cleaned
  full shield on navy with safe padding, wording readable.
- Favicon declarations added to the head of all 16 warehouse pages
  (icon x-icon, png 32x32, png 16x16, apple-touch-icon 180x180,
  theme-color #0B1F3A) — exactly once each, no duplicates; NYC's old
  theme-color (#0e1b2a) replaced.
- REPAIR: NYC hub off-page checklist comment was missing its closing
  "-->" since the ulster-session edit (comment swallowed </body></html>
  in strict parsing; browsers unaffected). Terminator restored; all 16
  pages pass strict parser balance.
- UNCHANGED: page copy, phone routing, ratings, photographs and image
  SEO, sitemap (1,838), _redirects (871), navigation, schemas.
  File count unchanged (logo + 5 favicon files replaced in place).
==============================================================

SITE-REBUILD-61 — ULSTER COUNTY WAREHOUSE PAGE PUBLISHED — WAREHOUSE SILO COMPLETE
- New page: /warehouse-security-camera-installation-ulster-county (Blueprint v2.1, ~11,700 words, 28 H2, 12 FAQ synced to FAQPage schema, HowTo synced, 7 JSON-LD schemas incl. 12-entry ImageObject @graph). FINAL page of the 16-page warehouse silo.
- Bronx GBP routing: 460 E Fordham Rd, (845) 640-3835 x11, reviewCount 201, HV pricing band, 3-yr AESS product warranty w/ exclusions, $195/hr + 3-hr min ($585), Ulster County Sheriff refs.
- Angles: three Thruway exits (18 New Paltz / 19 Kingston / 20 Saugerties), Town of Ulster iPark 87 / Route 9W commercial belt, Kingston/Rondout trade core, Saugerties Kings Highway corridor, Rondout Valley Route 209 farm belt to Ellenville/Napanoch, Marlboro-Milton fruit belt (cold storage, packing houses, compressor-theft coverage), OCM cannabis compliance (real county operators).
- 12-photo image layer (rotation idx 15, hero = warehouse-video-surveillance-systems), 12 new ulster-county-ny webps, fingerprint-audited 12/12 to supplied sources, excluded photo absent.
- Similarity (5-shingle Jaccard, figures excluded): vs Dutchess 17.4%, Putnam 14.9%, Orange 13.2%, Rockland 12.1%, Westchester 10.3% — under floor with zero dedup passes (all narrative sections written fresh at build).
- Integration: Ulster link live in all 15 sibling silo footers; sitemap 1,838 URLs (lastmod 2026-07-17); _redirects 871 lines (+200 rewrite); mega-nav 16 warehouse keys; NYC hub comment updated (SILO COMPLETE 16/16).
- SITEMAP REPAIR: an insert-offset bug corrupted the </urlset> tail during this session; tail truncated after the putnam entry, dutchess + ulster entries rebuilt clean, ET-validated at 1,838 URLs. (site-rebuild-60's shipped sitemap was valid; the corruption existed only in-session.)
- Warehouse silo: 16/16 pages COMPLETE.


THIS IS A COMPLETE SITE DEPLOY.
Drop this entire zip into Netlify as a full replacement.

2,457 total files
1,847 HTML files
1,838 sitemap URLs

WHAT CHANGED vs PREVIOUS DEPLOY (site-rebuild-60, final version 60-2):

ULSTER COUNTY WAREHOUSE PAGE — one new HTML page plus its 12
WebP assets (ulster-county-ny family) and the sitewide
integration edits (15 sibling silo footers repointed, sitemap,
_redirects, mega-nav, NYC hub comment). FINAL PAGE — WAREHOUSE
SILO COMPLETE AT 16/16. Everything else carries forward from
site-rebuild-60 unchanged, including
the corrected loading-dock source imagery (technicians, van,
Hikvision boxes and cameras staged on the dock, 1402x1122) and
the full 12-supplied-photograph layer on every warehouse page.

WAREHOUSE SILO PAGES (16):
  warehouse-security-camera-installation-nyc.html
  warehouse-security-camera-installation-long-island.html
  warehouse-security-camera-installation-hudson-valley.html
  warehouse-security-camera-installation-manhattan.html
  warehouse-security-camera-installation-brooklyn.html
  warehouse-security-camera-installation-queens.html
  warehouse-security-camera-installation-bronx.html
  warehouse-security-camera-installation-staten-island.html
  warehouse-security-camera-installation-nassau-county.html
  warehouse-security-camera-installation-suffolk-county.html
  warehouse-security-camera-installation-westchester-county.html
  warehouse-security-camera-installation-rockland-county.html
  warehouse-security-camera-installation-orange-county.html
  warehouse-security-camera-installation-putnam-county.html
  warehouse-security-camera-installation-dutchess-county.html
  warehouse-security-camera-installation-ulster-county.html  (NEW — FINAL PAGE)

Per page:
  - 1 of the 12 photographs inside the hero section
    (loading="eager", fetchpriority="high", decoding="async")
  - 11 photographs distributed through page sections
    (loading="lazy", decoding="async"), never grouped as a gallery
  - Hero photo and body order ROTATE per page (no duplicated layout)
  - Each photo targets one of 12 unique keywords; keyword + exact
    area applied to: WebP filename, alt, title, visible figcaption,
    ImageObject name / caption / description / contentUrl
  - JSON-LD @graph with 12 ImageObject entries (absolute URLs,
    width/height, representativeOfPage on the hero)
  - Service schema carries the hero image URL
  - og:image and twitter:image set to the page's hero WebP
    (absolute production URL); og:image:alt matched to hero alt
  - Accurate width/height on all images + responsive .wimg CSS with
    object-fit (no stretch, no layout shift)

IMAGE ASSETS (192 WebP = 12 keywords x 16 areas):
  For each area slug [new-york-city, long-island-ny, hudson-valley-ny, manhattan-ny, brooklyn-ny, queens-ny, bronx-ny, staten-island-ny, nassau-county-ny, suffolk-county-ny, westchester-county-ny, rockland-county-ny, orange-county-ny, putnam-county-ny, dutchess-county-ny, ulster-county-ny]:
    warehouse-security-camera-installation-[area].webp
    commercial-security-camera-installation-[area].webp
    warehouse-cctv-installation-[area].webp
    industrial-surveillance-system-installation-[area].webp
    warehouse-video-surveillance-systems-[area].webp
    commercial-cctv-camera-installer-[area].webp
    warehouse-access-control-installation-[area].webp
    warehouse-alarm-system-installation-[area].webp
    loading-dock-security-camera-installation-[area].webp
    warehouse-security-system-company-[area].webp
    industrial-security-camera-installer-[area].webp
    warehouse-cctv-system-installation-[area].webp

PHONE ROUTING VERIFIED (Westchester / Rockland / Orange / Putnam / Dutchess / Ulster):
  (845) 640-3835 + tel:+18456403835 x11 each; WhatsApp-only
  (718) 679-0359 / wa.me/17186790359; zero 347 occurrences.

PRESERVED UNTOUCHED: all existing page copy, H1/H2 structure, pricing,
three-year warranty + exclusions, $195/hr + $585 minimum, FAQs,
existing JSON-LD, ratings, breadcrumbs, internal links, forms,
navigation on non-warehouse pages.

AUTOMATED IMAGE QA: all 16 warehouse pages PASS (12 visible photos,
1 hero, 11 distributed/lazy, 12 unique keywords, every one of the
12 photos serves as hero on at least one page, area in every
filename/alt/title/figcaption, 12 ImageObjects, og/twitter = hero,
all files present, no duplicate filenames per page, correct loading
attrs, phones OK, fingerprint match to supplied sources, excluded
photo absent).

WAREHOUSE SILO STATUS: COMPLETE — 16/16 PAGES LIVE
  NYC hub + 5 boroughs + LI hub + Nassau + Suffolk + HV hub + all 6 HV counties
  (Westchester, Rockland, Orange, Putnam, Dutchess, Ulster).
  Silo-Completion Checklist PASS: all 16 URLs in sitemap.xml, all 16 have
  200 rewrites in _redirects (no stale 301s), all 16 registered in
  js/mega-nav.js, all 16 silo footers verified (15 links + self, 0 grey spans).

POST-DEPLOY CHECKLIST:
1. Drag this zip into Netlify; wait for deploy to complete
2. Spot-check the new Ulster County URL + 2 sibling warehouse URLs:
   hero photo + body photos render
   /warehouse-security-camera-installation-ulster-county
3. Validate one page in Google Rich Results test (ImageObject)
4. GSC: submit /warehouse-security-camera-installation-ulster-county
==============================================================

==============================================================
SITE-REBUILD-67 — July 17, 2026
==============================================================
NEW: /school-security-camera-installation-nyc (School Security
  Camera Installation silo — NYC hub, first page of 16).
  11 WebP photos (1 hero eager + 10 lazy), figcaptions,
  ImageObject schema x11 (hero representativeOfPage), og/twitter
  hero wiring, 2 Web3Forms (Hero + Detail) with consent + AJAX,
  v66 logo/favicon branding, silo footer shows all 16 areas but
  ONLY NYC is clickable — 15 future pages render as grey spans
  until built.
SITEWIDE: rating corrected to 4.7 / 201 Google Reviews (zero
  4.6/190 remain, visible + schema). Warranty language migrated
  to 3-year AESS-supplied-products terms (zero one-year / 1-year /
  1-yr / twelve-month / 12-month warranty references remain;
  $195/hr 3-hr-min post-warranty service preserved).
REGISTERED: sitemap.xml (0.9/weekly), _redirects 200 rewrite,
  js/mega-nav.js (schoolcameras — node --check PASS).
POST-DEPLOY:
1. Drag zip into Netlify; wait for deploy
2. Spot-check /school-security-camera-installation-nyc:
   hero photo eager-loads, 10 body photos lazy-load, both forms
   submit, silo footer greys except NYC
3. Rich Results test: FAQPage + ImageObject on the school page
4. GSC: submit /school-security-camera-installation-nyc
==============================================================

BUILD ID: site-rebuild-67 (repackaged as site-rebuild-67-fixed.zip
after transfer truncation of the first archive — content identical,
max compression). THIS IS A COMPLETE FULL-SITE DEPLOYMENT ZIP.
FINAL COUNTS: 2,469 files | 1,848 HTML | 1,839 sitemap URLs |
872 _redirects rules. School page ships with 11 WebP images
(1 hero eager/high-priority + 10 lazy), 11 ImageObject entries,
og/twitter/Service hero wiring, 2 consent-gated AJAX Web3Forms,
sitemap + 200 rewrite + mega-nav registration.
==============================================================

--------------------------------------------------------------
SITE-REBUILD-67-FINAL — AJAX repair (school page only)
--------------------------------------------------------------
The two .js-ajax forms previously declared AJAX but shipped
without a handler (native POST only). A shared handler is now
inline directly before </body> on
school-security-camera-installation-nyc.html:
preventDefault + checkValidity/reportValidity, submit button
disabled while sending and re-enabled after, fetch POST of
new FormData(form) to form.action with Accept: application/json,
success/error announced in each form's .fmsg (role="status",
aria-live="polite", .ok/.err classes), form reset on success
only. action/method preserved so native Web3Forms submission
still works with JavaScript disabled; access key stays in the
hidden field only — not duplicated in JS. No other file changed.
==============================================================

==============================================================
SITE-REBUILD-68 - July 17, 2026
==============================================================
NEW: /school-security-camera-installation-long-island (School
  silo 2/16 - Long Island hub). Full blueprint: 28 H2, ~10.0K
  words, 11 LI-named WebP photos (1 hero eager + 10 lazy,
  representative-scene figcaptions), 11 ImageObjects, og/twitter/
  Service hero wiring, 2 consent-gated AJAX Web3Forms (target_area
  Long Island), 4.7/201, 3-year AESS-supplied warranty terms,
  Nassau/Suffolk content: DRVC 35+9 schools, Five Towns yeshiva
  corridor, Nassau BOCES police-feed context, Alyssa's Law, salt-
  air coastal spec, x1.20 LI pricing band, Nassau 8.625%/Suffolk
  8.75% tax. Silo footer: NYC live, LI current, 14 grey spans.
CROSS-LINKS: NYC school page Long Island spans flipped to live
  links (silo footer + coverage prose).
REGISTERED: sitemap 1,840 URLs (0.9/weekly), _redirects 873 rules,
  mega-nav schoolcameras.longisland (node --check PASS).
COUNTS: 2,481 files | 1,849 HTML.
POST-DEPLOY: spot-check LI page hero + both forms; GSC submit
  /school-security-camera-installation-long-island.
==============================================================
SITE-REBUILD-68-FINAL: added full three-year warranty exclusions
paragraph under the LI school pricing tables (LI page only).
==============================================================
REGEN 2026-07-17T21:41 — fresh repackage; LI warranty paragraph verified at HTML line 537 pre-zip.
==============================================================

==============================================================
SITE-REBUILD-69 - July 17, 2026
==============================================================
NEW: /school-security-camera-installation-hudson-valley (school
  silo 3/16 - HV hub). 28 H2, ~9.6K words, 11 HV-named WebP
  (1 hero eager + 10 lazy), 11 ImageObjects, Bronx GBP routing:
  460 E Fordham Rd / (845) 640-3835, 347=0, Troy=0, NYPD=0.
  Six-county content: Archdiocese belt, Monsey/Kiryas Joel yeshiva
  communities + NPSE grant, Rockland stop-arm program, county
  sheriff routing (Rockland Sheriff, no county PD), winter/acreage
  spec, locked HV band $5,600-9,500 / $11,400-20,000 /
  $22,800-41,000+, county multipliers +25/30/35, taxes 8.375/
  8.125/8.0, full 3-year warranty exclusions paragraph, county
  selector on detail form.
CROSS-LINKS: HV spans flipped live on NYC + LI school pages.
REGISTERED: sitemap 1,841 | _redirects 874 | mega-nav
  schoolcameras.hudsonvalley (node --check PASS).
COUNTS: 2,493 files | 1,850 HTML.
POST-DEPLOY: GSC submit /school-security-camera-installation-hudson-valley.
==============================================================

==============================================================
SITE-REBUILD-70 - July 17, 2026
==============================================================
NEW: /school-security-camera-installation-manhattan (school silo
  4/16). 28 H2, ~9.5K words, 11 manhattan-ny WebP (1 hero eager +
  10 lazy), 11 ImageObjects, warehouse-manhattan routing: 347
  phone + Bronx GBP NAP (460 E Fordham Rd) in footer + schema,
  NYPD ok, Troy=0, 845=0. UES/Carnegie Hill + UWS + downtown +
  Harlem/Wash Heights school landscape, vertical-campus/riser/
  landmark-LPC/roof-deck/sidewalk-framing/co-op angles, x1.20
  pricing band, NYC tax 8.875%, full 3-year warranty exclusions
  paragraph, building-size/camera/timeline selectors on detail
  form.
CROSS-LINKS: Manhattan spans flipped live on NYC + LI + HV pages.
REGISTERED: sitemap 1,842 | _redirects 875 | mega-nav
  schoolcameras.manhattan (node --check PASS).
COUNTS: 2,505 files | 1,851 HTML.
POST-DEPLOY: GSC submit /school-security-camera-installation-manhattan.
==============================================================

==============================================================
SITE-REBUILD-71 - July 17, 2026
==============================================================
NEW: /school-security-camera-installation-brooklyn (school silo
  5/16). 28 H2, ~9.7K words, 11 brooklyn-ny WebP (1 hero eager +
  10 lazy), 11 ImageObjects, Brooklyn GBP routing: 347 phone +
  1282 Troy Ave NAP in footer + schema (@id #organization),
  NYPD ok, Fordham=0, 845=0. Yeshiva-capital content: Borough
  Park/Williamsburg/Crown Heights/Flatbush corridors, Diocese of
  Brooklyn (own diocese), Heights/Slope independents, charters,
  Al-Noor/Islamic academies, colleges. Multi-building/annex
  bridges, schoolyard/gate/bus-curb coverage, bus-fleet LPR +
  catalytic-theft angle, brownstone/landmark technique, base
  pricing $450-950/cam, NYC tax 8.875%, full warranty paragraph,
  campus-size/camera/timeline selectors on detail form.
CROSS-LINKS: Brooklyn spans flipped live on NYC + LI + HV +
  Manhattan pages.
REGISTERED: sitemap 1,843 | _redirects 876 | mega-nav
  schoolcameras.brooklyn (node --check PASS).
COUNTS: 2,517 files | 1,852 HTML.
POST-DEPLOY: GSC submit /school-security-camera-installation-brooklyn.
ORIGINALITY PASS (71-final): Brooklyn page rewritten from scratch in
  13 sections (terminology, entry stack, feature set, compliance,
  Reddit answers, ATP, PAA, AI Overview, DIY, nationals comparison,
  stats, 12 FAQs + regenerated FAQPage schema, pricing prose/cells,
  comparison table) plus Systems/Brands cards and both emergency
  blocks. Images, alts, captions, ImageObject schema, forms, AJAX,
  phone routing, rating, exact warranty paragraph, sitemap,
  _redirects, mega-nav, and all other pages byte-identical to v71.
  Verified 5-word-shingle Jaccard (headers/footers/nav/forms/
  figures/schema removed): vs NYC 0.97% | vs Long Island 3.53% |
  vs Hudson Valley 3.94% | vs Manhattan 5.80% - all under the 20%
  ceiling.
==============================================================

==============================================================
SITE-REBUILD-72 - July 17, 2026
==============================================================
NEW: /school-security-camera-installation-queens (school silo
  6/16). 28 H2, ~9.0K words, 11 queens-ny WebP (1 hero eager +
  10 lazy), 11 ImageObjects, warehouse-queens routing: 347 phone
  + Bronx GBP NAP (460 E Fordham Rd) in footer + schema, NYPD ok,
  Troy=0, 845=0. Written from scratch for originality; verified
  5-word-shingle Jaccard vs existing school pages: NYC 0.90% |
  LI 2.48% | HV 2.42% | Manhattan 2.76% | Brooklyn 4.93% - all
  under 20%. Content: Diocese-of-Brooklyn Catholic belt (St.
  Francis Prep largest in US), KGH/Forest Hills + Bukharian +
  Far Rockaway yeshiva map, St. Demetrios/Islamic/heritage
  schools, freestanding-campus design (parking lots, fields,
  modular annexes), Rockaway salt-air marine spec, converted-
  house electrical audits, x1.10 pricing $495-1,045/cam, NYC tax
  8.875%, exact warranty paragraph, campus-size selectors.
CROSS-LINKS: Queens spans flipped live on NYC + LI + HV +
  Manhattan + Brooklyn pages.
REGISTERED: sitemap 1,844 | _redirects 877 | mega-nav
  schoolcameras.queens (node --check PASS).
COUNTS: 2,529 files | 1,853 HTML.
POST-DEPLOY: GSC submit /school-security-camera-installation-queens.
==============================================================

==============================================================
SITE-REBUILD-73 - July 17, 2026
==============================================================
NEW: /school-security-camera-installation-bronx (school silo
  7/16 - office borough). 28 H2, ~9.1K words, 11 bronx-ny WebP
  (1 hero eager + 10 lazy), 11 ImageObjects, warehouse-bronx
  routing: 347 phone + Bronx GBP NAP (460 E Fordham Rd) in
  footer + schema, NYPD ok, Troy=0, 845=0. Written from scratch;
  verified 5-word-shingle Jaccard vs existing school pages:
  NYC 0.93% | LI 2.40% | HV 2.45% | Manhattan 2.75% | Brooklyn
  4.54% | Queens 7.84% - all under 20%. Content: 460 E Fordham
  Rd office-borough / fastest-response angle, Archdiocese belt
  (Hayes, Spellman, Fordham Prep, Mount St. Ursula 1855),
  Riverdale hill campuses + SAR + gatehouse/driveway LPR,
  KIPP-birthplace charter belt Mott Haven/Port Morris,
  el-corridor engineering (anti-flicker profiles + isolation
  mounts, Jerome/White Plains Rd/Westchester Ave), Sound-side
  marine spec (Throggs Neck/City Island), pre-war Concourse
  masonry, x1.10 pricing $495-1,045/cam + el/coastal uplift
  rows, NYC tax 8.875%, exact warranty paragraph, el-corridor
  field notes (parish school under the 6). FAQPage schema
  regenerated post-rewrite: 12=12, mismatch 0.
CROSS-LINKS: Bronx spans flipped live on NYC + LI + HV +
  Manhattan + Brooklyn + Queens pages.
REGISTERED: sitemap 1,845 | _redirects 878 | mega-nav
  schoolcameras.bronx (node --check PASS).
COUNTS: 2,541 files | 1,854 HTML.
POST-DEPLOY: GSC submit /school-security-camera-installation-bronx.
==============================================================

==============================================================
SITE-REBUILD-74 - July 18, 2026
==============================================================
NEW: /school-security-camera-installation-staten-island (school
  silo 8/16). 28 H2, ~9.5K words, 11 staten-island-ny WebP
  (1 hero eager + 10 lazy), 11 ImageObjects, warehouse-SI
  routing confirmed: 347 phone + Brooklyn GBP NAP (1282 Troy
  Ave) in footer + schema, 122nd Pct refs, Fordham=0, 845=0.
  Written from scratch; 5-word-shingle Jaccard vs all 7 school
  pages: NYC 0.71% | LI 2.08% | HV 1.95% | MN 2.15% | BK 3.25%
  | QNS 5.14% | BX 7.26% - all under 20%. Content: island-spec
  register - marine-tiered exteriors by shore proximity,
  flood-zone recorder elevation (BFE, 2012 memory), deer/turkey
  person-classification tuning, suburban lot/field perimeter
  design, hilltop driveway capture (Grymes/Todt), Archdiocese
  network (Farrell, St. Peter's, Notre Dame, Hill, Moore, Sea),
  SI Academy 1884, Yeshiva of SI, CSI 204 acres, x1.20 pricing
  $540-1,140/cam + marine/flood-elevation uplift rows, NYC tax
  8.875%, exact warranty paragraph, South Shore lot field notes
  (marine rebuild + recorder upstairs + deer tuning + converter
  -theft catch). FAQPage schema regenerated post-rewrite: 12=12
  mismatch 0.
CROSS-LINKS: Staten Island spans flipped live on NYC + LI + HV
  + Manhattan + Brooklyn + Queens + Bronx pages.
REGISTERED: sitemap 1,846 | _redirects 879 | mega-nav
  schoolcameras.statenisland (node --check PASS).
COUNTS: 2,553 files | 1,855 HTML.
POST-DEPLOY: GSC submit
  /school-security-camera-installation-staten-island.
==============================================================

==============================================================
SITE-REBUILD-75 - July 18, 2026
==============================================================
CSS REGRESSION FIX on all 8 school-silo pages (NYC, Brooklyn,
  Manhattan, Queens, Bronx, Staten Island, Long Island, Hudson
  Valley): main section:nth-of-type(even) was overriding
  .fieldnotes background, leaving light text on light ground.
  Added scoped override block (background #102a17 !important,
  h2 #ffd18a, body #e7f5ec, .sig #bcd9c6, figcaption #d7e8dc)
  immediately before </style>. .pgimg/.heroimg image rules
  untouched (object-fit:contain preserved, no cropping/heights
  added). Content, schema, forms, phones, sitemap, _redirects,
  mega-nav all unchanged from v74. Supersedes the interim
  site-rebuild-73-final.zip - this build includes both the CSS
  fix AND the Staten Island page.
COUNTS: 2,553 files | 1,855 HTML | 286+11 WebP | sitemap 1,846
  | _redirects 879.
==============================================================

==============================================================
SITE-REBUILD-76 - July 18, 2026
==============================================================
NEW: /school-security-camera-installation-nassau-county (school
  silo 9/16). 28 H2, ~9.6K words, 11 nassau-county-ny WebP
  (1 hero eager + 10 lazy), 11 ImageObjects, warehouse-nassau
  routing confirmed: 347 phone + Brooklyn GBP NAP (1282 Troy
  Ave), Nassau County Police refs, NYPD=0, 845=0, 516=0.
  Written from scratch; 5-word-shingle Jaccard vs all 8 school
  pages after two thinning passes: NYC 0.74% | LI 2.05% | HV
  1.92% | MN 2.13% | BK 2.59% | QNS 3.82% | BX 6.20% | SI
  7.93% - all under 20%. Content: expectations-county register
  - Diocese of Rockville Centre (Chaminade, Kellenberg, Sacred
  Heart, St. Mary's), Gold Coast estate campuses (Friends 1876,
  Portledge, Green Vale, LIU Post/NYIT), Five Towns + Great
  Neck day-school belt (HAFTR, HALB, HANC, NSHA) + NPSE, postwar
  15-20 exterior-door egress engineering (signature angle),
  Canada-geese detection tuning, South Shore marine + 2012
  flood-line recorder discipline, Viscardi/Mill Neck special-ed,
  x1.20 pricing $540-1,140/cam + egress + coastal uplift rows,
  Nassau tax 8.625%, exact warranty paragraph, 19-door field
  notes (Feb-break day school, door-tester catch to Fourth Pct).
  FAQPage schema regenerated post-thinning: 12=12 mismatch 0.
  Fieldnotes CSS override inherited from fixed LI head.
CROSS-LINKS: Nassau spans flipped live on all 8 prior school
  pages.
REGISTERED: sitemap 1,847 | _redirects 880 | mega-nav
  schoolcameras.nassau (node --check PASS).
COUNTS: 2,565 files | 1,856 HTML.
POST-DEPLOY: GSC submit
  /school-security-camera-installation-nassau-county.
==============================================================

==============================================================
SITE-REBUILD-77 - July 18, 2026
==============================================================
NEW: /school-security-camera-installation-suffolk-county
  (school silo 10/16). 28 H2, ~9.7K words, 11 suffolk-county-ny
  WebP (1 hero eager + 10 lazy), 11 ImageObjects,
  warehouse-suffolk routing confirmed: 347 phone + Brooklyn GBP
  NAP (1282 Troy Ave), Suffolk County Police refs, NYPD=0,
  845=0, 631=0. Written from scratch; 5-word-shingle Jaccard vs
  all 9 school pages, NO thinning pass needed: NYC 0.75% | LI
  1.94% | HV 1.84% | MN 1.99% | BK 2.34% | QNS 2.90% | BX 3.05%
  | SI 4.16% | Nassau 4.16% - all under 20%. Content:
  distance-honest working-county register - 90-mile Melville-to-
  Montauk framing, St. Anthony's/St. John the Baptist DRVC,
  Stony Brook School 1922 boarding, Knox/Ross/Harbor Country
  Day east end, MDQ Academy Brentwood, SBU + SCCC 3 campuses +
  St. Joseph's Patchogue, DDI special-ed, SCPD-vs-town-PD
  response framing, acreage/outbuilding coverage, deer-silenced
  detection, two-shore marine spec (Sound vs bay/ocean), 2012
  Great South Bay recorder elevation, seasonal-campus vacancy
  mode, x1.20 pricing $540-1,140/cam + extended-run/site-work +
  shore-package rows, Suffolk tax 8.625%, exact warranty
  paragraph, East End field notes (9-acre August job, wireless
  barn link, 1 a.m. pickup plate to town police). FAQ 12=12
  mismatch 0. Fieldnotes CSS override inherited.
CROSS-LINKS: Suffolk spans flipped live on all 9 prior school
  pages.
REGISTERED: sitemap 1,848 | _redirects 881 | mega-nav
  schoolcameras.suffolk (node --check PASS).
COUNTS: 2,577 files | 1,857 HTML.
POST-DEPLOY: GSC submit
  /school-security-camera-installation-suffolk-county.
==============================================================

==============================================================
SITE-REBUILD-78 - July 18, 2026
==============================================================
NEW: /school-security-camera-installation-westchester-county
  (school silo 11/16; first HV county). 28 H2, ~9.5K words, 11
  westchester-county-ny WebP (1 hero eager + 10 lazy), 11
  ImageObjects. HV routing per warehouse-westchester + school
  HV hub: 845 phone (845) 640-3835 + Bronx GBP NAP (460 E
  Fordham Rd, #organization-bronx, geo 40.8615/-73.8891),
  Westchester County Police + village PD refs, NYPD=0, 347=0,
  Troy=0. AJAX cloned from HV hub (845 fallback). Related-slug
  mix honored: -westchester-county for repair/nvr/dahua/lorex/
  hub, bare -westchester for dvr-upgrade + intercom-repair.
  Written from scratch; 5-word-shingle Jaccard vs all 10 school
  pages, NO thinning pass needed: NYC 0.70 | LI 1.81 | HV 2.30
  | MN 1.93 | BK 2.09 | QNS 2.82 | BX 3.84 | SI 4.92 | Nassau
  5.95 | Suffolk 6.61% - all under 20%. Content: terrain-
  literate register - ADNY (Iona Prep, Stepinac, Salesian,
  Ursuline, Kennedy Catholic, Holy Child, Maria Regina),
  Hackley 1899 hilltop + RCDS/Masters/Harvey, Keio + French-
  American/German international, Leffell + Westchester Day,
  Windward special-ed, Sarah Lawrence-to-SUNY-Purchase higher
  ed, hillside/terraced-campus engineering (signature angle),
  winter-rated exteriors +$40-70 uplift, deer/coyote/bear
  classification tuning, Sound Shore salt, neighbor lens-
  framing documentation, tournament-lot break-ins, x1.25
  pricing $565-1,190/cam, HV tier table (5,600-9,500 / 11,400-
  20,000 / 22,800-41,000+ / 45,000-120,000+ / 250K+ college),
  Westchester tax 8.375%, exact warranty paragraph, field notes
  (4-elevation river-town campus, wireless bridge, December
  dock/box-truck catch to village PD). FAQ 12=12 mismatch 0.
  Fieldnotes CSS override inherited from HV hub head.
CROSS-LINKS: Westchester spans flipped live on all 10 prior
  school pages.
REGISTERED: sitemap 1,849 | _redirects 882 | mega-nav
  schoolcameras.westchester (node --check PASS).
COUNTS: 2,589 files | 1,858 HTML.
POST-DEPLOY: GSC submit
  /school-security-camera-installation-westchester-county.
==============================================================

==============================================================
SITE-REBUILD-79 - July 18, 2026
==============================================================
NEW: /school-security-camera-installation-rockland-county
  (school silo 12/16). 28 H2, ~9.4K words, 11 rockland-county-ny
  WebP (1 hero eager + 10 lazy), 11 ImageObjects. HV routing per
  warehouse-rockland: 845 phone + Bronx GBP NAP
  (#organization-bronx), Rockland County SHERIFF refs (no county
  PD - locked rule honored, RocklandCountyPolice=0), NYPD=0,
  347=0, Troy=0. Slug mix honored: -rockland-county for
  repair/nvr/dahua/lorex/hub, bare -rockland for dvr-upgrade +
  intercom-repair. AJAX cloned from HV hub (845 fallback).
  Written from scratch; two thinning passes vs Westchester
  (13.95 -> 10.43 -> 8.74); final Jaccard vs all 11: NYC 0.57 |
  LI 1.51 | HV 1.92 | MN 1.64 | BK 1.75 | QNS 1.99 | BX 2.58 |
  SI 3.14 | Nassau 3.87 | Suffolk 4.02 | WC 8.74% - all under
  20%. FAQPage schema regenerated post-thinning: 12=12 mm0.
  Content: institutional-density register - Ramapo yeshiva/girls
  -school infrastructure at 3:1 private:public, New Square +
  Kaser village systems, Monsey building boom, 2019 Hanukkah
  attack security-investment context (factual, respectful),
  multi-building campus interlink design (signature angle), bus
  yard/fleet package (gate LPR + fuel-point zone), construction-
  phase cellular packages, dormitory-line law, luach-aware
  scheduling + Shabbos-unattended operation FAQ, NPSE-at-volume,
  Albertus Magnus + ADNY parishes, Green Meadow/Blue Rock, STAC/
  Dominican/RCC, Jawonio, Harriman-edge bear tuning, x1.25
  pricing $565-1,190/cam, HV tier table, Rockland tax 8.375%,
  exact warranty paragraph, field notes (3-building campus,
  wireless bridge + fiber, 2:04 a.m. diesel-siphon catch to
  Rockland County Sheriff's Office). Fieldnotes CSS inherited.
CROSS-LINKS: Rockland spans flipped live on all 11 prior school
  pages.
REGISTERED: sitemap 1,850 | _redirects 883 | mega-nav
  schoolcameras.rockland (node --check PASS).
COUNTS: 2,601 files | 1,859 HTML.
POST-DEPLOY: GSC submit
  /school-security-camera-installation-rockland-county.
==============================================================

==============================================================
SITE-REBUILD-80 - July 19, 2026
==============================================================
NEW: /school-security-camera-installation-orange-county
  (school silo 13/16). 28 H2, ~9.5K words, 11 orange-county-ny
  WebP (1 hero eager + 10 lazy), 11 ImageObjects. HV routing per
  warehouse-orange: 845 phone + Bronx GBP NAP
  (#organization-bronx), Orange County Sheriff refs, NYPD=0,
  347=0, Troy=0. Slug mix honored: -orange-county for
  repair/nvr/dahua/lorex/hub, bare -orange for dvr-upgrade +
  intercom-repair. AJAX cloned from HV hub (845 fallback).
  Written fresh; one thinning pass vs Rockland (9.12 -> 7.48);
  final Jaccard vs all 12: NYC 0.58 | LI 1.52 | HV 1.82 | MN
  1.61 | BK 1.84 | QNS 2.14 | BX 2.68 | SI 3.05 | Nassau 3.71 |
  Suffolk 5.00 | WC 7.16 | RK 7.48% - all under 20%. FAQPage
  schema regenerated post-thinning: 12=12 mm0.
  Content: crossroads/frontier-of-growth register - KJ/Palm Tree
  UTA village-scale + growth-ready expansion architecture
  (signature angle), Storm King 1867 / NYMA / Tuxedo Park
  Highlands boarding + break-season self-monitoring, rooftop
  HVAC copper-theft protection package (new angle), Black Dirt /
  Warwick farm-edge perimeter-first design, Newburgh river-city
  parishes + Mount Saint Mary + SUNY Orange, Burke Catholic
  Goshen, commuter-corridor daycare boom, bear/deer commissioning
  certainty, Sheriff-distance "recording is the response"
  framing, x1.30 pricing $585-1,235/cam, HV tier table, Orange
  tax 8.125%, exact warranty paragraph, unique pricing rows
  (expansion provisioning + rooftop package), field notes
  (26-cam river-city parish school, masonry raceway methods,
  3:07 a.m. rooftop ladder crew caught, export to city police,
  matched to church/school HVAC theft string, insurer renewed).
  Fieldnotes CSS inherited.
CROSS-LINKS: Orange spans flipped live on all 12 prior school
  pages.
REGISTERED: sitemap 1,851 | _redirects 884 | mega-nav
  schoolcameras.orange (node --check PASS).
COUNTS: 2,613 files | 1,860 HTML.
POST-DEPLOY: GSC submit
  /school-security-camera-installation-orange-county.
==============================================================

==============================================================
SITE-REBUILD-81 - July 19, 2026
==============================================================
NEW: /school-security-camera-installation-putnam-county
  (school silo 14/16). 28 H2, ~9.5K words, 11 putnam-county-ny
  WebP (1 hero eager + 10 lazy), 11 ImageObjects. HV routing per
  warehouse-putnam: 845 phone + Bronx GBP NAP
  (#organization-bronx), Putnam County Sheriff refs, NYPD=0,
  347=0, Troy=0. Slug mix honored: -putnam-county for
  repair/nvr/dahua/lorex/intercom-repair/hub, bare -putnam for
  dvr-upgrade only (NOTE: intercom-repair-putnam-COUNTY differs
  from WC/RK/OC bare pattern - verified from filesystem). AJAX
  cloned from HV hub (845 fallback). Written fresh; one thinning
  pass vs Orange (10.50 -> 7.98); final Jaccard vs all 13: NYC
  0.62 | LI 1.55 | HV 1.91 | MN 1.67 | BK 1.79 | QNS 2.20 | BX
  2.41 | SI 2.80 | Nassau 3.36 | Suffolk 3.53 | WC 5.62 | RK
  6.60 | OC 7.98% - all under 20%. FAQPage schema regenerated
  post-thinning: 12=12 mm0.
  Content: small-quiet-commuter/lake-hamlet register - six
  districts incl. Haldane/Garrison river-village scale, small-
  campus-engineered-properly (signature angle: 12-20 cams w/
  full discipline), farm-based & animal-program campus design
  (barns/paddocks/therapy-animal-respecting, eastern-county
  residential special-ed), wooded quarter-mile driveway
  approach-first design, DEP watershed-adjacent routing
  constraints, Breakneck/trailhead hiker overflow on river-
  village grounds, Sheriff-distance one-person-operability,
  lake-hamlet daycares (Mahopac/Lake Carmel/Putnam Lake), scout
  camps, x1.30 pricing $585-1,235/cam, HV tier table (residential/
  farm campus tier label), Putnam tax 8.375%, exact warranty
  paragraph, unique pricing rows (driveway/approach package +
  farm & animal-area package), field notes (22-cam residential
  farm campus, dorm-threshold-lawful design, wildlife-heaviest
  tuning, POSITIVE catch: eloped resident student located in
  under 4 minutes via doorway->path->paddock->treeline timeline,
  state reviewer closed without follow-up - new catch type, no
  theft). Fieldnotes CSS inherited.
CROSS-LINKS: Putnam spans flipped live on all 13 prior school
  pages.
REGISTERED: sitemap 1,852 | _redirects 885 | mega-nav
  schoolcameras.putnam (node --check PASS).
COUNTS: 2,625 files | 1,861 HTML.
POST-DEPLOY: GSC submit
  /school-security-camera-installation-putnam-county.
==============================================================

==============================================================
SITE-REBUILD-82 - July 19, 2026
==============================================================
NEW: /school-security-camera-installation-dutchess-county
  (school silo 15/16). 28 H2, ~9.6K words, 11 dutchess-county-ny
  WebP (1 hero eager + 10 lazy), 11 ImageObjects. HV routing per
  warehouse-dutchess: 845 phone + Bronx GBP NAP
  (#organization-bronx), Dutchess County Sheriff refs, NYPD=0,
  347=0, Troy=0. Slug mix honored: -dutchess-county for repair/
  nvr/dahua/lorex/intercom-repair/hub, bare -dutchess for
  dvr-upgrade only. AJAX cloned from HV hub (845 fallback).
  Written fresh; two thinning passes (PT 10.79 -> 9.52 -> 8.35,
  OC 10.11 -> 8.95 -> 8.40); final Jaccard vs all 14: NYC 0.57 |
  LI 1.48 | HV 1.78 | MN 1.58 | BK 1.69 | QNS 2.00 | BX 2.20 |
  SI 2.58 | Nassau 3.20 | Suffolk 3.35 | WC 5.77 | RK 7.45 | OC
  8.40 | PT 8.35% - all under 20%. FAQPage schema regenerated
  after each pass: 12=12 mm0.
  Content: river-city/estate-county/college-town register -
  preservation-sensitive installation as county signature
  (National Register stone facades, interior/soffit routing,
  reversible fasteners, consultant-documentation packets, NEW
  angle), historic copper gutter/downspout theft defense
  (distinct from Orange rooftop HVAC), Vassar/Marist/Bard/CIA
  college row, Millbrook + Trinity-Pawling + Oakwood Friends
  (1796 stat) boarding + underwriter/placement-consultant audit
  framing + international-family FERPA, estate-drive gatehouse
  framing, Staatsburg/Rhinebeck residential special-ed, Beacon
  storefront preschools, Lourdes/ADNY parishes, deer-herd
  tuning, x1.35 pricing $610-1,285/cam, HV tier table (boarding/
  estate tier label), Dutchess tax 8.125%, exact warranty
  paragraph, unique pricing rows (preservation-sensitive routing
  + estate drive/gatehouse package), field notes (30-cam
  riverfront campus, 1910s stone hall zero-penetration install,
  chapel copper protected via treeline pole + soffit, 1:52 a.m.
  downspout crew caught from road/pole/soffit angles, plate +
  faces to Dutchess County Sheriff's Office, tied to two-county
  historic-metal string, copper recovered - new catch type).
  Fieldnotes CSS inherited.
CROSS-LINKS: Dutchess spans flipped live on all 14 prior school
  pages.
REGISTERED: sitemap 1,853 | _redirects 886 | mega-nav
  schoolcameras.dutchess (node --check PASS).
COUNTS: 2,637 files | 1,862 HTML.
POST-DEPLOY: GSC submit
  /school-security-camera-installation-dutchess-county.
==============================================================

==============================================================
SITE-REBUILD-83 - July 19, 2026
==============================================================
NEW: /school-security-camera-installation-ulster-county
  *** SCHOOL SILO COMPLETE - 16/16 PAGES LIVE ***
  28 H2, ~9.7K words, 11 ulster-county-ny WebP (1 hero eager +
  10 lazy), 11 ImageObjects. HV routing per warehouse-ulster:
  845 phone + Bronx GBP NAP (#organization-bronx), Ulster County
  Sheriff refs, NYPD=0, 347=0, Troy=0. Slug mix honored:
  -ulster-county for repair/nvr/dahua/lorex/hub, bare -ulster
  for dvr-upgrade. NOTE: no intercom-repair-ulster page exists
  sitewide - all 4 intercom links on this page use
  /intercom-repair-hudson-valley hub fallback per HV fallback
  rule; repoint to /intercom-repair-ulster-county if/when that
  page is built. AJAX cloned from HV hub (845 fallback).
  Written fresh; two thinning passes (DC 10.37 -> 8.68 -> 8.35,
  PT 9.32 -> 8.91 -> 7.99); final Jaccard vs all 15: NYC 0.58 |
  LI 1.40 | HV 1.72 | MN 1.48 | BK 1.63 | QNS 1.75 | BX 2.07 |
  SI 2.31 | Nassau 2.86 | Suffolk 2.97 | WC 4.95 | RK 5.81 |
  OC 6.97 | PT 7.99 | DC 8.35% - all under 20%. FAQPage schema
  regenerated after FAQ-touching pass: 12=12 mm0.
  Content: Catskills-creative/seasonal register - SEASONAL CAMP
  BELT as county signature (two-mode operation: June
  commissioning + fall winterization + cellular watch mode +
  caretaker alert routing, NEW angle), bunk-line/shower-house
  strictest 250.45 reading, camp insurer off-season-monitoring
  questionnaire framing, maker-space/studio equipment-theft
  coverage (cage cameras + fob-aligned video), rail-trail
  boundary design, deep-winter coldest-county spec, spring
  moisture dead-channel angle, Kingston 1777 first-capital stat,
  9 districts + SUNY New Paltz/SUNY Ulster + Waldorf/communal/
  special-ed types, x1.35 pricing $610-1,285/cam, camp tier
  label in table (40-128 cams), Ulster tax 8.0%, exact warranty
  paragraph, unique pricing row (seasonal camp watch package),
  detail form adds Camp/seasonal property + Before camp season
  options, field notes (34-cam camp western hills, June
  commission + October winterize, 1:47am January gate pickup
  lights-off, two men w/ pry bar at dining-hall kitchen door,
  cellular alert -> caretaker live view + Ulster County
  Sheriff's Office, plate tied to two other seasonal-property
  hits, camp reopened intact - new catch type). Fieldnotes CSS
  inherited. PASF + silo footer + coverage: ZERO soon spans
  (final page).
CROSS-LINKS: Ulster spans flipped live on ALL 15 prior school
  pages (incl 3 on Dutchess); DC coverage prose updated
  ("completes this silo next" -> "completes this silo").
SILO-COMPLETION CHECKLIST (MANDATORY, 16/16): PASS -
  sitemap.xml all 16 school URLs (uniform weekly/0.9),
  _redirects all 16 x 200 rewrites (zero stale 301s),
  js/mega-nav.js schoolcameras block all 16 keys, node --check
  PASS, soon spans across silo = 0.
REGISTERED: sitemap 1,854 | _redirects 887 | mega-nav
  schoolcameras.ulster (node --check PASS).
COUNTS: 2,649 files | 1,863 HTML.
POST-DEPLOY: GSC submit
  /school-security-camera-installation-ulster-county + request
  recrawl of all 16 silo URLs.
==============================================================
