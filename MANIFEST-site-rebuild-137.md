# site-rebuild-137 — Low voltage silo (7 pages) + sitewide phone routing

**Baseline:** site-rebuild-135. No GitHub, no Netlify, no deploy. **1065 changed and new files.**

---

# Pages

| Page | Phone | GBP | Thesis |
|---|---|---|---|
| Low Voltage NYC | (800) 486-0943 | Brooklyn | hub — citywide code and permits |
| Low Voltage Long Island | (800) 486-0943 · Nassau 516 · Suffolk 631 | Brooklyn | hub — Suffolk vs Nassau licensing split |
| Low Voltage Hudson Valley | (800) 486-0943 · Westchester 914 · HV 845 | Bronx | hub — county regimes, Westchester 48V, Yonkers permits |
| Low Voltage Manhattan | (929) 560-0737 | Bronx | building access and vertical distribution |
| Low Voltage Brooklyn | (347) 934-8335 | Brooklyn | converted industrial, structure and distance |
| Low Voltage Queens | (347) 434-6392 | Bronx | new construction and rough-in stage |
| **Low Voltage Bronx** | **(646) 490-0629** | **Bronx** | **cold chain, wash-down, facilities that never close — NEW** |

All seven: 20 sections, 7 JSON-LD blocks, 14 images, 13–14 Q&A, 12 FAQ mirrored exactly in schema, AI Overview at 7 H3 x 3 paragraphs, 3 Web3Forms.

**Zero duplicate questions across all 21 page pairs. Zero duplicate AI-Overview headings across all seven.**

---

# Bronx — the differentiator

The only borough in this portfolio where the defining technical problem is **environment** rather than access, structure or construction stage.

Hunts Point is one of the largest food distribution centres in the world; its produce market is undergoing a redevelopment reported at roughly $405M with construction anticipated to begin late 2026. The surrounding Industrial Business Zone carries cold storage, processing and freight, and the former Spofford site is being redeveloped as The Peninsula with around 740 homes plus roughly 30,000 SF of light industrial space.

Content no other page in the silo carries:

- **Low-temperature rated cable** — standard jacket stiffens and cracks at sustained cold, so a drop installed with ordinary components works on handover and fails two winters later.
- **Wash-down enclosure ratings** — a box rated for a dry office wall does not survive a pressure washer twice a week.
- **Temperature-zone transitions** — where cable crosses between refrigerated and ambient space, condensation collects in the nearest enclosure. Standard knowledge in the cold-chain trade, absent from every general answer about low voltage.
- **Work windows set by production**, agreed before the technical scope because the programme depends on it.
- **Mounting heights set by forklifts**, not by reach.
- **Pre-war multifamily with no riser** on the Grand Concourse — a permission problem before a technical one.

The page gives buyers a diagnostic: ask any bidder how they will handle transitions between temperature zones. A contractor who has done facility work answers immediately.

---

# The dedup flag worked

The Queens build flagged the Bronx as the next page at high duplicate risk, since Bronx and Queens industrial invite identical vocabulary, and instructed building from Hunts Point and the IBZ rather than from an existing file.

**Result: 2 duplicate questions and 2 non-boilerplate shared paragraphs** — against Queens's 7 questions and 8 paragraphs when it was built from the Brooklyn template. All four rewritten. Final: 9 shared paragraphs, all approved boilerplate plus the "Related:" inbound-link lines that accumulate on the hub as children are added.

**Building a page from its own research rather than from the nearest existing file cut duplicate remediation by roughly three quarters.** Apply to Staten Island, Nassau, Suffolk and the six Hudson Valley counties.

---

# Neighbourhood pairing rule applied

Per the corrected rule from the Queens build, every neighbourhood is paired with a head service term in natural copy, and QA now tests the **pairing** rather than the presence: structured cabling + Hunts Point · low voltage contractor + Mott Haven · structured cabling + Grand Concourse · network cabling + Fordham Road · data cabling + Riverdale. All five verified by proximity check.

---

# Sitewide phone routing

