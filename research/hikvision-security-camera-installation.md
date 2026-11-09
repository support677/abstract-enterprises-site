# Hikvision Security Camera Installation — silo research

Created 2026-10-18 by the REBUILD of `hikvision-security-camera-installation-long-island-ny` (Long Island hub). Format per blueprint v2.3 §12.4: **exact query · platform · URL · finding · page+section used**. Sources that could not be opened are written `EMPTY (not accessible in build env)`. Shell curl is blocked in the build environment; tools used: WebSearch, WebFetch, Firecrawl search (`mcp__Firecrawl__firecrawl_search`, excerpts) and Firecrawl scrape (`mcp__Fire_Crawl__firecrawl_scrape`, markdown / directQuote). Nothing below is invented; where only a search excerpt was seen, the entry says "excerpt".

Later area builds: reuse the silo findings, add only a `## <area>` section, and append your questions to the register at the bottom.

---

## 1. Source matrix (blueprint v2.3 §3, all 11 sources)

| # | Source | Status for this silo build |
|---|---|---|
| 1 | Reddit | Excerpts only via Firecrawl search (reddit.com cannot be scraped in full). Rows R1–R5 below. |
| 2 | Google People Also Ask | **EMPTY (not accessible in build env)** — no live Google SERP surface. |
| 3 | Google PASF | **EMPTY (not accessible in build env)**. |
| 4 | Answer the Public | **EMPTY (not accessible in build env)**. |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)**. The LI hub's §10.5 says so and tests seven claims commonly repeated in search summaries, retailer pages and forums against the primary sources below; it does not quote an AI Overview. |
| 6 | Area landmarks | Long Island section (carried, verified sources). |
| 7 | Area use cases / building stock | Long Island section (Census ACS carried). |
| 8 | Bing / DuckDuckGo | **EMPTY (not accessible in build env)** — one search backend per tool; no Bing/DDG related-search surface. |
| 9 | Local news | News 12 Long Island (2026), Nassau County PD news flash (2026), ABC7 (2024), CBS New York (2025), LIPA report (2020), DFS (2024). |
| 10 | Hyperlocal | Rep. Gillen press release (Garden City, Aug 2026); Garden City PD; SCPD camera registry; East Hampton Star (carried). Patch / LI Herald Hikvision-specific: **EMPTY** (no hit). |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** — no Yelp result surfaced for Long Island camera installers. |

---

## 2. Silo-wide findings — Hikvision regulation

### 2.1 FCC equipment authorization and the Covered List
| ID | Exact query · platform | URL | Finding | Used on LI page |
|---|---|---|---|---|
| F1 | `FCC 2025 Hikvision previously authorized equipment marketing prohibition order Covered List` · WebSearch → `FCC PS Docket 26-72 prohibit importation marketing previously authorized covered equipment Hikvision decision 2026` · Firecrawl search (excerpt) | https://docs.fcc.gov/public/attachments/DA-26-635A1.pdf | **DA 26-635, released June 26, 2026**, PS Docket 26-72 (PSHSB + OET): "prohibit the continued importation and marketing of certain previously authorized covered equipment added to the Covered List in 2024 or earlier"; "this prohibition will not affect the continued use or operation of already-purchased communications equipment"; the prohibition for *physical security surveillance of critical infrastructure* is **suspended** until the FCC adopts a definition of "critical infrastructure"; for use-based entries (Hikvision) import/marketing is prohibited only for public safety, government facilities, (suspended) critical infrastructure, and "other national security purposes". FCC states continued disagreement with Hikvision's argument that it lacks authority. | §5 para 2; §5.5; §9 cluster "2026 rules" H3 1–3; §10.5 H3 1–2; Sources |
| F2 | same · Firecrawl scrape (directQuote) | https://www.federalregister.gov/documents/2026/07/06/2026-13518/prohibiting-importation-and-marketing-of-previously-authorized-covered-communications-equipment | Federal Register July 6, 2026 (FR Doc 2026-13518): "this prohibition takes effect **July 16, 2026**"; "for any equipment that is 'covered' when used for certain purposes, the prohibitions on continued importation and marketing that we adopt in this Notice will not apply to importation and marketing for non-'covered' uses"; "consumers may continue to use any device or equipment that they currently possess, if the equipment was legally purchased and maintains an existing equipment authorization." | §5; §5.5; §9 H3 1–2; §10.5 H3 1–2; FAQ; Sources |
| F3 | `Hikvision ... Important Notice to Our Partners` · Firecrawl scrape (markdown) | https://www.hikvision.com/us-en/newsroom/latest-news/2026/Important-Notice-to-Our-Partners | Hikvision USA, **April 7, 2026**: FCC Public Notice **DA 26-294** (March 27, 2026) proposed the import/marketing prohibition; "the continued use or operation of any such equipment that is already in the hands of end users would not be prohibited"; Hikvision "filed a petition for judicial review" in **December 2025** challenging related FCC actions; comment period to May 6, 2026; Hikvision itself notes that limits on importation "could affect access to replacement parts, warranty service, and technical support". | §9 H3 "replacement camera"; §10.5 H3 2; Sources |
| F4 | `... understanding-the-fcc-s-regulatory-updates` · Firecrawl scrape (markdown) | https://www.hikvision.com/us-en/newsroom/latest-news/2026/understanding-the-fcc-s-regulatory-updates/ | Hikvision USA, **Sept 10, 2026**: notice effective July 16, 2026; Hikvision says it is "not a blanket ban"; advises dealers to apply a **Use Restriction Label** ("THIS PRODUCT IS SUBJECT TO USE PROHIBITIONS AND MAY NOT BE USED FOR PUBLIC SAFETY, SECURITY OF GOVERNMENT FACILITIES, PHYSICAL SECURITY SURVEILLANCE OF CRITICAL INFRASTRUCTURE AND OTHER NATIONAL SECURITY PURPOSES…"); FAQ: no requirement to remove installed products; **"public safety"** per n.42 = services of State/local government entities (or authorized non-governmental agencies) protecting life, health and property "including but not limited to police, fire, and emergency medical services"; **"government facilities"** per n.43 = federal, state, local and tribal government buildings incl. general-use office buildings, courthouses etc.; Hik-Connect "is a software service and is not itself subject to equipment authorization, so it is not affected" (vendor statement); Hikvision USA says sales, technical support and warranty continue in the US for non-covered uses. | §8.5; §9 H3 "fire district / village hall"; §9 H3 "Hik-Connect"; FAQ; §10.5 H3 3; Sources |
| F5 | `FCC 2025 Hikvision…` · WebSearch → WebFetch | https://docs.fcc.gov/public/attachments/FCC-26-50A1.txt | FCC 26-50, Third Report and Order, adopted July 22 / released **July 23, 2026**, ET Docket 21-232: new logic-bearing-component rule is prospective and "does not affect previously authorized equipment"; previously authorized equipment "may not be modified in a manner that would render it covered equipment"; marketing rules reach "ecommerce platforms"; platforms must display FCC IDs at online point of sale. Section III.F (revised critical-infrastructure definition) could not be located in the fetched text → **not used**. | §10.5 H3 "online kit"; §9 H3 rebrand/FCC ID; Sources |
| F6 | `Hikvision USA v. FCC D.C. Circuit 2024 decision covered list critical infrastructure remand` · WebSearch → WebFetch | https://cooley.com/news/insight/2024/2024-04-09-court-instructs-fcc-to-amend-definition-of-critical-infrastructure-in-equipment-authorization-order | Cooley, Apr 9 2024: D.C. Circuit (No. 23-1032) upheld the bar on authorization of Hikvision/Dahua equipment for covered uses and held the Secure Equipment Act ratified the Covered List; vacated the "critical infrastructure" definition as "arbitrarily broad" and remanded. | §9 H3 1; §10.5 H3 1; Sources |
| F7 | carried from research/dahua-camera-installation.md (fetched 2026-10-18) | https://www.globalsecurity.org/intell/library/news/2022/intell-221125-fcc01.htm | FCC news release Nov 25, 2022 (mirror): Hikvision/Dahua barred from new authorizations; rules apply "to future authorizations". | §5.5 timeline; Sources |

### 2.2 NDAA FY2019 Section 889 and federal grants
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| N1 | `2 CFR 200.216 prohibition video surveillance Hikvision federal grant funds Nonprofit Security Grant Program` · WebSearch → WebFetch | https://www.law.cornell.edu/cfr/text/2/200.216 | 2 CFR 200.216(a): recipients/subrecipients may not use loan or grant funds to procure, obtain, extend or renew contracts for covered telecommunications equipment or services; (b)(2): "For the purpose of public safety, security of government facilities, physical security surveillance of critical infrastructure, and other national security purposes, video surveillance and telecommunications equipment produced by … Hangzhou Hikvision Digital Technology Company, or Dahua Technology Company". | §8.5; §9 H3 "grant-funded house of worship"; §10.5; Sources |
| N2 | `Nonprofit Security Grant Program Long Island synagogues churches security cameras grant Nassau Suffolk 2025` · Firecrawl search → scrape (directQuote) | https://gillen.house.gov/media/press-releases/rep-gillen-delivers-over-2-million-new-federal-security-funding-houses-worship | Aug 17, 2026, Garden City: eleven faith-based institutions in NY-04 awarded more than $2 million in NSGP funding; "Each institution will receive nearly $200,000 for safety enhancements, such as physical barriers, security cameras and contracted security personnel"; named recipients include St. John's Baptist Church of Inwood, Young Israel of Woodmere, HALB DRS Yeshiva High School. | §5 para 3; §5.5; §8 houses-of-worship card; §9 H3 grant; Sources |
| N3 | same search (excerpts) | https://www.governor.ny.gov/news/governor-hochul-announces-32-million-federal-funding-strengthen-security-nonprofits-facing ; https://www.jcrcny.org/security-grant-faqs/ | Governor: $32 million federal NSGP funding to NY nonprofits; nationwide $274.5 million in FY2025 (excerpt). JCRC-NY FAQ (excerpt): "Nassau, Suffolk & Westchester are eligible. Funding can be used for the acquisition and installation of security equipment … cameras". | §9 H3 grant (excerpt-level, figures not restated beyond the excerpt) |
| N4 | carried from research/dahua-camera-installation.md | https://www.research.ucsb.edu/export-control/NDAA-889 | Part B effective Aug 13, 2020; bars federal contracts with entities that *use* covered equipment; "many consumer video surveillance systems are rebranded products from one of the prohibited companies". | §8 Route 110/Hauppauge card; §9 H3 contractor; §9 H3 rebrand; Sources |

### 2.3 Other governments (context)
| ID | Query · platform | URL | Finding | Used |
|---|---|---|---|---|
| G1 | `Canada orders Hikvision to cease operations June 2025 Investment Canada Act` · WebSearch → WebFetch | https://www.securityinfowatch.com/video-surveillance/article/55300419/canada-orders-hikvision-to-cease-operations-cites-national-security-concerns | June 28, 2025: Minister Mélanie Joly ordered Hikvision Canada to cease operations after an Investment Canada Act review; federal bodies barred from procuring/using Hikvision; directive "does not explicitly bar private citizens from purchasing Hikvision products". | §10.5 H3 "everywhere is banning it"; Sources |

