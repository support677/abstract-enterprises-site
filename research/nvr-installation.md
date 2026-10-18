# NVR Installation — silo research

Created 2026-10-18 by the REBUILD of `nvr-installation-bronx` (area page, up-link `/nvr-installation-nyc`, direct line (646) 490-0629, Bronx GBP 460 E Fordham Rd / `#bronx`). Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Shell curl/wget are blocked in the build environment; tools used: Firecrawl search (`mcp__Firecrawl__firecrawl_search`, excerpts) and Firecrawl scrape (`mcp__Firecrawl__firecrawl_scrape`, query/directQuote). Items "carried" come from other research files in this repo where they were fetched with a URL; the original row is named. Nothing below is invented; where only a search excerpt was seen, the entry says "excerpt". Sources that could not be opened are written `EMPTY (not accessible in build env)`.

Silo: `nvr-installation-*` (16 pages: NYC hub + Manhattan/Brooklyn/Queens/Bronx/Staten Island; Long Island hub + Nassau/Suffolk; Hudson Valley hub + Westchester/Rockland/Orange/Putnam/Dutchess/Ulster). Before this batch all 16 were the same template (same 12 FAQ intents, same prices, ±2 KB sizes). A parallel builder is rebuilding `nvr-installation-hudson-valley` in this batch and writes to `research/nvr-installation--hudson-valley.part.md` (not touched here).

Later area builds: reuse §1–§3, add only a `## <area>` section, and append your questions to the register (§4).

---

## 1. Source matrix (blueprint v2.3 §3, all 11 sources)

