# Abstract Enterprises Site — Page Blueprint

**Owner:** Anwar Timothy
**Status:** v2.1 (canonical, single source of truth)
**Scope:** every service × area page on `abstractenterprisessecuritysystems.com`
**Last revised:** 2026-05-07

> Any AI session, contractor, or human touching this site reads this file FIRST. No exceptions. Pages built without compliance to this blueprint are rejected and rebuilt.

---

## 1. The Hard Rules (non-negotiable)

1. **No find-and-replace city swaps.** Ever. Every page is written from scratch with research specific to that neighborhood/county.
2. **Real local research first.** All 7+ research sources (§3) must be searched BEFORE writing a single line of HTML. No exceptions.
3. **Every neighborhood, landmark, street, building, and stat must be REAL and LOCAL.** No invented landmarks. No stat that didn't come from a source.
4. **100% unique Q&A/FAQ per page.** Zero duplicate questions across pages in the same silo. Every answer written from scratch.
5. **Title ≤ 60 characters.** Hard cap.
6. **Mandatory post-build audit (§7) before file delivery.** Never skip.
7. **Cumulative deploy zips.** Pages ship as `site-rebuild-N.zip`, never as scattered files.
8. **GBP routing (§8) is enforced on every page.** Wrong GBP = page rejected.
9. **Silo cross-links on every sibling page.** Service-correct, area-correct. No wrong-service blocks.
10. **No reuse of body content across pages**, including the "Why X Properties Need Y" intro, FAQ, landmarks, packages, or process — all rewritten per neighborhood.

---

## 2. Detection Patterns That Mean "Cloned" (auto-reject)

A page is rejected if any of these are true:

- File size within ±2KB of another page in the same silo (size-cluster = clone signature).
- Two non-sibling pages share an identical FAQ question.
- Landmarks section reuses a landmark on a page where that landmark is geographically wrong.
- A page's silo cross-link block links to a different service's siblings (e.g. fire-alarm page linking to alarm-installation siblings).
- A page named `*-bronx-ny.html` contains "All 76 Brooklyn Neighborhoods" or any Brooklyn-only block.

---

## 3. Mandatory Research Sources (search BEFORE writing HTML)

Search all of these for the specific neighborhood/county before drafting:

| # | Source | What to extract |
|---|---|---|
| 1 | Reddit (r/[neighborhood], r/Brooklyn, r/AskNYC, etc.) | Real resident concerns, complaints, slang, recent incidents |
| 2 | Google PAA (People Also Ask) | Top 8-12 questions for "[service] [neighborhood]" |
| 3 | PASF (People Also Search For) | Related queries / lateral keywords |
| 4 | Answer the Public | Question fan-out for service+area |
| 5 | AI Overview (Google SGE) | What Google's AI says about the topic — write a "Reality Check" section |
| 6 | Area landmarks | Real streets, parks, buildings, transit, schools, military bases |
| 7 | Area-specific use cases | What types of buildings/properties dominate (row houses, co-ops, brownstones, ranches, estates, commercial strips) |
| 8 | Bing & DuckDuckGo (v2.1) | Cross-check that Google isn't the only signal |
| 9 | Local news outlets (v2.1) | Recent news mentioning the neighborhood/service category |
| 10 | Hyperlocal outlets (v2.1) | Patch, BKReader, Bronx Times, neighborhood blogs |
| 11 | Yelp reviews (v2.1) | What residents complain about / praise re: similar services |

Rule: if any of these comes back empty for the neighborhood, document it in the page draft notes — don't fabricate to fill the gap.

---

## 4. Page Structure — v2.0 Spec (22 elements, all required)

Section order is fixed. Section labels (the small uppercase eyebrow text above each H2) are fixed. Content inside each section is unique per page.

### Head + Hero (elements 1–3)

1. **`<title>`** — `[Service] [Neighborhood] [Borough] NY`. ≤ 60 chars.
2. **`<meta description>`** — 150-160 chars, must mention the neighborhood + 2 specific local hooks (e.g. "row houses, co-ops").
3. **`<link rel="canonical">`** — `https://www.abstractenterprisessecuritysystems.com/[slug]` (no trailing slash, no `.html`).

### Hero Section (element 4)

H1 format: `[Service]<br>Installation in<br><span class="ac">[Neighborhood]</span>`
Hero includes:
- Pre-headline badge (e.g. "TRUSTED LOCAL INSTALLER")
- Subhead (1.12rem, max 640px) — neighborhood-specific value prop
- Two CTAs side-by-side: primary (red) "Get Free Quote", outline "Call (XXX) XXX-XXXX"
- Inline lead-capture mini-form on the right (name, phone, service dropdown, message, SMS consent checkbox, submit)
- Stats bar (4 cells): `25+` Years Experience · `✓` Same-Day Estimates · `100%` Licensed & Insured · `$0` Monthly Fees

### Body Sections (elements 5 through 20)

