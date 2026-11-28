# MANIFEST — site-rebuild-186

**Date:** August 18, 2026
**Baseline:** site-rebuild-182-FULL.zip
**Supersedes:** site-rebuild-183, 184 and 185 — deploy 186 only
**Build:** Cat6 Installation NYC money page + site-wide wiring

---

## New page

`cat6-installation-nyc.html` — 169,953 bytes, **13,100 rendered visible words**

| Field | Value |
|---|---|
| Primary keyword | Cat6 Installation NYC |
| Slug | `/cat6-installation-nyc` |
| Title (53 chars) | Cat6 Installation NYC \| Data Cabling, Drops & Testing |
| Parent | `/structured-cabling-installation-nyc` (child, not a competing hub) |
| Mega-nav key | `cat6` |
| Phone | (800) 486-0943 — matches every other NYC silo page on this site |
| Rating | 4.7 / 201 |
| Design identity | Copper #B87333 on slate #1C2530, technical grid hero, Space Grotesk + JetBrains Mono |

### Section inventory
Hero + form-hero · What's included · Who this is for (6 audience blocks) · Cable selection (category, fire rating, shielding, conductor) · Drop planning + count table · Four installation methods · Termination & hardware · Pathways, separation, firestopping · Testing (dark section, page centerpiece) · Labeling & documentation · PoE · NYC building conditions · 14 field observations · Pricing table · 8 comparison cards · Project workflow (8 steps) + subcontractor + scheduling · Service Standard (6 cards) · Property types (8 verticals) · Upgrades/takeovers/MACs · Troubleshooting · Materials · FAQ (12) · People Also Ask (8) · Myths (7) · Coverage (25 areas) · Related services · form-detail + warranty · Footer

### Keyword targeting
Primary: Cat6 installation NYC. Secondary on-page: Cat6 cable installation NYC, Cat6 installer NYC, Cat6 cabling contractor NYC, Cat6 data drop installation NYC, Cat6 network drop installation NYC, commercial Cat6 installation NYC, office Cat6 installation NYC, Cat6 installation cost NYC, Cat6 cost per drop NYC, Cat6 cable certification NYC, Cat6 patch panel installation NYC, Ethernet cable installation NYC, Cat5e-to-Cat6 upgrade NYC, Cat6 installer near me.

Deferred by design: all Cat6A terms (sibling page), all fiber terms (existing silo), borough/neighborhood variants (coverage section only, no spokes built).

---

## Images — 15 total

All 15 are the dedicated Cat6 photos supplied Aug 18. Converted PNG → WebP at 1402×1122 (quality 84), total 2.4 MB. Stored in `images/cat6/`. Previous build's 11 renamed low-voltage reuses were deleted, not kept.

1 hero eager inside `<header class="hero">` below text and form, 14 inline lazy, non-consecutive, mixed layouts. Unique keyword filename / alt / title / caption per image. 15-entry ImageObject `@graph` as the 5th JSON-LD block.

| File | Shows | Placement |
|---|---|---|
| cat6-installation-nyc-ceiling-drop-cable-box.webp | ladder pull through open tile, Cat 6 CMR box in frame | hero (eager) |
| office-cat6-installation-nyc-corridor-crew-pull.webp | two-tech corridor pull off a box on a cart | full-width, scope |
| commercial-cat6-installation-nyc-metal-stud-rough-in.webp | cable through stud knockouts, pre-drywall | side-by-side, cable selection |
| cat6-data-drop-installation-nyc-dual-workstation-outlets.webp | finished DATA 1 / DATA 2 / VOICE plates at a desk | narrow, drop planning |
| cat6-wiring-nyc-fish-tape-conduit-entry.webp | fish tape into existing conduit on block wall | side-by-side, install methods |
| cat6-patch-panel-installation-nyc-network-room-rack.webp | labeled bundle dressed at the panel, network room | full-width, termination |
| cat6-installer-nyc-jhook-ceiling-pathway.webp | bundle laid into J-hooks, open ceiling | narrow, pathways |
| commercial-cat6-installation-nyc-workstation-outlet-bank.webp | run of outlets terminated along a bench | side-by-side, testing |
| cat6-keystone-termination-nyc-cubicle-outlet.webp | keystone punch-down at cubicle plate | narrow, documentation |
| cat6-floor-box-installation-nyc-conference-room.webp | jacks landed in a conference room floor box | narrow, PoE |
| cat6-cable-installation-nyc-conference-table-drop.webp | cable up through a table grommet, high-rise | full-width, NYC conditions |
| cat6-retrofit-installation-nyc-drywall-cut-in.webp | cutting in an old-work box, cable fished | narrow, field observations |
| office-cat6-installation-nyc-printer-data-jack.webp | labeled PRINTER DATA jack beside a copier | narrow, property types |
| cat6-voice-data-outlet-installation-nyc.webp | combined DATA + VOICE plate termination | inline, upgrades |
| cat6-network-drop-installation-nyc-workstation-outlet.webp | re-terminating a labeled workstation outlet | narrow, troubleshooting |

