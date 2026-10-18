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


<!-- Merged from nvr-installation-long-island builder (batch 2026-10-18 09:12Z) -->
# NVR Installation — Long Island hub research (part file, for merge into research/nvr-installation.md)

Page: `nvr-installation-long-island` (REBUILD in place, 2026-10-18; was crawled-not-indexed as a near-duplicate template). Regional hub: (800) 486-0943 only; GBP Brooklyn (1282 Troy Ave, Brooklyn NY 11203, `#brooklyn`, LocalBusiness block as on lorex-camera-installation-long-island.html); up-link Home (/); down-links to /nvr-installation-nassau-county and /nvr-installation-suffolk-county; cross-links to NYC hub + 5 boroughs and HV hub + 6 counties; WhatsApp only as wa.me/17186790359.

Built in parallel with the Putnam County and Staten Island NVR rebuilds (their questions were read at ~09:36Z and this page was adjusted afterwards — see §B.3). Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. Shell curl blocked; tools used: Firecrawl search/scrape (`mcp__Firecrawl__*`). "carried" = sourced by an earlier run in another research file in this repo (file + row named); not re-fetched today.

---

## Long Island

**Thesis (distinct from Bronx = custody of evidence in apartment buildings/stores; HV = self-sufficient recorder in empty rural houses, outbuildings, Starlink; Putnam = lakes/lightning/Ch. 145; Staten Island = Sandy flood houses, two-families, shoreline):** on Long Island the recorder's problem is *ground level and the house itself*. A large share of houses have no cellar (Levittown's 17,447 slab houses with radiant pipes in the slab; Nassau median year built 1955), South Shore houses were raised after Sandy so the old ground floor is now a flood-vented enclosure, East End houses sit closed half the year (East Hampton 47% seasonal), and businesses are tenants in strip-centre units where the landlord controls roof/ceiling/lot cameras. Layered on that: one utility with six-figure outages (PSEG LI: Isaias 271,352; Sept 2026 storm >124,000 outages in 72 h) → battery + surge protection incl. restoration surges; provider gateways (Optimum/Fios) that get swapped and break remote access, Optimum fibre terminals landing in garages; two counties with two licensing offices (Nassau OCA HIC licence + fingerprinting; Suffolk DLLCA Ch. 563 HIC/electricians) plus the NYS DOS 6-D licence; and police registries (SCPD camera registry + opt-in emergency remote access; Garden City village registry, "does NOT provide us access").

### Mandatory sources (§3) — status for this page
| # | Source | Result |
|---|---|---|
| 1 | Reddit | r/longisland excerpts via Firecrawl search (LI-R1–R4); threads not scraped in full |
| 2 | Google PAA | EMPTY (not accessible in build env) |
| 3 | Google PASF | EMPTY (not accessible in build env) |
| 4 | Answer the Public | EMPTY (not accessible in build env) |
| 5 | Google AI Overview | EMPTY (not accessible in build env) — §10.5 says so on the page and tests seven commonly repeated claims instead |
| 6 | Landmarks | LI-L1–L6 |
| 7 | Building stock / use cases | LI-H1–H6 |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env) |
| 9 | Local news | Nassau County PD news flashes (Jan + Jul 2026), PSEG LI newsroom (Sept 28, 2026), NY Post (Oct 2026, carried), RiverheadLOCAL/ABC7 (carried) |
| 10 | Hyperlocal | Garden City PD village page; Patch Southampton; Newsday Sandy database (carried); LI Herald: EMPTY (query `Nassau County burglaries homes 2026 surveillance video police Newsday OR Patch OR "Herald" crew wifi jammer` returned only irrelevant PDFs) |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env) — silo precedent, not re-tried |
| — | Google Drive "AESS Website Photos" | no NVR folder (only Cat6 Repair, Sonos, Fiber Optic, Soundbar, Smart Lock) — per brief |
| — | CompanyCam | not connected — per brief |

### Building stock / housing (LI-H)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-H1 | `Levittown houses built 1947 1951 slab no basement number of homes` · Firecrawl search (excerpts) | https://www.jlconline.com/how-to/foundations/levittowns-cellarless-homes_o ; https://kerimurrayarchitecture.com/levittown-ny/ (also carried research/cat6-repair.md L145 directQuote) | JLC "Levittown's 'Cellarless' Homes": by 1951, 17,447 homes. Keri Murray: "ranch homes built on concrete slabs, included an expandable attic but no garage, and were heated with hot-water radiant heating pipes"; 17,447 homes 1947–1951. | §5 para 1, §5 facts list, §7 card 1, §9 Q1–Q2, §10.5 H3 1, §13 Levittown card, Sources |
| LI-H2 | carried — research/cat6-repair.md L1035–1036 | https://www.point2homes.com/US/Neighborhood/NY/Nassau-County-Demographics.html ; https://www.census.gov/quickfacts/nassaucountynewyork | ACS via Point2: Nassau median construction year 1955; 76.1% 1-unit detached. QuickFacts: 480,591 housing units, 81.9% owner-occupied. | §5 para 1 ("about three in four detached"), Sources |
| LI-H3 | carried — research/dahua-camera-installation.md L65 (ny.gov) | https://www.ny.gov/counties/nassau ; https://www.ny.gov/counties/suffolk | Nassau: two cities, three towns, 64 incorporated villages, 453 sq mi. Suffolk: 10 towns, 2,373 sq mi. | Two Counties section intro, Sources |
| LI-H4 | `East Hampton OR Southampton town share of housing units seasonal recreational occasional use census percent` · Firecrawl search (excerpt) | https://www.ehamptonny.gov/DocumentCenter/View/28279/Route-114-Affordable-Housing-Market-Study-and-Update | East Hampton Town market assessment: "total of 44,227 housing units, 17,993 (41%) are owner-occupied (primary residence) while 20,952 (47%) are used for seasonal, recreational…" (study date not shown in excerpt — page says "a town housing market study"). | §5 para 4, §5 facts list, §13 East Hampton card, Sources |
| LI-H5 | same search (excerpt) | https://patch.com/new-york/southampton/census-says-there-are-fewer-people-in-southampton-vil3b29943a21 | Patch: Southampton Town 2010, of 41,759 housing units, Census designated 49% vacant. | §5 facts list ("counted as vacant"), Sources |
| LI-H6 | carried — research/apartment-building-security-camera-installation.md L785–786 | https://www.nysenate.gov/newsroom/in-the-news/2021/todd-kaminsky/long-beach-residents-ny-officials-call-stricter-inspections ; https://www.habitatmag.com/Publication-Content/Building-Operations/2012/2012-November/Hurricane-Sandy-Long-Beach-Co-op-Condo-Cleanup | "Long Beach is the only area on Long Island with oceanfront high-rises"; Habitat Nov 2012: 840 Shore Road ground and first floor flooded; Ocean Club condo lost first floor, pool, heating systems, gym, lobbies. | §13 Long Beach card, Sources |

### Floods / Sandy (LI-F)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-F1 | carried — research/apartment-building-security-camera-installation.md L275 | https://www.suffolkcountyny.gov/mend/index.html | Sandy: "16' Storm Surge on Fire Island; Over 31,000 homes flooded" (Suffolk). | §5 para 2, §10.5 H3 1, Sources |
| LI-F2 | carried — research/cat6-repair.md L1040 | https://projects.newsday.com/long-island/sandy-by-the-numbers/ | "nearly 3,500" LI homes elevated or slated, mostly in flood zones where raising is required for flood insurance / rebuilding. | §5 para 2, §5 facts list, Sources |
| LI-F3 | carried — research/cat6-repair.md L152 | https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20240823 | Aug 18–19 2024: "first-ever flash flood emergency for Suffolk County"; "1-in-1,000-year rain event". | §5 para 2, Sources |
| LI-F4 | `Superstorm Sandy Long Island homes elevated flood zone mechanical equipment above base flood elevation Nassau` · Firecrawl search (excerpt) | https://dec.ny.gov/sites/default/files/2024-01/NYS%20Floodplain%20Management%20Quick%20Guide%202023.pdf | NYS DEC quick guide: "Require new and substantially improved buildings, manufactured homes, and additions to be elevated to or above the Base Flood Elevation (BFE) plus 2 feet". | §5 facts list, §9 raised-house H3, §10.5 H3 7, Sources |
| LI-F5 | same search (excerpt) | https://www.slcinsure.com/wp-content/uploads/2018/03/FEMA.pdf | FEMA Hurricane Sandy Recovery Advisory 7 (mirror on an insurer site): repairs entail "making sure any mechanical, electrical, and plumbing equipment are elevated…". FLAG: mirror, not fema.gov. | §9 raised-house H3, §10.5 H3 7, Sources |

### Power (LI-P)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-P1 | `PSEG Long Island outage customers 2025 OR 2026 storm restored Nassau Suffolk` · Firecrawl search → scrape | https://www.psegliny.com/en/Newsroom/2025/092826-StormUpdate0800 | "(UNIONDALE, N.Y. – Sept. 28, 2026)": >95% restored; 6,108 of 1.2 million customers out; "Over the course of 72 hours, the storm caused more than 124,000 outages"; majority in Suffolk; "More than 1,150 trees and nearly 700 large branches fell"; "More than 1,350 local and off-Island field workers" restoring "in 16-hour shifts"; "Additional outages continued to come in overnight"; ETRs "provided and refined" as damage is assessed. (URL path says /2025/ but the release is dated 2026.) | §5 para 3, §5 facts list, repair section para 2 (staged restoration, added after size fix), §10.5 H3 2, Sources |
| LI-P2 | carried — research/network-installation.md P1 | https://riverheadlocal.com/2020/08/06/isaias-update-outages-restoration-progress-and-lingering-road-closures | Isaias: PSEG-LI map "271,352 affected customers as of 6:32 a.m." | §5 para 3, §5 facts, §10.5 H3 2, Sources |
| LI-P3 | carried — research/network-installation.md P2 | https://abc7ny.com/weather/widespread-damage-and-power-outages-across-long-island/6353608/ | "almost half of PSEG's 1.1 million customers in the dark at the peak" (Aug 2020). | §5 para 3, Sources |
| LI-P4 | same search (excerpt) | https://poweroutage.us/area/utility/32 | Tracks 1,159,093 PSEG LI customers (Suffolk 640,928; Nassau 480,048). | Not used (aggregator) |

### Internet (LI-I)
| # | Source | URL | Finding | Used |
|---|---|---|---|---|
| LI-I1 | carried — research/network-installation.md C1 | https://alticeusa.com/node/3151 | Oct 2024: Optimum fibre "nearly 900,000 on Long Island". | §5 facts list, Sources |
| LI-I2 | carried — C2 | https://www.verizon.com/home/internet/near-me/long-island-new-york/ | Verizon Home Internet (Fios or 5G Home) listed for "much of Long Island"; per-address checker. | §5 facts list, Sources |
| LI-I3 | carried — C3 | https://longislandpress.com/2021/11/21/oped-broadband-access-is-a-long-island-problem | Comptroller (Sept 2021) via op-ed: ~51,700 Suffolk residents missing last-mile wired broadband; 61,231 Long Islanders without wired high-speed. | §5 facts list ("about 51,700 Suffolk residents"), Sources |
| LI-I4 | carried — research/cat6-repair.md L721 | https://www.optimum.net/pages/fiber.html | Optimum fibre installation: "Ethernet CAT 6 or higher"; "We'll work with you to find the best location for your new equipment". | §9 Optimum fibre-box H3, Sources |

