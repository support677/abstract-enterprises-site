# MANIFEST — site-rebuild-183

**Date:** August 15, 2026
**Type:** Emergency hardening — CSS single-point-of-failure removed
**Baseline:** site-rebuild-182 (3,671 files) → this build: 3,672 files (content identical to 182 + this manifest)

## What changed
- `css/mega-nav.css` (15,542 B) **inlined as a `<style>` block into every HTML file that referenced it**: 1,777 files, 3,286 `<link>` tags removed (1,509 files carried the tag twice — duplicate removed).
- `css/mega-nav.css` kept on disk unchanged (harmless, still in repo/zips).
- Zero content changes. No sitemap/_redirects/mega-nav.js changes.

## Why
Two consecutive Netlify deploys rendered the entire site unstyled — every page depended on one external stylesheet resolving. Root exposure: `github-commit-N.zip` (repo diff) does not contain `css/mega-nav.css` (unchanged since baseline), so a mis-drag of the diff zip into Netlify drag-and-drop strips site-wide styling. Inlining makes every page self-styling: no deploy mistake, partial upload, or stale cache can render the site naked again.

## Verification
- Residual `css/mega-nav.css` references in HTML: 0
- Inline block confirmed present in index.html, door-buzzer-repair-eastchester-bronx-ny.html, fire-alarm-installation-nyc.html
- Playwright (localhost:8899): `.mn-bar` computed `display:flex, max-width:1320px, height:72px` — mega-nav rules applying from inline CSS; no page errors
- Size impact: ~+27 MB raw HTML, compresses to single-digit MB in zip

## Deploy rule (unchanged, restated)
- `site-rebuild-N-FULL.zip` → Netlify drag-and-drop ONLY
- `github-commit-N.zip` → extract over `C:\dev\abstract-enterprises-site` ONLY (GitHub Desktop push → Netlify auto-deploy)
- From this build, `github-commit-N.zip` force-includes css/, js/, _redirects, sitemap.xml, index.html as insurance.

## Batch-8 status
Batch-8 pages (eastchester / edenwald / edgewater-park) unchanged in content; still awaiting Anwar's audit. buzzer-audit-batch8.zip regenerated with the inlined-CSS versions of the 3 files.
