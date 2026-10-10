let cards = [], i = 0;
const img = document.getElementById('card-img');
const title = document.getElementById('card-title');
const card = document.getElementById('card');
const idxEl = document.getElementById('idx');
const totalEl = document.getElementById('total');

fetch('cards.json').then(r => r.json()).then(data => {
  cards = data;
  totalEl.textContent = cards.length;
  show(0);
});

function show(n) {
  i = (n + cards.length) % cards.length;
  img.src = cards[i].img;
  title.textContent = cards[i].title;
  idxEl.textContent = i + 1;
  card.style.transform = 'scale(.96)';
  setTimeout(() => card.style.transform = 'scale(1)', 60);
}
// preload neighbours
setInterval(() => {
  if (!cards.length) return;
  [1, -1].forEach(d => { const im = new Image(); im.src = cards[(i + d + cards.length) % cards.length].img; });
}, 4000);

document.getElementById('next').onclick = () => show(i + 1);
document.getElementById('prev').onclick = () => show(i - 1);
document.getElementById('shuffle').onclick = () => {
  for (let k = cards.length - 1; k > 0; k--) {
    const j = Math.floor(Math.random() * (k + 1));
    [cards[k], cards[j]] = [cards[j], cards[k]];
  }
  show(0);
};

// touch swipe
let sx = 0, dx = 0, dragging = false;
const deck = document.getElementById('deck');
deck.addEventListener('touchstart', e => { sx = e.touches[0].clientX; dragging = true; }, {passive: true});
deck.addEventListener('touchmove', e => {
  if (!dragging) return;
  dx = e.touches[0].clientX - sx;
  card.style.transition = 'none';
  card.style.transform = `translateX(${dx}px) rotate(${dx / 28}deg)`;
}, {passive: true});
deck.addEventListener('touchend', () => {
  dragging = false;
  card.style.transition = 'transform .18s ease-out';
  if (dx > 90) show(i - 1);
  else if (dx < -90) show(i + 1);
  else card.style.transform = 'scale(1)';
  dx = 0;
});
// mouse drag for desktop
deck.addEventListener('mousedown', e => { sx = e.clientX; dragging = true; });
window.addEventListener('mousemove', e => {
  if (!dragging) return;
  dx = e.clientX - sx;
  card.style.transition = 'none';
  card.style.transform = `translateX(${dx}px) rotate(${dx / 28}deg)`;
});
window.addEventListener('mouseup', () => {
  if (!dragging) return;
  dragging = false;
  card.style.transition = 'transform .18s ease-out';
  if (dx > 90) show(i - 1);
  else if (dx < -90) show(i + 1);
  else card.style.transform = 'scale(1)';
  dx = 0;
});
document.addEventListener('keydown', e => {
  if (e.key === 'ArrowRight') show(i + 1);
  if (e.key === 'ArrowLeft') show(i - 1);
});
