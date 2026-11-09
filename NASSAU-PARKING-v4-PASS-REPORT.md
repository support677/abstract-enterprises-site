# Nassau County Parking-Lot Camera Page — Correction PASS Report (pricing / canonical / images / sitemap)

Page: parking-lot-camera-installation-nassau-county.html
Canonical (new): https://www.abstractenterprisessecuritysystems.com/parking-lot-camera-installation-nassau-county.html
Scope: the FOUR verified failures only. No clone/expand/rewrite; approved wording, forms, phones, address, license, warranty and BYOE untouched.

## VERDICT: PASS

---

## Fix 1 - PRICING (Nassau was using Brooklyn x1.20 / the Suffolk multiplier; must be 1.15x)
Brooklyn parking-page package prices were read from the current repo and multiplied by 1.15, using the site's existing whole-dollar rounding. No Brooklyn prices were invented.

  Tier            Brooklyn base (repo)   x1.15       Rounded     Was on Nassau (x1.20)
  Starter low     $850                   $977.50     $978        $1,020
  Starter high    $1,500                 $1,725.00   $1,725      $1,800
  Standard low    $1,500                 $1,725.00   $1,725      $1,800
  Standard high   $2,500                 $2,875.00   $2,875      $3,000
  Premium low     $2,800                 $3,220.00   $3,220      $3,360
  Premium high    $4,500                 $5,175.00   $5,175      $5,400

Only $850 x 1.15 = $977.50 required rounding -> $978 (nearest whole dollar); all other products are already whole dollars.
Result on page: Starter $978-$1,725, Standard $1,725-$2,875, Premium $3,220-$5,175. All six former x1.20 values are gone. AI-Overview national figures ($1,296, $600) and the service rate ($195/hr, $585 min) were NOT touched. No priceRange/Offer node exists in the JSON-LD, so no schema price edit was required.

## Fix 2 - CANONICAL (locked rule: canonical includes .html, force www, extensionless rewrites to .html)
- <link rel="canonical"> -> .../parking-lot-camera-installation-nassau-county.html (www).
- og:url and the JSON-LD self-referencing page URLs (WebPage/Service url, BreadcrumbList item @id) -> .html (5 full-URL self-refs updated).
- The 11 ImageObject @id fragments -> ...nassau-county.html#image1..11 (schema self-refs kept consistent).
- LEFT UNCHANGED by design: the two Web3Forms landing_page hidden fields (form data, not a metadata/schema URL) and the four .../images/parking/....webp image URLs.
- _redirects extensionless rule kept exactly as-is: /parking-lot-camera-installation-nassau-county -> /parking-lot-camera-installation-nassau-county.html 200 (line 946).

## Fix 3 - IMAGES (11 referenced; 10 filenames absent from the repo)
Of the 11 referenced Nassau project images, only the hero parking-lot-camera-installation-nassau-county.webp physically existed; the other 10 were absent. (Silo-wide condition: every parking sibling references 11 and has only its hero; 90 of 99 sibling project images are likewise absent.) Because no distinct Nassau project images exist anywhere in the repo, the 10 missing files were created at their exact referenced paths from the approved Nassau hero (valid .webp, 152 KB each) - option (a) in the brief. The 11 distinct filenames and the approved keyword-based Nassau alt/title tags are intact (no alt/title change needed), and every referenced path now resolves. Follow-up: replace these ten placeholders with distinct real Nassau photos at the same paths (no HTML change required).

## Fix 4 - SITEMAP
Nassau parking <loc> updated to the canonical .html URL, exactly once; the extensionless parking <loc> no longer appears (0). sitemap.xml remains valid XML with an intact </urlset> tail.

---

## Pre-PASS verification (all required checks)
- Nassau multiplier is 1.15x - confirmed against Brooklyn base prices (table above); page shows $978 / $1,725 / $2,875 / $3,220 / $5,175.
- .html canonical and sitemap AGREE: both https://www.abstractenterprisessecuritysystems.com/parking-lot-camera-installation-nassau-county.html
- Extensionless redirect remains valid: _redirects line 946 unchanged, 200 rewrite to the .html file.
- All 11 project images resolve (0 missing).
- All 6 JSON-LD blocks parse (LocalBusiness, Service, BreadcrumbList, ImageObject @graph, HowTo, FAQPage).
- Visible FAQ exactly matches FAQ schema - Q match = True, A match = True (9/9).
- No unrelated files changed - diff vs baseline shows only parking-lot-camera-installation-nassau-county.html and sitemap.xml modified; new files are the 10 Nassau images, the research matrix, this report and the manifest. _redirects, js/mega-nav.js, keyword reports and all sibling pages are byte-identical to baseline.

## Preserved / untouched (verified)
License 12000287431 x6; 1282 Troy Ave x7; phone +13479348335 x12 (stray 845 = 0); three-year warranty x3; BYOE present; Web3Forms key x2; form-hero + form-detail present; service rate $195/$585 x2; single H1; <div> 234/234 balanced.

Baseline of record: uploaded ZIP deploy-6a6c0f4d5317c60008e61c49.zip
SHA-256 (baseline ZIP): 22372f2634d30f031fa3dd6610a72261a73ea91e28e0264fad98487e7a452f35
