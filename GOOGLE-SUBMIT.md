# GOOGLE-SUBMIT — URLs waiting for Google Search Console "Request indexing"

Daily page runs append one line per new page. The evening task on Anwar's desktop takes the oldest QUEUED lines (up to 10, Google's daily cap), requests indexing in Search Console, and changes QUEUED to REQUESTED <date> (or FAILED <reason>). Then it resubmits sitemap.xml in Search Console and Bing Webmaster Tools.

Format: `YYYY-MM-DD | <url> | QUEUED`

2026-10-14 | https://www.abstractenterprisessecuritysystems.com/fiber-optic-installation-nyc | QUEUED
2026-10-15 | https://www.abstractenterprisessecuritysystems.com/fiber-optic-installation-manhattan | QUEUED
2026-10-16 | https://www.abstractenterprisessecuritysystems.com/fiber-optic-installation-brooklyn | QUEUED