| Area | Number | Pages |
|---|---|---|
| Hub pages | (800) 486-0943 | 117 |
| Brooklyn | (347) 934-8335 | 654 |
| Bronx | (646) 490-0629 | 612 |
| Queens | (347) 434-6392 | 46 |
| Nassau | (516) 346-5778 | 44 |
| Suffolk | (631) 407-2884 | 44 |
| Manhattan | (929) 560-0737 | 44 |
| Westchester | (914) 877-2578 | 43 |
| Staten Island | (347) 934-8335 | 43 |
| Rockland / Orange / Putnam / Dutchess / Ulster | (845) 640-3835 | 207 |
| WhatsApp, all pages | (718) 679-0359 | — |

**Watch after deploy:** Westchester Square and Westchester Heights are Bronx neighbourhoods. An earlier pass mis-scoped 16 such pages before the matcher was corrected.

---

# QA — all pass on all seven

20 sections each · 7 JSON-LD blocks parsing · FAQ 12 == schema 12 exact · AI Overview 881–1,173 words across 7 H3 · balanced div and section counts · correct phone per area · 14 images each with unique area-bearing alts and titles · zero broken links · zero duplicate questions across 21 pairs · zero duplicate AI-Overview headings · zero cross-area content leakage. Rendered at 390x844 on all seven: zero blank images, zero horizontal overflow.

---

## Still open

1. **`(555) 123-4567` placeholders live on deployed pages** — Manhattan and Queens camera pages, a Brooklyn door buzzer page. Active lead leak.
2. **`300 Cadman Plaza West`** in schema on 166 Brooklyn pages, not in any routing rule.
3. **9 child pages unbuilt** — Staten Island, Nassau, Suffolk, and the six Hudson Valley counties. **Staten Island returned EMPTY for low-voltage-specific findings and needs its own query set rather than imported material.** Westchester and Rockland carry the county-level search volume in the Hudson Valley.

**Nothing invented.** Licensing and permit statements cite the NYC Administrative Code, Suffolk County Code, Westchester County licensing materials and City of Yonkers permit materials, marked general information rather than legal advice.

---

## Addendum — Bronx term sets, and a second correction to the pairing rule

25 related terms and 16 PAA questions audited. **Six were absent and have been folded in. Four of the six expose a flaw in the pairing rule as first written.**

### The flaw

The Queens build established that a neighbourhood must be paired with a head service term rather than appearing as a bare place name. The Bronx page was built to that rule and passed its own check on five pairings — including **network cabling + Fordham Road** and **data cabling + Riverdale**.

The supplied set asks for the **inverse** on three of them: **low voltage contractor** + Fordham, **data cabling** + Mott Haven, **network cabling** + Riverdale.

Every neighbourhood was present. Every neighbourhood was paired with *a* service term. **They were paired with the wrong ones.** There is no way to guess which head term a given neighbourhood will attract.

### The rule, corrected again

**Pair each significant neighbourhood with at least two different head service terms** — from low voltage contractor, structured cabling, data cabling, network cabling. Cheap to do at writing time, and it covers the likely variants without contorting the copy.

The Bronx page now carries Riverdale with both network and data cabling, Mott Haven with both data cabling and low voltage contractor, and Fordham with both low voltage contractor and network cabling. Also added: network cabling + Bronx, office network cabling + Bronx, and **South Bronx** as a distinct area term — the first sub-borough directional term any supplied set has produced.

### And the audit has to change again

A build-time check that tests one pairing per neighbourhood **will pass a page missing the pairings that matter**. The check must test each neighbourhood against every head service term and report which combinations are absent. That is the version to run on Staten Island, Nassau, Suffolk and the six Hudson Valley counties.

### Neighbourhood granularity — third borough confirmed

| Borough | Neighbourhood terms |
|---|---|
| Manhattan | none |
| Brooklyn | Bushwick, Williamsburg, Downtown Brooklyn, Park Slope |
| Queens | Astoria, Long Island City, Flushing, Jamaica |
| Bronx | Fordham, Mott Haven, Riverdale, South Bronx |

Three of four outer boroughs produce neighbourhood terms; Manhattan produces none. **Staten Island is the remaining test.**

Post-insertion QA: all pass. 20 sections, 7 JSON-LD blocks, 13 Q&A, FAQ 12 == schema 12 exact, AI Overview 896 words across 7 H3, 14 images, zero broken links, zero duplicate questions across all 21 pairs. Rendered clean at 390x844.

