# site-rebuild-171 — Commercial Security silo: Bing PAA + DuckDuckGo/PASF blocks on all 10 pages

## Scope (per Grok directive)
Every silo page (nyc, long-island, hudson-valley, manhattan, brooklyn, queens, bronx, staten-island, nassau-county, suffolk-county) gained, inside its existing People Also Ask section:
1. **Bing PAA block** — H3 "Asked on Bing: Commercial Security in [Market]" + 10 market-specific Q&As as `<details class="fi paa">` (inherits .fi styling, deliberately excluded from FAQ counting/schema — FAQPage stays 12=12 everywhere). New intents not previously covered: insurance premium credits, tax deductibility/Section 179, system lifespan, camera signage rules (hedged), audio/private-area limits, monthly monitoring cost, 24/7-operation design, lot-coverage legality, seasonal year-round monitoring, plus market-worded cost/permit/local-vs-national/internet-down/license-verify variants — all phrasings unique silo-wide and vs corpus.
2. **PASF block** — H2 id="pasf" "Related Searches for Commercial Security in [Market]" + 10 natural phrases in two tick-list columns; 3–4 per page linked to verified clean URLs (own-area service pages on children, silo siblings on hubs; e.g. "warehouse security cameras Hunts Point", "dealership security cameras Sunrise Highway", "winery and farm stand security cameras North Fork", "warehouse security cameras Hauppauge industrial park"). No .html in any link.

## Untouched (per rules)
No files deleted · favicon block untouched · sitemap.xml / _redirects / js/mega-nav.js untouched (no new URLs) · all 7 JSON-LD blocks byte-identical in structure (7 parse, FAQ 12=12) · phone routing unchanged · existing content unchanged.

## QA
All 10 pages: div/section/ul balance OK · 7 schemas parse · FAQ 12=12 with paa excluded · paa=10 + pasf H2=1 each · zero duplicate questions across silo (qsub+FAQ+PAA domains) · zero corpus collisions on 100 new PAA questions (corpus 2,583) · zero duplicate H2/H3 silo-wide · every new href resolves (file or _redirects) · Playwright: renders clean, details toggle works, zero JS errors at 1440+390 on nyc/hudson-valley/suffolk-county.
