==============================================================
site-rebuild-131  —  parking silo: Staten Island page added
==============================================================
Cumulative. Carries v127 (12 photos + UNV), v128 (dedup),
v129 (hero/pricing/placeholder completion + first research),
v130 (full per-area research matrix).

THIS BUILD adds the Staten Island parking-lot camera page —
the eighth live page in the parking silo. The mega-nav no
longer routes Staten Island parking to a /free-quote fallback;
it points to the real page. The page was built to Blueprint
v2.2 and cleared a five-item deep-integrity audit:

  1 AI Overview source is EMPTY (web_search does not return
    Google's AI Overview box, per the v130 methodology note);
    the fabricated seven-topic "AI Overview Reality Check"
    section — which also duplicated body intents — was removed
    rather than fabricated.
  2 Duplication scan across H2/H3/body/Q&A/FAQ/schema: zero
    editorial duplicates (only approved legal/business + nav
    language is shared with siblings).
  3 Retention + warranty FAQ items removed as body duplicates;
    FAQPage schema regenerated (visible FAQ 9 == schema 9).
  4 False "at-grade Staten Island Railway crossing" research
    finding + on-page usage deleted (crossings eliminated by
    the mid-1960s); replaced with a CBS-sourced abandoned-
    vehicle concern; pain-map tally corrected.
  5 202-keyword mapping: NOT PASSED. The 202 terms are assigned
    to six pages (NYC/Queens/LI/Brooklyn/Manhattan/HV); Staten
    Island carries no assignment. Coverage stays 84 USED / 118
    FOR REVIEW; those terms belong to the six assigned pages and
    need their own keyword pass. Nothing was stuffed onto SI.

INTEGRATION: sitemap (0.7/monthly), _redirects (200 rewrite),
mega-nav (statenisland repointed to the real page), and a
reciprocal "Parking Lot Cameras Staten Island" silo card added
to all seven siblings. 11 SI photos + research matrix + pain-
question map added. Queens and Long Island body content is
unchanged; the seven siblings changed only by one cross-link
card each.

Full detail + per-page verification: changelog-rebuild-131.md.
