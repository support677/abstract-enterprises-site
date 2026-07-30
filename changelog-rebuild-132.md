# site-rebuild-132 — parking silo: Nassau County page added + integrated

**Date:** 2026-07-30 · **Source:** site-rebuild-131 · Cumulative. Carries forward v127 (12 photos + UNV), v128 (dedup), v129 (hero/pricing/placeholder completion), v130 (research matrix), v131 (Staten Island page + integration).

## Scope of this build
Adds the **Nassau County parking-lot camera page** to the silo — the **ninth live page** and the first of the two Long Island county children (Nassau, then Suffolk) to get its own page. Previously the mega-nav routed Nassau parking to a `/free-quote` fallback; it now points to a real page. The page was built to Blueprint v2.2 and cleared the full pre-delivery audit; then it was integrated into sitemap, redirects, navigation and the reciprocal silo cross-links. The eight existing parking pages changed only by one added silo cross-link card each — no body/keyword edits.

## Build method (no geo-swap)
Cloned the corrected **Staten Island** child as the structural donor — it shares Nassau's exact routing (Brooklyn GBP `1282 Troy Ave`, LocalBusiness `#brooklyn`, phone `(347) 934-8335`, no `(845)`, no GBP swap), so no phone/GBP work was required. Every SI-specific editorial block was then **independently rewritten with genuine Nassau content** (pure geo-swap = ~84% similarity = rejected). Rewritten sections: the neighborhood/why-area, coverage area (8 real Nassau regions), hero SEO caption, what-we-install property types, commercial corridors, curb-cuts/LPR, trenching, waterfront/flood/salt, night coverage, structured garages, industrial/fleet, auto-body, privacy/signage, unauthorized-parking/enforcement, all 14 Q&As, and all 9 FAQs.

Nassau content is grounded in fresh `web_search` research: NCPD's **348 catalytic-converter thefts in a single year** (Commissioner Patrick Ryder; repeat hotspots Plainview, Bethpage, Hicksville, Massapequa, Levittown, Westbury, Mineola), the **Glen Cove** parking-lot phone-alert case (converters sawed off two delivery trucks), push-button-start fob thefts and dealership-row losses; **Roosevelt Field** (largest LI mall, ~12,000 spaces / four garages off Old Country Rd + the Meadowbrook Pkwy), **Mineola** (county seat + Main Line LIRR hub beside the courts and NYU Langone), **UBS Arena** at Belmont (Islanders, 150+ events/yr) and **Nassau Coliseum** (Uniondale), the Hempstead Turnpike / Jericho Turnpike / Sunrise Highway / Old Country Road / Franklin Avenue corridors, the **Freeport** Nautical Mile / Woodcleft Canal marinas, the **Long Beach / Island Park** barrier island (Sandy flood history), and the North Shore Gold Coast (Great Neck / Manhasset / Port Washington / Roslyn) glacial-ridge rock.

## Pre-delivery audit — resolution (Nassau page)
1. **SI-content sweep:** every Staten Island landmark, precinct, neighborhood and self-reference ("the Island", "an Island lot", "mid-Island", St. George/ferry/Great Kills/Todt Hill/West Shore/Hylan/Forest Ave/Richmond Ave/New Springville/Empire Outlets/Bluebelt/Fresh Kills, etc.) was rewritten out — **final sweep ALL CLEAR**. Legitimate Nassau tokens preserved (Island Park, Cross Island Parkway, Islanders, and generic "marina").
2. **Fabricated stat removed:** the SI-only "**more than 1,300 abandoned-vehicle complaints borough-wide**" figure carried in by the clone was **deleted** and the Q&A reframed generically (LIRR/out-of-state vehicles left for weeks) — no invented number remains.
3. **Duplication:** editorial/process prose is independently rewritten; against the siblings the only shared blocks are approved legal/business language (rating, license, warranty, pricing structure, disclaimers, NAP) and coverage-grid nav labels — no editorial copy is duplicated. Byte size 160,421 sits normally inside the sibling range (nearest SI 159,237); dedup is verified by the content sweep and independent rewrites, not by byte count (all area pages share the same template/boilerplate by design).
4. **FAQ vs schema:** the FAQPage schema was **regenerated from the visible FAQ** after the rewrites — **visible FAQ 9 == schema 9**. HowTo step text re-synced to the visible copy. Fixed a recurring "Installatiin" typo (including in `<title>`) and the "on Nassau County" island-idiom (a county is *in*, not *on*).
5. **202-keyword mapping — NOT PASSED (honest):** the 202 approved terms are assigned to six primary pages only (NYC 131, Queens 34, Long Island 16, Brooklyn 10, Manhattan 7, Hudson Valley 4). **Nassau County carries no primary approved-term assignment.** Coverage stands at 84 USED / 118 FOR REVIEW; those terms belong to the six assigned pages and need their own keyword pass — placing them on Nassau would be stuffing (prohibited). Nothing was force-placed.

## Pricing
Nassau uses the **×1.20** labor tier (Manhattan / Staten Island / Nassau / Suffolk): Starter **$1,020–$1,800** · Standard **$1,800–$3,000** · Premium **$3,360–$5,400** (Brooklyn base $850/$1,500/$2,500/$2,800/$4,500). Post-warranty rate is the locked, non-area-priced **$195/hr + $585 three-hour minimum** (unchanged).

## Integration
- **sitemap.xml:** Nassau added (`priority 0.7`, `changefreq monthly`); XML validated.
- **_redirects:** `/parking-lot-camera-installation-nassau-county → …-nassau-county.html 200` added.
- **js/mega-nav.js:** `nassau` parking repointed from the `/free-quote` fallback to the real page; `node -c` validated.
- **Reciprocal silo cross-links:** a "Parking Lot Cameras Nassau County" card added to the *ALL AREAS SERVED* grid on all eight siblings (nyc, brooklyn, manhattan, queens, bronx, long-island, hudson-valley, staten-island); the Nassau page links to all eight. Div balance verified on every edited page.
- **Assets:** 11 Nassau photos added at `/images/parking/*-nassau-county.webp` (1 hero + 10 body), following the deployed per-area renamed-set convention.

## Files changed this build
- Added: `parking-lot-camera-installation-nassau-county.html`; 11 `images/parking/*-nassau-county.webp`; `changelog-rebuild-132.md`.
- Modified: `sitemap.xml`; `_redirects`; `js/mega-nav.js`; the eight sibling `parking-lot-camera-installation-{nyc,brooklyn,manhattan,queens,bronx,long-island,hudson-valley,staten-island}.html` (one silo cross-link card each); `deploy-readme.txt`.
- Removed: `changelog-rebuild-131.md`.

## Nassau page verification (against this live codebase)
title 58 (≤60) · meta 157 (147–160) · one H1 · canonical www + extensionless · Brooklyn GBP 1282 Troy Ave, LocalBusiness `#brooklyn` · phone (347) 934-8335, zero (845)/(800) leak · both-offices contact block (Brooklyn + Bronx) intact, consistent with siblings · 2 Web3Forms + `target_area=Nassau County` + 2 consent checkboxes · 12 `<img>` (1 logo + 11 Nassau, all on disk, unique alts) · 6 JSON-LD blocks valid (LocalBusiness, Service, BreadcrumbList, Person, HowTo, FAQPage) · visible FAQ 9 == FAQPage schema 9 · div balance 232/232 · section balance 38/38 · all required disclaimers verbatim ($195/hr, $585 min, three-year warranty, scheduling/results/AHJ/legal) · Nassau file size 160,421 bytes · reciprocal links both directions · zero broken internal links · sitemap XML + mega-nav JS validate clean.