### 2.4 Security advisories / exploited vulnerabilities
| ID | Query · platform | URL | Finding | Used |
|---|---|---|---|---|
| V1 | `CISA Known Exploited Vulnerabilities Hikvision CVE-2021-36260 command injection` · WebSearch → WebFetch | https://www.sentinelone.com/vulnerability-database/cve-2021-36260/ | CVE-2021-36260: command injection in the web server of many Hikvision products, unauthenticated RCE as root; CVSS 9.8; published Sept 22, 2021; affects DS-2CD IP cameras, PTZs, some DS-7xxx recorders etc.; fix = vendor firmware; restrict network access. | §9 H3 "old recorder exposed"; Field Notes; §5.5; Sources |
| V2 | same · WebFetch | https://stack.watch/vuln/CVE-2021-36260 | Listed in CISA KEV; federal remediation due **January 24, 2022** ("Apply updates per vendor instructions"). Date added not shown → page states the due date only. | §5.5; §9 H3; Sources |
| V3 | `CISA KEV Hikvision CVE-2017-7921 CVE-2021-36260 dateAdded` · Firecrawl search (excerpts) | https://www.cisa.gov/known-exploited-vulnerabilities-catalog (vendor filter) ; https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html | CVE-2017-7921 (Hikvision improper authentication) **added to KEV March 5, 2026**, federal due date March 26, 2026; THN headline: "CVSS 9.8". Hikvision's own notice page: https://www.hikvision.com/us-en/support/document-center/special-notices/privilege-escalating-vulnerability-in-certain-hikvision-ip-cameras/ (excerpt: CVE-2017-7921/7923, "attackers could obtain an unauthorized escalated additional user privilege"). | §5.5; §9 H3; §10.5 H3 "old firmware is fine"; Sources |
| V4 | `Hikvision security advisory 2025 vulnerability HikCentral OR camera firmware CVE-2025 Hikvision` · WebSearch → WebFetch | https://securityaffairs.com/181896/hacking/severe-hikvision-hikcentral-product-flaws-what-you-need-to-know.html | Sept 4, 2025: CVE-2025-39245 (HikCentral Master Lite, CSV injection, 4.7), CVE-2025-39246 (HikCentral FocSign, unquoted service path, 5.3), CVE-2025-39247 (HikCentral Professional access-control flaw, 8.6 — unauthenticated user could obtain admin permission; fixed V2.6.3 / V3.0.1). | §8 multi-site card; §9 H3 HikCentral; Sources |
| V5 | same search (excerpt) | https://www.hikvision.com/ca-en/support/cybersecurity/security-advisory/partner-letter-re-security-vulnerabilities-in-some-hikvision-dvr | Hikvision partner letter on vulnerabilities in some DVR products (excerpt, title only) → not quoted. | — |

### 2.5 Product lines
| ID | Query · platform | URL | Finding | Used |
|---|---|---|---|---|
| P1 | `Hikvision ColorVu AcuSense TandemVu explained official hikvision.com` · WebSearch → Firecrawl scrape (directQuote) | https://www.hikvision.com/us-en/newsroom/latest-news/2022/Hikvision-Introduces-TandemVu-PTZ-Cameras-with-ColorVu-Technology- | Apr 26, 2022: TandemVu PTZ = 4 MP fixed bullet (4 mm) + 4 MP PTZ in one unit; models with 32x (DS-2SE7C432MW-AEB) or 42x (DS-2SF8C442MXS-DLW) optical zoom; strobe and audio alarm speaker; "ideal for parking lots, crosswalks, industrial parks"; ColorVu "for full-color imaging in a variety of lighting conditions, including darkness"; AcuSense "precise detection and classification of humans and vehicles, reducing false alarms by up to 90%" (vendor claim). | §6; §9 cluster "lines"; §10 cards; §10.5 H3 "90%"; Sources |
| P2 | `Hikvision ColorVu technology F1.0 aperture warm supplemental light official` · Firecrawl search (excerpt) | https://www.hikvision.com/us-en/core-technologies/low-light-imaging/colorvu/ ; https://www.hikvision.com/us-en/products/network-products/network-cameras/colorvu-series/ | "F1.0 Super Aperture and advanced sensor ensure excellent color imaging in ultra-low light"; varifocal ColorVu keeps a fixed F1.0 aperture while zooming. | §9 H3 ColorVu vs IR; §10 |
| P3 | `Hikvision AcuSense technology human vehicle classification false alarm official us-en` · Firecrawl search (excerpt) | https://www.hikvision.com/en/core-technologies/see-smarter-technology/acusense/ ; https://www.hikvision.com/us-en/core-technologies/ai-analytics/acusense/ | AcuSense embeds deep-learning algorithms in select cameras and recorders to "automatically detect humans and vehicles" and push notifications; US page: "configuration-free function is ON by default". | §9 H3 AcuSense; §10 |
| P4 | WebFetch | https://www.securitywholesalers.com.au/guides/hikvision/hikvision-camera-series-explained/ | Reseller labels: "Hybrid ColorVu (has both infrared and light capabilities)"; AcuSense "(with AI Human & Vehicle detection / Strobe + Speaker)". | §9 H3 ColorVu vs IR (labelled as reseller description) |
| P5 | `Hikvision anti-corrosion camera salt spray C5-M stainless 316L coastal series` · Firecrawl search (excerpts) | https://www.hikvision.com/en/products/IP-Products/Explosion-Proof---Anti-corrosion-Series/ | "Housed in advanced polymer material or marine-grade stainless steel, Hikvision's anti-corrosion cameras offer superior defense against salts…"; Hikvision HQ posts mention 316L anti-corrosion bullets (excerpt). No C5-M rating found → not claimed. | §7 South Shore card; §10 card (body text only — coastal *question* is owned by older pages) |

### 2.6 Aggregator / forum claims (for §10.5)
| ID | Query · platform | URL | Finding | Used |
|---|---|---|---|---|
| A1 | carried from research/dahua-camera-installation.md | https://www.angi.com/articles/how-much-does-it-cost-install-surveillance-camera/ny/new-york | Angi New York average $1,509, typical $797–$2,222 (Mar 2026 excerpt). | §10.5 H3 cost |
| A2 | carried | https://www.homeadvisor.com/cost/safety-and-security/install-a-surveillance-camera/ | HomeAdvisor national average $1,289 ($589–$2,040); labor $80–$200 per camera. | §10.5 H3 cost |

### 2.7 Reddit (silo)
| ID | Query · platform | URL | Finding (excerpt only) | Used |
|---|---|---|---|---|
| R1 | `site:reddit.com longisland security cameras hikvision installer` · Firecrawl search | https://www.reddit.com/r/longisland/comments/1h8ygon/what_cameraalarm_system_do_you_use_andor/ | r/longisland: "Hikvision. Amazon has a kit with 4 cameras and a NVR. Use ivms4500 app. Requires hardwiring and configuration but is well worth it." | §5 para 1 (paraphrased as a resident's reply); §9 H3 DIY-kit takeover |
| R2 | same | https://www.reddit.com/r/longisland/comments/1cn1pcu/security_system_suggestions/ | r/longisland reply: "Hikvision makes some of the highest quality cameras available right now." | §5 para 1 |
| R3 | same | https://www.reddit.com/r/videosurveillance/comments/1c8ep2z/help_bought_a_house_with_hikvision_cameras/ | Title: "[HELP] Bought a house with Hikvision cameras"; a reply suggests port forwarding and dynamic DNS. | §9 H3 inherited system; §10.5 H3 port forwarding |
| R4 | same | https://www.reddit.com/r/homedefense/comments/1erdshr/quoted_3750_for_4_poe_cameras_and_1_doorbell/ | "Hikvision is fine if you run them on a separate network and change the defaults and turn off a bunch of call home stuff." | §9 H3 hardening |
| R5 | same | https://www.reddit.com/r/homesecurity/comments/15t7puq/how_much_should_it_cost_to_install_5_cameras_av/ | Title "How much should it cost to install 5 cameras? AV company wants 1500…" (UK pricing in excerpt) | not used (not LI, mixed currency) |

### 2.8 Keywords — five layers (silo)
- **Service:** Hikvision camera installation, Hikvision installer, Hikvision NVR setup, Hikvision system takeover, Hikvision firmware update service, Hik-Connect setup, Hikvision camera replacement, Hikvision to Uniview / Ubiquiti migration, Hikvision PTZ installation.
- **Problem:** FCC Covered List, NDAA 889 compliance, grant compliance, exploited vulnerabilities (CVE-2021-36260, CVE-2017-7921), inherited system, port-forwarded recorder, false alerts, power outage recording, footage export for police, spare parts supply.
- **Technology:** ColorVu, AcuSense, TandemVu, DarkFighter (named only as Hikvision newsroom topic), PoE, NVR, ONVIF, Hik-Connect, iVMS-4500 / iVMS-4200, HikCentral, varifocal, PTZ, anti-corrosion housings, UPS.
- **Industry:** homeowners, landlords of two-family houses, retail strips, flex/industrial and defense suppliers, houses of worship with NSGP grants, fire districts and village halls (excluded), HOAs/condos, marinas.
- **Geographic (LI page):** Long Island, Nassau, Suffolk, Hempstead, Levittown, Garden City, Mineola, New Hyde Park, Inwood, Woodmere, Massapequa, Hicksville, Route 110, Melville, Farmingdale, Hauppauge, Ronkonkoma, Lindenhurst, Bay Shore, Patchogue, Riverhead, Stony Brook, East End.

---

## 3. Pricing (silo; §9 multipliers) — no invented prices

Base = the live Brooklyn Hikvision page (`hikvision-security-camera-installation-brooklyn-ny.html`, pre-rebuild): roughly **$400–$700 per camera installed**; tiers **Small $1,800–$3,500** (4–6 cameras), **Mid $3,500–$8,000** (8–16 cameras), **Large / Commercial $8,000+**. Service/callback rate (blueprint §9, protected): **$195/hr, 3-hour minimum ($585)**.

| Line | Brooklyn 1.00× | Nassau 1.15× | Suffolk 1.20× |
|---|---|---|---|
| Per camera installed | $400–$700 | $460–$805 | $480–$840 |
| Small, 4–6 cameras | $1,800–$3,500 | $2,070–$4,025 | $2,160–$4,200 |
| Mid, 8–16 cameras | $3,500–$8,000 | $4,025–$9,200 | $4,200–$9,600 |
| Large / commercial | $8,000+ | $9,200+ | $9,600+ |

Used on the LI hub §14/§15 (both counties side by side, arithmetic shown). BYOE labor-only: no silo price exists → page says "quoted per camera after the walkthrough" (no number invented).

**FLAGS (inconsistencies in the live silo):**
- Old Nassau page: $480–$800 per camera, Basic $2,000–$3,800 — neither matches 1.15× ($460–$805; $2,070–$4,025).
- Old Suffolk page: $480–$850, Basic $2,200–$4,200, Estate $10,000+ — 1.20× gives $480–$840 and $9,600+.
- Old LI hub: $480–$850, Basic $2,200–$4,000, Estate $9,000+ — mixed; replaced by the table above.
- NYC hub and Queens use the Brooklyn numbers unchanged (Queens should be 1.05×; Manhattan 1.25× not checked).

---

## Long Island

Thesis of the LI hub: on Long Island in late 2026 most Hikvision work is about systems already on the house or the store. Since the FCC's July 16, 2026 import/marketing prohibition (covered uses only) and the authorization freeze since 2022, the honest job is to decide, camera by camera, whether to **keep, harden, extend or replace** — and to know which Long Island buildings (fire districts, village halls, grant-funded houses of worship, federal contractors on Route 110 and in Hauppauge) should not get new Hikvision at all. Nassau (older, tighter post-war lots) and Suffolk (newer, wider lots, coastal and seasonal) change the answer.

### LI-1 Building stock and geography (carried, verified)
| ID | Query · platform | URL | Finding | Used |
|---|---|---|---|---|
| L1 | carried from research/dahua-camera-installation.md (Firecrawl Alexandria census-gov, ACS 5-yr 2023) | https://api.census.gov/data/2023/acs/acs5 | Nassau 477,860 housing units, 364,529 one-unit detached, median year built 1955; Suffolk 579,790 units, 463,095 detached, median year built 1970. | §5 para 2; §5.5; §7 cards |
| L2 | carried | https://www.ny.gov/counties/nassau ; https://www.ny.gov/counties/suffolk | Nassau: two cities, three towns, 64 incorporated villages, 60+ hamlets, ~453 sq mi. Suffolk: ten towns, ~2,373 sq mi. | §5; §8.5 |
| L3 | carried | https://kerimurrayarchitecture.com/levittown-ny/ | 17,447 Levittown homes built 1947–1951, many ranches on concrete slabs. | §7 slab-ranch card; §13 |
| L4 | carried | https://www.census.gov/quickfacts/nassaucountynewyork ; https://www.newsday.com/long-island/population-gains-losses-long-island-c19872 | 2020 Census: Nassau 1,395,774; Suffolk 1,525,920 (excerpts). | §5.5 |

