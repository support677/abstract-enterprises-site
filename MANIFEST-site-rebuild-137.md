# site-rebuild-137 — Low voltage silo, 11 pages

**Baseline:** site-rebuild-135. No GitHub, no Netlify, no deploy. **1209 changed and new files.**

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
| **Westchester County** | **(914) 877-2578** | **Bronx** | **the threshold is 48 volts, not 50 — NEW** |

**Zero duplicate questions across all 55 page pairs. Zero duplicate AI-Overview headings. 11 unique heroes.**

---

# Westchester — the sharpest fact in the silo

**Westchester County defines its Special Electrician licence category at 48 volts and 5 amperes.** Every other source in this project — industry guides, national contractors, and all four AI specimen batches — says fifty.

Two volts is a narrow band and a real one. **A piece of equipment can sit inside the low-voltage definition in the Bronx and outside it in Yonkers, ten minutes up the road.** An answer that is correct nationally and wrong locally is more dangerous than one that is obviously hedged, because nothing about it looks like a guess.

Supporting county facts: the county runs its own **Electrical Licensing Board** through Consumer Protection at **148 Martine Avenue, White Plains, (914) 995-2657**, with **four hours of continuing education before a licence is renewed or shelved** — which gives a buyer both a place to verify and a question worth asking.

## Second pillar: Yonkers inverts the general rule

City permit materials state **all low voltage work requires a separate electrical permit**, the only exception being HVAC control wiring in one and two family residences, with central-panel fire alarm routing through a Fire Department building permit. **Permits issue only to contractors registered or licensed within city limits** — so a perfectly qualified contractor from the next town may be unable to pull the permit your building needs.

That is the reverse of what nearly every general summary supplies, in the largest city in the county.

---

# Pre-assembly matrix — third run, biggest catch yet

Run against the **county's full municipal roster** rather than the places that happened to appear in the draft — the correction forced by the Brookhaven miss on Suffolk.

**Caught 15 of 22 municipalities under two head terms**, including Scarsdale, Port Chester, Greenburgh, Mamaroneck, Ossining and New Castle at **zero**. All fixed before assembly in one edit pass. Final: **22 municipalities at 2+ head terms, 11 named roads and routes.**

# Three faults caught in final QA

AI Overview at 795 words, under the 800 floor — extended with a buyer diagnostic on clinical containment. **Four duplicate questions** against Staten Island, Hudson Valley, Nassau and Suffolk. **Thirteen shared paragraphs with Suffolk**, reduced to five boilerplate by rewriting nine.

**The Nassau and Suffolk duplicates appeared because those pages are recent and share a county-page shape.** The closer two pages sit in build order and structure, the harder the dedup pass has to work.

---

# QA — all eleven pass

20 sections each · 7 JSON-LD blocks · favicon block on all · balanced div and section counts · FAQ 12 == schema 12 exact · AI Overview 805–1,173 words across 7 H3 · correct phone per area · 14 images with unique area-bearing alt and title · **11 unique heroes, worst image-set overlap 11/14** · zero broken or malformed links · zero duplicate questions across 55 pairs · zero cross-area leakage. Rendered clean at 390x844.

---

## Still open

1. **`(555) 123-4567` live on deployed Manhattan, Queens and Brooklyn pages** — active lead leak.
2. **`300 Cadman Plaza West`** in schema on 166 Brooklyn pages, not in any routing rule.
3. **5 child pages unbuilt** — Rockland, Orange, Putnam, Dutchess, Ulster. **Rockland carries the remaining volume.**

**Nothing invented.** Westchester licensing cites County Department of Consumer Protection materials; Yonkers permitting cites City of Yonkers published permit materials. Both marked general information rather than legal advice, with a direction to confirm current requirements.

---

## Addendum — Suffolk Bing, DuckDuckGo, ATP and Reddit sets

29 related terms and a 22-question ATP set audited against the built page. **All 13 audited terms present, zero insertions required.** Five of six distinct ATP intents already covered.

### The licence term rose from #5 to #3 in commercial intent

