# Abstract Enterprises Site — Page Blueprint (FULL / CONSOLIDATED)

**Owner:** Anwar Timothy
**Status:** v2.3 (full consolidation — single source of truth)
**Scope:** every service × area page on `abstractenterprisessecuritysystems.com`
**Consolidates:** v2.2 master (2026-07-28) + resolved §5 element specs + Appendix A locked project facts + Appendix B recurring-failure checklist. Where anything conflicts with an older count/phrasing, the later rule wins (§12 > §4/§7 counts; this file > chat memory).

> Any AI session, contractor, or human touching this site reads this file FIRST. No exceptions. Pages built without compliance are rejected and rebuilt. **Two items still need Anwar's confirmation — flagged `⚠CONFIRM` — do not treat as locked until confirmed.**

---

## 1. The Hard Rules (non-negotiable)
1. **No find-and-replace city swaps.** Ever. Every page written from scratch with research specific to that neighborhood/county.
2. **Real local research first.** All 7+ sources (§3) searched BEFORE writing a line of HTML.
3. **Every neighborhood, landmark, street, building, stat is REAL and LOCAL.** No invented landmarks. No stat without a source.
4. **100% unique Q&A/FAQ per page** (semantic, not just wording — §12.3). Zero duplicate intents across a silo.
5. **Title ≤ 60 characters.** Hard cap.
6. **Mandatory post-build audit (§7) before delivery.** Never skip. **Never claim PASS without a hash-verified baseline** (Appendix B).
7. **Deploy zips are cumulative** — never scattered files; **a single-file Netlify drag wipes the whole site.**
8. **GBP routing (§8) enforced on every page.** Wrong GBP = rejected.
9. **Silo cross-links on every sibling page** — service-correct, area-correct, match-area (§ Appendix A).
10. **No reuse of body content across pages** — intro, FAQ, landmarks, packages, process all rewritten per area.
11. **Fabricated content is removed, never disclaimed.** A disclaimer on top of an invented testimonial/case study/statistic is not acceptable.

---

## 2. Detection Patterns That Mean "Cloned" (auto-reject)
- File size within **±2 KB** of another page in the same silo (size-cluster = clone signature).
- **Geo-swapped donor text** — masked (geo names removed) paragraph similarity ≥ **0.65** vs any sibling/donor. Geo-swap typically lands ~0.84; every content block must be independently rewritten to **< 0.65**. (Excluded from this verdict: Service Standards block, "not legal advice" note, forms, pricing numbers, standardized equipment part-specs, shared silo-nav area descriptions.)
- Two non-sibling pages share an identical FAQ question (or intent).
- Landmarks section reuses a landmark that is geographically wrong for the page.
- Silo cross-link block links to a **different service's** siblings.
- A `*-bronx-ny.html` (or any non-Brooklyn) page contains "All 76 Brooklyn Neighborhoods" or a Brooklyn-only block.

---

## 3. Mandatory Research Sources (search BEFORE writing HTML)
| # | Source | What to extract |
|---|---|---|
| 1 | Reddit (r/[area], r/Brooklyn, r/AskNYC, r/longisland, r/hudsonvalley, r/homedefense, r/landlord…) | Real resident concerns, complaints, slang, recent incidents |
| 2 | Google PAA | Top questions for "[service] [area]" |
| 3 | Google PASF | Related/lateral queries |
| 4 | Answer the Public | Question fan-out for service+area |
| 5 | Google AI Overview (SGE) | What Google's AI claims — brands named, cost ranges, features, follow-ups, cited sources → feeds the "Reality Check" (§10.5) |
| 6 | Area landmarks | Real streets, parks, buildings, transit, campuses, corridors |
| 7 | Area-specific use cases | Dominant property/building types |
| 8 | Bing & DuckDuckGo (PAA/Related/Autocomplete) | Cross-check Google isn't the only signal |
| 9 | Local news (Patch, Brownstoner, TheCity, AMNY, Newsday, Lohud, SI Advance, Pix11, ABC7) | Recent area news in the service category |
| 10 | Hyperlocal (BK Paper/Eagle/Bay News/Caribbean Life; Bronx Times/Norwood/Riverdale; Queens Chron/Ledger; Herald-Record/Daily Freeman/Poughkeepsie Jrnl; News12 by region) | Neighborhood-level incidents/context |
| 11 | Yelp 1–3★ | Competitor pain points / what residents complain about |