### LI-2 Local news / police / incidents
| ID | Query · platform | URL | Finding | Used |
|---|---|---|---|---|
| LN1 | `Nassau County police 2026 home burglaries surveillance video arrests Long Island Newsday OR News12` · Firecrawl search (excerpt) | https://www.pdcn.org/CivicAlerts.aspx?AID=15190 | Nassau County PD news flash (2026): detectives say a defendant entered multiple residences across Nassau between **July 11, 2025 and May 23, 2026** and removed jewelry; arrested in New Hyde Park. (Defendant not named on page.) | §5 para 3; §5.5 |
| LN2 | same (excerpt) | https://longisland.news12.com/2026/08/26/he-wasnt-aware-of-the-eyes-up-above-police-drone-helps-catch-lindenhurst-home-burglary-suspect/7uEkpEC3mtZ7JH2P3YLlRT | News 12, Aug 26 2026: police drone helped catch a Lindenhurst home-burglary suspect on Kings Avenue. | §5 para 3 |
| LN3 | same (excerpt) | https://longisland.news12.com/homeowners-asked-to-check-home-security-video-after-string-of-nassau-county-break-ins | News 12 headline: "Homeowners asked to check home security video after string of Nassau County break-ins" (undated excerpt). | §9 H3 export for police |
| LN4 | carried | https://abc7ny.com/post/nassau-county-police-task-force-burglaries-long-island/14337932/ | Jan 2024 multi-agency burglary/stolen-car task force; burglars "attracted by cars in people's driveways". | §5 para 3 |
| LN5 | carried | https://www.cbsnews.com/newyork/news/suffolk-county-porch-pirate-ring/ | Nov 2025: Suffolk DA charged 14 men; 200+ phones/tablets stolen from porches in 31 communities. | §5.5 |
| LN6 | carried | https://scpdshield.org/Initiatives | SCPD Camera Registry Program — owners register locations; retrieval at owner's convenience. | §9 H3 police export |
| LN7 | carried | https://gardencitypolice.net/private-camera-reg | Garden City PD voluntary Private Camera Registration; "does NOT provide us access". Nassau County-wide registry: EMPTY. | §9 H3 police export |
| LN8 | `Hikvision cameras Long Island school district OR Suffolk County OR Nassau County removed replaced Chinese cameras` · Firecrawl search | (results: school speed-camera repeal, Bay Shore HS hidden camera) | **EMPTY** — no Long Island news found about Hikvision removal by a county, town or district. Page makes no such claim. | — |

### LI-3 Power / weather / coast (carried)
| ID | URL | Finding | Used |
|---|---|---|---|
| W1 | https://www.lipower.org/wp-content/uploads/2020/09/LIPA-Isaias-30-Day-Report-Final.pdf | Isaias Aug 4 2020: ~645,000 customer outages; full restoration took eight days. | §9 H3 UPS; §5.5 |
| W2 | https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20240823 | Aug 18–19 2024: first-ever flash flood emergency for Suffolk; Stony Brook Mill Pond dam failed. | §7 basement card; FAQ recorder location; §13 |
| W3 | https://en.wikipedia.org/wiki/Effects_of_Hurricane_Sandy_in_New_York | Long Beach ~$150 million damage. | §7 South Shore card |

### LI-4 Licensing / permits
| ID | URL | Finding | Used |
|---|---|---|---|
| K1 | carried: https://dos.ny.gov/system/files/documents/2024/05/security_0.pdf | 19 NYCRR §195.2(b)(1): NYS DOS licence required for work on a CCTV / video surveillance system used to detect or monitor intrusion, theft etc. (GBL Art. 6-D). | §8.5; Sources |
| K2 | carried: https://www.nassaucountyny.gov/1563/Licensing-Registrations | Nassau Office of Consumer Affairs home-improvement licensing (fingerprinting). Which camera jobs need it: EMPTY → page says check per job. | §8.5 |
| K3 | carried: https://ecode360.com/14948079 ; https://www.suffolkcountyny.gov/Portals/0/formsdocs/labor/code.pdf | Suffolk Ch. 563 licensing via Office of Consumer Affairs (towns/villages with own licensing carved out); "Communication Cable Installer" restricted licence covers cabling of 90 V or less incl. audio/video systems; line-voltage reserved to master electricians. | §8.5 |
| K4 | carried: https://newyork-811.com/homeowners/ | Call 811 at least 48 hours before digging. | §7.5 trench note |

### LI-5 Corridors / landmarks (carried, sources fetched by earlier LI runs)
Roosevelt Field / Old Country Road (Wikipedia); Long Island Innovation Park at Hauppauge (~1,350 businesses, ~11 sq mi); Route 110 corridor Farmingdale–Melville–Huntington Station (iraceenterprises.com); Ronkonkoma Hub / Station Yards 53 acres (governor.ny.gov); Stony Brook University (213 buildings / 1,454 acres); The Shops at Riverhead / Route 58 (brixmor.com); Levittown (above). Used: §8, §13.

### LI-6 Reddit r/longisland — see R1, R2 above. Local-sub threads about Hikvision removal or FCC: EMPTY.

### LI-7 House practices stated without an external source (FLAG for Anwar)
- Keeping a spare camera or two of the installed model on the shelf for multi-camera Hikvision sites.
- Not installing new Hikvision at fire districts, village/town buildings, police-adjacent sites, grant-funded projects or federal-contractor premises (AESS policy, stated as policy, legal text cited separately; "not legal advice").
- Separate camera VLAN / recorder off the main LAN, UPnP and P2P decisions, removing port forwards (installer practice; R4 forum view as support).
- UPS sizing in hours, putting the modem on the same UPS.
- Moving recorders off basement floors in flood-prone areas.

---

## 4. Question register (every FAQ / Q&A / "?" heading on every existing hikvision-security-camera-installation-*.html page)

Extracted 2026-10-18 with tools/check_page.py's parser (`.faq-question` + h2/h3/summary ending in "?"). Count = number of pages carrying the identical question.

### Asked on all or most pages (generic template intents — never reuse)
- (16 pages) Why is my Hikvision camera offline or not recording? · How long does Hikvision footage stay recorded? · Are you licensed and insured? · Do you service Hikvision systems you didn’t install? · How do I get started?
- (15) Do you offer a warranty? · Will it work without internet?
- (12) Can I add more cameras later?
- (10) How much does it cost?
- (8) Can cameras avoid recording a neighbor’s property?
- (5) What resolution do you recommend? · Do Hikvision cameras handle snow and ice? · Can you handle long rural cable runs?
- (4) Do I need to post that the building is recorded? (bronx, manhattan, rockland, westchester) · Do you provide board documentation? (bronx, brooklyn, rockland, westchester) · Can you place cameras discreetly on a historic home? (dutchess, putnam, rockland, westchester) · Are the cameras built for upstate winters? (dutchess, hudson-valley, orange, putnam)
- (3) Can the building manager and owner both view the cameras? (bronx, rockland, westchester) · Do Hikvision cameras work in winter? (bronx, rockland, westchester) · Do you cover full estate perimeters? (dutchess, rockland, westchester) · Do you cover the full property perimeter? (hudson-valley, long-island [old], orange) · Are the cameras weatherproof for the coast? (long-island [old], nassau, suffolk)
- (2) Do Hikvision cameras work in the cold? (brooklyn, queens) · Can you handle long cable runs to outbuildings? (long-island [old], suffolk) · Can you set up a seasonal/vacation home? (long-island [old], putnam) · Do you install for businesses too? (long-island [old], staten-island) · Do you integrate Hikvision with access control or alarms? (manhattan, nyc) · Is there a warranty? (manhattan, nyc) · How many Hikvision cameras do I need? (manhattan, nyc) · Can Hikvision cameras record audio? (manhattan, nyc) · What internet speed do Hikvision cameras need? (manhattan, nyc) · Do you cover the full home perimeter? (nassau, staten-island) · Can you handle a condo or co-op board? (rockland, westchester) · Can I view my property from anywhere? (rockland, westchester) · Do you cover apartment and condo buildings? (rockland, westchester)

