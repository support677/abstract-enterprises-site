# site-rebuild-135 — Suffolk County page: surgical correction pass

**Date:** 2026-07-30 · **Baseline:** site-rebuild-134 (cumulative). Surgical pass — the **only** file changed is `parking-lot-camera-installation-suffolk-county.html`. No research, no new pages, no cloning, no approved-prose rewrites, no pricing/keyword/image/alt/title/form changes, and no sibling pages, sitemap, `_redirects` or `mega-nav.js` were touched (all three infra files verified byte-identical to 134).

## Corrections (Suffolk page only)

1. **Schema area contamination removed.** In both the LocalBusiness and Service JSON-LD blocks, `areaServed` was reduced to only `["Suffolk County NY"]` (removed the stray `Richmond County NY` and `New York NY` carried in from the Staten Island clone). Brooklyn GBP routing left unchanged — 1282 Troy Ave, LocalBusiness `#brooklyn`, (347) 934-8335.

2. **Five Staten Island navigation entries repaired** in the embedded header nav (all had been geo-swapped to "Suffolk County" during the clone):
   - Security Camera Installation → NYC Boroughs → `<a href="/security-camera-installation-staten-island-ny">Staten Island</a>`
   - Security Camera Repair → NYC Boroughs → `<a href="/security-camera-repair-staten-island">Staten Island</a>`
   - Camera Pricing → NYC Boroughs → `<a href="/security-camera-pricing-staten-island">Staten Island</a>`
   - Desktop area trigger `data-area="statenisland"` display text → "Staten Island"
   - Mobile button `mnmPickArea('statenisland')` display text → "Staten Island"
   The legitimate Suffolk County entries under Long Island were left unchanged.

3. **Multiplier sentence corrected.** In the AI Overview section, replaced the sentence claiming Suffolk uses "the same 1.20× band as Manhattan, Staten Island and Nassau" with: "On a Suffolk lot the labor sits in the 1.20× Suffolk County tier, reflecting travel across a large county and the pole, trenching and surge work an open field demands. A four-camera storefront and a multi-pole big-box field are not the same job at any price." Approved Suffolk package prices unchanged.

4. **Section order fixed.** The complete AI OVERVIEW REALITY CHECK section was moved (not rewritten) to sit after EQUIPMENT. Order is now YOUR QUESTIONS ANSWERED → EQUIPMENT → AI OVERVIEW REALITY CHECK → mid-page CTA → GET IN TOUCH. The AI section's seven H3 headings and three-paragraphs-per-H3 structure are unchanged.

## Final QA (verified against this codebase)
Zero Richmond County references in the Suffolk schema/page · both areaServed == `["Suffolk County NY"]` · Staten Island correctly labeled in all five nav positions · legitimate Long Island Suffolk entries intact · Equipment precedes AI Overview, AI Overview followed by the mid-page CTA · title 60 (≤60) · meta 159 (150–160) · canonical unchanged · all 11 Suffolk images with alt/title byte-identical to 134 · both `target_area` values = "Suffolk County" · FAQ visible == FAQPage schema (9 == 9, exact) · all nine reciprocal parking-silo links present · sitemap.xml / _redirects / js/mega-nav.js unchanged · div 236/236 · section 41/41 · AI section 7 H3 / 3-paras-each preserved.
