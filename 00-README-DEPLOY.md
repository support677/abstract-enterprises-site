# Network Cable Repair — 3 hubs + 5 boroughs + 6 counties (14 of 16)

Supersedes network-cable-repair-10PAGE-COMMIT.zip. If that has not been pushed, use this instead.

## IMPORTANT: git commit, not a Netlify drag-and-drop
Netlify auto-deploys from `main`. Dragging a zip into Netlify would break that link.

1. GitHub Desktop -> **Branch -> Pull**
2. Extract this zip **over** `C:\dev\abstract-enterprises-site`, keep folder structure, overwrite
3. Commit, Push. Netlify deploys itself. Ctrl+Shift+R.

## New pages (13)
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
| /network-cable-repair-rockland-county    | (845) 640-3835 | Bronx    | Hudson Valley hub |
| /network-cable-repair-orange-county      | (845) 640-3835 | Bronx    | Hudson Valley hub |
| /network-cable-repair-putnam-county      | (845) 640-3835 | Bronx    | Hudson Valley hub |

County pages breadcrumb to their regional hub. Hubs carry the 800; children carry direct CallRail lines
in body and schema. Zero foreign numbers on any page outside the shared mega-nav component.
Rockland, Orange and Putnam share one CallRail line by design, so CTA copy carrying that number is
identical across those three by necessity.

## New images (208)
/images/network-cable-repair/ — 16 per page, keyword+geo filenames, webp q82 at 1536px, fixed slot order.

## Modified (3)
- sitemap.xml     1944 -> 1958 locs. Hubs 0.9/weekly, children 0.7/monthly. XML validated.
- _redirects      4289 -> 4303 rules. Forced 301! .html -> clean. Nothing deleted.
- js/mega-nav.js  networkcablerepair group, all 16 slugs. `node --check` passes.

Also fixes an existing defect: `/network-cable-repair-nyc` was live with zero entries in all three.

## Measured — the three new pages
| Page | Title | Meta | Words | Schema | FAQ | Images | Parent |
|---|---|---|---|---|---|---|---|
| Rockland County | 48 | 137 | 7,538 | 7/7 | 12=12 | 16 | Hudson Valley hub |
| Orange County   | 49 | 149 | 7,651 | 7/7 | 12=12 | 16 | Hudson Valley hub |
| Putnam County   | 48 | 138 | 7,432 | 7/7 | 12=12 | 16 | Hudson Valley hub |

All fourteen: 4.7/201, Lic. #12000287431, self-referencing extensionless canonical, zero .html internal
links, breadcrumb position 3 = own URL, all off-silo link targets verified against the live repo.

## Dedup — body only, chrome, shared-phone CTA copy and constants excluded, 14x14
Worst pair anywhere: 14 (Staten Island/Suffolk).
New pages: Rockland/Orange 11, Rockland/Putnam 7, Orange/Putnam 7.
Rockland/Orange and Orange/Putnam started at 25 and 27 and took one rewrite pass each.

## Theses
- Rockland — the continuous plaza ceiling. Demising walls in strip retail stop at the grid, so the void
  above runs the length of the building and your cable crosses units you have never entered. Damage from
  neighbouring fit-outs, the shared landlord utility room, and marking runs so they read as owned.
- Orange (New York, not the six other US Orange Counties — disambiguation carried in intro, FAQ and an
  AI Overview section) — high-bay distribution. Roof-deck cable sitting in the warmest air in the
  building, lift access as the governing cost, improvised support on sprinkler pipe and purlin edges,
  and mechanical damage on descending drops.
- Putnam — telling a power event from a cable fault. Long overhead feeders under heavy tree cover,
  equipment restarting in the wrong order after weather, remote triage before dispatch, boot-order
  guidance and battery backup, and findings written for owners with no technical staff.

## Open items
1. **Warranty contradiction** — live network-installation silo says three-year; all fourteen of these say
   one-year parts-only. Still needs your decision.
2. **2 children unbuilt** — dutchess-county, ulster-county. Linked from the Hudson Valley hub, 404 until
   built. Both take 845-640-3835.
3. **YouTube embed** placeholder on all thirteen pending a clip ID.
4. **Reciprocal cross-links** — live network-installation pages still do not link to network cable repair.

## No files deleted.
