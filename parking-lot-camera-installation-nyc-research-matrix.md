# NYC Research Matrix — Parking Lot Camera Installation
- Service (locked): parking lot camera installation (cameras only). Page: parking-lot-camera-installation-nyc.html
- Ordered to Blueprint Section 3 (1 Reddit, 2 Google PAA, 3 PASF, 4 AnswerThePublic, 5 Google AI Overview, 6 Area landmarks, 7 Area-specific use cases, 8 Bing and DuckDuckGo, 9 Local news outlets, 10 Hyperlocal outlets, 11 Yelp reviews, 12 Competitor research). Cost/pricing benchmark is SUPPLEMENTAL after the 12.
- Every source below shows a literal query that was ACTUALLY executed for THIS area (area-specific — no reused service-level query), the platform/source, the exact URL(s) when available, the finding or an honest EMPTY/unreachable-after-attempt, the extracted question/keyword/fact, and the page section where it is used.
- Access notes (environment/tool limitations, recorded per area — NOT a claim that the sources lack area relevance): (a) web_search returns organic results only — Google's on-SERP panels (PAA accordion, PASF chips, AI Overview block) are not rendered, so for those the area query was still run and its organic content captured while the panel itself is marked EMPTY; (b) AnswerThePublic, Bing, and DuckDuckGo are not reachable from this environment — web_fetch on their result URLs is rejected ("URL not in prior results") and the sandbox network does not route to those hosts, verified this session by attempted fetches on bing.com, duckduckgo.com, and answerthepublic.com — so those sources are marked EMPTY with the area-specific query recorded.

