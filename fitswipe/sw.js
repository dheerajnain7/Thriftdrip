const CACHE = 'fitswipe-v1';
const ASSETS = [
  './', './index.html', './styles.css', './app.js',
  './manifest.json', './cards.json', './icon.png',
  './images/streetwear.jpg', './images/earphones.jpg',
  './images/fit1.jpg', './images/moodboard.jpg',
  './images/fit3.jpg', './images/fit4.jpg', './images/fit5.jpg',
  './images/pro1.jpg', './images/pro2.jpg', './images/pro3.jpg',
  './images/pro4.jpg', './images/pro5.jpg'
];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => { e.waitUntil(self.clients.claim()); });
self.addEventListener('fetch', e => {
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});
