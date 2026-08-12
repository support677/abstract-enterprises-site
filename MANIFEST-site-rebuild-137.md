# site-rebuild-137 — Three low voltage hubs + sitewide phone routing

**Baseline:** site-rebuild-135. No GitHub, no Netlify, no deploy. **1,003 changed and new files.**

---

# 1. Low Voltage Installation Hudson Valley — NEW

`low-voltage-installation-hudson-valley.html` — 20 sections, six counties.
**Phone (800) 486-0943** per the hub rule; Westchester (914) 877-2578 and the 845 line for Rockland, Orange, Putnam, Dutchess and Ulster appear in the contact block. **Bronx GBP** per the Hudson Valley routing rule.

## Two verified findings, both of which contradict what every AI answer says

**1. Westchester draws the line at 48 volts, not 50.** The county runs its own Electrical Licensing Board under Westchester County Law, administered by the Department of Consumer Protection's Trades Licensing Division at 148 Martine Avenue, White Plains, (914) 995-2657. Licence categories include Master, **Special Electrician**, reciprocal and inspector. The Special Electrician category covers low voltage, alarm and signal work, audio and sound systems and telephone interconnect — and it is framed at **forty-eight volts or five amperes**, not the fifty volts the rest of the industry uses and not the under-fifty-volts NYC writes into its Administrative Code. Renewal requires four hours of continuing education from a board-approved provider, and no licence renews until written proof reaches Consumer Protection.

**2. Yonkers requires a permit for all low voltage work.** The City of Yonkers Department of Housing and Buildings states on its own electrical permit application that **all low voltage work requires a separate electrical permit**, with the only listed exception being HVAC controls in one- and two-family residences. The city's electrical code adds that permits issue only to contractors registered and licensed to work within Yonkers city limits, and fire alarm work with a central panel routes through the Fire Department on a building permit instead.

That second finding matters because "low voltage under fifty volts generally does not need a permit" is close to universal in AI answers, competitor pages and industry summaries. In Yonkers it is simply wrong, and the contradiction is on a city government form. Both findings are on the page, both cite their source, and both direct the reader to the relevant authority.

**Three regions, three regimes now documented across the silo:** NYC certifies an *individual* under Administrative Code 27-3016.1 · Suffolk issues a Restricted Electrical Licence under County Code Chapter 924 · Westchester issues a Special Electrician licence at a 48V threshold, and at least one Hudson Valley city permits all low-voltage work. No competitor page covers any of the three.

## Hudson Valley content, not recycled

Verified clean of NYC and Long Island leakage — no Navy Yard, Hunts Point, OneLIC, Hauppauge, Nassau Hub or Mineola. The page runs on this region's conditions: buildings that spread rather than stack, converted mill and industrial space where the exposed ceiling is the tenant's reason for leasing, municipal campuses extended piecemeal over decades, distribution along I-84 and I-87, and school districts spread across large footprints. Technical spine is the hundred-metre channel limit and fiber backbone between separate structures.

## Duplicate check

An initial build shared 17 long paragraphs with the Long Island hub. 13 were rewritten, a second pass caught 3 more in the FAQ and 3 duplicate question strings. **Final: 5 shared with NYC and 4 with Long Island, all approved sitewide boilerplate** — warranty clause, service-rate clause, timing disclaimer, one inbound-link line. **Zero duplicate questions across the entire site.** Against every other page: zero.

## Spec compliance note

