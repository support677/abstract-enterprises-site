==============================================================
site-rebuild-132  —  parking silo: Nassau County page added
==============================================================
Cumulative. Carries v127 (12 photos + UNV), v128 (dedup),
v129 (hero/pricing/placeholder completion), v130 (per-area
research matrix), v131 (Staten Island page + integration).

THIS BUILD adds the Nassau County parking-lot camera page —
the NINTH live page in the parking silo, and the first of the
two Long Island county children (Nassau, then Suffolk). The
mega-nav no longer routes Nassau parking to a /free-quote
fallback; it points to the real page.

Donor was the corrected Staten Island child (identical routing:
Brooklyn GBP 1282 Troy Ave, LocalBusiness #brooklyn, phone
(347) 934-8335, no (845), no GBP swap). Every SI-specific
editorial block was independently rewritten with genuine Nassau
content (pure geo-swap ~84% similarity is rejected), grounded in
fresh web_search research (NCPD 348 catalytic-converter thefts,
Cmsr Ryder, Plainview/Bethpage/Hicksville/Massapequa hotspots,
the Glen Cove camera-alert case; Roosevelt Field, Mineola LIRR/
county seat, UBS Arena/Belmont, Nassau Coliseum, Hempstead/
Jericho/Sunrise/Old Country corridors, Freeport Nautical Mile,
Long Beach barrier island, North Shore Gold Coast).

PRE-DELIVERY AUDIT:
  1 SI-content sweep ALL CLEAR (every SI landmark, precinct,
    neighborhood and "Island" self-reference rewritten out;
    Island Park / Cross Island Pkwy / Islanders / generic
    "marina" preserved).
  2 Fabricated SI "1,300 abandoned-vehicle complaints" stat
    (carried in by the clone) removed; Q&A reframed generically.
    No invented number remains.
  3 Duplication scan across H2/H3/body/Q&A/FAQ/schema: zero
    editorial duplicates (only approved legal/business + nav
    language is shared with siblings). Byte size sits normally
    in the sibling range; dedup verified by content, not bytes.
  4 FAQPage schema regenerated from the visible FAQ (visible 9
    == schema 9); HowTo step text re-synced. Fixed a recurring
    "Installatiin" typo (incl. <title>) and the "on Nassau
    County" island-idiom.
  5 202-keyword mapping: NOT PASSED. The 202 terms are assigned
    to six pages (NYC/Queens/LI/Brooklyn/Manhattan/HV); Nassau
    carries no assignment. Coverage stays 84 USED / 118 FOR
    REVIEW; those terms belong to the six assigned pages and
    need their own keyword pass. Nothing was stuffed onto Nassau.

PRICING: Nassau uses the x1.20 labor tier (Manhattan/SI/Nassau/
Suffolk): Starter $1,020-$1,800 / Standard $1,800-$3,000 /
Premium $3,360-$5,400. Post-warranty rate is the locked
$195/hr + $585 3-hr minimum (unchanged).

INTEGRATION: sitemap (0.7/monthly), _redirects (200 rewrite),
mega-nav (nassau parking repointed to the real page), and a
reciprocal "Parking Lot Cameras Nassau County" silo card added
to all eight siblings. 11 Nassau photos added at
/images/parking/*-nassau-county.webp. The eight siblings
changed only by one cross-link card each.

Full detail + per-page verification: changelog-rebuild-132.md.
