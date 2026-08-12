# site-rebuild-137 — Low voltage silo (6 pages) + sitewide phone routing

**Baseline:** site-rebuild-135. No GitHub, no Netlify, no deploy. **1050 changed and new files.**

---

# Pages in this build

| Page | Phone | GBP | Role |
|---|---|---|---|
| Low Voltage Installation NYC | (800) 486-0943 | Brooklyn | hub |
| Low Voltage Installation Long Island | (800) 486-0943 · Nassau 516 · Suffolk 631 in contact block | Brooklyn | hub |
| Low Voltage Installation Hudson Valley | (800) 486-0943 · Westchester 914 · HV 845 in contact block | Bronx | hub |
| Low Voltage Installation Manhattan | (929) 560-0737 | Bronx | child |
| Low Voltage Installation Brooklyn | (347) 934-8335 | Brooklyn | child |
| **Low Voltage Installation Queens** | **(347) 434-6392** | **Bronx** | **child — new** |

All six: 20 sections, 7 JSON-LD blocks, 14 images, 13–14 Q&A, 12 FAQ mirrored exactly in FAQPage schema, AI Overview Reality Check at 7 H3 x 3 paragraphs, 3 Web3Forms, instant action block, 60-second qualifier, 2 CTA strips, 2 repair captures.

**Zero duplicate questions across all fifteen page pairs.**

---

# Queens — the differentiator

Every other page in this silo describes work inside a finished building. **Queens is the borough where a large share of the work happens before the walls close**, and the page is built on that.

The pipeline is real: the OneLIC Neighborhood Plan rezones 54 blocks of the Long Island City waterfront with an estimated **15,000 apartments** over a decade and roughly **3.5 million square feet** of new commercial, office and retail space. Hunters Point South continues building out its 30-acre master plan.

What that gives the page, and what no other page in the silo carries:

- **Rough-in as the defining stage** — cable before drywall, priced closest to the published figures because there is no fishing, coring or making good.
- **Trade sequencing** — low voltage as one sub among several, following the electricians and preceding drywall, where slipping costs the next trade too.
- **The signature Queens failure: walls closing with nothing in them**, because the low-voltage scope was never named in the schedule. A coordination failure, not a technical one, and the most avoidable line item in the borough.
- **Spare conduit capacity** — nearly free at rough-in, expensive forever after, and invisible in any per-drop price model.
- **Cabling from drawings**, with discrepancies raised on paper rather than discovered at rough-in.
- **Queens as several markets** — an LIC tower, a Maspeth warehouse, a Flushing medical suite above retail and a Jamaica community facility have almost nothing in common as jobs.

Neighbourhood specificity throughout: Long Island City, Hunters Point, Jackson Avenue, Queens Plaza, Astoria, Steinway Street, Flushing, Main Street, Roosevelt Avenue, Jamaica, Sutphin Boulevard, 165th Street, Maspeth, Ridgewood and the JFK perimeter.

---

# Dedup — the closest call in the silo so far

The first Queens build shared **14 long paragraphs and 7 question strings with Brooklyn** — the highest overlap between any two pages in this project. Both are outer-borough commercial pages with similar service grids, and Brooklyn was the nearest template to hand.

**Eight paragraphs and seven questions were rewritten.** Final state: 7 shared paragraphs, all approved sitewide boilerplate and "Related:" link lines, and zero duplicate questions across all fifteen pairs.

**Flag for the next build:** the Bronx page carries the same risk, because Bronx industrial and Queens industrial invite identical vocabulary. Build it from Hunts Point and the Industrial Business Zone rather than from the Queens or Brooklyn file, and run the pairwise check against both before delivery.

---

# Sitewide phone routing

| Area | Number | Pages |
|---|---|---|
| Hub pages (`-nyc`, `-long-island`, `-hudson-valley`) | (800) 486-0943 | 117 |
| Brooklyn | (347) 934-8335 | 654 |
| Bronx | (646) 490-0629 | 611 |
| Queens | (347) 434-6392 | 46 |
| Nassau | (516) 346-5778 | 44 |
| Suffolk | (631) 407-2884 | 44 |
| Manhattan | (929) 560-0737 | 44 |
| Westchester | (914) 877-2578 | 43 |
| Staten Island | (347) 934-8335 | 43 |
| Rockland / Orange / Putnam / Dutchess / Ulster | (845) 640-3835 | 207 |
| WhatsApp, all pages | (718) 679-0359 | — |

**Watch after deploy:** Westchester Square and Westchester Heights are Bronx neighbourhoods. An earlier pass mis-scoped 16 such pages before the matcher was corrected to give borough names precedence.

**No CallRail swap script exists on the site**, so these are static and hardcoding is correct.

---

# QA — all pass on all six pages

