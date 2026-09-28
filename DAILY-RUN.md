# DAILY-RUN — one new page per day

One run = one page. Read this file, then `BLUEPRINT.md` and `blueprint-v2_3-full.md` (v2.3 is the consolidated spec; where they differ, v2.3 wins), then the newest `MANIFEST-site-rebuild-*.md` for current build conventions. Nothing below overrides the blueprint; it only fixes the daily order of work.

**Working copy:** `C:\Users\opene\Documents\GitHub\abstract-enterprises-site` (outside OneDrive — OneDrive sync corrupts reads). Netlify deploys automatically from `main`, so a push is a deploy. Never drag a zip into Netlify.

**Tools:** Python 3.12 (`python tools/check_page.py …`). Git with a GitHub login that can push to `support677/abstract-enterprises-site`.

---

## The run

### 0. Start clean
1. `git pull --ff-only` on `main`. If it fails, stop and log it. Someone else (GitHub Desktop at `C:\dev\abstract-enterprises-site`) may have pushed.
2. `git status`. If there are uncommitted changes from a previous failed run for the same page, continue that page. If they're for anything else, stop and log it — never commit files you didn't make in this run.

### 1. Take the first TODO
Open `PAGE-QUEUE.md`, take the first line starting `TODO |` above the NEIGHBORHOODS heading. Its fields give the slug, silo, area, up-link, approved phone and GBP. If `<slug>.html` already exists, mark the line LIVE only if `tools/check_page.py <slug>` passes; otherwise log it and take the next TODO.

### 2. Research — once per silo, then local only
- `research/<silo>.md` doesn't exist → do the full silo research (blueprint v2.3 §3, all 11 sources) and save it there:
  - silo-wide findings: PAA, PASF, Answer the Public, AI Overview claims, Reddit, Yelp 1–3★, Bing/DDG, keywords (five layers: Service · Problem · Technology · Industry · Geographic);
  - a **question register**: every question used on any page of the silo, with the page it's on — this is what keeps FAQ/Q&A unique across the silo.
- It exists → reuse it. Add only a `## <area>` section with the local research for this geo: landmarks, streets and corridors, building stock, local news/hyperlocal, local Reddit, local licensing/permits.
- Every entry records **exact query · platform · URL · finding · page+section used** (v2.3 §12.4). A source that can't be reached is written `EMPTY (not accessible in build env)` — never invented. No stat, landmark, quote or story without a source.

### 3. Build the page to the blueprint
- Structure, section content, schema stack (6 blocks: LocalBusiness, Service, FAQPage, BreadcrumbList, ImageObject `@graph`, HowTo), forms, freshness stamp and advanced elements per v2.3 §4–§5 and the current silo pattern in the newest manifest.
- Page standard checked by the tool: **12,000–14,000 rendered words**, title ≤ 60, meta 150–160, one H1, canonical `https://www.abstractenterprisessecuritysystems.com/<slug>` (extensionless — live convention), **4.7 / 201**, NYS license #12000287431, two Web3Forms forms (hero + detail, access key, extensionless `landing_page`, consent checkbox, `botcheck` honeypot), approved phone only (queue line), GBP per queue line.
- Phone, warranty and rating copy the **Network Cable Repair** silo (the most recent live pages):
  - Phones: hubs carry only (800) 486-0943; area pages carry their direct line (queue line) in the body, CTAs and schema, with the 800 allowed in the shared header. WhatsApp only as `wa.me/17186790359` (the footer may show "WhatsApp (718) 679-0359" as text), never `tel:`.
  - Warranty: this exact sentence, and no three-year wording anywhere: *Full terms — including 50% deposit, one-year parts-only warranty on AESS-supplied products, and the late-fee schedule — are set out in the service agreement.*
  - Rating: 4.7★ / 201 Google Reviews (schema `ratingValue` 4.7, `reviewCount` 201).
- Pricing per the §9 area multipliers — never invent prices.
- Written from scratch for this area. Masked-geo similarity to any sibling < 0.65. No FAQ/Q&A question may repeat any question in the silo's question register (add this page's questions to the register).

**Images — 11 per page.**
- `/images/<silo>/` has 11 or more photos for this silo → use 11 of them.
- Otherwise apply the **permanent image rule** (as practiced in manifests 186/187): copy 11 photos from the closest silo into `/images/<silo>/` under new keyword + geo filenames (e.g. `fiber-optic-installation-bronx-riser-pull.webp`), WebP. Alt, title and caption are rewritten for this page and describe only what is visible — pick photos whose content genuinely fits the service. Never claim an image shows a customer, a named building, a completed local project, or equipment that isn't in the frame. Each file is used once per page, alt and title unique. When real photos for the silo are uploaded to `/images/<silo>/`, they replace the reuses (as in manifest 186).
- Closest silo to borrow from (by what the photos show):

  | New silo | Borrow from | Why |
  |---|---|---|
  | Fiber Optic Installation | `images/network/`, then `images/low-voltage/` | network rooms, racks, cable pulls |
  | Cat6 Repair | `images/network-cable-repair/`, then `images/cat6/` | cable fault, termination, testing |
  | Smart Lock Installation | `images/low-voltage/`, then `images/commercial-security/` | door-lock wiring, electric strikes, access readers |
  | Sonos Installation | `images/low-voltage/` | ceiling speakers, AV/low-voltage wiring |
  | Soundbar Installation | `images/low-voltage/` | speakers, AV/low-voltage wiring |

