/* Ad-platform tags — AESS site (Nov 11 2026).
   One loader for every retargeting / conversion tag except Meta (js/fbp.js) and PostHog (js/ph.js).
   Loaded by js/ph.js on every page. A platform turns on when its ID below is filled in; empty = off.

   Events sent (no names, phones or emails are ever sent):
     page view        every page
     lead             a quote/contact form sent with a phone or email (and the camera quote builder)
     contact          tap on a phone (tel:) or text (sms:) link
   /careers forms are never counted as leads. */
(function () {
  if (window.__aessTags) return;
  window.__aessTags = true;

  var ID = {
    google: [],                 // Google tag IDs: 'AW-XXXXXXXXX' (Google Ads → YouTube/Gmail/Display remarketing) and/or 'G-XXXXXXX' (GA4)
    googleLeadSendTo: '',       // optional 'AW-XXXXXXXXX/label' conversion for form leads
    microsoft: '30005756',      // Microsoft Advertising UET tag "Abstract" (Bing, MSN, Outlook, LinkedIn-profile targeting)
    tiktok: '',                 // TikTok pixel ID
    linkedin: '',               // LinkedIn Insight Tag partner ID (numbers)
    pinterest: '',              // Pinterest tag ID
    reddit: '',                 // Reddit pixel ID (a2_...)
    snapchat: '',               // Snap pixel ID (uuid)
    nextdoor: ''                // Nextdoor pixel ID
  };

  function inject(src) {
    var s = document.createElement('script'); s.async = true; s.src = src;
    var f = document.getElementsByTagName('script')[0];
    if (f && f.parentNode) f.parentNode.insertBefore(s, f); else document.head.appendChild(s);
  }
  var on = {};

  /* Google tag (Google Ads + GA4) */
  if (ID.google.length) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    inject('https://www.googletagmanager.com/gtag/js?id=' + ID.google[0]);
    window.gtag('js', new Date());
    for (var g = 0; g < ID.google.length; g++) window.gtag('config', ID.google[g]);
    on.google = true;
  }

  /* Microsoft Advertising UET */
  if (ID.microsoft) {
    window.uetq = window.uetq || [];
    var u = document.createElement('script'); u.async = true; u.src = 'https://bat.bing.com/bat.js';
    u.onload = function () {
      var o = { ti: ID.microsoft, enableAutoSpaLoading: true };
      o.q = window.uetq; window.uetq = new window.UET(o); window.uetq.push('pageLoad');
    };
    document.head.appendChild(u);
    on.microsoft = true;
  }

  /* TikTok pixel */
  if (ID.tiktok) {
    (function (w, d, t) {
      w.TiktokAnalyticsObject = t; var ttq = w[t] = w[t] || [];
      ttq.methods = ['page', 'track', 'identify', 'instances', 'debug', 'on', 'off', 'once', 'ready', 'alias', 'group', 'enableCookie', 'disableCookie', 'holdConsent', 'revokeConsent', 'grantConsent'];
      ttq.setAndDefer = function (o, m) { o[m] = function () { o.push([m].concat(Array.prototype.slice.call(arguments, 0))); }; };
      for (var i = 0; i < ttq.methods.length; i++) ttq.setAndDefer(ttq, ttq.methods[i]);
      ttq.instance = function (x) { for (var e = ttq._i[x] || [], n = 0; n < ttq.methods.length; n++) ttq.setAndDefer(e, ttq.methods[n]); return e; };
      ttq.load = function (e, n) {
        var r = 'https://analytics.tiktok.com/i18n/pixel/events.js';
        ttq._i = ttq._i || {}; ttq._i[e] = []; ttq._i[e]._u = r; ttq._t = ttq._t || {}; ttq._t[e] = +new Date; ttq._o = ttq._o || {}; ttq._o[e] = n || {};
        inject(r + '?sdkid=' + e + '&lib=' + t);
      };
      ttq.load(ID.tiktok); ttq.page();
    })(window, document, 'ttq');
    on.tiktok = true;
  }

  /* LinkedIn Insight Tag */
  if (ID.linkedin) {
    window._linkedin_partner_id = ID.linkedin;
    window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
    window._linkedin_data_partner_ids.push(ID.linkedin);
    if (!window.lintrk) { window.lintrk = function (a, b) { window.lintrk.q.push([a, b]); }; window.lintrk.q = []; }
    inject('https://snap.licdn.com/li.lms-analytics/insight.min.js');
    on.linkedin = true;
  }

  /* Pinterest tag */
  if (ID.pinterest) {
    if (!window.pintrk) {
      window.pintrk = function () { window.pintrk.queue.push(Array.prototype.slice.call(arguments)); };
      window.pintrk.queue = []; window.pintrk.version = '3.0';
      inject('https://s.pinimg.com/ct/core.js');
    }
    window.pintrk('load', ID.pinterest); window.pintrk('page');
    on.pinterest = true;
  }

  /* Reddit pixel */
  if (ID.reddit) {
    if (!window.rdt) {
      var p = window.rdt = function () { p.sendEvent ? p.sendEvent.apply(p, arguments) : p.callQueue.push(arguments); };
      p.callQueue = [];
      inject('https://www.redditstatic.com/ads/pixel.js');
    }
    window.rdt('init', ID.reddit); window.rdt('track', 'PageVisit');
    on.reddit = true;
  }

  /* Snap pixel */
  if (ID.snapchat) {
    if (!window.snaptr) {
      var a = window.snaptr = function () { a.handleRequest ? a.handleRequest.apply(a, arguments) : a.queue.push(arguments); };
      a.queue = [];
      inject('https://sc-static.net/scevent.min.js');
    }
    window.snaptr('init', ID.snapchat, {}); window.snaptr('track', 'PAGE_VIEW');
    on.snapchat = true;
  }

  /* Nextdoor pixel */
  if (ID.nextdoor) {
    if (!window.ndp) {
      var nd = window.ndp = function () { nd.handleRequest ? nd.handleRequest.apply(nd, arguments) : nd.queue.push(arguments); };
      nd.queue = [];
      inject('https://ads.nextdoor.com/public/pixel/ndp.js');
    }
    window.ndp('init', ID.nextdoor, {}); window.ndp('track', 'PAGE_VIEW');
    on.nextdoor = true;
  }

  /* ---- Events -------------------------------------------------------- */
  function safe(fn) { try { fn(); } catch (_) {} }
  function lead() {
    if (on.google) safe(function () {
      window.gtag('event', 'generate_lead');
      if (ID.googleLeadSendTo) window.gtag('event', 'conversion', { send_to: ID.googleLeadSendTo });
    });
    if (on.microsoft) safe(function () { window.uetq.push('event', 'submit_lead_form', {}); });
    if (on.tiktok) safe(function () { window.ttq.track('SubmitForm'); });
    if (on.pinterest) safe(function () { window.pintrk('track', 'lead'); });
    if (on.reddit) safe(function () { window.rdt('track', 'Lead'); });
    if (on.snapchat) safe(function () { window.snaptr('track', 'SIGN_UP'); });
    if (on.nextdoor) safe(function () { window.ndp('track', 'LEAD'); });
  }
  function contact() {
    if (on.google) safe(function () { window.gtag('event', 'contact'); });
    if (on.microsoft) safe(function () { window.uetq.push('event', 'contact', {}); });
    if (on.tiktok) safe(function () { window.ttq.track('Contact'); });
    if (on.reddit) safe(function () { window.rdt('track', 'Custom', { customEventName: 'Contact' }); });
  }

  var isCareers = /^\/?careers/.test(location.pathname.replace(/^\/+/, ''));
  document.addEventListener('click', function (e) {
    var el = e.target.closest && e.target.closest('a[href]');
    if (!el) return;
    var h = el.getAttribute('href') || '';
    if (h.indexOf('tel:') === 0 || h.indexOf('sms:') === 0) contact();
  }, true);

  function hasContact(f) {
    var els = f.querySelectorAll('input, textarea');
    for (var i = 0; i < els.length; i++) {
      var x = els[i];
      if (x.type === 'hidden') continue;
      if (/phone|tel|email/i.test((x.name || '') + ' ' + (x.type || '') + ' ' + (x.id || '')) && x.value) return true;
    }
    return false;
  }
  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (!f || f.tagName !== 'FORM' || isCareers || !hasContact(f)) return;
    lead();
  }, true);

  /* For the camera quote builder, which sends without a <form> submit. */
  window.aessTagsLead = lead;
})();
