# MANIFEST — site-rebuild-185

**Date:** August 16, 2026
**Type:** Photos distributed THROUGHOUT every door-buzzer-repair page
**Baseline:** site-rebuild-184 → same file count (3,547); includes the 183 CSS inlining fix and all 184 photo work.

## What changed
The 139 non-blueprint buzzer pages (silo hubs, counties, old Brooklyn/Bronx hoods, pricing) previously carried a single hero photo. Now each page has the branded photos **spread through the body**: a figure inserted after roughly every 6th H2 section, deterministic per-page photo rotation, no photo repeated on a page.

- Pages photo-distributed: **139**
- Total branded photo placements sitewide: **1,103** across 163 buzzer pages (was 283)
- Photos per page: min 2 (pricing, short pages) / max 8 / avg 6.9
- Every inserted figure: kw+geo alt (`Door buzzer repair in {Area} — AESS technician {photo description}`), matching title attr, short figcaption, lazy loading, width/height set, 900px max-width, rounded.
- The 24 blueprint hood pages remain at their audited 6-figure spec (photos already distributed across their 20 sections) — untouched this pass to protect qa3 counts and the pending batch-8 audit.

## Verification
- 1,103/1,103 placements: src exists on disk, alt ≥25 chars — 0 problems.
- Playwright desktop (5 page types incl. 43-H2 county page and pricing): broken images 0, container overflow 0.
- Playwright mobile 390px: horizontal overflow 0 px.
- No text/question changes — qa3/corpus untouched (3,573).

## Deploy
- site-rebuild-185-FULL.zip → Netlify drag-and-drop (covers styling fix + all photo work)
- github-commit-185.zip → extract over C:\dev\abstract-enterprises-site, push via GitHub Desktop