- **Every page that uses borrowed images gets a note in its `DAILY-LOG.md` line:** `images: 11 reused from images/<source>/ (no real <silo> photos yet)`.

### 4. Wire it in (every day)
- `sitemap.xml` — one `<url>` for `https://www.abstractenterprisessecuritysystems.com/<slug>` (extensionless, live convention), hub 0.9/weekly, child 0.7/monthly; check `</urlset>` tail after editing.
- `_redirects` — exactly two rules, each present once:
  `/<slug> /<slug>.html 200` (clean URL served) and `/<slug>.html /<slug> 301!` (live convention). Delete any stale rule that points the new slug elsewhere.
- Parent hub — the page links up to its hub (queue "up"); the hub links down to the page. Hubs link up to Home.
- Siblings — the page links to every LIVE page of its silo, and every LIVE sibling gets a link back (silo cross-link block). Any sibling anchor pointing at `/free-quote` as a "coming soon" stand-in for this page is flipped to `/<slug>`.
- **Do NOT touch `js/mega-nav.js`, the nav triggers or the cache version on weekdays.**

### 5. Sundays only — nav + cache (batch the week)
On Sunday runs, after the day's page passes:
1. `js/mega-nav.js` — add every page that went LIVE since the last Sunday under its silo key (new key for a new silo); `node --check js/mega-nav.js`.
2. Add the desktop + mobile nav triggers for any new silo site-wide (as in manifest 186).
3. Bump the site-wide cache version once (the `mega-nav.js?v=` string, currently `wifi17` on most pages) on every page — count-guarded replace: grep, assert the count, then replace.
4. Commit this separately: `Weekly nav: <silos/pages>`.
Never do this on any other day.

### 6. Check until PASS
`python tools/check_page.py <slug>` → fix every failure → re-run. Repeat until it prints `PASS`. The tool is mechanical: also confirm by reading that local facts are real and questions are genuinely different in meaning, not just wording (v2.3 §12.3).

### 7. Ship
1. In `PAGE-QUEUE.md` change only this line's `TODO` to `LIVE`.
2. Commit the page, its images, `sitemap.xml`, `_redirects`, the edited hub/sibling pages, `research/<silo>.md` and `PAGE-QUEUE.md`: `git commit -m "Daily page: <slug>"`.
3. `git push origin main`.

### 8. If it can't reach PASS
Don't commit to `main` and don't push. Leave the work uncommitted for the next run and write the reason (the failing check lines, and what blocks fixing them) to `DAILY-LOG.md`. Stop after three full fix rounds, or at once if a fix would need a rule decision (Open decisions below) or invented content.

### 9. Log every run
Append one line to `DAILY-LOG.md`, pass or fail:
`YYYY-MM-DD | <slug> | PASS pushed <short-sha> | <words> words | <notes>` or
`YYYY-MM-DD | <slug> | FAIL not pushed | <first failing check> | <reason>`.

---

## Decisions (Anwar, 2026-09-28)

1. **Phones, warranty, rating** — copy the most recent live pages (Network Cable Repair silo): per-area direct lines on area pages with the 800 in the header, 800-only on hubs; the one-year parts-only terms sentence; 4.7 / 201. This overrides v2.3 §8 and the Cat6 three-year block. Encoded in `tools/check_page.py`.
2. **Canonical / sitemap** — extensionless URL (every live page), not v2.3's `.html`.
3. **Word count and images** — 12–14k rendered words and exactly 11 images per page.
4. **Images for Smart Lock / Sonos / Soundbar** — reuse and rename 11 from the closest silo (table above) until real photos are uploaded; log it in `DAILY-LOG.md` every time.

## Kept private on Netlify

`_redirects` 404s these repo files so they are never served publicly: `PAGE-QUEUE.md`, `DAILY-RUN.md`, `DAILY-LOG.md`, `BLUEPRINT.md`, `blueprint-v2_3-full.md`, every `MANIFEST*` file, `/tools/*` and `/research/*`. The rules sit at the very top of `_redirects` (first match wins). **A new MANIFEST file needs its own 404 line** — Netlify can't wildcard part of a filename.