Rule: if a source comes back empty, **write `EMPTY` in the research matrix — never fabricate to fill the gap.** In a build environment that cannot open a live surface (Reddit/PAA/PASF/ATP/AI-Overview/Yelp), mark it `EMPTY (not accessible in build env)` and substitute verified primary sources (local-news URLs) instead.

---

## 4. Page Structure — 22 elements, all required (fixed order + fixed eyebrow labels)
### Head + Hero (1–4)
1. **`<title>`** — `[Service] [Area] NY`, ≤ 60 chars.
2. **`<meta description>`** — 150–160 chars, area + 2 specific local hooks.
3. **`<link rel="canonical">`** — `https://www.abstractenterprisessecuritysystems.com/[slug]`. *(Static-HTML silo convention in production uses the `.html` canonical + `www`; `_redirects` serves the extensionless URL 200→`.html`; sitemap `loc` uses `.html`. Keep form `landing_page` and `.webp` URLs extensionless.)*
4. **Hero** — H1 `[Service]<br>Installation in<br><span class="ac">[Area]</span>`; pre-headline kick/badge; area-specific subhead; two CTAs (primary "Get Free Quote" + outline "Call (XXX) XXX-XXXX"); inline lead mini-form (name/phone/service/message/consent/botcheck honeypot); stats/trust row; freshness stamp matching `dateModified`.

### Body (5–20) — eyebrow → H2 pattern
| # | Eyebrow | H2 pattern | Content |
|---|---|---|---|
| 5 | THE NEIGHBORHOOD | Why [Area] Properties Need [Service] | Real local concerns (Reddit/news), building types, pain points. 3–4 paras. |
| 5.5 | (cont.) | — | 4–6 real local stats/facts. |
| 6 | WHAT WE INSTALL | [Service] Services in [Area] | 3-col service card grid, 6+ services with local context. |
| 7 | BUILDING SPECIALISTS | [Service] for [Area]'s Architecture | Building-type cards true for the area. |
| 7.5 | (cont.) | — | Material/method specifics per type. |
| 8 | COMMERCIAL [SERVICE] | Business [Service] in [Area] | 4–6 real commercial corridors + who operates there. |
| 8.5 | (cont.) | — | Compliance callouts (Building Code/FDNY/ADA) where relevant. |
| 9 | YOUR QUESTIONS ANSWERED | [Service] in [Area]: Questions Answered | H2/H3 pain-question clusters (count per §12, not fixed). 100% unique across silo. |
| 10 | EQUIPMENT | Types of [Service] We Install | Equipment grid, 6+ categories, local use cases. |
| 10.5 | AI OVERVIEW REALITY CHECK | What AI Gets Wrong About [Service] in [Area] | **800–1,200 words, 7 H3 × 3 paras.** Name real competitors (Angi/HomeAdvisor/Fixr); quote AI claim then correct with local field reality. |
| 11 | GET IN TOUCH | Request a Free Quote | Full quote form (name/phone/email/service/message/consent). |
| 12 | HOW IT WORKS | Our Installation Process | 4–8 numbered steps. |
| 13 | COVERAGE AREA | [Service] Near [Area]'s Landmarks | 6 real landmark cards + "we also serve [adjacent areas]". |
| 14 | PRICING | [Service] Cost in [Area] | Pricing drivers/table; area multiplier (§9). |
| 15 | SHOP OUR SYSTEMS | [Service] Packages & Pricing | 3 package cards (starter/standard/premium) with $ (§9 multiplier). |
| 15.5 | (cont.) | — | BYOE labor-only callout. |
| 16 | COMPLETE SERVICES | Every [Service] Service in [Area] | Grid linking to related services — **match-area** (§ Appendix A). |
| 17 | FAQ | [Area] [Service] FAQ | Accordion; **different intents from §9**; 8–12 typical (§12: only valuable, non-duplicated questions). |
| 18 | FAQ Schema | (no visible H2) | `FAQPage` JSON-LD — must match §17 **exactly** (same set, answers, count). |
| 19 | ALL AREAS SERVED | [Service] Across [Region] | Silo cross-link block — **same-service** siblings only; hub-and-spoke correct. |
| 20 | Footer + GBP | — | NAP per §8; `LocalBusiness` schema; social links. |

---

