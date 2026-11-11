/* Meta (Facebook/Instagram) Pixel — AESS site (dataset 704169342972793, "Anwar's Pixel",
   attached to ad account 209986961). Added Nov 11 2026 for retargeting site visitors.
   Loaded by js/ph.js on every page (ph.js is loaded by mega-nav.js or directly).

   Events sent:
     PageView           every page
     ViewContent        every page, tagged with service / area / region from the slug
     Contact            tap on a phone (tel:) or text (sms:) link
     Lead               a quote/contact form sent (and the camera quote builder)
     InitiateCheckout   click to a Stripe checkout link
     SubmitApplication  a form sent from /careers (job seekers — kept out of customer audiences)
   No form field values (names, phones, emails) are ever sent to Meta. */
(function () {
  if (window.__aessFBP) return;
  window.__aessFBP = true;
  var PIXEL_ID = '704169342972793';

  !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
  n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
  document,'script','https://connect.facebook.net/en_US/fbevents.js');

  fbq('init', PIXEL_ID);
  fbq('track', 'PageView');

  /* Page context from the slug, same idea as ph.js (kept independent so either file can load alone). */
  var REGIONS = ['staten-island','brooklyn','bronx','queens','manhattan','nyc','nassau-county','nassau',
    'suffolk-county','suffolk','long-island','westchester-county','westchester','rockland-county','rockland',
    'orange-county','putnam-county','putnam','dutchess-county','dutchess','ulster-county','ulster','hudson-valley'];
  var path = location.pathname.replace(/\/index\.html?$/, '/').replace(/\.html?$/, '');
  var slug = path.replace(/^\/+|\/+$/g, '') || 'home';
  var core = slug.split('/').pop().replace(/-(ny|new-york|newyork|us)$/, '');
  var region = '';
  for (var i = 0; i < REGIONS.length; i++) {
    if (new RegExp('(^|-)' + REGIONS[i] + '(-|$)').test(core)) { region = REGIONS[i]; break; }
  }
  var service = region ? core.slice(0, core.search(new RegExp('(^|-)' + region + '(-|$)'))) : core;
  var isCareers = /^careers/.test(slug);
  var ctx = { content_name: slug, content_category: service || 'home', region: region || 'none' };

  fbq('track', 'ViewContent', ctx);

  function digits(s) { return (s || '').replace(/\D/g, '').slice(-10); }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href') || '';
    if (h.indexOf('tel:') === 0) {
      fbq('track', 'Contact', { content_name: slug, content_category: ctx.content_category, method: 'call', line: digits(h.slice(4)).slice(-4) });
    } else if (h.indexOf('sms:') === 0) {
      fbq('track', 'Contact', { content_name: slug, content_category: ctx.content_category, method: 'text' });
    } else if (/buy\.stripe\.com|checkout\.stripe\.com/.test(h)) {
      fbq('track', 'InitiateCheckout', { content_name: slug, content_category: ctx.content_category });
    }
  }, true);

  /* A form counts as a lead only if a phone or email was filled in (skips search boxes etc.). */
  function hasContact(f) {
    var els = f.querySelectorAll('input, textarea');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (el.type === 'hidden') continue;
      if (/phone|tel|email/i.test((el.name || '') + ' ' + (el.type || '') + ' ' + (el.id || '')) && el.value) return true;
    }
    return false;
  }
  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (!f || f.tagName !== 'FORM' || !hasContact(f)) return;
    if (isCareers) fbq('track', 'SubmitApplication', { content_name: slug });
    else fbq('track', 'Lead', { content_name: slug, content_category: ctx.content_category, region: ctx.region });
  }, true);

  /* For lead senders without a <form> submit (js/quote-builder.js calls this after a successful send). */
  window.aessFbLead = function (extra) {
    var p = { content_name: slug, content_category: ctx.content_category, region: ctx.region };
    if (extra) for (var k in extra) if (Object.prototype.hasOwnProperty.call(extra, k)) p[k] = extra[k];
    fbq('track', 'Lead', p);
  };
})();
