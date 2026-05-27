// ── Accordion ──
    document.querySelectorAll('.gv-acc-trigger').forEach(t => {
      t.addEventListener('click', () => {
        const open = t.getAttribute('aria-expanded') === 'true';
        t.closest('.gv-accordion')?.querySelectorAll('.gv-acc-trigger').forEach(x => {
          x.classList.remove('gv-expanded'); x.setAttribute('aria-expanded','false');
          const b = document.getElementById(x.getAttribute('aria-controls'));
          if (b) b.classList.add('gv-hidden');
        });
        if (!open) {
          t.classList.add('gv-expanded'); t.setAttribute('aria-expanded','true');
          const b = document.getElementById(t.getAttribute('aria-controls'));
          if (b) b.classList.remove('gv-hidden');
        }
      });
    });

    // ── Tabs ──
    document.querySelectorAll('[role="tablist"]').forEach(tl => {
      tl.querySelectorAll('[role="tab"]').forEach(tab => {
        tab.addEventListener('click', () => {
          tl.querySelectorAll('[role="tab"]').forEach(x => { x.classList.remove('gv-tab-active'); x.setAttribute('aria-selected','false'); });
          tab.classList.add('gv-tab-active'); tab.setAttribute('aria-selected','true');
          const panel = document.getElementById(tab.getAttribute('aria-controls'));
          tl.closest('.comp-preview, section')?.querySelectorAll('.gv-tab-panel').forEach(p => p.classList.remove('gv-panel-active'));
          if (panel) panel.classList.add('gv-panel-active');
        });
      });
    });

    // ── Filter chips ──
    document.querySelectorAll('.gv-chip:not(.gv-chip-radio)').forEach(c => c.addEventListener('click', () => c.classList.toggle('gv-chip-active')));
    document.querySelectorAll('.gv-chip-radio').forEach(c => {
      c.addEventListener('click', () => {
        c.closest('div')?.querySelectorAll('.gv-chip-radio').forEach(x => x.classList.remove('gv-chip-active'));
        c.classList.add('gv-chip-active');
      });
    });

    // ── Char counter ──
    document.querySelectorAll('.gv-char-counter-input input, .gv-char-counter-input textarea').forEach(input => {
      const counter = input.closest('.gv-form-option')?.querySelector('.gv-char-total');
      if (counter) { input.addEventListener('input', () => counter.textContent = input.value.length); }
    });

    // ── Sidebar scroll highlight ──
    const navLinks = document.querySelectorAll('.gv-side-nav a.gv-nav-item');
    const observer = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          navLinks.forEach(l => l.classList.remove('gv-active'));
          const a = document.querySelector(`.gv-side-nav a[href="#${e.target.id}"]`);
          if (a) a.classList.add('gv-active');
        }
      });
    }, { rootMargin: '-72px 0px -55% 0px' });
    document.querySelectorAll('section[id]').forEach(s => observer.observe(s));