### Per-page questions (one page each)
- **bronx-ny:** How much does Hikvision camera installation cost in the Bronx? · Is Hikvision good value for a Bronx apartment building? · Are you a local Bronx installer? · Can you handle a co-op or condo board approval? · Can I install Hikvision myself in my Bronx building? · Which Hikvision camera is best for an apartment lobby? · Is Hikvision legal to install in the Bronx? · Ready for Hikvision in your Bronx property? · How many cameras does a Bronx apartment building need? · Can I view the cameras from my phone? · Are you a local Bronx company? · What areas of the Bronx do you cover? · Do you cover apartment lobbies and vestibules? · Do you install for bodegas and restaurants?
- **brooklyn-ny:** How much does Hikvision camera installation cost in Brooklyn? · Is Hikvision cheaper than the premium brands? · Can you install on a brownstone without damaging the brick? · Do you handle co-op and condo board approvals? · Can I install Hikvision myself on my Brooklyn house? · Which Hikvision camera is best for a brownstone? · Are wired PoE cameras better than wireless in Brooklyn? · Is Hikvision legal to install in Brooklyn? · Do I need to post that my business is recorded? · Ready for Hikvision in your Brooklyn property? · How many Hikvision cameras does a brownstone need? · Can I view my Brooklyn cameras from work or vacation? · Do you follow Landmarks rules in historic districts? · Wired or wireless for my Brooklyn property? · Do you cover all Brooklyn neighborhoods?
- **dutchess-county-ny:** How much does … in Dutchess County? · Why does a Dutchess estate cost more to cover? · Can you cover a farm or equestrian property? · Can I install Hikvision myself on my Dutchess home? · Which Hikvision cameras are best for a Dutchess property? · Do the cameras hold up in Dutchess winters? · Is Hikvision legal to install in Dutchess County? · Ready for Hikvision on your Dutchess property? · How many cameras does a Dutchess home need? · Can I view my Dutchess home from anywhere? · What areas of Dutchess County do you cover? · Do you cover farms and equestrian properties?
- **hudson-valley-ny:** How much does … in the Hudson Valley? · Why does a Hudson Valley property cost more than a city apartment? · Do you cover all six Hudson Valley counties? · Can you cover a wooded or rural property? · Can I install Hikvision myself on my Hudson Valley home? · Which Hikvision cameras are best for a Hudson Valley property? · Do the cameras hold up in Hudson Valley winters? · Is Hikvision legal to install in the Hudson Valley? · Ready for Hikvision on your Hudson Valley property? · How many cameras does a Hudson Valley home need? · Can I view my Hudson Valley home from anywhere? · Do you cover all of the Hudson Valley? · Can you handle a historic or estate home?
- **long-island-ny (OLD version, replaced by this rebuild):** How much does … on Long Island? · Why does a Long Island home cost more than a city apartment? · Do you cover both Nassau and Suffolk? · Can you secure a seasonal or vacation home? · Can I install Hikvision myself on my Long Island home? · Which Hikvision cameras are best for a large lot? · Wired or wireless for a large Long Island property? · Is Hikvision legal to install on Long Island? · Ready for Hikvision on your Long Island property? · How many cameras does a Long Island home need? · Can I watch my Long Island home from the city or while away? · Do Hikvision cameras handle coastal weather? · Do you cover all of Long Island?
- **manhattan-ny:** How much does … in Manhattan? · Why does a Manhattan install cost more than the outer boroughs? · Can you get a co-op or condo board to approve the install? · Will you damage the walls in my pre-war building? · Can I install Hikvision myself in my Manhattan apartment? · Which Hikvision camera is best for a high-rise lobby? · Can the doorman and the board both view the cameras? · Is Hikvision legal to install in Manhattan? · Ready for Hikvision in your Manhattan building? · Do you provide board documentation for co-op/condo approval? · Will the cabling be hidden? · Can you cover lobbies, elevators, and garages? · Do you also cover the other boroughs?
- **nassau-county-ny:** How much does … in Nassau County? · Why does a Nassau home cost more than a city apartment? · Can you cover a North Shore estate? · Can you mount on vinyl, stucco, or cedar shake siding? · Can I install Hikvision myself on my Nassau home? · Which Hikvision cameras are best for a Nassau home? · Wired or wireless for a Nassau property? · Is Hikvision legal to install in Nassau County? · Ready for Hikvision on your Nassau property? · How many cameras does a Nassau home need? · Can I view my Nassau home from anywhere? · Do Hikvision cameras handle Nassau winters and coast? · What areas of Nassau do you cover? · Can you handle a North Shore estate? · Can you mount on vinyl or stucco siding?
- **nyc:** Why Choose Hikvision Security Cameras? · How much does … in NYC? · Is Hikvision cheaper than other camera brands? · Are Hikvision cameras good? · Can Hikvision cameras be viewed on a phone? · Can I install Hikvision cameras myself? · Which Hikvision camera is best for a warehouse? · I forgot my Hikvision password — can it be reset? · Why does my night footage look blurry or washed out? · Is Hikvision banned in the US? · Do I need to notify people they’re being recorded? · Ready for a Hikvision system in NYC? · Do you install Hikvision in all five boroughs? · What are the best Hikvision cameras for apartment buildings? · Can you upgrade my old cameras to Hikvision? · Will my Hikvision system work without internet?
- **orange-county-ny:** How much does … in Orange County? · Why does a rural Orange County property cost more to cover? · Can you cover a rural or wooded property? · Can you cover a farm or agricultural property? · Can I install Hikvision myself on my Orange County home? · Which Hikvision cameras are best for a large Orange County lot? · Do the cameras hold up in Orange County winters? · Is Hikvision legal to install in Orange County? · Ready for Hikvision on your Orange County property? · How many cameras does an Orange County home need? · Can I view my Orange County home from anywhere? · What areas of Orange County do you cover? · Do you cover farms and agricultural properties? · Is Hikvision OK near West Point?
- **putnam-county-ny:** How much does … in Putnam County? · Is it worth it in such a safe county? · Can you secure a lakefront or seasonal home? · Can I install Hikvision myself on my Putnam home? · Which Hikvision cameras are best for a Putnam property? · Do the cameras hold up in Putnam winters? · Is Hikvision legal to install in Putnam County? · Ready for Hikvision on your Putnam property? · How many cameras does a Putnam home need? · Can I watch my Putnam lake home from anywhere? · What areas of Putnam County do you cover? · Do you cover lakefront properties?
- **queens-ny:** How much does … in Queens? · Is Hikvision a good value for a small business? · Do you serve all Queens neighborhoods? · Can you handle a Forest Hills co-op’s HOA requirements? · Can I install Hikvision myself on my Queens home? · Which Hikvision camera is best for a storefront? · Can I watch my Queens store from home on my phone? · Is Hikvision legal to install in Queens? · Do I need to post that my store is recorded? · Ready for Hikvision in your Queens property? · How many cameras does a Queens home need? · Can multiple people view the cameras? · What areas of Queens do you cover? · Do you cover home driveways and yards? · Do you install for small businesses and restaurants? · Wired or wireless for my Queens property? · Do you provide co-op board documentation?
- **rockland-county-ny:** How much does … in Rockland? · Is Hikvision good value for a Rockland estate? · Can I install Hikvision myself on my Rockland home? · Which Hikvision cameras are best for a Rockland estate? · Is Hikvision legal to install in Rockland? · Ready for Hikvision on your Rockland property? · How many cameras does a Rockland home need? · What areas of Rockland do you cover?
- **staten-island-ny:** How much does … on Staten Island? · Why does a Staten Island home need more cameras? · Can you cover a large hillside lot with a long driveway? · Will the cameras survive coastal weather and storms? · Can I install Hikvision myself on my Staten Island home? · Which Hikvision cameras are best for a house perimeter? · Wired or wireless for a Staten Island home? · Is Hikvision legal to install on Staten Island? · Can my cameras see the property line without invading a neighbor’s privacy? · Ready for Hikvision on your Staten Island property? · How many cameras does a Staten Island house need? · Can I view my home from work or vacation? · Do Hikvision cameras handle snow and coastal weather? · What areas of Staten Island do you cover? · Can you handle long cable runs on a big lot? · Are the cameras weatherproof? · Can you avoid recording my neighbor’s property?
- **suffolk-county-ny:** How much does … in Suffolk County? · Why does a Suffolk property cost more to cover? · Can you secure a Hamptons or seasonal home? · Can you cover a winery, farm, or marina? · Can I install Hikvision myself on my Suffolk property? · Which Hikvision cameras are best for a big Suffolk lot? · Wired or wireless for a large Suffolk property? · Is Hikvision legal to install in Suffolk County? · Ready for Hikvision on your Suffolk property? · How many cameras does a Suffolk property need? · Can I watch my Suffolk home from the city or while away? · Do Hikvision cameras handle the East End coast? · What areas of Suffolk do you cover? · Do you cover large lots and estates? · Can you set up a Hamptons/seasonal home? · Do you cover wineries, farms, and marinas?
- **ulster-county-ny:** How much does … in Ulster County? · Why does a mountain property cost more to cover? · Can you work with historic-home preservation rules? · Can you secure a weekender second home? · Can I install Hikvision myself on my Ulster home? · Which Hikvision cameras are best for an Ulster property? · Do the cameras hold up in Catskills winters? · Is Hikvision legal to install in Ulster County? · Ready for Hikvision on your Ulster property? · How many cameras does an Ulster home need? · Can I watch my Ulster second home from the city? · What areas of Ulster County do you cover? · Do you cover mountain and wooded properties? · Can you work with historic-preservation rules? · Can you set up a weekender second home? · Are the cameras built for Catskills winters?
- **westchester-county-ny:** How much does … in Westchester? · Is Hikvision good value for a Westchester estate? · Can I install Hikvision myself on my Westchester home? · Which Hikvision cameras are best for a Westchester estate? · Is Hikvision legal to install in Westchester? · Ready for Hikvision on your Westchester property? · How many cameras does a Westchester home need? · What areas of Westchester do you cover?

### hikvision-security-camera-installation-long-island-ny (REBUILD 2026-10-18) — new questions
See section 5 (filled in after the page was written).

## 5. Question register — hikvision-security-camera-installation-long-island-ny (REBUILD 2026-10-18)

§9 Questions Answered (H3) and other headings ending in '?':
1. Hikvision Recorder Beeping or Cameras Dark on Long Island?
2. Can AESS still get brand-new Hikvision cameras for a Long Island house after the FCC's July 2026 order?
3. Which Long Island buildings count as a “covered use” where new Hikvision is off the table?
4. Our synagogue or church won a Nonprofit Security Grant. Can that money pay for Hikvision cameras?
5. We supply parts to a federal agency from a building on Route 110. What does Section 889 mean for the cameras in our own warehouse?
6. Will the Hik-Connect app keep working on our phones after the FCC's action?
7. If one of our Hikvision cameras dies next year, how do we replace it if spares get scarce?
8. Our Hikvision system is eight years old and still records. What would make replacing it worth the money now?
9. The new Hikvision box has a “use restriction” label. Does that mean the camera is unsafe for our house?
10. How often should a Long Island Hikvision recorder be checked for firmware updates?
11. How do we find out whether our recorder is one of the models hit by the exploited Hikvision flaws?
12. What should be turned off on a Hikvision recorder that can be reached from the internet?
13. We bought a house in Massapequa that came with Hikvision cameras. What should we check before trusting the recordings?
14. How can we tell whether a no-name camera kit is really Hikvision under another label?
15. Can new non-Hikvision cameras record to our Hikvision NVR, or our Hikvision cameras to a new recorder?
16. Can the cameras be stopped from contacting outside servers while the phone app keeps working?
17. Our gated condo community in Suffolk has Hikvision at the gatehouse. Does the 2026 rule reach a private HOA?
18. We switched internet providers and our Hikvision cameras vanished from the app. What happened?
19. Should a two-family house have one Hikvision recorder or two?
20. Should a Nassau street with streetlights get ColorVu, and an unlit Suffolk lane get infrared?
21. Will AcuSense stop alerts from headlights and trees on a road like Sunrise Highway?
22. When does a TandemVu PTZ earn its price at a Long Island business lot?
23. How long will a Hikvision NVR on a battery keep recording when PSEG Long Island loses power?
24. Nassau or Suffolk detectives asked neighbours for video. How do we hand it over quickly?
25. We run three Long Island stores on Hikvision. Should we standardize or migrate one location at a time?
26. Need a Hikvision Repair on Long Island Today?

§17 FAQ (visible == FAQPage schema):
1. Who keeps the Hikvision administrator password after you finish on Long Island?
2. What is written on the handover sheet you leave with the recorder?
3. Can you move our recorder out of a basement that took water in the last storm?
4. Will you take away old Hikvision equipment and wipe the drives?
5. How far ahead should a North Fork or South Fork Hikvision job be booked?
6. Can you replace one failed Hikvision camera without redoing the whole system?
7. Can the recorder warn us when a camera stops working?
8. Can we put cameras on a rented storefront without the landlord's permission?
9. Do you work on Hikvision analog Turbo HD systems as well as IP cameras?
10. What do you need from us on the day of the visit?

De-dup notes: compared by meaning against every question in section 4. Deliberately NOT asked here (owned by older pages / generic intents): cost, "is it legal/banned", DIY, how many cameras, wired vs wireless, remote viewing from anywhere, coastal/winter weather, seasonal homes, outbuilding cable, neighbour privacy, offline/not recording, retention days, licensed/insured, servicing others' systems, warranty, internet-free operation, adding cameras later, resolution, signage, board documents, access-control integration, audio, internet speed, password reset, blurry night video. Coastal corrosion, warranty and cost are covered in body text and tables only. This page owns for the silo: the July 2026 FCC import/marketing prohibition (supply, covered-use buildings, Hik-Connect, spare parts), 2 CFR 200.216 grants, Section 889 contractors, exploited CVEs and hardening, inherited-system takeover, rebranded kits / FCC ID, ONVIF mixing, ColorVu vs IR by street lighting, AcuSense on busy roads, TandemVu, UPS during PSEG outages, police export, multi-store migration/HikCentral, use-restriction label, firmware cadence, router change, two-family recorders, HOA gatehouse.

## 6. Page build notes (LI hub)
- Thesis: keep / harden / extend / replace an existing Long Island Hikvision system after the FCC's July 16, 2026 prohibition, and know which buildings (fire districts, village halls, grant-funded houses of worship, federal contractors) should not get new Hikvision.
- Masked paragraph similarity vs every hikvision-security-camera-installation-* page: max 0.367 (Suffolk); page-level <= 0.035. Vs dahua-camera-installation-long-island: only NAP/licence/warranty boilerplate >= 0.6.
- Images (11) in images/hikvision-security-camera-installation/: 7 real AESS job photos from other jobs (re-cropped: manhattan-deli-exterior-camera, manhattan-deli-interior-cameras, nassau-window-depot-storage-camera, rockland-toyota-office-camera, rockland-toyota-active-deterrent, rockland-toyota-wall-camera, rockland-toyota-nvr-monitor) + 4 Hikvision product shots (nvr-hikvision-ds7616ni, hikvision-tandemvu-ptz-camera, hikvision-colorvu-dome-camera-black, hikvision-varifocal-bullet-camera). Drive has no Hikvision folder; CompanyCam not connected.



# PENDING MERGE → research/hikvision-security-camera-installation.md
Written 2026-10-18 by the parallel builder of `hikvision-security-camera-installation-ulster-county-ny` (REBUILD). Merge the `## Ulster County` section below into the silo file and append the register block to section 4/5. Format per blueprint v2.3 §12.4: exact query · platform · URL · finding · page+section used. Shell curl blocked; tools used: Firecrawl search (`mcp__Firecrawl__firecrawl_search`, excerpts) and Firecrawl scrape (`mcp__Fire_Crawl__firecrawl_scrape`, markdown / directQuote). Silo-wide rows F1–F7, N1, N4, V1–V3, P1–P3, A1–A2 reused from the silo file, not re-fetched.

---

## Ulster County

**Thesis:** an Ulster Hikvision system usually works alone — in a seasonal house, a farmhouse watching a distant barn, or a seasonal shop — so it must survive Central Hudson outages and lightning, reach owners over Starlink/satellite/LTE without port forwarding, and link outbuildings by bridge/fiber/solar; and because Ulster is dense with covered-use buildings (51 fire companies, four state prisons, SUNY New Paltz, county/town halls), the 2026 FCC rule decides *which building* may get new Hikvision. Private homes, farms, rentals and shops: yes; firehouses, halls, state sites, grant-funded projects: no. Differs from LI hub (keep/harden/extend/replace after FCC; Nassau vs Suffolk) and from the Westchester page (institutions/estates/permits).