Every caption describes only what is visible. No image is claimed to show a specific customer, building or completed local project.

---

## Site-wide changes

- `js/mega-nav.js` — new `cat6` SVC group added above `lowvoltage`
- **1,639 pages** — desktop nav trigger inserted after Structured Cabling
- **1,634 pages** — mobile nav trigger inserted after Structured Cabling
- **1,579 pages** — cache version bumped `parking118` → `cat119`
- `index.html` — Cat6 entry added to the Structured Cabling area dropdown, and a link added to the Structured Cabling service blurb
- `structured-cabling-installation-nyc.html` — cable-specific link block added to the child page above the footer
- `sitemap.xml` — `/cat6-installation-nyc` added at priority 0.9
- `_redirects` — clean URL → `.html` **200 rewrite**, source route present exactly once, no 301, no reverse rule

---

## Post-build audit

| Check | Result |
|---|---|
| Rendered visible words | 13,100 (target 12,000–14,000) ✅ |
| Title length | 53 chars ✅ |
| JSON-LD blocks | 6 (LocalBusiness, Service, FAQPage, BreadcrumbList, ImageObject ×15, HowTo) ✅ |
| FAQ visible ↔ schema | 12 / 12, questions and answers verbatim-identical ✅ |
| Forms | 2 (form-hero, form-detail), unique `h-`/`d-` ids, hidden fields present, consent → `/privacy-policy` ✅ |
| Duplicate element ids | none ✅ |
| Figures | 15 (1 eager, 14 lazy), all image paths resolve, zero unused files ✅ |
| Alt / title attribute uniqueness | unique ✅ |
| Phone | `tel:+18004860943` in chrome and CTAs, `tel:+13479348335` as NYC direct in the body contact block; WhatsApp via `wa.me`, never tel-linked ✅ |
| Rating | 4.7 / 201 ✅ |
| Cache version | `cat119` only ✅ |
| Verbatim collision scan vs 6 siblings | 7 hits, all intended (verbatim warranty block + shared nav chrome). Zero content collisions ✅ |
| Fabricated claims | no testimonials, no invented statistics, no deployment or client claims, no named customers ✅ |
| Permit language | conditional throughout, AHJ + building management confirmation stated, nyc.gov/buildings linked ✅ |
| Brand names | listed as materials only; explicit statement that AESS is not a dealer or authorised partner ✅ |

---

## Open items for the next build

1. **Certifying tester question is still unanswered.** None of the 15 supplied photos shows a tester, so the tester-pass figure that was in 183 is gone. Title changed from "Certified Data Cabling" to "Data Cabling, Drops & Testing," and the word "Fluke" appears nowhere on the page. Remaining language is "tested," "test results," "permanent link" and "what an installer certifies" — defensible if every drop is genuinely tested and results are handed over. If testing is wiremap-only with no report given to the client, the testing section needs a further pass.
2. **Photos resolved.** All 15 are dedicated Cat6 images. No reused low-voltage stock remains on this page.
3. **Design identity** (copper/slate, Space Grotesk + JetBrains Mono) was chosen without sign-off. Easy to reskin — the palette is CSS variables at the top of the page's style block.
4. **Cat6A sibling page** not built. Recommended as Phase 2.
5. **Orange County calculator bug** — the hidden `slDiscount` span leaking raw HTML into the add-ons panel is untouched in this build and still open.

