# MANIFEST — site-rebuild-187

**Date:** August 19, 2026
**Baseline:** site-rebuild-186
**Supersedes:** 183, 184, 185, 186 — deploy 187 only
**Build:** three new Cat6 pages + registration

---

## New pages

| URL | Words | Figures | Schema |
|---|---|---|---|
| `/cat6-installation-long-island` | 7,573 | 11 | 6 blocks |
| `/cat6-installation-hudson-valley` | 6,898 | 11 | 6 blocks |
| `/cat6-installation-manhattan` | 6,916 | 11 | 6 blocks |

Existing `/cat6-installation-nyc` unchanged except for three new cross-links down to the pages above.

**Word counts are below the 13,156 of the NYC hub.** Stated plainly rather than padded. All three are still substantially longer than every sibling page on the site (the Long Island structured cabling page is 5,556 words).

---

## Original content, not geo-swapped

Each page was written to a different thesis:

- **Long Island** — horizontal geometry. Buildings spread rather than stack, so the 90m limit becomes the central design question and closet count is settled with a tape measure at walkthrough. Covers the Suffolk Ch. 563 Art. XI licensing regime including the town/village carve-out, Nassau Office of Consumer Affairs, the Hauppauge industrial concentration, Route 110 corridor, attic-heat PoE failure mode.
- **Hudson Valley** — three building eras side by side: 1980s suburban office parks, 19th-century riverfront masonry conversions, and new I-84/I-87 distribution construction. Campus and multi-building fiber backbone design. County-level licensing across Westchester (Consumer Protection trade licence), Rockland (Ch. 250, third-party inspector verification), Orange (Consumer Affairs, Goshen). Institutional/municipal work where test documentation is a contract deliverable.
- **Manhattan** — access, not distance, governs. COI wording, freight windows, permitted hours, management approval, riser capacity and abandoned-cable removal. Four building types: Class A tower, pre-war, loft/landmarked, office-to-residential conversion. Deeper and entirely rewritten versus the borough paragraph on the NYC hub.

**Cross-page duplicate scan** (sentences ≥10 words): reduced from 43/34 shared pairs on first draft to 8–11 per pair after a differentiation pass. Remainder is intentional constants — the verbatim warranty block, hero trust chips, the Fluke/testing sentence, the TIA-568/606 lines and the pre-wire line, all of which are required to be identical.

---

## Local detail (required standard, built in from first draft)

- **Long Island** — Mineola, Garden City, Old Country Road, Hempstead, Westbury, Great Neck, Lake Success, Uniondale/Nassau Hub, Hicksville, Plainview, Route 106/107, Route 110 through Melville/Farmingdale/Huntington Station, Hauppauge Innovation Park, Islandia, Ronkonkoma/MacArthur, Bohemia, Holbrook, Smithtown, Commack, Bay Shore, Patchogue, Sayville, Stony Brook, Riverhead/Route 58, North Fork, East End.
- **Hudson Valley** — White Plains (Main St, Mamaroneck Ave), I-287 through Harrison/Purchase/Rye Brook, Elmsford/Greenburgh/Saw Mill River Rd, Yonkers (Getty Square, Ridge Hill, Central Park Ave), New Rochelle, Valhalla/Hawthorne, Tarrytown, Armonk, Mount Kisco, Port Chester, Mount Vernon; Route 59 through Nanuet/Spring Valley/West Nyack, Pearl River, Orangeburg, Nyack, Suffern, New City; Newburgh, Route 300, Stewart, Montgomery, Maybrook, Chester, Middletown/Crystal Run, Goshen, Woodbury, Harriman; Brewster, Carmel, Mahopac; Poughkeepsie, Route 9/Fishkill/Wappingers, East Fishkill, Beacon; Kingston (Stockade District, Rondout, Route 209), New Paltz, Route 9W.
- **Manhattan** — Sixth/Park/Madison, Grand Central and E 42nd, Plaza District, Columbus Circle, Garment District, Penn Plaza, Hudson Yards, Manhattan West; Water/Broad/Wall, Battery Park City, WTC; SoHo (Broadway, Greene, Mercer), Tribeca, Ladies' Mile, Flatiron, Chelsea, Meatpacking; Union Square, NoMad, Murray Hill; UES medical corridor, UWS, 125th Street, Washington Heights.

---

## Registration

- `sitemap.xml` — three URLs added, 1,916 total
- `_redirects` — clean URL → `.html` 200 rewrite for each, source route present exactly once
- `js/mega-nav.js` — all three added under the `cat6` key
- Nav triggers (desktop + mobile) present on the three new pages; cache `cat119`
- `/cat6-installation-nyc` now links down to all three from its related-services list

---

## Audit — all four Cat6 pages

| Check | LI | HV | MN | NYC |
|---|---|---|---|---|
| Title ≤60 chars | 52 | 54 | 50 | 53 |
| Self-referencing canonical | ✅ | ✅ | ✅ | ✅ |
| Schema blocks (LocalBusiness, Service, FAQPage, BreadcrumbList, ImageObject, HowTo) | 6 | 6 | 6 | 6 |
| FAQ 12 = 12, questions **and** answers verbatim | ✅ | ✅ | ✅ | ✅ |
| Figures, all unique, 1 eager | 11 | 11 | 11 | 15 |
| Duplicate element ids | 0 | 0 | 0 | 0 |
| Broken internal links | 0 | 0 | 0 | 0 |
| Missing image files | 0 | 0 | 0 | 0 |
| `.html` links in body | 0 | 0 | 0 | 0 |
| 4.7 / 201 + NYS #12000287431 | ✅ | ✅ | ✅ | ✅ |

Fixed during the pass: `/security-camera-installation-{area}` does not exist for any of the three markets — corrected to `/commercial-security-camera-installation-{area}`; `/intercom-installation-manhattan` corrected to `/intercom-installation-manhattan-ny`.

---

## Phone pattern

(800) 486-0943 in chrome, hero CTA and both forms on all three. Direct lines in the body contact block: Manhattan (347) 934-8335, Hudson Valley (845) 640-3835, Long Island none (routes to the toll-free line). No new numbers invented.

## Images

11 per page, sourced from the 15 supplied Cat6 photos, each copied under an area-specific keyword filename with alt, title and caption rewritten per market. Placement order and layout mix differ per page.

## Open

- Word counts below the NYC hub, as noted above.
- Per-drop pricing published identically across all four pages. If Long Island or Hudson Valley carries an area multiplier in the cabling calculator, these numbers need swapping.
