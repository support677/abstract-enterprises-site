# site-rebuild-186 — Batch 9 Bronx buzzer pages (Fairmount · Fieldston · Fordham Heights)

## Pages (3)
| Page | Words | Title chars | KW bank | Status |
|---|---|---|---|---|
| /door-buzzer-repair-fairmount-bronx-ny | 7,128 | 48 | 109/109 | PASS (rebuilt) |
| /door-buzzer-repair-fieldston-bronx-ny | 7,246 | 48 | 109/109 | PASS (rebuilt) |
| /door-buzzer-repair-fordham-heights-bronx-ny | 7,157 | 54 | 109/109 | PASS (NEW page) |

Blueprint v2.1 per page: 20 sections, 6 branded figures (/images/buzzer-repair/, 1402×1122, hood-specific alt/title/caption), 3 forms, 7 schemas (LocalBusiness #bronx · Service · Breadcrumb · HowTo · ImageObject @graph · FAQPage · Person), 31 unique questions (11 Q&A + 8 PAA + 12 FAQ), Bronx phone routing (646/800/WA), breadcrumb pos-3 = own URL, inline mega-nav CSS.

## Angles registered (batch 9 — never reuse)
- **fairmount** — one street, two generations: 1931 elevator riser buildings beside 2001 builder-grade infill three-families crossing the 20-year line as a cohort; trench-edge grit/vibration at the Cross Bronx service roads; hill-name identity (one of Tremont's three hills); riser discipline; "specified to outlast."
- **fieldston** — privately governed landmark enclave: FPOA private streets/patrol/annual closure, 2006 LPC district (~257 houses), gate-pier stations, long-run voltage drop metered before blame, garden-cut buried-pair splices via mapping, landmark-manners invisible workmanship, carriage-house second stations, weather-following faults.
- **fordham-heights** — panel-to-population mismatch / reconciliation: basement board read first, buttons tested to true doors, shared buttons untangled onto spare pairs, orphaned lines documented, directory truth, brown-out = supply metered first, the map is the deliverable. Streets: Ryer/Walton/Anthony + Concourse flank + 182nd–183rd Sts B/D (Creston/Morris/Valentine left to the Fordham page).

## Infrastructure
- **_redirects:** DELETED stale hijack rule `/door-buzzer-repair-fordham-heights-bronx-ny → /door-buzzer-repair-fordham-bronx-ny 301` (would have redirected the new page to Fordham on live). Added clean-URL 200 rewrite + `.html`→clean 301 for fordham-heights, matching file convention. Other fordham-heights service 301s (intercom/camera/etc → fordham) intentionally left — those services have no Fordham Heights pages.
- **sitemap.xml:** fordham-heights buzzer URL added (monthly / 0.7), XML validated, `</urlset>` tail intact — 1,881 URLs.
- Bronx buzzer hub intentionally not edited (batches 1–9 precedent: hub carries silo links only).

## QA
qa3 PASS ×3 (img check updated to shared-library convention: 6 distinct /images/buzzer-repair/ figures + hood name in every alt). Question corpus 3,573 → 3,666 (+93, zero duplicates; 7 collision rewords applied on Fordham Heights). Playwright desktop 1440 + mobile 390: broken=[], overflow=false, nav renders, 6 figs/page.

## Deploy
Drag **site-rebuild-186-FULL.zip** into Netlify → Publish → Ctrl+Shift+R. Note: until this deploy, the live `_redirects` still hijacks /door-buzzer-repair-fordham-heights-bronx-ny to the Fordham page.
