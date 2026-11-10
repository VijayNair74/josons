"""Phone-format brochure PDFs (90 x 176 mm pages, 2-column cards, big text, tap-to-WhatsApp on every product)."""
import json, pathlib, urllib.parse, html as H
from PIL import Image
src = open('/root/flyer/build_lang.py', encoding='utf-8').read().split('from playwright.sync_api import sync_playwright')[0]
ns = {}; exec(src, ns)           # reuse lists_for, audience, FONT_CSS, LANG, S, OUT, D
lists_for, audience, FONT_CSS, LANG, S, OUT, D = (ns[k] for k in ('lists_for', 'audience', 'FONT_CSS', 'LANG', 'S', 'OUT', 'D'))
P = D / 'img_p'; P.mkdir(exist_ok=True)
for f in (D / 'img').iterdir():
    if f.suffix == '.jpg':
        im = Image.open(f).convert('RGB'); im.thumbnail((300, 300)); im.save(P / f.name, quality=55, optimize=True)
    elif f.suffix == '.png':
        im = Image.open(f).convert('RGBA'); im.thumbnail((240, 240)); im.quantize(colors=96, method=Image.Quantize.FASTOCTREE).save(P / f.name, optimize=True)

WA = '919447029905'
wa = lambda t: f'https://wa.me/{WA}?text=' + urllib.parse.quote(t)
CATS = [('spices', 'Spices &amp; Roots', 'linear-gradient(120deg,#0F3D2E,#185A43)'), ('nuts', 'Nuts &amp; Beans', 'linear-gradient(120deg,#8B4A2B,#4f2614)'), ('herbal', 'Ayurvedic &amp; Herbal', 'linear-gradient(120deg,#8B4A2B,#4f2614)')]
PER = 6
CSS = '''
@page { size: 90mm 176mm; margin: 0 }
:root { --leaf:#0F3D2E; --leaf2:#185A43; --turmeric:#E8A317; --chili:#B3261E; --cream:#FBF4E4; --gold:#C9A227; --ink:#2A1A10; --muted:#6E5B4B }
* { box-sizing:border-box; margin:0; padding:0 }
body { font-family:Poppins,sans-serif; color:var(--ink); -webkit-print-color-adjust:exact }
a { color:inherit; text-decoration:none }
.page { width:90mm; height:176mm; position:relative; overflow:hidden; page-break-after:always; background:var(--cream) }
.band { height:17mm; padding:4mm 5mm 0; color:#fff; position:relative }
.band .eb { color:var(--turmeric); font-size:6pt; letter-spacing:2.5px; font-weight:600 }
.band .t { font-family:Lora,serif; font-size:15pt; margin-top:.5mm }
.band .pg { position:absolute; right:5mm; top:4.5mm; font-family:Lora,serif; font-size:16pt; opacity:.4 }
.grid { position:absolute; top:20mm; left:4mm; right:4mm; bottom:12mm; display:grid; grid-template-columns:1fr 1fr; grid-template-rows:repeat(3,1fr); gap:3mm }
.card { background:#fff; border:.3mm solid #e9dcc0; border-radius:3mm; padding:1.6mm; display:flex; flex-direction:column; overflow:hidden }
.ph { height:28.5mm; border-radius:2mm; background-size:cover; background-position:center; flex:none }
.nm { font-weight:600; font-size:9.6pt; line-height:1.28; color:var(--leaf); margin-top:1.6mm; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; font-family:IndicAll,Poppins,sans-serif }
.sb { font-size:6.3pt; line-height:1.3; color:var(--muted); margin-top:.6mm; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; font-family:IndicAll,Poppins,sans-serif }
.foot { position:absolute; left:0; right:0; bottom:0; height:9mm; background:var(--leaf); color:#f3e9cf; font-size:6.2pt; letter-spacing:.4px; display:flex; justify-content:space-between; align-items:center; padding:0 5mm; border-top:1mm solid var(--gold) }
.cover { background:linear-gradient(170deg,#0F3D2E,#0b2a20) }
.cover .logo { width:24mm; height:24mm; border-radius:50%; margin:11mm auto 0; display:block; background:#0F3D2E; border:.6mm solid var(--gold) }
.cover .brand { text-align:center; color:#fff; font-family:Lora,serif; font-weight:700; letter-spacing:2.5px; font-size:17pt; margin-top:4mm }
.cover .loc { text-align:center; color:var(--turmeric); font-size:6.5pt; letter-spacing:3px; margin-top:1mm }
.cover h1 { font-family:Lora,serif; font-weight:500; color:#fff; font-size:17pt; line-height:1.15; text-align:center; margin:7mm 6mm 0 }
.cover h1 em { color:var(--turmeric) }
.cover p { color:#e7dcc3; font-size:8pt; line-height:1.55; text-align:center; margin:3.5mm 7mm 0; font-weight:300 }
.cover .badge { margin:4mm 8mm 0; padding-top:2.5mm; border-top:.4mm solid var(--gold); color:var(--turmeric); font-weight:600; font-size:7.5pt; text-align:center; font-family:IndicAll,Poppins,sans-serif }
.dots { display:grid; grid-template-columns:repeat(4,1fr); gap:2.2mm; margin:5mm 7mm 0 }
.dots i { aspect-ratio:1; border-radius:50%; background-size:cover; background-position:center; border:.5mm solid var(--gold) }
.btn { display:block; margin:5mm 12mm 0; padding:3mm 0; border-radius:20mm; background:var(--gold); color:#0F3D2E; font-weight:700; font-size:8.5pt; text-align:center }
.how { position:absolute; top:22mm; left:6mm; right:6mm }
.how h2 { font-family:Lora,serif; color:var(--leaf); font-size:16pt }
.step { display:flex; gap:3mm; margin-top:4.5mm; align-items:flex-start }
.step b { flex:none; width:7mm; height:7mm; border-radius:50%; background:var(--leaf2); color:#fff; display:flex; align-items:center; justify-content:center; font-size:9pt }
.step div { font-size:8pt; line-height:1.45; color:var(--ink) } .step strong { display:block; color:var(--leaf); font-size:9pt }
.contact { margin-top:7mm; background:#fff; border:.3mm solid #e9dcc0; border-radius:3mm; padding:3.5mm 4mm; font-size:7.6pt; line-height:1.9 }
.contact span { color:var(--chili); font-size:6pt; letter-spacing:1.5px; display:inline-block; width:19mm; font-weight:600 }
'''
def build(lang):
    L = lists_for(lang)
    en = {c: [p['name'] for p in S['products'] if p['cat'] == c] for c, _, _ in CATS}
    pages, pn = [], 1
    # catalogue pages
    for cat, title, grad in CATS:
        items = L[cat]
        for i in range(0, len(items), PER):
            pn += 1; cards = []
            for k, (img, name, sub) in enumerate(items[i:i + PER]):
                enn = en[cat][i + k]
                cards.append(f'<a class="card" href="{wa("Hello Josons, I would like a quote for: " + enn)}"><div class="ph" style="background-image:url(img_p/{img}.jpg)"></div><div class="nm">{name}</div><div class="sb">{sub}</div></a>')
            pages.append(('cat', grad, title + (' (continued)' if i else ''), ''.join(cards), pn))
    N = pn + 1
    first6 = [L['spices'][j][0] for j in (1, 2, 3, 5, 8, 12, 16, 20) if j < len(L['spices'])][:8]
    dots = ''.join(f'<i style="background-image:url(img_p/{x}.jpg)"></i>' for x in first6)
    badge = f'Product names in {LANG[lang]}<br>{audience(lang)}' if lang != 'en' else 'All India edition'
    out = [f'''<section class="page cover"><img class="logo" src="img_p/logo.png"><div class="brand">JOSONS SPICES</div><div class="loc">ALUVA · KERALA</div>
<h1>Straight from Kerala's <em>Spice Coast</em></h1><p>Whole spices, nuts, beans and Ayurvedic raw materials, sourced, graded and supplied from Aluva by a family with generations in the spice trade.</p>
<div class="badge">{badge}</div><div class="dots">{dots}</div><a class="btn" href="{wa("Hello Josons, I would like a quote.")}">Enquire on WhatsApp</a>
<div class="foot"><span>Parakkal Buildings, Aluva, Kerala</span><span>1 / {N}</span></div></section>''']
    for _, grad, title, cards, n in pages:
        out.append(f'<section class="page"><div class="band" style="background:{grad}"><div class="eb">CATALOGUE</div><div class="t">{title}</div></div><div class="grid">{cards}</div><div class="foot"><span>Tap a product to enquire on WhatsApp</span><span>{n} / {N}</span></div></section>')
    out.append(f'''<section class="page"><div class="band" style="background:linear-gradient(120deg,#0F3D2E,#185A43)"><div class="eb">ORDER</div><div class="t">How to enquire</div></div>
<div class="how"><div class="step"><b>1</b><div><strong>Pick your products</strong>Tap any product in this brochure. It opens WhatsApp with the name filled in.</div></div>
<div class="step"><b>2</b><div><strong>Tell us the quantity</strong>Send the message with the amount you need. Samples are available.</div></div>
<div class="step"><b>3</b><div><strong>Get today's price</strong>We reply with the current price and dispatch from Aluva by road, rail or courier.</div></div>
<div class="contact"><span>WHATSAPP</span>+91 94470 29905<br><span>PHONE</span>+91 484 262 3585<br><span>EMAIL</span>manudparakkal@hotmail.com<br><span>VISIT</span>Parakkal Buildings, Aluva, Kerala</div>
<a class="btn" style="margin:6mm 4mm 0" href="{wa("Hello Josons, I would like a quote.")}">Enquire on WhatsApp</a></div>
<div class="foot"><span>Prices on request · Not in the list? Ask, we source on request</span><span>{N} / {N}</span></div></section>''')
    css = CSS + (FONT_CSS if lang != 'en' else '')
    return f'<!doctype html><html><head><meta charset="utf-8"><title>Josons Spices</title><style>{css}</style></head><body>{"".join(out)}</body></html>', N

from playwright.sync_api import sync_playwright
import sys
only = sys.argv[1:] 
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page()
    for lang in ['en'] + [k for k, _ in S['langs']]:
        if only and lang not in only: continue
        h, N = build(lang); f = D / f'phone_{lang}.html'; f.write_text(h, encoding='utf-8')
        pg.goto(f.as_uri()); pg.wait_for_load_state('networkidle')
        out = OUT / f'Josons_Spices_{LANG[lang]}_Phone.pdf'
        pg.pdf(path=str(out), width='90mm', height='176mm', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        print(f'{LANG[lang]:10s} {N} pages {out.stat().st_size/1e6:.2f} MB')
    b.close()
