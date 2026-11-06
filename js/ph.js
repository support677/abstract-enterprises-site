/* PostHog analytics — AESS site (project 713268).
   Loaded by mega-nav.js on every page (or directly).
   Module 3 (Nov 5 2026): every event carries page_slug / service / area / region,
   first-touch source is kept for the person, and lead forms carry the PostHog
   ids + attribution through to /api/contact so a lead (and later a paid job)
   can be tied back to the page, post and channel that produced it. */
(function () {
  if (window.__aessPH) return;
  window.__aessPH = true;
  !function(t,e){var o,n,p,r;e.__SV||(window.posthog&&window.posthog.__loaded)||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);

  /* ---- Page context: service × area from the slug ---------------------- */
  // Every landing page slug ends in one of these regions (checked across all 3,400 pages).
  var REGIONS = [
    ['staten-island', 'Staten Island'], ['brooklyn', 'Brooklyn'], ['bronx', 'Bronx'],
    ['queens', 'Queens'], ['manhattan', 'Manhattan'], ['nyc', 'NYC'],
    ['nassau-county', 'Nassau'], ['nassau', 'Nassau'], ['suffolk-county', 'Suffolk'], ['suffolk', 'Suffolk'],
    ['long-island', 'Long Island'], ['westchester-county', 'Westchester'], ['westchester', 'Westchester'],
    ['rockland-county', 'Rockland'], ['rockland', 'Rockland'], ['orange-county', 'Orange'],
    ['putnam-county', 'Putnam'], ['putnam', 'Putnam'], ['dutchess-county', 'Dutchess'], ['dutchess', 'Dutchess'],
    ['ulster-county', 'Ulster'], ['ulster', 'Ulster'], ['hudson-valley', 'Hudson Valley']
  ];
  function titleCase(s) { return s.replace(/-/g, ' ').replace(/\b\w/g, function (c) { return c.toUpperCase(); }); }
  var SERVICES = 'apartment-building-security-camera-installation|construction-site-security-camera-installation|digital-watchdog-camera-installation-prices|residential-security-camera-installation|commercial-security-camera-installation|ens-security-camera-installation-prices|tp-link-vigi-camera-installation-prices|first-alert-camera-installation-prices|gw-security-camera-installation-prices|hikvision-security-camera-installation|warehouse-security-camera-installation|invid-tech-camera-installation-prices|geovision-camera-installation-prices|honeywell-camera-installation-prices|school-security-camera-installation|guarding-vision-app-support-repair|super-live-plus-app-support-repair|d-link-camera-installation-prices|eyemax-camera-installation-prices|hanwha-camera-installation-prices|turing-camera-installation-prices|lilin-camera-installation-prices|q-see-camera-installation-prices|speco-camera-installation-prices|swann-camera-installation-prices|tp-link-tapo-camera-installation|arlo-camera-installation-prices|axis-camera-installation-prices|eufy-camera-installation-prices|google-nest-camera-installation|parking-lot-camera-installation|structured-cabling-installation|wyze-camera-installation-prices|zosi-camera-installation-prices|floodlight-camera-installation|hik-connect-app-support-repair|alarm-com-camera-installation|night-owl-camera-installation|doorbell-camera-installation|security-camera-installation|ubiquiti-camera-installation|wireless-camera-installation|access-control-installation|amcrest-camera-installation|capture-camera-installation|commercial-security-systems|luminys-camera-installation|reolink-camera-installation|security-camera-maintenance|uniview-camera-installation|avycon-camera-installation|solar-surveillance-trailer|structured-cabling-pricing|annke-camera-installation|blink-camera-installation|dahua-camera-installation|lorex-camera-installation|door-buzzer-installation|fiber-optic-installation|low-voltage-installation|ring-camera-installation|dmss-app-support-repair|fire-alarm-installation|security-camera-pricing|smart-lock-installation|smart-pss-support-setup|video-wall-installation|security-camera-repair|av-sound-installation|intercom-installation|soundbar-installation|network-cable-repair|network-installation|alarm-installation|door-buzzer-repair|sonos-installation|tv-mounting-prices|cat6-installation|nvr-installation|security-cameras|home-automation|intercom-repair|tv-installation|cat6-repair|dvr-upgrade'.split('|'); // longest first
  function pageContext() {
    var path = location.pathname.replace(/\/index\.html?$/, '/').replace(/\.html?$/, '');
    var slug = path.replace(/^\/+|\/+$/g, '') || 'home';
    var last = slug.split('/').pop();
    var core = last.replace(/-(ny|new-york|newyork|us)$/, '');
    var ctx = { page_slug: slug, page_type: 'other', service: null, area: null, locality: null, region: null };
    if (slug === 'home') { ctx.page_type = 'home'; return ctx; }
    // Region = the LAST region token in the slug (e.g. ...-white-plains-westchester-county).
    var hit = null, at = -1;
    for (var i = 0; i < REGIONS.length; i++) {
      var re = new RegExp('(^|-)' + REGIONS[i][0] + '$');
      var m = re.exec(core);
      if (m && (at === -1 || m.index < at)) { at = m.index; hit = REGIONS[i]; }
    }
    if (!hit) { // region in the middle (rare) — take the first one found
      for (var j = 0; j < REGIONS.length; j++) {
        var m2 = new RegExp('(^|-)' + REGIONS[j][0] + '(-|$)').exec(core);
        if (m2 && (at === -1 || m2.index < at)) { at = m2.index; hit = REGIONS[j]; }
      }
    }
    var head = hit ? core.slice(0, at) : core;
    var svc = null;
    for (var k = 0; k < SERVICES.length; k++) {
      if (head === SERVICES[k] || head.indexOf(SERVICES[k] + '-') === 0) { svc = SERVICES[k]; break; }
    }
    var loc = svc ? head.slice(svc.length + 1) : '';
    if (!svc) svc = head || null;
    if (hit) ctx.region = hit[1];
    ctx.service = svc ? titleCase(svc) : null;
    ctx.locality = loc ? titleCase(loc) : null;
    ctx.area = ctx.locality || (hit ? ctx.region : null);
    if (!svc && hit) ctx.page_type = 'area';
    else if (svc && /prices?$|pricing$/.test(svc)) ctx.page_type = 'price';
    else if (svc && hit) ctx.page_type = 'service_area';
    return ctx;
  }
  var CTX = pageContext();
  window.aessPage = CTX;

  // Known Quo lines (Oct 2 2026 rule) — labels the line a call/text went to.
  var LINES = {
    '5162617110': 'Quo Nassau', '6315705699': 'Quo Suffolk', '9144365218': 'Quo Westchester',
    '8452624137': 'Quo Hudson Valley', '9172683951': 'Quo NYC', '8004860943': 'Toll-free',
    '9297305331': 'Main', '7186790359': 'Office', '3473492067': 'Allo AI receptionist'
  };
  function digits(h) { var d = (h || '').replace(/[^0-9]/g, ''); return d.length === 11 && d[0] === '1' ? d.slice(1) : d; }
  function ctaSpot(el) {
    var tag = el.closest('[data-cta]');
    if (tag) return tag.getAttribute('data-cta');
    if (el.closest('header, nav, .mega-nav')) return 'header';
    if (el.closest('footer')) return 'footer';
    if (el.closest('.sticky, .sticky-cta, .mobile-cta, [class*="sticky"], [class*="float"]')) return 'sticky';
    if (el.closest('.hero, [class*="hero"]')) return 'hero';
    return 'body';
  }

  posthog.init('phc_wJyrBYx3gBLsevhvXiMhFUSFt2JjFeK6iSXyhrHRnogj', {
    api_host: 'https://us.i.posthog.com',
    person_profiles: 'identified_only',
    autocapture: true,
    capture_pageview: true,
    capture_pageleave: true,
    capture_heatmaps: true,
    capture_dead_clicks: true,
    enable_heatmaps: true,
    disable_session_recording: false,
    session_recording: { maskAllInputs: true, maskTextSelector: '[data-ph-mask]' },
    loaded: function (ph) {
      var props = { page_slug: CTX.page_slug, page_type: CTX.page_type };
      if (CTX.service) props.service = CTX.service;
      if (CTX.area) props.area = CTX.area;
      if (CTX.locality) props.locality = CTX.locality;
      if (CTX.region) props.region = CTX.region;
      ph.register(props);
      // First touch: where this visitor first landed and from what source.
      var q = new URLSearchParams(location.search);
      ph.register_once({
        first_landing_slug: CTX.page_slug,
        first_service: CTX.service || '',
        first_region: CTX.region || '',
        first_utm_source: q.get('utm_source') || '',
        first_utm_medium: q.get('utm_medium') || '',
        first_utm_campaign: q.get('utm_campaign') || '',
        first_utm_content: q.get('utm_content') || '',
        first_referrer: document.referrer || '$direct'
      });
    }
  });

  /* Server-side copy of call/text taps for the nightly attribution match
     (survives ad-blockers; no personal data). */
  var TOUCH_URL = 'https://aess-hcp-webhooks.onrender.com/touch';
  function beacon(event, props) {
    try {
      var q = new URLSearchParams(location.search);
      var g = function (k) { try { return posthog.get_property(k) || ''; } catch (_) { return ''; } };
      var body = JSON.stringify({
        event: event, ts: new Date().toISOString(),
        touch_id: event + '-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8),
        page_slug: CTX.page_slug, service: CTX.service, area: CTX.area, region: CTX.region,
        number: props.number, line: props.line,
        utm_source: q.get('utm_source') || g('first_utm_source'), utm_medium: q.get('utm_medium') || g('first_utm_medium'),
        utm_campaign: q.get('utm_campaign') || g('first_utm_campaign'), utm_content: q.get('utm_content') || g('first_utm_content'),
        first_referrer: g('first_referrer') || document.referrer || '$direct', first_landing: g('first_landing_slug'),
        distinct_id: (function () { try { return posthog.get_distinct_id(); } catch (_) { return ''; } })()
      });
      if (navigator.sendBeacon) navigator.sendBeacon(TOUCH_URL, new Blob([body], { type: 'text/plain' }));
      else fetch(TOUCH_URL, { method: 'POST', body: body, keepalive: true, mode: 'no-cors' });
    } catch (_) {}
  }

  /* ---- Clicks: call / text / email / checkout -------------------------- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href') || '';
    var base = { cta_location: ctaSpot(a), cta_text: (a.textContent || '').trim().slice(0, 60) };
    if (h.indexOf('tel:') === 0) {
      var n = digits(h.slice(4));
      base.number = n; base.line = LINES[n] || 'Tracking ' + n.slice(-4);
      posthog.capture('click_to_call', base);
      beacon('click_to_call', base);
    } else if (h.indexOf('sms:') === 0) {
      var s = digits(h.slice(4).split('?')[0].split('&')[0]);
      base.number = s; base.line = LINES[s] || 'Tracking ' + s.slice(-4);
      posthog.capture('click_to_text', base);
      beacon('click_to_text', base);
    } else if (h.indexOf('mailto:') === 0) {
      posthog.capture('click_email', base);
    } else if (/buy\.stripe\.com|checkout\.stripe\.com/.test(h)) {
      base.href = h;
      posthog.capture('checkout_click', base);
    }
  }, true);

  /* ---- Forms: tag the submission + carry attribution to /api/contact --- */
  function setHidden(f, name, val) {
    if (val == null || val === '') return;
    var i = f.querySelector('input[type="hidden"][name="' + name + '"]');
    if (!i) { i = document.createElement('input'); i.type = 'hidden'; i.name = name; f.appendChild(i); }
    i.value = String(val).slice(0, 300);
  }
  function filled(f, re) {
    var els = f.querySelectorAll('input, textarea, select');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (el.type === 'hidden') continue;
      if (re.test((el.name || '') + ' ' + (el.type || '') + ' ' + (el.id || '')) && el.value) return true;
    }
    return false;
  }
  function stamp(f) {
    var g = function (k) { try { return posthog.get_property(k); } catch (_) { return ''; } };
    var id = ''; var sid = '';
    try { id = posthog.get_distinct_id(); sid = posthog.get_session_id(); } catch (_) {}
    setHidden(f, 'ph_distinct_id', id);
    setHidden(f, 'ph_session_id', sid);
    setHidden(f, 'page_slug', CTX.page_slug);
    setHidden(f, 'lead_service', CTX.service);
    setHidden(f, 'lead_area', CTX.area);
    setHidden(f, 'lead_region', CTX.region);
    var q = new URLSearchParams(location.search);
    setHidden(f, 'utm_source', q.get('utm_source') || g('first_utm_source'));
    setHidden(f, 'utm_medium', q.get('utm_medium') || g('first_utm_medium'));
    setHidden(f, 'utm_campaign', q.get('utm_campaign') || g('first_utm_campaign'));
    setHidden(f, 'utm_content', q.get('utm_content') || g('first_utm_content'));
    setHidden(f, 'first_landing', g('first_landing_slug'));
    setHidden(f, 'first_referrer', g('first_referrer'));
  }
  // For lead senders that build FormData without a <form> submit (js/quote-builder.js).
  window.aessStamp = stamp;
  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (!f || f.tagName !== 'FORM') return;
    stamp(f); // runs in the capture phase, before any fetch()/FormData handler reads the form
    posthog.capture('form_submit', {
      form: f.id || f.getAttribute('name') || f.className || 'form',
      form_action: f.getAttribute('action') || '',
      cta_location: ctaSpot(f),
      has_phone: filled(f, /phone|tel/i),
      has_email: filled(f, /email/i)
    });
  }, true);
})();
