/**
 * AESS Click-Fraud Guard — Google Ads Script (account 549-269-6630)
 * Schedule: Tools > Bulk actions > Scripts > + > paste > Authorize > Frequency: Hourly.
 *
 * Location = Google's most specific physical location for each click (usually the ZIP).
 * What it does every hour, for every campaign whose name starts with CAMPAIGN_PREFIX:
 *   1. Pulls today's clicks per ZIP (click_view, user's physical location).
 *   2. Any ZIP over MAX_CLICKS_PER_ZIP_PER_DAY clicks today in a campaign gets excluded from
 *      that campaign for the rest of the day (logged to the sheet).
 *   3. On the first run of a new day, it lifts yesterday's automatic ZIP blocks
 *      (blocks Anwar adds by hand are never touched).
 *   4. Reads the "Blocked IPs" tab and adds any new IP there as an IP exclusion on every pilot
 *      campaign (Google allows 500 per campaign) — used for competitors / repeat price-checkers.
 *   5. Emails ALERT_EMAIL with what it did.
 *
 * Starts in PREVIEW mode (DRY_RUN = true): it only logs + emails. Flip to false after review.
 */
var CAMPAIGN_PREFIX = 'AESS | Cameras | Brooklyn';
var MAX_CLICKS_PER_ZIP_PER_DAY = 5;
var ALERT_EMAIL = 'support@abstractenterprisessecuritysystems.com';
var SHEET_URL = 'PASTE_GOOGLE_SHEET_URL_HERE'; // sheet with tabs "Auto ZIP Blocks" and "Blocked IPs"
var DRY_RUN = true;

function main() {
  var ss = SpreadsheetApp.openByUrl(SHEET_URL);
  var zipTab = tab_(ss, 'Auto ZIP Blocks', ['Date', 'Campaign ID', 'Campaign', 'ZIP geo ID', 'ZIP', 'Clicks', 'Criterion resource', 'Lifted']);
  var ipTab = tab_(ss, 'Blocked IPs', ['IP address', 'Reason', 'Added by script on']);
  var tz = AdsApp.currentAccount().getTimeZone();
  var today = Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd');
  var cid = AdsApp.currentAccount().getCustomerId().replace(/-/g, '');
  var log = [];

  var camps = {};
  var it = AdsApp.search(
    "SELECT campaign.id, campaign.name FROM campaign WHERE campaign.name LIKE '" + CAMPAIGN_PREFIX + "%' AND campaign.status != 'REMOVED'");
  while (it.hasNext()) { var r = it.next(); camps[r.campaign.id] = r.campaign.name; }
  var ids = Object.keys(camps);
  if (!ids.length) { Logger.log('No pilot campaigns found.'); return; }

  // ---- 3. lift yesterday's automatic ZIP blocks ----
  var zrows = zipTab.getDataRange().getValues();
  for (var i = 1; i < zrows.length; i++) {
    var d = zrows[i][0] instanceof Date ? Utilities.formatDate(zrows[i][0], tz, 'yyyy-MM-dd') : String(zrows[i][0]);
    if (d < today && !zrows[i][7] && zrows[i][6]) {
      if (!DRY_RUN) AdsApp.mutate({ campaignCriterionOperation: { remove: String(zrows[i][6]) } });
      zipTab.getRange(i + 1, 8).setValue(DRY_RUN ? 'preview-only' : today);
      log.push('Lifted ZIP block ' + zrows[i][4] + ' on ' + zrows[i][2]);
    }
  }

  // ---- 1+2. today's clicks per ZIP per campaign ----
  var q = "SELECT campaign.id, click_view.location_of_presence.most_specific, click_view.gclid " +
          "FROM click_view WHERE segments.date = '" + today + "' AND campaign.id IN (" + ids.join(',') + ")";
  var counts = {};
  var cv = AdsApp.search(q);
  while (cv.hasNext()) {
    var c = cv.next();
    var pc = c.clickView && c.clickView.locationOfPresence && c.clickView.locationOfPresence.mostSpecific;
    if (!pc) continue;
    var key = c.campaign.id + '|' + pc;
    counts[key] = (counts[key] || 0) + 1;
  }
  var already = {};
  zrows = zipTab.getDataRange().getValues();
  for (var j = 1; j < zrows.length; j++) if (!zrows[j][7]) already[zrows[j][1] + '|' + zrows[j][3]] = true;

  for (var k in counts) {
    if (counts[k] <= MAX_CLICKS_PER_ZIP_PER_DAY || already[k]) continue;
    var parts = k.split('|'), campId = parts[0], geo = parts[1]; // geo = 'geoTargetConstants/9004347'
    var info = geoInfo_(geo);
    if (info.type !== 'Postal Code') { log.push('Heads-up: ' + counts[k] + ' clicks today from ' + info.name + ' (not a ZIP-level location) on "' + camps[campId] + '"'); continue; }
    var zip = info.name;
    var res = '';
    if (!DRY_RUN) {
      var m = AdsApp.mutate({ campaignCriterionOperation: { create: {
        campaign: 'customers/' + cid + '/campaigns/' + campId, negative: true,
        location: { geoTargetConstant: geo } } } });
      res = m.isSuccessful() ? m.getResourceName() : 'ERROR ' + m.getErrorMessages().join('; ');
    }
    zipTab.appendRow([today, campId, camps[campId], geo, zip, counts[k], res, '']);
    log.push((DRY_RUN ? '[PREVIEW] Would block ' : 'Blocked ') + 'ZIP ' + zip + ' on "' + camps[campId] + '" — ' + counts[k] + ' clicks today');
  }

  // ---- 4. IP exclusions from the sheet ----
  var iprows = ipTab.getDataRange().getValues();
  for (var n = 1; n < iprows.length; n++) {
    var ip = String(iprows[n][0]).trim();
    if (!ip || iprows[n][2]) continue;
    var ok = 0;
    ids.forEach(function (id) {
      if (DRY_RUN) return;
      var m2 = AdsApp.mutate({ campaignCriterionOperation: { create: {
        campaign: 'customers/' + cid + '/campaigns/' + id, negative: true, ipBlock: { ipAddress: ip } } } });
      if (m2.isSuccessful()) ok++;
    });
    if (!DRY_RUN) ipTab.getRange(n + 1, 3).setValue(today);
    log.push((DRY_RUN ? '[PREVIEW] Would block IP ' : 'Blocked IP ') + ip + (DRY_RUN ? '' : ' on ' + ok + ' campaigns'));
  }

  if (log.length) {
    MailApp.sendEmail(ALERT_EMAIL, 'AESS Ads click-fraud guard: ' + log.length + ' action(s)', log.join('\n'));
  }
  Logger.log(log.join('\n') || 'Nothing to do.');
}

function geoInfo_(geo) {
  var id = geo.split('/')[1];
  var r = AdsApp.search("SELECT geo_target_constant.name, geo_target_constant.target_type FROM geo_target_constant WHERE geo_target_constant.id = " + id);
  if (!r.hasNext()) return { name: geo, type: '' };
  var g = r.next().geoTargetConstant;
  return { name: g.name, type: g.targetType };
}

function tab_(ss, name, header) {
  var sh = ss.getSheetByName(name) || ss.insertSheet(name);
  if (sh.getLastRow() === 0) sh.appendRow(header);
  return sh;
}
