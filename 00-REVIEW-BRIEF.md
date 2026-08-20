# AUDIT REQUEST — Batch 3: Staten Island, Nassau, Westchester

- https://www.abstractenterprisessecuritysystems.com/cat6-installation-staten-island
- https://www.abstractenterprisessecuritysystems.com/cat6-installation-nassau-county
- https://www.abstractenterprisessecuritysystems.com/cat6-installation-westchester-county

Audit as before: adversarial, no compliments on the writing, exact sentence plus corrected replacement for anything wrong.

## 1. Two bugs were found on the LIVE site this round — please verify the fixes

**Template tokens printing literally.** Long Island, Hudson Valley and Manhattan were serving `${C6}` as raw text in the meta description and inside three FAQ answers each. Cause: those pages' bodies were f-strings but their meta descriptions and FAQ answers were plain strings, so the token never resolved. The builder now resolves tokens after assembly and throws a hard error if any survive.

**Stale base prices in prose.** Long Island and Manhattan said "the gap to Cat5e is $35 a drop" and "Cat6A earns its $353" — Brooklyn's figures — while their tables correctly showed $296 and $424.

Please confirm on every page that the price is consistent in five places: hero chip, pricing table, prose, FAQ answers, and `hasOfferCatalog` schema. Derived figures per market:

| Market | Cat6 | Cat5e gap | Cat6A |
|---|---|---|---|
| Brooklyn | $247 | $35 | $353 |
| Queens · Bronx · NYC | $272 | $39 | $388 |
| Manhattan · Long Island · Staten Island · Nassau | $296 | $42 | $424 |
| Hudson Valley · Westchester | $309 | $44 | $441 |

## 2. Phones

No 800 on any of the three. Staten Island 347-934-8335 (shared with Brooklyn until a dedicated SI line exists), Nassau 516-346-5778, Westchester 914-877-2578. Each page should carry exactly one number, including in the nav chrome.

## 3. Uniqueness — priority check

Theses: **Staten Island** — West Shore industrial and warehouse against a borough that is otherwise detached housing, plus ferry-dependent access. **Nassau** — suburban single and two-story commercial where horizontal distance drives closet count. **Westchester** — pre-war and mid-century corporate stock side by side, campus fiber between buildings.

`DUPLICATE-REPORT.md` covers all ten pages. First build had Long Island vs Nassau at 14, Hudson Valley vs Westchester at 14, Queens vs Staten Island at 12 — parent/child pairs pulling together. After differentiation the worst pair is 11.

For every entry, say whether it is a legitimate constant or laziness. Note: identical pricing tables between Long Island/Nassau and Hudson Valley/Westchester are correct, since they share a market multiplier.

## 4. Local accuracy

**Staten Island** — South Ave and Gulf Ave West Shore industrial, Teleport and Corporate Park in Bloomfield, Charleston distribution, St. George and Borough Hall, Hylan Blvd retail and medical, Richmond Ave.
**Nassau** — Mineola, Garden City, Old Country Rd, Hempstead, Westbury, Great Neck, Lake Success, Uniondale/Nassau Hub, Hicksville, Plainview, Routes 106/107, Route 110 edge at Farmingdale.
**Westchester** — White Plains (Main St, Mamaroneck Ave), I-287 through Harrison/Purchase/Rye Brook, Elmsford/Greenburgh/Saw Mill River Rd, Yonkers (Getty Square, Ridge Hill, Central Park Ave), New Rochelle, Tarrytown, Sleepy Hollow, Valhalla, Armonk, Mount Kisco, Port Chester, Mount Vernon.

Flag anything misplaced or fabricated. Confirm no place or institution is presented as a customer.

## 5. Technical accuracy

Same standard: Cat6 250 MHz vs Cat5e 100 MHz · 10GBASE-T ~55m · 90m + 10m cords · Cat6A not extending the limit · CMP/CMR/CM · shielded bonding and grounding · CCA under PoE · 802.3af/at/bt · permanent link vs channel · split pairs · category as a property of the cable.

Page-specific: **Staten Island** claims ferry and bridge access affect scheduling and crew logistics — reasonable? **Westchester** repeats the county trade-licence claim via Department of Consumer Protection with permits from local building departments — still accurate?

## 6. Liability

No fabricated testimonials, no invented statistics, conditional permit and licensing language, no named buildings as clients, warranty verbatim and uncontradicted.

## 7. Schema and SEO

Six blocks per page. FAQPage verbatim-matched to visible FAQ — spot-check several. GBP routing: Staten Island and Nassau to `#brooklyn` / 1282 Troy Ave, Westchester to `#bronx` / 460 E Fordham Rd. Confirm coherent. Titles under 60. Do the three compete with their parent hubs?

## 8. Verdict

Per page: convincing to its buyer? Weakest section? What to cut? Across the three, which is weakest?

## Files
Rendered text, six JSON-LD blocks and raw HTML for all three, plus the ten-page duplicate report.
