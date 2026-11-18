// AESS Click-Fraud Guard (hourly) — Google Ads script, v2 (Nov 16 2026)
// Readable source. The minified copy in AESS-click-fraud-guard.js is what gets pasted into Google Ads.
//
// What changed from v1:
//  - Counts clicks per ZIP code (user_location_view + segments.geo_target_postal_code) instead of
//    click_view "most specific" location, which almost always came back as the whole borough.
//  - A ZIP with more than MAX_CLICKS clicks today is blocked on that campaign until tomorrow (unchanged rule).
//  - Campaign spike alert: only when a campaign's clicks today are well above its normal day,
//    and the email shows the ZIP breakdown and the clicks by hour.
//  - Every alert is sent once. It only re-sends if the count grows by RESEND_STEP or more.
//  - Shares the log sheet with support@ so it can be opened.

var PREFIX = 'AESS | BK |';
var EXTRA = ['Security Camera Installation Brooklyn NY', 'Door Buzzer Repair Brooklyn'];
var MAX_CLICKS = 5;          // per ZIP, per campaign, per day
var SPIKE_MIN = 8;           // a campaign needs at least this many clicks today to count as a spike
var SPIKE_X = 3;             // ...and at least this many times its normal daily clicks
var RESEND_STEP = 5;         // re-alert only if the count has grown by this much since the last alert
var EMAIL = 'support@abstractenterprisessecuritysystems.com';
var SHEET_NAME = 'AESS Click-Fraud Guard Log';

