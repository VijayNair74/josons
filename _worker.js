// Cloudflare Pages advanced-mode worker: API routes + static assets
const json = (d, s = 200) => new Response(JSON.stringify(d), { status: s, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' } });
const cut = (v, n) => (typeof v === 'string' ? v.trim().slice(0, n) : '');
const STATUSES = ['New', 'Quoted', 'Sample sent', 'Ordered', 'Lost'];
function authed(request, env) {
  const got = (request.headers.get('authorization') || '').replace(/^Bearer\s+/i, '');
  const want = env.ADMIN_PASSWORD || '';
  if (!want || got.length !== want.length) return false;
  let diff = 0; for (let i = 0; i < want.length; i++) diff |= got.charCodeAt(i) ^ want.charCodeAt(i);
  return diff === 0;
}
// Approximate visitor location comes from Cloudflare (request.cf, from the IP address). No popup, no GPS. The IP itself is never stored.
let colsReady = false;
async function ensureCols(env) {
  if (colsReady) return;
  const { results } = await env.DB.prepare('PRAGMA table_info(enquiries)').all();
  const have = new Set(results.map((r) => r.name));
  for (const c of ['loc_city', 'loc_region', 'loc_country']) if (!have.has(c)) await env.DB.prepare(`ALTER TABLE enquiries ADD COLUMN ${c} TEXT`).run();
  colsReady = true;
}
async function enquiry(request, env) {
  if (request.method !== 'POST') return json({ error: 'method' }, 405);
  let b; try { b = await request.json(); } catch { return json({ error: 'bad json' }, 400); }
  if (b.hp) return json({ ok: true });
  const items = Array.isArray(b.items) ? b.items.slice(0, 40).map((i) => ({ product: cut(i.product, 80), qty: cut(String(i.qty ?? ''), 10), unit: cut(i.unit, 10) })).filter((i) => i.product) : [];
  if (!items.length) return json({ error: 'no items' }, 400);
  const id = /^JS-\d{6}-\d{4}$/.test(b.id || '') ? b.id : 'JS-' + Date.now();
  const row = [id, new Date().toISOString(), cut(b.name, 80), cut(b.business, 100), cut(b.btype, 60), cut(b.state, 60), cut(b.phone, 20), JSON.stringify(items), b.sample ? 1 : 0, cut(b.notes, 500), cut(b.lang, 5)];
  const cf = request.cf || {};
  const loc = [cut(cf.city, 60), cut(cf.region, 60), cut(cf.country, 2)];
  let saved = false;
  try {
    await ensureCols(env);
    await env.DB.prepare(`INSERT OR IGNORE INTO enquiries (id, created_at, name, business, btype, state, phone, items, sample, notes, lang, loc_city, loc_region, loc_country)
      VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11, ?12, ?13, ?14)`).bind(...row, ...loc).run();
    saved = true;
  } catch (e) { /* location columns unavailable: never lose the enquiry */ }
  if (!saved) await env.DB.prepare(`INSERT OR IGNORE INTO enquiries (id, created_at, name, business, btype, state, phone, items, sample, notes, lang)
      VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11)`).bind(...row).run();
  return json({ ok: true, id });
}
// Tells the page roughly where the visitor is (country and state) so the form can pre-select it. Nothing is stored here.
function whereami(request) {
  const cf = request.cf || {};
  return json({ country: cut(cf.country, 2), region: cut(cf.region, 60) });
}
async function admin(request, env) {
  if (!authed(request, env)) return json({ error: 'Wrong password' }, 401);
  const m = request.method;
  if (m === 'GET') {
    const { results } = await env.DB.prepare('SELECT * FROM enquiries ORDER BY created_at DESC LIMIT 1000').all();
    return json({ enquiries: results.map((r) => ({ ...r, items: JSON.parse(r.items || '[]') })) });
  }
  const b = await request.json().catch(() => ({}));
  if (m === 'PATCH') {
    if (!b.id) return json({ error: 'id needed' }, 400);
    const status = STATUSES.includes(b.status) ? b.status : null;
    const fu = /^\d{4}-\d{2}-\d{2}$/.test(b.follow_up || '') ? b.follow_up : (b.follow_up === '' ? '' : null);
    await env.DB.prepare(`UPDATE enquiries SET status = COALESCE(?2, status), follow_up = COALESCE(?3, follow_up), admin_note = COALESCE(?4, admin_note) WHERE id = ?1`)
      .bind(b.id, status, fu, typeof b.admin_note === 'string' ? b.admin_note.slice(0, 500) : null).run();
    return json({ ok: true });
  }
  if (m === 'DELETE') {
    if (Array.isArray(b.ids) && b.ids.length) {
      const ids = b.ids.slice(0, 500); const q = ids.map((_, i) => `?${i + 1}`).join(',');
      const r = await env.DB.prepare(`DELETE FROM enquiries WHERE id IN (${q})`).bind(...ids).run(); return json({ deleted: r.meta.changes });
    }
    if (b.all === true) { const r = await env.DB.prepare('DELETE FROM enquiries').run(); return json({ deleted: r.meta.changes }); }
    const days = Math.max(1, Number(b.olderThanDays) || 30); const cutoff = new Date(Date.now() - days * 864e5).toISOString();
    const r = await env.DB.prepare(`DELETE FROM enquiries WHERE created_at < ?1 ${b.closedOnly ? "AND status IN ('Ordered','Lost')" : ''}`).bind(cutoff).run();
    return json({ deleted: r.meta.changes });
  }
  return json({ error: 'method' }, 405);
}
export default {
  async fetch(request, env) {
    const p = new URL(request.url).pathname;
    try {
      if (p === '/api/enquiry') return await enquiry(request, env);
      if (p === '/api/whereami') return whereami(request);
      if (p === '/api/admin/enquiries') return await admin(request, env);
    } catch (e) { return json({ error: 'server' }, 500); }
    return env.ASSETS.fetch(request);
  },
};
