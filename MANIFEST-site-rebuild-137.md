# site-rebuild-137 — Low voltage silo (5 pages) + sitewide phone routing

**Baseline:** site-rebuild-135. No GitHub, no Netlify, no deploy.

---

# Pages in this build

| Page | Phone | GBP | Role |
|---|---|---|---|
| Low Voltage Installation NYC | (800) 486-0943 | Brooklyn | hub |
| Low Voltage Installation Long Island | (800) 486-0943 · Nassau 516 · Suffolk 631 in contact block | Brooklyn | hub |
| Low Voltage Installation Hudson Valley | (800) 486-0943 · Westchester 914 · HV 845 in contact block | Bronx | hub |
| Low Voltage Installation Manhattan | (929) 560-0737 | Bronx | child |
| **Low Voltage Installation Brooklyn** | **(347) 934-8335** | **Brooklyn** | **child — new** |

All five: 20 sections, 7 JSON-LD blocks, 14 images, 14 Q&A, 12 FAQ mirrored exactly in FAQPage schema, AI Overview Reality Check at 7 H3 x 3 paragraphs, 3 Web3Forms, instant action block, 60-second qualifier, 2 CTA strips, 2 repair captures.

**Zero duplicate questions between any two of the five.** Verified pairwise across all ten combinations.

---

# Brooklyn — what makes it different from the other four

The NYC hub spans five boroughs and Manhattan goes vertical on tower access. Brooklyn goes at **structure and distance**, because that is what actually governs work here:

- **Converted industrial floorplates.** Wide, high, structurally heavy, and leased because the ceiling is exposed. Pathway becomes a design decision rather than a hidden one — tray and conduit will be looked at every day, so the route is agreed on paper before anything is fixed.
- **The hundred-metre channel limit as the live constraint.** On a deep converted floorplate the limit arrives far sooner than people expect, and the answer is often a second closet rather than a heroic pull. That single decision moves a budget more than the per-drop rate does.
- **Campus tenancies, not single buildings.** Industry City, Bush Terminal and the Navy Yard are estates. A tenancy across two structures is a backbone problem before it is a cabling problem. The Navy Yard is landlord to hundreds of businesses employing thousands across roughly four million square feet, and BNYDC and NYCEDC have continued putting remaining industrial floors out for redevelopment.
- **Fixings chosen for the material.** Brick, heavy timber, steel and poured concrete inside one tenancy, each taking different hardware.
- **Light manufacturing and maker space**, where the floor gets rearranged and positions are chosen knowing it will.
- **Home base.** The office is at 1282 Troy Ave, which matters far more on a service call than on a planned install.

The AI Overview section argues that generated answers describe Brooklyn as a discounted Manhattan, when the constraints are simply different — access dominates across the river, structure and distance dominate here.

---

# Duplicate remediation on this page

The first Brooklyn build shared 11 long paragraphs with the Hudson Valley page and carried 3 question strings already used on other low-voltage pages. **Six paragraphs were rewritten and three questions reworded.** Final state: 8 shared paragraphs, all of which are approved sitewide boilerplate — the warranty clause, the service-rate clause, the timing disclaimer, the NYC-code legal disclaimer — plus inbound "Related:" link lines. Zero duplicate questions sitewide.

A cross-area leak check flagged "Nassau County" on the page. Verified as a **false positive** — it appears only in the shared mega-nav, which is identical across all 1,889 site pages, never in Brooklyn body copy.

---

# Sitewide phone routing

| Area | Number | Pages |
|---|---|---|
| Hub pages (`-nyc`, `-long-island`, `-hudson-valley`) | (800) 486-0943 | 117 |
| Brooklyn | (347) 934-8335 | 654 |
| Bronx | (646) 490-0629 | 611 |
| Queens | (347) 434-6392 | 45 |
| Nassau | (516) 346-5778 | 44 |
| Suffolk | (631) 407-2884 | 44 |
| Manhattan | (929) 560-0737 | 44 |
| Westchester | (914) 877-2578 | 43 |
| Staten Island | (347) 934-8335 | 43 |
| Rockland / Orange / Putnam / Dutchess / Ulster | (845) 640-3835 | 207 |
| WhatsApp, all pages | (718) 679-0359 | — |

**Watch after deploy:** Westchester Square and Westchester Heights are Bronx neighbourhoods. An earlier pass mis-scoped 16 such pages before the matcher was corrected to give borough names precedence over county names.

**No CallRail swap script exists on the site**, so these are static and hardcoding is correct.

---

# QA — all pass on all five pages

20 sections each · titles under 60 · metas 150–160 · single H1 · 7 JSON-LD blocks parsing with no raw HTML inside · 14 images each with unique area-bearing alts and titles, alt never equal to title, all assets on disk · 14 Q&A · FAQ 12 == schema 12 exact · AI Overview 800–1,200 words across 7 H3 · balanced div and section counts · 3 Web3Forms each · approved pricing, warranty and BYOE preserved · zero broken internal links · zero duplicate questions across all ten page pairs.

Rendered at 390x844 on all five: zero blank images, zero horizontal overflow, zero failed requests.

---

## Still open

1. **`(555) 123-4567` placeholders live on deployed pages** — Manhattan and Queens camera pages, a Brooklyn door buzzer page. Active lead leak.
2. **`300 Cadman Plaza West`** in schema on 166 Brooklyn pages, not in any routing rule on file.
3. **11 silo child pages unbuilt** — Queens, Bronx, Staten Island, Nassau, Suffolk, and the six Hudson Valley counties. Supplied Bing and DuckDuckGo term sets indicate Westchester and Rockland carry the county-level search volume in the Hudson Valley.

