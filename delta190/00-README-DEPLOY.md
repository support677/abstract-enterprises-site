# Batch 2 final — Brooklyn, Queens, Bronx + repricing + CallRail phone routing

**43 files, 7.0 MB.** Copy into `C:\dev\abstract-enterprises-site` preserving folder structure, commit, push.

**Supersedes both earlier batch-2 zips.** Use only this one.

## Pages built
- `/cat6-installation-brooklyn`
- `/cat6-installation-queens`
- `/cat6-installation-bronx`

## Phone routing — new standing rule applied

**(800) 486-0943 on hub pages only. Borough pages carry their CallRail direct number and nothing else.**

| Page | Number on page |
|---|---|
| `/cat6-installation-brooklyn` | 347-934-8335 |
| `/cat6-installation-queens` | 347-434-6392 |
| `/cat6-installation-bronx` | 646-490-0629 |
| `/cat6-installation-manhattan` | 929-560-0737 |
| `/cat6-installation-nyc` (hub) | (800) 486-0943 |
| `/cat6-installation-long-island` (hub) | (800) 486-0943 |
| `/cat6-installation-hudson-valley` (hub) | (800) 486-0943 + (845) 640-3835 |

Each borough page carries **exactly one number**, verified across the whole document: hero CTA, both form footers, the contact block, the AJAX success message, LocalBusiness and Service schema `telephone`, **and the mega-nav chrome** — desktop CTA, mobile CTA and the emergency link. Zero occurrences of 486-0943 on any borough page.

Note the nav consequence: the four borough pages now show the borough number in the site header instead of the 800 line, unlike every other page on the site. That is deliberate — it keeps CallRail attribution clean, since a visitor who lands on the Bronx page and taps the header would otherwise be counted against the 800 line.

GBP schema routing is unchanged: Brooklyn `#brooklyn` / 1282 Troy Ave; Manhattan, Queens and Bronx `#bronx` / 460 E Fordham Rd. Only displayed numbers moved.

## Pricing — market multiplier

| Market | × | Cat5e | Cat6 | Cat6A |
|---|---|---|---|---|
| Brooklyn | 1.00 | $212 | **$247** | $353 |
| Queens · Bronx · NYC | 1.10 | $233 | **$272** | $388 |
| Manhattan · Long Island | 1.20 | $254 | **$296** | $424 |
| Hudson Valley | 1.25 | $265 | **$309** | $441 |

Applied in the price table, hero chip, prose, FAQ answers and `hasOfferCatalog` schema, with the Cat5e-to-Cat6 gap recalculated per market.

**Source-level fix this round:** the earlier repricing was patched into the built HTML, not the page sources. Rebuilding Manhattan for the phone change silently reverted it to $247. All page sources are now multiplier-driven, so a rebuild can never regress the price again. Long Island and Hudson Valley were converted the same way even though they did not need rebuilding.

## Files

| Path | Count |
|---|---|
| `cat6-installation-{brooklyn,queens,bronx}.html` | 3 new |
| `cat6-installation-{nyc,manhattan,long-island,hudson-valley}.html` | 4 updated |
| `images/cat6/*.webp` | 33 |
| `sitemap.xml` · `_redirects` · `js/mega-nav.js` | 3 |

## Audit — all seven pages pass

Price consistent in hero, table and schema · phone rule enforced (hubs 800, boroughs single direct, no 845 outside Hudson Valley) · FAQ 12=12 verbatim · 6 schema blocks, all valid JSON · self-referencing canonicals · all images resolve · zero broken links · zero duplicate ids · zero `.html` links · 4.7/201 · NYS #12000287431 · registered in sitemap, redirects, mega-nav.

Cross-page duplicate scan unchanged after rebuild: worst pair 11 (NYC vs Long Island), all constants.