---

## Addendum 2 — the corrected pairing audit ran, and found four more gaps

29 Bing and DuckDuckGo terms plus a 20-question ATP set audited.

**The matrix audit specified in Addendum 1 was run for the first time** — every neighbourhood against every head service term, rather than confirming one arbitrary pairing. Result:

| Neighbourhood | Head terms paired, before |
|---|---|
| **Hunts Point** | **1** — structured cabling only |
| **Grand Concourse** | **1** — structured cabling only |
| **South Bronx** | **1** — low voltage contractor only |
| Mott Haven, Port Morris, Fordham, Riverdale | 2 each ✓ |

Three neighbourhoods sat at a single head term, **including Hunts Point — the most important place name on the page.** `data cabling installers` was also absent as a phrase. All four fixed. Final matrix: all seven neighbourhoods at two head terms.

### Why this matters beyond the Bronx

The one-pairing check passed this page twice — at build time and again on the first term audit. The matrix version caught three gaps immediately. **A check that confirms what you expect to find will keep passing pages that are missing what you did not think to look for.**

The matrix audit is now standard for the remaining nine pages: print the full neighbourhood by head-term grid, flag anything under two, fix before delivery.

### Reddit

EMPTY across seven regions now — NYC, Long Island, Hudson Valley, Manhattan, Brooklyn, Queens, Bronx. Retired, and not to be attempted on the remaining pages.

### ATP

20 questions, all intents already covered. No additions required.

Post-fix QA: all pass. 20 sections, 7 JSON-LD blocks, 13 Q&A, FAQ 12 == schema 12 exact, AI Overview 896 words across 7 H3, zero broken links, zero duplicate questions across all 21 pairs. Rendered clean at 390x844.


---

## Addendum 3 — sitemap and internal linking audit

Run across all seven built low-voltage pages. **Registration was clean. The linking graph was not.**

### Registration — clean
sitemap.xml valid with closing tag intact, 1,887 URLs · hubs at 0.9/weekly, children at 0.7/monthly · `_redirects` 200 rewrite plus two alias 301s per page · no stale 301s pointing new slugs at old pages · mega-nav carries all seven URLs and passes `node --check`.

### Three faults found and fixed

**1. The NYC hub linked down to zero children.** Its coverage cards were written before any child page existed and pointed at `structured-cabling-installation-*`. A hub that does not link to its children is not a hub — it breaks the hub-and-spoke standard and gives Google no structural signal that the four borough pages belong to it. Four cards repointed.

**2. 102 links had a low-voltage label pointing at a structured-cabling URL.** Across all seven pages, anchors reading "Low voltage cabling in Manhattan", "…in Brooklyn", "…in Queens", "…in the Bronx", "…on Long Island" pointed elsewhere. **The label and the destination disagreed** — bad for users and worse for relevance, since an anchor is a promise about where it goes. All 102 corrected.

**3. Inbound links were skewed by build order.** Each new page linked back to its predecessors and nothing linked forward: NYC 6, Manhattan 4, Brooklyn 3, Queens 2, **Bronx 1**. Under that pattern the newest page is always the most orphaned. Seven reciprocal links added. **Final: every borough child at 4 inbound, hubs at 5–6.**

### Bug introduced and repaired in the same pass

The bulk href rewrite spliced an anchor tag into the middle of a URL on the NYC hub. Caught by the broken-link check in the same run, repaired, re-verified — zero malformed hrefs, zero broken links, div balance intact.

**Lesson for future bulk link edits:** match the whole anchor element, never substitute inside an `href` value, because a partial match inside a URL will corrupt it silently.

### Six standing checks added to every future delivery

1. Hub links down to every built child. 2. Every child links up to its hub. 3. Sibling mesh complete. 4. No anchor whose label names one page while pointing at another. 5. No malformed hrefs. 6. Inbound count per page, flagged if any falls more than two below the others.

Post-fix QA on all seven: 20 sections, 7 JSON-LD blocks, FAQ 12 == schema 12 exact, AI Overview 896–1,173 words across 7 H3, zero malformed or broken links, zero duplicate questions across 21 pairs, sitemap and mega-nav valid, zero mobile overflow.
