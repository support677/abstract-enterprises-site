# site-rebuild-137 — Per-area tracking numbers + Low Voltage Installation NYC

**Baseline:** site-rebuild-135, extracted fresh. No GitHub, no Netlify, no deploy.
**Contains two pieces of work:** the sitewide phone routing correction, and the new Low Voltage Installation NYC hub page.

## Changed and new files: 971 (948 HTML, 20 images, plus sitemap, _redirects, mega-nav and this manifest)

---

# 1. Phone routing — every area now has its own CallRail tracking number

Previously every NYC borough page carried 347-934-8335 and every Hudson Valley page carried 845-640-3835, so six areas shared numbers belonging to two of them and calls could not be attributed by area.

| Area | Number | Pages | Changed |
|---|---|---|---|
| **Hub pages** (`-nyc`, `-long-island`, `-hudson-valley` slugs) | **(800) 486-0943** RingCentral | 115 | **yes** |
| Brooklyn | (347) 934-8335 | 653 | no |
| Bronx | **(646) 490-0629** | 611 | **yes** |
| Queens | **(347) 434-6392** | 45 | **yes** |
| Nassau | **(516) 346-5778** | 44 | **yes** |
| Suffolk | **(631) 407-2884** | 44 | **yes** |
| Manhattan | **(929) 560-0737** | 43 | **yes** |
| Westchester | **(914) 877-2578** | 43 | **yes** |
| Staten Island | (347) 934-8335 | 43 | no |
| Rockland / Orange / Putnam / Dutchess / Ulster | (845) 640-3835 | 207 | no |
| WhatsApp, all pages | (718) 679-0359 | — | no |

Hub pages span multiple areas, so no single area tracking number fits them; they carry the RingCentral line by owner instruction. Those calls will not attribute in CallRail.

Replaced on each page: `tel:` and `tel:+1` hrefs, both visible display formats, raw 10-digit strings, and JSON-LD `telephone` values. Malformed schema values of the form `+1-(xxx) xxx-xxxx` were normalised.

**Verified programmatically across all 16 areas plus hubs after the run — every `tel:` link matches its assigned number, zero strays.**

### Bug caught and fixed mid-run
The first pass matched by filename substring and gave **16 Bronx pages the Westchester number** — Westchester Square and Westchester Heights are Bronx neighbourhoods. The matcher was rewritten to give borough names precedence over county names and the run repeated from a clean baseline. Worth spot-checking those pages after deploy.

### Channel trackers deliberately kept off area pages
Putting these on area pages would corrupt attribution: **website (718) 306-6389** · **Google Business Brooklyn (718) 550-5992** · **Facebook (646) 846-2113** (routes calls to 347-349-2067) · four unlabelled 718 numbers · **Bronx Astor Pl (929) 205-6567**, since CCTV Bronx was selected for Bronx.

**No CallRail swap script exists anywhere on the site**, so these are static and hardcoding is correct. If dynamic number insertion is added later, DNI would overwrite these at runtime and this pass would need revisiting.

---

# 2. Low Voltage Installation NYC — new hub page

`low-voltage-installation-nyc.html` — all original NYC content. **Zero shared long paragraphs with any other page on the site**, checked pairwise against all 1,889 baseline pages including the existing 160-page structured-cabling silo.

**20 sections:** the neighborhood · what we install · building specialists · equipment · terminology · five separate borough blocks · industries · how it works · 14 Q&A sub-questions · AI Overview Reality Check (1,173 words, 7 H3 x 3 paragraphs) · pricing · shop our systems · local problems · field notes · coverage · 12 FAQ mirrored exactly in FAQPage schema · complete services · get in touch · warranty · all areas served. Two mid-page CTA strips, two repair-capture blocks, three Web3Forms including a 60-second qualifier.

**Boroughs kept strictly separate:** Manhattan office-to-residential conversions · Brooklyn Navy Yard and industrial campuses · Queens OneLIC rezoning and Hunters Point South · Bronx Hunts Point and the Industrial Business Zone · Staten Island commercial corridors.

**14 images** from the new "LOW VOLTAGE DIVISION" set. The previous set showed (800) 486-0943 on every garment and vehicle; the new set carries no phone number on any garment, cap, glove or vehicle. Native aspect ratios preserved, nothing cropped. Every alt and title unique, keyword-varied, carrying NYC or New York, and alt is never identical to title. All 14 in the ImageObject graph with explicit dimensions. Six assets held back for the borough children so the silo does not reuse one identical set across 16 pages.

**Phone:** (800) 486-0943, since this is a `-nyc` hub slug covering all five boroughs.

**Registration:** sitemap entry at 0.9/weekly with XML validated and the closing tag verified; `_redirects` 200 rewrite plus alias 301s from `/low-voltage-installer-nyc` and `/low-voltage-nyc`; `js/mega-nav.js` key added and validated with node --check. Inbound links added to the structured cabling NYC hub, its five borough siblings and the cabling pricing page.

**QA:** 20 sections · 7 JSON-LD blocks parse · 14 images with unique NYC-bearing alts and titles, all assets present · FAQ 12 == schema 12 exact · AI Overview 1,173 words / 7 H3 · div and section balanced · zero broken internal links · zero duplicate content sitewide. Rendered at 1440x900 and 390x844: zero blank images, zero overflow.

---

## Still open

1. **`(555) 123-4567` placeholders live on deployed pages** — Manhattan and Queens camera pages, a Brooklyn door buzzer page. Active lead leak, separate sweep.
2. **NYS Department of State Article 6-D** — confirm whether AESS camera, alarm, access control and intercom work falls inside the state security and fire alarm licensing scope before promoting a page that discusses licensing authoritatively.
3. **`300 Cadman Plaza West`** appears in schema on 166 Brooklyn pages, not in any routing rule on file.
4. 15 low-voltage silo child pages unbuilt.

**Nothing invented** — no fact, statistic, customer, testimonial, price or rule. Regulatory statements cite the NYC Administrative Code and the 2025 NYC Electrical Code, are marked general information rather than legal advice, and point the reader to the Department of Buildings.
