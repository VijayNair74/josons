# Builds crawler-facing extras: prerendered product list, JSON-LD, robots/sitemap/llms. Called from build_site.py
import json, html, glob, os, datetime, re
SITE = 'https://josons.pages.dev'
esc = lambda s: html.escape(str(s), quote=True)

def apply(tpl, D):
    P, C = D['products'], D['comm']; n = len(P)
    CAT = {'spices': 'Spices & Roots', 'nuts': 'Nuts & Beans', 'herbal': 'Ayurvedic & Herbal'}
    def aka(p):
        c = C[p['c']]; seen = []
        for x in list(c.get('aka', [])) + [v for k, v in c['names'].items() if k in ('hi', 'ml', 'ta', 'te', 'kn')]:
            for y in str(x).split(' / '):
                y = y.strip()
                if y and y.lower() != p['name'].lower() and y not in seen: seen.append(y)
        return seen
    # 1. counts typed into the static HTML
    tpl = tpl.replace('<b id="statN">35</b>', f'<b id="statN">{n}</b>').replace('<span id="catN">35</span>', f'<span id="catN">{n}</span>')
    # 2. prerendered grid (JS replaces it on load; crawlers and no-JS readers keep it)
    out, last = [], None
    for p in P:
        if p['cat'] != last: out.append(f'<h3 class="catlabel">{CAT[p["cat"]]}</h3>'); last = p['cat']
        c = C[p['c']]; a = aka(p)
        out.append(f'<article class="card"><img src="{esc(p["img"])}" alt="{esc(p["name"])}, {esc(p["sub"])}" loading="lazy">'
                   f'<h4 class="loc" style="font-size:18px">{esc(p["name"])}</h4><span class="sb">{esc(p["sub"])}</span>'
                   + (f'<span class="tl">Also known as: {esc(", ".join(a[:8]))}</span>' if a else '')
                   + (f'<span class="tl">{esc(c["bot"])}</span>' if c.get('bot') and not any(x in c['bot'] for x in '[?') else '') + '</article>')
    tpl = tpl.replace('<div class="grid" id="grid"></div>', '<div class="grid" id="grid">' + ''.join(out) + '</div>', 1)
    # 3. title, description, canonical
    desc = f'Josons Spices, Aluva, Kerala: wholesale whole spices, nuts, beans and Ayurvedic raw materials. {n} products with local names in 12 Indian languages. Enquire on WhatsApp.'
    tpl = tpl.replace('<title>Josons Spices</title>', '<title>Josons Spices, Aluva, Kerala | Wholesale spices, nuts &amp; Ayurvedic raw materials</title>', 1)
    tpl = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(desc)}">\n<link rel="canonical" href="{SITE}/">\n<meta name="robots" content="index,follow,max-image-preview:large">', tpl, 1)
    tpl = tpl.replace('<meta name="twitter:card" content="summary_large_image">', f'<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="Josons Spices, Aluva, Kerala">\n<meta name="twitter:description" content="{esc(desc)}">\n<meta name="twitter:image" content="{SITE}/img/og.jpg">', 1)
    # 4. structured data
    org = {'@type': 'Organization', '@id': SITE + '/#org', 'name': 'Josons Spices', 'url': SITE + '/', 'logo': SITE + '/img/logo.png',
           'description': 'Family-run wholesale supplier of whole spices, nuts, beans and Ayurvedic raw materials from Aluva, Kerala.',
           'email': 'manudparakkal@hotmail.com',
           'address': {'@type': 'PostalAddress', 'streetAddress': 'Parakkal Buildings', 'addressLocality': 'Aluva', 'addressRegion': 'Kerala', 'addressCountry': 'IN'},
           'contactPoint': [{'@type': 'ContactPoint', 'telephone': '+91-484-262-3585', 'contactType': 'sales', 'availableLanguage': ['English', 'Malayalam', 'Hindi']},
                            {'@type': 'ContactPoint', 'telephone': '+91-94470-29905', 'contactType': 'sales (WhatsApp)'}]}
    items = []
    for i, p in enumerate(P, 1):
        c = C[p['c']]; a = aka(p)
        pr = {'@type': 'Product', 'name': p['name'], 'category': CAT[p['cat']], 'image': f'{SITE}/{p["img"]}', 'brand': {'@id': SITE + '/#org'},
              'description': f'{p["name"]} ({p["sub"]}). Wholesale supply from Aluva, Kerala. Price on request.'.replace('?','')}
        if a: pr['alternateName'] = a[:8]
        items.append({'@type': 'ListItem', 'position': i, 'item': pr})
    ld = {'@context': 'https://schema.org', '@graph': [org,
          {'@type': 'WebSite', 'name': 'Josons Spices', 'url': SITE + '/', 'publisher': {'@id': SITE + '/#org'}},
          {'@type': 'ItemList', 'name': 'Josons Spices catalogue', 'numberOfItems': n, 'itemListElement': items}]}
    tpl = tpl.replace('<link rel="stylesheet" href="https://fonts.googleapis.com', '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False).replace('</', '<\\/') + '</script>\n<link rel="stylesheet" href="https://fonts.googleapis.com', 1)
    # 5. files
    os.makedirs('/root/site/seo', exist_ok=True); today = datetime.date.today().isoformat()
    pdfs = sorted(glob.glob('/home/claude/josons_site/pdf/*.pdf'))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', f'<url><loc>{SITE}/</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>']
    sm += [f'<url><loc>{SITE}/pdf/{os.path.basename(f)}</loc><lastmod>{today}</lastmod><priority>0.5</priority></url>' for f in pdfs] + ['</urlset>']
    open('/root/site/seo/sitemap.xml', 'w').write('\n'.join(sm) + '\n')
    open('/root/site/seo/robots.txt', 'w').write(f'User-agent: *\nAllow: /\nDisallow: /admin.html\nDisallow: /api/\n\nSitemap: {SITE}/sitemap.xml\n')
    L = ['# Josons Spices', '', '> Family-run wholesale supplier of whole spices, nuts, beans and Ayurvedic raw materials, based in Aluva, Kerala, India. Prices on request. Enquiries by WhatsApp +91 94470 29905, phone +91 484 262 3585 or manudparakkal@hotmail.com.', '',
         f'The catalogue has {n} products. Product names are shown in 12 Indian languages. Brochures are available as PDF in English and 12 Indian languages.', '', '## Pages', f'- [Catalogue and enquiry]({SITE}/#catalogue): all products, search in any language, enquiry cart that sends one WhatsApp message', '', '## Brochures (PDF, 8 pages)']
    L += [f'- [{os.path.basename(f)[14:-4]}]({SITE}/pdf/{os.path.basename(f)})' for f in pdfs]
    for k, name in CAT.items():
        L += ['', f'## {name}'] + [f'- {p["name"]}: {p["sub"]}' for p in P if p['cat'] == k]
    open('/root/site/seo/llms.txt', 'w').write('\n'.join(L) + '\n')
    return tpl