| # | Source | Status for this silo build |
|---|---|---|
| 1 | Reddit | Excerpts only via Firecrawl search (reddit.com not scraped in full). Rows R1–R7. |
| 2 | Google People Also Ask | **EMPTY (not accessible in build env)** — no live Google SERP surface. |
| 3 | Google PASF | **EMPTY (not accessible in build env)**. |
| 4 | Answer the Public | **EMPTY (not accessible in build env)**. |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)**. The Bronx page §10.5 says so on the page and tests seven claims commonly repeated in cost guides, blogs and forum answers (rows A1–A3, R2–R3) against primary sources; it does not quote an AI Overview. |
| 6 | Area landmarks | Bronx section (sourced). |
| 7 | Area use cases / building stock | Bronx section (Furman Center, UNHP, LPC, Co-op City). |
| 8 | Bing / DuckDuckGo | **EMPTY (not accessible in build env)** — one search backend per tool; no Bing/DDG related-search surface. |
| 9 | Local news | amNewYork, ABC7, News 12 Bronx, Fox 5, CBS NY, NBC NY, NY Daily News (2026). |
| 10 | Hyperlocal | Bronx Times (Oct 2026 Third Avenue BID cameras; Jan 2019 DA CAMS program). BronxNet: **EMPTY** (no camera/recorder item surfaced). Norwood News / Riverdale Press recorder items: **EMPTY**. |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** — the Yelp search page surfaced only as a listing excerpt (https://m.yelp.com/search?find_desc=Security+Camera+Installation&find_loc=Bronx%2C+NY), no review text. |

---

## 2. Silo-wide findings (NVR)

### 2.1 Reddit / forums (excerpts)
| ID | Exact query · platform | URL | Finding | Used on Bronx page |
|---|---|---|---|---|
| R1 | `reddit NVR in closet overheating hard drive failure surveillance recorder ventilation` · Firecrawl search (excerpt) | https://www.reddit.com/r/reolinkcam/comments/1jsjqwm/2_failed_rln8410/ | "NVRs need to breath, HDD run hot. If they are in an enclosed closet or cabinet without ventilation or in a hot attic, overheating can shorten …" | §9 H3 boiler room (paraphrased "owners on forums describe…"); Sources |
| R2 | same (excerpt) | https://www.reddit.com/r/SecurityCamera/comments/1g2eiej/repair_or_replace/ | "make sure to get a Surveillance Grade HDD like Western Digital Purple or Seagate Skyhawk, regular HDDs will fail within just a few months." (forum claim) | §10.5 H3 2 (framed as forum experience, not as fact); Sources |
| R3 | same (excerpt) | https://www.reddit.com/r/reolinkcam/comments/1j40zlp/nvr_in_the_attic/ | "Some hide the NVR in a cabinet or closet but NVRs need ventilation due to HDD heat. If in cabinet make holes for the NVR fan…" | background §9 heat H3 |
| R4 | same (excerpt) | https://www.reddit.com/r/homelab/comments/16hdy8p/putting_a_hard_drive_in_a_safe_cooling_issues/ | owner after a break-in: thieves "took a few but didn't get the DVR" — hiding recorder vs cooling | background §9 bodega H3 (not quoted) |
| R5 | `site:reddit.com r/bronx security cameras building landlord footage` · Firecrawl search (excerpts) | https://www.reddit.com/r/AskNYC/comments/1959k2t/ring_camera_in_apartment_building_opinions/ | commenter: "For NYC common area video, only thing not allowed is if camera can film into someone's apartment." (opinion, not law) | background §9 accounts H3 ("we keep cameras away from views into apartments") — not quoted |
| R6 | `site:reddit.com/r/bronx packages stolen lobby camera building` · Firecrawl search (excerpt) | https://www.reddit.com/r/bronx/comments/1pfhikq/i_hate_porch_pirates/ | r/bronx resident: "a camera shows a group of teens enter the building and steal the package" | Sources list only |
| R7 | same search (excerpt) | https://www.reddit.com/r/bronx/comments/1jetrgt/my_coworkers_car_at_havermeyer_st_parked_the_car/ | r/bronx (Havermeyer St car theft): commenter suggests paying a homeowner across the street to see their camera footage | Not used (illustrates neighbour footage requests) |
| R8 | `reddit … NVR $320 for a 4 channel` (from cost search below, excerpt) | https://www.reddit.com/r/homesecurity/comments/1ewdiuu/is_this_a_good_quote_for_a_wired_camera_system/ | quote: "price to hardwire each camera: $150 … NVR: $320 for a 4 channel to $500 for an 8 channel" | Not used (single quote) |

### 2.2 Cost guides (for §10.5 Reality Check)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | `NVR installation cost Angi OR HomeAdvisOR OR Fixr network video recorder setup price` · Firecrawl search (excerpt) | https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera.htm | Angi 2026: professional security camera installation $590–$2,040 per home project. | §10.5 H3 1; Sources |
| A2 | same (excerpt) | https://wasserstein-home.com/blogs/smart-home/security-camera-installation-cost-all-you-need-to-know-in-2025 | blog (2026 title): "$100–$500 for DVR/NVR", cloud $3–$30/month per camera. | §10.5 H3 1 ("one 2026 cost guide") |
| A3 | same (excerpt) | https://www.facebook.com/groups/lowvoltagenation/posts/3973859569570509/ | installer group: hourly ~$150–$175, "1 hour per camera + 4 hours programming" | Not used (forum) |

### 2.3 Equipment / technical
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| T1 | `WD Purple surveillance hard drive workload rate 180 TB/year 24/7 cameras specification` · Firecrawl search (excerpt) | https://documents.westerndigital.com/content/dam/doc-library/en_us/assets/public/western-digital/product/internal-drives/wd-purple-hdd/data-sheet-wd-purple-hdd.pdf ; https://www.westerndigital.com/products/internal-drives/wd-purple-sata-hdd?sku=WD11PURZ | "WD Purple drives feature a workload rating of up to 180TB/year - up to three times that of desktop drives - to handle the unique demands of mainstream video surveillance DVR and NVR systems." | §9 heat H3; §10 drives card; §10.5 H3 2; Sources |
| T2 | (carried general fact, no URL — same as floodlight/lorex research FLAG) | — | Copper Ethernet channel limit ≈100 m (328 ft). | §9 tower/garage H3 — FLAG general technical fact |
| T3 | (no source fetched) | — | ONVIF interoperability between IP cameras and other-brand NVRs. | §9 H3 13 — FLAG general technical fact |
| T4 | `NYCHA Bronx developments CCTV cameras installed layered access program 2025 2026` · Firecrawl search (excerpt) | https://nychajournal.nyc/nycha-completes-over-24-million-in-safety-and-security-upgrades-at-23-campuses/ | NYCHA (Nov 2023): new CCTV "operated by the same video management systems as NYPD cameras to allow for variable speed recording and 21-day footage retention"; OFSS gives NYPD access to footage. | §7 NYCHA paragraph; §10.5 H3 4; Sources |
| T5 | same (excerpt) | https://citymeetings.nyc/meetings/new-york-city-council/2025-04-15-1000-am-committee-on-public-housing/chapter/number-and-distribution-of-functioning-cctv-cameras-at-nycha-developments/ | Apr 15, 2025 Council Committee on Public Housing: "Over 20,000 cameras are installed across 214 developments and 1,519 buildings". | §7 NYCHA paragraph; Sources |
| T6 | carried from research/apartment-building-security-camera-installation.md (line 31) | https://www.fsresidential.com/new-york/news-events/articles-and-news/security-cameras-best-practices-nyc-condos-co-ops | FirstService Residential: footage typically kept 30 to 90 days; access limited, with a log of requests/viewers. | §9 accounts H3; §10.5 H3 4; Sources |
| T7 | carried from research/apartment-building-security-camera-installation.md (lines 75, 101) | https://www.brickunderground.com/rent/realty-bites-package-thief-landlord-security-camera | Attorney: landlord "isn't obligated to share surveillance footage" outside police request/court order; buildings not required to have working cameras. | §9 accounts H3 ("real-estate press … reported"); Sources |

### 2.4 Footage, police and prosecutors
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| P1 | `NYPD request surveillance video businesses canvass footage overwritten days retention store owners New York` · Firecrawl search (excerpt) | https://www.hornwright.com/bronx/civil-rights/false-imprisonment/how-to-preserve-body-cam-dash-cam-and-store-surv/ | Bronx law-firm guide: "Store cameras: many overwrite in 7 to 10 days." | §9 detective H3; §10.5 H3 4; Sources |
| P2 | same → Firecrawl scrape (query/directQuote) | https://abc7ny.com/post/nyc-retail-theft-program-mayor-eric-adams-nypd-launch-innovative-technology-initiative-to-combat/14827113/ | May 16, 2024: pilot on 125th Street; businesses connect "a box that looks like a router -- made by the company Fusus by Axon -- that gives detectives at the local precinct real-time access to cameras"; "still at the behest or the control of the business owner". | §9 live-share H3; §10.5 H3 7; Sources |
| P3 | `Bronx Times security cameras small businesses Fordham Road OR "Southern Boulevard" OR "Grand Concourse" 2025 2026` · Firecrawl search → scrape (directQuote) | https://www.bxtimes.com/exclusive-look-at-das-new-surveilence-camera-program/ | Bronx Times, Jan 20, 2019: DA's office with the Bronx Chamber of Commerce and BIDs unveiled the **Bronx Community Assisted Mapping System (CAMS)** at the end of 2018; "an intranet of security camera locations provided by members of each of the borough's BIDs"; previously NYPD collected footage from corridor businesses and delivered it "by hand"; "nearly 1,000 surveillance cameras enrolled". | §9 CAMS H3; §10.5 H3 7; Sources |

### 2.5 Rules (silo-wide; NY / NYC / federal)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | carried from research/hikvision-security-camera-installation.md F1 | https://docs.fcc.gov/public/attachments/DA-26-635A1.pdf | DA 26-635 (June 26, 2026, PS Docket 26-72): prohibits continued importation and marketing of certain previously authorized covered equipment added to the Covered List in 2024 or earlier; "will not affect the continued use or operation of already-purchased communications equipment"; use-based entries prohibited only for covered uses (public safety, government facilities, suspended critical infrastructure, other national security purposes). | §8.5 bullet 4; §9 H3 12–13; §10.5 H3 3; Sources |
| G2 | carried F2 | https://www.federalregister.gov/documents/2026/07/06/2026-13518/prohibiting-importation-and-marketing-of-previously-authorized-covered-communications-equipment | Federal Register July 6, 2026: takes effect **July 16, 2026**; non-covered uses not affected; consumers may continue to use equipment they possess. | §8.5; §9 H3 12; Sources |
| G3 | carried F3 | https://www.hikvision.com/us-en/newsroom/latest-news/2026/Important-Notice-to-Our-Partners | Hikvision USA (Apr 7, 2026): import limits "could affect access to replacement parts, warranty service, and technical support". | §9 H3 12; §10.5 H3 3; Sources |
| G4 | carried F4 | https://www.hikvision.com/us-en/newsroom/latest-news/2026/understanding-the-fcc-s-regulatory-updates/ | Hikvision USA (Sept 10, 2026): "not a blanket ban"; no requirement to remove installed products. | §9 H3 12; Sources |
| G5 | carried F7 | https://www.globalsecurity.org/intell/library/news/2022/intell-221125-fcc01.htm | FCC Nov 25, 2022: Hikvision/Dahua barred from new authorizations. | §9 H3 13 |
| G6 | `NYC biometric identifier information law commercial establishments sign facial recognition Administrative Code 22-1202` · Firecrawl search (excerpt) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-131285 | §22-1202: commercial establishment collecting/retaining/converting/storing/sharing customers' biometric identifier information must post "a clear and conspicuous sign near all of the commercial establishment's customer entrances" in form prescribed by DCWP; (b) bars selling/profiting. | §8.5 bullet 2; §9 H3 14; Sources |
| G7 | same (excerpt) | https://legistar.council.nyc.gov/LegislationDetail.aspx?ID=3704369&GUID=070402C0-43F0-47AE-AA6E-DEF06CDF702A | Int 1170-2018 summary: private right of action — $500 for failing to post signage or negligent sale/sharing, $5,000 intentional/reckless sale. | §9 H3 14; Sources |
| G8 | carried from research/apartment-building-security-camera-installation.md item 13 | https://www.nysenate.gov/legislation/laws/PEN/250.00 (and 250.05) | Mechanical overhearing = recording a conversation without consent of at least one party; eavesdropping is a class E felony. | §8.5 bullet 3; §9 H3 15; Sources |
| G9 | carried (apartment-building research lines 27, 102) | https://dos.ny.gov/get-security-or-fire-alarm-installer-license ; https://dos.ny.gov/system/files/documents/2024/05/security_0.pdf | NYS DOS security/fire alarm installer licence (Article 6-D): 81 hours education, exam, fingerprints; 19 NYCRR §195.2(b)(1) covers CCTV / video surveillance systems. | §8.5 bullet 1; Sources |
| G10 | carried (floodlight G8 / dvr-upgrade G4) | https://nyc-business.nyc.gov/nycbusiness/description/nyscommercialsecuritytaxcredit | NYS Commercial Security Tax Credit: ≤50 employees, up to $3,000 per retail location, cameras eligible. | §8.5 bullet 5; Sources |
| G11 | carried (cat6-repair Bronx) | https://www.nyc.gov/site/lpc/applications/applications.page | LPC permits required for work affecting the exterior of landmarked buildings. | §8.5 bullet 6; Sources |
| G12 | `NYC Department of Consumer and Worker Protection home improvement contractor license security system installation required` · Firecrawl search (excerpts) | https://www.nyc.gov/site/dca/businesses/license-checklist-home-improvement-contractor.page ; https://adaptdigitalsolutions.com/articles/new-york-contractor-license-requirements/ | DCWP issues Home Improvement Contractor licences; third-party summary: required for residential home-improvement work over $200. Whether low-voltage camera/NVR work counts was **not established**. | Not used on page — FLAG |

### 2.6 Keywords (five layers, silo)
- **Service:** NVR installation, network video recorder installation, NVR setup, NVR replacement, recorder relocation, NVR configuration, PoE NVR, 8/16/32-channel NVR.
- **Problem:** NVR overheating, NVR not recording / "No HDD", hard drive failure, power outage reset, wrong date/time stamp, lost admin password, footage overwritten, police footage request, recorder stolen, port-forwarded recorder.
- **Technology:** PoE switch, surveillance hard drive (WD Purple), RAID / mirrored drives, UPS (online / line-interactive), H.265, bitrate, retention, ONVIF, time sync (NTP), user roles, export, face detection/biometrics, audio.
- **Industry:** apartment buildings (walk-up, elevator, co-op, condo), managing agents, supers, bodegas/delis, storefronts, BIDs, wholesale markets/warehouses, offices, clinics.
- **Geographic:** per area section.

### 2.7 Silo pricing base (no invented prices) — FLAG
| Figure | Source in repo |
|---|---|
| Set up NVR + cameras you own **$220–$480**; new 8-channel system (recorder + PoE + drive) **$650–$1,500** (cameras/cabling separate); 16–32 ch / RAID **$1,600–$5,500+**; upgrade/migration/repair **$190–$900** | Published identically on all 16 pre-rebuild `nvr-installation-*` pages, incl. `nvr-installation-brooklyn.html` (Brooklyn = §9 base 1.00×) and the hub `nvr-installation-nyc.html`. |
| Camera line **$175** (Cat6 ≤100 ft exposed, mount, terminate, connect); concealed hollow drywall **$200/line**; raceway **$100/line**; conduit **$200/line**; J-box **$25**; old equipment removal **$50**; COI **$0**; NVR/DVR setup only **$150** (Brooklyn base) | `install-your-own-camera-system.html` SVCS + AREAS.brooklyn (line 175, conceal 200) |
| Service **$195/hr, 3-hr min ($585)** | blueprint v2.3 §9 (protected) |
FLAGS: (1) the BYOE calculator gives the Bronx a **+15%** markup (line $201, conceal $230, hourly $225), which conflicts with blueprint §9 (Bronx 1.00×); the Bronx page follows §9 and publishes the Brooklyn base. (2) The calculator's "NVR/DVR Setup Only" **$150** vs the silo's "setup & config of your hardware" **$220–$480** — published as "recorder setup only, labor, from $150" and "set up a recorder and cameras you already own $220–$480" (different scopes); Anwar to confirm. (3) The silo ranges were carried from the old template pages; they were never re-derived and other area rebuilds should apply §9 to them.

---

## 3. Images (silo)
Step A — Google Drive "AESS Website Photos" (id 1hAcALEIANNRWVFVsbt4qqVder5_E4Bac) has no NVR Installation folder (only Cat6 Repair, Sonos, Fiber Optic, Soundbar, Smart Lock) — per main-run brief. Step B — CompanyCam not connected. → permanent image rule; `images/nvr-installation/` created by this build. See Bronx section for the 11 files.

---

## 4. Question register (every FAQ / Q&A question on all 16 nvr-installation-* pages)

### 4.1 Old-template pages (15 siblings, read 2026-10-18 before any rebuild in this batch landed)

Every one of the 15 sibling pages (and the pre-rebuild Bronx page) carries the same 11 questions in its FAQ schema / FAQ, plus one area-specific cost question:

- Can I add more cameras to my existing NVR later? — all 16 nvr-installation-* pages (pre-rebuild)
- Can I view my NVR cameras remotely from my phone? — all 16 (pre-rebuild)
- Can you upgrade or migrate my old recorder? — all 16 (pre-rebuild)
- Do NVRs have monthly fees? — all 16 (pre-rebuild)
- Do you install NVRs for businesses and warehouses, not just homes? — all 16 (pre-rebuild)
- How many channels do I need? — all 16 (pre-rebuild)
- How much hard drive storage do I need? — all 16 (pre-rebuild)
- What is RAID and do I need it? — all 16 (pre-rebuild)
- What is an NVR and how is it different from a DVR? — all 16 (pre-rebuild)
- Why did my NVR stop recording? — all 16 (pre-rebuild)
- Will cameras from one brand work with another brand's NVR? — all 16 (pre-rebuild)

Area-specific cost question (same intent on every page):
- How much does NVR installation cost in Brooklyn? — nvr-installation-brooklyn
- How much does NVR installation cost in Dutchess County? — nvr-installation-dutchess-county
- How much does NVR installation cost in the Hudson Valley? — nvr-installation-hudson-valley (pre-rebuild)
- How much does NVR installation cost on Long Island? — nvr-installation-long-island
- How much does NVR installation cost in Manhattan? — nvr-installation-manhattan
- How much does NVR installation cost in Nassau County? — nvr-installation-nassau-county
- How much does NVR installation cost in NYC? — nvr-installation-nyc
- How much does NVR installation cost in Orange County? — nvr-installation-orange-county
- How much does NVR installation cost in Putnam County? — nvr-installation-putnam-county
- How much does NVR installation cost in Queens? — nvr-installation-queens
- How much does NVR installation cost in Rockland County? — nvr-installation-rockland-county
- How much does NVR installation cost on Staten Island? — nvr-installation-staten-island
- How much does NVR installation cost in Suffolk County? — nvr-installation-suffolk-county
- How much does NVR installation cost in Ulster County? — nvr-installation-ulster-county
- How much does NVR installation cost in Westchester County? — nvr-installation-westchester-county
- How much does NVR installation cost in the Bronx? — nvr-installation-bronx (pre-rebuild; removed in rebuild)

The rebuilt Bronx page deliberately does NOT ask any of these intents as a question (cost, channels, storage sizing, RAID, NVR vs DVR, monthly fees, remote viewing, stopped recording, adding cameras, cross-brand compatibility, upgrade/migration, business vs home). Cost lives in §14/§15 tables only; drives in §10 card/§10.5.

### 4.2 nvr-installation-bronx (rebuilt 2026-10-18)
§9 "Questions Answered" (H3), by cluster:
- Where the Recorder Lives in a Bronx Building
  1. The only room in our walk-up that locks is the boiler room — can the recorder live in there?
  2. Should a six-storey building's recorder go in the cellar with the super, or up in the lobby where the cameras are?
  3. Our bodega has no back office — where can the recorder go so nobody walks out with the evidence?
  4. The building's internet comes in on the top floor but the recorder belongs in the cellar — how do the two meet?
- Power, Heat and Outages
  5. Con Edison cut the voltage in our part of the Bronx during the July heat — can a brownout hurt the recorder even when the lights stay on?
  6. Our recorder sits in a closet with no window, and it gets hot up there every August — what does that do?
- Who Holds the Keys
  7. Our building is changing managing agents — who should own the recorder's admin password?
  8. The owner, the super and the tenant association all want to see the cameras — can one recorder handle that?
- When Detectives, the DA or an Insurer Ask for Video
  9. A detective asked for footage from last Tuesday night — how do we get it off without giving up the recorder?
  10. What is the Bronx DA's camera-mapping program, and should our store's cameras be on it?
  11. Can our store share a live camera view with the precinct without handing over the password?
- The 2026 Rules on Hikvision and Dahua Recorders
  12. Our store's recorder is a Hikvision — after the FCC's July 2026 order, do we have to take it out?
  13. If the covered-brand recorder dies next year, can we still get the same model?
- Faces, Voices and Signs
  14. Our new recorder offers face recognition — does a Bronx store have to post a sign if we turn it on?
  15. Should the recorder save sound from the camera over the register?
- Docks, Big Buildings and Spread-Out Sites
  16. Our Hunts Point dock runs all night — should those cameras record continuously or only on motion?
  17. Can one recorder cover a tower lobby and a parking garage a block apart in our complex?

§17 FAQ (visible == FAQPage, 10):
  1. How long does a recorder install take in an occupied Bronx apartment building, and will the intercom or internet go down?
  2. Do you provide a certificate of insurance before work starts in our building?
  3. Can you install after the store closes or before the market opens?
  4. What do you leave behind when the job is finished?
  5. Can the recorder warn us when a camera goes dark or a drive fails?
  6. How do you keep the recorder's clock right so time stamps hold up?
  7. Will you take away the old recorder, mounts and dead cameras?
  8. Is there a charge to come and look at the building first?
  9. How is payment handled for a Bronx recorder job?
  10. Can the monitor at the register show the cameras without giving the cashier access to the recordings?

De-dup vs the Hudson Valley rebuild (nvr-installation-hudson-valley.html rewritten 08:42Z, 25 question headings read at ~08:45Z): the Bronx outage question was rewritten from "how long will the recorder keep going in an outage" to the brownout/voltage-reduction intent, and the clean-shutdown-on-low-battery content was dropped, because HV owns "What has to share the recorder's battery backup?" and "What should the recorder do when its battery is about to run out?". Other HV intents checked and not repeated here: unheated barn/garage, generator vs UPS, barn 500 ft link, rented cottage, gate camera power, Starlink/port forwarding, upload bandwidth, internet down for days, electrical permit, fire district/library/town hall buying covered brands, "critical infrastructure" neighbours, off-site clip backup, caretaker checks, moving a recorder without rewiring, selling the house, built-in PoE vs switch, separate network, install before closing/renovation, monitor vs TV, end of firmware updates, remote settings changes, power-off test at handover. Masked paragraph similarity Bronx vs HV max 0.625 (freshness-stamp boilerplate); vs the 14 old-template siblings 0.388.

Intents this page owns for the silo (later pages should not repeat): recorder room selection (boiler room, cellar vs lobby, back-of-store/lockbox), internet entry on another floor, UPS/outages, closet heat, admin password custody on agent change, role-based accounts for owner/super/tenant association, footage export for detectives, Bronx DA CAMS, NYPD live-sharing, keep/replace covered-brand recorder and replacement availability, biometric sign law, audio recording, continuous vs motion at a dock, linking buildings/garage; FAQ: install duration in occupied building, COI, after-hours work, handover pack, fault alerts, time sync, old equipment removal, estimate visit, payment, register monitor without playback rights.

---

## Bronx

Build 2026-10-18 (nvr-installation-bronx). Phone (646) 490-0629 · GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`, LocalBusiness block modelled on cat6-repair-bronx.html) · up-link `/nvr-installation-nyc`.

**Thesis (local):** In the Bronx an NVR is a shared evidence locker in a building someone else controls. Housing is mostly rented (19.7% homeownership) and old (median multifamily building 87 years), so the recorder lands in a super's cellar office beside the boiler, a walk-up closet, behind a bodega counter or in a market unit — rooms that kill drives through heat, water, power cuts and theft. Footage is regularly requested (detectives, the DA's CAMS map, housing court, insurers, new managing agents). So the job is custody first — room, power (July 2026 Con Ed outages), keys/accounts, retention, export — and the box second; plus the 2026 FCC covered-equipment rule for the Hikvision/Dahua recorders common in Bronx stores.

### Building stock / use cases
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX1 | carried from research/cat6-repair.md (Bronx, scrape directQuote, page updated 05/06/2026) | https://www.furmancenter.org/neighborhoods/the-bronx/ | "In 2024, the homeownership rate in The Bronx was 19.7%, which is lower than the citywide share of 32.7%."; "Between 2010 and 2025, 63,066 units in 4+ unit buildings were built in The Bronx." | §5.5 bullets 1, 4; Sources |
| BX2 | `Bronx housing stock built before 1940 share of units pre-war apartment buildings census` · Firecrawl search (excerpt) | https://unhp.org/blog/how-will-bronx-buildings-survive-as-they-age/ | "Here in the Bronx, the median age of multifamily apartment buildings is 87 years. In Community Board 6 it's 98 years old." | §5.5 bullet 2; Sources |
| BX3 | same search (excerpt) | https://chpcny.org/visualization/housing-stock-visualization/ | Citywide: over half of units (~2 million) built before 1947. | Not used (citywide) |
| BX4 | carried (cat6-repair Bronx) | https://s-media.nyc.gov/agencies/lpc/lp/2403.pdf | Grand Concourse HD: 78 properties along one mile between E 153rd and 167th Sts; 61 apartment houses 1917–1959; five- and six-storey apartment house "the dominant building type along the Grand Concourse and within the Bronx". | §5.5 bullet 3; §13 card 3; Sources |
| BX5 | carried (cat6-repair Bronx, excerpt) | https://www.coopcity.com/aboutus/ | Co-op City: 15,372 residential units in 35 high-rise buildings and seven townhouse clusters. | §9 H3 17; §13 card 6; Sources |
| BX6 | T4/T5 above | NYCHA Journal; citymeetings.nyc | NYCHA camera count and 21-day retention. | §7 NYCHA paragraph |

### Corridors / landmarks
| ID | Source | URL | Finding | Used |
|---|---|---|---|---|
| BX7 | carried (cat6-repair Bronx, excerpt) | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page?bid=49 | Fordham Road BID: 35 block faces, 333 ground-floor retail businesses. | §5.5 bullet 5; §8 card 1; §13 card 1 |
| BX8 | carried (fiber-optic research) | https://www.nyc.gov/site/sbs/neighborhoods/bid-directory.page | 12 Bronx BIDs incl. 161st Street, Belmont, Castle Hill, Fordham Road, HUB Third Avenue, Jerome-Gun Hill, Kingsbridge, Morris Park, Southern Boulevard, Throggs Neck, Westchester Square, White Plains Road. | §8 cards 3, 6 |
| BX9 | `Bronx Times security cameras small businesses Fordham Road OR "Southern Boulevard" OR "Grand Concourse" 2025 2026` · Firecrawl search (excerpt incl. article body) | https://www.bxtimes.com/third-avenue-bid-adds-security-measures/ | Bronx Times, Oct 2, 2026 (Marina Samuel): Third Avenue BID announced Oct 1 near Roberto Clemente Plaza: 18 security cameras across 10 locations (state Downtown Revitalization Initiative funding) and 75 solar-powered lighting fixtures across 30 storefronts ($100,000 SBS public-realm grant). | §5.5 bullet 5; §8 card 2; §13 card 2; Sources |
| BX10 | carried (cat6-repair Bronx, excerpt) | https://en.wikipedia.org/wiki/The_Hub,_Bronx | The Hub: 2/5 at Third Avenue–149th Street. | §13 card 2; Sources |
| BX11 | carried (cat6-repair Bronx, excerpt) | https://en.wikipedia.org/wiki/Bronx_Terminal_Market | 913,000 sq ft GLA; 17-acre site south of Yankee Stadium. | §8 card 5; Sources |
| BX12 | carried (cat6-repair / fiber Hunts Point) | https://www.nycfoodpolicy.org/hunts-point-distribution-center-brief-overview-spotlight-produce-market/ | Hunts Point FDC: 329 acres, 155+ wholesalers. | §8 card 4; §13 card 4; §9 H3 16; Sources |
| BX13 | carried (cat6-repair Bronx, excerpt) | https://www.fordham.edu/about/campuses/rose-hill-campus/ | Rose Hill campus 85 acres. | §13 card 5; Sources |
| BX14 | carried (cat6-repair Bronx, excerpt) | https://en.wikipedia.org/wiki/Bay_Plaza_Shopping_Center | Bay Plaza by Hutchinson River Pkwy / I-95, beside Co-op City. | §13 card 6 (name only) |

### Local news / hyperlocal
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| BX15 | `Bronx bodega robbery surveillance video NYPD 2026` · Firecrawl search (news, excerpts) → scrape amNY (directQuote) | https://www.amny.com/news/bronx-bodega-shot-robbery-brooklyn-shooting/ ; https://www.fox5ny.com/news/bronx-bodega-shooting-149-grill-deli-robbed ; https://bronx.news12.com/2026/08/25/man-dead-after-being-shot-in-chest-during-gunpoint-robbery-inside-bronx-deli/3TZhMMKr5PgOgxNFYjtjRF ; https://www.nbcnewyork.com/bronx/bodega-shooting-video-grand-concourse/6539946/ | Aug 25, 2026 (Tuesday): customer (33) shot and killed during a robbery at 149 Grill & Deli, East 149th Street, West Concourse; "caught on video"; amNY: cops found a discarded red hooded sweatshirt on Walton Avenue between East 149th and 150th Streets; "According to surveillance footage obtained by amNewYork, the sweater appears to match that which was worn by the gunman". Suspect later arrested (NY Post Aug 30). | §5 para 3 (stated factually, no names); Sources |
| BX16 | `Con Edison Bronx power outage 2025 OR 2026 customers heat wave` · Firecrawl search → scrape News 12 (directQuote) | https://bronx.news12.com/2026/07/03/5000-con-edison-customers-in-the-bronx-without-power-amid-heat-wave/ONmoL7BVphOWvTtg2dafc | Jul 3, 2026: ~5,000 Bronx customers without power; northeast and southeast Bronx most affected; ~1,000 in Riverdale; 8% voltage reduction in parts of northern Manhattan and the northwest Bronx incl. Riverdale, Marble Hill, Kingsbridge and Van Cortlandt Park. Also coned.com Jul 2 2026 release (31,000 restored citywide, excerpt). | §5.5 bullet 6; §9 H3 5; Sources |
| BX17 | P3 above | Bronx Times 2019 | Bronx DA CAMS. | §9 H3 10 |
| BX18 | BronxNet / Norwood News / Riverdale Press NVR or recorder stories | — | **EMPTY** (no item surfaced in the searches above). | — |

### Local Reddit
- r/bronx: R6 (porch-pirate thread, building camera) → Sources list; R7 not used. Bronx-specific NVR/recorder threads: **EMPTY**.

### Local licensing / rules
- NYS DOS Article 6-D licence covers CCTV work (G9) → §8.5 bullet 1. NYC DCWP: Home Improvement Contractor licence exists (G12) — scope for low-voltage NVR work not established → not on page, FLAG.
- NYC biometric sign law §22-1202 (G6–G7) → §8.5 bullet 2; §9 H3 14.
- NY Penal Law 250 audio (G8) → §8.5 bullet 3; §9 H3 15.
- FCC covered equipment (G1–G5) → §8.5 bullet 4; §9 H3 12–13; §10.5 H3 3.
- NYS Commercial Security Tax Credit (G10) → §8.5 bullet 5.
- LPC permits in historic districts (G11) → §8.5 bullet 6.
- NYC rules specifically on retention of private camera footage: **EMPTY** — no city law found requiring private buildings/stores to keep footage a set time (Brick Underground T7: no city law requires rental buildings to have working cameras).

### Prices used (Bronx §9 = 1.00× → Brooklyn base unchanged)
$220–$480 setup of owned NVR + cameras; $650–$1,500 new 8-channel build; $1,600–$5,500+ 16–32 ch/RAID; $190–$900 migration/expansion/repair; $175 camera line; $200 concealed drywall; $100 raceway / $200 conduit per line; $25 J-box; $150 recorder setup only (labor); $50 old equipment removal; $0 COI; $195/hr 3-hr min ($585) service after install. Worked example (§14): $650–$1,500 + 6 × $175 ($1,050) + 2 × $100 raceway ($200) = $1,900–$2,750 before cameras, UPS, lockbox. Instant block: "from $650 … each new camera line $175". Service schema AggregateOffer low $150 / high $5,500. See §2.7 FLAGS.

### Keywords (Bronx geo layer)
NVR installation Bronx; NVR installation Bronx NY; network video recorder installation Bronx; bodega camera recorder Bronx; apartment building NVR Bronx; Hikvision recorder replacement Bronx; Fordham Road, The Hub / Third Avenue, Southern Boulevard, Grand Concourse, Hunts Point, Bronx Terminal Market, Belmont, Westchester Square, White Plains Road, Co-op City, Riverdale, Kingsbridge, Mott Haven, Port Morris + §13 "we also serve" list. Alt/title on all 11 images carry "NVR installation" + "Bronx".

### Images (11) — permanent image rule
Drive "AESS Website Photos" has no NVR folder; CompanyCam not connected. All 11 copied, converted with Pillow (WebP q80, ≤1600 px wide, RGBA flattened on white for the PNG), each viewed before use; no faces, house numbers, readable plates or documents. Captions say "Example photo from another AESS job (not a Bronx property)" or "Manufacturer product photo". Library jpgs in images/commercial-security/, images/network/, images/cat6/, images/low-voltage/ showing uniformed technicians were rejected as AI-looking.
| images/nvr-installation/ | Source | Section |
|---|---|---|
| nvr-installation-bronx-recorder-monitor-camera-grid-under-cable-runs.webp (hero, 1107×935) | images/apartment-building-security-camera-installation/apartment-building-security-camera-installation-manhattan-recorder-monitor-showing-camera-grid-by-rack.webp | Hero |
| nvr-installation-bronx-turret-camera-storage-room-corner.webp | images/apartment-building-security-camera-installation/…-manhattan-turret-camera-in-corner-of-storage-room.webp | §5 |
| nvr-installation-bronx-network-cable-bundles-along-ceiling.webp | images/lorex-camera-installation/…-hudson-valley-blue-and-white-network-cable-bundles-along-ceiling.webp | §6 |
| nvr-installation-bronx-camera-on-steel-arm-stone-facade.webp | images/apartment-building-security-camera-installation/…-brooklyn-stone-facade-with-camera-on-steel-wall-arm.webp | §7 |
| nvr-installation-bronx-dome-camera-under-storefront-fascia.webp | images/commercial-security-camera-installation/…-dutchess-county-white-dome-camera-under-storefront-fascia.webp | §8 |
| nvr-installation-bronx-recorder-tile-dim-back-storeroom.webp | images/hikvision-security-camera-installation/…-ulster-county-recorder-tile-of-dim-back-storeroom.webp | §9 (after cluster 3) |
| nvr-installation-bronx-recorder-playback-brick-wall-to-lot.webp | images/dahua-camera-installation/…-suffolk-county-recorder-view-along-brick-wall-to-lot.webp | §9 (after cluster 5) |
| nvr-installation-bronx-hanwha-wisenet-recorder-product-photo.webp | images/nvr-hanwha-wisenet-arn1610s.png (manufacturer product photo) | §10 |
| nvr-installation-bronx-per-channel-bitrate-readout.webp | images/lorex-camera-installation/…-brooklyn-recorder-screen-per-channel-bitrate-readings.webp | §14 |
| nvr-installation-bronx-store-monitor-aisle-camera-grid.webp | images/commercial-security-camera-installation/…-dutchess-county-store-monitor-showing-aisle-camera-grid.webp | §15 |
| nvr-installation-bronx-bullet-camera-down-corridor-to-door.webp | images/dahua-camera-installation/…-long-island-bullet-camera-aimed-down-corridor-to-door.webp | Field Notes |
Scene choice: all indoor/commercial/apartment/urban (HV builder told to prefer outdoor/rural/house scenes). DAILY-LOG note: `images: 11 reused from images/apartment-building-security-camera-installation/, commercial-security-camera-installation/, dahua-camera-installation/, hikvision-security-camera-installation/, lorex-camera-installation/ + 1 manufacturer product photo (no real NVR Installation photos yet)`.

### FLAGS for Anwar (Bronx page)
1. Pricing: BYOE calculator Bronx +15% vs §9 1.00× (page uses §9); $150 recorder-setup vs $220–$480 setup range (both published with different scopes); silo ranges carried from old template pages. See §2.7.
2. Unsourced practice statements (installer knowledge, no URL): UPS sizing/clean shutdown, ventilation fixes, lockbox placement, port-forwarding/UPnP advice, ONVIF migration, ~100 m Ethernet limit, continuous-vs-motion bitrate behaviour at docks, time-sync advice, "most recorder faults back recording within one to two hours of arrival" (blueprint element 36 wording), install durations in FAQ 1.
3. Field Notes are written in Anwar's voice as general practice (what is checked in a cellar), not a specific job story — Anwar to confirm or replace with a real Bronx anecdote.
4. "Free estimates" (FAQ 8) relies on the site-wide "Get Free Quote"/"Same-Day Estimates" copy; COI $0 from the BYOE calculator.
5. NYC DCWP Home Improvement Contractor licence: not established whether it applies to NVR/camera work or whether AESS holds one — kept off the page.
6. Old-template siblings carry no cross-links to each other; every "live sibling … doesn't link back to /nvr-installation-bronx" failure in check_page.py is main-run wiring (siblings not edited by this builder).
7. The Hanwha product photo filename says ARN-1610S; the caption/alt name only "Hanwha Wisenet network video recorder" (model not independently verified).


<!-- Merged from nvr-installation-hudson-valley builder (batch 2026-10-18) -->
# NVR Installation — Hudson Valley hub research (part file, for merge into research/nvr-installation.md)

Page: `nvr-installation-hudson-valley` (REBUILD in place, 2026-10-18; was crawled-not-indexed as a near-duplicate template). Regional hub: (800) 486-0943 only; GBP Bronx (460 E Fordham Rd, `#bronx`); up-link Home (/); down-links to all six HV county NVR pages; cross-links to the NYC hub + 5 boroughs and the LI hub + Nassau/Suffolk; WhatsApp only as wa.me/17186790359.

Written by the HV hub builder in parallel with the Bronx builder (who owns `research/nvr-installation.md`, not edited here). Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. Shell curl blocked; tools used: WebSearch, WebFetch, Firecrawl search/scrape. "carried" = sourced by an earlier run in another research file (file + row named); not re-fetched today.

---

## A. Silo-level notes added by this build (usable on any NVR page)

| # | Exact query · platform | URL | Finding | Used (HV hub) |
|---|---|---|---|---|
| S1 | `Uniview NVR501 datasheet operating temperature power supply` · WebSearch → Firecrawl scrape (query, directQuote) | https://www.123securityproducts.com/nvr50108b.html | Uniview NVR501-08B (reseller spec table): operating temperature "-10°C+ 55°C (+14°F+131°F)"; power consumption "≤ 6W"; 12V DC; "Incoming bandwidth 80Mbps, Outgoing bandwidth 64Mbps"; 1 SATA; NDAA compliance "Yes" (reseller claim, not used). The manufacturer page (uniview.com → sgcdn.uniview.com redirect) **EMPTY (not accessible in build env — permission prompt timed out)**. | §5 para/5.5 bullet; Q&A barn/garage; Q&A battery; Q&A upload; §10.5 H3 1; hero caption; Sources |
| S2 | `WD Purple surveillance hard drive operating temperature specification datasheet` · WebSearch → WebFetch | https://www.wdc.com/products/business-internal-storage/wd-purple-nv.html | WD Purple: operating temperature "0°C to 65°C"; "workload rating of up to 180TB/year"; MTBF up to 1M hours (at 90 TB/yr and 40°C); "support up to 64 single-stream HD cameras". | §5.5; Q&A barn; §10 drives card; §10.5 H3 1; Sources |
| S3 | `Starlink port forwarding CGNAT residential public IP support` · WebSearch → WebFetch | https://www.dishytech.com/does-starlink-have-port-forwarding/ | "Starlink uses CGNAT to hand out IP addresses on most service plans"; "Starlink routers don't support port forwarding configurations"; public IPv4 via the Priority plan "meant for business customers"; public IPv6 possible but default router firewall blocks inbound. (Third-party guide, not Starlink — FLAG: Starlink's own support page not fetched.) | §5 para 3; §5.5; Q&A Starlink/port forwarding; §10.5 H3 3; Sources |
| S4 | carried — research/lorex-camera-installation.md L1, L3 | https://www.lorex.com/blogs/help/cables-ethernet-cable-length ; https://www.lorex.com/products/aex8-2-8port-epoe-switch | 328 ft (100 m) max Ethernet recorder→camera; ePoE 800 m at 10 Mbps / 300 m at 100 Mbps. | §5.5; Q&A barn 500 ft; Q&A gate power; §10.5 H3 2; Sources |
| S5 | carried — research/lorex-camera-installation.md R4 | https://www.reddit.com/r/Starlink/comments/17ub07p/rural_iowa_experiences_with_starlink_and_security/ | Mixed rural Starlink camera experiences ("works great" vs app stopped working). | Q&A Starlink; §10.5 H3 3; Sources |
| S6 | carried — research/hikvision-security-camera-installation.md F1, F2, F3, F4, F6, F7, N1, WF1 | DA-26-635A1.pdf; federalregister.gov 2026-13518; hikvision.com notices (Apr 7 / Sept 10, 2026); cooley.com 2024; globalsecurity mirror of FCC 2022 release; law.cornell.edu 2 CFR 200.216; fcc.gov/supplychain/coveredlist | FCC 2026 rule **confirmed by sources**: DA 26-635 (June 26, 2026), FR July 6, 2026, effective **July 16, 2026** — prohibits continued importation/marketing of previously authorized covered equipment; use-based for Hikvision/Dahua (public safety, government facilities, national security; critical-infrastructure prong **suspended** pending a definition); "consumers may continue to use any device… legally purchased and maintains an existing equipment authorization"; no new authorizations since Nov 2022; D.C. Cir. 2024 vacated CI definition as "arbitrarily broad"; Hikvision: import limits "could affect access to replacement parts, warranty service, and technical support"; Hikvision quotes FCC n.42/n.43 meanings of public safety (police, fire, EMS) and government facilities; 2 CFR 200.216 grant bar. | §5.5; §8.5 callouts; Q&A fire district; Q&A critical infrastructure; FAQ end of support; §10.5 H3 5; Sources |
| S7 | carried — research/hikvision-security-camera-installation.md A1, A2 | https://www.homeadvisor.com/cost/safety-and-security/install-a-surveillance-camera/ ; https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera/ny/new-york | HomeAdvisor national avg $1,289 ($589–$2,040), labour $80–$200/camera; Angi NY typical $797–$2,222. | §10.5 H3 6; Sources |

### Mandatory sources (§3) — status for this page
| # | Source | Result |
|---|---|---|
| 1 | Reddit | r/hudsonvalley excerpts (HV-R1, HV-R2 new; R5 carried); r/Starlink (S5). Excerpts only via Firecrawl search; reddit.com not scraped. |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so and tests seven commonly repeated claims instead |
| 6 | Landmarks | HV-LM1–LM6 |
| 7 | Use cases / building types | descriptive (FLAG: building-type cards are general practice, no statistics) |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Putnam DA (HV-N1), Governor broadband awards (HV-B2), Ulster ConnectALL (HV-B1), Daily Voice/Times Union/Central Hudson (HV-U*) |
| 10 | Hyperlocal | Putnam DA press item; Kingston HLPC; Newburgh city page |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — silo note research/lorex-camera-installation.md 1.1 #11; not re-tried |
| — | Google Drive "AESS Website Photos" | no NVR folder (only Cat6 Repair, Sonos, Fiber Optic, Soundbar, Smart Lock) — per brief |
| — | CompanyCam | not connected — per brief |

---

## B. Question register

### B.1 Old-template questions checked (asked on all 16 pre-rebuild nvr-installation-* pages; read 2026-10-18)
1. What is an NVR and how is it different from a DVR?
2. How many channels do I need?
3. How much hard drive storage do I need?
4. Do NVRs have monthly fees?
5. Can I view my NVR cameras remotely from my phone?
6. Why did my NVR stop recording?
7. Can I add more cameras to my existing NVR later?
8. Will cameras from one brand work with another brand's NVR?
9. What is RAID and do I need it?
10. Can you upgrade or migrate my old recorder?
11. Do you install NVRs for businesses and warehouses, not just homes?
12. How much does NVR installation cost in <area>? (area-worded on each of the 16 pages)

### B.2 nvr-installation-bronx (rebuilt 2026-10-18, mtime 08:36) — read and checked against before finalizing
Questions read from the rebuilt Bronx page (29 incl. two "?" H2s): install time in an occupied building; certificate of insurance; after-hours install; what is left behind; recorder warnings for dark camera/failed drive; keeping the recorder clock right; removing old recorder; charge to look first; payment; register monitor without recording access; boiler-room recorder; cellar vs lobby; bodega without back office; top-floor internet to cellar recorder; Con Edison drop — how long will the recorder keep going; hot windowless closet in August; admin password when managing agents change; owner/super/tenant association viewing; detective footage export; Bronx DA camera mapping; live view to precinct; Hikvision after July 2026 — must we take it out; covered-brand replacement availability; face-recognition signage; audio at the register; dock continuous vs motion; one recorder for lobby and garage a block apart.
**Changed on the HV hub because of overlap in meaning:** clock-after-outage FAQ (→ moving an existing recorder), footage-to-police FAQ (→ selling the house), "how will I know it stopped" (→ off-site clip copy), continuous-vs-motion (→ caretaker checklist), battery-hours Q (→ low-battery shutdown behaviour), "is my Hikvision illegal to keep" (→ critical-infrastructure neighbour Q; the keep-using fact stays as body text), install duration FAQ (→ remote settings changes), guest cottage own recorder (→ tenant cottage privacy/network).
Also checked against the Lorex HV hub (non-sibling) and reworded to avoid identical intents: licensing Q (→ who handles the permit), Starlink Q (→ port forwarding stopped after the move), burial/lightning Q (→ gate power budget).

### B.3 nvr-installation-hudson-valley — REBUILT 2026-10-18 (this run)
**Repair H2:** Recorder Gone Quiet Since the Last Storm?
**Q&A H3 (15):**
1. Can the recorder live in an unheated barn or detached garage?
2. What has to share the recorder's battery backup?
3. What should the recorder do when its battery is about to run out?
4. Does a whole-house standby generator make a battery on the recorder unnecessary?
5. Our barn sits about 500 feet from the house — what is the best way to get its cameras onto the recorder?
6. What changes when the cottage on the property is rented to a tenant?
7. Does a camera at the gate need its own power, or can the recorder end feed it?
8. Our old recorder setup relied on port forwarding — why did it stop working when we moved to Starlink?
9. How much upload does watching the recorder from the city take, and can it be reduced?
10. Does the recorder keep recording if the internet is down for days?
11. Who handles the permit when the recorder needs a new outlet or circuit?
12. Can a fire district, library or town hall still buy a Hikvision or Dahua recorder after the 2026 FCC order?
13. Does living beside a reservoir, substation or rail line turn a home recorder into "critical infrastructure" surveillance?
14. Should a weekend house's recorder copy clips off the property as a backup?
15. What should a caretaker check on the recorder during a visit to an empty house?
**FAQ (9, = FAQPage):**
1. Can an existing recorder be moved to a better room without rewiring every camera?
2. What should happen to the recorder when we sell the house?
3. Is a recorder with built-in PoE ports better than a separate switch for a property with outbuildings?
4. Should the recorder sit on the same network as the family's phones and laptops?
5. Can you install the recorder before we close on a house or while it is being renovated?
6. Does the recorder need its own monitor, or can it use a TV?
7. What happens when the recorder's maker stops releasing updates for it?
8. Can you adjust the recorder's settings without a technician driving up?
9. What does the power-off test at handover actually prove?
**§10.5 claim H3s (quoted claims, not questions):** "An NVR can go anywhere…"; "Power over Ethernet reaches about 300 feet, so a barn is no problem"; "You can watch your NVR from anywhere…"; "The recorder will just carry on when the power fails"; "Every Hikvision and Dahua box is now illegal in America"; "Having an NVR put in only costs a few hundred dollars"; "Anyone handy can install an NVR — no licence needed".
County child builds: do not reuse any of the above intents.

---

## Hudson Valley

**Thesis (distinct from the Bronx rebuild, which is about apartment buildings, stores, supers and police footage):** north of the city the recorder is the one component that must look after itself — often in an empty weekend house, on four utilities whose storms leave most of a county dark (Isaias: 34,150 of 38,693 NYSEG Putnam customers out), behind internet that may be Starlink/cellular CGNAT (no port forwarding) or a thin DSL/fixed-wireless uplink, with cameras on barns and gates beyond the 328-ft Ethernet limit. So valley NVR work is placement (heated interior; recorder 14–131°F, drive 0–65°C), power (UPS for recorder + PoE switch + modem + router; generator transfer; clean low-battery shutdown), reach (remote switch, fibre, bridge, long-range PoE; PoE power budget at the gate), remote access (cloud relay/VPN, sub-streams sized to the uplink), absence (off-site clip copies, caretaker checks), and rules (FCC July 2026 use-based Covered List order for public buyers; county electrician licensing; Putnam Ch. 145 low-voltage licence naming video surveillance). Same-silo brand-agnostic; distinct from the Lorex HV hub (brand/app-specific).

### Local news / incidents (HV-N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| HV-N1 | `Putnam County OR Dutchess County burglaries 2026 police surveillance video homes` · WebSearch → WebFetch | https://putnamcountyny.gov/component/zoo/item/burglers-convicted-after-long-term-investigation?Itemid=141 | Putnam DA, announced Sept 9, 2025: April 22, 2024 burglary in the Town of Southeast; "all-terrain vehicles and a motorcycle being stolen from the garage"; investigators "had no identifying information" at first (face coverings, gloves) and "extensively reviewed surveillance videos"; three co-defendants (Suffolk/Nassau residents) pleaded guilty to Attempted Burglary 2nd. | §5 para 4; §13 Town of Southeast card; Sources |
| HV-N2 | carried — research/lorex-camera-installation.md HV-N1 (Kingston thefts), HV-N2 (Tarrytown) | hudsonvalleyone.com 2026-09-01; lohud 2026-03-13 | Not used on this page (kept for county pages). | — |

### Broadband / internet (HV-B)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| HV-B1 | carried — research/lorex-camera-installation.md HV-B1 | https://www.ulstercountyny.gov/Government/News/Newsroom/2025/09/2025-09-25-Funding-for-Broadband-Expansion | Ulster $20.8M ConnectALL award; fibre to nearly 1,300 unserved locations; $61.8M incl. Verizon match. | §5 para 3; Sources |
| HV-B2 | `Dutchess County broadband unserved homes 2025 2026 rural internet Hudson Valley announcement` · WebSearch → WebFetch | https://www.governor.ny.gov/news/governor-hochul-announces-broadband-projects-totaling-more-636-million-achieve-universal | Sept 17, 2025: ~$391M proposed awards, 11 providers, nearly 54,000 locations; Reasnor Telephone $23.2M for 904 locations in Dutchess (fibre); Archtop Fiber five-county award incl. Dutchess (2,511 locations); Comcast $11.5M for 390 Putnam locations; Planet Fiber 16 Orange locations; **SpaceX (satellite) listed for 37 counties incl. Dutchess, Orange, Putnam, Rockland, Westchester** (13,615 locations, $20.4M); Verizon 13 counties incl. Ulster. | §5 para 3 (satellite in five HV counties); Sources |
| HV-B3 | same search (result title only) | https://hvwisp.com/counties/dutchess | Fixed-wireless ISP page for Dutchess (title only, not opened). | background only (fixed wireless named generally) |

### Reddit (HV-R)
| # | Exact query · platform | URL | Finding (excerpt) | Used |
|---|---|---|---|---|
| HV-R1 | `site:reddit.com hudsonvalley power outage generator internet cameras OR "security camera" OR NVR` · Firecrawl search | https://www.reddit.com/r/hudsonvalley/comments/snmpjq/my_past_power_outage_experience_solution/ | "After experiencing several multi-day outages, I called an electrician to see what I can do to have a portable generator hookup to my house." | Sources (owner discussions); informs generator Q&A |
| HV-R2 | same | https://www.reddit.com/r/hudsonvalley/comments/pkgj39/what_is_life_like_living_in_hv/ | "We lose power alot so if you work from home a generator will be necessary. During storms trees fall and roads close." | Sources; informs §5 para 2 |
| HV-R3 | carried — research/lorex-camera-installation.md R5 | https://www.reddit.com/r/hudsonvalley/comments/1ww3ifc/secondhome_owners_in_the_hudson_valley_who_looks/ | Second-home owners thread. | Sources (weekend-house context) |
| HV-R4 | `reddit hudsonvalley security cameras weekend house internet Starlink NVR` · WebSearch | (no r/hudsonvalley results; vendor/forum pages only) | EMPTY for a local thread on NVRs/Starlink. | — |

### Licensing / permits (carried — research/lorex-camera-installation.md HV-K1–K7, Putnam re-checked there 2026-10-18)
| # | URL | Finding | Used |
|---|---|---|---|
| HV-K1 | https://consumer.westchestercountyny.gov/trade-licenses | Westchester: plumbers and electricians must hold a county trade licence. (Also carried from hikvision WK1–WK7: home-improvement licence, county alarm licensing; Art. XV alarm-device definition EMPTY — not used.) | §8.5; Q&A permit; §10.5 H3 7; Sources |
| HV-K2 | https://ecode360.com/26997705 | Rockland Ch. 250: electrical contractor licence for wiring of 50 V or more. | same |
| HV-K3 | https://ecode360.com/6607815 ; https://www.putnamcountyny.gov/consumer-affairs | Putnam Ch. 145 low-voltage/limited-data technician: covers video surveillance systems ≤90 V/5 A starting at an outlet installed by a licensed electrician; no one may offer that work unlicensed; county list of licensed technicians. | §5.5; Six Counties (Putnam); §8 Route 6 card; §8.5; Q&A permit; §10.5 H3 7; Sources |
| HV-K4 | https://ecode360.com/35131702 | Ulster Ch. 185 Electrical Licensing Law; electrical work includes signalling, communication, alarm, data transmission. | Q&A permit; Sources |
| HV-K5 | https://www.orangecountyny.gov/DocumentCenter/View/311/Local-Law-No-1-of-2024-Electrical-Licensing-PDF | Orange: L.L. 8-2007 county electrician licence, revised by L.L. 1-2024. | Six Counties (Orange); Q&A permit; Sources |
| HV-K6 | carried | Dutchess: no county-wide contractor licence found → town rules apply. | §8.5; Q&A permit |
| HV-K7 | http://www.fishkill-ny.gov/uploads/3/8/0/7/38072219/building_permit_package_2016_-_commerical___multi-family.pdf | Town of Fishkill 2016 commercial/multi-family package: electrical inspection by an approved independent agency. | Q&A permit |
| HV-G6 | https://www.nysenate.gov/legislation/laws/CVR/52-A | Civil Rights Law §52-a (neighbour's residential backyard). | §8.5; Q&A tenant cottage; Sources |
| HV-G8 | https://nyc-business.nyc.gov/nycbusiness/description/nyscommercialsecuritytaxcredit | NYS Commercial Security Tax Credit: ≤50 employees, up to $3,000 per retail location. | §8.5; Sources |

### Utilities / outages (carried — research/lorex-camera-installation.md HV-U1–U6)
| # | URL | Finding | Used |
|---|---|---|---|
| HV-U1 | https://www.oru.com/en/about-us/media-center/corporate-facts | O&R serves Orange, Rockland (and Sullivan). | §5 para 2; Six Counties |
| HV-U2 | https://www.cenhud.com/en/about-us/our-service-territory/ | Central Hudson ~315,000 electric customers, NYC suburbs to Capital District. | §5 para 2 |
| HV-U3 | https://dailyvoice.com/article/isaias-new-update-these-putnam-county-communities-most-affected-by-power-outages/ | Isaias Aug 2020: 34,150 of 38,693 NYSEG Putnam customers out (≈88%, our arithmetic). | §5 para 2; §5.5; Six Counties (Putnam); Q&A low battery; §10.5 H3 4 |
| HV-U4 | https://www.timesunion.com/hudsonvalley/news/article/hudson-valley-thunderstorms-damage-outages-19542886.php | June 2024: ~60,000 O&R + Central Hudson customers out. | §5 para 2; §10.5 H3 4 |
| HV-U5 | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ | Sept 2026 nor'easter: restoring >19,000 homes and businesses. | §5 para 2; §10.5 H3 4 |
| HV-U6 | https://www.nyseg.com/documents/d/nyseg/psc120_section-1 | NYSEG Westchester towns: Bedford, Lewisboro, North Salem, Pound Ridge, Somers. | Six Counties (Westchester) |

### Landmarks / places (HV-LM)
| # | Source | Finding | Used |
|---|---|---|---|
| HV-LM1 | carried hikvision WL5 · https://dec.ny.gov/places/kensico-reservoir | 2,145-acre NYC reservoir in Valhalla; Catskill + Delaware water; last stop before aqueducts. | §13 card; Q&A critical infrastructure |
| HV-LM2 | carried hikvision WL3 · https://airport.westchestercountyny.gov/ (Wikipedia excerpt) | County-owned; land in North Castle, Harrison, Rye Brook; ~3 nmi NE of White Plains. | §13 card |
| HV-LM3 | carried lorex HV-LM1 · https://www.newburghny.org/discover-newburghs-east-end-historic-district/ | "second largest designated historic site in New York State"; Washington's Headquarters. | §13 card |
| HV-LM4 | carried lorex HV-LM2 · https://kingston-ny.gov/hlpc | Five historic districts (Stockade 1974); HLPC review of exterior work visible from public ROW before permit. | §7 river-city card, §7.5 bullet; §13 card |
| HV-LM5 | carried lorex HV-LM3 · https://www.governor.ny.gov/news/governor-hochul-announces-development-partner-build-transit-oriented-housing-beacon-metro | 265 mixed-income units on the lot beside Beacon station. | §13 card |
| HV-LM6 | HV-N1 (Putnam DA) | Town of Southeast garage burglary solved with surveillance video. | §13 card |
Corridor and town names (Route 59, Central Avenue, Route 17/I-84, Route 9, Route 6, Broadway Kingston/Route 9W; Mahopac, Carmel, Kent, Patterson, Millbrook, Rhinebeck, Woodstock, Saugerties, Pearl River, Esopus) are used as place names only — FLAG: no per-corridor source, no business claims attached.

### Pricing used (§9 multipliers — no invented prices)
Silo base (Brooklyn 1.00×) = the figures published identically on all 16 pre-rebuild NVR pages (also recorded by the Bronx builder in research/nvr-installation.md §2.7): BYOE setup $220–$480; new 8-channel system (recorder + PoE + drive, cameras/cabling separate) $650–$1,500; 16–32 ch/RAID $1,600–$5,500+; upgrade/migration/repair $190–$900. Each end × county factor, round half-up (Python Decimal ROUND_HALF_UP).
| County | × | Setup own recorder | New 8-ch system | 16–32 ch / RAID | Upgrade/migration/repair |
|---|---|---|---|---|---|
| Westchester | 1.25 | $275–$600 | $813–$1,875 | $2,000–$6,875+ | $238–$1,125 |
| Rockland | 1.30 | $286–$624 | $845–$1,950 | $2,080–$7,150+ | $247–$1,170 |
| Orange | 1.40 | $308–$672 | $910–$2,100 | $2,240–$7,700+ | $266–$1,260 |
| Putnam | 1.45 | $319–$696 | $943–$2,175 | $2,320–$7,975+ | $276–$1,305 |
| Dutchess | 1.53 | $337–$734 | $995–$2,295 | $2,448–$8,415+ | $291–$1,377 |
| Ulster | 1.53 | $337–$734 | $995–$2,295 | $2,448–$8,415+ | $291–$1,377 |
Service $195/hr, 3-hr minimum ($585) verbatim, not multiplied. Schema Offers: new 8-ch min/max per county.
**FLAG:** the base ranges bundle equipment with labour (the 8-ch line includes the recorder and drive); v2.3 §9 says camera-calculator multipliers apply to labour only, but no labour/equipment split exists for these NVR ranges, so the whole range was multiplied. Anwar to confirm, or supply a labour/equipment split. The old HV hub page showed the Brooklyn figures unchanged ($220–$480 etc.) — replaced.

### House practices stated without an external source (FLAG for Anwar)
- Recorder kept in heated interior space (never attic/barn/garage unless conditioned); camera covering the recorder's location; battery backup on recorder + PoE switch + modem + router; power-off (main breaker) test and mobile-data remote test at handover; after-dark check.
- Low-battery shedding of low-priority cameras at the PoE switch and clean recorder shutdown via UPS signal (general practice; depends on model support — page says "many" devices can).
- Separate camera network/VLAN; sub-stream for remote viewing; off-site clip copies sized to the uplink; caretaker login without delete/settings rights; caretaker 5-point checklist; written channel map and handover sheet with model/firmware.
- Policy: covered (Hikvision/Dahua) recorders declined at fire districts, libraries, town/village halls and federally grant-funded projects; non-covered brand suggested for businesses paid to watch infrastructure (our reading of the FCC use test, not an FCC ruling).
- No standing remote access to customer recorders unless agreed in writing.
- Two-hour arrival windows any day 8 AM–8 PM (openingHours Mo-Su 08:00-20:00, silo convention); "writing video again within one to two hours of arrival" (silo convention).
- Six-county building-type descriptions (fieldstone cellars, raised ranches, structured-wiring panels in new subdivisions) are general descriptions, not sourced statistics.
- Field Notes = installer-voice method note (Anwar), no specific job story.

### Images (11) — Drive: no NVR folder; CompanyCam not connected → permanent image rule
Folder: `images/nvr-installation/` (shared with the Bronx builder; HV files all named `nvr-installation-hudson-valley-*`). Each source opened and looked at (contact sheets). 6 manufacturer product shots (labelled as product photos on the page, white margins trimmed) + 5 real AESS job photos from other silos (labelled "from an AESS job outside the region, shown only as an example"); no faces, house numbers, plates or readable documents. Chose different source files from the Bronx builder's set (Bronx used the stone-facade arm, storefront fascia, bitrate readout, cable bundles, brick-wall playback, storage-room turret, dim storeroom, aisle grid, corridor bullet, recorder grid, Hanwha recorder).
| Output (…/nvr-installation-hudson-valley-<name>.webp) | Source | Note |
|---|---|---|
| uniview-recorder-product-photo (500×200) | images/nvr-uniview-nvr501.png | product; trimmed |
| ubiquiti-unvr-four-bay-recorder-product-photo (475×128) | images/nvr-ubiquiti-unvr.png | product; trimmed |
| reolink-recorder-product-photo (500×165) | images/nvr-reolink-nvs8.png | product; trimmed |
| tp-link-vigi-eight-channel-recorder-product-photo (444×191) | images/nvr-tplink-vigi-nvr1008h.png | product; trimmed |
| hikvision-sixteen-channel-recorder-product-photo (500×140) | images/nvr-hikvision-ds7616ni.png | product; trimmed |
| exacqvision-rack-mount-server-product-photo (500×182) | images/commercial-security-camera-installation/commercial-security-camera-installation-dutchess-county-rack-mount-video-recorder-product-photo.webp | product; trimmed |
| pan-tilt-camera-with-warm-light-product-photo (257×272) | images/dahua-camera-installation/dahua-camera-installation-orange-county-pt-camera-with-warm-light-leds-product-photo.webp | product; trimmed |
| eyeball-dome-in-corner-above-wall-sensor (440×560) | images/hikvision-security-camera-installation/hikvision-security-camera-installation-westchester-county-white-eyeball-dome-in-corner-above-wall-sensor.webp | real AESS job photo |
| black-bullet-camera-high-on-plain-wall (1247×935) | images/dahua-camera-installation/dahua-camera-installation-orange-county-black-bullet-camera-high-on-painted-wall.webp | real AESS job photo |
| small-cameras-on-high-wall-of-open-room (907×440) | images/dahua-camera-installation/dahua-camera-installation-long-island-small-cameras-on-high-wall-of-open-hall.webp | real AESS job photo |
| bullet-and-dome-at-two-heights (750×560) | images/hikvision-security-camera-installation/hikvision-security-camera-installation-westchester-county-high-wall-bullet-and-ceiling-dome-at-two-heights.webp | real AESS job photo |
Rejected after viewing: images/cat6/*hudson-valley* crew photos, images/low-voltage/* crew photos (polished, branded-shirt, AI-looking scenes with faces); hikvision LI / westchester "dome under fascia / signboard beside bare tree" (same building as the Lorex HV and Bronx storefront-fascia images); hikvision LI bitrate table (same source family as Bronx's bitrate readout).
No real outdoor/rural house photos exist in the repo; FLAG — real valley NVR job photos needed.

### Build notes
- check_page.py: all page-side checks pass; the only failures are 8 sibling link-backs (brooklyn, long-island, manhattan, nassau-county, nyc, queens, staten-island, suffolk-county don't link to /nvr-installation-hudson-valley) — main-run wiring; subagents may not edit sibling pages.
- Paragraph masked-similarity scan (difflib, ≥6-word paragraphs/headings): no body paragraph ≥0.65 vs the rebuilt Bronx page or the old-template siblings; residual ≥0.65 matches are blueprint-fixed H2 patterns ("Types of NVR Equipment We Install", "What AI Gets Wrong About…"), short step headings and the source-link lists / contact+warranty block shared in form with the Lorex HV hub.

---

## Westchester County

Build 2026-10-18 (REBUILD in place of `nvr-installation-westchester-county`, was crawled-not-indexed). Direct line (914) 877-2578 in body, CTAs, sticky bar and schema; (800) 486-0943 only in the shared mega-nav header. GBP Bronx (460 E Fordham Rd, `#bronx`). Up-link `/nvr-installation-hudson-valley`. WhatsApp only wa.me/17186790359. Tools: Firecrawl search (`mcp__Firecrawl__firecrawl_search`) and scrape (`mcp__Fire_Crawl__firecrawl_scrape`, query/directQuote). Rows marked "carried" were fetched by earlier runs in research/hikvision-security-camera-installation.md (W*) or research/dvr-upgrade.md (H-W/C-W/F-W/L-W) and are cited there with URLs.

**Thesis (distinct from Bronx = custody in old rented buildings; HV hub = outages/Starlink/barns/weekend houses; Ulster = Catskill/Kingston/rural; hikvision-…-westchester-county-ny = FCC "use test"; dvr-upgrade-westchester = co-op governance):** a Westchester recorder is bought by one party and judged by another — a management company running new towers (New Rochelle downtown, Yonkers waterfront), a district manager and insurer for corridor stores (Central Park Ave, Boston Post Rd, Mamaroneck Ave), the Office of Cannabis Management for dispensaries (9 NYCRR §125.3), one of 45 local police agencies, or household staff law on estates. So the job is a written spec: central vs per-floor recording, door-event and POS integration, multi-site viewing, retention matched to claim lag, 60-day/8-hour/5-minute dispensary requirements, export format, licence verification.

### Source matrix (§3) — Westchester
| # | Source | Result |
|---|---|---|
| 1 | Reddit | r/Westchester Flock-camera threads (WR-N1, excerpts); carried RW1/R-W1 not reused. Westchester NVR-specific thread: EMPTY. |
| 2–5 | PAA / PASF / Answer the Public / AI Overview | EMPTY (not accessible in build env). §10.5 says so on the page and tests seven commonly repeated claims. |
| 6–7 | Landmarks / building stock | WN-H1–H4, WN-C1–C4 below. |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env). |
| 9–10 | Local news / hyperlocal | News 12 Westchester (New Rochelle burglary Jul 2026; Cross County Center arrests Oct 2026; Yonkers garage Sept 2026 carried), News 12 HV (Hudson Piers 2025), Governing (2025), ABC7 Ida (carried). |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env); a Yelp dispensary listing page surfaced as an excerpt only (no review text). |

### Rows
| ID | Exact query · platform | URL | Finding | Page + section |
|---|---|---|---|---|
| WN-R1 | `New York Office of Cannabis Management adult-use dispensary security video surveillance requirements retain footage days 9 NYCRR` · Firecrawl search → scrape (directQuote) | https://www.law.cornell.edu/regulations/new-york/9-NYCRR-125.3 (also https://cannabis.ny.gov/chip-academy-2.17-retail-regulations-compliance-overview excerpt) | §125.3: continuous recording during hours of operation and when cannabis handled, motion otherwise; remote access/login for immediate viewing by the Office; ≥60-day retention; unaltered copies on request; hold for pending investigations; date/time stamp synchronised to NIST; storage secured against tampering/theft; failure notification within 5 minutes; ≥8 hours operation in power outage; surveillance rooms locked; (iv) "proprietary format that ensures authentication … no alteration". | §5 para 4 + facts; §6 card; §8 card; §8.5; Q&A dispensary ×2; §10.5 claims 1, 2, 7; FAQ 2; Sources |
| WN-R2 | `Westchester County cannabis dispensary opened Yonkers OR "White Plains" OR "New Rochelle" OR "Mount Vernon" 2025 2026` · Firecrawl search (excerpts) | https://cannabisrealmny.com/ ; https://budrcannabis.com/location/yonkers/ ; https://www.ocala.com/videos/news/local/westchester/2025/10/10/new-rochelle-ny-new-cannabis-reserve-dispensary-opens/86629005007/ ; https://blackwestchester.com/westchesters-first-recreational-cannabis-dispensary-opens-in-mount-vernon/ | Licensed dispensaries at 475 Central Ave White Plains (OCM-CAURD-24-000046), 887 Yonkers Ave Yonkers, North Ave New Rochelle (opened Oct 10, 2025); first Westchester rec dispensary in Mount Vernon (headline). Businesses NOT named on page. | §5 para 4; §8 card; §13 n/a |
| WN-L1 | `New York Labor Law 203-c video recording restroom locker room changing room employer prohibited` · Firecrawl search (excerpts) | https://www.nysenate.gov/legislation/laws/LAB/203-C ; https://newyork.public.law/laws/n.y._labor_law_section_203-c | "No employer may cause a video recording to be made of an employee in a restroom, locker room, or room designated by an employer for employees to change their clothes, unless authorized by court order." | §8.5; Q&A housekeeper/nanny; §10.5 claim 5; Sources |
| WN-L2 | `Westchester County Consumer Protection license lookup search licensed home improvement contractor alarm business verify` · Firecrawl search (excerpts) | https://consumerlicenseweb.westchestergov.com/ ; https://consumer.westchestercountyny.gov/trade-licenses-search ; https://consumer.westchestercountyny.gov/home-contractors-and-trades/home-improvement-contractors ; https://www.westchestercountyny.gov/licenses-and-permits | County online search for licensed home improvement contractors; separate plumber/electrician trade-licence search; judgments/liens check via county clerk; Consumer Protection phone (914) 995-2155 on the licences page. | §5.5; §8.5; Q&A licence check; Sources |
| WN-L3 | carried WK1/L-W1/L-W3 | consumer.westchestercountyny.gov; municode Ch. 863 Art. XVI | HI licence = residences ≤3 units, alarm-business exemption; electricians need county trade licence. | §8.5; Q&A licence check |
| WN-P1 | `Westchester County number of local police departments …` · Firecrawl search → scrape (directQuote) | https://en.wikipedia.org/wiki/Law_enforcement_in_Westchester_County ; https://www.nyclu.org/uploads/2026/06/…COMPLAINT…pdf (excerpt: RTC created 2017, "almost 40 local police departments") | "There are forty-five local police agencies in Westchester County." | §5 para 3; facts; Q&A export format; §10.5 claim 7; Sources |
| WN-P2 | carried WP1/WP2 | publicsafety.westchestercountyny.gov/crime-analysis-unit ; patch.com Peekskill 2017 | RTC: >100 agencies; cameras + fixed/mobile LPR; HQ Hawthorne; launched Dec 2017. | §5; facts; §13 card; Q&A plate readers; §10.5 claim 4 |
| WN-N1 | `westchester.news12.com 2026 surveillance video store burglary …` · Firecrawl search → scrape (directQuote) | https://westchester.news12.com/2026/07/24/family-owned-new-rochelle-restaurant-loses-more-than-30000-in-brazen-burglary/3aU8y0asc3gPYBcOAehUqH | Jul 24, 2026: ~3:30 a.m. Monday, Modern Restaurant & Lounge, Huguenot Street; security video shows two suspects breaking through front doors; went directly to office with safe; >$30,000 taken. (Restaurant not named on page.) | §5 para 3; §8 added paragraph; Sources |
| WN-N2 | same search → scrape | https://westchester.news12.com/body-cam-video-shows-police-arresting-two-shoplifting-suspects-fleeing-macys-on-same-day | Oct 9, 2026: two shoplifting arrests at Macy's, Cross County Center (Sept 18), captured on Yonkers police body cameras. | Not used on page (body-cam, not store NVR) |
| WN-N3 | carried N-W1 | westchester.news12.com 2026-09-05 Yonkers garage | Surveillance video from garage + stores linked pair to car break-ins, Warburton Ave. | §5 para 3; Sources |
| WN-H1 | `New Rochelle downtown redevelopment apartments units built since 2015 rezoning towers` · Firecrawl search → scrape (directQuote) | https://www.governing.com/magazine/getting-ahead-of-the-nimby-energy-an-older-city-learns-to-build (Oct 20, 2025) ; https://www.newrochelleny.gov/1015/TOD-Downtown-Cluster (excerpt) | Zoning approved Dec 8, 2015; ">4,500 new units are already online, with another 6,500 on the way"; quote "We've authorized 11,000 units downtown." | §5 para 2; facts; §13 card; Sources |
| WN-H2 | `Yonkers downtown waterfront new apartment towers units …` · Firecrawl search → scrape (directQuote) | https://hudsonvalley.news12.com/2025/06/19/new-apartments-on-the-yonkers-downtown-waterfront-open-10-to-be-affordable-housing/OwWLBWS3Sl1XcdzgvMPgR | Jun 18, 2025: Hudson Piers Phase 1 = two of six rental buildings; "final and largest piece of the Yonkers Downtown Waterfront Revitalization". (Westfair 2018 map: excerpt only, not used.) | §5 para 2; facts; §13 card; Sources |
| WN-H3 | carried H-W1 (Census ACS 2023 5-yr B25024 etc.) | api.census.gov … ucgid=0500000US36119 | 391,861 units; 66,378 in 50+ unit buildings; median year built 1958. | §5 para 2; facts; §7 card |
| WN-C1 | carried C-W1/C-W2/C-W3/C-W4 | 914inc Platinum Mile; NYT 1995 Central Park Ave; Wikipedia US 1; Wikipedia Cross County Center | Platinum Mile medical conversions; Central Park Ave ~8.5 mi Yonkers–Greenburgh–White Plains; US 1 to Port Chester; Cross County opened 1954, lot on former peat bog. | §5; §8 cards; §13 cards; Sources |
| WN-F1 | `Mamaroneck flood … Ida … Mamaroneck Avenue` · Firecrawl search (excerpts) | https://abc7ny.com/post/flooding-brooklyn-nj-nyc-flooded/10994078/ ; https://www.nan.usace.army.mil/Missions/Civil-Works/Projects-in-New-York/Mamaroneck-Sheldrake-Rivers/ | ABC7 Sept 2, 2021: up to 14 ft of water, Mamaroneck Avenue completely covered, basements to first floor; USACE: "severe flood risk persists" along Mamaroneck and Sheldrake Rivers "based on the recurrence of flood events". | §5 facts; §6 card; §7 table/bullets; §13 card; Sources |
| WR-N1 | `site:reddit.com r/Westchester OR r/yonkers OR r/NewRochelle security camera footage package stolen building management` · Firecrawl search (excerpts) | https://www.reddit.com/r/Westchester/comments/1vom0uv/why_is_flock_cameras_expanding_so_fast_in/ ; …/1v68ji3/flock_spy_cameras_in_westchester/ ; …/1vh30pk/flock_cameras/ ; …/1nuvppj/close_your_windows_lock_your_doors/ | r/Westchester residents debating Flock plate-reader cameras spreading in the county; a burglary victim: "My entire block has over 30 videos of …" (excerpt). | Q&A plate readers; §10.5 claim 4; Sources (one thread) |
| WN-G1 | carried silo G1/G2, G8, G9, G10 | FCC DA 26-635 / FR 2026-13518; NY Penal Law 250; DOS 19 NYCRR 195.2; NYS Commercial Security Tax Credit | as in §2.5 | §8.5; Q&A locked recorder; §10.5 claim 5; FAQ brands |

### Pricing used (§9 Westchester 1.25×, Decimal ROUND_HALF_UP on the silo base in §2.7)
$275–$600 setup own NVR; $813–$1,875 new 8-ch; $2,000–$6,875+ 16–32 ch/RAID; $238–$1,125 migration/expand/repair; $219 camera line; $250 concealed drywall; $125 raceway / $250 conduit; $31 J-box; from $188 recorder setup only; $63 removal; $0 COI; $195/hr 3-hr min ($585) not multiplied. Worked example: $813–$1,875 + 8×$219 ($1,752) + 3×$125 ($375) = $2,940–$4,002. Service schema AggregateOffer $188–$6,875. Same as HV hub's Westchester row for the four ranges.

### Images (11) — Drive: no NVR folder; CompanyCam not connected → permanent image rule
Viewed every source; no faces, plates, house numbers or readable documents (logo/TV/"Guest Services"/monitors cropped out). The Drive-sourced `images/cat6-repair/aess-*` and `images/fiber-optic-installation/aess-*` photos were viewed and REJECTED (polished branded-uniform crew shots with faces — AI-looking). Remaining real AESS sources not already used by Bronx/HV/Ulster crops were few, so the set is 3 real + 8 product.
| images/nvr-installation/nvr-installation-westchester-county-… | Source | Placement |
|---|---|---|
| sixteen-channel-recorder-front-panel-product-photo.webp (867×167) | images/nvr-lorex-4k-16ch.png (trimmed) | Hero |
| bullet-camera-on-pendant-mount-in-office-ceiling.webp (935×850) | images/rockland-toyota-ceiling-bullet.jpeg crop (0,150,935,1000), monitors excluded | §5 |
| recorder-kit-with-four-bullet-cameras-and-monitor-product-photo.webp | images/products/d5.png | §6 |
| black-dome-camera-on-drop-ceiling-above-tall-white-wall.webp (635×440) | images/rockland-toyota-dome-camera.jpeg crop (300,0,935,440), logo/TV/sign excluded | §7 |
| small-black-camera-in-ceiling-grid-above-soffit.webp (555×470) | images/rockland-toyota-active-deterrent.jpeg crop (380,150,935,620) | §8 |
| eight-channel-poe-recorder-product-photo.webp | images/nvr-trendnet-tv-nvr208.png | §9 (stores) |
| large-vented-recorder-chassis-product-photo.webp | images/nvr-ens-titanium.png | §9 (dispensaries) |
| compact-recorder-with-front-usb-ports-product-photo.webp | images/nvr-honeywell-35-series.png | §10 |
| recorder-with-four-turret-cameras-product-photo.webp | images/products/a2.png | §14 |
| dual-lens-turret-camera-with-warning-lights-product-photo.webp | images/cam-dual-lens-active.jpeg | §15 |
| two-lens-ptz-camera-product-photo.webp (554×554) | images/cam-ptz-dual.jpeg | Field Notes |
DAILY-LOG note: `images: 11 = 3 real AESS job photos (re-cropped, other jobs) + 8 manufacturer/retail product shots (no real NVR Installation photos yet)`.

### House practices stated without an external source (FLAG)
Central vs per-floor recording advice; door-event integration feasibility "depends on products"; VMS per-camera licensing as "commonly"; claim-letter timing and clip-locking; POS overlay methods and card masking; multi-site light sub-streams; landlord lot-footage advice; package-room camera pattern; elevator travelling-cable/bridge and elevator-contractor involvement; dispensary load measurement + generator transfer + timed breaker test; recorder not in the safe room + offline alert; Platinum Mile privacy masks; flood-height mounting; locked-recorder owner-reset routes (no unofficial tools); export native + MP4 routine; plate-camera narrow/fast-shutter; drive wipe/destroy options; twice-yearly check visit content; no trip line on price sheet; brands list (Lorex, Uniview, Hanwha, Dahua, Hikvision); "most recorder faults writing again within one to two hours of arrival" (silo convention); ADT/Ring/SimpliSafe comparison table is qualitative (no competitor prices). Field Notes = method in Anwar's voice, not a specific job story.

### Question register additions — nvr-installation-westchester-county (REBUILD 2026-10-18)
§9 Q&A (H3):
1. Our new New Rochelle tower has a telecom closet on every floor — should each floor get its own recorder, or should everything record in one place?
2. The building's fob system logs every door swipe — can the recorder line those swipes up with the video?
3. Our management company already runs a video management platform at its other buildings — should this one get a standalone NVR or join that system?
4. Can the cameras inside our tower's elevator cabs record to the same NVR as the lobby?
5. Residents say parcels keep disappearing from our Yonkers building's package room — what should the recorder be set to capture there?
6. A slip-and-fall claim letter reached our Central Avenue store six weeks after the fall — why was the clip already gone, and how do we keep the next one?
7. Can the recorder show the register transaction on top of the video at our Boston Post Road store?
8. Our district manager oversees six Westchester stores — can one screen show all six recorders without six separate apps?
9. The landlord of our Central Park Avenue strip centre records the parking lot — how do we make sure we can get that video when a customer's car is hit?
10. Our White Plains dispensary opens next quarter — what has to be finished on the recorder before the state inspects the shop?
11. The dispensary rule says the system must keep running for eight hours in a power cut — what does that take for the recorder and cameras?
12. We have a housekeeper and a nanny at our Scarsdale house — which indoor cameras can the recorder keep, and where must there never be one?
13. We bought a house in Scarsdale and the previous owner's recorder is locked — can anyone get into it, or does it have to go?
14. How do we check that a camera company is properly licensed in Westchester before it opens our recorder?
15. Should exported clips be MP4 files or the recorder's own format when a Westchester police department or an insurer asks for them?
16. Licence-plate readers are going up around our village — does our building still need its own camera on the parking entrance?
§17 FAQ (visible == FAQPage, 10):
1. Can you price a new tower's recording system from the low-voltage drawings before the building is finished?
2. Can you give us the camera, storage and power details in a form our dispensary security plan can use?
3. Can you come back twice a year to check the drives, clock and firmware?
4. How far into northern Westchester do you travel, and does the price change?
5. Which recorder brands do you install in Westchester?
6. What happens to the data on our old recorder's drives when you take it away?
7. Will the written quote name the recorder model and drive size so we can compare it against another bid?
8. Do you need our internet login to set up the recorder?
9. Our store lease says no drilling into the storefront — how do the cameras and recorder go in?
10. Can you work around a tower's move-in schedule and elevator bookings?
§10.5 claims (not questions): motion-only always smart; MP4 is all anyone needs; bigger building = bigger NVR; police plate readers make private cameras pointless; camera anywhere inside your own home; analytics catch shoplifters for you; any recorder's clock is good enough.
De-dup notes: read against §4 register, Bronx/HV lists and the parallel Ulster page (read 09:36). Dropped my first-draft "Ida — where should a Sound Shore shop keep its recorder?" (≈ Ulster "sea-level rise … where should a Rondout business put its recorder") — flood placement kept as body text only; reframed dispensary Q from "what does the rule ask of the recorder" to pre-inspection readiness (Ulster owns continuous-vs-motion, OCM remote access, investigation hold, locked room); dropped a cost-claim §10.5 H3 (≈ Ulster's national-average claim). Borderline pair for coordinator: my fob-swipe/door-event Q2 vs Ulster "Can our existing alarm panel tell the recorder when someone opens the door after hours?" (access-control credential search vs alarm-panel input). Repair/CTA H2s rewritten so they do not end in "?" (avoid Bronx "Recorder Beeping, Dark or Full…?" and old-template storage intent).
This page owns for the silo: per-floor vs central recording in towers, fob/door-event search, VMS vs standalone, elevator cab cameras, package rooms, claim-lag retention and clip locking, POS overlay, multi-store viewing, landlord lot footage, dispensary pre-inspection and 8-hour runtime, household-staff interior recording, locked inherited recorder, licence verification lookups, export format, public plate readers vs private cameras; FAQ: pricing from drawings, dispensary documentation, twice-yearly checks, northern travel, brands, drive data disposal, model/drive on quote, internet login, no-drill leases, tower elevator bookings.

### Build notes
- check_page.py: 13,229 rendered words; title 55; meta 158; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10; 186,265 B (HV hub 183,846 → margin 2.4 KB; Bronx 178,365; Ulster 174,765 at check time). Only failures: 12 live siblings not linking back (main-run wiring).
- Masked-geo similarity (difflib on masked word lists; blocks p/li/td/h2/h3/figcaption ≥8 words): page vs Bronx 0.111, HV 0.048, Ulster 0.051, old-template siblings ≤0.039. Paragraph max ≥0.65 only for: blueprint-fixed H2 "What AI Gets Wrong About NVR Installation in…", the mandated warranty sentence paragraphs and the constant NAP/licence lines. Highest non-constant 0.632 (Bronx coverage intro).

---

## Ulster County

Build 2026-10-18 (REBUILD of `nvr-installation-ulster-county`, was crawled-not-indexed). Direct line (845) 640-3835 in body/CTAs/schema; (800) 486-0943 only in the shared header chrome · GBP Bronx (460 E Fordham Rd, `#bronx`) · up-link `/nvr-installation-hudson-valley` · WhatsApp only as wa.me/17186790359. Format v2.3 §12.4. Tools: WebSearch, WebFetch (+ rows carried from other research files, named). Nothing invented; excerpts marked.

**Thesis (distinct from Bronx = custody/evidence in buildings others control; HV hub = absence, outages, Starlink CGNAT, 328-ft barns; Westchester (parallel) = towers/estates/municipal/managed portfolios; hikvision-…-ulster-county-ny = covered-use buildings, absence, satellite, solar):** in Ulster the recorder has two enemies — **water** (Irene's record creek floods on the Esopus/Stony Clove/Rondout; Kingston's tidal Rondout waterfront with an 8.2-ft base flood elevation and up to 36 in sea-level rise by 2060; damp stone cellars) and **the calendar** (regulated retention: NY cannabis rules 60 days / 8-hour outage / 5-minute failure alert; Kingston PD's own cameras overwrite in 14–21 days). So the page is about placement above water, retention sized in writing, and the county's own building stock (Stockade/Rondout historic districts, iPark 87 campus, Ellenville mill/canal buildings, Woodstock/Saugerties studios) and rules (Ulster Ch. 185, Kingston HLPC).

### Source matrix (v2.3 §3) — Ulster
| # | Source | Result |
|---|---|---|
| 1 | Reddit | `site:reddit.com kingstonnewyork security camera NVR OR "security cameras" OR break-in` · WebSearch → only Kingston, Ontario results (kingstonist, globalnews). **EMPTY** for an Ulster NVR thread. Carried: r/kingstonnewyork Flock/Jenoptik threads (dvr-upgrade U4) — not used. |
| 2 | Google PAA | **EMPTY (not accessible in build env)** |
| 3 | Google PASF | **EMPTY (not accessible in build env)** |
| 4 | Answer the Public | **EMPTY (not accessible in build env)** |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)** — §10.5 says so on the page and tests 7 commonly repeated claims (basement placement, "30 days is standard", motion-only, any NVR satisfies inspectors, cloud makes placement irrelevant, historic districts ban cameras, national averages) |
| 6 | Landmarks | Rondout II Lighthouse, Coldbrook/Upper Esopus, Rondout Creek at Rosendale, iPark 87, Ellenville, SUNY New Paltz (rows UN1–UN9, carried UC*) |
| 7 | Use cases / building stock | Stacker pre-1940 share (carried UC3); iPark 87; Ellenville factory/resort history; dispensary list; Shawangunk Wine Trail |
| 8 | Bing / DuckDuckGo | **EMPTY (not accessible in build env)** |
| 9 | Local news | Hudson Valley One (Irene 2011; iPark 87 2024; dispensary guide; KPD cameras Sept 2026 carried); WAMC 2013; Times Union 2024 (carried) |
| 10 | Hyperlocal | Saugerties PD on CrimeWatch (2022 commercial alarm, Village of Saugerties); HV One 2020 Saugerties burglaries; Lower Esopus Watershed Partnership |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** — not re-tried (silo note §1) |
| — | Drive "AESS Website Photos" / CompanyCam | no NVR folder / not connected (per brief) |

### New rows (fetched this run)
| ID | Exact query · platform | URL | Finding | Used (page section) |
|---|---|---|---|---|
| UN1 | `New York OCM adult-use cannabis retail dispensary video surveillance requirements footage retention days 9 NYCRR 125` · WebSearch → WebFetch | https://www.law.cornell.edu/regulations/new-york/9-NYCRR-125.3 | (c)(2)(vi) "All recordings shall be retained for at least 60 days"; (c)(2)(viii) longer while investigation/proceeding pending; coverage "all areas, except in areas where cannabis consumers are consuming" + "any parking lot"; (c)(2)(i) safes, vaults, sales areas; (c)(2)(ii) entry/exit points, each point-of-sale; (c)(2)(iii) "clear color still photo from any camera image (live or recorded)"; remote access/login for immediate viewing by the Office; unaltered copy on request; (c)(2)(ix) media "secured … from tampering or theft"; (c)(3) failure notice to licensee's designated representative "within five (5) minutes"; (c)(4) operational in outage "minimum of eight (8) hours". | §5 para 4; §5.5; Regulated Retention table; Q 60-day; Q OCM remote access; Q investigation hold; FAQ locked room; §10.5 H3 2–4; Sources |
| UN2 | `New York cannabis cultivator processor security requirements video surveillance 9 NYCRR 123 OR 124 retention 60 days` · WebSearch → WebFetch | https://regulations.justia.com/states/new-york/title-9/subtitle-b/chapter-ii/part-113/section-113-14 | 9 NYCRR 113.14 (medical, registered organizations' manufacturing and dispensing sites): retention 60 days; 8 hours in outage; alert within 5 minutes; cameras on all areas that may contain cannabis + entries/exits. Cultivator/processor adult-use sections **not fetched** (FAQ says only that their rules sit elsewhere). | §5.5; Regulated Retention para; FAQ cultivators |
| UN3 | `Ulster County dispensaries open Kingston New Paltz Saugerties Woodstock adult-use cannabis 2025 2026 number` · WebSearch → WebFetch | https://hudsonvalleyone.com/2024/11/24/ulster-county-marijuana-dispensary-holiday-gift-guide | HV One guide (page metadata Apr 13 2025, Zac Shaw) lists 5 Ulster dispensaries: Route 28 Town of Ulster; North Chestnut St New Paltz; Plaza Rd Kingston; Route 32 Kingston; Route 213 Stone Ridge. Page names towns only, no business names. | §5 para 4; §8 Route 28 / Route 213 cards; Sources |
| UN4 | `Hurricane Irene 2011 Ulster County flooding Esopus Creek Phoenicia Rondout Creek damage` · WebSearch → WebFetch | https://loweresopus.org/2011/09/snapshot-of-rainfall-and-gauge-data-for-irene/ | "Almost all of Ulster County received more than six inches of rain"; Slide Mountain 11.53 in; Coldbrook (Upper Esopus) 23.34 ft (provisional), 1.4 ft above 1980 record, 2.76 ft above 2005; Mount Marion 25.39 ft; record flood levels Stony Clove (Phoenicia) and Rondout (Rosendale). | §5 para 2; §5.5; Places (Phoenicia); §10.5 H3 1; §13 Coldbrook & Rosendale cards; Sources |
| UN5 | same · WebFetch | https://hudsonvalleyone.com/2011/09/01/waterworld-kingston-irene-drenches-city | County EMO director Art Snyder: Esopus crested 12 ft above flood stage, Rondout 9, Wallkill 6; >80 roads impassable; Coldbrook Bridge in Shandaken swept away; $8–10M county roads/bridges. | §5 para 2; §10.5 H3 1; §13 Coldbrook card |
| UN6 | `City of Kingston NY flood zone Rondout waterfront FEMA flood map …` · WebSearch → WebFetch | https://www.wamc.org/post/flooding-task-force-issues-findings-kingston | Nov 20 2013: Kingston Flooding Task Force studied severe flooding on Rondout and Hudson waterfront from Sandy, Irene and Lee; sewage plant damaged by Sandy. | §5 para 3; Sources |
| UN7 | same · WebFetch | https://kingston-ny.gov/filestorage/8399/8469/26768/12450/31097/191023_Kingtson_Shoreline-FINAL.pdf | Rondout Riverport Shoreline Stabilization & Public Access Ph. 2 (CAD date 10/23/2019): "may experience up to 36 inches of sea level rise by 2060"; 2014 1% annual chance flood elevation 8.2 ft NAVD88; Sandy (Oct 29 2012) surge "entered the exterior basement door and flooded the basement" of the Rondout II Lighthouse. | §5 para 3; §5.5; Q sea-level rise; §13 lighthouse card; Sources |
| UN8 | `iPark 87 Kingston former IBM Tech City redevelopment tenants 2025 2026` · WebSearch → WebFetch | https://hudsonvalleyone.com/2024/05/13/ipark-87-progress-report | "200-plus-acre, million-square-foot former IBM campus"; owned by National Resources (Joe Cotter); seeking major private tenants (none named). | §5.5; Places (Town of Ulster); §7 campus card; Q iPark lease; §13 card; Sources |
| UN9 | `Ellenville village Ulster County Route 209 …` · WebSearch → WebFetch | https://en.wikipedia.org/wiki/Ellenville,_New_York | Village in Town of Wawarsing; 4,167 (2020); junction NY 52 / US 209; Rondout Valley, Shawangunk Ridge east, Catskills west; D&H Canal 1820s boom; Ellenville Regional Hospital; Nevele closed 2009; Ulster Knife Co. from 1870s → Imperial Schrade closed 2004. | Places (Ellenville); §7 mill card; Q slabs; §13 card; Sources |
| UN10 | `Shawangunk Wine Trail Ulster County wineries number Route 32 Route 208` · WebSearch → WebFetch | https://www.chronogram.com/food-drink/shawangunk-wine-trail-tells-the-regions-story-by-the-glass-23340721/ | May 2025: "13 highlights along the west side of the Hudson River"; Ulster and Orange counties. (Routes 32/208 named on page as roads only — FLAG.) | §8 wineries card; Sources |
| UN11 | `Daily Freeman 2026 burglary surveillance video Saugerties OR Ellenville OR Woodstock OR Kingston store police` · WebSearch → WebFetch | https://crimewatch.net/us/ny/ulster/saugerties-pd/161206/arrests/monarch-wiiliam-joseph-burglary-3rd-degree-and-1-additional-charge | Saugerties PD: Aug 29 2022 commercial burglar alarm at a store in the Village of Saugerties (no video mentioned). | Places (Saugerties) — "commercial alarm calls at local stores"; Sources |
| UN12 | `hudsonvalleyone.com 2026 "surveillance footage" New Paltz OR Saugerties OR Woodstock OR Ellenville arrest` · WebSearch → WebFetch | https://hudsonvalleyone.com/2020/02/14/arrest-made-in-saugerties-home-burglary-spree | Feb 3–12 2020: four residential burglaries in Village of Saugerties; Town of Ulster PD assisted; no camera mention. | Sources only |
| UN13 | `Ellenville NY news 2025 2026 … security cameras theft` · WebSearch | (Daily Voice tag pages for other towns only) | **EMPTY** for Ellenville camera/theft news. | — |

### Carried rows (not re-fetched; source file named)
| ID | From | URL | Finding | Used |
|---|---|---|---|---|
| UC3 | hikvision research U-2 | https://stacker.com/stories/new-york/counties-oldest-homes-new-york (excerpt) | 21,829 Ulster homes (25.3%) built 1939 or earlier | §5.5; Sources |
| UH1 | hikvision research U-1 | https://hudsonvalleyone.com/2026/09/02/police-defend-kingstons-surveillance-cameras-as-residents-raise-privacy-concerns/ | KPD Ubiquiti street-camera video erased every 14–21 days; cameras concentrated in Midtown and Uptown | §5 para 4; §8 Broadway card; §10.5 H3 2; Sources |
| C1/UC11 | dvr-upgrade C1 | https://kingston-ny.gov/hlpc | Districts Stockade, Rondout–West Strand, Chestnut St, Fair St; COA for material change visible from street/alley; ordinary maintenance exempt | Places; §8.5; Q historic districts; §10.5 H3 6 |
| C5 | dvr-upgrade C5 | https://www.timesunion.com/hudsonvalley/news/article/kingston-waterfront-flooding-grant-19373867.php | Mar 2024: $1.5M federal grant to raise East Strand/North Street against frequent tidal flooding | §5 para 3; Q sea-level rise; Sources |
| C9 | dvr-upgrade C9 | ulstercountyny.gov 2026-02-27 | iPark 87 East Campus hosts Ulster BOCES and Archtop Fiber | §5.5; §13 card |
| C15 | dvr-upgrade C15 | https://hudsonvalleyone.com/2016/12/29/dead-zones-more-than-a-decade-into-the-cell-phone-era-much-of-ulster-county-still-has-no-service/ | dead zones along Routes 212/28 | Places (Route 28); §10.5 H3 5; Sources |
| C20/HV-K4 | dvr-upgrade C20 | https://ecode360.com/35131702 | Ulster Ch. 185 electrical licensing; electrical work includes signalling, communication, alarm, data transmission | §5.5; §8.5; Q licensing; Sources |
| UC15 | hikvision U-2 | https://www.newpaltz.edu/about/glance.html | >7,000 students | Places (New Paltz); §13 card |
| G8/G9/G10 | silo §2.5 | nysenate PEN 250; dos.ny.gov installer licence; NYS Commercial Security Tax Credit | eavesdropping; DOS licensing; ≤50 employees up to $3,000/location | §8.5; Sources |
| S7 | silo HV part | homeadvisor.com; angi.com NY | HomeAdvisor $1,289 avg ($589–$2,040), labour $80–$200/camera; Angi NY $797–$2,222 | §10.5 H3 7; Sources |

### Prices used (Ulster §9 = 1.53×, round half-up; silo base §2.7)
Setup own NVR $337–$734; new 8-ch $995–$2,295; 16–32 ch/RAID $2,448–$8,415+; upgrade/migration/relocation/repair $291–$1,377 (same as HV hub's Ulster line). Per-line (BYOE calculator Brooklyn base ×1.53): camera line $268; concealed drywall $306; raceway $153; conduit $306; J-box $38; recorder setup only $230; old-equipment removal $77; COI $0. Service $195/hr, 3-hr min ($585), not multiplied. Worked example: $995–$2,295 + 6×$268 ($1,608) + 2×$153 ($306) = $2,909–$4,209. FLAGS: per-line items multiplied by 1.53; the BYOE calculator's own Ulster entry (install-your-own-camera-system.html AREAS.ulster) says markup .41 / note '+41%', line $267, conceal $306, hourly $275 — i.e. $1 below §9 on the camera line and an internally inconsistent markup label; page follows §9 ($268); §2.7 FLAGS still apply (equipment+labour multiplied together; $150 vs $220–$480 setup scopes).

### Unsourced house practices on the page (FLAG for Anwar)
Recorder above known flood line/one storey above basement; switch left low as the only at-risk part; dehumidifier near equipment in damp rooms; one cored sleeve per masonry wall; per-floor switches; filtered cabinets near kilns/woodshops; "leave a wet recorder off" and lab recovery advice; continuous recording of named areas for dispensaries (our cautious reading, not OCM guidance); viewer-only account + relay/VPN for OCM; lock + export + log for pending investigations; two-week retention re-check visit; printed export card; alarm-input integration; travel included in the 1.53 factor (no separate trip charge — confirm); "recording again within one to two hours of arrival" (silo convention); recorder life "every several years / five or eight years"; Field Notes = method note in Anwar's voice, not a specific job.

### Keywords (Ulster geo layer)
NVR installation Ulster County; NVR installation Ulster County NY; network video recorder Kingston NY; dispensary camera recorder Ulster; 60-day video retention dispensary New York; recorder flood Rondout; Kingston, Rondout, East Strand, Stockade, Uptown, Broadway/Midtown, Town of Ulster, Route 9W, iPark 87, New Paltz Main Street, Route 299, Saugerties, Partition Street (name only), Route 32, Woodstock, Route 212, Ellenville, Route 209, Route 52, Stone Ridge, Route 213, Phoenicia, Mount Tremper, Route 28, Rosendale, Coldbrook. All 11 alts carry "Ulster County".

### Images (11) — images/nvr-installation/nvr-installation-ulster-county-*.webp
Drive: no NVR folder; CompanyCam not connected → permanent image rule. Real-photo pool exhausted by siblings (Bronx/HV and the hikvision Ulster page already used most of the 16 real jpegs), so new non-overlapping crops of 5 real AESS job photos + 6 manufacturer recorder shots not used anywhere in the silo. All viewed; no faces (deli crop stops above shoppers; Toyota office crop stops above the seated person), no plates, house numbers or readable documents; poster/QR crop removed from the hallway shot.
| File | Source (crop l,t,r,b) | Section |
|---|---|---|
| recorder-live-view-tiles-with-time-stamp (485×300) | images/rockland-toyota-nvr-monitor.jpeg (560,230,1045,530) | Hero |
| dome-camera-below-water-stained-ceiling-tile (835×560) | images/nassau-window-depot-storage-camera.jpeg (100,0,935,560) | §5 |
| idis-eight-channel-recorder-product-photo | images/nvr-idis-dr2508p.png (trimmed) | §6 |
| white-turret-camera-in-drop-ceiling-by-light-panel (935×560) | images/rockland-toyota-office-camera.jpeg (0,0,935,560) | §7 |
| avycon-sixteen-channel-recorder-product-photo | images/nvr-avycon-avr-nsv16p.png | Regulated Retention |
| small-domes-among-light-panels-in-shop-ceiling (1230×440) | images/manhattan-deli-interior-cameras.jpeg (0,0,1230,440) | §8 |
| luminys-rack-recorder-product-photo | images/nvr-luminys-r5216pa.png | §10 |
| swann-recorder-front-and-rear-ports-product-photo | images/nvr-swann-advancedx-4k.png | §10 comparison |
| digital-watchdog-recorder-product-photo | images/nvr-digital-watchdog-cova.png | §12 |
| bullet-camera-on-ceiling-grid-beside-air-vent (935×470) | images/rockland-toyota-hallway-camera.jpeg (0,0,935,470) | §13 |
| speco-sixteen-channel-recorder-product-photo | images/nvr-speco-n16nrx.png | §14 |
DAILY-LOG note: `images: 11 = 5 real AESS job photos from other jobs (new crops of rockland-toyota, nassau-window-depot, manhattan-deli) + 6 manufacturer recorder product shots (no real NVR Installation photos yet)`. FLAG: hero/turret/hallway/storage sources are the same jpegs the Bronx and HV builders cropped differently.

### Question register — nvr-installation-ulster-county (REBUILT 2026-10-18)
§9 H2 (question form): Ulster Recorder Wet, Full or Silent?
§9 H3:
1. Does the sea-level rise Kingston is planning for change where a Rondout business should put its recorder today?
2. Can footage be recovered from a recorder whose drive sat in floodwater?
3. Does a damp fieldstone or bluestone cellar hurt a recorder even if it never floods?
4. Does the state's 60-day rule for dispensaries mean continuous video or just motion clips?
5. What does giving the Office of Cannabis Management "remote access" to our recorder look like in practice?
6. The cannabis rules say keep footage longer if an investigation is pending — how do we hold one incident past the 60 days?
7. We lease a suite on a large campus like iPark 87 — can we run our own recorder, or must we use the landlord's?
8. Coring through an old mill's concrete floors is slow and costly — how few holes can a three-storey camera system get by with?
9. Our pottery or woodworking studio is dusty — where should the recorder go?
10. Can the recorder black out part of a camera's view, such as a neighbour's window across a narrow Uptown street?
11. Does Ulster County's electrical licensing law reach the low-voltage camera cable?
12. Does putting a recorder and new cable into a building in one of Kingston's historic districts need the preservation commission's approval?
13. Can our existing alarm panel tell the recorder when someone opens the door after hours?
§17 FAQ (= FAQPage, 8):
1. Can you audit how many days of video our current recorder actually keeps?
2. Why are Ulster County prices 1.53 times the Brooklyn base?
3. Our building still has coax cameras from the 1990s — can a network recorder use them?
4. We are switching internet providers — what has to be redone on the recorder?
5. Can the recorder be fixed to the wall instead of sitting on a shelf?
6. Do you install recorders for cannabis cultivators and processors, not just dispensaries?
7. Does a dispensary's recorder have to be in a locked room?
8. What should we write down about the recorder for our insurance agent?
§10.5 claim H3s (not questions): basement is cool and out of the way; 30 days is the industry standard; motion recording is all a business needs; any NVR can give an inspector/detective what they need; cloud backup makes recorder location irrelevant; can't add cameras in a historic district; national averages tell you the Ulster cost.
De-dup notes: checked against Bronx §4.2, HV B.3 and the parallel Westchester rebuild (read 09:35Z). Changed because of overlap: "how high should the recorder sit (Rondout flood)" → sea-level-rise planning (Westchester owns "Ida … where should a Sound Shore shop keep its recorder now?"); FAQ "how far into the Catskills do you travel" → retention audit (Westchester owns "how far into northern Westchester … price change?"); "how do cameras on three storeys reach one recorder" → minimising slab penetrations (Westchester owns per-floor vs central recorder). Dispensary topic overlaps Westchester in subject (both cite 9 NYCRR 125.3), but intents differ: Westchester asks "what does the rule ask of the recorder" / "eight hours" / "security-plan details"; Ulster asks continuous-vs-motion, OCM remote access, investigation hold, locked room, cultivators. Not repeated: HV battery/generator/caretaker/off-site/move-recorder intents; Bronx fault alerts, time sync, detective export, role accounts.
Similarity (masked, block-level SequenceMatcher, h3/p/li/td/figcaption ≥8 words): max paragraph 0.643 (vs Bronx per-line price label; vs HV DVR-upgrade service card); page 5-shingle Jaccard ≤0.007, page SequenceMatcher ≤0.086 vs every nvr-installation-* page, hikvision-…-ulster-county-ny and dvr-upgrade-ulster. Only the blueprint-fixed H2 "What AI Gets Wrong About NVR Installation in …" matches ≥0.65.
