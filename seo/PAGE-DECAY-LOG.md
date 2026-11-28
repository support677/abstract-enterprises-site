# Page decay log (weekly "pages that slipped" refresh)

Weekly scheduled task, Mondays. Compares the last 28 days of Search Console data with the previous 28 days (and the same window last year), flags pages that are losing ground, diagnoses why, and refreshes up to 5 pages. The daily GSC optimizer owns zero-click titles/metas, regex plays and cannibalization; this log only covers pages that slipped over time.

## Lessons (read before every run)

1. **Check where a lost query went before rewriting the page.** In run 1, most "lost" queries had moved to a sibling page on our own site (borough page to NYC hub, hub to neighborhood pages, homepage to the borough camera page). Pull the query × page table for the lost query first. If our own page took it, that's silo redistribution: fix it with one contextual link to the page that should own the query, and leave the content alone.
2. **Legacy borough pages share their Q&A with dozens of neighborhood siblings.** /structured-cabling-installation-brooklyn shares 19 Q&As with 58 neighborhood pages (check_page.py "question duplicated on sibling"). A refresh can add unique sections, but the shared Q&A blocks stay until the page gets a full blueprint REBUILD. Flag those pages to Anwar instead of editing the shared text page by page.
3. **The big impression swings come from one head term, not from pages decaying.** In run 1, "security camera" alone accounted for about 47,000 of the roughly 67,000 lost page-level impressions (the Bronx camera URL and the GBP homepage link). It had zero clicks in both periods. Leave those swings out when you rank pages by loss, so they don't crowd out real money-page drops.
4. **Click counts per page are small (most pages get 0 to 5 a month).** A drop like 4 → 1 is noise on its own. Rank by lost clicks, but require a matching position drop on the page's own head query before you call it decay.

## Recovery checks (refreshes 4–8 weeks old)

| Refreshed | Page | Check due | Baseline (prev 28d → cur 28d at refresh) | Result |
|---|---|---|---|---|
| 2026-11-23 | /intercom-repair-nyc | Dec 21 – Jan 18 | clicks 3 → 0; "intercom replacement nyc" pos 11.4 → 18.2; "intercom repair manhattan" 21.9 → 50.5 | pending |
| 2026-11-23 | /structured-cabling-installation-brooklyn | Dec 21 – Jan 18 | clicks 4 → 1; "home network installation brooklyn" pos 2.6 → 6.0; "ethernet wiring near me" pos 4.9 → not shown | pending |
| 2026-11-23 | /parking-lot-camera-installation-brooklyn | Dec 21 – Jan 18 | clicks 1 → 0; "parking lot video surveillance nyc" pos 6.1 → 17.8 (Queens/Bronx siblings now rank 7.0 / 9.7) | pending |

Run 1 had no earlier refreshes from this task to check. Related: the daily optimizer's Nov 2 internal-link boost pointed 3 links at /intercom-repair-nyc for "intercom replacement nyc" (11.7 at the time). That query has since slipped to 18.2, so links alone did not hold it. It falls in the 4–8 week window from Nov 30 to Dec 28.

---

## 2026-11-23 — run 1