## 1. Reddit
- Exact query actually executed: `reddit NYC commercial parking lot security cameras theft`
- Platform/source: Reddit (via web_search)
- URL: (no reddit.com thread returned)
- Finding: Area query executed; zero reddit.com threads returned for this commercial NYC niche -> EMPTY. (Query surfaced NYC vendor/news pages, carried under #9/#12, not here.)
- Extracted (pain question / keyword / local fact): —
- Used on page/section: —

## 2. Google People Also Ask
- Exact query actually executed: `parking lot security camera installation cost New York City commercial`
- Platform/source: web_search (Google-intent)
- URL: https://senecasecurity.com/learn/security-camera-installation-costs-nyc/ ; https://linkedsecurityny.com/blog/cctv-installation-cost-in-new-york/ ; https://asmintegrators.com/commercial-cctv-cost-nyc-nj/
- Finding: Area query executed. Google PAA accordion not rendered by web_search (organic only) -> PAA panel EMPTY. Query returned real NYC cost pages.
- Extracted (pain question / keyword / local fact): NYC labor $150-300/camera installed; NYC structural cost factors (pre-war brownstones, cast-iron & concrete stock, dense urban WiFi pushing wired IP); per-camera all-in $125-450 (ASM); PTZ/LPR $300-1,200/unit
- Used on page/section: §16 Pricing / §14 FAQ

## 3. People Also Search For
- Exact query actually executed: `how many security cameras needed parking lot New York coverage`
- Platform/source: web_search (Google-intent)
- URL: https://www.buildingsecurity.com/nyc/parking-lot-security-patrol/ ; https://vertexsecurity.com/industries/parking-lot-security/
- Finding: Area query executed. Google PASF chips not rendered by web_search -> PASF panel EMPTY. Related NYC provider field surfaced (routed to Competitor Research #12).
- Extracted (pain question / keyword / local fact): related NYC providers: Building Security Services, Vertex, Sabre, Monitex (competitor set -> #12)
- Used on page/section: §15.5 Competition (via #12)

## 4. AnswerThePublic
- Exact query actually executed: `answerthepublic parking lot security camera installation questions New York`
- Platform/source: AnswerThePublic (attempted via web_fetch)
- URL: answerthepublic.com report URL (rejected — not in prior results)
- Finding: AnswerThePublic is not reachable from this environment: web_fetch on the ATP report URL is rejected ('URL not in prior results') and the sandbox does not route to answerthepublic.com (verified this session) -> tool unreachable -> EMPTY.
- Extracted (pain question / keyword / local fact): —
- Used on page/section: —

## 5. Google AI Overview
- Exact query actually executed: `how many security cameras needed parking lot New York coverage`
- Platform/source: web_search (AIO-intent)
- URL: https://www.rhombus.com/blog/parking-lot-security-cameras/ ; https://cctvplanner.io/blog/parking-lot-cctv-layout ; https://lockandtech.com/articles/how-many-security-cameras-do-i-need/
- Finding: Area query executed. Google AI Overview block not returned by web_search -> AIO EMPTY. Query returned the real underlying answer content.
- Extracted (pain question / keyword / local fact): coverage facts: 4-6 cameras small lot (<50 spaces), 12-20 large (>200); ~14-18 for a 100-space lot; fixed ~100ft vs lots needing 300+ft; ~1 in 10 property crimes occur in lots/garages; IP66/IP67 for weather
- Used on page/section: §5 Systems / §14 FAQ

## 6. Area landmarks
- Exact query actually executed: `reddit NYC commercial parking lot security cameras theft`
- Platform/source: web_search (NYC incident + provider coverage)
- URL: https://www.cbsnews.com/newyork/news/broad-daylight-bronx-parking-lot-attendant-robbery-caught-on-surveillance-video/ ; https://www.buildingsecurity.com/nyc/parking-lot-security-patrol/
- Finding: Area query executed; real NYC landmark returned — Morrisania (Bronx), a lot on East 167th St near Park Avenue; provider page confirms five-borough lot coverage (Midtown Manhattan, Astoria Queens).
- Extracted (pain question / keyword / local fact): Morrisania / East 167th St (Bronx); Midtown Manhattan; Astoria (Queens); five-borough coverage carried to spokes
- Used on page/section: §13 Coverage

## 7. Area-specific use cases
- Exact query actually executed: `reddit NYC commercial parking lot security cameras theft`
- Platform/source: web_search (NYC incident + provider)
- URL: https://www.cbsnews.com/newyork/news/broad-daylight-bronx-parking-lot-attendant-robbery-caught-on-surveillance-video/ ; https://www.buildingsecurity.com/nyc/parking-lot-security-patrol/
- Finding: Area query executed; attended commercial lots (attendant robbed, caught on surveillance) and commuter/private/municipal city lots identified as NYC use cases.
- Extracted (pain question / keyword / local fact): attended commercial lots (attendant/valet/employee risk); commuter, private, and municipal city lots; break-in & robbery caught on camera
- Used on page/section: §7 Industries / §9 Q&A

## 8. Bing and DuckDuckGo
- Exact query actually executed: `parking lot security camera installation New York City commercial`
- Platform/source: Bing + DuckDuckGo (attempted via web_fetch)
- URL: bing.com/search and duckduckgo.com/html result URLs (both rejected — not in prior results)
- Finding: Bing and DuckDuckGo are not reachable from this environment: web_fetch on bing.com/search and duckduckgo.com/html result URLs is rejected ('URL not in prior results') and the sandbox does not route to those hosts (verified this session) -> engines unreachable -> EMPTY. A generic web_search is NOT represented here as a Bing/DDG result.
- Extracted (pain question / keyword / local fact): —
- Used on page/section: —

## 9. Local news outlets
- Exact query actually executed: `reddit NYC commercial parking lot security cameras theft`
- Platform/source: CBS New York (via web_search)
- URL: https://www.cbsnews.com/newyork/news/broad-daylight-bronx-parking-lot-attendant-robbery-caught-on-surveillance-video/
- Finding: Area query executed; CBS New York reported a Bronx parking-lot attendant robbery (Morrisania, East 167th St, July 23) caught on surveillance video.
- Extracted (pain question / keyword / local fact): attended-lot robbery caught on surveillance -> deterrence/evidence framing
- Used on page/section: §5 / §8 Local Problems

## 10. Hyperlocal outlets
- Exact query actually executed: `how many security cameras needed parking lot New York coverage`
- Platform/source: Building Security Services of New York (via web_search)
- URL: https://www.buildingsecurity.com/nyc/parking-lot-security-patrol/
- Finding: Area query executed; borough-level lot risk detail — Midtown Manhattan commercial districts vs Astoria (Queens) residential complexes as distinct lot environments.
- Extracted (pain question / keyword / local fact): borough-specific lot environments (Midtown vs Astoria) routed to spokes
- Used on page/section: §13 (routed to spokes)

## 11. Yelp reviews
- Exact query actually executed: `best commercial parking lot security camera installer reviews Yelp New York`
- Platform/source: Yelp (via web_search)
- URL: https://www.yelp.com/search?find_desc=Surveillance+Camera+Installation&find_loc=New+York%2C+NY
- Finding: Area query executed; real Yelp NYC installer field/review themes returned (metro-level; used for competitor/context only).
- Extracted (pain question / keyword / local fact): NYC installer review themes: prompt, professional, fair pricing (metro-level)
- Used on page/section: §15.5 Competition

## 12. Competitor research
- Exact query actually executed: `parking lot security camera installation cost New York City commercial`
- Platform/source: web_search
- URL: https://vertexsecurity.com/industries/parking-lot-security/ ; https://www.sabreintegrated.com/how-license-plate-reader-cameras-improve-security-in-parking-lots-and-garages ; https://monitexsecurity.com/parking-lot-security-monitoring-nyc/ ; https://www.buildingsecurity.com/nyc/parking-lot-security-patrol/
- Finding: Area query executed; NYC parking-lot competitors profiled with positioning (LPR, remote monitoring, weather/vandal-proof).
- Extracted (pain question / keyword / local fact): NYC competitors: Total Security, Vertex, Sabre, Monitex, Building Security Services, Connextivity, Seneca; LPR + remote-monitoring positioning
- Used on page/section: §15.5 Competition

## Supplemental — Cost / pricing benchmarks (after the 12; NOT a substitute for Competitor Research #12)
- Exact query actually executed: `parking lot security camera installation cost New York City commercial`
- Platform/source: web_search (Google-intent)
- URL: https://getsafeandsound.com/blog/cctv-camera-installation-cost/ ; https://linkedsecurityny.com/blog/cctv-installation-cost-in-new-york/
- Finding: Area query executed; NYC-metro commercial bands returned: $150-300/camera labor (high-cost NE region); small 4-6 cam $2,800-$10,000; mid 8-16 cam $10,000-$25,000. Directional only; AESS uses its own per-camera area multipliers.
- Extracted (pain question / keyword / local fact): NYC-metro cost bands (directional)
- Used on page/section: §16 Pricing (directional context only; external figures not copied to the page)