20 sections each · titles under 60 · metas 150–160 · single H1 · 7 JSON-LD blocks parsing · 14 images each with unique area-bearing alts and titles, alt never equal to title, all assets on disk · 13–14 Q&A · FAQ 12 == schema 12 exact · AI Overview 800–1,200 words across 7 H3 · balanced div and section counts · 3 Web3Forms each · approved pricing, warranty and BYOE preserved · zero broken internal links · zero duplicate questions across all fifteen pairs · zero cross-area content leakage.

Rendered at 390x844 on all six: zero blank images, zero horizontal overflow.

---

## Still open

1. **`(555) 123-4567` placeholders live on deployed pages** — Manhattan and Queens camera pages, a Brooklyn door buzzer page. Active lead leak.
2. **`300 Cadman Plaza West`** in schema on 166 Brooklyn pages, not in any routing rule on file.
3. **10 silo child pages unbuilt** — Bronx, Staten Island, Nassau, Suffolk, and the six Hudson Valley counties. Westchester and Rockland carry the county-level search volume in the Hudson Valley.

**Nothing invented.** Licensing and permit statements cite the NYC Administrative Code, Suffolk County Code, Westchester County licensing materials and City of Yonkers permit materials. They are marked general information rather than legal advice.

---

## Addendum — Queens term sets applied

16 PAA questions and 26 related terms supplied after the build and audited against the page. **All 26 verified present — zero insertions required.** This is the first area page in the project to need no post-build term remediation, because it was built against the pattern rather than retrofitted to it.

### The Brooklyn neighbourhood prediction is confirmed

The Brooklyn build flagged that Queens was the borough most likely to repeat Brooklyn's sub-borough search pattern, and the coverage sections were built at neighbourhood level in anticipation. The supplied Queens set produced exactly that: **Astoria, Long Island City, Flushing, Jamaica** — four neighbourhood terms, same shape as Brooklyn's four.

**The pattern is about borough structure, not about Brooklyn specifically.** What is now established across the portfolio:

| Area | Search granularity |
|---|---|
| Hudson Valley | County — Westchester and Rockland dominate |
| Long Island | County — Nassau and Suffolk |
| Manhattan | Borough only — no sub-borough terms in any supplied set |
| Brooklyn | Neighbourhood — Bushwick, Williamsburg, Downtown Brooklyn, Park Slope |
| Queens | Neighbourhood — Astoria, Long Island City, Flushing, Jamaica |

Manhattan is the exception worth noting: despite having the strongest neighbourhood identities in the city, its supplied sets produced no sub-borough commercial terms. The plausible reading is that Manhattan is itself the unit of commercial search — the borough name already means a commercial market, where Brooklyn and Queens do not, so searchers add the neighbourhood.

### Carry forward

**Build the Bronx and Staten Island coverage sections at neighbourhood level from the start.** Bronx: Hunts Point, Mott Haven, Port Morris, Fordham Road, Grand Concourse, Riverdale, the Industrial Business Zone. Staten Island: Teleport and Bloomfield, Hylan Boulevard, Forest Avenue, St. George and Bay Street, Richmond Valley — with the standing caveat that Staten Island returned EMPTY for low-voltage-specific findings and needs its own query set rather than imported material.

If both produce neighbourhood terms too, the rule is settled for the whole outer-borough set and can be applied without waiting for a term list to confirm it.

---

## Addendum 2 — Queens Reddit and ATP sets

**ATP:** 20 questions across Who / What / Where / When / Why / How. All 16 distinct intents probed against the page and **all 16 covered — no additions required.** With the 26 PASF terms also verified present, Queens needed zero post-build remediation of any kind.

### Reddit is retired as a source for this silo

Reddit has now returned EMPTY across **six regions** — NYC, Long Island, Hudson Valley, Manhattan, Brooklyn and Queens. Six independent attempts, six empty results, same explanation each time.

**It should not be attempted for the remaining ten pages** — Bronx, Staten Island, Nassau, Suffolk and the six Hudson Valley counties — and should not appear as an open item on any future area page. Recording EMPTY a seventh time produces no information the first one did not.

**Where the effort belongs instead.** Every differentiating fact in this silo came from primary documents:

| Finding | Source type |
|---|---|
| Suffolk County Code Chapter 924, two-year terms, $750/$1,500 penalties | County code and licensing PDFs |
| Westchester Special Electrician defined at 48 volts, not 50 | County licensing materials |
| Yonkers requires a separate electrical permit for all low voltage work | City permit application form |
| NYC 27-3016.1 certifies an individual, not a business | Administrative Code |
| Local Law 128 of 2024 / 28-105.4.7 with its conditional and life-safety carve-out | Administrative and Electrical Code |
| Abandoned cable as lease holdover; Tenant Delay clauses naming cabling | Standard lease clause libraries |
| OneLIC 15,000 units and 3.5M SF | City planning and development reporting |

