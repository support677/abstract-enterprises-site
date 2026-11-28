# site-rebuild-174 — _redirects: kill all legacy .html URLs (canonical consolidation)

## What changed
`_redirects` only. Fully additive — zero rules removed, zero files touched otherwise.

## Appended (3,272 rules + 5 comment/blank lines)
1. **1,370 × 200 clean-route backfills** — every page whose clean path had no route now serves at its clean URL (`/slug  /slug.html  200`). Includes /pay, /generate-invoice, /alarm-calculator, /intercom-pricing and ~1,366 service/neighborhood pages.
2. **1,902 × 301 .html kills** — every legacy `.html` path now permanently redirects to its clean equivalent (`/slug.html  /slug  301`), including /index.html → /. Netlify preserves query strings, so /pay.html?job=…&amount=…&area=… lands on /pay with params intact and the Stripe flow keeps working.

## Deliberately excluded (19)
- 16 × commercial-security-systems-*.html — silo already clean, per directive untouched
- 404.html (Netlify error page), googleb71cfc9ca1a95ac4.html (Search Console verification)
- 7 legacy custom .html→custom-target 301s kept intact and un-shadowed (services/areas/terms/pricing/av-installation-nyc/marble-hill/home-automation-manhattan)

## Pre-existing quirks left as-is (do not delete rule)
- Line 5 `/*.html  /:splat  301!` — the old global splat attempt; Netlify ignores patterns with content after the splat, which is why GSC still saw .html duplicates. Left in place (harmless either way); the explicit per-URL rules below it do the real work.
- 18 legacy duplicate FROM paths among old Wix-era vanity 301s — pre-existing, first-match-wins, untouched.

## Validation
4,288 lines total · 4,204 rules · 0 malformed lines · 0 new duplicate FROMs · 0 self-loops · every new 301 target resolves (clean route exists) · every new 200 target file exists on disk · 0 silo rules added.

## Expected GSC effect
"Alternate page with proper canonical tag" .html entries convert to "Page with redirect" as Google recrawls; clean URLs already in sitemap (1,912) remain the indexed set. No sitemap or canonical changes required.

Deploy: Netlify drag-and-drop of site-rebuild-174-FULL.zip (or extract github-commit-174.zip over C:\dev\abstract-enterprises-site and push).