### Police / news (LI-N)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-N1 | `Suffolk County Police camera registration program residents businesses register home security cameras` · Firecrawl search → scrape | https://scpdshield.org/Initiatives | SCPD SHIELD: Camera Registry Program "allows citizens and business owners to register the locations of their video surveillance systems"; Department may "request program participants to check their video surveillance system for a specific date and time"; video retrieval "at the convenience of the camera owner". Emergency Remote Camera Access: remote access to "previously authorized I.P. based video monitoring systems" only "in the event of a true emergency, such as an active shooter attack, hostage situation…"; opt in/out any time. Suffolk Crime Analysis Center at SCPD HQ in Yaphank, video wall of countywide surveillance cameras. | §5 para 4, §5 facts list, Two Counties police H3, §10.5 H3 5, Sources |
| LI-N2 | `Nassau County Police Department camera registry program private security cameras register` · Firecrawl search → scrape | https://gardencitypolice.net/private-camera-reg | Garden City PD (village, Nassau): voluntary Private Camera Registration Program; "strictly voluntary and does NOT provide us access to security camera systems that are privately owned by participants"; detectives "may ask to inspect your surveillance video recorded during a finite period"; "Currently, officers go door to door talking with residents and businesses looking for video evidence"; "We will continue to canvass"; registry gives "detectives and patrol officers an instant list of locations". | Two Counties police H3 para 2 (canvass sentence), §5 para 4, §5 facts, Two Counties police H3, §10.5 H3 5, Sources |
| LI-N3 | `Nassau County police home burglaries surveillance footage 2026 Patch` · Firecrawl search (tbs past year) → scrape | https://www.pdcn.org/CivicAlerts.aspx?AID=15186 | NCPD news flash July 24, 2026: Grand Larceny Sat July 11, 2026, West Hempstead; "a female health aide, 60, was observed on a home video surveillance removing a black locked box containing US currency"; victim 95. (Defendant named on source; NOT named on page.) | Two Counties police H3 para 2, Sources |
| LI-N4 | same → scrape | https://www.pdcn.org/CivicAlerts.aspx?AID=14776 | NCPD Jan 16, 2026: burglary Wed Jan 14, 2026, 10:30 p.m.: subject entered "the delivery station in the rear of the Nordstrom Rack located at 1040 Old Country Road through an unlocked door and removed merchandise"; video released. (Store not named on page; suspect description not used.) | §8 Old Country Road card, §13 Old Country Road card, Sources |
| LI-N5 | `Suffolk County Police camera registration…` (same search, excerpt) | https://suffolkpd.org/Precincts-and-Specialized-Units/Specialized-Units/Alarm-Management-Program | Alarm Management Program: registration fee $50 residences, $100 commercial. | §8.5 bullet 7, Sources |
| LI-N6 | carried — research/apartment-building-security-camera-installation.md L270 | https://nypost.com/2026/10/04/us-news/suffolk-county-more-than-doubles-number-of-big-brother-flock-cameras-in-past-year/ | NY Post Oct 4, 2026: county Flock plate cameras 25 → about 60. | Two Counties police H3 para 1, Sources |

### Licensing (LI-K)
| # | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LI-K1 | `Nassau County Office of Consumer Affairs home improvement license security alarm installation contractor` · Firecrawl search (excerpts) | https://www.nassaucountyny.gov/1547/Consumer-Affairs ; https://www.nassaucountyny.gov/1563/Licensing-Registrations | OCA licenses home improvement contractors (HOME IMPROVEMENT 21-11); carried (cat6-repair L138): "All Licensed Home Improvement Contractors must be fingerprinted". Page body JS-only → detail of whether low-voltage work needs a HIC licence: EMPTY. | §8.5 bullet 2, §9 licence H3, Sources |
| LI-K2 | `Suffolk County Department of Labor Licensing and Consumer Affairs home improvement license required who needs` · Firecrawl search (excerpts) | https://www.suffolkcountyny.gov/Departments/Consumer-Affairs/Type-of-License ; https://ecode360.com/14947425 ; https://ca.suffolkcountyny.gov/dcasearch | Consumer Affairs licenses >15,000 vendors, >50% of licences issued/renewed each year are home improvement (now on page, §8.5 bullet 2); Ch. 563 Art. II home improvement contractors ("a person who engages in home improvement contracting upon residential property"); online licence/complaint search. Carried (apartment research L249): licence-type list has no low-voltage/alarm/camera licence. | §8.5 bullet 2, §9 licence H3, Sources |
| LI-K3 | carried — research/cat6-repair.md L137 / apartment research L248 | https://ecode360.com/14948079 | Ch. 563 Art. XI electricians and plumbers (licence required for electrical work for hire in the county). | §8.5 bullet 3, §9 licence H3, Sources |
| LI-K4 | carried — research/cat6-repair.md L1048 | https://ehhaineselectric.com/resource/do-i-need-a-permit-for-electrical-work-in-nassau-county/ | Contractor guide: "Low-voltage systems (security, data, A/V) may not require a permit, but running new wiring through walls or attics often does."; "Electrical permits must be pulled by a licensed master electrician registered in the specific township or village." | §8.5 bullet 3, Sources (labelled "contractor guide") |
| LI-K5 | silo G9 (research/nvr-installation.md) | https://dos.ny.gov/get-security-or-fire-alarm-installer-license | NYS DOS Article 6-D; 19 NYCRR §195.2(b)(1) covers CCTV/video surveillance. | §8.5 bullet 1, §9 licence H3, Sources |

### Places / landmarks (LI-L)
| # | Source | URL | Finding | Used |
|---|---|---|---|---|
| LI-L1 | LI-H1 | — | Levittown | §13 card |
| LI-L2 | LI-H6 | — | Long Beach / Shore Road | §13 card |
| LI-L3 | LI-N4 | — | Old Country Road, East Garden City | §8 card, §13 card |
| LI-L4 | carried — research/network-installation.md B2 / cat6-repair L147 | https://cmmllp.com/hauppauge-industrial-park-update-2017-long-islands-oasis-productivity-innovation/ | ~1,350 businesses, ~55,000 workers, ~11 sq mi; about two-thirds under Town of Smithtown; renamed Long Island Innovation Park at Hauppauge (2019). | §8 card, §13 card, Sources |
| LI-L5 | carried — research/apartment-building-security-camera-installation.md L253; cat6-repair L149 | https://www.governor.ny.gov/news/governor-hochul-unveils-next-phase-12-billion-transit-oriented-hub-station-yards-creating-more | Oct 22, 2024: Station Yards (Ronkonkoma Hub), 53 acres; site between MacArthur Airport and the Ronkonkoma station (govmarketnews excerpt carried). | §13 card, Sources |
| LI-L6 | LI-H4 | — | East Hampton | §13 card |
Corridor/hamlet names (Hempstead Turnpike, Jericho Turnpike, Sunrise Highway, Route 110, Route 58, Route 27, LIE, the hamlets in the "we also serve" list, Gold Coast towns) are used as place names only — FLAG: no per-corridor source, no business claims attached.

### Reddit (LI-R) — excerpts only
| # | Exact query · platform | URL | Finding (excerpt) | Used |
|---|---|---|---|---|
| LI-R1 | `site:reddit.com r/longisland NVR OR "security cameras" OR "camera system" house recommendations installer` · Firecrawl search | https://www.reddit.com/r/longisland/comments/1kc5ygw/home_security_cameras/ | commenter: "I install security cameras and to be totally honest. Simple Ring camera doorbell and Wyze cameras are as good as you can find." | §10.5 H3 3 (claim tested, not quoted verbatim), Sources |
| LI-R2 | same | https://www.reddit.com/r/longisland/comments/nbmls1/security_camera_installer/ | "Can anyone recommend a provider/installer for home PoE cameras and an NVR…" | Sources |
| LI-R3 | same | https://www.reddit.com/r/longisland/comments/1cn1pcu/security_system_suggestions/ | "considering Reolink as a cheaper option to Hikivision" | Not used |
| LI-R4 | carried — research/apartment-building-security-camera-installation.md L798 | https://www.reddit.com/r/longisland/comments/1h8ygon/what_cameraalarm_system_do_you_use_andor/ | "the gangs used the jammers. The cameras didn't record anything" | §10.5 H3 3 (4-word quote), Sources |

### Silo/equipment rows reused (no new fetch)
Silo T1/S2 (WD Purple 180 TB/yr, 0–65°C), S4 (Lorex 328 ft), G1–G2 (FCC DA 26-635 / FR July 6 2026, effective July 16 2026), G8 (Penal Law 250), HV-G6 (Civil Rights Law §52-a), G10 (Commercial Security Tax Credit), S7 (HomeAdvisor $589–$2,040; Angi NY $797–$2,222).

---

## B. Question register — nvr-installation-long-island (rebuilt 2026-10-18)

**Repair H2 ("?" heading):** Cameras Back but the Recorder Still Blank After an Outage?

**§9 Q&A H3 (11):**
1. Our Levittown-era house sits on a slab with no basement — where does a recorder go when there is no cellar?
2. The floor slab has radiant heating pipes in it — how does camera cable reach the recorder without drilling the floor?
3. Can the surge when PSEG restores power after a storm damage the recorder, and what protects it?
4. A technician swapped our Optimum or Fios router and the recorder vanished from the app — why, and how is it prevented?
5. Optimum's fibre upgrade put the new box in the garage — does the recorder have to move out there with it?
6. When an East End house is winterized for the off-season, should the recorder be left running?
7. We lease a unit in a strip centre on Hempstead Turnpike — whose permission do we need to run camera cable across the roof or above the neighbours' ceilings?
8. When our strip-centre lease ends, does the recorder system belong to us or to the landlord?
9. The house we are buying comes with cameras and a recorder — what should we check before closing?
10. Our recorder was installed by a company that no longer exists, and it is locked to their cloud account — can we take it over?
11. What licence should a Long Island homeowner ask to see before someone installs a recorder — county, state, or both?
(Non-question H3s in §9: "Raised houses: what may stay in the flood-vented space below"; "Privacy masks on tight suburban lots".)

**§17 FAQ (9, = FAQPage):**
1. Can one crew handle our house in Nassau and our shop in Suffolk on the same account?
2. Does the recorder need its own electrical circuit?
3. We bought a recorder kit at a big-box store — what makes it worth installing rather than returning?
4. When is the best time of year to schedule a recorder installation at an East End house?
5. Which photos let you price the job without a site visit?
6. Can the crew work while we are at our jobs in the city, if we leave a key or a lockbox code?
7. We own a unit in a Nassau garden co-op — what does the board have to approve before a recorder goes in?
8. How many years should a recorder last before it needs replacing?
9. Can a renter have a recorder installed in a Long Island house or apartment?