### U-0 Source matrix (blueprint v2.3 §3)
| # | Source | Status |
|---|---|---|
| 1 | Reddit | Excerpts: r/Ubiquiti HV installer thread (new, UH8); r/hudsonvalley second-home owners thread and r/kingstonnewyork Flock thread (carried from dvr-upgrade-ulster page). Ulster Reddit thread naming Hikvision specifically: **EMPTY**. |
| 2 | Google PAA | **EMPTY (not accessible in build env)** |
| 3 | Google PASF | **EMPTY (not accessible in build env)** |
| 4 | Answer the Public | **EMPTY (not accessible in build env)** |
| 5 | Google AI Overview | **EMPTY (not accessible in build env)** — §10.5 says so; tests 7 commonly repeated claims, not AI quotes. |
| 6 | Landmarks | Senate House/Stockade, Rondout, Huguenot Street, Ashokan/Route 28, Mohonk/Shawangunks, Opus 40 (carried, sourced). |
| 7 | Use cases / building stock | Census ACS seasonal housing; Stacker pre-1940 share; Comptroller STR report; USDA farms (carried). |
| 8 | Bing / DDG | **EMPTY (not accessible in build env)** |
| 9 | Local news | Hudson Valley One Sept 2 2026 (new, scraped in full); Daily Freeman Sept 27 2026 (carried, excerpt); Central Hudson Sept 26 2026 (carried). |
| 10 | Hyperlocal | HV One Esopus burglaries Jan 2025 (carried); HV One cell dead zones 2016 (carried). Ulster news on Hikvision removal by a town/district/county: **EMPTY**. |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)** |

### U-1 New rows (fetched this run)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| UH1 | (scrape of carried URL) · Firecrawl scrape markdown | https://hudsonvalleyone.com/2026/09/02/police-defend-kingstons-surveillance-cameras-as-residents-raise-privacy-concerns/ | Rokosz Most, Sept 2 2026: since 2020 KPD has 7 Vigilant/Motorola LPRs + 71 other cameras; street cameras are **Ubiquiti**, "bought the cameras outright"; Ubiquiti video erased every 14–21 days; LPR data held up to six months; 32 KPD members access public-safety cameras, 4 the LPRs, every viewing time-stamped; KPD and Sheriff do not use Flock; DA Nneji: city system "and with the surveillance of private companies" showed two Broadway cases; 440 Pizza interior camera caught tip-jar thief; Deputy Chief Negron: "not looking into private windows"; cameras concentrated in Midtown and Uptown. | §5 para 4; §9 Q "Kingston's police run Ubiquiti"; §10.5 H3 7; Privacy section; Complete Services (Ubiquiti card); Sources |
| UH2 | `Ulster County fire departments fire districts list number Ulster County Emergency Management` · Firecrawl search → scrape markdown | https://www.dhses.ny.gov/location/ulster-county-fire-departments | NYS DHSES FDID list for Ulster: 51 fire departments/companies/districts numbered 56001–56054 (Accord FD … Lake Mohonk), plus IBM Kingston, Dyno Nobel, SUNY at New Paltz, Eastern / Shawangunk / Wallkill / Ulster Corr. Facilities, County of Ulster, towns/villages, ENCON field office. (Count = 51 entries in the 560xx fire range; Lake Mohonk listed twice, counted once.) | §5 para 2; §5.5; Covered Uses table; §9 fire-hall Q; Sources |
| UH3 | `Hikvision solar powered 4G camera kit DS-2XS official` · Firecrawl search → scrape directQuote | https://www.hikvision.com/us-en/products/network-products/network-cameras/solar-powered-series/ds-2xs6a47g1-izs-c36s80/ | 80 W panel; 360 Wh lithium (90 Wh ×4); LTE-FDD/WCDMA micro-SIM; built-in SSD / microSD to 256 GB; battery charging −20 °C to 45 °C (−4 °F to 113 °F); cloudy/rainy runtime "Performance mode: 5 days, Proactive mode: 8 days, Standby mode: 80 days"; approx. 26.45 kg (58.3 lb). | Rural Design H3 Distance; §9 solar Q; Equipment card; Sources |
| UH4 | `Hikvision wireless bridge DS-3WF0AC kit distance km point to point camera` · Firecrawl search → scrape directQuote | https://www.hikvision.com/en/products/transmission/wireless-bridge/ | DS-3WF1000-EI-2N "2.4Ghz 300Mbps 1KM Wireless Bridge Kit"; DS-3WF02-5AC/D "5Ghz 867Mbps 5KM Wireless Bridge Kit"; DS-3WF15KS-SI-5ACG/H 15 km industrial. | Rural Design H3 Distance; §9 barn Q; Equipment card; Sources |
| UH5 | `Hikvision ColorVu turret operating temperature -30 °C datasheet DS-2CD2347G2` · Firecrawl search (excerpt) | https://www.adiglobaldistribution.us/product/HX-TR2347SL2 | ADI listing DS-2CD2347G2-LSU/SL: max operating 140 °F, **min −22 °F**. | §7.5 Unheated spaces; Sources |
| UH6 | `Starlink CGNAT port forwarding not supported security camera NVR remote access` · Firecrawl search (excerpts) | https://docs.remote.it/introduction/get-started/starlink ; https://www.reddit.com/r/Starlink/comments/1j7f0u3/port_forwarding_for_nvr/ | "Starlink uses CGNAT, so port forwarding can't work"; r/Starlink: "Port forwarding won't work with starlink because they use cgnat." | Rural Design H3 Internet; §9 Starlink Q; §10.5 H3 3; Sources (remote.it only) |
| UH7 | `Hik-Connect P2P remote access without port forwarding hikvision.com how it works` · Firecrawl search (excerpts) | https://www.use-ip.co.uk/forum/threads/hik-connect-no-remote-access.6530/ | "there's no need to setup port forwarding on the router with Hik Connect" (dealer forum). Hikvision-own page stating this: not found → attributed to dealer forums. | §9 Starlink Q; Rural Design; Sources |
| UH8 | `site:reddit.com kingstonnewyork OR hudsonvalley OR newpaltz hikvision camera` · Firecrawl search (excerpt) | https://www.reddit.com/r/Ubiquiti/comments/sr6f9s/looking_for_an_installer_in_the_hudson_valley_ny/ | Hudson Valley installer thread: "I wouldn't install Hikvision, Dahua, or any of their downstream OEM brands." | Sources only (forum sentiment; not quoted in body) |
| UH9 | `Village of New Paltz rental permit law inspection landlords off-campus housing SUNY New Paltz students` · Firecrawl search → scrape markdown | https://www.villageofnewpaltz.gov/rental-property-registration-and-inspection-forms/ | Village registers and inspects residential rentals; "a building codes official has examined their home within the previous 12 months". Code chapter / fee: not on page → not used. | §9 New Paltz turnover Q; Sources |
| UH10 | `Ulster County Sheriff burglary seasonal home OR camp 2026 …` · Firecrawl search → scrape directQuote of programs page | https://www.ulstersheriffny.gov/programsservices | Programs listed: Child Passenger Safety, Pharmaceutical Drop Off, Project Lifesaver, Sheriff's Summer Camp, Cadet Program — **no private-camera registry or vacant-home check program**. | §5 para 4 ("Sheriff's published programs include no private-camera registry"); Sources |
| UH11 | `Nonprofit Security Grant Ulster County Kingston synagogue church 2026 security cameras Pat Ryan` and `"Nonprofit Security Grant" Kingston NY OR "New Paltz" OR Woodstock …` · Firecrawl search | (no Ulster award found) | **EMPTY** — no Ulster-specific NSGP award located; page states the 2 CFR 200.216 rule only, names no local recipient. | — |
| UH12 | `Ulster County farm stand theft OR farm equipment theft 2025 2026 sheriff …` · Firecrawl search | (results Sullivan County / Fresno only) | **EMPTY** for Ulster farm-stand theft news; page's honesty-box Q is a design answer with no incident claimed. | — |
| UH13 | `site:hikvision.com us-en NVR "Operating Temperature" …` and `Hikvision NVR DS-7608NI operating temperature …` · Firecrawl search | — | **EMPTY** — no official NVR temperature spec retrieved; page says only that recorders are indoor equipment (no figure). | — |

### U-2 Carried Ulster rows (sources fetched by earlier Ulster runs; URLs in dvr-upgrade-ulster.html Sources and research/cat6-repair.md, smart-lock-installation.md, soundbar-installation.md)
| ID | URL | Finding | Used |
|---|---|---|---|
| UC1 | https://api.census.gov/data/2023/acs/acs5?get=group(B25004)&ucgid=0500000US36111 (+ town table) | 86,178 housing units; 13,073 vacant; 6,545 seasonal/recreational/occasional; town shares Hardenburgh ~70%, Denning ~55%, Shandaken ~33%, Woodstock ~19% | §5 para 1; §5.5 |
| UC2 | https://comptroller.ulstercountyny.gov/wp-content/uploads/2025/09/FINAL-STR-Report-2025.pdf (excerpt) | 2,827 STR listings May 2025, 3.28% of housing; Shandaken 261; Rochester 238 | §5; §5.5; §9 Airbnb Q |
| UC3 | https://stacker.com/stories/new-york/counties-oldest-homes-new-york (excerpt) | 21,829 homes (25.3%) built 1939 or earlier | §5.5 |
| UC4 | https://www.cenhud.com/en/news/2026/central-hudson-crews-work-to-restore-power-after-noreaster/ ; https://www.dailyfreeman.com/2026/09/27/noreaster-day-two-over-4000-central-hudson-customers-still-have-no-service/ (excerpt) | >19,000 customers out after late-Sept 2026 nor'easter, Woodstock/Shawangunk/Plattekill/Hurley hardest hit; Central Hudson serves 93,209 Ulster customers | §5.5; §10.5 H3 4 |
| UC5 | https://get.earthnetworks.com/hubfs/2021%20State%20Lightning%20Reports/Lightning_Report_NewYork.pdf | Ulster 2020: 182,760 pulses, 49 thunder days | §5.5; §9 lightning Q |
| UC6 | https://www.mohonkpreserve.org/wp-content/uploads/2021/02/17-02WEATHER.NSN_.pdf (excerpt) | Daily records since 1896; 1 °F low twice in 2016–17 | §9 45 °F Q; §13 Mohonk card |
| UC7 | https://www.ulstercountyny.gov/Government/News/Newsroom/2025/09/2025-09-25-Funding-for-Broadband-Expansion ; https://radiocatskill.org/ulster-county-secures-59m-for-fiber-broadband-expansion/ (excerpt) | $20.8M ConnectALL (Sept 2025), ~1,300 unserved; May 2026 all 1,293 to get fiber under BEAD | §5.5; §9 fiber Q |
| UC8 | https://hudsonvalleyone.com/2016/12/29/dead-zones-more-than-a-decade-into-the-cell-phone-era-much-of-ulster-county-still-has-no-service/ | gaps along Routes 212 and 28 where mountains block cell access | Rural Design H3 Internet |
| UC9 | https://hudsonvalleyone.com/2025/01/09/string-of-town-of-esopus-burglaries-prompt-ulster-county-sheriff-to-issue-warning/ | Jan 2025 Sheriff warning, Union Center Road; advice: security system and motion lighting | §5 para 4 |
| UC10 | https://www.reddit.com/r/hudsonvalley/comments/1ww3ifc/secondhome_owners_in_the_hudson_valley_who_looks/ (excerpt) | caretakers/neighbours/cameras; "extensive cameras and a full house battery backup, combined with cellular fallback on their Internet package" | §9 alerts Q; §10 comparison note |
| UC11 | https://kingston-ny.gov/hlpc ; https://ecode360.com/6728919 | Landmark districts (Stockade, Rondout–West Strand, Chestnut St, Fair St); COA for material change visible from street/alley; ordinary maintenance exempt | §8.5; §9 bracket Q |
| UC12 | https://kingston-ny.gov/filestorage/8399/8469/48370/STR_Fact_Sheet_-_City_of_Kingston_Form-Based_Code.pdf (excerpt) | full STR permits capped at 1% of city housing units | §8.5 |
| UC13 | https://ecode360.com/35131702 | Ulster County Code Ch. 185 electrical licensing (signaling/communication/alarm/data in definitions) | §8.5 |
| UC14 | https://news.airbnb.com/an-update-on-our-policy-on-security-cameras (excerpt) | Indoor cameras banned in all listings from April 30, 2024; outdoor disclosure; no outdoor showers/saunas | §8.5; §9 Airbnb Q; §10.5 H3 5 |
| UC15 | https://www.newpaltz.edu/about/glance.html | 6,197 undergrad + 1,036 grad (>7,000) | §9 New Paltz Q |
| UC16 | parks.ny.gov / clerk.ulstercountyny.gov Stockade exhibit; huguenotstreet.org; opus40.org (bluestone 10,000 livelihoods by 1898); Ashokan 1915; thruway.ny.gov exits 18/19/20 | Landmark cards | §13 |
| UC17 | USDA 2022 Census of Agriculture (carried in cat6-repair.md) | 486 Ulster farms, avg 150 acres | §8 Route 209/farm card |
| UC18 | https://www.nysenate.gov/legislation/laws/CVR/52-A ; https://nysenate.gov/legislation/laws/PEN/250.05 | backyard-camera claim; eavesdropping | §8.5; FAQ shared gate |

