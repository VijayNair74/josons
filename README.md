# Josons Spices website

Static catalogue site for Josons Spices (Aluva, Kerala) with a WhatsApp enquiry cart, an admin page for enquiries, and per-language PDF brochures.

Hosted on Cloudflare Pages (advanced mode `_worker.js`) with a D1 database binding named `DB` and a secret `ADMIN_PASSWORD`. See [SETUP.md](SETUP.md) for the one-time setup.

## What is here
- `index.html`: the public site (data is embedded in the file)
- `admin.html`: enquiry inbox for Manu (password-protected via the Worker)
- `_worker.js`: API routes `/api/enquiry`, `/api/whereami`, `/api/admin/enquiries`
- `schema.sql`: D1 table (location columns are added automatically)
- `img/`, `pdf/`: photos and the 13 language brochures
- `tools/`: generators. `site_template.html` is the page source, `native.py` holds the native-script names, `build_site.py` and `build_lang.py` rebuild the site and PDFs. Paths inside them point at the original build machine and need adjusting before reuse.

## Deploy
Upload the repository contents (without `tools/` and `.git`) through Cloudflare Pages, or connect the repo to Pages. Data, the admin password and enquiries persist across deployments.

## Notes
- Local names in 12 languages were written without a native-speaker review. Treat spellings as drafts.
- Visitor location is approximate and comes from Cloudflare. The IP address is never stored.
