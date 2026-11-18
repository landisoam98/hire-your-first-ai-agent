/* Shared runtime for every slide: glass backdrop, chrome, count-ups, typewriter, timers. */
(function () {
  const b = document.body;
  const STATIC = navigator.webdriver || location.hash === '#static';
  if (STATIC) document.documentElement.classList.add('static');
  const dark = b.classList.contains('dark');
  const STAR = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c.6 6.4 5.6 11.4 12 12-6.4.6-11.4 5.6-12 12-.6-6.4-5.6-11.4-12-12C6.4 11.4 11.4 6.4 12 0z"/></svg>';

  // backdrop: glow + glass tiles + a few sparkles sitting on tile corners
  const bg = document.createElement('div');
  bg.className = 'bg';
  bg.innerHTML = '<div class="glow"></div><div class="glow b"></div><div class="tiles"></div>';
  const sparks = b.dataset.sparks === 'none' ? [] : (b.dataset.sparks || '7,1 9,3 8,5').split(' ').filter(Boolean);
  sparks.forEach((s, i) => {
    const [c, r] = s.split(',').map(Number);
    const el = document.createElement('div');
    el.className = 'spark'; el.innerHTML = STAR;
    el.style.left = (c * 192) + 'px'; el.style.top = (r * 180) + 'px';
    el.style.animationDelay = (i * 1.3) + 's';
    bg.appendChild(el);
  });
  b.prepend(bg);

  // chrome: logo + section name (no page numbers: the shell owns those)
  if (!b.classList.contains('bare')) {
    const c = document.createElement('div');
    c.className = 'chrome';
    c.innerHTML = '<img src="../assets/' + (dark ? 'logo-white' : 'logo-dark') + '.png" alt="SuDu AI"><span>' + (b.dataset.section || '') + '</span>';
    b.appendChild(c);
  }

  // count-up: <span data-count="20800" data-dur="1.6" data-delay="1.2">
  const fmt = n => n.toLocaleString('en-US');
  document.querySelectorAll('[data-count]').forEach(el => {
    const to = parseFloat(el.dataset.count), dur = (parseFloat(el.dataset.dur) || 1.4) * 1000;
    const delay = (parseFloat(el.dataset.delay) || 0) * 1000, dec = parseInt(el.dataset.dec || '0', 10);
    const from = parseFloat(el.dataset.from || '0');
    if (STATIC) { el.textContent = dec ? to.toFixed(dec) : fmt(to); return; }
    el.textContent = dec ? from.toFixed(dec) : fmt(from);
    setTimeout(() => {
      const t0 = performance.now();
      (function tick(t) {
        const p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 4);
        const v = from + (to - from) * e;
        el.textContent = dec ? v.toFixed(dec) : fmt(Math.round(v));
        if (p < 1) requestAnimationFrame(tick);
      })(t0);
    }, delay);
  });

  // typewriter: <span data-type="breakfast" data-delay="2">
  document.querySelectorAll('[data-type]').forEach(el => {
    const text = el.dataset.type, delay = (parseFloat(el.dataset.delay) || 0) * 1000, cps = parseFloat(el.dataset.cps || '22');
    if (STATIC) { el.textContent = text; return; }
    el.textContent = '';
    setTimeout(() => {
      let i = 0;
      const iv = setInterval(() => { el.textContent = text.slice(0, ++i); if (i >= text.length) clearInterval(iv); }, 1000 / cps);
    }, delay);
  });

  // countdown: <span data-timer="900">
  document.querySelectorAll('[data-timer]').forEach(el => {
    let s = parseInt(el.dataset.timer, 10);
    const show = () => { el.textContent = String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'); };
    show();
    setInterval(() => { if (s > 0) { s--; show(); } }, 1000);
  });

  // opened on its own (not inside the deck shell): fit 1920x1080 to the window
  function fit() {
    if (window.parent !== window) return;
    const s = Math.min(innerWidth / 1920, innerHeight / 1080);
    b.style.transform = 'translate(' + (innerWidth - 1920 * s) / 2 + 'px,' + (innerHeight - 1080 * s) / 2 + 'px) scale(' + s + ')';
  }
  fit(); addEventListener('resize', fit);

  // keys pressed while the slide has focus still drive the deck
  addEventListener('keydown', e => {
    if (window.parent !== window) window.parent.postMessage({ deckKey: e.key }, '*');
  });
})();
