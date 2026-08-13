# site-rebuild-137 — Low voltage silo, 13 pages

**Baseline:** site-rebuild-135. No GitHub, no Netlify, no deploy. **1240 changed and new files.**

| Page | Phone | GBP | Thesis |
|---|---|---|---|
| NYC hub | (800) 486-0943 | Brooklyn | citywide code and permits |
| Long Island hub | (800) 486-0943 · 516 · 631 | Brooklyn | Nassau vs Suffolk comparison |
| Hudson Valley hub | (800) 486-0943 · 914 · 845 | Bronx | county regimes compared |
| Manhattan | (929) 560-0737 | Bronx | building access, vertical distribution |
| Brooklyn | (347) 934-8335 | Brooklyn | converted industrial, structure and distance |
| Queens | (347) 434-6392 | Bronx | new construction, rough-in stage |
| Bronx | (646) 490-0629 | Bronx | cold chain, wash-down, 24-hour facilities |
| Staten Island | (347) 934-8335 | Brooklyn | legacy plant, campus backbone |
| Nassau County | (516) 346-5778 | Brooklyn | jurisdictional fragmentation |
| Suffolk County | (631) 407-2884 | Brooklyn | centralised, enforced, published |
| Westchester County | (914) 877-2578 | Bronx | the threshold is 48 volts, not 50 |
| Rockland County | (845) 640-3835 | Bronx | the jurisdiction changes within a mile |
| **Orange County** | **(845) 640-3835** | **Bronx** | **the distance problem is inside one building — NEW** |

**Zero duplicate questions across all 78 page pairs. Zero duplicate AI-Overview headings. 13 unique heroes.**

---

# Orange — the only page where distance is an internal problem

**On a 595,900 SF floorplate a single closet physically cannot reach the building.** The hundred-metre channel limit stops being a specification footnote and becomes the design driver: not one telecom room with a backbone leaving it, but a network of intermediate frames placed so every dock position, scanner and access point falls inside a channel from one of them.

**This inverts every other distance page in the silo:**

| Page | Distance problem |
|---|---|
| Suffolk | 86 miles **across a county** |
| Rockland | almost none, but **two states** |
| **Orange** | **inside a single building** |

Verified: I-87, I-84 and Route 17 converge here · **New York Stewart International Airport**, Port Authority operated, 2,400 acres, oversized freight and daily FedEx/UPS, with Kalitta Air moving 747/767 freighter ops there from JFK in 2019 · a Newburgh filing at **595,900 SF with 116 loading docks** on a 58-acre parcel across from Stewart · a **1.7M SF** five-warehouse Cornwall proposal · mega-warehouse and last-mile across Montgomery, Newburgh and Wallkill · Orange County Airport, 528 acres · Woodbury Common, Legoland New York, West Point.

Supporting angles unique to this page: **dock-level device density** (116 perimeter positions, furthest from any central frame), **racking changes wireless coverage** after the plan is drawn, and **yard/gate/trailer positions** that are fibre-fed remotes rather than copper runs.

## Political content deliberately excluded

Sources include a state senator quoted calling warehouse proliferation "completely out of control," and organised local opposition. **The page uses the scale figures and none of the politics.** Whether Orange County should have more warehouses is a contested local political question — a commercial services page has no business taking a side, and the technical argument doesn't need one.

---

# Pre-assembly matrix — fifth run

**9 of 17 municipalities under two head terms** (three at zero) plus **`fiber optic cabling` missing entirely.** All fixed pre-assembly in one pass. Final: **17 municipalities at 2+ head terms, 14 roads and routes.**

Streets passed at draft this time (12) unlike Rockland (3) — because the highway convergence *is* the thesis, so the roads wrote themselves in.

# Three faults in final QA — including a hero collision

AI Overview at 788 words. One duplicate question against Bronx. And **a hero collision with Bronx** — both pages had independently chosen the warehouse tray photo, because both are industrial-thesis pages. Orange moved to the PTZ mount, tray relocated to a lazy slot so the signature visual stays.

**The hero check earns its place when two pages share a building type, not a filename.** Bronx and Orange are 200 miles of thesis apart and still reached for the same image.

# Orphan pattern pre-empted again

