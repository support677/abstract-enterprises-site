# Network Cable Repair — 3 hubs + 5 borough children (8 of 16)

Supersedes network-cable-repair-5PAGE-COMMIT.zip. If that has not been pushed, use this instead — it contains everything in it plus Bronx and Staten Island.

## IMPORTANT: git commit, not a Netlify drag-and-drop
Netlify auto-deploys from `main`. Dragging a zip into Netlify would break that link.

1. GitHub Desktop -> **Branch -> Pull**
2. Extract this zip **over** `C:\dev\abstract-enterprises-site`, keep folder structure, overwrite
3. Commit, Push. Netlify deploys itself. Ctrl+Shift+R.

## New pages (7)
| URL | Phone | GBP |
|---|---|---|
| /network-cable-repair-long-island   | (800) 486-0943 | Brooklyn |
| /network-cable-repair-hudson-valley | (800) 486-0943 | Bronx |
| /network-cable-repair-manhattan     | (929) 560-0737 | Bronx |
| /network-cable-repair-brooklyn      | (347) 934-8335 | Brooklyn |
| /network-cable-repair-queens        | (347) 434-6392 | Bronx |
| /network-cable-repair-bronx         | (646) 490-0629 | Bronx |
| /network-cable-repair-staten-island | (347) 934-8335 | Brooklyn |

Hubs carry the 800. Children carry direct CallRail lines in body and schema. Zero foreign numbers on
any page outside the shared mega-nav component, which is sitewide chrome identical on all 2,531 pages.

## New images (112)
/images/network-cable-repair/ — 16 per page, keyword+geo filenames, webp q82 at 1536px, fixed slot order.

## Modified (3)
- sitemap.xml     1944 -> 1952 locs. Hubs 0.9/weekly, children 0.7/monthly. XML validated.
- _redirects      4289 -> 4297 rules. Forced 301! .html -> clean. Nothing deleted.
- js/mega-nav.js  networkcablerepair group, all 16 slugs. `node --check` passes.

Also fixes an existing defect: `/network-cable-repair-nyc` was live with zero entries in all three.

## Measured
| Page | Title | Meta | Words | Schema | FAQ | Images |
|---|---|---|---|---|---|---|
| Long Island   | 51 | 152 | 8,477 | 7/7 | 12=12 | 16 |
| Hudson Valley | 47 | 159 | 8,325 | 7/7 | 12=12 | 16 |
| Manhattan     | 50 | 139 | 8,196 | 7/7 | 12=12 | 16 |
| Brooklyn      | 47 | 142 | 7,928 | 7/7 | 12=12 | 16 |
| Queens        | 45 | 140 | 7,865 | 7/7 | 12=12 | 16 |
| Bronx         | 44 | 144 | 7,911 | 7/7 | 12=12 | 16 |
| Staten Island | 48 | 146 | 7,852 | 7/7 | 12=12 | 16 |

All: 4.7/201, Lic. #12000287431, self-referencing extensionless canonical, zero .html internal links,
breadcrumb position 3 = own URL, up-link to /network-cable-repair-nyc, off-silo link targets verified
against the live repo.

## Dedup — body only, chrome and constants excluded, 8x8
Worst pair anywhere: 14 (LI/HV, previously audited and passed).
Bronx: 0-7 against every other page. Staten Island: 0-11, highest against Brooklyn.
Bronx/Staten Island: 6.

## Theses
- Bronx — hostile environments. Cold-room transitions where condensation attacks the termination at the
  doorway, yard and gate entries with wrong jacket and no seal or bond, wash-down floors, corrosion
  lingering years after a wet cellar, and continuous operations that need quiet-shift zone-at-a-time work.
- Staten Island — the only borough where commercial property sits on its own lot. Runs leave the building
  routinely: jacket rating, sleeved and sealed penetrations, bonding, drip loops, buried conduit holding
  water, flood corrosion on the East and South Shores, distance in deep West Shore buildings, and visits
  scoped to finish in one trip because of the crossing.

## Open items
1. **Warranty contradiction** — live network-installation silo says three-year; all seven of these say
   one-year parts-only. Still needs your decision.
2. **8 children unbuilt** — nassau-county, suffolk-county, westchester-county, rockland-county,
   orange-county, putnam-county, dutchess-county, ulster-county. Linked from hubs, 404 until built.
   Nassau 516-346-5778 | Suffolk 631-407-2884 | Westchester 914-877-2578 | other HV 845-640-3835.
3. **YouTube embed** placeholder on all seven pending a clip ID.
4. **Reciprocal cross-links** — live network-installation pages do not yet link to network cable repair.

## No files deleted.
