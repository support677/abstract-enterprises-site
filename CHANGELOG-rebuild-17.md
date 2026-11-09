# site-rebuild-17 — Changelog

**Date:** 2026-05-07
**Type:** Contamination fix + canonical blueprint commit

## What changed

### 1. Wrong-service link block removed from 16 home-automation pages

All 16 home-automation area pages previously contained a section titled
"Alarm Installation — All 76 Brooklyn Neighborhoods" with 76 links to
**alarm-installation Brooklyn pages**. This was wrong-service, wrong-borough
contamination — most visibly placing a Brooklyn alarm block on Bronx,
Manhattan, Queens, HV county, etc. pages.

The block has been replaced with a service-correct, area-correct
"Home Automation — Other Areas We Serve" cross-link block that links
to the 15 sibling home-automation area pages (not self, not wrong service).

**Files changed:**
- home-automation-dutchess-county.html
- home-automation-installation-bronx.html
- home-automation-installation-brooklyn.html
- home-automation-installation-hudson-valley.html
- home-automation-installation-long-island.html
- home-automation-installation-manhattan.html
- home-automation-installation-nassau-county.html
- home-automation-installation-nyc.html
- home-automation-installation-orange-county.html
- home-automation-installation-queens.html
- home-automation-installation-rockland-county.html
- home-automation-installation-staten-island.html
- home-automation-installation-westchester-county.html
- home-automation-putnam-county.html
- home-automation-suffolk-county.html
- home-automation-ulster-county.html

Each page lost ~12-13KB of wrong content; replaced with ~3KB of correct cross-links.

### 2. New file: BLUEPRINT.md

Canonical page-build specification, drawn from the verified-clean
security-camera-installation-bay-ridge-brooklyn-ny.html plus v2.1 additions.
Single source of truth — every future build reads this BEFORE writing HTML.

**Note:** v2.1 elements 21, 22, 24, 25, 30 have specs flagged "needs confirmation"
pending Anwar's review. Elements 35, 37, 40, 41 are pending.

## What did NOT change

- 651 cloned pages identified in the audit (AC Brooklyn 75, alarm Brooklyn 75,
  fire-alarm Brooklyn 75, alarm Bronx 71, fire-alarm Bronx 71, intercom Bronx 71,
  security-camera Bronx 71, structured-cabling Bronx 71, tv-installation Bronx 71)
  — these still need full v2.1 rebuilds with real local research per neighborhood.

## Verification

- Zero remaining alarm-installation Brooklyn block contamination on home-automation pages
- Replacement block links to 15 areas (not self) on every page
- All canonicals still correct
