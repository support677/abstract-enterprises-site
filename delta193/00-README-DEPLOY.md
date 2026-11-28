# Cat6 silo complete — 16 of 16

**Cumulative.** Contains batches 3, 4 and 5, because none of them have been pushed yet. This zip supersedes `cat6-batch3-4-CHANGED-FILES.zip` — deploy this alone.

Copy the **contents of this folder** (not the folder itself) into `C:\dev\abstract-enterprises-site`, replace when asked, commit, push.

## The three new pages

- `/cat6-installation-putnam-county` — 845-640-3835 — $321/drop
- `/cat6-installation-dutchess-county` — 845-640-3835 — $333/drop
- `/cat6-installation-ulster-county` — 845-640-3835 — $333/drop

Dutchess and Ulster are the first pages at the 1.35 multiplier, the top of the table.

## The silo, finished

| Page | Price | Phone | Words |
|---|---|---|---|
| NYC hub | $272 | 800 + 347 | 13,225 |
| Long Island hub | $296 | 800 | 7,573 |
| Hudson Valley hub | $309 | 800 + 845 | 6,898 |
| Manhattan | $296 | 929-560-0737 | 6,908 |
| Brooklyn | $247 | 347-934-8335 | 6,420 |
| Queens | $272 | 347-434-6392 | 6,006 |
| Bronx | $272 | 646-490-0629 | 6,309 |
| Staten Island | $296 | 347-934-8335 | 6,262 |
| Nassau | $296 | 516-346-5778 | 6,891 |
| Suffolk | $296 | 631-407-2884 | 6,738 |
| Westchester | $309 | 914-877-2578 | 6,525 |
| Rockland | $309 | 845-640-3835 | 6,264 |
| Orange | $321 | 845-640-3835 | 6,595 |
| Putnam | $321 | 845-640-3835 | 5,512 |
| Dutchess | $333 | 845-640-3835 | 5,476 |
| Ulster | $333 | 845-640-3835 | 5,807 |

**109,409 words across sixteen pages.** All sixteen pass the full suite.

## Distinct theses

**Putnam** — the smallest county covered, where almost every job is a ten or twenty drop job. The discipline is not inventing line items on work that needs no rack and no lift, and documenting properly for buildings with no IT staff.

**Dutchess** — an unusually mixed commercial base. A converted mill floor, a 1980s Route 9 office plaza and a hospital campus within a few miles of each other, needing three different methods. Which building you occupy predicts the price better than which town.

**Ulster** — most buildings here have no cavity to run cable through. Stone and brick, plaster over lath, tin ceilings, exposed structure kept deliberately. Containment becomes the primary method rather than the fallback, and its routing is a design decision made before anything touches a wall.

## Duplicate scan

This batch opened at Dutchess vs Ulster 18, Putnam vs Ulster 14, Putnam vs Dutchess 13. After differentiation the worst pair across all sixteen pages is **11**, matching the ceiling passed on every prior batch.

## Bug caught again

All three shipped from the builder with a figure count mismatch — the hero image reused in a body section, leaving 11 references but only 10 unique files. Same failure as batch 4. Corrected to exactly 11 unique figures per page. Worth me hardening the builder against this rather than catching it in audit each time.

## Files

| Path | Count |
|---|---|
| 9 new pages (batches 3–5) | 9 |
| 4 pages corrected (batch 3 bug fixes) | 4 |
| `images/cat6/*.webp` | 99 |
| `sitemap.xml` · `_redirects` · `js/mega-nav.js` | 3 |

Sitemap now 1,928 URLs. 16 Cat6 redirect rules. All sixteen in mega-nav.

## Audit

Every page: market price consistent in hero, table and schema · phone rule enforced, no 800 outside the three hubs · zero unresolved tokens · FAQ 12=12 verbatim · 6 schema blocks, valid JSON · self-referencing canonicals · exactly 11 unique figures (15 on the NYC hub), all resolving · zero broken links · zero duplicate ids · zero `.html` links · 4.7/201 · NYS #12000287431 · registered in sitemap, redirects and mega-nav.
