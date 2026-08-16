# MANIFEST — site-rebuild-184

**Date:** August 16, 2026
**Type:** Branded technician photos deployed across the entire door-buzzer-repair silo + minor fixes
**Baseline:** site-rebuild-183 (3,672 files) → this build: **3,547 files** (+19 photos, +1 manifest, −144 orphaned hood images, −1 intercom-keypad-dark.png)
**Includes:** the 183 CSS hardening (mega-nav.css inlined into all pages) — deploying 184 covers the styling fix.

## New photo library
`/images/buzzer-repair/` — 19 AESS-branded technician photos (supplied by Anwar), optimized 1402–1600px JPEG q82, 180–340 KB each, 4.7 MB total:
strike/release test · handset station wiring · handset release check · wall station replacement · riser tone tracing · basement terminal panel · power-supply service · transformer voltage test · door-frame wire splice · junction-box tracing · contact cleaning · lobby directory diagnostics · lobby panel button wiring · weather sealing · vandal-damage replacement · video intercom tenant verification · two-technician release test · tenant-call wire mapping · terminal voltage measurement.
(The 20th upload — "mk dance on Hudson" storefront, IMG_4879.jpeg — excluded as unrelated.)

## Page changes (all 163 door-buzzer-repair pages)
1. **24 rebuilt Bronx hood pages** — all 6 figures per page remapped to topic-matched photos from the new library (keyword-scored against each figure's alt+caption, deterministic per-page rotation for variety). Alt text rewritten kw+geo to describe the actual photo; figcaptions and titles preserved; width/height updated to 1402×1122. All 360 og:image / schema ImageObject URLs repointed and distributed across each page's 6 photos (6 distinct per page verified).
2. **120 template pages** (silo hubs, counties, old Brooklyn/Bronx hoods) — the shared `intercom-keypad-dark.png` hero swapped for a rotated branded photo, alt kw+geo.
3. **19 image-less pages** (incl. pricing + Westchester silo) — branded hero figure inserted after the H1 intro paragraph, rotated, alt kw+geo.
Distribution across pages: every one of the 19 photos in use (min 4×, max 32×).

## Cleanup
- Deleted 144 orphaned `/images/door-buzzer-repair-*` files (11 MB) + `intercom-keypad-dark.png` — zero remaining references verified.
- Fixed broken `src="/logo.png"` → `/images/logo.png` on **77 pages** (pre-existing broken nav logo on old-template pages, caught during Playwright pass).

## Verification
- 163/163 buzzer pages carry `/images/buzzer-repair/` photos; every referenced src exists on disk.
- Playwright forced-eager across 6 page types (2 rebuilt hoods, county silo, old Brooklyn hood, inserted-hero, pricing): broken images = [] everywhere after logo fix.
- No content/question/text changes — qa3 not re-run (corpus unchanged at 3,573).
- Sitemap/_redirects/mega-nav untouched.

## Note for repo route
The GitHub overlay zip cannot delete files. If deploying via GitHub Desktop, the 145 deleted images remain in the repo harmlessly (unreferenced). The Netlify FULL-zip route removes them.

## Batch-8 status
Still awaiting Anwar's audit (eastchester / edenwald / edgewater-park). buzzer-audit-batch8.zip regenerated with the photo-swapped versions.

## 184.1 addendum (same delivery)
- Caption↔photo coherence pass on the 24 rebuilt hood pages: device words in figcaptions (video, camera, directory, keypad, handset, transformer, vandal) validated against the assigned photo; 5 figures reassigned (fordham ×4, crotona-park-east ×1). Zero clashes, zero per-page duplicate photos remain.
- All 144 rebuilt-figure `title` attributes rewritten to describe the actual photo (was: legacy titles describing the removed images).
- og:image/schema arrays on fordham + crotona-park-east resynced to final figure order.
- Sitewide validation: 283 branded imgs across 163 pages, 0 missing/short alts, 0 broken images (Playwright).