**§10.5 claim H3s (quoted claims):** "Put the recorder in the basement, out of the way"; "A surge-protector power strip is all a recorder needs in a storm"; "Plug-in Wi-Fi cameras are as good as a wired system"; "The internet company's router takes care of remote viewing"; "Register your cameras with the police and they can log in to watch"; "Island prices are the same as anywhere else"; "Building rules don't care where the electronics go".

### B.3 De-dup notes (checked by meaning)
- Old 12-question template register; Bronx (29) and HV (25) registers in research/nvr-installation.md — none repeated. Cost lives in §14/§15 only (no cost question).
- **Changed after reading the parallel Staten Island page (09:34Z) and Putnam page (09:36Z):** dropped "Should we move the recorder or unplug anything when a hurricane is forecast?" (SI: unplug when hurricane forecast); turned "can camera equipment stay in the flood-vented space under our raised house?" into a non-question H3 (SI: lifted-house floor / cameras in flood space wiring); dropped "landlord already has cameras on the lot — can our recorder record them?" (SI: Hylan Blvd landlord cameras on one recorder); dropped "Route 110 office with outside IT company — who looks after the recorder?" (SI: Teleport IT department sign-off); turned the neighbour-yard privacy-mask Q into a non-question H3 (SI shared driveway / Putnam neighbour across the cove); dropped "single-provider address — cellular backup for alerts?" (Putnam: power and internet both down at empty lake house — how do we find out); replaced FAQs on recorder noise (SI), working with the alarm company (SI) and North Fork/Montauk surcharge (SI Verrazzano surcharge); reworded "what to photograph before the visit" → "which photos let you price without a visit" (Putnam: getting the house ready for install day).
- Borderline, kept (FLAG): Q4 router swap vs HV "port forwarding stopped after moving to Starlink" (different cause: lost gateway config vs CGNAT); Q9 buyer-side check vs HV FAQ seller-side "what happens to the recorder when we sell the house"; FAQ 8 lifespan vs HV "maker stops releasing updates" (lifespan covers drives/fan/battery first).
- Masked paragraph similarity (difflib, blocks ≥8 words, geo masked with check_page.mask): after rewrites, no body paragraph ≥0.65 vs any of the 15 siblings; remaining ≥0.65 matches are blueprint-fixed H2 patterns ("What AI Gets Wrong About NVR Installation on…", "NVR Installation Cost on…", "…Questions Answered") and the silo cross-link list labels ("NYC NVR installation (hub)" etc.).

Intents this page owns for the silo: recorder placement in cellarless/slab houses; no-drill routing over radiant slabs; raised-house enclosure (statement); utility restoration surge; ISP gateway swap breaking remote access; fibre terminal location vs recorder location; winterized seasonal house; strip-centre landlord route permission; lease-end ownership of the system; buyer inheriting a recorder; recorder locked to a defunct installer's cloud; county vs state licence to ask for; FAQ: two-county single account, dedicated circuit, big-box kit keep/return, East End scheduling season, photo-based pricing, working while owners are away, garden co-op board approval, recorder lifespan, renter installs.

---

## Pricing used (§9 multipliers — no invented prices)
Silo base (Brooklyn 1.00×) = figures published identically on all 16 pre-rebuild NVR pages (research/nvr-installation.md §2.7): setup of own recorder $220–$480; new 8-channel system (recorder + PoE + drive; cameras/cabling separate) $650–$1,500; 16–32 ch/RAID $1,600–$5,500+; upgrade/migration/repair $190–$900. Blueprint v2.3 §9 verified: **Nassau 1.15, Suffolk 1.20**. Each end × factor, Decimal ROUND_HALF_UP:
| County | × | Setup | New 8-ch | 16–32 ch/RAID | Upgrade/migration/repair |
|---|---|---|---|---|---|
| Nassau | 1.15 | $253–$552 | $748–$1,725 (747.5→748) | $1,840–$6,325+ | $219–$1,035 (218.5→219) |
| Suffolk | 1.20 | $264–$576 | $780–$1,800 | $1,920–$6,600+ | $228–$1,080 |
Service $195/hr, 3-hr minimum ($585) verbatim, not multiplied. Service schema OfferCatalog: setup / new 8-ch / upgrade lines per county.
FLAG: same as HV — base ranges bundle equipment with labour; v2.3 says calculator multipliers apply to labour only; no split exists, so whole ranges multiplied. The old LI page showed the Brooklyn figures unmultiplied — replaced.

## Images (11) — Drive: no NVR folder; CompanyCam not connected → permanent image rule
Converted with Pillow 12.3 (WebP q80, ≤1600 px; PNG alpha flattened on white; product shots trimmed of white margins). Each source opened and viewed (contact sheets). No faces, house numbers, plates or readable documents; banner text/licence frames cropped out of the office photo. Captions say "Manufacturer product photo, not an installed unit" or "Example photo from an AESS job/installation, not a specific Long Island property".
| Output (images/nvr-installation/nvr-installation-long-island-…) | Source | Section |
|---|---|---|
| swann-recorder-front-and-rear-poe-ports-product-photo.webp (454×346) | images/nvr-swann-advancedx-4k.png (product) | Hero / og:image |
| dome-camera-under-stained-storeroom-ceiling.webp (420×360) | images/nassau-window-depot-storage-camera.jpeg crop (300,280,720,640) — tighter than the apartment-silo crop (100,100,935,600) | §5 |
| dome-camera-at-fascia-corner-against-sky.webp (517×235) | images/lorex-camera-installation/lorex-camera-installation-long-island-two-cameras-on-yellow-fascia-corner-against-sky.webp, right-hand crop (400,0,917,235) | Two Counties |
| digital-watchdog-recorder-product-photo.webp (482×100) | images/nvr-digital-watchdog-cova.png (product) | §6 |
| dome-camera-and-wall-sensor-high-on-office-wall.webp (380×550) | images/nassau-window-depot-office-camera.jpeg crop (420,250,800,800) — banner, framed licences and flag excluded | §7 |
| ceiling-camera-near-lit-exit-sign-in-office.webp (845×620) | images/floodlight-camera-installation/floodlight-camera-installation-orange-county-ceiling-camera-and-device-beside-red-lit-exit-sign.webp | §8 |
| honeywell-recorder-with-front-usb-ports-product-photo.webp (500×140) | images/nvr-honeywell-35-series.png (product) | §9 |
| black-ball-camera-at-ceiling-edge.webp (535×400) | images/floodlight-camera-installation/floodlight-camera-installation-staten-island-black-ball-camera-at-ceiling-edge-beside-light-panel.webp | §9 end |
| ens-large-recorder-with-side-vents-product-photo.webp (420×183) | images/nvr-ens-titanium.png (product) | §10 |
| avycon-slim-recorder-product-photo.webp (500×151) | images/nvr-avycon-avr-nsv16p.png (product) | §12 |
| small-white-domes-across-drop-ceiling.webp (720×310) | images/lorex-camera-installation/lorex-camera-installation-orange-county-small-white-domes-spread-across-drop-ceiling.webp | §13 |
Rejected after viewing: nassau-window-depot-monitor.jpeg (top-left tile shows a door number "1096"; top-right and bottom-right tiles are the sources already used by the Bronx NVR page and apartment LI page; bottom-left shows people); cable-bundle photos (same scene family as Bronx's ceiling-cable image); lorex orange-county dim storeroom tile (same family as Bronx's storeroom tile).
DAILY-LOG note: `images: 11 reused — 5 manufacturer product photos (images/nvr-*.png) + 6 real AESS photos from images/nassau-window-depot-*.jpeg, images/floodlight-camera-installation/, images/lorex-camera-installation/ (no real NVR Installation photos yet)`.

## Keywords (LI geo layer)
NVR installation Long Island; NVR installation Nassau / Suffolk; network video recorder installation Long Island; recorder for slab house / no basement; raised house camera recorder; PSEG outage recorder battery backup; Optimum / Fios router swap recorder app; East End seasonal house recorder; strip centre recorder Hempstead Turnpike / Jericho Turnpike / Old Country Road / Route 110; Hauppauge; Ronkonkoma; Levittown; Long Beach; East Hampton; Suffolk police camera registry. Alt/title on all 11 images carry "Long Island NVR installation".

## FLAGS for Anwar (LI hub)
1. Pricing: whole bundled ranges multiplied (no labour/equipment split) — as HV. North Fork/Montauk "same Suffolk factor" and East End "planned windows" follow the network-cable-repair-suffolk-county changelog convention (research/cat6-repair.md L164), not a stated price policy for NVR — confirm.
2. Unsourced house practices (installer knowledge): closet-on-interior-wall placement in slab houses; no slab drilling; attic routing; conduit under raised houses; restoration-surge mechanism and layered surge protection; recorder auto-restart; maker relay/VPN instead of port forwarding; reserved address; cellular backup mentions in service/equipment cards; winterized-house guidance; landlord one-page route plan; lease-end split (typical lease terms, not legal advice); buyer checklist; defunct-installer recovery; privacy masks; co-op board approvals; recorder lifespan; noise of recorders; "writing video again within one to two hours of arrival" and two-hour windows 8 AM–8 PM any day (silo convention); "insurance certificates on request".
3. "Nassau's office handles verification by phone and its website" — page wording is generic; no Nassau online licence-search URL was confirmed (page body JS-only).
4. FEMA Recovery Advisory 7 cited via an insurer-hosted PDF mirror (slcinsure.com), not fema.gov.
5. PSEG Sept 28, 2026 release sits under a /2025/ URL path but is dated 2026 in the body.
6. Field Notes are Anwar-voice general method, not a specific job story — confirm or replace with a real island anecdote.
7. Borderline intents vs HV listed in B.3 (router swap vs Starlink; buyer vs seller; lifespan vs end of updates).
8. Product photo brand/model: captions name only the brand (Swann, Digital Watchdog, Honeywell, ENS, AVYCON); models from filenames not verified.
9. nassau-window-depot-* photos appear to be from a real AESS job in Nassau; captions deliberately do not claim a Long Island job (brief rule). Anwar may want to caption them as Nassau work if he confirms.


<!-- Merged from nvr-installation-putnam-county builder (batch 2026-10-18 09:12Z) -->
## Putnam County

