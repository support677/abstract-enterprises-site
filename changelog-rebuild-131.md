# site-rebuild-131 — parking silo: Staten Island page added + integrated

**Date:** 2026-07-30 · **Source:** site-rebuild-130 · Cumulative. Carries forward v127 (12 photos + UNV), v128 (dedup), v129 (hero/pricing/placeholder completion + first research pass), v130 (full research matrix).

## Scope of this build
Adds the **Staten Island parking-lot camera page** to the silo — the eighth live page. Previously the mega-nav routed Staten Island parking to a `/free-quote` fallback; it now points to a real page. The page was built to Blueprint v2.2 and cleared a five-item deep-integrity audit; then it was integrated into sitemap, redirects, navigation and the reciprocal silo cross-links. Queens and Long Island body content is unchanged; the seven existing parking pages changed only by one added silo cross-link card each (no body/keyword edits).

## Five-item deep-integrity audit — resolution (SI page)
1. **AI Overview (source EMPTY):** consistent with the v130 methodology note — `web_search` does not return Google's AI Overview box, so the source is EMPTY. The page had carried an "AI Overview Reality Check" section written as a rebuttal of a captured overview; because the source is EMPTY *and* all seven of its topics duplicated intents already covered canonically in the body (pricing, wireless/point-to-point links, pole mounting, motion-rule tuning, consumer-kit limits, lead-matching competitors, "cameras document rather than prevent"), the section was **removed** rather than fabricated. Angi/HomeAdvisor/Fixr (only in that section) removed with it. No unsupported AI-summary claim remains.
2. **Duplication (H2/H3/body/Q&A/FAQ/schema):** post-removal scan shows **0 strong heading/question intent duplicates**; against the real Brooklyn page the only shared blocks are approved legal/business language (rating, license, warranty, pricing, disclaimers, NAP) and two coverage-grid nav labels — no editorial/process copy is duplicated.
3. **FAQ duplicates:** the retention and warranty FAQ items duplicated the body "Recording, Retention and Remote Access" and "Warranty and Service Terms" sections and were **removed**; the FAQPage schema was regenerated so **visible FAQ 9 == schema 9**.
4. **Stale railway claim:** the research matrix Section 6 false "at-grade Staten Island Railway crossing" finding and its on-page usage mapping were **deleted** (SIR grade crossings were eliminated 1938–40 on the South Shore line and borough-wide by the mid-1960s); the related Q&A was replaced with a **CBS-sourced abandoned/mystery-vehicle** concern, and the pain-map tally was corrected (Q#7 is the abandoned-vehicle question, not a crossing question).
5. **202-keyword mapping — NOT PASSED (honest):** the 202 approved terms are assigned to six primary pages only (NYC 131, Queens 34, Long Island 16, Brooklyn 10, Manhattan 7, Hudson Valley 4). **Staten Island carries no primary approved-term assignment.** Coverage stands at 84 USED / 118 FOR REVIEW; the FOR-REVIEW terms belong to those six pages and require their own keyword pass — they cannot be advanced from the Staten Island page, and placing them on Staten Island would be stuffing (prohibited). No terms were force-placed on Staten Island.

## Integration
- **sitemap.xml:** Staten Island added (`priority 0.7`, `changefreq monthly`); XML validated.
- **_redirects:** `/parking-lot-camera-installation-staten-island → …-staten-island.html 200` added.
- **js/mega-nav.js:** `statenisland` repointed from the `/free-quote` fallback to the real page; `node -c` validated.
- **Reciprocal silo cross-links:** a "Parking Lot Cameras Staten Island" card added to the *ALL AREAS SERVED* grid on all seven siblings (nyc, brooklyn, manhattan, queens, bronx, long-island, hudson-valley); the Staten Island page links to all seven. Div balance verified on every edited page.
- **Assets:** 11 Staten Island photos added at `/images/parking/*-staten-island.webp` (1 hero + 10 body); `parking-lot-camera-installation-staten-island-research-matrix.md` and `-pain-question-map.md` added (documentation, matching the existing per-area matrix convention).

## Files changed this build
- Added: `parking-lot-camera-installation-staten-island.html`; 11 `images/parking/*-staten-island.webp`; `parking-lot-camera-installation-staten-island-research-matrix.md`; `parking-lot-camera-installation-staten-island-pain-question-map.md`; `changelog-rebuild-131.md`.
- Modified: `sitemap.xml`; `_redirects`; `js/mega-nav.js`; the seven sibling `parking-lot-camera-installation-{nyc,brooklyn,manhattan,queens,bronx,long-island,hudson-valley}.html` (one silo cross-link card each); `deploy-readme.txt`.
- Removed: `changelog-rebuild-130.md`.

## SI page verification (against this live codebase)
title 59 (≤60) · meta 158 (147–160) · one H1 · canonical www + extensionless · Brooklyn GBP 1282 Troy Ave, LocalBusiness `#brooklyn` · phone (347) 934-8335, zero (845) leak · 2 Web3Forms + `target_area=Staten Island` + 2 consent checkboxes · 12 `<img>` (1 logo + 11 SI, all on disk, unique alts, 11 SI alts carry Staten-Island + keyword) · 6 JSON-LD blocks valid · div balance 232/232 · all required disclaimers verbatim ($195/hr, $585 min, three-year warranty, scheduling/results/AHJ/legal) · SI file size 159,237 bytes, nearest sibling Long Island 4,218 bytes away (all >2,048) · reciprocal links both directions · zero broken internal links · desktop 1280 + mobile 390 render with no horizontal overflow and no JS errors.
