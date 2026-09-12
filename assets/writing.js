// The complete archive remains readable without JavaScript.
(() => {
  const form = document.querySelector('#writing-filters');
  if (!form) return;
  const search = form.elements.namedItem('q');
  const topic = form.elements.namedItem('topic');
  const year = form.elements.namedItem('year');
  const entries = [...document.querySelectorAll('.archive-entry')];
  const groups = [...document.querySelectorAll('.year-group')];
  const status = document.querySelector('#writing-status');
  const empty = document.querySelector('#writing-empty');
  const normalize = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const text = new Map(entries.map(entry => [entry, normalize(entry.textContent)]));
  function update() {
    const terms = normalize(search.value.trim()).split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const entry of entries) {
      const matches = (!topic.value || entry.dataset.topic === topic.value)
        && (!year.value || entry.dataset.year === year.value)
        && terms.every(term => text.get(entry).includes(term));
      entry.hidden = !matches;
      if (matches) visible += 1;
    }
    for (const group of groups) {
      const count = group.querySelectorAll('.archive-entry:not([hidden])').length;
      group.hidden = count === 0;
      group.querySelector('.year-count').textContent = `${count} ${count === 1 ? 'article' : 'articles'}`;
    }
    status.textContent = `Showing ${visible} of ${entries.length} articles`;
    empty.hidden = visible !== 0;
  }
  form.hidden = false;
  form.addEventListener('submit', event => event.preventDefault());
  form.addEventListener('input', update);
  form.addEventListener('change', update);
  form.addEventListener('reset', () => {
    search.value = ''; topic.value = ''; year.value = '';
    update(); search.focus();
  });
  update();
})();
