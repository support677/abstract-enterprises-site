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
- Page standard checked by the tool: **12,000–14,000 rendered words**, title ≤ 60, meta 150–160, one H1, canonical `https://www.abstractenterprisessecuritysystems.com/<slug>` (extensionless — live convention), **4.7 / 201**, NYS license #12000287431, the **exact warranty block** (text in `tools/check_page.py`, `WARRANTY`), two Web3Forms forms (hero + detail, access key, extensionless `landing_page`, consent checkbox, `botcheck` honeypot), approved phone only (queue line), GBP per queue line.
- Pricing per the §9 area multipliers — never invent prices.
- Written from scratch for this area. Masked-geo similarity to any sibling < 0.65. No FAQ/Q&A question may repeat any question in the silo's question register (add this page's questions to the register).

**Images — 11 per page.**
- `/images/<silo>/` has 11 or more photos for this silo → use 11 of them.
- Otherwise apply the image rule as practiced in manifests 186/187 (not written down elsewhere in the repo — see Open decisions): copy 11 photos from the closest silo into `/images/<silo>/` under new keyword + geo filenames (e.g. `fiber-optic-installation-bronx-riser-pull.webp`), WebP. Alt, title and caption are rewritten for this page and describe only what is visible. Never claim an image shows a customer, a named building or a completed local project. Each file is used once per page, alt and title unique. When dedicated photos for the silo arrive, they replace the reuses (as in manifest 186).
- Closest silo to borrow from: Fiber Optic Installation → `images/network/` or `images/low-voltage/` · Cat6 Repair → `images/network-cable-repair/` or `images/cat6/` · Smart Lock, Sonos, Soundbar → no close silo exists (see Open decisions).

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

## Open decisions (flagged, not guessed)

These rules differ between documents. The checker uses the value marked **(used)**. Change `tools/check_page.py` if you decide otherwise.

1. **Phone routing.** v2.3 §8 says SEO pages use (347) 934-8335 / (845) 640-3835 and never the 800. The live Cat6 and Network Cable Repair silos use per-area CallRail lines on children and (800) 486-0943 on hubs. **(used: the live per-area map.)**
2. **Warranty.** v2.3 and the Cat6 silo publish the three-year block. The Network Cable Repair silo publishes one-year parts-only (its deploy notes list this as undecided). **(used: three-year, Cat6 wording.)**
3. **Canonical / sitemap.** v2.3 §4 says `.html`. Every live page and the sitemap use the extensionless URL. **(used: extensionless.)**
4. **Word count and images.** You set 12–14k words and 11 images. The Cat6 hub is ~13k with 15 images; Cat6 and Network Cable Repair children are ~7–7.5k words with 11–16 images. **(used: 12–14k and exactly 11.)**
5. **Image rule.** The "permanent image rule" isn't written in the repo. The practice from manifests 186/187 is written above. Smart Lock, Sonos and Soundbar have no close image silo. Supply photos or name the silo to borrow from before those silos start.
6. **Rating.** v2.3 flags ⚠CONFIRM on 4.7/201 vs each GBP's own numbers. **(used: 4.7 / 201.)**
