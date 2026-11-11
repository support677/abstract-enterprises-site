/* AESS Google Ads website call tracking (Nov 11 2026).
   Loads the Google tag and turns on "Calls to a phone number on your website" (calls 60s+).
   Ad visitors see a Google forwarding number in place of each number below; the call still rings the
   same line (Quo / AI receptionist), and Google records which ad, keyword and campaign drove it.
   Organic visitors keep seeing the real numbers.
   Injected into every HTML page by netlify/edge-functions/gads-tag.ts, so new factory pages get it too.

   FILL THESE TWO IN from Google Ads -> Goals -> Conversions -> the website-call action -> Tag setup.
   Until both are filled in this file does nothing. */
(function () {
  var AW_ID = 'AW-XXXXXXXXXX';         // Google tag ID, e.g. AW-123456789
  var CALL_LABEL = 'XXXXXXXXXXXXXXXX'; // conversion label for the website-call action

  if (/X{4}/.test(AW_ID) || /X{4}/.test(CALL_LABEL)) return;

  // Every number shown on the site, in the format it appears on the page.
  var NUMBERS = [
    '(646) 490-0629', '(800) 486-0943', '(347) 934-8335', '(845) 640-3835',
    '(718) 679-0359', '(347) 434-6392', '(929) 560-0737', '(914) 877-2578',
    '(631) 407-2884', '(516) 346-5778', '(718) 957-1295'
  ];

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + AW_ID;
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;
  gtag('js', new Date());
  gtag('config', AW_ID);
  for (var i = 0; i < NUMBERS.length; i++) {
    gtag('config', AW_ID + '/' + CALL_LABEL, { phone_conversion_number: NUMBERS[i] });
  }
})();