The earlier Suffolk set ranked `low voltage restricted license Suffolk` fifth. **This combined set ranks it third** — above Cat6 installation and structured cabling cost.

More striking is the concentration in the ATP data: **six of twenty-two questions are about the Restricted Licence specifically** — who needs it, what it is, why the county requires it, when it applies, how it differs from Nassau, and how to get one.

**No other area in this portfolio comes close.** Most areas produce one licensing question among twenty-plus. Suffolk produces six, and the term outranks core service phrases. **This is a county where the credential is itself the search category** — which validates building the page around enforcement and verification rather than around service description.

### One ATP question is deliberately not answered

*"How do I get a Low Voltage Restricted License in Suffolk County?"* is **applicant intent, not buyer intent.** Someone asking that wants to become a licensed installer, not hire one.

The standing rule in this project is that career-intent queries — salary, "how to become", application routes — are never answered on a commercial page. Answering it would pull traffic that cannot convert and dilute a page built for property owners and facility managers.

The page answers the five buyer-side licence questions and omits the applicant-side one. **That split should hold for the remaining pages: if a supplied ATP set contains an application-route question, note it and skip it rather than treating volume as a reason to chase it.**

### Reddit

EMPTY across nine regions now. Retired, and not to be attempted on the five remaining county pages.

---

## Addendum 2 — six Suffolk AI specimens: the prediction validated

Part 23 put a prediction on record before any Suffolk specimen batch existed: *expect them to name Chapter 924 or county-level licensing correctly, and to miss the $750/$1,500 penalties, the two-year terms, the CE requirement and the public non-compliance listing.*

| Item | Predicted | Actual |
|---|---|---|
| Names the Restricted Licence | hit | **6 of 6** |
| States Suffolk is stricter than Nassau | — | **4 of 6** |
| **$750 / $1,500 penalties** | **miss** | **0 of 6** |
| **Two-year terms** | **miss** | **0 of 6** |
| **Continuing education** | **miss** | **0 of 6** |
| **Public non-compliance listing** | **miss** | **0 of 6** |

**Exactly right on all four miss items and on the hit.** This is the most accurate batch in the project — genuinely local, correctly stated, several telling the reader to verify the licence. Section 10.5 now credits that with the counts, then makes the sharper point: **not one of the six attaches any consequence to the rule, and none mentions the public listing exists to verify against.** Saying "make sure they hold it" without saying a means of checking exists stops one step short of useful.

### An unverified detail the specimens supply — deliberately NOT adopted

Two of six state the licence is issued by **"Suffolk County Consumer Affairs."** Plausible, possibly correct, but **not in any source captured for this project — so it has not been added to the page.**

This is exactly what the provenance rules exist to prevent. A confident, official-sounding attribution in AI output is not a source. The page continues to cite Chapter 924 of the Suffolk County Code, which is verified, and names no issuing department.

**Standing rule reinforced: never adopt a factual detail from a specimen batch.** Specimens are evidence of what generated answers say, not of what is true.

### Pattern across five batches

| Batch | Locally specific content |
|---|---|
| Brooklyn / Queens / Staten Island | **none** — same text, borough name swapped |
| Nassau | yes — no county-wide licence, contrasted with Suffolk |
| **Suffolk** | **yes, strongest** — names the licence, says stricter than Nassau |

**Borough batches carry no local content. County batches do.** So the commercial argument differs by page type: on borough pages the gap is that answers say nothing local; on county pages the gap is that they stop one level above the decision. **The remaining five county pages should be written to the second.**

All eleven pages re-verified: AI Overview 853–1,173 words across 7 H3, zero duplicate questions across 55 pairs, zero duplicate headings, div balance intact.

---

## Addendum 3 — Westchester PAA and PASF

16 PAA questions and 25 related terms audited. **21 of 23 present; two town pairings added** — `low voltage contractor White Plains` and `network cabling Scarsdale`.

### The set names Greenburgh on permits, not just Yonkers

The supplied local notes state: *"Some towns (Yonkers, Greenburgh, etc.) require permits even for low-voltage work."*