## 5. Advanced Elements (21–41) — 37-element blueprint (RESOLVED)
> Reconciles the v2.1 additions with current build conventions. Numbers marked **pending** are genuinely undefined; everything else is locked and in use.

| # | Element | Spec (locked unless noted) |
|---|---|---|
| 21 | **Field Notes** | 150–250-word installer-voice sidebar with a real, area-specific install anecdote (no fabricated stories). |
| 22 | **Author / Person schema** | `Person` for Anwar Timothy with NYS Low-Voltage License #12000287431 + social profiles. |
| 23 | **Anchor diversity** | Internal-link anchor mix ≈ **40/30/20/10** (branded / exact-match / partial / generic). |
| 24 | **Freshness stamp + changelog** | Visible "Reviewed and updated [Month D, YYYY]" matching schema `dateModified`; changelog note. |
| 25 | **Comparison subsections** | "[National brand] vs local" — **ADT / Ring / SimpliSafe** vs AESS, inside §10/§14 as relevant. |
| 26 | **Embedded YouTube short** | 30–60s area install short (source = @openeye0007) where available. |
| 27 | **Schema stack** | `Service` + `AggregateRating` + `HowTo` JSON-LD alongside `FAQPage`. Full parking-silo stack = **6 blocks**: LocalBusiness, Service, BreadcrumbList, HowTo, ImageObject `@graph` (11×), FAQPage. |
| 28 | **Off-page checklist** | Per-page off-page/citation checklist delivered with the page. |
| 29 | **PAA quarterly rescrape** | Re-scrape PAA/PASF quarterly; refresh Q&A/FAQ + freshness stamp. |
| 30 | **Instant qualifier micro-form** | Above-fold micro-form (fast qualify → full form). |
| 31 | **Alt + filename SEO** | Every image: descriptive **keyword + geo** alt/title AND slug-style filename matching service+area; unique per image; **never** replace with generic scene descriptions. |
| 33 | **Alt + filename SEO (kw + geo)** | (duplicate of 31 in older numbering — treat as one rule.) |
| 34 | **Instant Action Block** | Under the intro: click-to-call + "Quote in 60 sec" + 3 trust bullets. |
| 36 | **Emergency / Repair Capture** | "Need Repair in [Area]?" — same-day, "fixed in 1–2 hrs" — placed early-mid AND near final; repair/emergency pages get a top red banner. |
| 38 | **Mid-Page CTA Reinforce** | Secondary CTA after §10.5 and after §14: Call Now / Fast Quote / Speak to a Tech. |
| 39 | **Cross-Sell** | In §5, §7, §18: "most [area] [property] pair this with access control" (or the relevant adjacent service). |
| 27a | **Sticky Instant Action bar** | Floating "Call / Text / WhatsApp" action bar. |
| 28a | **Emergency banner** | Top-of-page red banner on emergency/repair pages only. |
| 35, 37, 40, 41 | **pending** | Not yet defined — do not invent. |

---

## 6. Title & Meta Constraints
- `<title>` **≤ 60 chars** (hard). `<meta description>` **150–160 chars**. H1 contains service + area, not an exact copy of `<title>`. **Exactly one H1**; all else H2/H3. Canonical uses `www` (production static silo uses `.html`; see §4).

---

## 7. Mandatory Post-Build Audit (run BEFORE delivery)
- [ ] Elements 1–20 (incl. .5 subsections) present in `<head>`, hero, and body.
- [ ] Title ≤ 60 chars.
- [ ] **Exactly one H1**; `<section>`/`<div>`/`<details>` tags all balanced (rewrites drop closers — re-verify after every section resplice).
- [ ] Silo cross-link block (§19) links only to same-service siblings; hub-and-spoke + match-area correct.
- [ ] Keyword coverage checked (complete approved list across the silo, natural placement; correct geo modifier only on its own page).
- [ ] §9 Q&A and §17 FAQ have **zero duplicate intents** (semantic, geo-masked) across silo.
- [ ] Every neighborhood/landmark/street REAL and verifiable.
- [ ] **All JSON-LD parses; entity-free (Unicode only — no `&mdash;`/`&#39;`/`&amp;` inside JSON-LD).**
- [ ] **FAQ schema (§18) matches visible FAQ (§17) exactly — question set AND answers AND count.**
- [ ] **HowTo steps == HOW IT WORKS step count** (parking silo); AggregateRating present (schema stack).
- [ ] Sitemap entry added (once, `.html`, hub 0.9/weekly · child 0.7/monthly); `</urlset>` tail intact + XML valid.
- [ ] `_redirects` clean-URL 200 rule added; **stale 301s pointing new slugs to old pages deleted.**
- [ ] Mega-nav (`js/mega-nav.js`) entry added; `node -c` OK.
- [ ] Canonical correct (www, `.html`) and matches sitemap `loc`.
- [ ] GBP schema matches §8 routing; phone matches §8 phone routing.
- [ ] File-size cluster check — **not within ±2 KB of any sibling**.
- [ ] All images referenced actually resolve on disk; alt/title keyword+geo, unique per image.
- [ ] Rendered QA (Playwright, `python3 -m http.server`): 1440×900, 768×1024, 390×844.
- [ ] All applicable v2.1/v2.2 advanced elements (§5) present.

