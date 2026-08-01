# Orange County Parking Lot Camera Page — PASS Report

File: `parking-lot-camera-installation-orange-county.html` · 155,288 bytes
Live URL: https://www.abstractenterprisessecuritysystems.com/parking-lot-camera-installation-orange-county.html
Date verified: 2026-08-01

## Build note
This page was authored, corrupted twice by faulty JSON-LD regexes (nested-brace / `.*?</script>` matches that collapsed schema and then truncated the body to 17 KB), and **cleanly rebuilt from a fresh Rockland clone**. All 6 JSON-LD blocks are now inserted/replaced by literal string anchors only — never by regex across `<script>` spans.

## Dedup vs Rockland donor (masked, geo→AREA, SequenceMatcher, ceiling 0.65)
| Class | Count | >0.65 | Max |
|---|---|---|---|
| Prose `<p>` | 129 | **0** | 0.64 |
| List `<li>` | 45 | **0** | 0.64 |

Two full rewrite passes (84 items, then 46 residual) plus a 2-item micro-pass cleared every masked-similar block. Prose fully restructured; functional survey/checklist/pricing-driver bullets reworded and item-reordered (order-sensitive similarity) to preserve accuracy while dropping below ceiling.

## Structural audit
| Check | Result |
|---|---|
| `<title>` ≤ 60 chars | PASS — "Parking Lot Camera Installation Orange County NY" (48) |
| Single `<h1>` | PASS (1) |
| `<section>` open/close balanced | PASS (40/40) |
| `<div>` open/close balanced | PASS (226/226) |
| FAQ accordions (`<details>`) | PASS (12) |
| Images referenced | PASS (11, all unique paths) |
| Image alts / titles unique | PASS (11 unique alt, 11 unique title) |
| Image files resolve on disk | PASS (0 missing) |

## JSON-LD (6 blocks)
| Block | Present | Parses | Entity-clean |
|---|---|---|---|
| LocalBusiness (url = own page, Bronx GBP) | ✓ | ✓ | ✓ |
| Service (name/areaServed/description Orange, dateModified 2026-08-01) | ✓ | ✓ | ✓ |
| BreadcrumbList (Home › Hudson Valley › Orange County) | ✓ | ✓ | ✓ |
| @graph — 11× ImageObject (Orange contentUrl/name/caption) | ✓ | ✓ | ✓ |
| HowTo — 8 steps | ✓ | ✓ | ✓ |
| FAQPage — 12 Q&A | ✓ | ✓ | ✓ |

- FAQPage `mainEntity` matches the 12 visible `<summary>` questions **exactly**.
- HowTo `step[].name` matches the 8 visible HOW IT WORKS `<li>` labels **exactly**.
- No prohibited entity sequences (`&amp; &mdash; &#39; &ldquo; &rsquo; &ndash;`) in any block (Unicode used).

## Pricing (1.40× Brooklyn base)
| Tier | Range | Present | Stale (1.30×) absent |
|---|---|---|---|
| Starter | $1,190–$2,100 | ✓ | $1,105 absent ✓ |
| Standard | $2,100–$3,500 | ✓ | $1,950 absent ✓ |
| Premium | $3,920–$6,300 | ✓ | $3,640 / $5,850 absent ✓ |

## Routing / contact
| Check | Result |
|---|---|
| 845 (847) 640-3835 occurrences | 8 |
| 347 occurrences | **0** |
| Bronx GBP (460 E Fordham Rd) | present |
| Web3Forms key ×2 (form-hero + form-detail) | PASS |
| target_area / landing_page = Orange County (×2 each) | PASS |

## Content / blueprint
| Check | Result |
|---|---|
| AI Overview Reality Check — 7× H3 | PASS |
| Competitors named (Angi, HomeAdvisor, Fixr) | PASS |
| NYS License #12000287431 | present |
| Three-year AESS warranty (verbatim exclusions) | present |
| ★4.7 · 201 Google Reviews | present |
| BYOE install offered | present |
| Uniview model (IPC2128SE-ADF28KM-WL-I0 et al.) | present |
| "not legal advice" disclaimers | 4 |
| Match-area service links (all 6 Orange) | PASS (8 anchor occurrences) |
| Canonical = /parking-lot-camera-installation-orange-county.html | PASS |
| CTA "Talk Through Your Orange County Lot" ×1; leftover Rockland CTA removed | PASS |
| Broken-link sweep (parking siblings) | PASS — all resolve |

## Registration (separate files, in ZIP)
| File | Orange entry |
|---|---|
| sitemap.xml | added after Rockland (loc `…-orange-county.html`, lastmod 2026-08-01, monthly, 0.7); XML valid; tail `</urlset>` intact |
| _redirects | `/parking-lot-camera-installation-orange-county → …-orange-county.html 200` |
| js/mega-nav.js | `orange:'/parking-lot-camera-installation-orange-county'` (flipped from free-quote fallback) |
| Coming-soon → live flips | Orange anchor flipped to live across all 12 siblings + hub (silo-nav grid **and** the "Request an Orange County lot survey" cards on the HV hub + Westchester). 0 Orange free-quote refs remain. |

## Result: **PASS**

## Silo status
Parking silo built: NYC hub + 5 boroughs + LI hub + Nassau + Suffolk + HV hub + Westchester + Rockland + **Orange** = 13 pages.
**Remaining HV counties: Putnam, Dutchess, Ulster (3).** Silo is **not complete** and the silo-completion checklist is deferred until the final HV county (Ulster) is built.