Sections appear in this order. Eyebrow label / H2 title pattern shown:

| # | Eyebrow | H2 pattern | Required content |
|---|---|---|---|
| 5 | `THE NEIGHBORHOOD` | "Why [Neighborhood] Properties Need [Service]" | Real local concerns from research (Reddit/news). 3-4 paragraphs. Reference specific building types and resident pain points. |
| 5.5 | (cont.) | (subsections inside §5) | Bullet list of 4-6 real local stats / facts. |
| 6 | `WHAT WE INSTALL` | "[Service] Services in [Neighborhood]" | 3-column service card grid (.sc): 6+ specific services with neighborhood-relevant context. |
| 7 | `BUILDING SPECIALISTS` | "[Service] for [Neighborhood]'s Architecture" | Building-type cards (.cc): row houses, co-ops, brownstones, ranches, multi-family — whatever's true for the area. |
| 7.5 | (cont.) | (subsections inside §7) | Material/method specifics per building type. |
| 8 | `COMMERCIAL [SERVICE]` | "Business [Service] in [Neighborhood]" | Commercial block: name 4-6 real local commercial corridors, what businesses operate there. |
| 8.5 | (cont.) | (subsections inside §8) | Compliance callouts (NYC Building Code, FDNY, ADA) where relevant. |
| 9 | `YOUR QUESTIONS ANSWERED` | "[Service] in [Neighborhood]: Questions Answered" | 12-14 H2 sub-questions, each with 2-3 sentence answer. All neighborhood-specific. **100% unique across silo.** |
| 10 | `EQUIPMENT` | "Types of [Service] We Install" | Equipment grid (.sc): 6+ equipment categories with neighborhood-relevant use cases. |
| 10.5 | `AI OVERVIEW REALITY CHECK` | "What AI Gets Wrong About [Service] in [Neighborhood]" | **800–1,200 words.** 7 H3 subsections. Each H3 has 3 paragraphs. Quote the AI Overview claim, then correct it with local field reality. |
| 11 | `GET IN TOUCH` | "Request a Free Quote" | Full quote form (name, phone, email, service, message, SMS consent). |
| 12 | `HOW IT WORKS` | "Our Installation Process" | Numbered process cards (.pc): 4-6 steps. Dark section (.sd). |
| 13 | `COVERAGE AREA` | "[Service] Near [Neighborhood]'s Landmarks" | Landmark cards (.lcard): 6 real landmarks with 1-line description each. Plus a "We also serve [4 adjacent neighborhoods]" line. |
| 14 | `PRICING` | "[Service] Cost in [Neighborhood]" | Pricing table or 3-card pricing grid. Local pricing (use area multiplier — see §9). |
| 15 | `SHOP OUR SYSTEMS` | "[Service] Packages & Pricing" | 3 package cards: starter / standard / premium with $ amounts. |
| 15.5 | (cont.) | (subsections inside §15) | BYOE labor-only option callout where applicable. |
| 16 | `COMPLETE SERVICES` | "Every [Service] Service in [Neighborhood]" | Dark section grid linking out to related services on this site. |
| 17 | `FAQ` | "[Neighborhood] [Service] FAQ" | 8-12 FAQ items in accordion (.fc/.fi). **Different from §9.** |
| 18 | `FAQ Schema` | (no visible H2) | `application/ld+json` `FAQPage` schema reflecting §17 questions. |
| 19 | `ALL AREAS SERVED` | "[Service] Across [Borough] Neighborhoods" | Silo cross-link block — links ONLY to other [same service] [same borough] pages (sibling-correct). |
| 20 | (footer + GBP) | — | Footer with NAP (per §8 routing), GBP schema (`LocalBusiness`), social links. |

---

## 5. v2.1 Additions (elements 21–39)

These are added on top of the v2.0 structure. Some still have unconfirmed specs — flagged below. **Anwar to review and confirm specs before I treat them as locked.**

| # | Element | Spec status |
|---|---|---|
| 21 | **Field Notes** — short technician sidebar/callout with a real install anecdote from this neighborhood | spec needs confirmation |
| 22 | **Author / Person schema** — `Person` schema for Anwar with credentials, license # | spec needs confirmation |
| 23 | **Freshness stamp** — visible "Updated [Month YYYY]" + `dateModified` in schema | confirmed |
| 24 | **Comparison subsections** — "[Service] vs [Alternative]" comparison table inside §10 | spec needs confirmation |
| 25 | **Embedded YouTube short** — silent autoplay neighborhood install short, 30-60s | spec needs confirmation (URL source TBD) |
| 26 | **Schema stack** — `Service` + `AggregateRating` + `HowTo` JSON-LD blocks alongside `FAQPage` | confirmed structure, ratings source TBD |
| 27 | **Instant Action Block** — sticky "Call now / Text now / WhatsApp" floating action bar | confirmed |
| 28 | **Emergency / Repair Capture** — top-of-page red banner for emergency repair pages only | confirmed |
| 29 | **Mid-page CTA reinforce** — secondary CTA between §10 and §11 | confirmed |
| 30 | **Cross-sell signals** — sidebar/inline "Customers in [Neighborhood] also got [Other Service]" | spec needs confirmation |
| 31 | **Alt + filename SEO** — every image has descriptive alt + slug-style filename matching service+neighborhood | confirmed |
| 32 | (reserved) | — |
| 33 | (reserved) | — |
| 34 | (reserved) | — |
| 35 | **TBD** | pending |
| 36 | (reserved) | — |
| 37 | **TBD** | pending |
| 38 | (reserved) | — |
| 39 | (reserved) | — |
| 40 | **TBD** | pending |
| 41 | **TBD** | pending |