### U-3 Pricing (§9, Ulster 1.53×) — no invented prices
Base = silo base used by the LI hub (Brooklyn $400–$700/camera; Small $1,800–$3,500; Mid $3,500–$8,000; Large $8,000+; service $195/hr, 3-hr min $585).

| Line | Brooklyn | Ulster ×1.53 |
|---|---|---|
| Per camera | $400–$700 | $612–$1,071 |
| Small 4–6 cams | $1,800–$3,500 | $2,754–$5,355 |
| Mid 8–16 cams | $3,500–$8,000 | $5,355–$12,240 |
| Large | $8,000+ | $12,240+ |

BYOE labour-only: no silo number → "quoted per camera after the walkthrough".

**FLAGS:**
- Old Ulster page (overwritten) published $520–$900 per camera, Basic $2,400–$4,400, $4,400–$9,500, $9,500+ — none equals 1.53× of the silo base ($612–$1,071; $2,754–$5,355; $5,355–$12,240; $12,240+). Old page also carried "$250" service-call and "$175" items with no silo source.
- HV hub (`hikvision-security-camera-installation-hudson-valley-ny`, not yet rebuilt) publishes $480–$850 per camera and $2,200–$4,200 basic — does not match any §9 multiplier; once rebuilt, its HV figures should be per-county.
- The Brooklyn base itself comes from the pre-rebuild Brooklyn page (as recorded by the LI run) — confirm with Anwar that it is the approved Hikvision base.

### U-4 House practices stated without an external source (FLAG for Anwar)
- Pull-the-plug test (battery, offline alert, auto-restart, boot time on handover sheet) on every job.
- Continuous recording by default at unoccupied houses; drive sized beyond longest absence.
- Caretaker accounts with limited rights; caretaker restart instructions taped inside the closet door.
- Battery backups "older than three to five years often fail the first long outage" (installer rule of thumb).
- Not installing new Hikvision at fire companies (incl. halls they rent out), town/county/state buildings, agency-leased units, grant-funded projects (AESS policy, "not legal advice").
- ColorVu white light set to event-only or off where it faces neighbours.
- Recorder email/FTP snapshot feature and Hik-Connect share permissions described from product knowledge (no external source fetched).
- Travel built into the 1.53 factor (FAQ) — consistent with §9 note, but confirm no separate travel fee policy exists.

### U-5 Images (11) — Drive has no Hikvision folder; CompanyCam not connected
7 real AESS job photos from other jobs (re-cropped, viewed before captioning; no faces, plates, house numbers, readable documents; dealership/brand signage cropped out) + 4 Hikvision manufacturer product shots (odd-numbered files, none used by the LI page). Folder: images/hikvision-security-camera-installation/
| Output (…-ulster-county-) | Source | Crop (l,t,r,b) | Placement |
|---|---|---|---|
| high-ceiling-showroom-with-mezzanine-wall-camera.webp | images/rockland-toyota-showroom.jpeg | (345,0,1247,470) ceiling only; banner text, dealer signs, people removed | Hero (eager) |
| dark-dome-in-ceiling-corner-near-light-panel.webp | images/rockland-toyota-dome-camera.jpeg | (340,0,935,400) logo and TV removed | §6 |
| dark-coffered-ceiling-with-rows-of-downlights.webp | images/rockland-toyota-active-deterrent.jpeg | (390,690,935,870) lounge ceiling coffer only (swapped in after the Westchester builder used the nassau-window-depot-office-camera corner-dome crop) | §7 |
| small-camera-high-on-white-wall-with-double-shadow.webp | images/rockland-toyota-bullet-camera.jpeg | (210,380,935,790) banner and dealer sign removed | Rural Design |
| black-bullet-on-ceiling-mount-in-office-grid.webp | images/rockland-toyota-ceiling-bullet.jpeg | (0,0,935,520) monitors/desk removed | §8 |
| recorder-tile-of-dim-back-storeroom.webp | images/nassau-window-depot-monitor.jpeg | (690,450,1240,800) CAM 3 tile only (hik-connect-manhattan used the CAM 2 tile) | §9 |
| white-colorvu-bullet-product-photo.webp | images/hikvision-colorvu-bullet-camera.jpg | full | §10 |
| colorvu-turret-pair-product-photo.webp | images/hikvision-colorvu-turret-camera-pair.jpg | full | §10 |
| ptz-speed-dome-product-photo.webp | images/hikvision-ptz-speed-dome-camera.jpg | full | §10 |
| acusense-indoor-cube-product-photo.webp | images/hikvision-acusense-indoor-cube-camera.jpg | full | §14 |
| long-ceiling-run-toward-far-exit-sign.webp | images/rockland-toyota-active-deterrent.jpeg | (250,540,450,1000) corridor ceiling only (LI used the exit-sign camera crop of this file; this page uses two other, non-overlapping regions of it) | Field Notes |
Not used: solar-trailer-*.jpg (appear computer-generated; trailer shows a non-AESS domain) — excluded under the no-AI-image rule.

### U-6 Build notes
- Masked paragraph similarity (block-level, SequenceMatcher on masked word lists) vs every hikvision-security-camera-installation-* page, dvr-upgrade-ulster and hik-connect-app-support-repair-ulster-county: every block < 0.65 except excluded constants (verbatim warranty sentence, licence/rating line, the fixed blueprint H2 "What AI Gets Wrong About …"). Highest non-constant: 0.60–0.64 (hero freshness stamp vs Westchester). Westchester page was being rebuilt in parallel — re-run at merge.
- File size 184,682 B (LI 180,021; Westchester 176,751 at time of check).
- 13,321 rendered words; title 55; meta 154.

---

## Question register — hikvision-security-camera-installation-ulster-county-ny (REBUILD 2026-10-18)
Replaces the old ulster-county-ny entry in section 4.

§9 Questions Answered (H3) and other headings ending in '?':
1. Ulster Hikvision Recorder Dark After a Storm?
2. How will we know the Hikvision system has quietly stopped recording while the cabin sits empty for a month?
3. When the owners live two or three hours away, who should the alerts go to first?
4. At a house nobody visits for weeks, should the recorder run continuously or only save motion?
5. Will a Hikvision recorder survive a winter in a house kept at 45 °F?
6. For a weekend house, are motion alerts more useful than a simple daily check-in?
7. Our only internet is a Starlink dish. Can Hik-Connect still show us the cameras?
8. How much cellular data does watching Ulster cameras from the city use?
9. Our road is on the county's fiber list. Should we install cameras now or wait for the new line?
10. Our barn is about 600 feet from the farmhouse. Should the camera link be cable, fiber or a wireless bridge?
11. Can a Hikvision solar camera watch a farm gate through an Ulster January?
12. Will a lightning strike near the barn travel down the camera cable to the recorder?
13. Can a camera watch the honesty box at our farm stand without recording everyone driving past?
14. Can one Hikvision recorder in the main house also serve the cameras at a guest cottage on the same lot?
15. Our volunteer fire company rents its hall for weddings. Can Hikvision cameras go in the hall?
16. We rent part of our Kingston building to a county agency. Which cameras does the 2026 rule reach?
17. Kingston's police run Ubiquiti street cameras. Should a private Kingston business avoid Hikvision too?
18. Can an old camera bracket on a Stockade or Rondout storefront be reused for a new Hikvision camera without a new review?
19. What do Airbnb's 2024 camera rules mean for a Hikvision system on a Shandaken rental?
20. When New Paltz student tenants move out in May, what should be reset on the recorder?
21. Why do snowflakes glow like little headlights on our camera at night?
22. Will a ColorVu camera's white light shine into a neighbour's bedroom across a dark rural road?
23. Should a seasonal shop on Route 28 record around the clock or only while it is closed?
24. Hikvision System Down at an Empty Ulster House?

§17 FAQ (visible == FAQPage schema):
1. Do you charge extra to drive to Hardenburgh, Denning or the far end of Route 28?
2. Can the work be done while we are still in the city?
3. Will you show our caretaker how to get the system running again after an outage?
4. Can a camera at the barn switch on a light or a siren when someone walks in?
5. Can you install cameras in January, with snow on the ground?
6. Our lane is shared with neighbours. Can a camera at the shared gate record all of us?
7. Will you work around our well line, septic field and buried cables when trenching to the barn?
8. What happens to our system if the FCC changes the Hikvision rules again?
9. Do you install cameras inside a barn with animals?
10. Can the system tell us when a delivery or a contractor arrives at the house?

De-dup notes (meaning-level, against section 4, the LI rebuild list and the in-progress Westchester rebuild): dropped a "burglar takes the recorder" question and a "deposit" FAQ and a "pole at end of drive" FAQ after the Westchester builder used those intents; reframed the snow question around IR glare (LI owns AcuSense-on-busy-road). Deliberately not asked: cost, legality/ban, DIY, how many cameras, wired vs wireless, generic remote viewing, winter/coastal durability, seasonal-home setup in general, outbuilding cable in general, neighbour privacy in general, offline/not recording, retention days, licensed/insured, warranty, historic-home discretion, inherited systems, police export, ONVIF mixing, firmware cadence. This page owns for the silo: Ulster covered-use buildings (fire halls rented for events, agency tenants), Kingston's Ubiquiti street cameras, Starlink/CGNAT and cellular data, county fiber timing, barn links by bridge/fiber, solar 4G gate kits in winter, lightning on outbuilding runs, farm-stand honesty box, guest-cottage recorder, Airbnb on Catskill rentals, New Paltz lease turnover, IR snow glare, ColorVu light trespass, seasonal-shop schedules, recorder in a 45 °F house, continuous vs motion recording for empty houses.

- Image overlap FLAG: hikvision-ptz-speed-dome-camera.jpg is also used (full shot) by the parallel Westchester rebuild; no unused Hikvision product file remained (LI, hik-connect-manhattan and Westchester took the rest).


# PENDING MERGE → research/hikvision-security-camera-installation.md — `## Westchester`

Written 2026-10-18 by the REBUILD of `hikvision-security-camera-installation-westchester-county-ny` (parallel with the Ulster rebuild; main run merges this file into the silo research file and deletes it). Format per v2.3 §12.4: exact query · platform · URL · finding · page+section used. Tools: WebSearch, Firecrawl search (`mcp__Firecrawl__firecrawl_search`, incl. `categories:["gov"]`), Firecrawl scrape (`mcp__Fire_Crawl__firecrawl_scrape`). Shell curl blocked. "Excerpt" = read only as a search-result snippet. Silo findings F1–F7, N1–N4, V1–V4, P1–P5, A1–A2 in the silo file are reused as-is (cited on the page where used).

## Westchester

Page: `hikvision-security-camera-installation-westchester-county-ny` (REBUILD in place; was crawled-not-indexed). Up-link `/hikvision-security-camera-installation-hudson-valley-ny`. GBP Bronx (460 E Fordham Rd, `#bronx`). Direct line (914) 877-2578 in body, CTAs, forms copy, sticky bar, schema; (800) 486-0943 only in the shared mega-nav header (4 tel links, all inside the nav). WhatsApp only wa.me/17186790359.