All eleven peers plus the HV hub wired during registration. **Shipped at 11 inbound. Spread across thirteen: 10–12.**

---

# QA — all thirteen pass

20 sections each · 7 JSON-LD blocks · favicon on all · balanced div and section counts · FAQ 12 == schema 12 exact · AI Overview 821–1,173 words across 7 H3 · correct phone per area · 14 images with unique area-bearing alt and title · **13 unique heroes, worst image overlap 11/14** · zero broken or malformed links · zero duplicate questions across 78 pairs · zero cross-area leakage · inbound 10–12. Rendered clean at 390x844.

---

## Still open

1. **`(555) 123-4567` live on deployed Manhattan, Queens and Brooklyn pages** — active lead leak.
2. **`300 Cadman Plaza West`** in schema on 166 Brooklyn pages, not in any routing rule.
3. **3 child pages unbuilt** — Putnam, Dutchess, Ulster.

**Nothing invented.** Orange infrastructure and development figures cite county, Orange County Partnership, Port Authority and published planning and news sources, marked as filing or proposal stage subject to change, general information rather than legal advice.

---

## Addendum — Orange PAA and PASF

10 PAA questions, 12 related terms. **12 gaps found and fixed** — the largest post-build correction on any page in this silo, and the cause is a pattern nothing before this triggered.

### Every term carries the "NY" suffix — first in the project

`structured cabling Orange County **NY**` · `network cabling Newburgh **NY**` · `low voltage contractor Middletown **NY**` · `network wiring Monroe **NY** / Goshen **NY** / Warwick **NY**` · `structured cabling Hudson Valley **NY**`.

**No previous area produced this.** Brooklyn, Nassau, Suffolk, Westchester and Rockland sets never appended the state.

**The reason is disambiguation.** Orange County exists in California, Florida, Texas, North Carolina, Virginia and Indiana — several larger and better known than the New York one. Searchers append NY because without it the results are wrong. Newburgh, Middletown, Monroe, Goshen and Warwick all have well-known namesakes elsewhere for the same reason.

The page carried "NY" in the title and meta but **not once in the body**. Now placed in the hero subheading, three section H2s and the town references — naturally, in the phrasing searchers use.

**Standing check added: for any place with prominent out-of-state namesakes, verify the state-suffixed form appears in body copy, not just the title.** Candidates in the remaining three: **Ulster** (Northern Ireland), and to a lesser extent **Putnam** (exists in eight other states) and **Dutchess**.

### Two head-term variants nothing else produced

- **`network wiring`** rather than `network cabling` — paired with Monroe, Goshen and Warwick
- **`fiber optic installation`** rather than `fiber optic cabling`

Both are synonyms the matrix doesn't test for, because it runs on a fixed head-term list. **A fixed list cannot catch a synonym it doesn't contain** — a different failure from the Congers/Valley Cottage near-miss, and one only the supplied set can surface.

### The credential named precisely

The set names the **NYS Department of State security and fire alarm installer licence** and correctly scopes it to cameras, access control and monitored alarms rather than plain data cabling. The page previously said only "licensed at state level by New York." Now named as commonly referred to, scoped, and pointed at the Department of State to confirm.

All thirteen pages re-verified: zero duplicate questions across 78 pairs, div balance intact, favicon on all, no broken links.

---

## Addendum 2 — Orange Reddit, ATP and Bing

The most valuable **negative** result in the project.

### Bing's own results mix California and New York

The report states Bing results are "heavily mixed" between **Orange County California** companies (Irvine, Anaheim) and Orange County New York ones.

**This independently confirms the NY-suffix finding from the opposite direction.** The PASF set showed searchers append NY. This shows why: **the engine itself cannot reliably distinguish the two counties.** The ambiguity isn't a quirk of how people type — it's in the index.

That turns a keyword observation into a positioning argument. If Bing returns Anaheim companies for a Newburgh query, unambiguous NY signalling isn't tidiness — it's the difference between appearing and not appearing.

**Action taken beyond term coverage:** a short disambiguation paragraph now opens the page's positioning section, stating plainly that Orange Counties exist in California, Florida, Texas, North Carolina, Virginia and Indiana, that search engines mix them, and that this page is about **Orange County, New York** — naming Newburgh, Middletown, Montgomery, Goshen, Monroe, Warwick and Port Jervis.

