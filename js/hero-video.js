/* AESS hero video (Nov 5 2026): turns a hero photo into an autoplaying kinetic video.
   Markup: <div class="rh-photo" data-hero-video="/videos/hero/<slug>.mp4"><img ...></div>
   The photo stays in the HTML as the poster, so the page paints instantly and keeps its alt text.
   Browsers only autoplay muted video, so it starts muted with a "Tap for sound" button. */
(function () {
  function prefersStill() {
    try {
      if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return true;
      var c = navigator.connection;
      if (c && (c.saveData || /(^|-)2g$/.test(c.effectiveType || ''))) return true;
    } catch (e) {}
    return false;
  }
  function boot(box) {
    var src = box.getAttribute('data-hero-video');
    var img = box.querySelector('img');
    if (!src || !img || prefersStill()) return;
    var v = document.createElement('video');
    v.muted = true; v.defaultMuted = true; v.autoplay = true; v.loop = false;
    v.playsInline = true; v.setAttribute('playsinline', ''); v.setAttribute('muted', '');
    v.preload = 'auto';
    v.poster = img.currentSrc || img.src;
    v.width = img.width || 1200; v.height = img.height || 675;
    v.setAttribute('aria-label', img.alt || 'AESS video');
    v.style.cssText = 'display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;background:#091638';
    v.src = src;
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'hv-sound';
    btn.textContent = '🔊 Tap for sound';
    btn.style.cssText = 'position:absolute;left:12px;bottom:12px;z-index:2;border:0;border-radius:999px;padding:8px 14px;font:700 14px/1 Inter,system-ui,sans-serif;background:#1B4AD6;color:#fff;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.35)';
    btn.addEventListener('click', function () {
      if (v.ended) v.currentTime = 0;
      v.muted = !v.muted;
      btn.textContent = v.muted ? '🔊 Tap for sound' : '🔇 Mute';
      v.play();
    });
    v.addEventListener('ended', function () { btn.textContent = '↻ Replay with sound'; v.muted = true; });
    v.addEventListener('error', function () { if (v.parentNode) { v.parentNode.replaceChild(img, v); btn.remove(); } });
    box.style.position = 'relative';
    v.addEventListener('loadeddata', function () {
      if (img.parentNode === box) box.replaceChild(v, img);
      box.appendChild(btn);
      var p = v.play(); if (p && p.catch) p.catch(function () {});
    }, { once: true });
    v.load();
  }
  function run() {
    var els = document.querySelectorAll('[data-hero-video]');
    for (var i = 0; i < els.length; i++) boot(els[i]);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run); else run();
})();