function main() {
  var f = DriveApp.getFilesByName(SHEET_NAME);
  var ss = f.hasNext() ? SpreadsheetApp.open(f.next()) : SpreadsheetApp.create(SHEET_NAME);
  try { ss.addEditor(EMAIL); } catch (e) {}
  var zt = tab(ss, 'Auto ZIP Blocks', ['Date', 'Campaign ID', 'Campaign', 'Geo', 'ZIP', 'Clicks', 'Criterion', 'Lifted']);
  var ipt = tab(ss, 'Blocked IPs', ['IP address', 'Reason', 'Added on']);
  var at = tab(ss, 'Alerts Sent', ['Date', 'Key', 'Clicks', 'Sent at']);
  var zl = tab(ss, 'ZIP Clicks Today', ['Checked at', 'Campaign', 'ZIP', 'Clicks']);

  var tz = AdsApp.currentAccount().getTimeZone();
  var now = new Date();
  var today = fmt(now, tz);
  var cid = AdsApp.currentAccount().getCustomerId().replace(/-/g, '');
  var log = [];

  // Campaigns covered
  var camps = {};
  each("SELECT campaign.id, campaign.name FROM campaign WHERE campaign.name LIKE '" + PREFIX + "%' AND campaign.status != 'REMOVED'",
    function (r) { camps[r.campaign.id] = r.campaign.name; });
  each("SELECT campaign.id, campaign.name FROM campaign WHERE campaign.name IN ('" + EXTRA.join("', '") + "') AND campaign.status != 'REMOVED'",
    function (r) { camps[r.campaign.id] = r.campaign.name; });
  var ids = Object.keys(camps);
  if (!ids.length) return;
  var inIds = ' AND campaign.id IN (' + ids.join(',') + ')';

  // 1) Lift yesterday's ZIP blocks
  var z = zt.getDataRange().getValues();
  for (var i = 1; i < z.length; i++) {
    var d = z[i][0] instanceof Date ? fmt(z[i][0], tz) : String(z[i][0]);
    if (d < today && !z[i][7] && z[i][6]) {
      AdsApp.mutate({ campaignCriterionOperation: { remove: String(z[i][6]) } });
      zt.getRange(i + 1, 8).setValue(today);
      log.push('Lifted yesterday\'s block on ZIP ' + z[i][4] + ' (' + z[i][2] + ')');
    }
  }

  // 2) Clicks per ZIP today
  var zipClicks = {}; // campId -> { geoRes: clicks }
  each("SELECT campaign.id, segments.geo_target_postal_code, metrics.clicks FROM user_location_view WHERE segments.date = '" + today + "'" + inIds + " AND metrics.clicks > 0",
    function (r) {
      var g = r.segments && r.segments.geoTargetPostalCode;
      if (!g) return;
      var c = Number(r.metrics.clicks) || 0;
      zipClicks[r.campaign.id] = zipClicks[r.campaign.id] || {};
      zipClicks[r.campaign.id][g] = (zipClicks[r.campaign.id][g] || 0) + c;
    });
  var zipName = {};
  function zipOf(res) {
    if (zipName[res]) return zipName[res];
    var n = res;
    each("SELECT geo_target_constant.name FROM geo_target_constant WHERE geo_target_constant.resource_name = '" + res + "'",
      function (r) { n = r.geoTargetConstant.name; });
    zipName[res] = n;
    return n;
  }

  // Snapshot of today's ZIP clicks in the sheet (replaced each run)
  if (zl.getLastRow() > 1) zl.getRange(2, 1, zl.getLastRow() - 1, 4).clearContent();
  var stamp = Utilities.formatDate(now, tz, 'yyyy-MM-dd HH:mm');
  var snap = [];
  for (var c1 in zipClicks) for (var g1 in zipClicks[c1]) snap.push([stamp, camps[c1], zipOf(g1), zipClicks[c1][g1]]);
  snap.sort(function (a, b) { return b[3] - a[3]; });
  if (snap.length) zl.getRange(2, 1, snap.length, 4).setValues(snap);

  // 3) Block any ZIP over MAX_CLICKS (once per day per campaign+ZIP)
  var blocked = {};
  z = zt.getDataRange().getValues();
  for (var j = 1; j < z.length; j++) if (!z[j][7]) blocked[z[j][1] + '|' + z[j][3]] = 1;
  for (var c2 in zipClicks) for (var g2 in zipClicks[c2]) {
    var n2 = zipClicks[c2][g2];
    if (n2 <= MAX_CLICKS || blocked[c2 + '|' + g2]) continue;
    var m = AdsApp.mutate({ campaignCriterionOperation: { create: {
      campaign: 'customers/' + cid + '/campaigns/' + c2, negative: true, location: { geoTargetConstant: g2 } } } });
    var rn = m.isSuccessful() ? m.getResourceName() : '';
    zt.appendRow([today, c2, camps[c2], g2, zipOf(g2), n2, rn, '']);
    log.push((rn ? 'BLOCKED ZIP ' : 'FAILED to block ZIP ') + zipOf(g2) + ' on ' + camps[c2] + ': ' + n2 + ' clicks today. Block lifts tomorrow.');
  }

  // 4) Campaign spike check (vs. its normal day over the last 14 days)
  var todayClicks = {}, hours = {};
  each("SELECT campaign.id, segments.hour, metrics.clicks FROM campaign WHERE segments.date = '" + today + "'" + inIds + " AND metrics.clicks > 0",
    function (r) {
      var c = Number(r.metrics.clicks) || 0;
      todayClicks[r.campaign.id] = (todayClicks[r.campaign.id] || 0) + c;
      hours[r.campaign.id] = hours[r.campaign.id] || {};
      hours[r.campaign.id][r.segments.hour] = (hours[r.campaign.id][r.segments.hour] || 0) + c;
    });
  var past = {};
  var from = fmt(new Date(now.getTime() - 14 * 864e5), tz), to = fmt(new Date(now.getTime() - 864e5), tz);
  each("SELECT campaign.id, metrics.clicks FROM campaign WHERE segments.date BETWEEN '" + from + "' AND '" + to + "'" + inIds,
    function (r) { past[r.campaign.id] = (past[r.campaign.id] || 0) + (Number(r.metrics.clicks) || 0); });

  var sent = {};
  var a = at.getDataRange().getValues();
  for (var k = 1; k < a.length; k++) {
    var ad = a[k][0] instanceof Date ? fmt(a[k][0], tz) : String(a[k][0]);
    if (ad === today) sent[a[k][1]] = Math.max(sent[a[k][1]] || 0, Number(a[k][2]) || 0);
  }
  for (var c3 in todayClicks) {
    var t = todayClicks[c3], avg = (past[c3] || 0) / 14;
    if (t < SPIKE_MIN || t < SPIKE_X * Math.max(avg, 1)) continue;
    var key = 'spike|' + c3;
    if (sent[key] && t - sent[key] < RESEND_STEP) continue;
    var zs = [];
    for (var g3 in (zipClicks[c3] || {})) zs.push([zipOf(g3), zipClicks[c3][g3]]);
    zs.sort(function (x, y) { return y[1] - x[1]; });
    var hs = [];
    Object.keys(hours[c3] || {}).sort(function (x, y) { return x - y; }).forEach(function (h) {
      hs.push(hr(h) + ': ' + hours[c3][h]);
    });
    log.push('SPIKE: ' + camps[c3] + ' has ' + t + ' clicks today (normal day about ' + avg.toFixed(1) + ').\n' +
      '   By ZIP: ' + (zs.length ? zs.map(function (q) { return q[0] + ' (' + q[1] + ')'; }).join(', ') : 'Google hasn\'t reported ZIPs yet') + '\n' +
      '   By hour: ' + (hs.join(', ') || 'n/a') + '\n' +
      '   Nothing was paused. ZIPs over ' + MAX_CLICKS + ' are blocked automatically.');
    at.appendRow([today, key, t, stamp]);
  }

  // 5) Manually listed IPs
  var ip = ipt.getDataRange().getValues();
  for (var p = 1; p < ip.length; p++) {
    var addr = String(ip[p][0]).trim();
    if (!addr || ip[p][2]) continue;
    var okc = 0;
    ids.forEach(function (id) {
      var mm = AdsApp.mutate({ campaignCriterionOperation: { create: {
        campaign: 'customers/' + cid + '/campaigns/' + id, negative: true, ipBlock: { ipAddress: addr } } } });
      if (mm.isSuccessful()) okc++;
    });
    ipt.getRange(p + 1, 3).setValue(today);
    log.push('Blocked IP ' + addr + ' on ' + okc + ' campaigns');
  }

  if (log.length) MailApp.sendEmail(EMAIL, 'AESS Ads click-fraud guard: ' + log.length + ' item(s)', log.join('\n\n') + '\n\nLog: ' + ss.getUrl());
  Logger.log((log.join('\n\n') || 'Nothing to do.') + '\n\nZIP clicks today:\n' +
    (snap.map(function (s) { return s[1] + ' | ' + s[2] + ' | ' + s[3]; }).join('\n') || 'none reported yet') + '\n\nLog sheet: ' + ss.getUrl());
}

function each(q, fn) { var it = AdsApp.search(q); while (it.hasNext()) fn(it.next()); }
function fmt(d, tz) { return Utilities.formatDate(d, tz, 'yyyy-MM-dd'); }
function hr(h) { h = Number(h); return (h % 12 || 12) + (h < 12 ? 'am' : 'pm'); }
function tab(ss, name, h) { var sh = ss.getSheetByName(name) || ss.insertSheet(name); if (sh.getLastRow() === 0) sh.appendRow(h); return sh; }