**Thesis:** in Westchester the Hikvision decision is set by *who watches the feed and whose money paid for it* — a "use test". The county has an unusually large public/quasi-public buyer base (county, 6 cities, 19 towns, ~2 dozen villages, 32 SWBOCES + PNWBOCES districts, county airport, federal courthouse, NYC's Kensico Reservoir) beside private estates and corridor retail where Hikvision stays legal; plus a county police Real Time Crime unit that uses surveillance cameras, so a permanent private live feed to police drifts toward a covered "public safety" purpose. Secondary: county alarm vs home-improvement licensing (2026 fee rise), estate gates on 3–4-acre northern lots, Central Ave / Platinum Mile / Post Road commercial. Distinct from dvr-upgrade-westchester (co-op governance) and from the LI hub (keep/harden/extend/replace).

### Source matrix (§3)
| # | Source | Result |
|---|---|---|
| 1 | Reddit | r/Westchester excerpt only (RW1). Westchester-specific Hikvision thread: **EMPTY** (none surfaced). |
| 2–5 | Google PAA / PASF / Answer the Public / AI Overview | **EMPTY (not accessible in build env)**. §10.5 says so; tests seven claims from cost guides/forums/sales pitches. |
| 6–7 | Landmarks / use cases | WL1–WL9, Census (reused H-W1/H-W2 from research/dvr-upgrade.md). |
| 8 | Bing / DuckDuckGo | **EMPTY (not accessible in build env)**. |
| 9–10 | Local news / hyperlocal | Patch Peekskill (2017 RTCC), Mount Kisco PD blotter 2026, News 12 (Yonkers garage Sept 2026, reused N-W1; Larchmont car thefts Aug 2026 excerpt), ABC7/Talk of the Sound (Ida, reused). Westchester news on Hikvision removal at public sites: **EMPTY** (search returned only national/foreign items) — page makes no such claim. |
| 11 | Yelp 1–3★ | **EMPTY (not accessible in build env)**. |
| Images | Drive / CompanyCam | Drive: no Hikvision folder. CompanyCam: not connected. → real AESS job photos from other jobs + Hikvision product shots. |

### Licensing / county rules (WK)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| WK1 | (homepage) · Firecrawl scrape markdown | https://consumer.westchestercountyny.gov/ | Dept of Consumer Protection; links Ch. 863 Art. XVI home improvement licensing law; "Plumbers and electricians must obtain a trade license in order to work in Westchester County"; "Home Improvement Licensing fee changes are effective January 1, 2026"; sample home improvement contract (02/2026). Nothing on camera brands. | §8.5 Electrical bullet; Q&A licence H3; §10.5 H3 1–2; Sources |
| WK2 | (fees page) · Firecrawl scrape markdown | https://consumer.westchestercountyny.gov/home-contractors-and-trades/home-improvement-licensing-fees | From Jan 1, 2026: application fee $750; expedited $100; renewal late fee $50; vehicle decal $10 each; duplicate certificate $50 (page dated 2025-12-17). | §5.5 bullet; §8.5; Q&A licence H3; Sources |
| WK3 | `Westchester County Code Chapter 863 Article XV alarm businesses alarm agents license "alarm device" definition` · Firecrawl search, categories gov (excerpt) | https://ecode360.com/7692228 | Town of Cortlandt Ch. 113: violation to install/service "any police or fire alarm device without having obtained an alarm business license or alarm agent license from the County of Westchester licensing authority pursuant to Chapter 863, Article XV". | §8.5 county alarm bullet; Q&A licence H3; Sources |
| WK4 | same search (excerpt) | https://ecode360.com/9157647 | Town of Mamaroneck Ch. 50: alarm business/agent licensing authority = Westchester County Dept of Consumer Affairs; owners/lessees with an alarm device must hold an annual alarm user permit from the Town Clerk (calendar year, valid to Jan 31 following); misdemeanor to install/service without licence; Alarm Review Board may deny/suspend/revoke permits. | §8.5 alarm-user bullet; Q&A alarm permit H3; Sources |
| WK5 | reused L-W1 (research/dvr-upgrade.md) | https://library.municode.com/ny/westchester_county/codes/code_of_ordinances?nodeId=PTVIIRUREDEENFA_CH863COPRCO_ARTXVILIPEENHOIMBU | Art. XVI home improvement = private residence ≤3 units; exemption for alarm work by county-licensed alarm business. | §8.5; Q&A licence H3 |
| WK6 | `Westchester County alarm business license Chapter 863 Article XV definition "alarm device" video surveillance camera` · WebSearch; then guessed municode node · Firecrawl scrape | (municode Art. XV node) | Art. XV definitions: **EMPTY** (scrape returned no text). Whether camera-only work is an "alarm device" in Westchester was NOT established → page says the county alarm question applies "when cameras are tied into an intrusion alarm" and tells owners to ask which licences cover the specific job. | §8.5; Q&A licence H3 |
| WK7 | reused silo K1 | https://dos.ny.gov/system/files/documents/2024/05/security_0.pdf | 19 NYCRR §195.2: NYS DOS licence for CCTV/video surveillance used to detect/monitor intrusion or theft. | §8.5; Q&A; §10.5 H3 2 |

### Police / Real Time Crime (WP)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| WP1 | `Westchester County Police Real Time Crime Center private cameras businesses share video feed program` · Firecrawl search → scrape markdown | https://publicsafety.westchestercountyny.gov/crime-analysis-unit | RTC connects "more than 100 local, state and federal law enforcement agencies"; "Westchester Putnam RTC"; "monitoring, deterring and evaluating criminal activity in real-time through surveillance cameras, fixed and mobile license plate recognition (LPR) systems". | §5 para 3 (quoted); Q&A live-link H3; §10.5 H3 4; Sources |
| WP2 | same → scrape | https://patch.com/new-york/peekskill/peekskill-partners-westchesters-real-time-crime-center | Patch, Dec 8, 2017: RTCC launched; "public-private partnerships"; operates from county police HQ in Hawthorne; pilot partners Yonkers, Mount Vernon, Mount Pleasant, Yorktown, Peekskill PDs; leads include "Images of persons or vehicles captured by security cameras". | §5 para 3; Q&A live-link H3; §10.5 H3 4; Sources |
| WP3 | `Metro-North station parking lot Westchester … thefts police 2025 2026` · Firecrawl search (full text in result) | https://mountkiscony.gov/departments/police_department/police_blotter.php | Mount Kisco 2026 blotter: repeated entries where store security video was reviewed (trespass, larceny, merchandise theft); landlord-provided security video; "Real Time Crime center broadcast an alert" about a stolen car; MTA PD at the station. | §8 northern village card; Sources |
| WP4 | same (excerpt) | https://www.facebook.com/News12WC/videos/car-thefts-following-the-thefts-local-police-say-they-will-have-increased-patrol/2125437728383599/ | News 12, Aug 25, 2026: "recent increase in car thefts and break-ins in Larchmont and the broader Westchester area" (excerpt). | §"Four Westchesters" Sound Shore; Sources |
| WP5 | reused N-W1 | https://westchester.news12.com/2026/09/05/several-vehicles-found-with-smashed-windows-in-yonkers-parking-garage/7xKdNpCKY1rAAULjrmWJ6H | Sept 2026 Yonkers Warburton Ave garage; surveillance video from garage and stores linked pair; two arrests. | §"Four Westchesters" south; Sources |

### Grants (WG)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| WG1 | `Nonprofit Security Grant Westchester County houses of worship 2025 OR 2026 …` · Firecrawl search → scrape | https://lawler.house.gov/news/documentsingle.aspx?DocumentID=3977 | Mar 24, 2025: Rep. Lawler (NY-17, parts of Rockland, Putnam, Dutchess, Westchester) and colleagues urged FEMA to lift pause on NSGP; letter lists "CCTV cameras to monitor threats" among what NSGP funds. | §10.5 H3 3; Sources |
| WG2 | `"Securing Communities Against Hate Crimes" grant Westchester …` · Firecrawl search → scrape (directQuote) | https://csiny.org/securitygrants/ | SCAHC: up to $70 million; up to $250,000 per organization (physical + cyber); deadline noon July 8, 2026; NSGP 2023 "212 grants to nonprofits in New York City, Nassau, Suffolk and Westchester"; CSI notes NSGP equipment restrictions ("Banned-equipment"). Whether SCAHC bars Hikvision: **not established** → page says read SCAHC's own RFA/contract. | §5.5 bullet; Q&A state-grant H3; §10.5 H3 3; Sources |
| WG3 | same search (excerpts) | https://www.governor.ny.gov/news/governor-hochul-announces-32-million-federal-funding-strengthen-security-nonprofits-facing ; https://www.fema.gov/grants/preparedness/nonprofit-security | FY2025 NSGP $274.5M nationwide; NY $32M (excerpt; already silo N3). | Not restated |
| WG4 | `Nonprofit Security Grant Program Westchester synagogues … Lawler OR Latimer` · WebSearch | (jns.org, amo.house.gov, jewishlink.news …) | No Westchester-specific 2026 award list found → **EMPTY** for a Westchester recipient list; page names none. | — |

### Federal Covered List (reconfirmed)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| WF1 | `FCC Covered List Hikvision "to the extent it is used for the purpose of public safety, security of government facilities"` · Firecrawl search (excerpt) | https://www.fcc.gov/supplychain/coveredlist | Hikvision entry: video surveillance and telecom equipment "to the extent it is used for the purpose of public safety, security of government facilities, physical security surveillance of critical infrastructure, and other national security purposes"; date of inclusion **March 12, 2021**. | Use-test section (quoted); Sources |

### Public buyers / landmarks (WL)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| WL1 | `Westchester County number of public school districts … BOCES` · Firecrawl search (excerpts) | https://www.swboces.org/page/about-our-boces/ ; https://pnwboces.org/site/Frequently-Asked-Questions ; https://www.lhric.org/o/lhric/page/supported-school-districts/ | SWBOCES: 32 component districts. PNWBOCES: ~60,000 students in 18 districts (Putnam + northern Westchester). LHRIC: 62 districts in Westchester, Putnam, Rockland. Page gives the SWBOCES 32 and the PNWBOCES 18 (two counties) separately and says "dozens of school districts" in the hero — no single county total stated. | Hero; §5 para 2; §5.5 |
| WL2 | reused L-W6 | https://www.westchestercountyny.gov/about-westchester (excerpt) | 6 cities, 19 towns, 20 villages (other counts 23). | Hero; §5 para 2; §5.5 |
| WL3 | `Westchester County Airport owned by Westchester County …` · Firecrawl search (excerpt) | https://en.wikipedia.org/wiki/Westchester_County_Airport ; https://airport.westchestercountyny.gov/ | County-owned; territory in North Castle, Harrison, village of Rye Brook; ~3 nmi NE of downtown White Plains. | §5; use-test table; Q&A airport H3; §13 card |
| WL4 | `Charles L. Brieant Jr. Federal Building and Courthouse White Plains 300 Quarropas Street` · Firecrawl search (excerpt) | https://www.nysd.uscourts.gov/courthouses/charles-l-brieant-jr-united-states-courthouse-white-plains | 300 Quarropas St at S. Lexington; near County Courthouse; "a few blocks from the Metro-North train station"; one block east of the Galleria garage. | §5; §8 downtown card; §13 card |
| WL5 | `Kensico Reservoir Valhalla New York City water supply DEP security` · Firecrawl search (excerpts) | https://dec.ny.gov/places/kensico-reservoir ; https://www.nyc.gov/site/dep/water/kensico-reservoir.page | 2,145-acre NYC reservoir in Valhalla; receives Catskill and Delaware water; last stop before the aqueducts to the city. | §5; use-test; Q&A airport H3; §13 card |
| WL6 | `Pound Ridge OR Bedford OR North Salem zoning minimum lot size acres` · Firecrawl search (excerpts) | https://ginnel.com/blog/understanding-bedfords-unique-four-acre-residential-zoning ; https://thewillstuartteam.com/blog/comparing-bedford-katonah-and-pound-ridge-for-buyers | Bedford "four-acre minimum lot size" (blog); Pound Ridge "in 1959 it rezoned 11,600 acres from 2-acre zoning to a 3-acre minimum" (realtor blog citing the town). Secondary sources only — FLAG. | §5 para 4; §7 card; §13 card; Q&A |
| WL7 | reused C-W1 / C-W2 / C-W3 (dvr-upgrade research) | 914inc.com Platinum Mile; nytimes 1995 Central Park Ave; Wikipedia US 1 | Platinum Mile 333→800 Westchester Ave, medical conversions; Central Park Ave 8.5 miles Yonkers–Greenburgh–White Plains; US 1 to Port Chester. | §5; §8 cards; §13 |
| WL8 | reused H-W1 / H-W2 (Census ACS 2023 5-yr via Firecrawl Alexandria census-gov) | https://api.census.gov/data/2023/acs/acs5?get=group(B25024)&ucgid=0500000US36119 | County 391,861 units; median built 1958; 109,608 built ≤1939; 170,635 detached; 66,378 in 50+ unit buildings. Yonkers 83,851 units, renters 42,519 > owners 38,031; Mount Vernon median 1952. | §5.5; §7; "Four Westchesters" |
| WL9 | reused F-W1/F-W2/F-W4 | ABC7 Ida (excerpt); talkofthesound.com Con Ed Ida; NYSEG tariff (excerpt) | Ida: Mamaroneck up to 14 ft water; Con Ed 15,975 Westchester out, 4,808 Mamaroneck Village; NYSEG Westchester towns Bedford, Lewisboro, North Salem, Pound Ridge, Somers. | "Four Westchesters" Sound Shore + north |

### Reddit (WR)
| ID | Exact query · platform | URL | Finding | Used |
|---|---|---|---|---|
| RW1 | `site:reddit.com Westchester hikvision OR "chinese cameras" OR NVR cameras house` · Firecrawl search (excerpt) | https://www.reddit.com/r/Westchester/comments/1hu8zqf/home_security_company_recs_for_security_camera/ | Reply: "They should look into wired POE (Power over Ethernet cameras) such as Ubiquiti or Lorex. Ubiquiti has their own NVR…" | §10.5 H3 5 (paraphrased); Sources |
| RW2 | same | (other results non-Westchester) | No Westchester thread about Hikvision → **EMPTY**. | — |

### Pricing (§9, Westchester 1.25×) — no invented prices
Silo base (Brooklyn page, per silo §3): $400–$700/camera; Small $1,800–$3,500; Mid $3,500–$8,000; Large $8,000+. ×1.25 (round half-up; all products integer): **$500–$875; $2,250–$4,375; $4,375–$10,000; $10,000+**. Service $195/hr, 3-hr min ($585) verbatim, not multiplied. BYOE labour-only: no silo number → "quoted per camera after the walkthrough".
**FLAGS:**
- The OLD Westchester Hikvision page showed $480–$800 per camera, $3,000–$6,000 and $9,000+ tiers, plus $250 / $175 / $0 widget chips — none match 1.25× of the silo base. Replaced.
- The Hudson Valley hub still shows old-template figures ($2,200 / $2,500+ / $175 chips etc.) — not checked against a multiplier; the main run may want to align it.
- The silo base itself comes from the pre-rebuild Brooklyn page (as the LI hub used); no separate price sheet was found.

### House practices stated without an external source (FLAG for Anwar)
- Policy: no new Hikvision at public school districts, public libraries, village/town/county buildings, police/fire/EMS, NSGP-funded projects, federal-contractor premises; side-by-side quotes in a non-covered line; labour-only (BYOE) declined at those sites.
- Policy: a business that wants a *permanent live police feed* gets a non-covered brand for those cameras (our reading — the FCC has not ruled; page says so).
- Treating private neighbours of the airport/reservoir/rail/substations as ordinary private sites but never aiming across the fence.
- Typical durations (house 1 day; estate 2–4 days), evening/weekend scheduling, 50% deposit (from the mandated warranty sentence), IT-managed network option, plough-line camera placement, boiler-room recorder relocation, purchase-contract checklist (password/reset/Hik-Connect unbind), kitchen-TV HDMI/decoder viewing, caretaker-only users.
- Field Notes = procedure (measure drive, power at gate, 811, night headlight check), not a story.

### Images (11) — Drive: no Hikvision folder; CompanyCam not connected
All viewed with Read before captioning; no faces, house numbers, plates or readable documents (deli house number "3778", signage text, posted papers, logos excluded by crop). WebP q80, ≤1600 px, in images/hikvision-security-camera-installation/. Sources chosen to avoid the LI and hik-connect-manhattan crops (different framings) and to favour Manhattan-deli sources + even-numbered/unused product files.
| Output (hikvision-security-camera-installation-westchester-county-…) | Source | Crop box | Placement |
|---|---|---|---|
| white-dome-at-signboard-corner-beside-bare-tree.webp (687×627) | images/manhattan-deli-exterior-camera.jpeg | (560,308,1247,935) — sign text excluded | Hero (eager) |
| wall-arm-camera-below-stone-cornice.webp (232×360) | images/manhattan-deli-exterior.jpeg | (0,40,232,400) — house number/sign excluded | §5 |
| mini-dome-and-round-speaker-in-store-ceiling.webp (430×280) | images/manhattan-deli-interior-cameras.jpeg | (290,110,720,390) ceiling only | §6 |
| mini-dome-at-ceiling-edge-over-wood-slat-wall.webp (275×150) | images/manhattan-deli-interior-cameras.jpeg | (515,395,790,545) — posted papers excluded | §9 Q&A |
| black-mini-dome-where-drop-ceiling-meets-tall-wall.webp (645×400) | images/rockland-toyota-dome-camera.jpeg | (290,0,935,400) — logo/TV excluded | Use-test section |
| black-bullet-on-pendant-mount-in-office-ceiling.webp (935×520) | images/rockland-toyota-ceiling-bullet.jpeg | (0,0,935,520) — desk/monitors excluded | §8 |
| high-wall-bullet-and-ceiling-dome-at-two-heights.webp (750×560) | images/rockland-toyota-bullet-camera.jpeg | (185,380,935,940) — banner, dealer sign excluded | §9 Q&A |
| white-eyeball-dome-in-corner-above-wall-sensor.webp (440×560) | images/nassau-window-depot-office-camera.jpeg | (370,240,810,800) — poster, licences, flag excluded | §7 |
| acusense-mini-dome-product-photo.webp (225×225) | images/hikvision-acusense-mini-dome-camera.jpg | full | §10 |
| mini-ptz-dome-product-photo.webp (225×225) | images/hikvision-mini-ptz-dome-camera.jpg | full | §10 |
| ptz-speed-dome-product-photo.webp (225×225) | images/hikvision-ptz-speed-dome-camera.jpg | full | §10 |
Captions say "photo from another AESS job / not a Westchester address" for job photos; the pendant-bullet caption states that camera is not Hikvision.

### Build notes
- check_page.py: only failures = 4 sibling back-links (nassau, nyc, rockland, suffolk don't link to /hikvision-security-camera-installation-westchester-county-ny) — main-run wiring. 12,548 rendered words; title 53; meta 157; 11 figures; 6 JSON-LD blocks; FAQ 10 = FAQPage 10; 176,869 B (LI hub 180,021; Ulster 183,454 at check time — re-check size cluster at wiring).
- Masked-geo block similarity (p/li/td/h2/h3/figcaption ≥8 masked words, SequenceMatcher) vs every hikvision-security-camera-installation-* page: all < 0.65 except the blueprint-fixed H2 "What AI Gets Wrong About … in [Area]" and the mandated warranty sentence (excluded). Max non-fixed: 0.632 (Suffolk). Vs all *westchester* pages: only NAP line / fixed H2 / warranty ≥0.65.
- Semantic de-dup: read against the full register (§4), the LI rebuild list (§5) and the live Ulster draft's questions. Changed one Q (gate recorder vs send-to-house) because Ulster asks one-recorder-for-guest-cottage and barn link medium.

### Question register additions — hikvision-security-camera-installation-westchester-county-ny (REBUILD 2026-10-18)
§9 Q&A (H2/H3 ending "?"):
1. Westchester Hikvision Recorder Down Right Now?
2. Our school district's buildings-and-grounds office asked whether the Hikvision cameras at the bus garage can stay. What should the board hear?
3. A Westchester village sent a camera bid that names Hikvision models. Will AESS bid it?
4. If our store gives the county police a live link to its cameras, does that change anything for Hikvision?
5. Our temple applied for New York's hate-crimes security grant, not the federal one. Do the same Hikvision limits apply?
6. Our public library is chartered separately from the village. Is it a "government facility" for Hikvision purposes?
7. Our private school takes no government money. Can it still choose Hikvision?
8. We are a private business next to Westchester County Airport. Does that make our cameras a "critical infrastructure" use?
9. Our engineering firm holds a federal task order and leases a Platinum Mile suite where the landlord's lobby cameras are Hikvision. Whose Section 889 problem is that?
10. Does a camera installer in Westchester need the county alarm licence, the home improvement licence, or both?
11. Our town makes us renew an alarm user permit every year. Does adding Hikvision cameras to the alarm change the permit?
12. Our Bedford gate already has a keypad and a lamp post. What else has to be there before a camera can go up?
13. Can a Hikvision camera at our gate read licence plates at night?
14. The caretaker lives in the cottage. Can he see the gate and barn cameras without seeing the cameras around the main house?
15. When is a PTZ camera worth it on a large northern Westchester property?
16. Our Central Avenue store shares a parking lot with three other tenants. Who should own the lot cameras?
17. Should our suite cameras be on the office-park landlord's Hikvision recorder, or our own?
18. Our medical office in a converted Platinum Mile building wants cameras at reception. What should they not see?
19. Why do our Hikvision clips show a time an hour off every spring?
20. Can our Hikvision recorder keep a copy of the footage somewhere other than the building?
21. Our committee wants to keep the Hikvision cameras for now. What does a sensible two-year plan look like?
22. How many days does a Hikvision installation on a large Westchester property usually take?
23. The snowplow keeps hitting the camera post at the edge of our drive. Where should that camera go instead?
24. Can we watch the cameras on the kitchen TV without opening the phone app?
25. How long should outdoor Hikvision cameras last on a Westchester house?
26. We are buying a house in Scarsdale that comes with Hikvision cameras. What should the purchase contract say about them?
27. Our apartment building's Hikvision recorder sits in the boiler room. Is that a problem?

§17 FAQ (visible == FAQPage):
1. Do you work evenings or weekends at Westchester offices and schools?
2. Can you price the same camera design in Hikvision and in a non-Hikvision line?
3. Will you take down cameras an earlier installer left and patch the holes?
4. Can a camera go on a pole or a tree at the end of a long drive?
5. Can a gate intercom be tied into the same recorder as the cameras?
6. What happens to the footage if a burglar takes the recorder?
7. Do you need floor plans or a survey before the walkthrough?
8. When is the deposit due, and how do we pay?
9. Can our own IT staff manage the recorder network settings instead of you?
10. Do you take a small job, such as one camera at a weekend house up north?

This page owns for the silo: the building-use test (school district existing cameras, village bids, public library, private school, airport/reservoir neighbours), live police feeds (county RTC), state SCAHC vs federal NSGP, landlord-owned Hikvision vs Section 889, county alarm vs home-improvement licensing and town alarm user permits, gate prerequisites, gate plate reading, caretaker-limited users, estate PTZ, shared-lot ownership, suite vs landlord recorder, medical reception masking, DST clock drift, off-site copies, two-year committee plan, install duration, plough-line placement, TV viewing, outdoor service life, purchase-contract terms, boiler-room recorder. Deliberately avoided: cost, legal/banned, DIY, how many cameras, wired vs wireless (body only), remote viewing, weather/winter/coast, neighbour privacy, retention, licensed/insured, warranty, offline, adding cameras later, board documentation, all LI-owned intents (FCC supply, Hik-Connect continuity, spare parts, CVE lookup, hardening, inherited takeover, rebrand/FCC ID, ONVIF mixing, ColorVu vs IR, AcuSense roads, TandemVu, UPS runtime, police export, multi-store, HOA gatehouse, two-family recorders).
