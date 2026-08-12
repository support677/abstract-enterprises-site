# site-rebuild-137 — Low voltage silo, 10 pages

**Baseline:** site-rebuild-135. No GitHub, no Netlify, no deploy. **1114 changed and new files.**

**All of NYC and all of Long Island complete.**

| Page | Phone | GBP | Thesis |
|---|---|---|---|
| NYC hub | (800) 486-0943 | Brooklyn | citywide code and permits |
| Long Island hub | (800) 486-0943 · 516 · 631 | Brooklyn | Nassau vs Suffolk comparison |
| Hudson Valley hub | (800) 486-0943 · 914 · 845 | Bronx | county regimes, 48V, Yonkers |
| Manhattan | (929) 560-0737 | Bronx | building access, vertical distribution |
| Brooklyn | (347) 934-8335 | Brooklyn | converted industrial, structure and distance |
| Queens | (347) 434-6392 | Bronx | new construction, rough-in stage |
| Bronx | (646) 490-0629 | Bronx | cold chain, wash-down, 24-hour facilities |
| Staten Island | (347) 934-8335 | Brooklyn | legacy plant, campus backbone |
| Nassau County | (516) 346-5778 | Brooklyn | jurisdictional fragmentation |
| **Suffolk County** | **(631) 407-2884** | **Brooklyn** | **centralised, enforced, published — NEW** |

**Zero duplicate questions across all 45 page pairs. Zero duplicate AI-Overview headings across all ten.**

---

# Suffolk — the inverse of Nassau

Nassau's thesis is that there is no single answer. **Suffolk's is that there is one, it's written down, and it has teeth.**

From Suffolk County Code Chapter 924 and county licensing materials: a **Restricted Electrical Licence** alongside the Master licence · **two-year terms** with CE before renewal (four hours restricted, eight master) · line-voltage connections reserved to a **Suffolk Master** · **$750 first offence, $1,500 thereafter** · and **a public listing of those found non-compliant**. The county CE catalogue names low voltage and communications topics directly, indicating the trade sits within county scope rather than adjacent to it.

**The public non-compliance listing is the sharpest detail in the whole county set.** It turns an abstract licensing requirement into a verification tool a buyer can actually use, and no general source mentions it. The page presents it that way — something the reader can check, not a threat.

Plus the geography: **Suffolk runs roughly 86 miles east to west.** Multi-site work is a logistics question, priced as a stated line rather than absorbed. The East End seasonal calendar gets its own treatment — a building quiet in March is at capacity in July.

## Three Long Island pages, three non-overlapping arguments

| Page | Argument |
|---|---|
| Long Island hub | Nassau vs Suffolk — the comparison |
| Nassau child | Within-county fragmentation — 64 villages, three Examining Boards |
| Suffolk child | Centralised, enforced, published — and 86 miles long |

Parent answers the comparison; each child answers its own county's condition.

---

# Pre-assembly matrix, second run

Run on raw body files before assembly. Caught **4 weak towns** (Farmingdale, Bohemia, Ronkonkoma, Commack) and **2 missing terms** (`low voltage license` and `low voltage permit` paired with Suffolk). All fixed at body-file stage — one edit pass, no schema or image rework.

Final: **13 towns and corridors at 2+ head service terms, 8 named roads, 24 of 26 anticipated terms present before any term set arrives.**

One duplicate question against Nassau caught at final QA and reworded.

---

# Prediction on record for the Suffolk specimen batch

Per the Nassau finding that county specimens carry real local content: **expect them to name Chapter 924 or county-level licensing correctly, and to miss the $750/$1,500 penalties, the two-year terms, the CE requirement and the public non-compliance listing.** Testable against a supplied batch.

---

# QA — all ten pass

20 sections each · 7 JSON-LD blocks · balanced div and section counts · FAQ 12 == schema 12 exact · AI Overview 805–1,173 words across 7 H3 · correct phone per area · 14 images with unique area-bearing alts and titles · zero malformed or broken links · zero duplicate questions across 45 pairs · zero duplicate AI-Overview headings · zero cross-area leakage. Rendered clean at 390x844.

---

## Still open

1. **`(555) 123-4567` live on deployed Manhattan, Queens and Brooklyn pages** — active lead leak.
2. **`300 Cadman Plaza West`** in schema on 166 Brooklyn pages, not in any routing rule.
3. **6 child pages unbuilt** — Westchester, Rockland, Orange, Putnam, Dutchess, Ulster. **Westchester and Rockland carry the volume**, and Westchester holds the **48-volt** finding that contradicts every specimen batch captured so far.

