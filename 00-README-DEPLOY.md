# Network Cable Repair — Long Island + Hudson Valley hubs

## IMPORTANT: this is a GIT commit, not a Netlify drag-and-drop

Netlify now auto-deploys from `main` (published deploy = main@25c15a3, "network cable repair nyc").
Dragging a zip into Netlify would break that link. Commit and push instead.

## Steps
1. GitHub Desktop -> **Branch -> Pull** (your local clone is behind origin/main).
2. Extract this zip **over** `C:\dev\abstract-enterprises-site`, keeping folder structure. Overwrite when asked.
3. GitHub Desktop shows the changed files. Commit, then Push.
4. Netlify deploys automatically. Hard-refresh with Ctrl+Shift+R.

## Files (37)

**New pages (2)**
- network-cable-repair-long-island.html
- network-cable-repair-hudson-valley.html

**New images (32)** — /images/network-cable-repair/
16 per page, keyword+geo filenames, webp q82 at 1536px wide.
Same 16 source photos as the NYC hub, area-suffixed. Fixed slot order, no rotation, no reuse within a page.

**Modified (3)** — these fix an existing defect, see below
- sitemap.xml     1944 -> 1947 locs. XML validated.
- _redirects      4289 -> 4292 rules. Nothing deleted.
- js/mega-nav.js  networkcablerepair group added, all 16 slugs. `node --check` passes.

## Defect this also fixes
`/network-cable-repair-nyc` is live but was never registered — 0 sitemap entries, 0 redirect rules,
0 mega-nav entries. It has been orphaned since it deployed. All three hubs are now registered.

## Locked parameters
- Phone (800) 486-0943 only on all three hubs. Zero 347 occurrences.
- 4.7 / 201. NYS Lic. #12000287431.
- $195/hr specialty, $585 three-hour minimum, replacement Cat6 drops from $175.
- Canonical www, extensionless, self-referencing. Zero .html internal links.
- 7 schema blocks per page: LocalBusiness, Service, FAQPage, BreadcrumbList, HowTo, ImageObject, Person.
- GBP routing: Long Island -> Brooklyn (#brooklyn). Hudson Valley -> Bronx (#bronx).

## Link targets verified against live repo
/network-installation-nyc            exists — repointed from /low-voltage-installation-nyc
/structured-cabling-installation-nyc exists — repointed from /structured-cabling-nyc
/home-automation-installation-nyc    exists — repointed from /home-automation-nyc

## Open items

**1. Warranty contradiction — needs your decision.**
The live network-installation silo states a **three-year** guarantee on AESS-supplied equipment and labour.
These three cable-repair hubs state **one-year parts-only**. Both are live. Tell me which is correct
and I will align whichever set is wrong.

**2. 13 silo children not built** — they are linked from the hubs and will 404 until built:
brooklyn, manhattan, queens, bronx, staten-island, nassau-county, suffolk-county,
westchester-county, rockland-county, orange-county, putnam-county, dutchess-county, ulster-county.
Children take DIRECT lines only, never the 800:
Nassau (516) 346-5778 | Suffolk (631) 407-2884 | HV counties (845) 640-3835 | boroughs (347) 934-8335

**3. YouTube embed** is a reserved placeholder on all three hubs pending a clip ID.

**4. Cross-link rule not yet applied.** The live network-installation pages cross-link to structured
cabling and Cat6 per county but not to network cable repair. Once the children exist, each area's
install page should point at its matching repair page.

## No files deleted.
