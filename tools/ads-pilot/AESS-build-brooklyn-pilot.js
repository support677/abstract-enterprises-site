/* AESS Brooklyn security-camera neighborhood pilot builder. Everything is created PAUSED.
   Run Preview first: it validates every operation without changing anything. */
var DATA_URL = 'https://abstractenterprisessecuritysystems.com/tools/ads-pilot/brooklyn-pilot-data.json';
function main() {
  var DATA = JSON.parse(UrlFetchApp.fetch(DATA_URL + '?v=' + Date.now()).getContentText());
  Logger.log('Loaded ' + DATA.length + ' campaigns');
  var cid = AdsApp.currentAccount().getCustomerId().replace(/-/g, '');
  var P = 'customers/' + cid + '/';
  var existing = {};
  var it = AdsApp.search("SELECT campaign.name FROM campaign WHERE campaign.status != 'REMOVED'");
  while (it.hasNext()) existing[it.next().campaign.name] = true;
  var tmp = -1, ok = 0, bad = 0;
  DATA.forEach(function (c) {
    if (existing[c.n]) { Logger.log('SKIP (already exists): ' + c.n); return; }
    var ops = [], b = P + 'campaignBudgets/' + (tmp--), cr = P + 'campaigns/' + (tmp--);
    ops.push({ campaignBudgetOperation: { create: { resourceName: b, name: c.n + ' budget', amountMicros: Math.round(c.b * 1e6), deliveryMethod: 'STANDARD', explicitlyShared: false } } });
    ops.push({ campaignOperation: { create: { resourceName: cr, name: c.n, status: 'PAUSED', advertisingChannelType: 'SEARCH', campaignBudget: b, manualCpc: { enhancedCpcEnabled: false },
      networkSettings: { targetGoogleSearch: true, targetSearchNetwork: false, targetContentNetwork: false, targetPartnerSearchNetwork: false },
      geoTargetTypeSetting: { positiveGeoTargetType: 'PRESENCE', negativeGeoTargetType: 'PRESENCE' },
      containsEuPoliticalAdvertising: 'DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING' } } });
    ops.push({ campaignCriterionOperation: { create: { campaign: cr, language: { languageConstant: 'languageConstants/1000' } } } });
    c.loc.forEach(function (g) { ops.push({ campaignCriterionOperation: { create: { campaign: cr, location: { geoTargetConstant: 'geoTargetConstants/' + g } } } }); });
    c.ex.forEach(function (g) { ops.push({ campaignCriterionOperation: { create: { campaign: cr, negative: true, location: { geoTargetConstant: 'geoTargetConstants/' + g } } } }); });
    c.neg.forEach(function (k) { ops.push({ campaignCriterionOperation: { create: { campaign: cr, negative: true, keyword: { text: k, matchType: 'PHRASE' } } } }); });
    c.ag.forEach(function (a) {
      var ag = P + 'adGroups/' + (tmp--);
      ops.push({ adGroupOperation: { create: { resourceName: ag, campaign: cr, name: a.n, status: 'ENABLED', type: 'SEARCH_STANDARD', cpcBidMicros: Math.round(a.cpc * 1e6) } } });
      a.kw.forEach(function (k) { ops.push({ adGroupCriterionOperation: { create: { adGroup: ag, status: 'ENABLED', keyword: { text: k, matchType: 'PHRASE' } } } }); });
      var h = a.ad.h.map(function (t, i) { return i === 0 ? { text: t, pinnedField: 'HEADLINE_1' } : { text: t }; });
      ops.push({ adGroupAdOperation: { create: { adGroup: ag, status: 'ENABLED', ad: { finalUrls: [a.ad.u],
        responsiveSearchAd: { headlines: h, descriptions: a.ad.d.map(function (t) { return { text: t }; }), path1: a.ad.p1, path2: a.ad.p2 } } } } });
    });
    var res = AdsApp.mutateAll(ops, { partialFailure: false });
    var errs = [];
    res.forEach(function (r) { if (r.isSuccessful()) ok++; else { bad++; errs = errs.concat(r.getErrorMessages()); } });
    Logger.log((errs.length ? 'ERRORS ' : 'OK ') + c.n + ' — ' + ops.length + ' operations' + (errs.length ? ': ' + errs.slice(0, 5).join(' || ') : ''));
  });
  Logger.log('DONE. successful=' + ok + ' failed=' + bad);
}
