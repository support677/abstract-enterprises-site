# AUDIT REQUEST — three new Cat6 pages (build 187)

You have already reviewed and passed `/cat6-installation-nyc`. These are three new pages built to that standard. Audit them the same way: adversarially, no compliments on the writing, exact sentence plus a corrected replacement wherever you find a problem.

- https://www.abstractenterprisessecuritysystems.com/cat6-installation-long-island
- https://www.abstractenterprisessecuritysystems.com/cat6-installation-hudson-valley
- https://www.abstractenterprisessecuritysystems.com/cat6-installation-manhattan

---

## 1. Business context

Abstract Enterprises Security Systems (AESS), licensed low-voltage contractor. NYS Low Voltage Contractor License #12000287431. Offices in Brooklyn and the Bronx. Serves the five boroughs, Long Island (Nassau, Suffolk) and the Hudson Valley (Westchester, Rockland, Orange, Putnam, Dutchess, Ulster).

These three sit under the passed `/cat6-installation-nyc` hub, which itself sits under `/structured-cabling-installation-nyc`.

**Published pricing, identical on all four pages** (real business rates): Cat5e $212/drop · **Cat6 $247/drop** · Cat6A $353/drop · Coax RG6 $212 · Speaker wire $176 · HDMI $282 · Fiber MM $494 · Fiber SM $564. Runs to 100 ft, including cable, plate, keystone, both terminations and testing. New construction −10%. Over 100 ft quoted on site.

**Word counts:** Long Island 7,724 · Hudson Valley 7,043 · Manhattan 7,068. The NYC hub is 13,156. These are shorter. That is a known gap, stated rather than hidden — assess whether they read thin or simply tighter.

---

## 2. The priority check: are these three distinct pages, or one page written three times?

This is the single most important thing to assess. The failure mode being guarded against is geo-swapping — the same copy with place names substituted.

Each page was written to a different thesis:

- **Long Island** — horizontal geometry. Buildings spread rather than stack, so the 90m limit is the central design question and closet count is settled with a tape measure at walkthrough. Attic-heat PoE failures. Warehouse/flex cabling.
- **Hudson Valley** — three building eras side by side: 1980s suburban office parks, 19th-century riverfront masonry conversions, new I-84/I-87 distribution construction. Campus and multi-building fiber backbone. Institutional/municipal work where test documentation is a contract deliverable.
- **Manhattan** — access governs, not distance. COI wording, freight windows, permitted hours, management approval, riser capacity, abandoned-cable removal. Four building types: Class A tower, pre-war, loft/landmarked, office-to-residential conversion.

**`DUPLICATE-REPORT.md` in this package lists every sentence of 10+ words appearing on more than one page.** First drafts shared 34–43 sentences per pair; after a differentiation pass that is down to 8–11. The remainder is claimed to be intentional constants — the verbatim warranty block, hero trust chips, the Fluke/testing sentence, the TIA-568/606 lines, the pre-wire line.

Verify that claim. For every entry in that report, say whether it is legitimately a constant that *should* be identical, or laziness that should have been rewritten. Then judge whether the three pages would read as genuinely different documents to someone who opened all three.

---

## 3. Local accuracy — flag anything wrong or misplaced

Every corridor, street, district and landmark should be real and correctly located. A fabricated or wrongly-placed place name is worse than none.

**Long Island** — Mineola, Garden City, Old Country Road, Hempstead, Westbury, Great Neck, Lake Success, Uniondale/Nassau Hub, Hicksville, Plainview, Routes 106/107, Route 110 through Melville/Farmingdale/Huntington Station, Long Island Innovation Park at Hauppauge, Islandia, Ronkonkoma/MacArthur Airport, Bohemia, Holbrook, Smithtown, Commack, Bay Shore, Patchogue, Sayville, Stony Brook, Riverhead/Route 58, North Fork, East End.

**Hudson Valley** — White Plains (Main St, Mamaroneck Ave), I-287 through Harrison/Purchase/Rye Brook, Elmsford/Greenburgh/Saw Mill River Rd, Yonkers (Getty Square, Ridge Hill, Central Park Ave), New Rochelle, Valhalla/Hawthorne, Tarrytown, Sleepy Hollow, Armonk, Mount Kisco, Port Chester, Mount Vernon; Route 59 through Nanuet/Spring Valley/West Nyack, Pearl River, Orangeburg, Nyack, Suffern, Valley Cottage, New City; Newburgh, Route 300, Stewart International, Montgomery, Maybrook, Chester, Middletown/Crystal Run, Goshen, Woodbury, Harriman; Brewster, Carmel, Mahopac; Poughkeepsie, Route 9/Fishkill/Wappingers Falls, East Fishkill, Hopewell Junction, Beacon; Kingston (Stockade District, Rondout, Route 209), New Paltz, Route 9W, Ulster Avenue.