The page was built naming **Yonkers only**, because Yonkers is the one whose position is verified against published city permit materials. **Greenburgh is not in any source captured for this project.**

Handled per the provenance rule established on Suffolk: the claim is **not asserted as fact**. A new Q&A was added — *"Is Yonkers the only Westchester municipality that permits low voltage work?"* — stating that Yonkers is the one with published materials saying so, that Greenburgh is commonly named alongside it, and that for any other municipality the answer is to confirm with that building department rather than assume either way.

**That's the right shape for a claim of this type: name it, attribute it as commonly reported rather than verified, give the reader the action.** Asserting it outright would adopt an unverified detail; omitting it would withhold something a Greenburgh owner needs to check.

### The set uses "Westchester" bare, not "Westchester County"

All 25 terms use the short form. The page uses the long form throughout, which still matches because the county name contains the bare form — and the bare form appears 26 times in body copy independently. No change needed, but worth recording: **on county pages the short form is what searchers type.** Copy written exclusively in the long form would be a near miss rather than a hit.

### Prediction still open

The Westchester specimen batch is predicted to state **50 volts rather than 48**. The PAA and PASF sets don't test that — it needs the AI Overviews. Prediction stands.

All eleven pages re-verified: 20 sections, 7 JSON-LD, FAQ 12 == schema 12, AI Overview 853–1,173 words, 13–14 Q&A, zero duplicate questions across 55 pairs, **all 22 Westchester municipalities at 2+ head terms**, zero broken images or empty alts.

---

## Addendum 4 — Westchester Bing, DuckDuckGo, ATP and Reddit

29 related terms and a 21-question ATP set. **12 of 13 audited terms present; one insertion.** All six distinct ATP intents already covered.

### A municipality-level permit term — first in the project

The DuckDuckGo set contains **`low voltage permit Yonkers`**.

**No other area in this portfolio has produced a sub-county permit search term.** Nassau produced village-level *service* terms; Suffolk produced a county *licence* term. This is the first time searchers are asking about permitting at the level of a single municipality inside a county.

That is direct demand-side confirmation of the page's second pillar. The Yonkers permit regime went into the page from city permit materials because it inverts the general rule — the search data now shows people looking for exactly that. The phrase is now carried in the Yonkers passage in the searcher's own wording.

**Carry forward:** on the remaining county pages, check whether any single municipality generates its own permit or licence term. Where one does, that municipality deserves named treatment rather than being folded into a coverage list.

### Three named-place patterns now distinguished

| Level | Example | Seen in |
|---|---|---|
| Neighbourhood + service | `structured cabling Williamsburg` | 4 of 5 boroughs |
| Town/village + service | `structured cabling Garden City` | Nassau, Suffolk, Westchester |
| **Municipality + permit** | **`low voltage permit Yonkers`** | **Westchester only** |

The third is the most commercially interesting: **a permit search sits closer to the transaction than a service search.** Somebody searching a permit requirement by municipality already has a building and a project.

### Reddit

EMPTY across ten regions. Retired, not to be attempted on the four remaining county pages.

All eleven pages re-verified: zero duplicate questions across 55 pairs, div balance intact, favicon on all, no broken links.

---

## Addendum 5 — six Westchester AI specimens: the 48-volt prediction validated

Part 26 recorded the prediction before any Westchester specimen existed: *expect them to state 50 volts rather than 48.*

| Claim | Result |
|---|---|
| **States 50 volts** | **6 of 6** |
| **States 48 volts** | **0 of 6** |
| Requirements handled municipally, not county-wide | 6 of 6 — **correct** |
| Names Yonkers as requiring permits | 4 of 6 — **correct** |
| Names Greenburgh | 3 of 6 |
| County Electrical Licensing Board | 0 of 6 |
| 148 Martine Avenue / county contact | 0 of 6 |
| Four-hour CE before renewal | 0 of 6 |

### The finding is sharper than "they got it wrong"

**These are good answers.** All six correctly identify that Westchester handles requirements municipally rather than county-wide, four name Yonkers specifically, several tell the reader to check the town. Genuinely local, genuinely useful, better than the borough batches on every measure.

