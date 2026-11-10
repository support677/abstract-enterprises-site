# Output spec — write ONE JSON file (UTF-8, valid JSON) at the path given in your task.
Strings may contain only these inline tags: <b>, <i>, <a href="/...">. Use HTML entities or plain Unicode (″ for inches is fine). No markdown.
Write in plain, confident, local, human English for homeowners/business owners. 2nd person. No fluff, no hype words ("unparalleled", "premier"). Every section must be specific to THIS area.
Total visible words from your fields must be ≥ 2,600.

{
 "title": "≤ 60 characters, pattern: TV Mounting Prices <Area> | <short hook>",
 "meta": "150–160 characters exactly, mentions the area + 2 specific local hooks (e.g. building types)",
 "hero_badge": "short uppercase-style badge e.g. 'TV MOUNTING PRICES · ALL 5 BOROUGHS'",
 "hero_sub": "≤ 45 words, area-specific value prop with the starting price",
 "quick_answer": "40–70 word direct answer to 'how much does TV mounting cost in <area>' using ONLY the verified prices (AI-overview style)",
 "why_h2": "Why <Area> Homes & Businesses Need Professional TV Mounting (or similar)",
 "why_paras": ["3–4 paragraphs, 70–120 words each, grounded in research: building stock, wall types, resident pain points, Reddit/news themes"],
 "why_facts": [{"text": "real local fact/stat", "source": "URL"}],   // 4–6
 "services_h2": "...", "services": [{"icon":"single emoji","title":"...","text":"35–60 words"}],   // 6–8, area-relevant
 "buildings_h2": "...", "buildings": [{"icon":"emoji","title":"building type that really dominates the area","text":"40–70 words"}],  // 5–6
 "building_methods": [{"title":"wall/material","text":"40–80 words: exactly how we anchor + its price add"}],  // 4–6
 "commercial_h2": "...", "commercial_intro": "60–100 words",
 "corridors": [{"name":"REAL commercial corridor/district","text":"25–50 words: what businesses there, TV use"}],  // 4–6
 "compliance": [{"title":"...","text":"40–80 words"}],  // 2–4, real & accurate (e.g. COI requirements, ADA 4-inch protrusion rule for wall-mounted objects in circulation paths, building alteration agreements, landlord consent). No made-up codes.
 "qa_h2": "...", "qa": [{"q":"real question phrased like Reddit/PAA","a":"60–110 words, area-specific"}],  // 12–14, UNIQUE
 "equipment_h2": "...", "equipment": [{"icon":"emoji","title":"mount/equipment type","text":"35–60 words with when to use it in this area"}],  // 6–8
 "comparison": {"title":"e.g. Fixed vs Tilting vs Full-Motion vs Pull-Down", "head":["Mount","Best for","Watch out for","Price add"], "rows":[["..."]]},  // 4–5 rows, prices from list
 "ai_h2": "What AI Answers Get Wrong About TV Mounting in <Area>",
 "ai_intro": "60–100 words",
 "ai_items": [{"claim":"short quoted AI-style claim","paras":["3 paragraphs, 40–70 words each, correcting it with local field reality"]}],  // EXACTLY 7, total 800–1,200 words
 "process": [{"title":"...","text":"30–50 words"}],  // 5 steps, booking→arrival window→wall check→install→walkthrough
 "landmarks_h2": "...", "landmarks": [{"name":"REAL landmark","text":"one line tying it to TV mounting jobs nearby (no invented customers)"}],  // exactly 6
 "also_serve": "one sentence listing 4+ real nearby towns/neighborhoods",
 "pricing_intro": "60–100 words introducing the price tables (I render the tables)",
 "packages_intro": "40–70 words",
 "package_notes": {"starter":"one line who it's for","standard":"...","premium":"..."},
 "byoe": "50–80 words: bring-your-own-bracket / TV-on-stand / labor-only option",
 "faq": [{"q":"...","a":"40–80 words"}],  // 10–12, must NOT repeat any qa question
 "field_notes": "70–120 words, written from the job details given in your task ONLY (no names/addresses), framed honestly (quoted / booked)",
 "local_close_h2": "...", "local_close": "70–110 words summary of local problems we solve",
 "keywords_used": ["list of exact phrases from the keyword file you included"],
 "research_notes": {"reddit":"...","google_paa":"...","pasf":"...","answer_the_public":"...","ai_overview":"...","landmarks":"...","use_cases":"...","bing_duckduckgo":"...","local_news":"...","hyperlocal":"...","yelp":"..."},  // what you found, or "empty — reason"
 "sources": ["URLs used"]
}