Build 2026-10-18 (REBUILD in place of `nvr-installation-putnam-county`, was crawled-not-indexed as a near-duplicate template). Queue line: `REBUILD | nvr-installation-putnam-county | NVR Installation | Putnam | up /nvr-installation-hudson-valley | (845) 640-3835 | GBP Bronx`. Up-link `/nvr-installation-hudson-valley`. GBP Bronx (460 E Fordham Rd, Bronx NY 10458, `#bronx`). Direct line (845) 640-3835 in body, CTAs, sticky bar, form error text and schema; (800) 486-0943 only in the shared mega-nav header. WhatsApp only as wa.me/17186790359 (+ contact-block text). Silo research §1–§3 and the HV hub section reused, not redone. Format per v2.3 §12.4: exact query · platform · URL · finding · page + section used. Tools: Firecrawl search/scrape (`mcp__Firecrawl__*`). Shell curl blocked. "Carried" = fetched by an earlier run in another research file (file + row named), not re-fetched.

**Thesis (distinct from the HV hub, which covers Isaias/Starlink/328 ft/barns generally, and from the Bronx page's custody-in-someone-else's-building angle):** Putnam's own officials made the local-storage argument in public — in Sept 2026 the Sheriff told the legislature the county kept its 21 plate-reader sites off commercial cloud networks, data on a government server under regional law-enforcement control (while neighbouring Dutchess switched its 64 Flock readers off). An NVR is that choice for one house or shop. In Putnam the recorder then has to survive town-wide NYSEG/Central Hudson outages (Isaias counts by town: Carmel 12,717, Kent 5,815 …), lightning (75,093 pulses in 2020), flash floods (Putnam Valley emergency July 29, 2026), houses empty midweek (1,757 seasonal units), lake-colony lots, ledge rock, private roads and lake associations, uneven broadband, Chapter 145 low-voltage licensing and Cold Spring's review board — and it has to capture the travelling burglary and retail-theft crews the Sheriff's data describes (27 burglary-crew vehicles, 22 retail-theft-ring vehicles, Jan–mid-Aug 2026) and the pre-dawn Mahopac car break-ins (Aug 5, 2026).

### Mandatory sources (§3) — Putnam status
| # | Source | Result |
|---|---|---|
| 1 | Reddit | EMPTY for Putnam NVR threads (also EMPTY in the floodlight/dvr-upgrade Putnam runs; not re-tried beyond the searches below). |
| 2–5 | PAA / PASF / Answer the Public / AI Overview | EMPTY (not accessible in build env). §10.5 says so on-page and tests seven commonly repeated claims against Putnam records. |
| 6 | Landmarks | carried L1–L6 (dvr-upgrade.md Putnam). |
| 7 | Use cases / building stock | carried H1–H4; property-type cards are general descriptions (FLAG). |
| 8 | Bing / DuckDuckGo | EMPTY (not accessible in build env). |
| 9 | Local news | Mid-Hudson News (new M1, M2), Mahopac News, The Examiner, Daily Voice, WAMC, NYSP (carried). |
| 10 | Hyperlocal | Highlands Current, Mahopac News, Town of Putnam Valley, Putnam Sheriff/DA (carried). PCNR search this run returned only Putnam County WV/FL/TN results → EMPTY for a new PCNR item. |
| 11 | Yelp 1–3★ | EMPTY (not accessible in build env). |
| — | Drive "AESS Website Photos" | no NVR folder (per brief). CompanyCam not connected (per brief). |

### New this run (Firecrawl, 2026-10-18)
| # | Exact query · platform | URL | Finding | Page + section used |
|---|---|---|---|---|
| M1 | `Mid-Hudson News Putnam County burglary surveillance video 2026` · Firecrawl search → scrape (markdown) | https://midhudsonnews.com/2026/09/10/putnam-license-plate-readers-controlled-locally/ | Sept 10, 2026 (Eric Gross): Sheriff Brian Hess and Undersheriff James Menton testified to the legislature's Protective Services Committee; county "deliberately chose not to join any commercial camera network"; data "stored on a government server in Westchester controlled by regional law enforcement, is never sold or shared with private companies, and is not accessible through a nationwide search network"; historical data searched only in an active criminal investigation; "no facial recognition". Jan 1–mid-Aug: 21 active fixed LPR sites, 808 investigative alerts on 250 vehicles, 184 stolen vehicles, "27 known burglary crew vehicles tied to residential burglaries across the region, many connected to New York City", "22 vehicles linked to organized retail theft rings, typically out-of-state criminal organizations that travel to Putnam specifically to steal from local stores". | Hero sub; §5 para 1, 4; §5.5 bullets 1–2; §8 para after cards; §9 cluster 1 Q1, cluster 6 Q1; §10.5 H3 1–2; Sources |
| M2 | `"County exec chastises legislature over Flock cameras" Mid Hudson News` · Firecrawl search (full excerpt) | https://midhudsonnews.com/2026/10/16/county-exec-chastises-legislature-over-flock-cameras/ | Oct 16, 2026: Dutchess sheriff and DA stopped using the county's 64 Flock cameras; "offline since September 25"; removal demanded by Oct 30, 2026. (Dutchess, not Putnam.) | §5 para 1 (contrast sentence); Sources |
| BB1 | `Putnam County NY broadband unserved homes Comcast expansion 2026 Kent Putnam Valley Philipstown internet` · Firecrawl search (excerpt) | https://broadbandnow.com/New-York/Putnam-Valley | Third-party excerpt: "Fiber internet is 53.4% available in Putnam Valley. Cable is available to 93.6%". | Town-by-town (Putnam Valley, "about half"); §10.5 H3 6; Sources (labelled third-party) |
| X1 | `Patch Mahopac Carmel police surveillance footage theft 2026` · Firecrawl search | (Carmel PD / Sheriff Facebook, News 12 excerpts) | Social/undated excerpts only — not used. | — |
| X2 | `Highlands Current Philipstown security cameras footage 2026` · Firecrawl search | (section index pages only) | No camera/footage article surfaced → EMPTY. | — |
| X3 | `NYSEG Putnam County outage customers 2026 storm Carmel Kent Patterson` · Firecrawl search (past year) | (Facebook group excerpts) | No citable 2026 outage count → EMPTY; Isaias town counts carried instead. | — |

### Carried Putnam rows used (not re-fetched)
| # | From | URL | Finding | Used |
|---|---|---|---|---|
| N1 | floodlight-camera-installation.md N1 | https://news.halstonmedia.com/mahopac-news/mahopac-news/stories/police-warn-mahopac-residents-after-string-ofcar-break-ins,91083 | Mahopac News Aug 7, 2026: seven unlocked vehicles, four streets, ~3:37–5:05 a.m. Aug 5; Lake Casse, Lake Drive, Ridge Road; residents with cameras asked to review footage. | §5 para 4; §5.5 bullet 6; Town (Carmel); §9 cluster 6 Q3; §10.5 H3 2 |
| N2 | floodlight N2 | https://www.theexaminernews.com/police-warn-of-increased-vehicle-break-ins-in-putnam/ | Oct 2020: 10 vehicle break-ins + 1 stolen vehicle in Carmel, Patterson, Southeast over one weekend. | §5 para 4; §10.5 H3 2 |
| P1 | dvr-upgrade.md P1 | https://troopers.ny.gov/news/public-safety-alert-targeted-residential-burglaries-hudson-valley-region | NYSP Jan 29, 2025 targeted residential burglaries alert (Dutchess/Westchester/Putnam). | §5 para 4; §10.5 H3 2 |
| P2 | dvr-upgrade.md P2 | https://highlandscurrent.org/2024/09/10/police-investigating-philipstown-burglaries/ | Sept 2024 break-ins Old Albany Post Rd / Indian Brook Rd. | Town (Philipstown); §10.5 H3 2 |
| HV-N1 | nvr-installation.md HV-N1 | Putnam DA Sept 2025 | Southeast garage burglary solved with surveillance video. | Town (Southeast) |
| H1 | dvr-upgrade.md H1 | county hazard-mitigation profile PDF | >240 sq mi; 6 towns + 3 villages; ~3/4 NYC watershed; forest 66.9%; >9/10 Hudson Highlands gneiss/granite; commercial along Routes 6, 9, 22, 52, I-84/Route 312. | §5.5 bullet 3; §8 intro; Town (Southeast) |
| H2 | dvr-upgrade.md H2 | https://www.census.gov/quickfacts/putnamcountynewyork | 38,713 housing units; 83.8% owner-occupied; broadband subscription 94.8%. | §5.5 bullet 4; §10.5 H3 6 |
| H3 | dvr-upgrade.md H3 | ACS B25004 | 1,757 seasonal/recreational/occasional units. | §5.5 bullet 4 |
| H4 | dvr-upgrade.md H4 | https://www.historicpatterson.org/Exhibits/ExhPutLake.php | Lake colonies from 1928; 11,000 Putnam Lake lots, 20×100 ft, $50. | Town (Patterson); §7 card |
| N4/H5 | dvr-upgrade.md N4 | Daily Voice Isaias | Aug 5, 2020 10:15 a.m.: NYSEG 34,150/38,693; CH 3,621/5,160; Carmel 12,717, Kent 5,815, Southeast 5,220, Putnam Valley 5,088, Patterson 4,422, Brewster 818; CH Philipstown 2,475, Cold Spring 992, Nelsonville 154. | Hero; §5 para 2; §5.5 bullet 5; Town table; §10.5 H3 1 |
| W2 | dvr-upgrade.md W2 | Earth Networks NY lightning report | Putnam 2020: 75,093 pulses, 35 thunder days. | §9 cluster 3 Q2; §10.5 H3 4 |
| W3 | dvr-upgrade.md W3 | WAMC Mar 2021 | NYSEG circuit upgrades Horsepound/Stebbins roads, Carmel, rock drilling. | Town (Carmel) |
| W4 | dvr-upgrade.md W4 | Town of Putnam Valley, July 29, 2026 | Flash-flood state of emergency; Cimarron, Horton Hollow, Canopus Hollow restrictions. | Town (Putnam Valley) |
| B1 | dvr-upgrade.md B1 | Governor Sept 17, 2025 | Comcast fibre to 390 Putnam locations; SpaceX satellite listed for Putnam (HV-B2). | §5 para 2; §10.5 H3 6 |
| B2 | dvr-upgrade.md B2 | Highlands Current May 2023 | Optimum fibre through Philipstown; Verizon reviewing Cold Spring, no timeframe. | §5 para 2; §10.5 H3 6 |
| N1-dz | dvr-upgrade.md N1 | Schumer press release Oct 5, 2015 | More cell dead zones in northern Westchester and Putnam than carriers' maps show. | §9 cluster 4 Q1 |
| E1/E2/E5 | floodlight E1, E2, E5 | ecode360.com/6607815; putnamcountyny.gov/consumer-affairs; townofkentny.gov/faq | Ch. 145 low-voltage technician scope incl. video surveillance ≤90 V/5 A from an outlet installed by a licensed electrician; no unlicensed trade in county; licence lists; Ch. 135 registration mandatory; Kent issues no electrical permits; Patterson names SWIS/NYEIS. | Town (Kent, Patterson); §8.5 bullets 1–2; §9 cluster 5 Q1; §10.5 H3 5; FAQ 3 |
| R4 | dvr-upgrade.md R4 | Cold Spring HDRB certificate PDF | Exterior changes visible from street need HDRB approval since 1976; not visible = not reviewed. | Town (Philipstown); §8.5 bullet 8; §9 cluster 5 Q2 |
| U3 | floodlight U3 | Central Hudson territory map | Cold Spring, Nelsonville in CH territory. | Town table |
| L1–L6 | dvr-upgrade.md L1–L6 | Wikipedia/DEP/parks.ny.gov | Lake Mahopac ~587 acres, three islands; Courthouse 1814 Gleneida Ave; West Branch (Kent & Carmel, 1895, 8 bn gal, Route 301); Cold Spring HD 691 acres, NRHP 1982; Tilly Foster ~199 acres, county 2002; Fahnestock 15,000 acres. | §13 cards; Town paras |
| L8b | floodlight L8b | Wikipedia Putnam County | Hamlet/CDP names (Mahopac Falls, Lake Carmel, Lake Peekskill, Putnam Lake, Peach Lake, Ludingtonville, Farmers Mills, Tompkins Corners, Garrison, Continental Village, Nelsonville). North Highlands from the Highlands Current masthead (search excerpt). | §13 "we also install"; schema areaServed |
| G6, G8, G9, G10, G1/G2 | silo rows | §52-a; Penal Law 250; NYS DOS 6-D; Commercial Security Tax Credit; FCC DA 26-635 / FR 2026-13518 | as silo | §8.5; §9 cluster 2 Q3 |
| S1, S2 | silo HV rows | Uniview NVR501-08B (reseller) ≤6 W; WD Purple 0–65°C, 180 TB/yr | as silo | §7 rule para; §10 drives card; FAQ 10 |

