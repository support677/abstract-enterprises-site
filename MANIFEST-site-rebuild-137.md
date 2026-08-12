# site-rebuild-137 — Low voltage silo, all 5 boroughs + 3 regions

**Baseline:** site-rebuild-135. No GitHub, no Netlify, no deploy. **1080 changed and new files.**

---

# Eight pages, eight distinct theses

| Page | Phone | GBP | Thesis |
|---|---|---|---|
| Low Voltage NYC | (800) 486-0943 | Brooklyn | hub — citywide code and permits |
| Low Voltage Long Island | (800) 486-0943 · Nassau 516 · Suffolk 631 | Brooklyn | hub — Suffolk vs Nassau licensing split |
| Low Voltage Hudson Valley | (800) 486-0943 · Westchester 914 · HV 845 | Bronx | hub — county regimes, Westchester 48V, Yonkers permits |
| Low Voltage Manhattan | (929) 560-0737 | Bronx | building access and vertical distribution |
| Low Voltage Brooklyn | (347) 934-8335 | Brooklyn | converted industrial, structure and distance |
| Low Voltage Queens | (347) 434-6392 | Bronx | new construction and rough-in stage |
| Low Voltage Bronx | (646) 490-0629 | Bronx | cold chain, wash-down, facilities that never close |
| **Low Voltage Staten Island** | **(347) 934-8335** | **Brooklyn** | **legacy plant and campus backbone — NEW** |

**Zero duplicate questions across all 28 page pairs. Zero duplicate AI-Overview headings across all eight.**

---

# Staten Island — the EMPTY was resolved properly

Staten Island was recorded as EMPTY for low-voltage findings with a standing instruction not to import material from other boroughs. A dedicated search produced real grounding:

**The Teleport** — a 100-acre business park east of Route 440, developed in the mid-1980s by the City and the Port Authority, holding **five Class A office and specialised buildings totalling roughly 700,000 SF**, and **created expressly to offer high-speed voice, data and video by satellite and fibre**. Expanded with office and medical space in 2017; NYCEDC has sought development proposals for a ~7.5-acre site within it.

**Matrix Global Logistics Park**, Bloomfield, opened 2018 — reported to have brought over 2,000 jobs to the West Shore. **New York Container Terminal** anchors maritime activity. The City's **Working West Shore 2030** plan names Arlington-Port Ivory, Bloomfield-Teleport, Travis-Freshkills, Rossville Waterfront and Charleston-Tottenville as opportunity areas.

## The differentiator: legacy plant

**Staten Island holds one of the few commercial campuses in New York City purpose-built around telecommunications — and it is now old enough that the question has come full circle.** Buildings fitted out in the mid-1980s were cabled to a standard predating Category 5, and four decades of tenancies since have stacked generations without removing any.

Content unique in the silo: legacy plant assessment before quoting · **certification used as a diagnostic rather than only a sign-off** · abandoned cable removal as an NEC requirement and as the thing occupying the pathway you need · pathway capacity as the constraint deciding whether a job starts with removal · campus backbone across multi-building parcels · documentation as a deliverable for buildings that have never had any.

---

# The pairing matrix ran BEFORE delivery for the first time

The full neighbourhood by head-term grid was run pre-delivery and caught **seven neighbourhoods sitting at a single head term** — Teleport, Bloomfield, West Shore, Travis, Tottenville, Hylan Boulevard, Rossville. All raised to two before the page shipped.

Previous builds caught these gaps *after* delivery, on the supplied term sets. This is the workflow for the remaining eight county pages.

---

# Two bugs caught in final QA

**A missing `</div>` on the NYC hub** (189 open, 188 closed), introduced when the Staten Island coverage card was added. Repaired and re-verified.

**One duplicate question** between Staten Island and the Bronx. Reworded. Final: zero duplicates across all 28 pairs.

---

# Linking

