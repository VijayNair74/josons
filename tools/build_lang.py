"""Build one classic-style brochure PDF per language, with local product names, small enough for WhatsApp."""
import json, pathlib, re
from PIL import Image

D = pathlib.Path('/root/flyer')
OUT = pathlib.Path('/root/site/build/pdf'); OUT.mkdir(parents=True, exist_ok=True)
S = json.load(open('/root/site/site_data.json', encoding='utf-8'))
LANG = dict(S['langs']); LANG['en'] = 'English'
SLUG = {k: v.lower() for k, v in LANG.items()}

# lighter images for WhatsApp-sized PDFs
small = D / 'img_s'; small.mkdir(exist_ok=True)
for f in (D / 'img').iterdir():
    if f.suffix == '.jpg':
        im = Image.open(f).convert('RGB'); im.thumbnail((210, 210)); im.save(small / f.name, quality=50)
    elif f.suffix == '.png':
        im = Image.open(f).convert('RGBA'); im.thumbnail((240, 240)); im.quantize(colors=96, method=Image.Quantize.FASTOCTREE).save(small / f.name, optimize=True)

src = open(D / 'build.py', encoding='utf-8').read()
head, rest = src[:src.index('SPICES = [')], src[src.index('def card('):]

def first(v): return (v or '').split(' / ')[0]

import sys; sys.path.insert(0, '/root/site')
from native import NATIVE, PQ, QUAL
FB = '/root/fonts/node_modules/@fontsource'
SCRIPTS = [('devanagari','0900-097F'),('bengali','0980-09FF'),('gurmukhi','0A00-0A7F'),('gujarati','0A80-0AFF'),('oriya','0B00-0B7F'),('tamil','0B80-0BFF'),('telugu','0C00-0C7F'),('kannada','0C80-0CFF'),('malayalam','0D00-0D7F')]
FONT_CSS = ''.join(f"@font-face{{font-family:IndicAll;font-weight:{w};unicode-range:{r},200C-200D,25CC;src:url('file://{FB}/noto-sans-{k}/files/noto-sans-{k}-{k}-{w}-normal.woff2') format('woff2')}}" for k, r in SCRIPTS for w in (400, 600))
FONT_CSS += ".nm,.sb{font-family:IndicAll,Poppins,sans-serif} .card.sm .nm{font-size:8.6pt;line-height:1.4} .card.sm .sb{font-size:6.2pt}"

def lists_for(lang):
    out = {'spices': [], 'nuts': [], 'herbal': []}
    for p in S['products']:
        c = S['comm'][p['c']]; img = pathlib.Path(p['img']).stem
        if lang == 'en':
            name, sub = p['name'], p['sub']
        else:
            k = lang if c['names'].get(lang) else ('hi' if c['names'].get('hi') else None)
            latin = first(c['names'][k]) if k else first(c['trade'])
            nat = first(NATIVE.get(p['c'], {}).get(k)) if k and (k == lang or lang in ('mr', 'kok')) else ''
            name = nat or latin
            qk = PQ.get(p['name']); qv = QUAL.get(qk, {}).get(k) if (nat and qk) else ''
            if qv: name += f' · {qv}'
            sub = (f"{latin} · " if nat and not p['name'].lower().startswith(latin.lower()) else '') + p['name'] + (f" · {p['sub']}" if p.get('grade') else '')
        out[p['cat']].append((img, name, sub))
    return out

def audience(lang):
    UT = {'Andaman & Nicobar Islands','Chandigarh','Dadra & Nagar Haveli and Daman & Diu','Delhi','Jammu & Kashmir','Ladakh','Lakshadweep','Puducherry'}
    st = [s for s, l in S['states'] if l == lang and s not in UT]
    if lang == 'en': return 'All India edition'
    if lang == 'hi': return 'For Hindi-speaking states'
    return 'For ' + ' &amp; '.join(st) if len(st) <= 2 else 'For ' + ', '.join(st[:-1]) + ' &amp; ' + st[-1]

from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page()
    for lang in ['en'] + [k for k, _ in S['langs']]:
        L = lists_for(lang)
        code = head + f"SPICES = {L['spices']!r}\nNUTS = {L['nuts']!r}\nHERBAL = {L['herbal']!r}\n" + rest
        code = code.replace("background-image:url(img/", "background-image:url(img_s/").replace("url(img/", "url(img_s/").replace('src="img/', 'src="img_s/')
        badge = f'<div class="langbadge">Product names in {LANG[lang]} · {audience(lang)}</div>'
        code = code.replace('supplied from Aluva by a family with generations in the spice trade.</div>',
                            'supplied from Aluva by a family with generations in the spice trade.</div>\n    ' + badge)
        code = code.replace("/* COVER */", "/* COVER */\n.langbadge {{ margin-top:4.5mm; padding-top:3mm; border-top:.4mm solid var(--gold); color:var(--turmeric); font-weight:600; font-size:10pt; letter-spacing:.3px; max-width:150mm }}")
        code = code.split("(D / 'flyer.html').write_text")[0]   # stop before the original render step
        ns = {}; exec(code, ns)
        ns['html'] = ns['html'].replace('</style>', FONT_CSS + '</style>', 1) if lang != 'en' else ns['html']
        page = D / f'flyer_{lang}.html'; page.write_text(ns['html'], encoding='utf-8')
        pg.goto(page.as_uri()); pg.wait_for_load_state('networkidle')
        out = OUT / f'Josons_Spices_{LANG[lang]}.pdf'
        pg.pdf(path=str(out), format='A4', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        print(f'{LANG[lang]:10s} {out.stat().st_size/1e6:.1f} MB')
    b.close()