**And all six state the wrong threshold for this county.**

That combination *is* the argument, and section 10.5 was rewritten to make it rather than to score a point — crediting what they get right first, then the count (six answers, six times fifty, zero mentions of forty-eight), then the conclusion that matters: **being correct about the hard part is no guarantee of being correct about the number.** An answer can be careful, locally researched and right about municipal structure and still hand you the wrong volts, with nothing in its presentation signalling which part to distrust.

### Greenburgh corroborated — still not adopted as fact

Three of six name Greenburgh alongside Yonkers, matching the owner-supplied local note. Four independent restatements of the same claim.

**It remains unverified against a primary source and the page still does not assert it.** The Q&A added last pass describes Greenburgh as *commonly named alongside* Yonkers and directs the reader to the building department. Corroboration across generated answers raises confidence the claim circulates widely; it does not make it a source. The phrasing stays as written.

### Five batches, three distinct failure modes

| Batch type | What they get wrong |
|---|---|
| Boroughs | Nothing local at all — same text, name swapped |
| Nassau, Suffolk | Correct headline, **stop one level above the decision** |
| **Westchester** | **Correct on the hard structural point, wrong on the specific number** |

The third is the hardest for a reader to spot. **The remaining four county pages should be checked for a Westchester-type error specifically** — a locally accurate answer carrying one wrong figure — rather than assumed to fail the Nassau/Suffolk way.

All eleven pages re-verified: AI Overview 868–1,173 words across 7 H3 with 3 paragraphs each, zero duplicate questions across 55 pairs, zero duplicate headings, div balance intact.


---

## Addendum 6 — sitemap, linking, streets and landmarks audit across all 11 pages

### Registration — clean
sitemap.xml valid, **1,891 URLs**, closing tag intact. Three hubs at 0.9/weekly, eight children at 0.7/monthly. Every page has a 200 rewrite plus two alias 301s, **no stale 301s pointing new slugs at .html**. mega-nav carries all eleven, passes `node --check`.

### Hub-and-spoke — clean
NYC hub → all 5 boroughs ✓ · Long Island hub → Nassau + Suffolk ✓ · Hudson Valley hub → Westchester ✓ · every child → its own hub ✓ 8/8 · sibling mesh complete ✓

### Inbound links badly skewed by build order — fixed

Structurally correct, numerically lopsided:

| Group | Inbound before |
|---|---|
| Boroughs and hubs | 8–10 |
| Nassau, Suffolk | **3** |
| **Westchester** | **2** |

The build-order artifact caught in the earlier linking audit had **reappeared** as the county pages were added — each new page linked back, nothing linked forward. **The three newest and most commercially valuable pages were the most orphaned in the silo.**

**19 links added.** The five boroughs and NYC hub now link across to all three county pages; Nassau and Suffolk link to Westchester. **Final inbound spread 8–10**, from 2–10.

**This is a recurring pattern, not an incident.** Every addition to a built silo starts orphaned. The inbound-balance check runs after every page added, not once at the end.

### Streets and landmarks — all pass

Every landmark from each page's research present; every page clears the **8-road minimum**:

| Page | Landmarks | Roads + routes |
|---|---|---|
| NYC | 5/5 | 21 |
| Manhattan | 6/6 | 11 |
| Brooklyn | 7/7 | 9 |
| Queens | 7/7 | 10 |
| Bronx | 6/6 | 13 |
| Staten Island | 7/7 | 11 |
| Long Island | 4/4 | 17 |
| Hudson Valley | 5/5 | 35 |
| Nassau | 7/7 | 10 |
| Suffolk | 7/7 | 11 |
| Westchester | 7/7 | 12 |

### Re-verified after the link edits

All eleven: 20 sections · 7 JSON-LD parsing · balanced div and section counts · FAQ 12 == schema 12 exact · AI Overview 868–1,173 words across 7 H3 · 14 images each · favicon block · zero malformed or broken links · zero duplicate questions across 55 pairs · rendered clean at 390x844.