**Nothing invented.** Suffolk licensing cites County Code Chapter 924 and county published materials, marked general information rather than legal advice, with a direction to confirm the current requirement with the county.

---

## Addendum — Suffolk term set: a licence term is a top-5 commercial keyword

25 related terms and 16 PAA questions audited. **Three gaps, and one is the most commercially significant miss in the project so far.**

### A named licence term ranks fifth in commercial intent

The supplied set ranks **`low voltage restricted license Suffolk` at number five**, above several generic service terms.

**No other area in this portfolio has produced a licence term anywhere in a top-five list.** Every other area's list is service-plus-geography — contractor, structured cabling, data cabling, Cat6, cost. Suffolk substitutes a specific statutory credential into that list.

That's a strong signal about buyer behaviour here. People aren't only searching for a contractor — **they're searching for the credential by name, which means they intend to verify.** It confirms the page's thesis from the demand side: a county that publishes penalties and maintains a public non-compliance listing produces buyers who check.

**The page had the licence but not the search phrase.** It described the Restricted Electrical Licence accurately throughout while never using the words searchers actually type. Now carried in both the licensing Q&A and the terminology block, phrased as what people search for versus what the county calls it.

**Rule for the remaining six pages:** check whether any licence or code term appears in the commercial intent ranking, and if so carry the searcher's phrasing alongside the official one. **Westchester is the likely candidate** — the Special Electrician licence and the 48-volt threshold may behave the same way.

### Two towns missed entirely

**Babylon and Brookhaven** — two of Suffolk's ten towns, and Brookhaven the largest by area — appeared at **zero head terms**. The pre-assembly matrix ran against a town list that omitted both, so the audit passed a page genuinely missing them.

**The matrix is only as good as the place list fed into it.** For the six Hudson Valley pages, the town list must be built from the county's actual municipal roster before the matrix runs — not from whichever towns happen to appear in the draft copy. Both now at three head terms.

### Independent confirmation

The supplied key local note reads: *Suffolk County requires a Low Voltage Restricted License (stricter than Nassau).* That matches the Nassau/Suffolk split the silo is built on, arrived at independently.

Post-insertion QA: all ten pages pass. Zero duplicate questions across 45 pairs, zero duplicate AI-Overview headings, div balance intact.

---

## Addendum 2 — re-inspection: a head-term count can hide the pairing that matters

The Suffolk term set was supplied a second time, identical. A repeated identical input is treated as a bug report requiring re-inspection rather than a rebuild, so **the shipped ZIP was opened and audited directly** rather than the working copy.

**Confirmed shipped correctly:** the `low voltage restricted license` phrasing and both Babylon pairings from the previous turn were present in the delivered package.

**One real gap found that the previous audit's summary had masked.** Brookhaven showed **three head terms** and passed the "two or more" rule comfortably. But the three present were low voltage contractor, structured cabling and data cabling — **and the term searchers actually use is `network cabling Brookhaven`**, which was the one missing.

**A count of head terms is not the same as coverage of the head terms that were asked for.** The two-or-more rule protects against a place name appearing bare; it does not guarantee a specific supplied pairing is present. Both checks are now required:

1. **Matrix check** — every place at 2+ head terms, run pre-assembly against the county's full municipal roster.
2. **Explicit check** — every pairing named in a supplied set verified individually, never inferred from the matrix passing.

Brookhaven now carries all four head terms. All ten pages re-verified: zero duplicate questions across 45 pairs, div balance intact, no broken or malformed links.


---

## Addendum 3 — image rotation audit

Run across all ten pages after a report that rotating images and alt tags were missing.

### Already correct

**Alt and title coverage was complete: 140 of 140 content images.** All carry the area name in alt, title and filename; alt never equals title; explicit width and height on every image; exactly one eager image per page; every ImageObject @graph carrying all fourteen entries. Rotation was working too — nine distinct orderings across ten pages.

### Two genuine hero collisions found and fixed

Comparing heroes **by image content rather than filename** — filenames differ per page because each is area-prefixed — found two pairs sharing the same photograph:

| Collision | Pages |
|---|---|
| Crew ceiling cable pull | **NYC hub and Brooklyn** |
| IDF rack patching | **Staten Island and Hudson Valley** |

Resolved with heroes not used anywhere else:
- **Brooklyn** → door lock and access control wiring detail, which suits its converted-industrial thesis better than a generic crew shot.
- **Staten Island** → conference room display cabling in a business park suite, matching the Teleport campus argument.