Hub links to all five boroughs ✓ · every borough links up to the hub ✓ · borough sibling mesh complete across all five ✓ · inbound 5–7 per page ✓ · sitemap valid with Staten Island at 0.7/monthly ✓ · `_redirects` 200 rewrite plus two alias 301s ✓ · mega-nav carries all eight and passes `node --check` ✓

---

# QA — all eight pass

20 sections each · 7 JSON-LD blocks parsing · balanced div and section counts · FAQ 12 == schema 12 exact · AI Overview 869–1,173 words across 7 H3 · correct phone per area · 14 images each with unique area-bearing alts and titles · zero malformed or broken links · zero duplicate questions across 28 pairs · zero duplicate AI-Overview headings · zero cross-area content leakage. Rendered at 390x844 on all eight: zero blank images, zero overflow.

---

## Still open

1. **`(555) 123-4567` placeholders live on deployed pages** — Manhattan and Queens camera pages, a Brooklyn door buzzer page. Active lead leak.
2. **`300 Cadman Plaza West`** in schema on 166 Brooklyn pages, not in any routing rule.
3. **8 child pages unbuilt** — Nassau, Suffolk, and the six Hudson Valley counties. Westchester and Rockland carry the county-level search volume.

**Nothing invented.** Licensing, permit and code statements cite the NYC Administrative Code, the 2025 NYC Electrical Code, the National Electrical Code, Suffolk County Code, Westchester County licensing materials and City of Yonkers permit materials, marked general information rather than legal advice.

---

## Addendum — Staten Island term set, and the pre-delivery audit paying off

26 related terms and 16 PAA questions audited. **25 of 26 already present. One insertion required** (`office network cabling Staten Island`).

### The pre-delivery matrix audit worked

This is the first page where the neighbourhood pairing matrix ran **before** shipping rather than after a supplied term set exposed the gaps. The supplied set asks for exactly three neighbourhood pairings — **data cabling + St. George, network cabling + New Dorp, low voltage contractor + Tottenville** — and **all three were already present**, because the pre-delivery matrix had caught seven weak neighbourhoods and raised each to two head terms before the page shipped.

| Page | Neighbourhood pairings missing when the term set arrived |
|---|---|
| Brooklyn | 2 |
| Queens | 3 |
| Bronx | 3, plus 3 more found by the first matrix run |
| **Staten Island** | **0** |

**Running the matrix pre-delivery eliminates this class of gap entirely.** Standard for the eight remaining county pages, run before packaging rather than after.

### The fifth borough completes the picture

| Borough | Neighbourhood terms |
|---|---|
| Manhattan | **none** |
| Brooklyn | Bushwick, Williamsburg, Downtown Brooklyn, Park Slope |
| Queens | Astoria, Long Island City, Flushing, Jamaica |
| Bronx | Fordham, Mott Haven, Riverdale, South Bronx |
| Staten Island | St. George, New Dorp, Tottenville, plus "structured cabling SI" |

**Four of five outer boroughs produce neighbourhood terms. Manhattan produces none.** The pattern is settled — Manhattan is the sole exception, consistent with the borough name being itself the unit of commercial search there.

`structured cabling SI` is worth noting separately: an abbreviation term no other borough produced, and the only borough in the portfolio with a common two-letter short form in commercial use.

### Carry forward to the eight county pages

The Long Island and Hudson Valley sets produced **county-level** terms only, never sub-county. Nassau, Suffolk, Westchester, Rockland, Orange, Putnam, Dutchess and Ulster should be built with **town and village specificity**, with the matrix audit run against town names before delivery.


---

## Addendum 2 — streets and landmarks audit

Run across all eight pages. **Landmark coverage was complete. Named-street coverage was not.**

**Landmarks: 100% on every page** — Hudson Yards, Penn District, Navy Yard, Industry City, Bush Terminal, OneLIC, Hunters Point, Hunts Point, the IBZ, the Teleport, Matrix Global Logistics Park, New York Container Terminal, Hauppauge Industrial Park, Stewart International Airport.