---

## 185 revision — post-review fixes to `/cat6-installation-nyc`

Targeted inserts only. No section rewritten, no unique content removed, no other file deleted.

1. **Testing section** — added: every drop wiremap-tested before the ceiling closes; where the job requires full certification, permanent links are certified with a Fluke DSX CableAnalyzer and the pass/fail report ships with the closeout package.
2. **Termination section** — added TIA-568 reference (T568B unless the building's existing standard governs) and TIA-606-style labeling and port-mapping practice.
3. **New construction** — added the pre-wire scheduling line: pathways stay open, cost per drop stays lower.
4. **Phone** — (800) 486-0943 retained in chrome and both CTAs; (347) 934-8335 added as "NYC direct" in the body contact block. No new numbers invented.
5. **Schema** — HowTo added as a 6th block (walkthrough → pull → terminate → test → label), including supplies, tools and the certification step. LocalBusiness, Service, FAQPage, BreadcrumbList and ImageObject all retained. BreadcrumbList parent confirmed as `/structured-cabling-installation-nyc`. FAQ still 12 = 12 with questions and answers verbatim-identical to the visible block. 4.7 / 201 and NYS license #12000287431 intact.
6. **Internal links** — up-link to `/structured-cabling-installation-nyc` confirmed. PoE paragraph now cross-links `/security-camera-installation-nyc`, `/access-control-installation-nyc` and `/intercom-installation-nyc`. All clean URLs, zero `.html` links in the body.

**Bug found and fixed during the pass:** the related-services list linked `/construction-site-camera-installation-nyc`, which does not exist. Corrected to `/construction-site-security-camera-installation-nyc`. Full internal-link sweep of the page now returns zero broken targets.

**Claim note:** the Fluke DSX language was inserted on instruction. It asserts that AESS certifies permanent links with a DSX and hands over pass/fail reports. If that is not accurate, this is the sentence to change.

---

## 186 revision — local detail on `/cat6-installation-nyc`

The thin coverage block was replaced with a full **"Where we install Cat6 in New York City"** section, borough by borough, written for a GC, IT manager or property manager rather than as a keyword list. The area-link pills below it are unchanged. No other content touched.

**Manhattan** — Midtown floors off Sixth and Park Avenues and the Grand Central / East 42nd Street corridor, where access and freight scheduling govern rather than the cable. Financial District along Water Street and Broad Street, including congested risers full of abandoned cable. Loft stock: cast-iron SoHo, Ladies' Mile on Broadway, the Flatiron District, the Garment District west of Seventh Avenue. The 125th Street corridor in Harlem.

**Brooklyn** — Downtown around MetroTech, Court Street and Jay Street. DUMBO warehouse conversions on Front and Water Streets. The industrial belt: Brooklyn Navy Yard, Industry City, the Sunset Park waterfront, Gowanus, East Williamsburg and Bushwick. Brownstone and row-house work borough-wide.

**Queens** — Long Island City at Jackson Avenue, Queens Plaza and Court Square. Flushing along Main Street and Roosevelt Avenue. Jamaica at Sutphin Boulevard and 165th Street, plus the Rockaway Boulevard logistics corridor toward JFK. Maspeth and Ridgewood industrial. Steinway Street in Astoria.

**Bronx** — the Fordham Road retail corridor. Hunts Point food distribution and surrounding warehousing, including cold rooms and wash-down areas. Mott Haven and Port Morris conversions along Bruckner Boulevard. Grand Concourse pre-war offices and institutional buildings. Riverdale residential.

**Staten Island** — West Shore industrial off South Avenue and Gulf Avenue, the Teleport and Corporate Park area in Bloomfield, distribution toward Charleston. St. George government and professional buildings around Borough Hall. Hylan Boulevard retail and medical.

Every corridor, street and district named is real and correctly located. No named building is presented as a customer or a completed project; all are geographic and building-condition context only.

**Standard going forward:** streets and landmarks are required on city hub pages, not only neighborhood and borough pages. Applied here; will be built into the Long Island and Hudson Valley hubs from the first draft rather than added afterward.
