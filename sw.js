const CACHE_PREFIX = 'thailand-trip-';
const CACHE_NAME = `${CACHE_PREFIX}v14`;
const PRECACHE_URLS = [
  './',
  './index.html',
  './manifest.json',
  './icon-192.png',
  './icon-512.png'
];

self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) =>
      Promise.allSettled(PRECACHE_URLS.map((url) => cache.add(url)))
    )
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    Promise.all([
      caches.keys().then((names) =>
        Promise.all(
          names
            .filter((name) => name.startsWith(CACHE_PREFIX) && name !== CACHE_NAME)
            .map((name) => caches.delete(name))
        )
      ),
      self.clients.claim()
    ]).then(() => {
      return self.clients.matchAll({ type: 'window' }).then((clients) => {
        clients.forEach((client) => {
          client.postMessage({ type: 'SW_ACTIVATED' });
        });
      });
    })
  );
});

self.addEventListener('message', (event) => {
  if (event.data?.type === 'SKIP_WAITING') self.skipWaiting();
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  const isHTML =
    req.mode === 'navigate' ||
    (req.headers.get('accept') || '').includes('text/html') ||
    url.pathname.endsWith('/') ||
    url.pathname.endsWith('index.html');

  // HTML — sieć najpierw z wymuszeniem braku cache HTTP, fallback do cache
  if (isHTML) {
    const indexUrl = self.registration.scope + 'index.html';
    event.respondWith(
      fetch(req, { cache: 'no-cache' })
        .then((response) => {
          if (response && response.status === 200) {
            const clone1 = response.clone();
            const clone2 = response.clone();
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(req, clone1);
              cache.put(indexUrl, clone2);
            });
            return response;
          }
          return caches.match(req, { ignoreSearch: true }).then((hit) => hit || caches.match(indexUrl));
        })
        .catch(() => {
          return caches.match(req, { ignoreSearch: true }).then((hit) => hit || caches.match(indexUrl));
        })
    );
    return;
  }

  // Pozostałe statyczne zasoby
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).then((response) => {
        if (response && response.status === 200 && url.protocol.startsWith('http')) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(req, clone));
        }
        return response;
      });
    })
  );
});
