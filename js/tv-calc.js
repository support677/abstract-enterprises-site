/* AESS TV installation calculator — ONE file for every TV page.
 * Change a price here and every TV page updates.
 *
 * Pricing (Oct 13 2026):
 *  - Base mounting labor benchmarked to Best Buy Geek Squad TV Basic Mounting
 *    ($179.99 up to 90", customer's bracket) for the $195/hr zones; other zones
 *    scale with the AESS hourly rate for that area.
 *  - Bracket is NOT included (same as Best Buy). Brackets sell at list price
 *    (Best Buy regular price, Oct 13 2026) with model numbers.
 *  - Bigger TVs (86"+) are priced as a two-technician job inside the size tier.
 *  - Paid in full at checkout through /pay (Stripe -> Housecall Pro job ->
 *    customer picks a 2-hour arrival window after payment).
 *  - Manhattan adds the $150 parking charge.
 *
 * Page markup: <div id="aessTvCalc" data-area="bronx" data-label="the Bronx"></div>
 */
(function () {
  var ZONES = {
    brooklyn:     { base: 179.99, hourly: 195, label: 'Brooklyn' },
    queens:       { base: 179.99, hourly: 195, label: 'Queens' },
    nyc:          { base: 179.99, hourly: 195, label: 'NYC' },
    bronx:        { base: 209.99, hourly: 225, label: 'the Bronx' },
    statenisland: { base: 209.99, hourly: 225, label: 'Staten Island' },
    nassau:       { base: 209.99, hourly: 225, label: 'Nassau County' },
    longisland:   { base: 209.99, hourly: 225, label: 'Long Island' },
    manhattan:    { base: 244.99, hourly: 265, label: 'Manhattan', parking: 150 },
    westchester:  { base: 219.99, hourly: 235, label: 'Westchester' },
    rockland:     { base: 219.99, hourly: 235, label: 'Rockland County' },
    hudsonvalley: { base: 219.99, hourly: 235, label: 'the Hudson Valley' },
    suffolk:      { base: 229.99, hourly: 250, label: 'Suffolk County' },
    orange:       { base: 229.99, hourly: 250, label: 'Orange County' },
    putnam:       { base: 229.99, hourly: 250, label: 'Putnam County' },
    dutchess:     { base: 254.99, hourly: 275, label: 'Dutchess County' },
    ulster:       { base: 254.99, hourly: 275, label: 'Ulster County' }
  };

  Object.keys(ZONES).forEach(function (k) {
    var z = ZONES[k];
    z.stand = Math.round(119.99 * z.hourly / 195) - 0.01;     // 119.99 / 137.99 / 144.99 / 152.99 / 162.99 / 168.99
  });

  var SIZES = [
    { id: 's55', t: '32"–55"', p: 0 },
    { id: 's75', t: '56"–75"', p: 0 },
    { id: 's85', t: '76"–85"', p: 40 },
    { id: 's97', t: '86"–97"', p: 150, note: '2 technicians' },
    { id: 's98', t: '98"+', p: 220, note: '2 technicians' }
  ];
  var STYLES = [
    { id: 'stand', t: 'On a stand — no wall mount', p: 0, note: 'unbox, set up & connect' },
    { id: 'flat', t: 'Flat / Tilt', p: 0 },
    { id: 'full', t: 'Full-Motion', p: 40 },
    { id: 'frame', t: 'Samsung Frame / Art TV', p: 70, note: 'flush, gallery-level' },
    { id: 'fire', t: 'Over Fireplace', p: 130 },
    { id: 'pull', t: 'Pull-Down Fireplace', p: 160 },
    { id: 'ceil', t: 'Ceiling', p: 85 },
    { id: 'outdoor', t: 'Outdoor (patio / deck)', p: 90, note: 'weather-sealed' }
  ];
  var WALLS = [
    { id: 'dry', t: 'Drywall — wood studs', p: 0, note: 'most houses' },
    { id: 'metal', t: 'Drywall — metal studs', p: 30, note: 'most apartment buildings' },
    { id: 'plaster', t: 'Plaster', p: 45 },
    { id: 'brick', t: 'Brick / Stone', p: 65 },
    { id: 'conc', t: 'Concrete', p: 75 },
    { id: 'unsure', t: 'Not Sure', p: 0, note: 'we confirm on site' }
  ];
  // List prices = Best Buy regular price, Oct 13 2026.
  var BRACKETS = [
    { id: 'own', t: 'I have my own bracket', p: 0 },
    { id: 'framekit', t: 'Samsung Frame slim mount (comes with the TV)', p: 0 },
    { id: 'vll5', t: 'Sanus VLL5-B2 Premium Fixed (51"–80")', p: 159.99 },
    { id: 'vxl7', t: 'Sanus VXL7-B2 XL Fixed (65"–140")', p: 199.99 },
    { id: 'vlt7', t: 'Sanus VLT7-B2 Advanced Tilt 4D (42"–90")', p: 199.99 },
    { id: 'vmf822', t: 'Sanus VMF822-B2 Full-Motion (32"–65")', p: 279.99 },
    { id: 'vlf828', t: 'Sanus VLF828-B2 Full-Motion (42"–90")', p: 429.99 },
    { id: 'vxf830', t: 'Sanus VXF830 XL Full-Motion (65"–100")', p: 499.99 },
    { id: 'mm340', t: 'MantelMount MM340 Pull-Down (44"–80")', p: 199.95 },
    { id: 'mm700', t: 'MantelMount MM700 Pull-Down (50"–90")', p: 399.95 },
    { id: 'ceil', t: 'Sanus Large Ceiling Mount (37"–70")', p: 449.99 },
    { id: 'terrace', t: 'Samsung Terrace Outdoor Mount (up to 55")', p: 149.99 },
    { id: 'outtilt', t: 'Sanus Premium Outdoor Tilt (37"–95")', p: 239.99 },
    { id: 'outfull', t: 'SunBriteTV Outdoor Full-Motion (37"–80")', p: 589.99 }
  ];
  var ADDONS = [
    { id: 'inwall', t: 'In-wall cable concealment (kit included)', p: 169 },
    { id: 'race', t: 'Paintable cord cover (on-wall)', p: 59 },
    { id: 'sbplace', t: 'Soundbar placed & connected', p: 79 },
    { id: 'sbmount', t: 'Soundbar wall-mounted & connected', p: 129 },
    { id: 'sbbracket', t: 'Sanus universal soundbar bracket', p: 84.99 },
    { id: 'stream', t: 'Apple TV / Roku / Fire TV / Google TV setup', p: 49 },
    { id: 'game', t: 'Gaming console hookup', p: 49 },
    { id: 'avr', t: 'A/V receiver & speaker setup', p: 129 },
    { id: 'sonos', t: 'Sonos / wireless surround setup', p: 125 },
    { id: 'remote', t: 'Universal remote programming', p: 99 },
    { id: 'led', t: 'LED bias lighting', p: 75 },
    { id: 'theater', t: 'Full home theater setup', p: 350 },
    { id: 'remove', t: 'Take down old TV', p: 85 },
    { id: 'haul', t: 'Haul away old TV for recycling', p: 79 },
    { id: 'coi', t: 'COI for your building', p: 0 }
  ];

  var host = document.getElementById('aessTvCalc');
  if (!host) return;
  var areaKey = (host.getAttribute('data-area') || 'brooklyn').toLowerCase();
  var Z = ZONES[areaKey] || ZONES.brooklyn;
  var where = host.getAttribute('data-label') || Z.label;
  var S = { size: 's55', style: 'flat', wall: 'dry', bracket: 'own', addons: {}, qty: 1 };

  function money(n) { return '$' + n.toLocaleString('en-US', { minimumFractionDigits: n % 1 ? 2 : 0, maximumFractionDigits: 2 }); }
  function find(list, id) { for (var i = 0; i < list.length; i++) if (list[i].id === id) return list[i]; return list[0]; }
  function r2(n) { return Math.round(n * 100) / 100; }

  var css = '' +
    '.atv-bar{position:fixed;left:0;right:0;bottom:0;z-index:9999;font-family:inherit}' +
    '.atv-toggle{background:#0b1f3a;color:#fff;padding:14px 18px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;border-top:3px solid #00a3ff}' +
    '.atv-toggle h4{margin:0;font-size:1rem}.atv-toggle span{font-size:.82rem;opacity:.75}' +
    '.atv-arrow{font-size:1.4rem;color:#00a3ff;transition:transform .3s}.atv-arrow.open{transform:rotate(180deg)}' +
    '#calcPanel.atv-panel{background:#fff;color:#1a2433;max-height:0;overflow:hidden;transition:max-height .45s ease;box-shadow:0 -10px 40px rgba(0,0,0,.15)}' +
    '#calcPanel.atv-panel.open{max-height:88vh;overflow-y:auto}' +
    '.atv-inner{max-width:820px;margin:0 auto;padding:24px 16px 110px}' +
    '.atv-inner h3{text-align:center;margin:0 0 4px;font-size:1.25rem;color:#0b1f3a}' +
    '.atv-sub{text-align:center;color:#5a6578;font-size:.88rem;margin:0 0 20px}' +
    '.atv-sec{margin:0 0 20px}.atv-lab{font-weight:800;font-size:.85rem;text-transform:uppercase;letter-spacing:.5px;color:#0b1f3a;margin:0 0 8px}' +
    '.atv-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}' +
    '.atv-grid.wide{grid-template-columns:repeat(auto-fill,minmax(240px,1fr))}' +
    '.atv-opt{border:2px solid #dde3ea;border-radius:8px;padding:11px 10px;background:#fff;cursor:pointer;text-align:left;font:inherit;color:#1a2433;width:100%}' +
    '.atv-opt:hover{border-color:#00a3ff}.atv-opt.sel{border-color:#00a3ff;background:#eaf6ff;box-shadow:0 0 0 1px #00a3ff}' +
    '.atv-opt b{display:block;font-size:.9rem}.atv-opt small{display:block;color:#0077cc;font-size:.78rem;margin-top:2px}' +
    '.atv-qty{display:flex;align-items:center;gap:14px}.atv-qty button{width:36px;height:36px;border:2px solid #dde3ea;border-radius:8px;background:#fff;font-size:1.2rem;cursor:pointer}' +
    '.atv-qty span{font-size:1.3rem;font-weight:800;min-width:30px;text-align:center}' +
    '.atv-est{background:linear-gradient(135deg,#0b1f3a,#14345e);color:#fff;border-radius:12px;padding:20px;margin-top:22px}' +
    '.atv-est h4{margin:0;font-size:.8rem;text-transform:uppercase;letter-spacing:1px;opacity:.7}' +
    '.atv-total{font-size:2.3rem;font-weight:800;line-height:1.1;margin:4px 0 10px}' +
    '.atv-line{display:flex;justify-content:space-between;gap:10px;font-size:.86rem;padding:2px 0;opacity:.88}' +
    '.atv-note{font-size:.76rem;opacity:.65;margin:10px 0 0}' +
    '.atv-cta{display:block;text-align:center;background:#00a3ff;color:#fff !important;padding:14px;border-radius:8px;font-weight:800;margin-top:14px;text-decoration:none}' +
    '.atv-cta.alt{background:transparent;border:2px solid rgba(255,255,255,.35)}' +
    '.atv-setup{border:2px dashed #00a3ff;border-radius:12px;padding:16px;margin-top:22px;background:#f5fbff}' +
    '.atv-setup h4{margin:0 0 4px;color:#0b1f3a}.atv-setup p{margin:0 0 10px;color:#3c4858;font-size:.9rem}' +
    '.atv-setup a{display:inline-block;background:#0b1f3a;color:#fff !important;padding:11px 16px;border-radius:8px;font-weight:700;text-decoration:none}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  function opts(group, list, wide) {
    return '<div class="atv-grid' + (wide ? ' wide' : '') + '">' + list.map(function (o) {
      var price = o.p ? '+' + money(o.p) : (group === 'bracket' || group === 'size' || group === 'style' || group === 'wall' ? 'Included' : 'Free');
      if (group === 'bracket' && o.p === 0) price = '$0';
      return '<button type="button" class="atv-opt" data-g="' + group + '" data-id="' + o.id + '"><b>' + o.t + '</b><small>' +
        price + (o.note ? ' · ' + o.note : '') + '</small></button>';
    }).join('') + '</div>';
  }

  var PROJ = r2(Z.base + 70), SCREEN = 149;
  var P = { proj: true, screen: false };
  var firstHour = Z.hourly, half = Math.round(Z.hourly / 2), setupPrice = firstHour + (Z.parking || 0);
  host.innerHTML =
    '<div class="atv-bar"><div class="atv-panel" id="calcPanel"><div class="atv-inner">' +
    '<h3>TV Mounting Price in ' + where + '</h3>' +
    '<p class="atv-sub">Build your exact price. Pay online, then pick your 2-hour arrival window.</p>' +
    '<div class="atv-sec"><div class="atv-lab">1 · TV size</div>' + opts('size', SIZES) + '</div>' +
    '<div class="atv-sec"><div class="atv-lab">2 · Mount style</div>' + opts('style', STYLES) + '</div>' +
    '<div class="atv-sec" id="atvWallSec"><div class="atv-lab">3 · Wall type</div>' + opts('wall', WALLS) + '</div>' +
    '<div class="atv-sec" id="atvBracketSec"><div class="atv-lab">4 · Bracket (sold separately)</div>' + opts('bracket', BRACKETS, true) + '</div>' +
    '<div class="atv-sec"><div class="atv-lab">5 · Add-ons</div>' + opts('addon', ADDONS, true) + '</div>' +
    '<div class="atv-sec"><div class="atv-lab">6 · Number of TVs</div><div class="atv-qty"><button type="button" data-q="-1">−</button><span id="atvQty">1</span><button type="button" data-q="1">+</button><small style="color:#5a6578">10% off each additional TV</small></div></div>' +
    '<div class="atv-est"><h4>Your price</h4><div class="atv-total" id="atvTotal"></div><div id="atvLines"></div>' +
    '<p class="atv-note">Paid in full at checkout (tax added at checkout). Anything we find on site that you didn\'t select — like brick behind drywall — is quoted before we do it.</p>' +
    '<a href="#" class="atv-cta" id="atvPay">Book &amp; Pay Now →</a>' +
    '<a href="tel:8004860943" class="atv-cta alt">Call (800) 486-0943</a></div>' +
    '<div class="atv-setup"><h4>Just need your TV &amp; devices set up?</h4>' +
    '<p>No mounting — we connect and program your TV, soundbar, streaming boxes, cable box and remotes. <b>' + money(firstHour) +
    ' for the first hour</b> in ' + where + ', then ' + money(half) + ' per extra 30 minutes (billed after the visit)' +
    (Z.parking ? '. Manhattan parking $' + Z.parking + ' added' : '') + '.</p>' +
    '<a href="#" id="atvSetup">Book a Setup Visit — ' + money(setupPrice) + ' →</a></div>' +
    '<div class="atv-setup"><h4>Projector &amp; screen installation</h4>' +
    '<p>Ceiling-mounted projector aligned and connected, and your screen hung level. Projector mount and screen are yours or quoted separately.</p>' +
    '<div class="atv-grid wide" style="margin-bottom:10px">' +
    '<button type="button" class="atv-opt" data-g="proj" data-id="proj"><b>Projector ceiling mount &amp; hookup</b><small>+' + money(PROJ) + '</small></button>' +
    '<button type="button" class="atv-opt" data-g="proj" data-id="screen"><b>Projection screen install</b><small>+' + money(SCREEN) + '</small></button></div>' +
    '<a href="#" id="atvProj">Book Projector Install →</a></div>' +
    '</div></div>' +
    '<div class="atv-toggle" id="atvToggle"><div><h4>📺 TV Mounting Price Calculator</h4><span>Exact price for ' + where + ' — book online</span></div><div class="atv-arrow" id="stickyArrow">▲</div></div></div>';

  var panel = document.getElementById('calcPanel');

  function compute() {
    var stand = S.style === 'stand';
    var labor = (stand ? Z.stand : Z.base) + find(SIZES, S.size).p;
    var one = labor + (stand ? 0 : find(STYLES, S.style).p + find(WALLS, S.wall).p);
    var extra = S.qty > 1 ? r2(one * 0.9) * (S.qty - 1) : 0;
    var lines = [[(stand ? 'Stand setup' : 'Mounting labor') + ' (' + find(SIZES, S.size).t + ')', labor]];
    if (!stand && find(STYLES, S.style).p) lines.push([find(STYLES, S.style).t, find(STYLES, S.style).p]);
    if (!stand && find(WALLS, S.wall).p) lines.push([find(WALLS, S.wall).t + ' wall', find(WALLS, S.wall).p]);
    if (S.qty > 1) lines.push([(S.qty - 1) + ' more TV' + (S.qty > 2 ? 's' : '') + ' (10% off)', r2(extra)]);
    var br = stand ? BRACKETS[0] : find(BRACKETS, S.bracket);
    var bracketTotal = br.p * S.qty;
    if (br.p) lines.push([br.t + (S.qty > 1 ? ' × ' + S.qty : ''), bracketTotal]);
    var addTotal = 0;
    ADDONS.forEach(function (a) { if (S.addons[a.id]) { addTotal += a.p; lines.push([a.t, a.p]); } });
    var park = Z.parking || 0;
    if (park) lines.push(['Manhattan parking', park]);
    var total = r2(one + extra + bracketTotal + addTotal + park);
    return { total: total, lines: lines, bracket: br };
  }

  function describe(c) {
    var parts = [(S.style === 'stand' ? 'TV stand setup ' : 'TV install ') + find(SIZES, S.size).t.replace(/"/g, 'in')];
    if (S.qty > 1) parts.push('x' + S.qty);
    if (S.style !== 'flat' && S.style !== 'stand') parts.push(find(STYLES, S.style).t);
    if (S.style !== 'stand' && S.wall !== 'dry' && S.wall !== 'unsure') parts.push(find(WALLS, S.wall).t);
    if (c.bracket.p) parts.push('bracket ' + c.bracket.t.split(' (')[0].replace('Sanus ', '').replace('MantelMount ', ''));
    ADDONS.forEach(function (a) { if (S.addons[a.id]) parts.push(a.t.split(' (')[0]); });
    return parts.join(', ') + ' — ' + Z.label.replace(/^the /, '');
  }

  function render() {
    var c = compute();
    document.getElementById('atvTotal').textContent = money(c.total);
    document.getElementById('atvLines').innerHTML = c.lines.map(function (l) {
      return '<div class="atv-line"><span>' + l[0] + '</span><span>' + money(r2(l[1])) + '</span></div>';
    }).join('');
    document.getElementById('atvQty').textContent = S.qty;
    var pAmt = (P.proj ? PROJ : 0) + (P.screen ? SCREEN : 0);
    document.getElementById('atvProj').textContent = pAmt ? 'Book Projector Install — ' + money(r2(pAmt + (Z.parking || 0))) + ' →' : 'Pick a projector service above';
    var standMode = S.style === 'stand';
    ['atvWallSec', 'atvBracketSec'].forEach(function (id) {
      var el = document.getElementById(id); if (el) el.style.display = standMode ? 'none' : '';
    });
    var btns = host.querySelectorAll('.atv-opt');
    for (var i = 0; i < btns.length; i++) {
      var g = btns[i].getAttribute('data-g'), id = btns[i].getAttribute('data-id');
      var on = g === 'addon' ? !!S.addons[id] : g === 'proj' ? !!P[id] : S[g] === id;
      btns[i].classList.toggle('sel', on);
    }
  }

  host.addEventListener('click', function (e) {
    var pb = e.target.closest('[data-g=proj]');
    if (pb) { P[pb.getAttribute('data-id')] = !P[pb.getAttribute('data-id')]; render(); return; }
    var b = e.target.closest('.atv-opt');
    if (b) {
      var g = b.getAttribute('data-g'), id = b.getAttribute('data-id');
      if (g === 'addon') S.addons[id] = !S.addons[id]; else S[g] = id;
      if (g === 'style' && id === 'frame' && S.bracket === 'own') S.bracket = 'framekit';
      render(); return;
    }
    var q = e.target.closest('[data-q]');
    if (q) { S.qty = Math.max(1, Math.min(10, S.qty + parseInt(q.getAttribute('data-q'), 10))); render(); return; }
    if (e.target.closest('#atvToggle')) {
      var open = !panel.classList.contains('open');
      panel.classList.toggle('open', open);
      document.getElementById('stickyArrow').classList.toggle('open', open);
      return;
    }
    if (e.target.closest('#atvPay')) {
      e.preventDefault();
      var c = compute();
      window.location.href = '/pay?desc=' + encodeURIComponent(describe(c)) + '&amount=' + c.total + '&area=' + areaKey;
      return;
    }
    if (e.target.closest('#atvProj')) {
      e.preventDefault();
      var amt = (P.proj ? PROJ : 0) + (P.screen ? SCREEN : 0);
      if (!amt) return;
      amt = r2(amt + (Z.parking || 0));
      var what = [P.proj ? 'projector ceiling mount & hookup' : '', P.screen ? 'screen install' : ''].filter(Boolean).join(' + ');
      window.location.href = '/pay?desc=' + encodeURIComponent('Projector: ' + what + (Z.parking ? ' + parking' : '') + ' — ' + Z.label.replace(/^the /, '')) +
        '&amount=' + amt + '&area=' + areaKey;
      return;
    }
    if (e.target.closest('#atvSetup')) {
      e.preventDefault();
      window.location.href = '/pay?desc=' + encodeURIComponent('TV & devices setup, first hour' + (Z.parking ? ' + parking' : '') + ' — ' + Z.label.replace(/^the /, '')) +
        '&amount=' + setupPrice + '&area=' + areaKey;
    }
  });

  // Old "Get Your Price" buttons open the panel by id; keep the arrow in sync.
  new MutationObserver(function () {
    document.getElementById('stickyArrow').classList.toggle('open', panel.classList.contains('open'));
  }).observe(panel, { attributes: true, attributeFilter: ['class'] });

  window.toggleCalc = function () { document.getElementById('atvToggle').click(); };
  // FAQ accordion used by the TV pages (lived in the old inline calculator script).
  if (!window.toggleFaq) {
    window.toggleFaq = function (el) {
      var a = el.nextElementSibling, ac = el.classList.contains('active');
      var q = document.querySelectorAll('.faq-question'), an = document.querySelectorAll('.faq-answer');
      for (var i = 0; i < q.length; i++) q[i].classList.remove('active');
      for (var j = 0; j < an.length; j++) an[j].classList.remove('show');
      if (!ac) { el.classList.add('active'); if (a) a.classList.add('show'); }
    };
  }
  render();
})();