---

## 6. Title & Meta Constraints

- `<title>` **≤ 60 chars** — hard cap. Audit fails if over.
- `<meta description>` **150-160 chars** — under 150 is too short, over 160 truncates in SERP.
- H1 must contain the service + neighborhood (no exact duplication of `<title>`).
- One H1 per page. Every other heading is H2 or H3.
- Canonical URL must use `www.` and must NOT include `.html`.

---

## 7. Mandatory Post-Build Audit (run BEFORE delivery)

Audit fails any of these → page goes back to rebuild, not to deploy:

- [ ] Elements 1, 2, 3 present in `<head>` and hero
- [ ] Elements 4, 5, 5.5, 6, 7, 7.5, 8, 8.5, 9, 10, 10.5, 11, 12, 13, 14, 15, 15.5, 16, 17, 18, 19, 20 visible in body
- [ ] Title ≤ 60 chars
- [ ] Silo cross-link block (§19) links only to same-service, same-borough siblings
- [ ] 87 keywords × 3 geo modifiers density check passed
- [ ] FAQ (§17) and Q&A (§9) have ZERO duplicate questions across silo
- [ ] Every neighborhood/landmark/street is REAL and verifiable
- [ ] FAQ schema (§18) matches FAQ section (§17)
- [ ] Sitemap entry added
- [ ] Mega-nav dropdown entry added
- [ ] Canonical correct (www, no .html)
- [ ] GBP schema matches §8 routing for this area
- [ ] Page passes file-size cluster check (not within ±2KB of any sibling)
- [ ] All v2.1 elements that apply to this page type are present

---

## 8. GBP Routing (mandatory)

Brooklyn GBP (1282 Troy Ave, 11203) handles:
- NYC hub pages
- Brooklyn (all 76 neighborhoods)
- Staten Island
- Long Island (Nassau + Suffolk)

Bronx GBP (460 E Fordham Rd) handles:
- Bronx (all neighborhoods)
- Manhattan (all neighborhoods)
- Queens (all neighborhoods)
- ALL Hudson Valley counties (Westchester, Rockland, Orange, Putnam, Dutchess, Ulster)

Wrong GBP on a page = rejected.

---

## 9. Area Pricing Multipliers (relative to Brooklyn base = 1.00×)

| Area | Multiplier | Notes |
|---|---|---|
| Brooklyn | 1.00× | base |
| Bronx | 1.00× | parity |
| Manhattan | 1.25× | high cost / access |
| Queens | 1.05× | |
| Staten Island | 1.10× | Verrazano surcharge |
| Long Island (Nassau) | 1.15× | |
| Long Island (Suffolk) | 1.20× | |
| Westchester | 1.25× | |
| Rockland | 1.30× | |
| Orange | 1.40× | West Point/Stewart Airport |
| Putnam | 1.45× | rural-luxury estates |
| Dutchess | 1.53× | IBM cleanroom protocols |
| Ulster | 1.53× | Woodstock audiophile baseline |

---

## 10. Process — How a Page Gets Built

1. **Receive URL.** Confirm slug, service, neighborhood, area, GBP routing.
2. **Run all 7+ research sources (§3).** Save findings to a local notes block. No HTML yet.
3. **Confirm research is sufficient.** If any source came back empty, document it.
4. **Draft body content per element spec (§4 and §5).** 100% unique. No reuse from sibling pages.
5. **Write HTML** following the canonical structure.
6. **Run post-build audit (§7) end to end.**
7. **Add to cumulative deploy zip** (`site-rebuild-N.zip`).
8. **Deliver to Anwar with the audit checklist filled in.**

---

## 11. Things That Are NOT Part of the Blueprint (and never have been)

- "All 76 Brooklyn Neighborhoods" link block on a non-Brooklyn page.
- Reusing the Bay Ridge body on any non-Bay-Ridge page.
- Linking the wrong service silo (e.g. fire-alarm page linking to alarm-installation siblings).
- Using a placeholder phone number, address, or license number.
- Skipping research sources because the neighborhood is "small" or "obvious."

---

*End of blueprint. Edit this file directly to evolve the spec — do not rely on memory or chat history.*