**Named streets were thin on four pages.**

| Page | Roads before | After |
|---|---|---|
| Manhattan | 5 | **11** |
| Bronx | **2** | **13** |
| Staten Island | **2** | **11** |
| Long Island | **1** | **17** |
| Hudson Valley | **1** | **35** |
| Brooklyn / Queens / NYC hub | 9 / 10 / 20 | unchanged |

The Bronx, Staten Island, Long Island and Hudson Valley pages named their neighbourhoods and counties but almost no actual roads. **A page that says "Hunts Point" without naming Food Center Drive or Halleck Street reads as researched at map level rather than street level.**

Added, attached to the districts they belong to: Bruckner Boulevard, Willis Avenue, Westchester Avenue, White Plains Road, Food Center Drive, Halleck Street and Ryawa Avenue (Bronx) · South Avenue, Teleport Drive, Veterans Road West, New Dorp Lane, Victory Boulevard, Richmond Avenue, Bay Street, Richmond Terrace, West Shore Expressway (Staten Island) · Old Country Road, Hempstead Turnpike, Northern Boulevard, Jericho Turnpike, Sunrise Highway, Motor Parkway, Marcus Boulevard, Oser Avenue (Long Island) · Westchester Avenue, South Broadway, Saw Mill River Road, Gramatan Avenue and 25 numbered routes (Hudson Valley) · Sixth Avenue, Lexington Avenue, West 36th–39th Street, Broome, Greene, Wooster, Franklin, Hudson, Nassau Street, Columbus Avenue, 125th Street (Manhattan).

### Standing check added

Verified before delivery alongside the pairing matrix: every landmark from the page's research present · **minimum 8 named roads or routes per area page** · streets attached to the district they belong to rather than scattered decoratively.

**Applies to the eight remaining county pages** — Westchester needs Central Avenue and Mamaroneck Avenue, Nassau needs Old Country Road and Hempstead Turnpike, and so on. Verify before packaging.

Post-edit QA: all eight pass. 20 sections, 7 JSON-LD blocks, FAQ 12 == schema 12 exact, AI Overview 800–1,200 words / 7 H3, zero broken or malformed links, zero duplicate questions across 28 pairs, zero mobile overflow.

---

## Addendum 3 — six Staten Island AI specimens: the substitution pattern confirmed three times

Three complete specimen batches now captured from the same six engines — Brooklyn, Queens, Staten Island. **All three are the same text with the borough name substituted.** Same opening sentence per engine, same four claims, same price range, same closing line.

| Claim | Brooklyn | Queens | Staten Island |
|---|---|---|---|
| Under 50 volts · no DOB permit · certification · Article 6-D · $150–$300 | 6/6 | 6/6 | 6/6 |
| **Anything specific to the borough** | **0/6** | **0/6** | **0/6** |

**Eighteen generated answers across three boroughs, zero borough-specific content between them.** This is established now, not observed once.

**What the Staten Island set omits specifically:** no mention of the Teleport, of a campus, of multi-building parcels, of existing cable, of assessment, or of removal. On a borough whose signature commercial campus was built in the mid-1980s and whose defining problem is four decades of accumulated plant, all six describe installing into an empty ceiling.

### Applied deliberately differently from Queens

The Queens section 10.5 already opens with the substitution finding. **Reusing that opener here would have created exactly the template duplication this project guards against**, and the cross-page H3 uniqueness check would have flagged it.

The Staten Island opener keeps its own argument — every answer assumes an empty ceiling — strengthened with the specimen evidence rather than rewritten around it.

**Rule for the remaining eight pages:** the substitution finding is available as supporting evidence anywhere, but only one page in the silo leads with it. Each page's 10.5 opens on the failure most relevant to its own thesis.

Verified: AI Overview 905 words across 7 H3, **zero duplicate AI-Overview headings across all eight pages**, div balance intact.
