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