**Not done this run:**
- Only 3 pages refreshed (cap is 5). Every other flagged page was too soon, seasonal/redistribution, or had no real position loss. Details below.
- Ahrefs GSC tools returned "Insufficient plan", so data came from the Composio Search Console fallback (sc-domain property, openeyesales@gmail.com). Ahrefs serp-overview was unavailable for the same reason, so SERPs came from Firecrawl search (top 8 per query).
- /structured-cabling-installation-brooklyn and /intercom-repair-nyc are still legacy pages (about 6,500–7,200 words, 2 images, shared sibling Q&A). This run added unique sections. They still need a full blueprint REBUILD, and that decision is Anwar's.
- IndexNow not pinged (the site host is blocked from this session's shell). URLs added to GOOGLE-SUBMIT.md as QUEUED for the evening request-indexing run.

**Data windows:** current Oct 23 – Nov 19 2026 vs previous Sep 25 – Oct 22 2026; last year Oct 23 – Nov 19 2025 vs Sep 25 – Oct 22 2025.

**Site-wide check (not a Google-update pattern):**
- Page-level totals: clicks 379 → 385 (+2%), impressions 203,406 → 136,203 (−33%), avg position 12.6 → 17.6. Last year in the same windows: 139 → 138 clicks, 59,473 → 59,654 impressions (flat).
- Weekly impressions fell from about 100k/week (early Sept) to about 25–35k/week (mid Oct onward). Clicks held at 78–126 a week the whole time.
- 56 of 143 pages with ≥200 earlier impressions dropped 30%+ (39%, not most). Most of the impression loss is one query, "security camera": /security-camera-installation-bronx 35,446 → 3,268 and /?utm_campaign=gmb 15,295 → 63, with 0 clicks in both periods. The average position rose because thousands of new pages now earn deep impressions.
- Verdict: no site-wide decay event. Clicks are steady. The impression drop is a head term with no clicks.
- Technical checks: URL Inspection on /, /intercom-repair-nyc, /structured-cabling-installation-brooklyn, /parking-lot-camera-installation-brooklyn and /security-camera-installation-bronx-ny all came back indexed, fetch OK, robots allowed, user canonical = Google canonical. /security-camera-installation-bronx = "Page with redirect" to -bronx-ny (expected).
- **FLAG for Anwar (indexing):** the Search Console sitemap report shows sitemap.xml with **3,105 URLs submitted and 14 indexed**, 0 errors, downloaded 2026-11-23. Search Console's sitemap count often runs low, but this gap fits his Nov 11 concern about crawled-not-indexed pages. It is bigger than any single page's decay.
- **FLAG for Anwar (deploys):** the evening "Search submit" job has pushed a commit that deleted the whole site three times: 05bcdf77 (Nov 8, 3,424 files), ab0a2323 (Nov 9, 3,424 files) and 3fa8c4db (Nov 17, 3,924 files). Each was restored 27–72 seconds later. Netlify deploys every push to main, so a site-wide 404 deploy may have gone live for a minute or two each time. The page guard catches it afterwards. The job itself needs fixing so it stops committing deletions.

**Filters applied:**
- TOO SOON: alarm-installation-nyc (GSC optimizer Nov 12), construction-site-security-camera-installation-nyc (optimizer Nov 13), security-camera-installation-manhattan-ny (CCTV/Max-daily content edits Nov 16 + Nov 21), home-automation-installation-{nyc,brooklyn,long-island,staten-island} (new photos + content Nov 9), fire-alarm-installation-queens-new-york (Nov 19–20 builds), alarm-installation-midwood-brooklyn-ny (factory rebuild Nov 12). Site-wide sweeps (Nov 17 restore of the deleted tree, Nov 19 free-assessment wording, Nov 14 "No AESS") and factory sibling-link wiring (+1–2 lines) were **not** counted as changes, otherwise every page on the site would be "too soon".
- SEASONAL: none confirmed. The homepage was up year over year last year (71 → 75 clicks in the same windows) and is down this year, so it isn't seasonal. Other pages have no year-ago data (built in 2026).
- REDISTRIBUTION (own pages took the query; logged, not rewritten):
  - Homepage / : 61 → 50 clicks. "security camera installation brooklyn" moved to /security-camera-installation-brooklyn-ny (25.0 → 5.4), which the daily optimizer retitled Nov 12. That's the intended page. "apartment security camera systems nyc" moved to the borough camera pages. The /?utm_campaign=gmb (GBP link) impressions fell 30,253 → 529, a Maps/GBP visibility change. The Local Falcon / GBP work covers that, not page copy.
  - /commercial-security-camera-installation-brooklyn: "commercial surveillance camera installation" moved to /commercial-security-camera-installation-nyc (now 5.3). Correct owner, left alone.
  - /security-camera-installation-bronx (301 to -bronx-ny): head-term loss only, see above.
- Structured cabling Nassau (5 → 1 clicks) and Staten Island (4 → 0): "network cabling nassau county" 2.2 → 3.0 and "network cabling long island" 6.8 → 6.4, no real slide on the head terms. The losses are generic "near me" phrases. Watch next week.

**Refreshed (3):**

| Page | Drop (prev → cur 28d) | Cause found | What changed |
|---|---|---|---|
| /intercom-repair-nyc | clicks 3 → 0, impr 706 → 652; "intercom replacement nyc" 11.4 → 18.2, "intercom repair manhattan" 21.9 → 50.5, "intercom repair nyc" 21.1 → 22.7 | Top results (Vertex "intercom replacement NYC", Connextivity repair-vs-replace guide updated Nov 5 2026, Reddit r/AskNYC) answer **repair or replace** with decision rules, HPD obligations and lifespan. Our page had none of it. Neighborhood pages (Cadman Plaza, Clinton Hill door buzzer) now split the NYC query. The page also carried a stale "14+ years" claim. | New section "Intercom Repair or Intercom Replacement in NYC? How We Decide": answer-first decision rule, repair/retrofit/replace table, HPD correction periods (Class A 90 days / B 30 / C 24 h) and the 70-day deemed-complied rule cited to nyc.gov HPD pages, our need-access-to-every-affected-unit rule, 3 first-hand job notes (DoorBird two-door replacing DoorKing, 3-unit Akuvox Wi-Fi retrofit, 42-unit Comelit three-brand comparison; no names or addresses), contextual links to /intercom-repair-manhattan and /intercom-installation-nyc. 3 new FAQs (visible + FAQPage schema). "14+ years" → "owner-run since 2002 (25+ years)". Visible "Last updated November 23, 2026" + Service dateModified. No new prices (it points to the existing pricing section). Inbound link added from /intercom-installation-nyc. check_page --legacy: no new failures (word count 6,321 → 7,174; pre-existing fails unchanged). |
| /structured-cabling-installation-brooklyn | clicks 4 → 1, impr 590 → 380; "home network installation brooklyn" 2.6 → 6.0, "ethernet wiring near me" 4.9 → gone, "structured wiring near me" 3.7 → 4.0 | Residential intent: those searches want home ethernet and Wi-Fi wiring, but the page is written for offices. Top results are home-network services, Thumbtack/Yelp lists and Reddit "rewiring a house in NYC". The page also said every run is Fluke-certified before we leave, which contradicts the Oct 27 rule that certification is a paid add-on. It also said "2025–2026". The page shares 19 Q&As with 58 Brooklyn neighborhood siblings. | New section "Home Network Installation in Brooklyn: Ethernet Wiring for Brownstones, Row Houses and Apartments": answer-first with the existing on-page prices ($175+ Cat6 drop, $300 Wi-Fi AP drop), sourced stat (51.3% of Kings County housing built 1939 or earlier, Cornell PAD / ACS), first-hand FiOS ONT-to-closet job, routing in old houses, quote limits (runs over 100 ft = extra home run, Cat6 vs Cat6A quoted separately, Fluke report = add-on). 2 new FAQs (visible + schema). The Fluke sentence corrected, "2025–2026" → "2026", visible "Last updated". Links to /structured-cabling-installation-nyc and /network-cable-repair-brooklyn. check_page --legacy: no new failures. |
| /parking-lot-camera-installation-brooklyn | clicks 1 → 0, impr 316 → 190; "parking lot video surveillance nyc" 6.1 → 17.8, "parking lot surveillance cameras nyc" 8.4 → gone | The lost queries are NYC-wide. Our Queens (#7 on the live SERP) and Bronx parking pages now take them. The NYC hub doesn't rank for them. The top 2 live results lead with live talk-down / 24/7 operators. dateModified was July 24. | Paragraph on two-way talk and siren-and-strobe cameras (products we install, no prices), contextual link "parking lot video surveillance in NYC" to /parking-lot-camera-installation-nyc so the hub can own the NYC phrase, 1 new Brooklyn FAQ (visible + schema), dateModified → 2026-11-23 + visible "Last updated". Inbound link added from /security-camera-installation-brooklyn-ny ("parking areas"). check_page (full): no new failures. Pre-existing §15 fails remain (no parking price page mapped, answer-first sentence, cross-links to 6 Hudson Valley county siblings). |

**Copy rules:** ranking-principles (answer first, first-hand jobs, 2 sourced facts on the intercom page, 1 on the cabling page) and stop-slop (no em dashes, no filler) applied to the new copy. No H1s, URLs or titles changed. No pages deleted or renamed. No "AESS" in page text. No owner byline. Only prices already on each page.

**Wiring:** sitemap.xml lastmod → 2026-11-23 for all 3. GOOGLE-SUBMIT.md: 3 URLs QUEUED.

**Recommendations for Anwar:**
1. Queue full blueprint REBUILDs for /structured-cabling-installation-brooklyn and /intercom-repair-nyc (borough/hub pages, so they come first under PAGE PRIORITY). The refresh helps, but the shared sibling Q&A and the 6–7k-word legacy body will keep dragging them down.
2. Look at the sitemap report: 3,105 submitted / 14 indexed.
3. Fix the evening Search-submit job that keeps committing whole-site deletions.

---

## Competitor-watch candidates (added by the weekly competitor sitemap watch)

Pages of ours that a competitor page matches, where the competitor's version is newer (or deeper). The decay task decides whether to refresh them; the watch never rewrites them.

| Added | Our page (sitemap lastmod) | Competitor page (lastmod) | Why | Angles they cover (don't copy wording) |
|---|---|---|---|---|
| 2026-11-24 | /door-buzzer-repair-nyc (2026-05-03) | imperasecurity.com/door-buzzer-repair-nyc (2026-11-16) | Newer; theirs is shorter (~1,600 words, scraped) | Door-hardware-first diagnosis (strike voltage, latch, closer), one unit vs whole building, repair-or-replace, upfront diagnostic charge, older audio buzzers |
| 2026-11-24 | /intercom-installation-nyc (2026-05-03) | imperasecurity.com/building-intercom-installation-nyc (2026-11-16) | Newer; theirs ~2,300 words (scraped) | Multiple Dwelling Law §50-a section with the statute link, board/managing-agent workflow, riser retrofit vs rewire, phased upgrades, fail-safe vs fail-secure |
| 2026-11-24 | /security-camera-repair-brooklyn, -manhattan, -queens (2026-04-27) | imperasecurity.com/security-camera-repair-{brooklyn,manhattan,queens} (2026-11-14) | Newer (not scraped) | — |
| 2026-11-24 | /intercom-installation-long-island-ny, /security-camera-installation-long-island-ny, /access-control-installation-long-island, /access-control-installation-suffolk-county (2026-05-03) | vertexsecurity.com/security-systems-long-island/{intercom,security-camera-installation,access-control}/, /access-control-suffolk-county/ (2026-11-17 to 11-20) | Newer (not scraped) | — |
