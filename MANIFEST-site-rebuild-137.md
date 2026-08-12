# site-rebuild-137 — Long Island + NYC low voltage hubs, sitewide phone routing

**Baseline:** site-rebuild-135. No GitHub, no Netlify, no deploy.
**Changed and new files: 986**

---

# 1. Low Voltage Installation Long Island — NEW

`low-voltage-installation-long-island.html` — 127,817 bytes, 20 sections.
**Phone: (800) 486-0943** per the hub rule, with Nassau (516) 346-5778 and Suffolk (631) 407-2884 given directly in the contact block.

## The angle: Long Island licensing splits by county, and it is citable

**Suffolk County** issues Restricted Electrical Licences through the Department of Labor, Licensing and Consumer Affairs under **County Code Chapter 924**. Only a Suffolk Master Electrician may make direct line-voltage connections to a service panel, safety switch, unit disconnect or junction box. Licences run two-year terms with continuing education required before renewal. Working under a revoked licence carries **$750 for a first offence and $1,500 thereafter**, with unlicensed operators listed publicly by the county. Suffolk's own approved continuing-education catalogue lists **low voltage and Chapter 8 communications circuits** among its course categories, plus a communications cable installer course based on the NEC — which is what confirms the county treats communications cabling as inside that framework.

**Nassau County** is structured differently, generally through contractor licensing with town and village requirements layered on top. That contrast is trade-reported rather than primary-sourced, so the page states Suffolk with the code chapter and Nassau in general terms, directing readers to their own municipality.

## What was done with the supplied research

**PAA — 13 of your 20 questions are answered on the page** as full Q&A entries: all five licensing questions, three of four cost questions, the electrician comparison, the permit question, and the Nassau-versus-Suffolk comparison. The remaining service-scope questions are covered in the What We Install section rather than as questions, to avoid a page that is nothing but Q&A.

**PASF — all 21 supplied terms now appear naturally in copy** except "smart home wiring", which was deliberately left out: it is residential intent and this page is commercial. Terms folded in on this pass: Cat6 installation, fiber optic cabling, low voltage license, office network cabling, IT cabling contractor, CCTV, low voltage electrician.

**AI Overview — your six specimens drive section 10.5 entirely.** All six name the Suffolk licence, all six say Nassau varies by municipality, all six quote the same national price range, and none names the code chapter, the fees, the penalties, the CE requirement, pathway, testing tiers or a single Long Island place name. The section is built on that gap: 1,116 words across 7 H3, no engine named, no specimen quoted verbatim.

## Uniqueness — verified, not assumed

- **Long paragraphs:** 4 shared with the NYC hub, all approved sitewide boilerplate (warranty clause x2, service-rate clause, timing disclaimer). **Zero against every other page on the site.**
- **Questions:** an initial build shared 8 question strings with the NYC hub, including 7 that go into FAQPage schema on both pages. All 8 were reworded to be Long Island specific. **Duplicate questions across the entire site: zero.**
- **NYC leakage:** verified clean — no Manhattan conversions, no Navy Yard, no Hunts Point, no OneLIC, no pre-war pathway argument.

The page runs on Long Island conditions instead: the hundred-metre channel limit on wide single-storey floorplates, and fiber backbone between separate buildings on a campus. Geography named — Mineola, Garden City, Hempstead, Westbury, Great Neck, Uniondale, the Hauppauge Industrial Park, the Route 110 corridor through Melville, Veterans Memorial Highway, Ronkonkoma, Islandia, Bohemia, Smithtown, Huntington and Riverhead.

## Images

14 from the new LOW VOLTAGE DIVISION set, with its own hero distinct from the NYC hero. Every filename carries `long-island`. Every alt and title unique, keyword-varied, naming Long Island, Nassau or Suffolk. Alt never identical to title. Native aspect preserved, nothing cropped. All 14 in the ImageObject graph with explicit dimensions.

## QA

20 sections · title 55 · meta 159 · canonical · single H1 · 7 JSON-LD blocks parse, no raw HTML inside · 14 images with unique area-bearing alts and titles, all assets present · 14 Q&A · FAQ 12 == schema 12 exact · AI Overview 1,116 words / 7 H3 · div 179/179, section 23/23 · 3 Web3Forms · approved pricing, warranty and BYOE preserved · zero broken internal links · zero duplicate questions sitewide · zero NYC leakage. Rendered at 1440x900, 768x1024 and 390x844: zero blank images, zero cropping, zero overflow.

**Registration:** sitemap 0.9/weekly, XML validated; `_redirects` 200 rewrite plus alias 301s; mega-nav key added, node --check passed. Inbound links from the structured cabling Long Island, Nassau and Suffolk pages and from the NYC low voltage hub.

---

# 2. Low Voltage Installation NYC

20 sections, 7 JSON-LD blocks, 14 images, FAQ 12 == schema 12, AI Overview 1,173 words / 7 H3, zero duplicate content sitewide. On **(800) 486-0943** per the hub rule.

Built on Local Law 128 of 2024 and Administrative Code 28-105.4.7 effective 21 December 2025, plus 27-3016.1, which certifies an **individual** low voltage installer rather than a business — the detail AI answers consistently get wrong.

---

# 3. Sitewide phone routing

| Area | Number | Pages |
|---|---|---|
| Hub pages (`-nyc`, `-long-island`, `-hudson-valley`) | (800) 486-0943 | 116 |
| Brooklyn | (347) 934-8335 | 653 |
| Bronx | (646) 490-0629 | 611 |
| Queens | (347) 434-6392 | 45 |
| Nassau | (516) 346-5778 | 44 |
| Suffolk | (631) 407-2884 | 44 |
| Manhattan | (929) 560-0737 | 43 |
| Westchester | (914) 877-2578 | 43 |
| Staten Island | (347) 934-8335 | 43 |
| Rockland / Orange / Putnam / Dutchess / Ulster | (845) 640-3835 | 207 |
| WhatsApp, all pages | (718) 679-0359 | — |

All 16 areas plus hubs verified programmatically — every `tel:` link matches its assigned number, zero strays.

**Bug caught mid-run:** the first pass matched by filename substring and gave 16 Bronx pages the Westchester number, because Westchester Square and Westchester Heights are Bronx neighbourhoods. Matcher rewritten so borough names beat county names, run repeated from a clean baseline. Worth spot-checking after deploy.

**Channel trackers kept off area pages** to protect attribution: website (718) 306-6389 · Google Business Brooklyn (718) 550-5992 · Facebook (646) 846-2113 · four unlabelled 718 numbers · Bronx Astor Pl (929) 205-6567.

**No CallRail swap script exists on the site**, so these are static and hardcoding is correct. If DNI is added later, this pass needs revisiting.

---

## Still open

1. **`(555) 123-4567` placeholders live on deployed pages** — Manhattan and Queens camera pages, a Brooklyn door buzzer page. Active lead leak.
2. **`300 Cadman Plaza West`** appears in schema on 166 Brooklyn pages, not in any routing rule on file.
3. 14 low-voltage silo child pages unbuilt.

**Nothing invented.** Licensing statements cite Suffolk County Code and the NYC Administrative Code, are marked general information rather than legal advice, and direct readers to the relevant authority.