Written for the reader who arrived confused, and it happens to be exactly the signal a crawler needs. Schema `areaServed` already read "Orange County NY" on both LocalBusiness and Service, and the address is a NY address — the structured signals were right, the prose wasn't.

**Standing check extended: where an area name has out-of-state namesakes, the page needs an explicit in-body statement of which one it is, not just the suffixed term.** Apply on **Ulster** and **Putnam**.

### AnswerThePublic BLOCKED — first occurrence

ATP now requires login and blocks automated collection. **This is source degradation, not an empty result** — different from Reddit, which returns data that's genuinely thin.

Recorded so the distinction stays clear: Reddit is retired because the data isn't there; ATP is unavailable because access is gated. If ATP access returns, the source is viable again. Reddit won't be.

### Reddit — EMPTY, twelfth region

Checked against r/HudsonValley and r/Newburgh specifically this time. Same result.

All thirteen pages re-verified: zero duplicate questions across 78 pairs, div balance intact, rendered clean at 390x844.

---

## Addendum 3 — Orange AI Overview: the strongest specimen in the project

A single long-form overview rather than six short ones, and **the best specimen this project has captured.**

### What it gets right

Names **Article 6-D** · names the NYS **Department of State** security and fire alarm installer licence · states that **New York issues no single statewide low voltage contractor licence** for basic data cabling · pure structured cabling generally needs no electrical permit in most Orange municipalities · lists **IDF and MDF closet buildouts** as a service · names **warehouses and distribution centres** as a customer type · names Newburgh, Middletown, Monroe, Harriman, Woodbury, Goshen, Warwick · raises riser access, firestopping and pathway approvals.

Very little is wrong. It's better than most contractors' own websites.

### The gap is narrower and more interesting than "it ignores warehouses"

**The same answer lists IDF closets as a service, names warehouses as a customer, and then prices large projects on "drop count, cable type and accessibility" — exactly as it prices a small office.**

It knows intermediate frames exist. It knows distribution buildings exist. **It never connects the two.**

That's materially different from what was predicted, which anticipated warehouses being absent. They're present. What's absent is the causal link: on a 595,900 SF floorplate the footprint determines the closet count, and the closet count determines the price far more than the per-drop rate does.

Section 10.5 now makes exactly this point — crediting the accuracy first at length, then naming the disconnect. **It's a stronger argument than a list of errors, because it isn't a claim the answer is bad. It's a demonstration that a good answer still can't price this county's signature building.**

### Failure modes now number five

| Batch | Failure mode |
|---|---|
| Boroughs | Nothing local at all |
| Nassau, Suffolk | Correct headline, stop above the decision |
| Westchester | Right on the hard part, wrong on the number |
| Rockland | Locally accurate, unsourced claim repeated until it looks settled |
| **Orange** | **Accurate and detailed, holds both halves of the answer, never joins them** |

The fifth is the most sophisticated failure yet, and the hardest to argue against — every individual statement checks out.

### Five gaps closed

`Article 6-D` named · no-statewide-licence point stated plainly · `Cat5e` and `VoIP` added to systems copy · `low voltage contractor Hudson Valley` and `network cabling Orange County NY` pairings added.

All thirteen pages re-verified: AI Overview 868–1,173 words across 7 H3, zero duplicate questions across 78 pairs, div balance intact.

---

## Addendum 4 — sitemap and linking audit, 13 pages

### Registration — clean
sitemap.xml valid, **1,893 URLs**, closing tag intact, **no duplicate entries**. Three hubs at 0.9/weekly, ten children at 0.7/monthly. Every page has a 200 rewrite plus exactly two alias 301s, **no stale 301s pointing new slugs at .html**. mega-nav carries all thirteen, passes `node --check`.

### Linking — all six standing checks pass

| Check | Result |
|---|---|
| Hub to all children | 5/5, 2/2, 3/3 |
| Child to its own hub | 10/10 |
| Sibling mesh within each hub | complete |
| Label/destination agreement | 0 mismatches |
| Malformed or `.html` hrefs | none |
| Inbound balance | **10–12, spread of 2** |

Plus **Hub → Home on all three regional hubs**, and on all thirteen pages.

