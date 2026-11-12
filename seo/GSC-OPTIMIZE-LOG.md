# GSC optimizer log

## 2026-11-02 — page-2 internal-link boost (manual run, tools/gsc_internal_links.py)
Source: Search Console Oct 3–31, queries at avg position 11–20 sorted by impressions. 3 contextual in-body links per target (§12.4).
| Target page | Keywords (pos, impr) | Linked from |
|---|---|---|
| /intercom-installation-nyc | building intercom nyc (20, 77), intercom installation nyc (17.1, 76), commercial intercoms nyc (16.7, 74) | intercom-installation-brooklyn-new-york, -manhattan-ny, -queens-ny |
| /intercom-repair-nyc | intercom replacement nyc (11.7, 90) | intercom-repair-manhattan, intercom-repair-brooklyn, door-buzzer-repair-nyc |
| /alarm-installation-nyc | alarm systems nyc (13.3, 82), alarm monitoring nyc (17.3, 83) | alarm-installation-brooklyn, alarm-installation-manhattan, home-automation-installation-nyc |
| /alarm-installation-queens | home security systems in queens, ny (15.1, 93) | security-camera-installation-queens, access-control-installation-queens, intercom-installation-queens-ny |
| /home-automation-installation-long-island | home automation long island (18.8, 84), control4 smart home long island (10.7, 67) | av-sound-installation-long-island, alarm-installation-long-island, home-automation-installation-nassau-county |
| /av-sound-installation-long-island | home theater installation long island ny (18.7, 69), av installation in long island (11.9, 81) | tv-installation-long-island, home-automation-installation-long-island, av-sound-installation-nassau-county |
Skipped: "commercial security cameras nyc" (homepage 11.4 / Bronx page 13.8 split; NYC commercial page sits at 38). Fix = strengthen /commercial-security-camera-installation-nyc first, then point links at it.
Re-check positions ~Nov 23.

## 2026-11-12 — daily zero-click + internal-link run (scheduled)
Source: Search Console (Composio), sc-domain property, Oct 12 – Nov 9 2026, query×page, 5,000 rows. 199 rows met zero-click (A), 309 met striking-distance (B).
**Attribution signal used:** seo/ATTRIBUTION.md generated 2026-11-11 (fresh). Service column is "(not set)" for nearly all paid jobs, so ranking used the **area** signal, last 30 days paid: Brooklyn $18,118 (top), Staten Island $6,886 + $2,069, White Plains $2,667 + Westchester $1,200, New York $1,754, Bronx $583. Unattributed (47 of 302 leads) counted for nothing.
Picks: 3 attribution-led (Brooklyn ×2, Westchester) + 2 ordinary picks by impressions (alarm NYC, access control NYC).

| # | Query (impr / pos / ctr) | Money page | Why picked | Changed |
|---|---|---|---|---|
| 1 | cctv installation brooklyn (129 / 6.7 / 0%); also cctv installation near me (64 / 7.2 / 0%) | /security-camera-installation-brooklyn-ny | Attribution: Brooklyn top paid area | Title "Brooklyn Security Camera Installation" → "CCTV & Security Camera Installation Brooklyn, NY \| AESS"; meta rewritten (CCTV + Bed-Stuy to Bay Ridge + booked within 2 hours); intro now opens "Need CCTV installation in Brooklyn?" with the answer in the first 40 words |
| 2 | access control installation brooklyn (113 / 5.4 / 0.9%) | /access-control-installation-brooklyn | Attribution: Brooklyn | Title → "Access Control Installation Brooklyn, NY \| Fob & Card"; meta rewritten (fob/card/keypad/cloud, brownstones/co-ops/offices, owner-run since 2002); intro opens "Access control installation in Brooklyn, NY: …" |
| 3 | alarm systems westchester (77 / 11.9 / 0%); commercial security systems westchester, ny (52 / 9.9 / 0%) | /alarm-installation-westchester-county | Attribution: White Plains + Westchester paid | Title → "Alarm Systems Westchester County, NY \| Home & Business"; meta rewritten (White Plains, Yonkers, New Rochelle) — also fixes the 149-char meta failure; intro opens "Looking for alarm systems in Westchester?" |
| 4 | alarm companies near me (155 / 6.2 / 0%); alarm companies (103 / 9.7 / 0%); alarm systems nyc (79 / 13.1 / 0%); alarm company nyc (62 / 13.6 / 0%) | /alarm-installation-nyc | Ordinary (highest-impression alarm cluster) | Title "Alarm Installation NYC" → "Alarm Company NYC \| Alarm System Installation, 5 Boroughs"; meta rewritten — fixes the 124-char meta failure; intro opens "Looking for an alarm company in NYC?" |
| 5 | access control installation nyc (165 / 7.0 / 0%); access control installation manhattan (72 / 6.1 / 0%) | /access-control-installation-nyc | Ordinary (highest-impression zero-click row on a service page) | Title → "Access Control Installation NYC \| Key Fob, Card & Keypad"; meta rewritten (lobbies, offices, garages, boroughs); intro opens "Access control installation in NYC: …" |

New intro copy uses only approved facts (§12.3: owner-operated since 2002, booked within 2 hours, NYS license #12000287431). No prices, phones, H1s or URLs changed.

**Internal links added (§12.4, one per source page, existing mention turned into a link):**
- /intercom-repair-brooklyn → /access-control-installation-brooklyn — "access control upgrades"
- /warehouse-security-camera-installation-brooklyn → /access-control-installation-brooklyn — "access control"
- /security-camera-installation-westchester-county-ny → /alarm-installation-westchester-county — "alarm system installation"
- /first-alert-camera-installation-prices-westchester-county → /alarm-installation-westchester-county — "alarm system"
- /commercial-security-systems-queens → /alarm-installation-nyc — "Commercial alarm systems"
- /commercial-security-systems-staten-island → /alarm-installation-nyc — "Commercial alarm systems"
- /commercial-security-systems-bronx → /alarm-installation-nyc — "Commercial alarm systems"
- /low-voltage-installation-manhattan → /access-control-installation-nyc — "Access control installation in NYC"
- /intercom-installation-nyc → /access-control-installation-nyc — "access control systems"
- /alarm-installation-manhattan → /access-control-installation-nyc — "access control systems"

Not linked: /security-camera-installation-brooklyn-ny got 0 new links. Every page that mentions Brooklyn CCTV or camera installation already links to it, except /wireless-camera-installation-brooklyn, where the only mention is that page's own hero line. /commercial-security-systems-westchester already linked to the Westchester alarm page, so it was skipped. "alarm systems brooklyn" (62 / 18.6) currently ranks the NYC alarm page. No Brooklyn-borough sources were pointed at the NYC page, so that keyword can consolidate on /alarm-installation-brooklyn later.

**check_page.py:** these legacy pages already failed before today (word count, forms, phone map, schema), and those failures are unchanged. The edits fixed 2 failures (the meta lengths on Westchester and NYC alarm). The only "new" lines are file-size clone-signature hits on alarm-installation-nyc, alarm-installation-manhattan and security-camera-installation-westchester-county-ny. Each page grew by a few hundred bytes and moved within 2 KB of an existing clone sibling. Wording share did not change: these pages already carry dozens of identical clone-signature lines, which needs a rewrite, not a link fix. Skipped all pages marked BUILDING in PAGE-QUEUE.md.
Re-check positions ~Dec 3.