Each swap carried through figure markup, alt, title, caption, `og:image`, `twitter:image`, the LocalBusiness and Service `image` fields, and a full ImageObject @graph rebuild. Zero old filename references remain.

### Why earlier checks missed it

Every previous audit checked images **within** a page. **None compared heroes across pages** — and because each file is named for its own area, two pages can carry the same photograph under different filenames and pass every filename-based check.

**The check has to compare image content, not filenames.** A perceptual hash of each hero across the silo catches it in one pass.

### Standing check added

1. **Hero uniqueness across the whole silo, compared by image content.**
2. Fourteen content images per page, alt and title unique and never equal.
3. Area name in filename, alt and title on every image.
4. Exactly one eager image per page; explicit dimensions on all.
5. ImageObject @graph count matching the page.

Verified: **ten unique heroes, 140/140 images with area-bearing alt and title, zero rendered-blank images and zero empty alts at 390x844 across all ten pages.**


---

## Addendum 4 — the real image fault was set duplication

A second report of missing pictures on Nassau prompted a direct audit of the shipped ZIP. **All 14 Nassau images were present, valid, alt-tagged and rendering — zero broken, zero network failures.** Nothing was missing in the literal sense.

**But the complaint was correct.** Comparing image sets by content across the silo:

| Pair | Shared photos |
|---|---|
| **Queens + Suffolk** | **14 of 14 — identical** |
| **Nassau + Queens** | **14 of 14** |
| **Nassau + Suffolk** | **14 of 14** |
| Staten Island + Suffolk | 13 of 14 |

**Only 18 photographs were serving 140 image slots.** Browsing Nassau after Queens, the page looks like it has no pictures of its own — which is exactly what "missing pictures" means from a reader's point of view, even though every file loads.

### Five unused clean assets were sitting in uploads

- **The `ChatGPT_Image_*` set (18 files) carries `800-486-0943` on the van and garments** — the emergency line, locked out of SEO landing pages. Correctly excluded, and it stays excluded.
- **Five unused UUID assets are clean "LOW VOLTAGE DIVISION" branding with no phone number anywhere:** school corridor cable pull, school corridor ceiling tile, video wall install, electric strike wiring, storefront camera install.

All five converted and distributed across Nassau, Queens, Suffolk and Staten Island.

| Metric | Before | After |
|---|---|---|
| Unique photos in silo | 18 | **20** |
| Worst pair overlap | **14/14 identical** | **13/14** |
| Nassau overlap with any page | 14/14 | **8–10/14** |

### One fix created one new fault, caught in the same pass

Swapping the Nassau hero to the school corridor image created a **new hero collision with Long Island**, which already used that photo as its hero. Caught by the hero-uniqueness check in the same run and resolved by moving Nassau to the electric strike image.

**An image swap is not a local edit.** It touches figure, alt, title, caption, `og:image`, `twitter:image`, the LocalBusiness and Service `image` fields, and the ImageObject @graph — and it can create a collision elsewhere. The hero check re-runs after every swap, not only before.

### Standing check extended

**Image-set overlap between every pair of pages, compared by content, flagged above 13 of 14.** Per-page checks and hero uniqueness alone will happily pass two pages carrying identical sets.

Verified: 10/10 unique heroes · 140/140 images with unique area-bearing alt and title · @graph matching every page · zero broken images and zero empty alts at 390x844 across all ten.


---

## Addendum 5 — full photo library now in rotation

All 18 remaining supplied photographs converted and distributed across the ten pages, six per page on a stride that gives every page a different combination.

| Metric | Before | After |
|---|---|---|
| Unique photos in silo | 20 | **33** |
| Worst pair overlap | 13/14 | **11/14** |
| Unique heroes | 10/10 | **10/10** |

New subject matter now covered: van load-out, retail storefront ceiling pull, exterior weatherproof enclosure, riser conduit pull, tone-generator tracing, rack switch configuration, lobby video intercom, maglock install, electric strike with keypad, ceiling speaker install, conference PTZ camera mount, recessed display box, stud rough-in boxes, IDF patch panel build, access point from a lift, fiber fusion splicing and splice tray work.

Every new image carries area-specific alt text, a distinct title, a caption, correct dimensions and an ImageObject entry. Verified across all ten pages: 140/140 images with unique area-bearing alt and title, alt never equal to title, @graph matching each page, one eager image per page, zero broken images and zero empty alts at 390x844.
