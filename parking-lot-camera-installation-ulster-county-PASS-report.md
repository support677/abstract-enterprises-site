# PASS Report — Parking Lot Camera Installation, Ulster County NY
Build: 2026-08-01 · site-rebuild-130 · FINAL Hudson Valley parking silo page

## Audit: 60/60 PASS
- title 48 chars ("Parking Lot Camera Installation Ulster County NY"); single H1 mentions Ulster
- structure balanced: section 40/40, div 230/230, p 212/212, details 12
- 6/6 JSON-LD parse (LocalBusiness, Service, BreadcrumbList, @graph[11 ImageObject], HowTo, FAQPage); 0 entity-sequences in JSON-LD
- pricing tier 1.53× present: Starter $1,301–2,295 / Standard $2,295–3,825 / Premium $4,284–6,885
- stale sibling prices absent (Rockland 1,105/1,950/3,250/3,640/5,850)
- routing: (845) 640-3835 present; 347 count = 0; Bronx 460 E Fordham ×3; #bronx entity
- AI Overview Reality Check present; competitors named (Angi, HomeAdvisor, Fixr)
- license 12000287431 ×6; three-year AESS warranty; 4.7 / 201 reviews; BYOE; Uniview IPC2128SE-ADF28KM-WL-I0
- not-legal-advice = 3 (>=3 required)
- all 6 Ulster match-area service links present (security-camera-installation-ulster-county-ny, security-camera-repair, commercial, access-control, warehouse, construction-site)
- canonical clean + ulster; 0 `.html` anchors; 11 unique Ulster image refs; 12/12 unique alts
- ZERO residual Dutchess facts: Wassaic/Harlem/Hudson Line/Culinary Institute/Vanderbilt/Poughkeepsie/MidHudson/I-84/Millbrook all = 0
- positive Ulster anchors present: Central Hudson, Ashokan, the Gunks, Thruway, SUNY New Paltz, TechCity, Kingston

## Dedup — parity PASS (standard = parity with delivered siblings, not zero)
Masked SequenceMatcher (geo-neutralized, autojunk=False, real_quick_ratio prefilter, >=0.65):
- PARITY BAR  Dutchess (shipped) vs Putnam: 118/177
- PARITY BAR  Orange   (shipped) vs Putnam: 101/174
- TARGET      **Ulster vs Putnam: 92/177**  → below both shipped siblings; more distinct than pages already live.
Residual similarity is the shared-silo floor (identical-by-design sibling cross-link cards + generic non-geo technical/FAQ blocks), which affects every silo page equally. No restructuring required.

## Registration
- sitemap.xml: Ulster URL added (clean loc, lastmod 2026-08-01, monthly, 0.7); XML valid; tail `</urlset>` intact
- _redirects: `/parking-lot-camera-installation-ulster-county → .html 200` added; no stale 301
- js/mega-nav.js: parkinglot ulster key flipped placeholder → `/parking-lot-camera-installation-ulster-county`; node --check OK
- Ulster coming-soon → live flipped across all 15 sibling parking pages + 3 hubs; 0 residual `area=ulster-county`

## Sibling cards preserved (correctly county-specific, not rewritten)
Putnam card (Brewster/Cold Spring/Carmel/Mahopac/Route 6/Taconic) and Orange card (Woodbury Common/Middletown/Newburgh/Route 17/Thruway) left intact.
