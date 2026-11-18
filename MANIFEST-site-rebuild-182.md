# MANIFEST — site-rebuild-182

**Date:** August 15, 2026
**Batch:** Bronx door-buzzer-repair remediation — batch 8 of the neighborhood sweep
**Baseline:** site-rebuild-181 (3,652 files) → this build: 3,671 files

## Pages rebuilt (3)

| Page | Words | Figures | Schemas | Title (len) | KW bank |
|---|---|---|---|---|---|
| /door-buzzer-repair-eastchester-bronx-ny | 7,119 | 6 | 7 | Door Buzzer Repair Eastchester Bronx NY \| Abstract (50) | 109/109 |
| /door-buzzer-repair-edenwald-bronx-ny | 6,943 | 6 | 7 | Door Buzzer Repair Edenwald Bronx NY \| Abstract (47) | 109/109 |
| /door-buzzer-repair-edgewater-park-bronx-ny | 7,151 | 6 | 7 | Door Buzzer Repair Edgewater Park Bronx NY \| Abstract (53) | 109/109 |

## Standard block (all 3 pages)
- Phones: (646) 490-0629 ×12 body/schema + (800) 486-0943 ×5 chrome-only; wa.me/17186790359 ×3
- 20 sections, 139 divs, 3 forms (qualifier + hero + detail), 12 FAQ + 8 PAA + 11 Q&A subheads = 31 unique questions per page
- 7 schemas: LocalBusiness#bronx (460 E Fordham Rd, 4.7/201) / Service / BreadcrumbList / HowTo (5 steps) / ImageObject @graph ×6 / FAQPage / Person (Anwar Timothy, Lic #12000287431)
- Self-canonical www URLs; freshness stamp + changelog Aug 15 2026; three-year products-we-supply warranty; $195/hr + $585 minimum; Web3Forms key standard
- Silo links: Bronx buzzer hub up-link, install cross-link /door-buzzer-installation-bronx-ny, matching-area intercom/camera/access siblings, 4 nearby buzzer pages each

## Per-hood uniqueness
- **Eastchester** — builder-batch rows at the end of the line: attached brick rows wired by one builder to one plan in one season ("batch clock" — identical parts age on identical curves), neighbor repair records as diagnostic evidence ("row record"), shared row windows (one dispatch, several addresses, separate invoices), Dyre Ave 5-terminus commuter-window scheduling (dawn failures triaged between rushes, tested before evening trains), duty-rated wear-item buttons, Boston Rd corridor doors, Seton Falls park-edge, honest NYCHA boundary (Eastchester Gardens maintains via NYCHA channels; page serves private stock). No salt-film language (n/a inland).
- **Edenwald** — high-cycle duty-rated hardware around the borough's biggest campus: perimeter private rows/rentals/corner doors where hardware wears by cycle count not calendar ("under-spec" quiet-door parts consumed in months), wear-vs-wiring diagnosis split, "peak fault" (works at dawn, fails at after-school rush — diagnose at the failing hour, rate for the peak), strike "chatter" as the cheap warning moment, corner-split restoration (storefront/residential honest separate circuits), portfolio duty-rating passes for landlords, explicit honest NYCHA boundary (Edenwald Houses maintains its own; page serves private side). Laconia/Baychester, E 225th–233rd, Schieffelin, Grenada Pl.
- **Edgewater Park** — bungalow co-op on private lanes: cottage-scale entry systems, unusual house-and-land tenure (homeowner owns bungalow, co-op owns land — homeowner decides own house, co-op office governs common elements), walk-in lane dispatch (truck parks at lane head), winterized summer-stock wiring "promotion" finished (seasonal-duty systems brought to year-round spec — distinct from East Tremont's braided multi-panel layers), close-set crossed lane pairs ("your ring answers next door"), shore-lane weather mentioned lightly (NO salt-film — Throggs Neck owns; NO bay-rated lead — Country Club owns). Sections A/B/C, Pennyfield Ave approach, Weir Creek, bayfront lanes.
- **Colony differentiation reserved:** Edgewater Park takes bungalow-co-op tenure + lane dispatch + summer-stock promotion. Silver Beach (the other colony, unbuilt) will need a different lead — volunteer institutions / hill-to-shore terraces or similar. Do not reuse EP's angle there.

## Defects prevented
- All 3 old pages carried Bay Ridge-era template contamination — fully replaced with original content
- No &mdashh; typos (grepped all 3)
- No marble-hill / woodlawn links
- No 845 numbers on Bronx pages
- Figure count verified 6/6 per page; forced-eager decode broken=[]
- NYCHA claims kept honest on both campus-adjacent pages (no claim of serving NYCHA stock)

## QA
- qa3.py PASS ×3 (109-kw bank, phone counts, section/div/form/schema counts, title lengths, href resolution, corpus collision check vs 3,480-line baseline)
- Collision fixes: internal QA/FAQ station-swap dupes reworded on all 3 pages (EC "Can a dead station at just one address on the row be renewed alone?", ED "Can one tenant's dead wall unit be swapped without a building project?", EP "Can just the cottage's inside station be replaced by itself?")
- Question corpus: 3,480 → 3,573 (93 new unique questions)
- Playwright: 1440px + 390px, h1==1, console clean (CallRail 403s filtered), forced-eager broken=[] on all 3

## File safety
- sitemap.xml / _redirects / js/mega-nav.js unchanged — all 3 URLs pre-registered (verified 1 sitemap + 2 redirects entries each)
- Images copied additively with existence checks (18 new image files, 6 per hood)
- Only the 3 target HTML files modified in the site tree