**The inbound rebalance has held through two additions.** Pre-empting the orphan condition during registration on Rockland and Orange kept the spread at 2 — against a spread of 8 found before the fix at the eleven-page audit.

### An inconsistency worth naming rather than silently changing

Hub outbound counts are uneven: **NYC 11, Hudson Valley 5, Long Island 4.**

Long Island and Hudson Valley link down to their own children and across to sibling hubs — textbook hub-and-spoke. **NYC links to almost everything**, because it sat in the peer list during the Rockland and Orange inbound rebalance and picked up all three county pages.

Neither behaviour is broken and no link is wrong. But the pattern is now inconsistent between hubs, and that was an accident of build order rather than a decision.

**Recorded, not changed.** Making NYC leaner would drop working cross-links to the highest-value county pages for no measured benefit; making the other two match NYC would dilute the hub-and-spoke structure the silo is built on. **This is your call, not a defect to fix quietly** — flagged so it stays a choice rather than a drift.

---

## Addendum 5 — CORRECTION, and the NAP fix

### ⚠ The "(555) 123-4567 lead leak" does not exist. I was wrong.

This was carried in the open-items list for many turns and repeated in several manifests. On inspection it is a **`placeholder` attribute on a phone input** — the greyed-out format hint inside a form field:

```html
<input type="tel" name="phone" placeholder="(555) 123-4567" required>
```

It appears on 479 pages, is not a `tel:` link, is not visible as contact information, and cannot be called. **It is correct as written and no change was made.** The item is struck from the open list. It should not have been reported as a live defect without being checked.

### The Cadman Plaza item was real, and worse than described

Not 166 pages of schema — **225 pages**, and not schema-only.

| Form | Pages |
|---|---|
| In `LocalBusiness` JSON-LD | 169 |
| **Visible contact text with a Google Maps link** | 56 |

The address published was `300 Cadman Plaza West, 12th Floor, NY 11201` — **neither GBP**, with "12th Floor" in the `addressLocality` field, so the block was malformed independent of the address being wrong. All 225 pages simultaneously displayed the correct `1282 Troy Ave` elsewhere, so structured data and visible copy contradicted each other on every one.

**Worse: the area name had been find-and-replaced into the fixed street address**, producing published addresses including:

- `300 Cadman Plaza West, 12th Floor, **Bronx**, NY 11201` (47 pages)
- `300 Cadman Plaza West, 12th Floor, **Orange County**, NY 11201`
- `300 Cadman Plaza West, 12th Floor, **Ulster County**, NY 11201`
- `... Nassau County / Long Island / Dutchess / Putnam / Queens / Staten Island / Hudson Valley`

### Fixed, routed by GBP

Every occurrence replaced with the correct office for that page's area — Brooklyn/SI/LI to `1282 Troy Ave, Brooklyn, NY 11203`, Bronx/Manhattan/Queens/HV counties to `460 E Fordham Rd, Bronx, NY 10458`.

A residual normalization pass then cleaned four further variants the replacement exposed (duplicated locality inside `streetAddress`, Fordham with a Brooklyn postcode, a stray 11201, and null locality fields) across **115 more files**.

**Sitewide result — two addresses, both correct:**

| Address | Pages |
|---|---|
| 1282 Troy Ave, Brooklyn, 11203 | 749 |
| 460 E Fordham Rd, Bronx, 10458 | 468 |

Zero occurrences of the bad address, zero `12th Floor` localities, zero 11201 postcodes, **zero JSON-LD parse failures across all 1,902 HTML files**.

### Two things caught by checking rather than assuming

**A misroute of my own making.** `manhattan-beach-brooklyn` matched a "manhattan" rule and was briefly given the Bronx address. Manhattan Beach is Brooklyn. Caught by the postcode sweep in the same pass and corrected.

**A false positive I did not act on.** A filename heuristic flagged 614 Brooklyn/Staten Island pages as carrying a Bronx address. Inspection showed the reference was a footer listing **both** offices correctly — a legitimate two-location block, not a defect. **No change made.** The heuristic was too crude, and mass-editing on it would have damaged 614 working pages.

**622 legitimate "Cadman Plaza" neighbourhood references are preserved** — it is a real Brooklyn area served, and only the street-address form was removed.