### Prices used (§9 Putnam 1.45× — verified against blueprint-v2_3-full.md §9 and the HV hub's Putnam row)
Silo base (Brooklyn 1.00×, research/nvr-installation.md §2.7) × 1.45, round half-up: setup own NVR $220–$480 → **$319–$696**; new 8-ch $650–$1,500 → **$943–$2,175**; 16–32 ch/RAID $1,600–$5,500+ → **$2,320–$7,975+**; upgrade/migration/repair $190–$900 → **$276–$1,305** (all four identical to the HV hub's Putnam row). Per-line items from the BYOE calculator Brooklyn base × 1.45: camera line $175 → **$254**; concealed $200 → **$290**; raceway $100 → **$145**; conduit $200 → **$290**; J-box $25 → **$36**; recorder setup only $150 → **$218**; removal $50 → **$73**. Service $195/hr, 3-hr min ($585) verbatim, not multiplied. Worked example: $943–$2,175 + 5 × $254 + 2 × $290 = $2,793–$4,025. Schema OfferCatalog uses the same figures (low $218, high $7,975). COI line not published on this page (no building-management context).
**FLAG:** `install-your-own-camera-system.html` AREAS.putnam uses **+30%** (line $247, conceal $282, hourly $250), conflicting with §9 1.45×; the page follows §9 (as the HV hub does). Also inherited silo flags: whole ranges multiplied though they bundle equipment (v2.3 says labour only); $218 setup-only vs $319–$696 setup range are different scopes.

### Keywords (Putnam geo layer)
NVR installation Putnam County; NVR installation Putnam County NY; network video recorder Putnam; recorder installation Carmel / Mahopac / Brewster / Kent / Patterson / Putnam Valley / Cold Spring / Garrison / Putnam Lake / Lake Carmel; local-only camera recording; NYSEG outage recorder battery backup; Chapter 145 low-voltage licence; Route 6, Route 22, Route 52, Route 312 / I-84, Route 9. All 11 image alts/titles carry "NVR installation" + "Putnam County".

### Images (11) — permanent image rule (Drive: no NVR folder; CompanyCam not connected)
All opened and looked at (contact sheets + full-size previews). WebP q80, ≤1600 px; product PNGs flattened on white and trimmed. No faces, house numbers, plates or readable documents. Real-photo captions say "Example photo from another AESS job (not a Putnam County …)"; product shots say "Manufacturer product photo". Source scenes chosen to avoid the Bronx/HV NVR sets (rejected as same-scene: dahua orange recorder-monitor grid, store aisle monitor, storage-room turret, black bullet high wall, alien-mural fascia dome, stone-cornice wall arm, stained-tile corner dome).
| images/nvr-installation/nvr-installation-putnam-county-… | Source | Placement |
|---|---|---|
| ceiling-turret-camera-above-glass-entrance.webp (935×810) | images/dahua-camera-installation/dahua-camera-installation-suffolk-county-turret-camera-above-glass-storefront.webp (real AESS job) | Hero (eager) |
| small-camera-on-tall-white-wall-below-mezzanine.webp (902×470) | images/hikvision-security-camera-installation/…-ulster-county-high-ceiling-showroom-with-mezzanine-wall-camera.webp (real) | §5 |
| black-mini-bullet-camera-beside-wall-sensor.webp (630×360) | images/hikvision-security-camera-installation/…-long-island-black-mini-bullet-and-motion-sensor-on-wall.webp (real) | Town by town |
| two-white-turret-cameras-on-one-base-product-photo.webp (329×153) | images/hikvision-security-camera-installation/…-ulster-county-colorvu-turret-pair-product-photo.webp (product) | §6 |
| white-turret-camera-in-drop-ceiling-near-light-panel.webp (620×500) | images/hikvision-security-camera-installation/…-long-island-turret-camera-in-drop-ceiling-near-light-panel.webp (real) | §7 |
| bullet-camera-on-ceiling-pendant-mount.webp (935×520) | images/hikvision-security-camera-installation/…-ulster-county-black-bullet-on-ceiling-mount-in-office-grid.webp (real) | §8 |
| mini-dome-camera-beside-round-ceiling-speaker.webp (430×280) | images/hikvision-security-camera-installation/…-westchester-county-mini-dome-and-round-speaker-in-store-ceiling.webp (real) | §9 after cluster 3 |
| stainless-steel-housing-bullet-camera-product-photo.webp (400×400) | images/dahua-camera-installation/…-orange-county-stainless-steel-housing-bullet-camera-product-photo.webp (product) | §10 |
| rack-width-recorder-with-silver-front-curve-product-photo.webp (500×108) | images/nvr-speco-n16nrx.png (product) | §14 |
| slim-angled-recorder-product-photo.webp (371×156) | images/nvr-luminys-r5216pa.png (product) | §15 |
| desktop-recorder-with-red-status-lights-product-photo.webp (469×182) | images/nvr-idis-dr2508p.png (product) | Field Notes |
Swapped late in the build because the parallel Long Island builder (finished 09:28Z) had used the same sources: Swann front/rear recorder, ENS multi-bay recorder, dahua suffolk mini dome (= LI "black ball camera at ceiling edge"), dahua orange exit-sign ceiling (= LI "ceiling camera near lit exit sign") → replaced by the four rows above. The unused-recorder product pool is now exhausted (all images/nvr-*.png and the apartment-silo recorder shots are on Bronx/HV/LI/SI pages) — FLAG: real NVR photos needed.
DAILY-LOG note: `images: 11 reused from images/dahua-camera-installation/, hikvision-security-camera-installation/ (6 real job photos) + 5 manufacturer product photos (no real NVR Installation photos yet)`.

### Question register — nvr-installation-putnam-county (REBUILT 2026-10-18): 12 Q&A H3 + 2 "?" H2s + 10 FAQ (final list below supersedes any earlier draft)
"?" H2s: Putnam Recorder Off Your Phone, or Missing the Storm Night? · Want the Footage to Stay on Your Property?
§9 Q&A H3 (clusters: Keeping Putnam footage in Putnam · Lake colonies, lake houses and associations · Private roads, lightning and wet ground · When the power and the internet fail together · Licences and the review board · Shops, offices and the crews the Sheriff described):
  1. The Sheriff told the county legislature that Putnam keeps its plate-reader data on a local server, not a vendor's cloud — can our cameras be set up the same way?
  2. From ice-out to freeze-up the dock is where things go missing — can a recorder get usable night video of a boat tied up 150 feet from the house?
  3. The lake association wants cameras on its beach and dock — should they record to one member's house or to a recorder of their own?
  4. Our dock camera can see a neighbour's yard across the cove — what does New York law say about that view?
  5. Who should own, power and keep the footage for a camera where our private road meets the town road?
  6. Putnam took tens of thousands of lightning pulses in a single year — can a strike near a camera at the far edge of the lot reach the recorder through the cable?
  7. When the power and the internet both go down at the empty lake house, how do we even find out?
  8. Does Putnam's Chapter 145 cover the network cable between the recorder and each camera, or only the outlet the recorder plugs into?
  9. Which camera positions on a house in Cold Spring's historic district can go up without a review-board application?
  10. The Sheriff says organized retail-theft crews travel to Putnam to target local stores — what should a shop's recorder capture so a clip is worth handing over?
  11. Our office near I-84 and Route 312 has to keep its recorder in the building's shared telecom room — how is it kept out of other tenants' reach?
  12. The Mahopac car break-ins happened between about 3:30 and 5 a.m. — can the recorder wake us for a person in the driveway at that hour without calling us for every deer?
§17 FAQ (visible == FAQPage, 10):
  1. We have a place in the city and the house in Putnam — can both recorders show up in one app?
  2. If the router has to move into the recorder's closet, will the Wi-Fi in the rest of the house suffer?
  3. Can you work with the electrician installing our generator transfer switch so the recorder circuit is on the backed-up panel?
  4. We rent the house to weekend guests — how do we keep them away from the recorder, and what should they be told about the cameras?
  5. What happens to the hard drive inside the old recorder you take away?
  6. If someone steals the recorder, can they play back what is on it?
  7. How often does the recorder's battery backup need a new battery?
  8. Do you cover the whole county — Garrison and Continental Village as well as Brewster and Putnam Lake?
  9. What should we do to get the house ready for install day?
  10. How much electricity does a recorder and its cameras use running all year?
§10.5 claim H3s (quoted claims, not questions): cloud safer than a recorder; Putnam is quiet so a recorder is overkill; Wi-Fi cameras do the same job; lightning only matters if it hits the house; your town's building department signs off camera work; fast internet is everywhere in the county; motion-only recording loses nothing.

De-dup notes: checked against the old-template register, the rebuilt Bronx and HV pages (research/nvr-installation.md §4, B.3), the rebuilt Long Island page (09:28Z, 23 question headings) and the rebuilt Staten Island page (09:34Z, 26 question headings) — this page finished last and was adjusted. Changed for LI: bungalow "no basement — where does the recorder go" (LI slab/no-cellar) → dock night-video Q; FAQ recorder noise in a closet (LI + SI) → install-day prep; FAQ storm-forecast prep (LI hurricane, SI nor'easter) → UPS battery replacement; FAQ winter install on a steep drive (LI best time of year) → router-in-closet Wi-Fi; cellular-backup removed from the outage question wording (LI owns "alerts over a cellular backup"). Changed for SI: plate-reading Q dropped (SI "Can our home recorder read the plates of cars that drive past?"); flash-flood "what saves the recordings" Q dropped (SI basement-flood footage + which-floor Qs); FAQ weekend booking (SI "Saturday or Sunday") → two homes in one app; office Q reframed from "separate from the landlord's system" (SI/LI landlord-camera Qs) to securing a recorder in a shared telecom room. Also avoided cross-silo Putnam intents already used on floodlight-/dvr-upgrade-putnam pages (licence-list lookup, Kent permits, private-road camera placement, winter shutdown, Dark House Check, cell signal at home, data caps, house number, video-call handover).
Masked paragraph similarity (SequenceMatcher on ≥8-word p/li/td/h2/h3/figcaption blocks, geo masked via check_page.mask, nav/scripts excluded): only ≥0.65 block is the blueprint-fixed H2 "What AI Gets Wrong About NVR Installation in [Area]"; excluding it, max 0.606 vs Bronx, 0.606 vs Staten Island, 0.571 vs Long Island, 0.556 vs HV, ≤0.30 vs every old-template sibling. File 190,430 B (Bronx 178,365; HV 183,846; LI 183,626; SI 173,851 at check time).

### FLAGS for Anwar (Putnam page)
1. Pricing: BYOE calculator Putnam +30% vs §9 1.45× (page uses §9, matching the HV hub); per-line items are the calculator's Brooklyn base × 1.45 and are not published anywhere else for Putnam.
2. AESS's own Putnam Ch. 145 low-voltage licence / Ch. 135 registration is NOT claimed; the page tells owners to check any installer, "including us", on the county lists. Confirm status — if licensed, the page can say so.
3. Unsourced practice statements (installer knowledge): VPN vs maker relay; dock night-video method (IR reflection, wireless radios, continuous at night); association/road recorder ownership advice; surge protection approach; offline-device alerts and LTE failover; Cold Spring camera positions likely outside HDRB scope (based on the "not visible from the street" rule); retail-capture four views; tenant network separation; person/vehicle alert scheduling; UPS battery life "every few years"; router/Wi-Fi advice; rental-guest guidance (no platform rule cited); drive wipe/thief playback; schema openingHours Mo-Su 08:00-20:00 (silo convention, as on floodlight-putnam; no arrival-window claim in the body); "recording again within one to two hours of arrival" (blueprint el. 36). Comparison table (NVR vs ADT-style vs Ring/SimpliSafe) is a general description, captioned as such.
4. Field Notes are installer-voice method (panel → wheel → road), not a specific Putnam job story.
5. BroadbandNow (Putnam Valley fibre 53.4%) is a third-party excerpt, labelled as such on the page.
6. Property-type cards (bungalows, lakefront, hillside, village, colonials, estates) and corridor cards are general descriptions without per-item sources (same as HV hub FLAG).
7. Sibling link-backs: 12 "live sibling … doesn't link back to /nvr-installation-putnam-county" lines from check_page.py are main-run wiring (old-template siblings + Bronx); the HV hub already links down to this page.


<!-- Merged from nvr-installation-staten-island builder (batch 2026-10-18 09:12Z) -->
# NVR Installation — Staten Island (part file, for merge into research/nvr-installation.md)

Page: `nvr-installation-staten-island` (REBUILD in place, 2026-10-18; was crawled-not-indexed). Queue line: `REBUILD | nvr-installation-staten-island | NVR Installation | Staten Island | up /nvr-installation-nyc | (347) 934-8335 | GBP Brooklyn`. Direct line (347) 934-8335 in body, CTAs and schema; (800) 486-0943 only in the shared mega-nav header. GBP Brooklyn: 1282 Troy Ave, Brooklyn NY 11203, `#brooklyn` (LocalBusiness block modelled on intercom-repair-staten-island.html; openingHours Mo-Su 08:00-20:00). WhatsApp only as wa.me/17186790359. Nothing from the old template text, FAQ, prices or images reused.

Tools: WebSearch, WebFetch, Firecrawl search/scrape (`mcp__Firecrawl__*`, summary / query-directQuote / markdown). Shell HTTP not used. Rows marked "carried" were fetched by earlier 2026-10-17/18 Staten Island builds (research/floodlight-camera-installation.md `## Staten Island`, research/intercom-repair.md `### Staten Island`) and re-used, not re-fetched. Format per v2.3 §12.4.

## Thesis (distinct from Bronx and Hudson Valley rebuilds)
On Staten Island the NVR is a **homeowner's recorder** (83% of units in one-/two-family homes) whose cameras watch a **driveway, a curb and a stoop**, and the island-specific risks are to the recorder itself: **water** (Sandy inundation area, raised houses, Appendix G equipment above the design flood elevation, July 2025 basement flooding in Rossville), **power** (Con Ed July 25, 2025: ~21,000 SI customers out, mostly East Shore; 8% voltage reduction on the east side), and **night image quality** for the car-door/package incidents island footage is used for, with a hand-off to one of four precincts. Plus two-household privacy (two-families, semi-attached shared drives), the 2026 private plate-reader debate, and strip-center/West Shore business sites. Bronx = evidence locker in a building someone else controls; HV = self-sufficient recorder in an empty weekend house; SI = recorder above the water line, tuned for the driveway at 4 a.m.

## Source matrix (§3) for this geo
| # | Source | Result |
|---|---|---|
| 1 | Reddit r/StatenIsland | `site:reddit.com r/statenisland security camera NVR package stolen footage` · Firecrawl search → only an unrelated r/HighStrangeness thread → **EMPTY**. Earlier SI builds also found no r/StatenIsland camera/intercom thread (carried). Not used. |
| 2–5 | PAA / PASF / Answer the Public / AI Overview | **EMPTY (not accessible in build env)**. §10.5 says so on the page and tests seven commonly repeated claims instead. |
| 6–7 | Landmarks / building stock | rows SI-H, SI-L (carried + new) |
| 8 | Bing / DDG | **EMPTY (not accessible in build env)** |
| 9–10 | Local news / hyperlocal | SILive (2017, 2022, 2025, Apr 2026, Sept 2026), NY1, Con Edison, Hoodline, DNAinfo |
| 11 | Yelp 1–3★ | not re-searched; earlier SI builds got listing pages only → **EMPTY (not accessible in build env)** |
| — | Google Drive "AESS Website Photos" | no NVR Installation folder (only Cat6 Repair, Sonos, Fiber Optic, Soundbar, Smart Lock) — per brief |
| — | CompanyCam | not connected — per brief |

## New local research (this build)
| ID | Exact query · platform | URL | Finding | Used (page section) |
|---|---|---|---|---|
| SIN-P1 | `Con Edison Staten Island power outage customers 2026` · WebSearch → WebFetch | https://www.coned.com/en/about-us/media-center/news/2025/07-25/con-edison-crews-restoring-service-more-than-24000-customers-initially-impacted | Jul 25, 2025: "A brief, intense storm caused approximately 21,000 Staten Island customers to initially lose power." "Most of those customers were located along the eastern shore." | §5 para 3; §5.5 bullet 4; Sources |
| SIN-P2 | same search · WebFetch | https://ny1.com/nyc/staten-island/news/2025/07/25/thousands-without-power-on-staten-island-amid-heat--storms | Jul 25, 2025: >18,100 SI customers out at 6:20 p.m.; Con Ed "reduced voltage by 8% on the east side of Staten Island"; neighborhoods named incl. New Brighton, St. George, Tompkinsville, Stapleton, Clifton, Rosebank, South Beach, Ocean Breeze, Midland Beach, Grant City, New Dorp, Dongan Hills | §5 para 3; §5.5 bullet 4; §10 H3 outage; §10.5 (none); Sources |
| SIN-N1 | `silive.com 2026 Staten Island cars broken into overnight caught on camera NYPD precinct` · Firecrawl search → scrape (summary) | https://www.silive.com/crime-safety/2022/09/residents-of-this-staten-island-community-say-thieves-are-accessing-locked-cars-are-high-tech-devices-at-work.html | Sept 21, 2022 (Kyle Lawson): Mariners Harbor; image caption "Surveillance footage captured Aug. 28 around 4:30 a.m. on Simonson Avenue shows an unidentified individual seemingly attempting to access parked vehicles"; residents suspect fob "code grabbers". (Article also cites a 121st Pct theft % — NOT used: blueprint App. B keeps NYPD crime-data citations off non-solar pages.) | §5 para 3; §9 night-blur H3; Sources |
| SIN-N2 | same search → scrape (summary) | https://www.silive.com/news/2017/07/watch_teens_break_into_cars_on.html | Jul 12, 2017 (Paul Liotta): surveillance footage of teens breaking into cars in Annadale early Monday; unlocked cars targeted; three arrested | §5 para 3; §9 night-blur H3; Sources |
| SIN-N3 | `silive car thefts Staten Island up 22% 2026 71 vehicles` · Firecrawl search → scrape (summary) | https://www.silive.com/crime-safety/2026/04/nypd-staffing-shortage-blamed-as-staten-island-car-thefts-spike-22-over-last-year.html | Apr 27, 2026: BP Fossella and DA McMahon press for more officers after a rise in car thefts; task force; CompStat 71 vs 58 | **Not used** (CompStat crime data — blueprint App. B rule). Background only. |
| SIN-N4 | `Staten Island District Attorney McMahon camera registry program …` · Firecrawl search → scrape (markdown) | https://www.silive.com/news/2026/09/always-watching-officials-say-staten-island-surveillance-cameras-caught-murderers-shooters-car-thieves-kidnappers.html | Sept 27, 2026 (Kyle Lawson): plate readers on SI; photo caption: "a Flock Safety camera is seen outside a business on Forest Avenue in Mariners Harbor"; "Data collected by privately owned Flock cameras belong to the owner, who could share the information with the authorities or whomever they choose."; "several businesses across Staten Island have Flock Safety cameras" (per DeFlock); NYPD uses Leonardo ELSAG; "In New York, there is currently no statewide statute in effect that comprehensively governs the operation of automatic license plate recognition systems by police agencies."; A10808/S9890 (2026) would create GBL §397-c. DA quote on plate readers. No SI camera-registry program found → **EMPTY** for a registry. | §5.5 bullet 6; §9 business plate-reader H3; §10.5 H3 5; Sources |
| SIN-N5 | (link in SIN-N4) | https://www.nysenate.gov/legislation/bills/2025/S9890 | 2026 bill S9890 (as described by SILive; bill page not fetched) | Sources (named as proposal only) |
| SIN-F1 | `Staten Island basements flooded storm 2025 OR 2026 silive flash flooding homes` · Firecrawl search (excerpt incl. article body) | https://www.silive.com/news/2025/07/severe-flash-flooding-cripples-major-staten-island-roads-during-storm-monday.html | Jul 14, 2025: flash flooding turned Hylan Blvd into a river (photo: past New Dorp Lane); "The basements of multiple homes on Poplar Avenue in Rossville were flooded" | §5 para 2; §9 wet-recorder H3; §10.5 H3 1; Sources |
| SIN-F2 | same search (Instagram excerpt) | https://www.instagram.com/reel/DdzWwLMkqcz/ | Sept 27, 2026 nor'easter flooded parts of Arthur Kill Rd and Travis Ave (SI Advance IG) | Not used (social excerpt) |
| SIN-T1 | `flooded hard drive do not power on data recovery advice …` · Firecrawl search (excerpts) | https://www.gillware.com/resources/water-damaged-hard-drive-handling-guidelines/ ; https://mdrepairs.com/blog/water-damaged-hard-drive/ ; https://acsdata.com/flooded-hard-drives.htm | "Do not power it on: a damp circuit board can short… spinning them up drags the read/write…" (Gillware); recovery common for drives never powered on (MDrepairs) | §9 wet-recorder H3; §10.5 H3 1; Sources (Gillware) |
| SIN-L1 | `NYPD 122nd precinct Staten Island neighborhoods covered 2320 Hylan Boulevard` · WebSearch → WebFetch | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/122nd-precinct.page | 2320 Hylan Blvd, New Dorp; "a portion of the South Shore"; Eltingville, Great Kills, Bay Terrace, Oakwood Heights, Oakwood Beach, Lighthouse Hill, New Dorp, Grant City, Midland Beach, South Beach, Todt Hill, Old Town, Grasmere | §5.5 bullet 5; §9 precinct H3; §13 Hylan card; Sources |
| SIN-L2 | precinct pages · WebFetch (**permission prompt timed out → EMPTY via WebFetch**) → Firecrawl scrape (query/directQuote) | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/120th-precinct.page | "The 120th Precinct serves the North Shore of Staten Island" — Castleton Corners, Westerleigh, … Tompkinsville, Concord, Sunnyside, West Brighton, … New Brighton, St. George, Ward Hill, Stapleton, Clifton, Silver Lake, Grymes Hill, Fox Hills, Shore Acres, Rosebank | §5.5 bullet 5; §9 precinct H3; Sources |
| SIN-L3 | same | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/121st-precinct.page | "serves the northwestern shore … Willowbrook, Westerleigh, Port Richmond, Mariner's Harbor, Elm Park, Port Ivory, Chelsea, and Bloomfield"; 970 Richmond Avenue | §5.5 bullet 5; §9 precinct H3; §13 Mall card; Sources |
| SIN-L4 | same | https://www.nyc.gov/site/nypd/bureaus/patrol/precincts/123rd-precinct.page | "a portion of the South Shore … Tottenville, Huguenot, Rossville, Annadale, and Eltingville"; 116 Main Street | §5.5 bullet 5; §9 precinct H3; Sources |
| SIN-L5 | same WebSearch · WebFetch | https://www.dnainfo.com/new-york/20130702/graniteville/new-nypd-precinct-opens-staten-island | 121st opened July 1, 2013 at "950 Richmond Ave", territory "formerly shared by the 120 and 122 precinct". **Conflict:** nyc.gov gives 970 Richmond Avenue → page says "on Richmond Avenue" only. | §5.5 bullet 5; Sources |
| SIN-L6 | same WebSearch · WebFetch | https://www.nyc.gov/site/nypd/news/f0614/your-neighborhood-police-123rd-precinct-staten-island | Jun 14, 2018: 123rd "covers the most out-of-the way part of Staten Island, on the South Shore" | Background |
| SIN-L7 | `Staten Island Teleport Bloomfield office park acres companies` · Firecrawl search (excerpts) | https://www.panynj.gov/port-authority/en/building-the-region/office-commercial-facilities.html ; https://en.wikipedia.org/wiki/Teleport_(Staten_Island) | Port Authority: "the 100-acre Teleport business park includes five Class A office and specialized buildings", 11 miles from Manhattan; Wikipedia: east of NY-440, west of Bulls Head | §8 Teleport card; §8 West Shore para; §9 PTZ H3; §13 Teleport card; Sources |
| SIN-R1 | `NY Civil Rights Law 52-a` · Firecrawl scrape (directQuote) | https://www.nysenate.gov/legislation/laws/CVR/52-A | private right of action against a person who installs a video imaging device on adjoining property to videotape the backyard without written consent "with intent to harass, annoy or alarm another person, or with intent to threaten" | §9 semi-attached H3; §10.5 H3 6; Sources |
| SIN-R2 | Firecrawl scrape (directQuote) | https://www.nysenate.gov/legislation/laws/PEN/250.45 | unlawful surveillance 2nd degree: surreptitious imaging in a bedroom, changing room, restroom, bathroom etc. "for no legitimate purpose" (rebuttable presumption) | §8.5 bullet 4; §9 two-family H3; §10.5 H3 6; Sources |
| SIN-N6 | `Staten Island package theft porch surveillance video 2026` · WebSearch | (CBS "S.I. Christmas present thief" — undated AMP page; other results not SI) | No 2026 SI package-theft article found → **EMPTY**; package Q answered as general practice | — |

## Carried facts re-used (fetched by earlier SI builds; source rows named)
| Fact | URL | From | Used |
|---|---|---|---|
| 83% of SI units in 1–2 family homes (CHPC Oct 2024) | https://chpcny.org/visualization/housing-stock-visualization/ | floodlight SI-H1 | §5 para 1; §5.5 bullet 1 |
| 11,700+ buildings in inundated area, ~90% 1–2 family | https://www.nyc.gov/site/sirr/rebuilding/east-and-south-shore-staten-island.page | floodlight SI-H6 | §5 para 2; §5.5 bullet 2 |
| Build It Back: 1,982 SI homeowners served | https://www.nyc.gov/site/housingrecovery/disaster-recovery/build-it-back.page | floodlight SI-H4 | §5 para 2; §5.5 bullet 2 |
| Appendix G: equipment at/above DFE; coastal high-hazard space below = parking, access, storage, crawl space | https://up.codes/viewer/new_york_city/nyc-building-code-2022/chapter/G/flood-resistant-construction | floodlight SI-R1 | §5.5 bullet 3; §7 raised-house H3; §8.5 bullet 7; §10.5 H3 1 |
| Great Kills high-ranch two-families; New Dorp/Dongan Hills semi-attached; Charleston/Rossville newer semi-attached; North Shore Victorians | https://prodigyre.com/blog/the-two-family-wealth-engine-how-staten-islands-most-common-home-type-built-middle-class-wealth | floodlight SI-H2 | §7 cards (descriptive) |
| Townhouse condo communities (Annadale, Huguenot, Eltingville); association owns roads/grounds | https://nacmiaslaw.com/practice-areas/closings/building-types/townhouse-condo-declaration/staten-island | floodlight SI-H3 | §7 card |
| St. George/New Brighton HD designated 1994 | https://hdc.org/preservation-resources/expanding-historic-district-boundaries/expanding-historic-district-boundaries/ | floodlight SI-R5 | §7 card; §13 card |
| Hylan Blvd longest street in NYC | https://en.wikipedia.org/wiki/Staten_Island | floodlight SI-H9 | §8 card; §13 card |
| SI Mall opened Aug 9 1973, Richmond Ave at Richmond Hill Rd | https://www.silive.com/news/erry-2018/03/05c8690920/10_things_to_know_about_the_st.html | floodlight SI-L3 | §8 card; §13 card |
| Empire Outlets 350,000 sq ft | https://en.wikipedia.org/wiki/Empire_Outlets | floodlight SI-L4 | §8 card; §13 card |
| Bay Street rezoning June 26 2019 | https://citylimits.org/2019/06/26/council-approves-bay-street-rezoning-the-sixth-under-de-blasios-housing-plan/ | floodlight SI-L5 | §8 card |
| Matrix Global Logistics Park 200 acres, former oil-tank site | https://www.margulieshoelzli.com/projects/matrix-global-logistics-park/ | floodlight SI-L6 | §8 card |
| SIUH 475 Seaview Ave | https://siuh.northwell.edu/ | floodlight SI-L7 | §8 card |
| Greenbelt 2,800 acres; along Todt Hill's western edge; Emerson Hill | https://www.nycgovparks.org/park-features/hiking/greenbelt | floodlight SI-L1 | §13 card |
| Seawall ~5 mi, elev. 21 ft, Fort Wadsworth → Oakwood Beach | https://www.dvidshub.net/news/482917/seawall-will-raise-quality-life-shore-communities-staten-island-new-york | floodlight SI-H7 | §13 card |
| Deer ~2,053 (Jan 2017) → ~1,616 (Jan 2021) | https://www.nycgovparks.org/news/press-releases?id=21871 | floodlight SI-N8 | §7 hillside para; Sources |
| Feb 2026 crowbar burglary spree, New Dorp / Dongan Hills / Todt Hill, early hours | https://hoodline.com/2026/02/nypd-hunts-for-trio-suspected-in-staten-island-burglary-spree/ | floodlight SI-N1 | §5 para 3; Sources |
| Silo rows G1 (FCC DA 26-635), G6 (§22-1202), G8 (Penal 250 audio), G9 (DOS licence), G10 (tax credit), T1/S2 (WD Purple 180 TB/yr, 0–65 °C), A1/A2/S7 (Angi, Wasserstein, HomeAdvisor), P1 (Hornwright 7–10 days) | see research/nvr-installation.md §2 / HV §A | silo | §8.5; §10 drives card; §10.5 H3 3–4; Sources |

## Question register — nvr-installation-staten-island (rebuilt 2026-10-18)
Repair H2 (ends "?"): Recorder Flooded, Dark or Stuck After a Staten Island Storm?
CTA H2: Not Sure Which Floor the Recorder Belongs On?
§9 Q&A H3 (11), by cluster:
- Water and Salt on the Shore
  1. The recorder sat in water after the storm — is it safe to switch it back on to see whether the video survived?
  2. We live a few blocks from the beach in Midland Beach — does the salt air reach the recorder, or only the cameras?
- Driveways, Cars and the Stoop
  3. Someone tries car door handles on our block before dawn — why does the recorder's night video show a blur instead of a face?
  4. A package went missing from the stoop — can the recorder show exactly when it arrived and who took it?
- Two-Families and Neighbors
  5. We rent the downstairs of our two-family — can the recorder cover the shared side door and the tenant's entrance?
  6. On our semi-attached block the driveway is shared — how do we keep the camera from recording the neighbors' comings and goings?
  7. A neighbor's car was broken into and they want our footage — should we give it to them?
- Break-Ins, Precincts and Plate Readers
  8. Our car was broken into overnight — what should we do on the recorder before we call the precinct?
  9. Is a Staten Island business allowed to run its own plate-reader camera, and who owns what it records?
- Strip Centers, Offices and the West Shore
  10. Our store closes at nine but the strip-center lot stays busy until midnight — how should the recorder treat the hours after we lock up?
  11. Our West Shore warehouse yard is too big for fixed cameras — when does a pan-tilt-zoom camera make sense on the recorder?
§17 FAQ (visible == FAQPage, 10):
  1. Is there an extra charge because the job is on the other side of the Verrazzano?
  2. Can the recorder keep more days of the driveway than of the backyard?
  3. Can the recorder protect a clip so it is not overwritten while an insurance claim or court case is open?
  4. Can the camera cables be hidden inside the walls of a finished house?
  5. Will our homeowner's insurance give us a discount for a recorded camera system?
  6. Do you install cameras inside the house too, and where do people usually put them?
  7. If a camera needs re-aiming months after the install, what does a return visit cost?
  8. Can you mount cameras on vinyl or aluminum siding without cracking it?
  9. What does the warranty cover on a recorder you supply?
  10. Will you set up the phone app for family members who do not use apps much?
§10.5 claim H3s (quoted claims, not questions): basement placement; 4K catches face/plate at night; cloud cheaper than NVR; month of video automatically; private plate readers illegal; point cameras anywhere on your property; same price anywhere in the city.

**De-dup decisions (by meaning, after reading the rebuilt Bronx, HV, Long Island (09:42 file) and Putnam (09:36 file) pages):** dropped/rewritten because a sibling owns the intent — "which floor after the house was raised" and "wiring under a raised house" (LI owns "can any camera equipment stay in the flood-vented space"; content kept as non-question §7 text "Raised houses: recorder up, cameras down"); "unplug before a hurricane" (LI); "how loud is the recorder in a living-floor cabinet" (LI); "work alongside the alarm company" (LI); "landlord's lot cameras on our recorder" (LI; kept as §8 body text); "office IT sign-off" (LI outside IT company); "weekend install" (Putnam); "home recorder reading plates of passing cars" (Putnam bottom-of-drive plates); "package alert while the person is still there" (Putnam person-in-driveway alert → reframed to evidence timeline); "semi-attached cost split / shared ownership" (Putnam private-road camera ownership → reframed to privacy masks on a shared drive); "three island houses in one app" (Putnam city + lake house in one app); "townhouse association approval paperwork" (LI garden co-op board approval). Brownout/battery, room selection, admin custody, role accounts, detective export, CAMS, live share, covered-brand keep/replace, biometric sign, audio, continuous vs motion at a dock, linked buildings (Bronx) and all HV intents avoided. Old-template 12 intents avoided (cost lives in §14/§15 tables only).

Intents this page owns for the silo: wet/flooded recorder salvage; salt air reach; night blur vs face on driveway; package arrival/theft timeline; two-family tenant entrance coverage; shared-driveway privacy masks; sharing footage with a neighbor; first steps on the recorder after an overnight car break-in + SI precinct map; business-owned plate readers legality/ownership; after-hours recording schedule for strip-center lots; PTZ for large yards; FAQ: Verrazzano/travel charge, per-camera retention priority, locking clips, hidden in-wall cabling, insurance discount, indoor cameras, re-aim return visit cost, siding mounts, warranty layers, app setup for older family members.

## Images (11) — Drive: no NVR folder; CompanyCam not connected → permanent image rule
All converted with Pillow (WebP q80, ≤1600 px; PNG transparency flattened on white; product shots auto-trimmed). Each source viewed with the Read tool (contact sheets + full-size for the real photos) before use; crops re-viewed. No faces, house numbers, plates or readable documents (the deli crop was tightened to exclude wall notices; the rack crop excludes the monitor and an installer sticker). Captions say "Manufacturer product photo, not an installed unit" or that the job photo is from an AESS job off the island.
Real AESS job scenes in the repo were already used by the Bronx, HV, LI and Putnam builds (deli monitor/fascia/ceiling, Rockland monitor/hallway/wall/office/showroom/active-deterrent/ceiling-bullet/dome, Nassau monitor/office/storage). Only three **new crops** of those scenes were possible; the rest are product shots. FLAG: real island NVR job photos needed.
| Output (images/nvr-installation/nvr-installation-staten-island-…webp) | Source | Size | Placement |
|---|---|---|---|
| lorex-sixteen-channel-4k-recorder-product-photo | images/nvr-lorex-4k-16ch.png (product) | 867×167 | Hero (eager) |
| patch-cable-bundles-down-equipment-rack | images/rockland-toyota-nvr-monitor.jpeg crop (0,0,250,700) — real AESS job; Bronx used the ceiling strip/monitor | 250×700 | §5 |
| trendnet-recorder-product-photo | images/nvr-trendnet-tv-nvr208.png (product) | 899×338 | §6 |
| eyeball-turret-camera-with-warm-light-product-photo | images/cam-eyeball-warm.jpeg (product, unbranded) | 205×219 | §7 |
| dome-camera-atop-wood-panel-store-wall | images/manhattan-deli-interior-cameras.jpeg crop (520,400,800,600) — real AESS job; LI used the ceiling area | 280×200 | §8 |
| dual-lens-turret-camera-with-warning-lights-product-photo | images/cam-dual-lens-active.jpeg (product, unbranded) | 894×893 | §9 after cluster 2 |
| plate-capture-bullet-camera-with-blue-ring-product-photo | images/apartment-building-security-camera-installation/…-staten-island-plate-reading-bullet-camera-product.webp (product) | 265×170 | §9 after cluster 4 |
| dome-camera-beside-track-lights-on-drop-ceiling | images/manhattan-deli-interior-cameras.jpeg crop (0,130,470,430) — real AESS job | 470×300 | §9 after cluster 5 |
| stainless-steel-ptz-dome-camera-product-photo | images/dahua-full-color-compact-bullet-camera-white.png — **filename mismatch: file shows a stainless PTZ dome** (brand mark only partly legible; caption names no brand) | 400×400 | §10 |
| hikvision-varifocal-bullet-camera-product-photo | images/hikvision-varifocal-bullet-camera.jpg (product; caption notes Covered List) | 299×134 | §14 |
| white-ptz-speed-dome-camera-product-photo | images/dahua-wizsense-ai-varifocal-bullet-camera-white.png — **filename mismatch: file shows a white Dahua PTZ speed dome** | 400×400 | §15 |
Also noted: images/dahua-marine-stainless-ptz-dome-camera.png actually shows a white Dahua bullet (not used). DAILY-LOG note suggestion: `images: 3 new crops of real AESS job photos (rockland-toyota, manhattan-deli) + 8 manufacturer product shots (no real NVR Installation photos yet)`.

## Pricing — §9 Staten Island 1.10 (verified in blueprint-v2_3-full.md §9 table), round half-up
Silo base (Brooklyn 1.00×, research/nvr-installation.md §2.7): recorder setup only $150 → **$165**; set up owned recorder + cameras $220–$480 → **$242–$528**; new 8-ch build $650–$1,500 → **$715–$1,650**; 16–32 ch / RAID $1,600–$5,500+ → **$1,760–$6,050+**; upgrade/migration/repair $190–$900 → **$209–$990**; camera line $175 → **$193** (192.5↑); concealed drywall $200 → **$220**; raceway $100 → **$110**; conduit $200 → **$220**; J-box $25 → **$28** (27.5↑); removal $50 → **$55**; COI $0; service $195/hr, 3-hr min ($585) protected, not multiplied.
Worked example (§14): $715–$1,650 + 5 × $193 ($965) + 2 × $220 ($440) = **$2,120–$3,055**. Package cards (§15) composed only from those lines: Driveway & Stoop = 8-ch + 4 lines ($772) = $1,487–$2,422; Raised House/Two-Family = 8-ch + 6 lines ($1,158) + 3 conduit ($660) = $2,533–$3,468; Store/Office = 16–32 ch $1,760–$6,050+ plus $193/line. Service schema AggregateOffer low $165 / high $6,050.
FLAGS: (1) the BYOE calculator (install-your-own-camera-system.html AREAS['staten-island']) uses **+20%** (line $210, conceal $240, hourly $225) — conflicts with §9 1.10; page follows §9. (2) Silo base ranges bundle equipment with labour; whole range multiplied (same as HV). (3) "No separate toll line or travel charge" carried from network-cable-repair-staten-island wording via floodlight/intercom SI research. (4) Package cards are line-item compositions, not separately published packages.

## House practices stated without an external source (FLAG for Anwar)
- Recorder/switch/modem/UPS on the first living floor of raised or flood-prone houses; one protected chase; no splices/switches/PoE extenders in the flood space; garage-under-house rejected.
- Salt air: sealed connector boots, stainless fixings, drip loops, splices indoors; stainless/treated housings only for piers/marinas/waterfront yards.
- Night tuning (shutter limit, IR/white light, main-stream recording) and after-dark verification; plate camera placement where cars slow; person-event search for package timelines.
- Two-family/semi-attached: written notice to tenant, audio off, view-only single-camera logins, privacy masks; neighbor footage given as copies.
- First steps after a break-in (clock offset, lock/export, call precinct); per-camera retention priority; clip locking + export; recorder schedule switching with alarm arming; PTZ preset patrols.
- West Shore IT coordination (address range, internet access, update policy, separate segment); strip-center lease/landlord camera practice.
- Insurance discount answer hedged ("ask your agent"); indoor-camera privacy practice; app setup for older relatives; siding blocks; deer false-alert mitigation.
- §10.5 H3 3 national-brand comparison (Wi-Fi/cloud subscription model) and §14 "National brands compared with a local installer" — general description, no brand-specific claims sourced.
- "Most recorder faults recording again within one to two hours of arrival" and same-day slot language (blueprint element 36 / silo convention); Mo–Su 8 AM–8 PM (SI intercom convention).
- Field Notes = Anwar-voice method note (water line first), not a specific job story — Anwar to confirm or replace with a real island anecdote.

## Keywords (SI geo layer)
NVR installation Staten Island; network video recorder installation Staten Island NY; NVR raised house Staten Island; recorder above flood line; driveway camera recorder Staten Island; two-family camera system Staten Island; plate-capture camera Staten Island; strip-center NVR Hylan Boulevard; Richmond Avenue; Forest Avenue; Teleport; West Shore; St. George; Midland Beach; Rossville; Great Kills; New Dorp; Mariners Harbor; Annadale; Tottenville + §13 "we also serve" list. All 11 image alts/titles carry "NVR installation" + "Staten Island".

## Build notes
- check_page.py: every page-side check passes; the only remaining lines are 10 "live sibling … doesn't link back to /nvr-installation-staten-island" (brooklyn, dutchess-county, manhattan, nassau-county, orange-county, queens, rockland-county, suffolk-county, ulster-county, westchester-county) — main-run wiring.
- 13,112 rendered words; 181,080 B (Bronx 178,365 → +2,715; HV 183,846 → −2,766; LI 187,157; Putnam 190,430; old-template siblings 151–155 KB). Re-check sizes after the main run wires cross-links.
- Masked paragraph similarity (difflib, blocks ≥12 masked words): max vs Bronx 0.63 (block containing the mandated warranty sentence), HV 0.565, LI 0.58, Putnam 0.588; vs old-template Brooklyn 0.516 (earlier draft).
- §10.5 = 1,188 words (7 H3 × 3 paras). Field Notes 221 words. HowTo 7 steps = process 7 steps.