Adding the Yonkers material pushed the AI Overview section to 8 H3 and the Q&A block to 15, both outside spec. The testing H3 was removed (that argument is carried on both sibling hubs and this page's strength is regulatory) and the generic permit question was merged into the Yonkers one. Final: **AI Overview 1,005 words across 7 H3 with 3 paragraphs each; 14 Q&A.**

## Images

14 from the LOW VOLTAGE DIVISION set with its own hero (IDF rack), distinct from both other hubs. Every filename carries `hudson-valley`. Every alt and title unique, keyword-varied, naming the Hudson Valley or one of the six counties. Alt never identical to title. Native aspect preserved, nothing cropped. All 14 in the ImageObject graph with explicit dimensions.

## QA — all pass

20 sections · title 49 · meta 160 · single H1 · 7 JSON-LD blocks parse · 14 images with unique area-bearing alts and titles, all assets present · 14 Q&A · FAQ 12 == schema 12 exact · AI Overview 1,005 words / 7 H3 · div 182/182, section 23/23 · 3 Web3Forms · approved pricing, warranty and BYOE preserved · zero broken internal links · zero duplicate questions sitewide · zero cross-hub leakage. Rendered at 1440x900, 768x1024 and 390x844: zero blank images, zero cropping, zero overflow.

**Registration:** sitemap 0.9/weekly, XML validated; `_redirects` 200 rewrite plus alias 301s; mega-nav key added, node --check passed. Inbound links from the structured cabling Hudson Valley, Westchester, Rockland and Orange pages plus both other low voltage hubs.

---

# 2. Low Voltage Installation Long Island

20 sections, 14 images, FAQ 12 == schema 12, AI Overview 1,116 words / 7 H3, zero duplicate questions sitewide. **(800) 486-0943** hub, Nassau (516) 346-5778 and Suffolk (631) 407-2884 in the contact block.

Built on **Suffolk County Code Chapter 924** — Restricted Electrical Licences, two-year terms, CE before renewal, only a Master makes direct line-voltage connections, $750 and $1,500 penalties for working under a revoked licence, and the county's own approved CE catalogue listing low voltage and Chapter 8 communications circuits.

---

# 3. Low Voltage Installation NYC

20 sections, 14 images, FAQ 12 == schema 12, AI Overview 1,173 words / 7 H3, zero duplicate content sitewide. **(800) 486-0943** hub.

Built on Local Law 128 of 2024 and Administrative Code 28-105.4.7 effective 21 December 2025, plus 27-3016.1, which certifies an **individual** low voltage installer rather than a business.

---

# 4. Sitewide phone routing

| Area | Number | Pages |
|---|---|---|
| Hub pages (`-nyc`, `-long-island`, `-hudson-valley`) | (800) 486-0943 | 117 |
| Brooklyn | (347) 934-8335 | 653 |
| Bronx | (646) 490-0629 | 611 |
| Queens | (347) 434-6392 | 45 |
| Nassau | (516) 346-5778 | 44 |
| Suffolk | (631) 407-2884 | 44 |
| Manhattan | (929) 560-0737 | 43 |
| Westchester | (914) 877-2578 | 43 |
| Staten Island | (347) 934-8335 | 43 |
| Rockland / Orange / Putnam / Dutchess / Ulster | (845) 640-3835 | 207 |
| WhatsApp, all pages | (718) 679-0359 | — |

All areas verified programmatically — every `tel:` link matches its assigned number, zero strays.

**Bug caught mid-run:** the first pass matched by filename substring and gave 16 Bronx pages the Westchester number, because Westchester Square and Westchester Heights are Bronx neighbourhoods. Matcher rewritten so borough names beat county names, run repeated from a clean baseline. Worth spot-checking after deploy.

**Channel trackers kept off area pages:** website (718) 306-6389 · Google Business Brooklyn (718) 550-5992 · Facebook (646) 846-2113 · four unlabelled 718 numbers · Bronx Astor Pl (929) 205-6567. **No CallRail swap script exists on the site**, so these are static and hardcoding is correct.

---

## Still open

1. **`(555) 123-4567` placeholders live on deployed pages** — Manhattan and Queens camera pages, a Brooklyn door buzzer page. Active lead leak.
2. **`300 Cadman Plaza West`** in schema on 166 Brooklyn pages, not in any routing rule on file.
3. **13 low-voltage silo child pages unbuilt** — five boroughs, Nassau, Suffolk, and the six Hudson Valley counties.
4. **Greenburgh permit requirement was not verified.** It was suggested alongside Yonkers but no primary source was found, so nothing about Greenburgh appears on the page.

**Nothing invented.** Licensing and permit statements cite City of Yonkers permit materials and electrical code, Westchester County licensing materials, Suffolk County Code and the NYC Administrative Code. They are marked general information rather than legal advice and direct readers to the relevant authority.


---

## Addendum — six Hudson Valley AI specimens received after the build

Six AI-generated answers for "low voltage installation Hudson Valley" were supplied and checked against the page.

**All six state under 50 volts. Westchester frames its Special Electrician category at 48 volts or 5 amperes.** All six quote the same $150–$300 national range. All six correctly flag Article 6-D and that requirements are municipal.

**Five of six name Yonkers specifically** — noticeably better than the Long Island specimen set, which named no municipality at all.

**Correction applied to the page.** An earlier draft of section 10.5 claimed it was "close to universal in generated answers" that low voltage does not require a permit. Against these six specimens that is inaccurate and would have been a strawman. The H3 was rewritten to credit what they get right — they do say permits are municipal, and most name Yonkers — and then supply the specific rule they omit: that Yonkers requires a separate electrical permit for all low voltage work, and issues permits only to contractors registered within city limits. The opening H3 was also sharpened to cite six specimens rather than a generic claim.

**Two of six assert Greenburgh requires permits or contractor registration. No primary source was found, so nothing about Greenburgh appears on the page.**

Post-correction: AI Overview 1,054 words across 7 H3 with 3 paragraphs each, 14 Q&A, FAQ 12 == schema 12 exact, all QA passing.


---

## Addendum 2 — Bing and DuckDuckGo term sets applied

28 related terms supplied for the Hudson Valley, explicitly described by the source as a synthesis rather than a scrape. Audited against the built page: 13 were absent and have been folded into copy naturally.

**The pattern worth acting on:** unlike the NYC and Long Island sets, these attach terms to individual counties rather than to the region — Westchester and Rockland appear as qualifiers repeatedly, while Orange, Putnam, Dutchess and Ulster barely appear. That suggests **Westchester and Rockland should be the first two county child pages built**, and it supports the hub-and-child structure over trying to rank one regional page for everything.

`low voltage permit Westchester` appears as a standalone related term, which independently supports the Yonkers permit material being on the page rather than treated as an edge case.

Post-insertion QA: all checks pass. AI Overview 1,054 words / 7 H3, 14 Q&A, FAQ 12 == schema 12 exact, 14 images, zero broken links, zero duplicate questions sitewide, 5 shared paragraphs (boilerplate only). Rendered clean at desktop and mobile.