None of those would have surfaced on a forum. **Research order for the remaining pages: county and municipal code, permit application forms, lease clause libraries, competitor pages, local development reporting.**

### The marketing conclusion, now evidenced six times

Buyers ask in property-manager, Nextdoor and building-management channels rather than public forums. **The off-page priority for this silo is property manager and general contractor outreach, not community content** — a conclusion drawn from six consecutive research results, and worth acting on independently of the pages.

---

## Addendum 3 — Queens Bing and DuckDuckGo sets, and a correction

30 related terms audited. **Six were absent and have been folded in.** Three of those six matter more than the count suggests.

### Correction to the earlier "zero insertions" claim

Addendum 1 reported that all 26 Queens PASF terms were present with zero insertions required, and the Bronx and Staten Island guidance was written on that basis. **That audit was checking the wrong thing.**

It confirmed Astoria, Long Island City, Flushing and Jamaica appeared somewhere on the page. It did not check whether they appeared **next to a service term**. The Bing and DuckDuckGo sets ask for exactly that pairing — *low voltage contractor Astoria*, *structured cabling Long Island City*, *data cabling Flushing* — and all three were missing as pairings despite all three neighbourhoods being named repeatedly elsewhere.

Naming a neighbourhood in a coverage grid is not the same as pairing it with the service somebody is searching for. Also absent: "near me", "best low voltage company", "commercial data cabling". All six are now in the copy naturally.

### The corrected rule for the Bronx and Staten Island

Neighbourhood-level coverage sections are necessary but not sufficient. **Each named neighbourhood needs at least one natural sentence pairing it with a head service term** — low voltage contractor, structured cabling, data cabling, network cabling — rather than appearing only as a bare place name in a card.

Bronx: pair the service with Hunts Point, Mott Haven, Port Morris, Fordham Road, Grand Concourse, Riverdale. Staten Island: Teleport and Bloomfield, Hylan Boulevard, Forest Avenue, St. George, Richmond Valley.

**And the audit has to test the pairing, not the presence** — a proximity check between service term and place name, not a substring search for the place name alone. The earlier audit passed a page that was genuinely missing three of the terms it claimed to have verified.

Post-insertion QA: all pass. 20 sections, 7 JSON-LD blocks, 13 Q&A, FAQ 12 == schema 12 exact, AI Overview 978 words across 7 H3, 14 images, zero broken links, zero duplicate questions across all fifteen pairs, max 7 shared paragraphs and all approved boilerplate. Rendered clean at 390x844.

---

## Addendum 4 — six Queens AI specimens, and the strongest finding in the project

**The Queens specimens are the Brooklyn specimens with the borough name substituted.** Not similar in structure — the same text. Same opening sentence per engine, same four bullets, same price range, same closing line about offices and multi-tenant properties. Across all six engines, in both boroughs, the only variable is the place name.

That is now demonstrable rather than asserted, because both sets were captured and can be compared directly.

**Why it matters commercially.** Queens has 15,000 apartments and 3.5 million square feet of commercial space coming out of the ground under the OneLIC plan. Brooklyn is a borough of converted factories with exposed ceilings and campus tenancies. They receive the same paragraph, because the paragraph was never about either of them.

Set that against the search data: buyers in both boroughs are going *below* borough level — Bushwick, Park Slope, Astoria, Long Island City, Flushing, Jamaica. **Generated answers are moving in the opposite direction from the searchers.** That divergence is the clearest commercial case for building these pages, and it is now evidenced rather than assumed.

**Applied to the page.** Section 10.5 previously opened with "Every generated answer assumes the building already exists." That claim is accurate against these six — every example they give is a finished building — but it was not the strongest opening available. The section now leads with the substitution finding, credits their accuracy, and then makes the point that a correct answer about New York City is not an answer about Queens. The construction argument follows as the second H3, which is where it belongs: the specific consequence rather than the headline. "Queens described as one market when it is several" was removed to hold the seven-H3 spec, since the new opener carries it more directly.

**New QA check added.** Cross-page uniqueness of AI-Overview H3 headings is now verified across all six low-voltage pages alongside the existing question and paragraph checks. Zero duplicates. Worth keeping as the silo grows, because section 10.5 is the most template-prone part of the blueprint — which is exactly the failure these specimens demonstrate.

Post-correction QA: all pass. AI Overview 986 words across 7 H3 with 3 paragraphs each, 13 Q&A, FAQ 12 == schema 12 exact, zero duplicate questions across all fifteen pairs, zero duplicate AI-Overview headings, zero broken links, rendered clean at 390x844.