**Manhattan** — Sixth/Park/Madison Avenues, Grand Central and E 42nd, Plaza District, Columbus Circle, Garment District, Penn Plaza, Hudson Yards, Manhattan West; Water/Broad/Wall Streets, Battery Park City, World Trade Center; SoHo (Broadway, Greene, Mercer), Tribeca, Ladies' Mile, Flatiron, Chelsea, Meatpacking; Union Square, NoMad, Murray Hill; Upper East Side medical corridor, Upper West Side, 125th Street, Washington Heights.

Also confirm: **no place, building or institution is presented as a customer or a completed project.** All should be geographic and building-condition context only.

---

## 4. Licensing claims — verify against primary sources

Each page makes specific licensing statements. These were researched from county code, not summarised from secondary sources, but verify them:

**Long Island page** — Suffolk County Code Chapter 563, Article XI, administered by the Department of Labor, Licensing and Consumer Affairs; broad definition of the electrical field; master and restricted licence classes; seven years' experience within the past ten; two-year terms; continuing education added by a 2017 amendment; and critically, the §563-125 carve-out that the county article does not apply inside any town or village that has enacted its own licensing legislation. Fines up to $750 first violation, $1,500 subsequent. Nassau via Office of Consumer Affairs.

**Hudson Valley page** — Westchester county trade licence via Department of Consumer Protection, permits through local building departments, and a limited licence class covering low voltage, alarm, signal, audio and telephone interconnect bounded by voltage and current limits. Rockland Chapter 250, Director of Consumer Protection, affirmative duty to notify an electrical inspection business, inspector verifies the installer's licence is active before issuing a certificate of approval. Orange via Consumer Affairs and Weights and Measures, Goshen. Putnam county-level; Dutchess and Ulster more municipal.

Flag anything overstated, out of date, or wrong. Also assess whether the framing stays properly conditional — the pages should tell the reader to confirm with the county rather than asserting what applies to their scope.

---

## 5. Technical accuracy

Same standard as the NYC hub audit. Verify every cabling claim against TIA-568 and current practice, including: Cat6 at 250 MHz vs Cat5e at 100 MHz; 10GBASE-T over Cat6 at ~55m and shorter under tight bundling and alien crosstalk; 90m horizontal + 10m cords = 100m channel; the claim that Cat6A does not extend the 90m limit; CMP/CMR/CM ratings and the return-air determination; shielded cable requiring bonding and grounding with an ungrounded shield acting as an antenna; CCA resistance and brittleness under PoE; 802.3af/at/bt device mapping; PoE heat raising resistance and reducing delivered power; permanent link vs channel; split pairs passing continuity; a damaged pair dropping gigabit to 100 Mbps; category being a property of the cable so Cat5e cannot be re-terminated to Cat6; Cat5e jacks on Cat6 cable producing a Cat5e channel.

**One page-specific claim to check hard:** the Hudson Valley page states that copper should not run between buildings on a campus, citing both the 90m limit and grounding problems between separate electrical services. Is that stated correctly?

---

## 6. Claims that could create liability

- No fabricated testimonials or customer stories. Service Standard sections are commitments, not reviews — confirm none reads as a testimonial.
- No invented statistics. Flag every number that is not a price, a technical spec or a standards figure. Note: the Long Island page cites published figures for the Hauppauge industrial park (1,000+ companies, ~55,000 employees, roughly one in twenty Long Island jobs) — check these are reasonable and appropriately hedged.
- Permit language must stay conditional throughout.
- No claims about named buildings, institutions or completed projects.
- The warranty block appears verbatim and must not be contradicted elsewhere.

---

## 7. SEO and schema

- Do the three pages compete with each other or with the NYC hub, or do they occupy distinct queries?
- Titles: Long Island 52 chars, Hudson Valley 54, Manhattan 50. Better options?
- Meta descriptions doing their job?
- Heading hierarchy, and does each H2 answer a question in its first sentence or two?
- Internal linking sensible, no cannibalisation?
- Schema: six blocks per page (LocalBusiness, Service, FAQPage, BreadcrumbList, ImageObject ×11, HowTo). All valid? FAQPage entries verbatim-matched to visible FAQ — spot-check several on each page. `aggregateRating` 4.7/201 placement. `hasOfferCatalog` with published prices — correctly structured, any risk?

---

## 8. Verdict

For each page separately:

1. Would it convince its actual buyer — a Long Island facilities manager, a Westchester school district IT director, a Manhattan GC?
2. Weakest section?
3. What would you cut?

And across all three: **which one is the weakest page, and why?**

---

## Files

- `cat6-long-island-text.txt`, `cat6-hudson-valley-text.txt`, `cat6-manhattan-text.txt` — full rendered copy, headings preserved, figure captions marked
- `cat6-long-island-schema.json`, `cat6-hudson-valley-schema.json`, `cat6-manhattan-schema.json` — six JSON-LD blocks each
- `DUPLICATE-REPORT.md` — every 10+ word sentence shared across pages, including against the passed NYC hub
