# Off-site page mirror plan (Anwar, Nov 13 2026)
Rule: every page on abstractenterprisessecuritysystems.com gets its own page on EVERY platform below.
Each off-site page links to its EXACT matching site page (UTM: utm_source=<platform>&utm_medium=<format>&utm_campaign=parasite-seo).
Content is unique per page AND per platform: about the service in that exact area, a different angle every time
(angles used are tracked per service in seo/ANGLE-LOG.md), never copied from the site or another platform, never name-swapped.
Queue + order: seo/gamma-queue.csv (tier 1 hubs -> tier 2 boroughs/counties -> tier 3 neighborhoods). Each platform keeps its own log: seo/<PLATFORM>-LOG.md.

## Platform order (best for AESS first: Google ranking + link value + can be automated)
| # | Platform | Link value | How it's built | Status |
|---|---|---|---|---|
| 1 | Gamma (gamma.app) | TBD (check after indexing on) | Gamma API + Chrome to turn on indexing | LIVE - 101 pages (Nov 21); indexing OFF on all - Claude in Chrome not reachable from the scheduled runs (Nov 14, Nov 15, Nov 16, Nov 17, Nov 18, Nov 19, Nov 20, Nov 21) |
| 2 | Google Sites | followed | Chrome (one site, silo: hub > borough > neighborhood) | needs Chrome |
| 3 | Blogger (blogspot) | followed | Blogger API (needs Google connection) or Chrome | needs connection (no Composio connection Nov 16; Chrome not reachable from scheduled runs) |
| 4 | WordPress.com | followed | WordPress.com API (Composio needs auth config) | needs setup (no Composio connection Nov 16, Nov 17, Nov 18, Nov 19, Nov 20, Nov 21) |
| 5 | LinkedIn articles | nofollow, ranks strong | Chrome (existing weekday task) | LIVE |
| 6 | Medium | nofollow, ranks strong | Chrome (no account yet) | needs account (not connected Nov 16) |
| 7 | GitHub Pages / Netlify / Cloudflare Pages | followed | GitHub/Netlify/Cloudflare (connected) | guides site LIVE (148 guides after Nov 17 off-site run; see seo/GUIDES-LOG.md) - Nov 18 run could not push: guides repo not in this task's repo access; Nov 19, Nov 20, Nov 21 same |
| 8 | Tumblr | check | API (needs connection) | needs connection (not connected Nov 16) |
| 9 | Substack | nofollow | Chrome | needs account |
| 10 | HubSpot pages | followed | HubSpot (connected) | BLOCKED Nov 16, Nov 17 - connector missing blog scopes (cms.blogs.settings.read, cms.blogs.blog_posts.write, publish); reconnect HubSpot with blog permissions (still blocked Nov 18, Nov 19, Nov 20, Nov 21) |
| 11 | Google Docs published | redirect | Drive (connected) | LIVE - 36 docs (Nov 21), link-shared; "Publish to web" must be switched on by hand (not in connector) |
| 12 | Canva sites / Notion | check | Chrome publish | needs Chrome |
| 13 | Pinterest | nofollow | Pinterest API (connecting) | not connected - Composio shows no ACTIVE pinterest account (Nov 16, Nov 17, Nov 18, Nov 19, Nov 20, Nov 21) |
| 14 | Patch / Nextdoor | local | Chrome, per town (not per page) | needs accounts |
| 15 | Scribd / Issuu / SlideShare / Prezi | varies | PDF per hub/county | planned |