**Nothing invented.** Licensing and permit statements cite the NYC Administrative Code, Suffolk County Code, Westchester County licensing materials and City of Yonkers permit materials. They are marked general information rather than legal advice.


---

## Addendum — Brooklyn term sets applied

26 Brooklyn PASF terms and 16 PAA questions supplied after the build and audited against the page. 9 terms were absent and folded into existing copy rather than bolted on: Cat6 installation Brooklyn, Cat6 installation cost, network cabling Brooklyn, office network cabling Brooklyn, low voltage security systems Brooklyn, low voltage permit, DOB low voltage license, Bushwick, Park Slope.

**The finding worth acting on: Brooklyn is the first area in this project to produce neighbourhood-level search terms** — Bushwick, Williamsburg, Downtown Brooklyn, Park Slope. Every other area, including Manhattan, produced borough or region terms only; the Hudson Valley went to county level and stopped.

That is a structural signal rather than a keyword list. Brooklyn is searched as a collection of neighbourhoods because that is how the borough is understood locally. It does not justify four new pages, and it has not been treated as licence to stuff neighbourhood names into copy. What it justifies is the borough page carrying genuine neighbourhood specificity in its coverage and building-type sections, which it now does.

**Watch for the same signal in Queens** — Astoria, Long Island City, Flushing and Jamaica carry comparable local identity. If the Queens term set behaves the same way, the pattern is about borough structure generally rather than Brooklyn specifically.

Post-insertion QA: all checks pass. 20 sections, 7 JSON-LD blocks, FAQ 12 == schema 12 exact, 14 Q&A, AI Overview 982 words across 7 H3, 14 images, zero broken links, **zero duplicate questions across all ten low-voltage page pairs**, max 8 shared paragraphs and all of those approved boilerplate. Rendered clean at 390x844.


---

## Addendum 2 — Brooklyn Bing, DuckDuckGo and ATP sets applied

27 related terms and a 20-question ATP-style set audited against the page. Seven terms were absent and folded in: structured cabling companies, data cabling installers, best low voltage company, server room cabling Brooklyn, commercial data cabling Brooklyn, low voltage vs electrician, and "near me".

Folding those in pushed the Q&A block to 15, outside the 12 to 14 spec. The provider-comparison entry was **merged into the existing electrician-versus-contractor answer** rather than kept separate, holding the count at 14 and avoiding two adjacent entries covering the same decision.

**The provider-comparison terms are answered as criteria, not self-nomination.** "Best low voltage company" and "structured cabling companies" are answered by handing the reader the nine proposal lines to compare and three questions to put to any bidder, with an explicit note that searching for the best company returns whoever bought the placement. A page that answers "who is best" with "we are" reads as an advert.

**Reddit is now EMPTY across five regions** — NYC, Long Island, Hudson Valley, Manhattan and Brooklyn. Five independent attempts, same result and same explanation each time. This is settled: treat Reddit as a known-empty source for the remaining low-voltage area pages and stop budgeting research time for it. The same effort spent on county code, municipal permit forms and lease clause libraries produced the Suffolk Chapter 924 penalties, the Westchester 48-volt threshold and the Yonkers blanket permit requirement, none of which would ever have surfaced on a forum.

Post-insertion QA: all pass. 20 sections, 7 JSON-LD blocks, 14 Q&A, FAQ 12 == schema 12 exact, AI Overview 982 words across 7 H3, 14 images, zero broken links, zero duplicate questions across all ten low-voltage page pairs, max 8 shared paragraphs and all approved boilerplate. Rendered clean at 390x844.


---

## Addendum 3 — six Brooklyn AI specimens, and a correction

Six AI-generated answers for "low voltage installation Brooklyn" supplied and checked against the page.

**This is the most factually accurate specimen batch collected so far. Nothing in it is false.** All six correctly state the under-50V scope, the usual absence of a DOB electrical permit for pure cabling, and the NYS Article 6-D requirement for security and alarm work.

**And none of the six says anything about Brooklyn.** The borough name appears in the opening sentence and in a closing line about offices and multi-tenant properties. Between those two points there is no converted industrial floorplate, no exposed ceiling, no campus tenancy, no masonry or timber fixing, no hundred-metre limit and no neighbourhood. They are New York City answers with a borough name substituted at top and bottom.

**Correction applied.** The Brooklyn section 10.5 previously opened by claiming AI answers describe the borough as "a smaller, cheaper Manhattan." Against these six that is inaccurate — they do not discount Manhattan, they say nothing about any borough at all. The H3 was rewritten to credit their accuracy first and then show why a correct answer about the city tells you nothing about the building you are standing in. That is both true and the stronger argument.

**Second correction.** The certification paragraph previously stated that AI answers "describe it as a business credential with some regularity." These six are more careful than that — they say "contractors should hold the appropriate Low Voltage Installer certification," which implies a company credential without asserting one. The paragraph now makes the distinction precisely rather than accusing them of a flat error: section 27-3016.1 issues to an individual, and it is worth knowing whether the paperwork in front of you is a person's certification or a company registration.

Worth recording: Brooklyn is the weakest of the three specimen batches for local specificity — the Long Island set named the Suffolk restricted licence and the Hudson Valley set named Yonkers, while this one names no local rule at all. That is the opposite of what the neighbourhood-level Brooklyn search data shows people want, and it is the clearest commercial argument for building these pages.

Post-correction QA: all pass. AI Overview 1,047 words across 7 H3 with 3 paragraphs each, 14 Q&A, FAQ 12 == schema 12 exact, zero duplicate questions across all ten pairs, zero broken links, rendered clean at 390x844.
