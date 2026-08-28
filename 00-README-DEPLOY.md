# Network Cable Repair — LI + HV hubs and the first 3 borough children

Supersedes network-cable-repair-LI-HV-COMMIT.zip. If that one has not been pushed yet, use this instead — it contains everything in it plus the three borough pages.

## IMPORTANT: this is a GIT commit, not a Netlify drag-and-drop

Netlify auto-deploys from `main`. Dragging a zip into Netlify would break that link.

## Steps
1. GitHub Desktop -> **Branch -> Pull**.
2. Extract this zip **over** `C:\dev\abstract-enterprises-site`, keeping folder structure. Overwrite when asked.
3. Commit, then Push. Netlify deploys itself. Ctrl+Shift+R to hard-refresh.

## New pages (5)
| URL | Phone | GBP |
|---|---|---|
| /network-cable-repair-long-island   | (800) 486-0943 | Brooklyn |
| /network-cable-repair-hudson-valley | (800) 486-0943 | Bronx |
| /network-cable-repair-manhattan     | (929) 560-0737 | Bronx |
| /network-cable-repair-brooklyn      | (347) 934-8335 | Brooklyn |
| /network-cable-repair-queens        | (347) 434-6392 | Bronx |

Hubs carry the 800 line. Children carry direct lines only — the 800 appears nowhere on a child page
except inside the shared mega-nav component, which is sitewide chrome and identical on every page
including the existing door-buzzer children.

## New images (80)
/images/network-cable-repair/ — 16 per page, keyword+geo filenames, webp q82 at 1536px.
Same 16 source photos across the silo, area-suffixed. Fixed slot order, no rotation, no reuse within a page.

## Modified (3)
- sitemap.xml     1944 -> 1950 locs. Hubs at 0.9/weekly, children at 0.7/monthly. XML validated.
- _redirects      4289 -> 4295 rules. Forced 301! .html -> clean URL. Nothing deleted.
- js/mega-nav.js  networkcablerepair group with all 16 slugs. `node --check` passes.

This also fixes an existing defect: `/network-cable-repair-nyc` was live but had zero entries in
sitemap.xml, _redirects and mega-nav.js. It has been orphaned since it deployed. Now registered.

## Measured
| Page | Title | Meta | Words | Schema | FAQ | Images |
|---|---|---|---|---|---|---|
| Long Island   | 51 | 152 | 8,477 | 7/7 | 12=12 | 16 |
| Hudson Valley | 47 | 159 | 8,325 | 7/7 | 12=12 | 16 |
| Manhattan     | 50 | 139 | 8,196 | 7/7 | 12=12 | 16 |
| Brooklyn      | 47 | 142 | 7,928 | 7/7 | 12=12 | 16 |
| Queens        | 45 | 140 | 7,865 | 7/7 | 12=12 | 16 |

Every page: 4.7/201, Lic. #12000287431, self-referencing extensionless canonical, zero .html internal
links, breadcrumb position 3 = own URL, up-link to /network-cable-repair-nyc, all off-silo link targets
verified against the live repo.

## Dedup — body text only, chrome and constants excluded
Worst pair among the three new borough pages: 10 shared sentences (Manhattan/Brooklyn).
Highest anywhere in the silo: 14 (Long Island/Hudson Valley, previously audited and passed).
Residuals are locked constants: warranty clause, licence number, pricing footnote, section labels.

## Theses
- Manhattan — access economics and the lease line. Freight windows, COI, plaster with no cavity,
  plenum ceilings, four tenancies of abandoned cable, tenant-vs-base-building fault documentation.
- Brooklyn — conversion-stock pathway failure. Staples through jackets, chafe at steel edges, heat from
  adjacent services, cellar moisture in low-lying blocks, shared mixed-use panels, visible routing as design.
- Queens — one borough, four commercial economies. Shared risers in stacked buildings, the 100 m limit
  in the Maspeth/College Point industrial belt, vibration and machinery, Rockaways coastal corrosion.

## Link targets repointed to slugs that exist in the live repo
/structured-cabling-nyc      -> /structured-cabling-installation-nyc
/network-installation-nyc    -> exists, linked directly
/home-automation-nyc         -> /home-automation-installation-nyc

## Open items

**1. Warranty contradiction — still needs your decision.**
The live network-installation silo promises a **three-year** guarantee on AESS-supplied equipment and
labour. All five pages here state **one-year parts-only**. Both are live on the same site. Say which is
correct and I will align whichever set is wrong.

**2. 10 silo children still unbuilt** — linked from the hubs, will 404 until built:
bronx, staten-island, nassau-county, suffolk-county, westchester-county, rockland-county,
orange-county, putnam-county, dutchess-county, ulster-county.
CallRail map for those: Bronx 646-490-0629 | Staten Island 347-934-8335 | Nassau 516-346-5778 |
Suffolk 631-407-2884 | Westchester 914-877-2578 | other HV counties 845-640-3835.

**3. YouTube embed** is a reserved placeholder on all five pages pending a clip ID.

**4. Reciprocal cross-links.** The live network-installation pages link to structured cabling and Cat6
per area but not to network cable repair. Worth adding now that five repair pages exist.

## No files deleted.
