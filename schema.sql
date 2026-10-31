-- Run once in Cloudflare D1 (database name: josons)
CREATE TABLE IF NOT EXISTS enquiries (
  id          TEXT PRIMARY KEY,
  created_at  TEXT NOT NULL,
  name        TEXT, business TEXT, btype TEXT, state TEXT, phone TEXT,
  items       TEXT NOT NULL,          -- JSON: [{product, qty, unit}]
  sample      INTEGER DEFAULT 0,
  notes       TEXT, lang TEXT,
  loc_city    TEXT, loc_region TEXT, loc_country TEXT,  -- approximate, from the visitor's IP via Cloudflare (added automatically on first enquiry)
  status      TEXT DEFAULT 'New',      -- New | Quoted | Sample sent | Ordered | Lost
  follow_up   TEXT,                    -- YYYY-MM-DD
  admin_note  TEXT
);
CREATE INDEX IF NOT EXISTS idx_created ON enquiries(created_at);
