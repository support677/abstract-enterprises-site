# Network Cable Repair — 3 hubs + 5 boroughs + 3 counties (11 of 16)

Supersedes network-cable-repair-7PAGE-COMMIT.zip. If that has not been pushed, use this instead.

## IMPORTANT: git commit, not a Netlify drag-and-drop
Netlify auto-deploys from `main`. Dragging a zip into Netlify would break that link.

1. GitHub Desktop -> **Branch -> Pull**
2. Extract this zip **over** `C:\dev\abstract-enterprises-site`, keep folder structure, overwrite
3. Commit, Push. Netlify deploys itself. Ctrl+Shift+R.

## New pages (10)
| URL | Phone | GBP | Parent |
|---|---|---|---|
| /network-cable-repair-long-island        | (800) 486-0943 | Brooklyn | NYC hub |
| /network-cable-repair-hudson-valley      | (800) 486-0943 | Bronx    | NYC hub |
| /network-cable-repair-manhattan          | (929) 560-0737 | Bronx    | NYC hub |
| /network-cable-repair-brooklyn           | (347) 934-8335 | Brooklyn | NYC hub |
| /network-cable-repair-queens             | (347) 434-6392 | Bronx    | NYC hub |
| /network-cable-repair-bronx              | (646) 490-0629 | Bronx    | NYC hub |
| /network-cable-repair-staten-island      | (347) 934-8335 | Brooklyn | NYC hub |
| /network-cable-repair-nassau-county      | (516) 346-5778 | Brooklyn | Long Island hub |
| /network-cable-repair-suffolk-county     | (631) 407-2884 | Brooklyn | Long Island hub |
| /network-cable-repair-westchester-county | (914) 877-2578 | Bronx    | Hudson Valley hub |

County pages breadcrumb to their regional hub, not to NYC. Hubs carry the 800; children carry direct
CallRail lines in body and schema. Zero foreign numbers outside the shared mega-nav component.

## New images (160)
/images/network-cable-repair/ — 16 per page, keyword+geo filenames, webp q82 at 1536px, fixed slot order.

## Modified (3)
- sitemap.xml     1944 -> 1955 locs. Hubs 0.9/weekly, children 0.7/monthly. XML validated.
- _redirects      4289 -> 4300 rules. Forced 301! .html -> clean. Nothing deleted.
- js/mega-nav.js  networkcablerepair group, all 16 slugs. `node --check` passes.

Also fixes an existing defect: `/network-cable-repair-nyc` was live with zero entries in all three.

## Measured — the three new county pages
| Page | Title | Meta | Words | Schema | FAQ | Images | Breadcrumb parent |
|---|---|---|---|---|---|---|---|
| Nassau County      | 48 | 144 | 7,553 | 7/7 | 12=12 | 16 | Long Island hub |
| Suffolk County     | 49 | 144 | 7,635 | 7/7 | 12=12 | 16 | Long Island hub |
| Westchester County | 46 | 147 | 7,424 | 7/7 | 12=12 | 16 | Hudson Valley hub |

All eleven: 4.7/201, Lic. #12000287431, self-referencing extensionless canonical, zero .html internal
links, breadcrumb position 3 = own URL, all off-silo link targets verified against the live repo.

## Dedup — body only, chrome and constants excluded, 11x11
Worst pair anywhere: 14 (LI/HV and SI/Suffolk).
New county pages: Nassau/Westchester 12, Nassau/Suffolk 10, Suffolk/Westchester 8.
Nassau/Suffolk took two rewrite passes to come down from 31.

## Theses
- Nassau — channel headroom. The county's medical and professional density means drops that pass by a
  whisker carry email all year and stall an imaging transfer in August. Plus telecom rooms built in the
  1960s for a telephone board, coupler extensions from repeated fit-outs, and converted-residential
  village commercial with no equipment room.
- Suffolk — the flex bay. Front office, rear warehouse, one telecom point at the front and 200 feet to
  the dock. Distance, tenant churn leaving coupler extensions, mezzanine chafe, unconditioned rear-bay
  temperature swing, and visits scoped to finish because the county is 86 miles long.
- Westchester — re-tenanted single-occupier office stock. Buildings cabled for one company in 1978 and
  now shared by eight: shared closets with controlled access, four decades of abandoned cable, damage
  from neighbouring fit-outs, mixed-category channels, and the closet legend as the durable deliverable.

## Open items
1. **Warranty contradiction** — live network-installation silo says three-year; all eleven of these say
   one-year parts-only. Still needs your decision.
2. **5 children unbuilt** — rockland-county, orange-county, putnam-county, dutchess-county,
   ulster-county. Linked from the Hudson Valley hub, 404 until built. All five take 845-640-3835.
3. **YouTube embed** placeholder on all ten pending a clip ID.
4. **Reciprocal cross-links** — live network-installation pages still do not link to network cable repair.

## No files deleted.