---

## 8. GBP + Phone Routing (mandatory)
**Brooklyn GBP** — 1282 Troy Ave, Brooklyn NY 11203 (#brooklyn entity) — serves: **NYC hub, Brooklyn, Staten Island, Long Island (Nassau + Suffolk)**. SEO phone **(347) 934-8335**.
**Bronx GBP** — 460 E Fordham Rd, Bronx NY 10458 (#bronx entity) — serves: **Bronx, Manhattan, Queens, all 6 Hudson Valley counties (Westchester, Rockland, Orange, Putnam, Dutchess, Ulster)**. Hudson Valley SEO phone **(845) 640-3835** (HV county pages use 845 **exclusively — zero 347**).
- Homepage + Bronx GBP contact context: **(800) 486-0943** (emergency line — **never** on SEO pages).
- WhatsApp shared line **(718) 679-0359** — **never** on SEO pages except as the WhatsApp CTA (`wa.me/17186790359`).
- Protect the string **"Fordham"** from any geo-swap map (it is the Bronx GBP street address).
- Two separate GBPs are intentional (linked-account suspension risk) — never cross-link them.
- Wrong GBP or wrong phone on a page = rejected.

---

## 9. Area Pricing Multipliers (Brooklyn base = 1.00×)
| Area | × | Area | × |
|---|---|---|---|
| Brooklyn | 1.00 | Suffolk | 1.20 |
| Bronx | 1.00 | Westchester | 1.25 |
| Queens | 1.05 | Rockland | 1.30 |
| Staten Island | 1.10 | Orange | 1.40 |
| Nassau | 1.15 | Putnam | 1.45 |
| Manhattan | 1.25 | Dutchess | 1.53 |
| | | Ulster | 1.53 |
Parking-silo package base (Brooklyn) = **850 / 1,500 / 2,500 / 2,800 / 4,500**; multiply, round half-up (only non-integer products round). **Never invent prices.**
Service/callback rate (protected, verbatim): **$195/hr, 3-hr minimum ($585)** — not on the initial install. Camera-calculator labor-only multipliers apply to the **labor** component (equipment locked at Lorex/street price across areas).

---

## 10. Process — How a Page Gets Built
1. Confirm slug, service, area, GBP + phone routing. **Hash-verify the working baseline** (os.walk + hashlib.sha256) before edits.
2. Run all 7+ sources (§3) → research-matrix notes. **No HTML yet.**
3. Confirm sufficiency; mark any `EMPTY` honestly.
4. Draft 100% unique body per §4/§5. No sibling reuse.
5. Write HTML (canonical structure). Count-guard every scripted replace (grep + assert count before replace).
6. Register: sitemap, `_redirects`, mega-nav, cross-links (hub↓children, child↑hub, match-area).
7. Run the full §7 audit + rendered QA.
8. Package the deliverable (§12.8) — verify ZIP integrity + SHA-256 + bytes.
9. Deliver with the PASS evidence (§12.8) and note any incomplete silo.

---

## 11. NOT Part of the Blueprint (and never has been)
- "All 76 Brooklyn Neighborhoods" block on a non-Brooklyn page. Reusing the Bay Ridge body anywhere. Linking the wrong service silo. Placeholder phone/address/license. Skipping research because an area seems "small/obvious." Disclaiming (rather than removing) fabricated content.

---

## 12. v2.2 Rules — Pain-Question Coverage, Structure, De-Dup, Research Matrix, Keywords
Where this conflicts with an older count/phrasing, **§12 wins.**
- **12.1 Pain-question coverage** — no fixed number; answer every relevant unique pain question from §3. Combine same-intent questions; never manufacture questions to hit a number.
- **12.2 Structure** — H2 per major intent cluster (e.g. Cost & Planning; Placement/Coverage/Blind Spots; License-Plate & Entrance; Wiring/Wireless/Pole; Recording/Storage/Remote; Theft/Vandalism/Liability; Repairs/Upgrades/Existing). H3 questions answered **immediately**. Supporting questions answered naturally in body. **Important answers must be visible — never only in schema.**
- **12.3 No duplicated questions/answers (semantic)** — compare all H2/H3/body/FAQ/schema **by meaning**; one intent answered once per page. Visible FAQ holds only questions not already fully answered; `FAQPage` matches visible exactly. Compare pages **after masking geo names** — must be genuinely area-specific, not swapped prose.
- **12.4 Research matrix (per area)** — for every source: **exact query searched · platform · exact URL when available · finding · page+section used.** Never "query that would be run." Unretrievable → **`EMPTY`**. Never invent results/URLs/quotes/stats/landmarks/stories. Every relevant pain question maps to a visible answer on the correct page.
- **12.5 Keyword coverage** — complete approved list across the silo, natural placement; no stuffing/hidden text; correct geo modifier only on its own page; image alt/title stay keyword+geo. Produce a **keyword-coverage report** (keyword · page · section · exact sentence/heading/attr · occurrences) accounting for the complete list; unusable keyword → report for review, don't stuff/omit.
- **12.6 Protected approved content (never remove/rewrite)** — Same-Day Estimates · 100% Licensed & Insured · pricing + §9 multipliers · BYOE pricing · warranty language · service rates · license number · phone numbers · addresses + GBP routing · forms · canonicals · image tags · existing valid links. No unrelated design/content changes.
- **12.7 Linking & tech (every delivery)** — correct parent hub; correct siblings; no wrong-area link; nav includes correct pages; sitemap lists every live page once; `_redirects` clean-URL rule present; canonicals correct; no broken links/orphans/placeholders; visible FAQ == `FAQPage`; all JSON-LD parses; exactly one H1; forms + responsive layouts work.
- **12.8 Delivery + PASS evidence** — work from current repo base; deliver **one changed-files ZIP** (new/modified files at correct relative paths); before claiming PASS provide: (1) files changed; (2) pain-question→page/section map; (3) keyword-coverage map; (4) semantic-dup results; (5) research-matrix completion; (6) link/nav/sitemap/redirect/canonical results; (7) schema-validation results; (8) confirmation no unrelated protected content changed. **Never claim PASS if any question is missing, duplicated, vague, wrong-area, unsupported, or schema-only.**

---

## Appendix A — Locked Project Facts

**Domains** — primary `abstractenterprisessecuritysystems.com` (full site); secondary `abstractcameranewyork.net` (CCTV-only, dark navy, phone (929) 730-5331, lead-form only). Canonical domain string on primary: `www.abstractenterprisessecuritysystems.com`.

**Forms** — Web3Forms key `88890030-1770-483e-a622-0e054d8e14b1`. Two forms per page (hero + detail; sf1-/sf2- or form-hero/form-detail): accessible status line, consent checkbox, botcheck honeypot, extensionless `landing_page`.

**Warranty / rate / rating** —
- SEO-page warranty language (protected, verbatim): **three-year warranty on AESS-supplied products** for normal wear/tear, with verbatim exclusions (existing/customer wiring, customer-supplied equipment, acts of God, power surges, physical damage/unplugging, internet/router/phone changes, **post-completion camera readjustments**); links to `/warranty`.
- Service/callback: **$195/hr, 3-hr min ($585)**.
- Page rating display (locked): **★ 4.7 · 201 Google Reviews** (ratingValue 4.7 / reviewCount 201). ⚠CONFIRM: GBP profiles read Brooklyn 4.6/190 and Bronx 4.7/170 — confirm whether pages should show the routed GBP's numbers or keep the 4.7/201 aggregate.
- Master service contract warranty (separate legal doc, not the page language): **1-yr parts-only**; 50% deposit + immediate final; conduct-based acceptance; $195/hr specialty rate; late fees $50/day+1.5%/mo cap 25%; liability capped at amount paid.

**Camera brands** — Lorex (U/V/X), Dahua, Hikvision, Uniview (UNV), Aiphone, ButterflyMX, 2N, Akuvox, Comelit, DoorBird, TVT (Super Live Plus). Uniview model numbers are standardized product specs — preserve verbatim. Confirmed real Lorex image bases: lorex-4k-bullet, lorex-4k-turret, lorex-4k-turret-dome, lorex-bullet-spotlight, lorex-color-night-vision-turret, lorex-dual-floodlight, lorex-video-doorbell, lorex-wifi-ptz (`lorex-smart-deterrence` is NOT real). Generic unbranded: cam-eyeball-white, cam-turret-side, cam-eyeball-ir.

**Silo template (16 pages/service)** — NYC hub + Brooklyn/Manhattan/Queens/Bronx/Staten Island + LI hub + Nassau/Suffolk + HV hub + Westchester/Rockland/Orange/Putnam/Dutchess/Ulster. Non-NYC pages replace landlord Q&A with residential/commercial. LocalBusiness schema `url` follows the silo's own convention (recent parking pages use the page's own URL) — keep it consistent within a silo rather than making one page an outlier.

**Hub-and-spoke + cross-link rules** —
- Every area child links **UP** to its regional hub (borough→NYC, Nassau/Suffolk→LI, HV county→HV). Every regional hub links **DOWN** to all children AND **UP** to Home.
- Silo footer cross-links all 16.
- **Match-area:** area pages link to their matching-area counterpart, never a different area's page. When a new silo page ships, immediately repoint that area's install/repair/brand/app pages and the hub-fallback links across siblings + hub to the new page (flip coming-soon `/free-quote` anchors to the live page).
- Five keyword layers to plan each page: Service · Problem · Technology · Industry · Geographic.

**Delivery format (every build)** — one changed-files ZIP + live URL + one-line stats + **SHA-256 + "verify downloaded size"**, in one message. Delete the prior ZIP from outputs first; only the current ZIP is present. Verify ZIP integrity before sending. Deploy = merge changed files into the local baseline tree, then re-zip the **full** site for Netlify (partial drag wipes the site).

**Tooling** — Netlify (drag-drop cumulative ZIP) · GitHub Desktop only (C:\dev\abstract-enterprises-site, account support677) · Housecall Pro (reviews) · Playwright + `python3 -m http.server` for rendered QA. Upload cap ~341 MB: split a full-site ZIP into raw 7-Zip byte-chunks (.001/.002) or strip `images/` for a lightweight source archive.

---

## Appendix B — Recurring-Failure Checklist (hard-won)
- **Never claim PASS before a hash-verified baseline.** Ask for the latest deployed ZIP if repo/deploy state can't be independently confirmed.
- **Geo-swap ≈ 0.84 masked similarity** → rewrite every block; ceiling **< 0.65**.
- **Section/div resplice drops closers** — the ai-overview + field-notes blocks lose a closing `</div>`/`</section>` on resplice; verify tag balance (not just div) after every rewrite.
- **Sitemap tail corruption** — inserting content can eat the `<` of `</urlset>`; verify the tail + XML validity after any sitemap edit.
- **Single-file Netlify drag wipes the site** — always the full cumulative ZIP for deploy.
- **Working baseline = the previously deployed Netlify ZIP**, never the local repo.
- **Stale 301s have 404'd silos** — on every silo page ship, delete stale 301s pointing new slugs to old pages.
- **Google cache lags rebuilds** — verify against the live URL, not the SERP snippet.
- **Rep() discipline** — grep current text, assert count, then replace (a failed script loses its reps).
- **FAQ schema drifts from visible** — regenerate `FAQPage` from the visible FAQ as the last content op; match questions AND answers.
- **All JSON-LD must be Unicode** (no HTML entities).
- **Dahua install donor bugs** — 3 in-hero DMSS anchors mis-wire to `/security-camera-repair-[area]` (correct: `/dmss-app-support-repair-[area]` or hub fallback); the "Dahua Across NYC" sibling grid mis-wires every borough label to `/dahua-camera-installation-nyc` (correct: each label→its own slug). Fix on every new/cloned Dahua page before delivery.
- **`dvr-upgrade-orange.html`** — filename "orange" (not "orange-county") slips the HV phone filter; force 845 explicitly.
- **NYPD crime-data citations** — keep only on the six NYC solar pages; remove elsewhere. **Palisades Center = Rockland, not Westchester.**

*End of full blueprint. Edit this file directly to evolve the spec — do not rely on memory or chat history.*
