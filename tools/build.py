import qrcode, pathlib
from playwright.sync_api import sync_playwright

D = pathlib.Path('/root/flyer')

qrcode.make("mailto:manudparakkal@hotmail.com?subject=Product%20enquiry%20-%20Josons%20Spices",
            border=1, box_size=12).save(D / 'img/qr.png')

SPICES = [
    ("n02", "Alleppey Turmeric", "Manjal · Haldi · Curcuma longa"),
    ("n09", "Black Pepper", "Kurumulaku · Kaali Mirch · Piper nigrum"),
    ("q_longp", "Long Pepper", "Thippali · Pippali · Piper longum"),
    ("n06", "Pepper Stem", "Piper nigrum stems"),
    ("n07", "Allspice", "Sarvasugandhi · Pimenta dioica"),
    ("p14", "Cloves", "Grambu · Laung"),
    ("n10", "Mace Flower", "Jathipathri · Javitri"),
    ("p03", "Mace Slice", "Javitri ordinary · Myristica fragrans"),
    ("p05", "Nutmeg", "Jathikka · Jaiphal"),
    ("p04", "Nutmeg with Shell", "Jathikka · Jaikai"),
    ("p06", "Nutmeg Splits", "Second quality · Jaiphal splits"),
    ("p07", "Nutmeg Shell Seconds", "Extraction quality"),
    ("p15", "Wild Turmeric", "Kasthuri Manjal"),
    ("n01", "Ambhaldi", "Amba haldi · Curcuma"),
    ("n04", "Galangal Root", "Kolinjan · Kulanjan"),
    ("p24", "Zedoary", "Kachoram · Curcuma zedoaria"),
    ("p21", "Garcinia / Kudampuli", "Malabar tamarind · Goraka"),
]
NUTS = [
    ("p08", "Arecanut", "Supari · Chaali"),
    ("p09", "Badala Arecanut", "Second quality supari"),
    ("q_mys", "Mysore Arecanut", "Pooja · Chotta supari"),
    ("p11", "Coffee Beans", "Kaapi · Clean green beans"),
    ("p12", "Coffee with Shell", "Whole dried cherry"),
    ("p25", "Cocoa Beans", "Koko · Dried & fermented"),
    ("p13", "Raw Cashew", "Kaju · In shell"),
]
HERBAL = [
    ("n03", "Samudraphal", "Barringtonia seeds"),
    ("q_trip", "Triphal", "Zanthoxylum rhetsa"),
    ("n08", "Poolamuttu", "No. 1 grade"),
    ("n11", "Marotty Kuru", "Marotty seeds · Chaulmoogra"),
    ("p20", "Nux Vomica", "Kanjiram · Kuchla"),
    ("q_cocc", "Cocculus Seeds", "Kakka kolli"),
    ("p26", "Varigar", "Herbal raw material"),
    ("p27", "Rampatri", "Bombay mace"),
    ("p28", "Ramgot", "Bombay nutmeg"),
    ("p29", "Madhana Poo", "Queen sago flower"),
    ("q_gotti", "Gotti Nagkesar", "Nageshwar · Ayurvedic raw material"),
]

def card(p, n, s, cls=""):
    return f'<div class="card {cls}"><div class="ph" style="background-image:url(img/{p}.jpg)"></div><div class="nm">{n}</div><div class="sb">{s}</div></div>'

def note(title, body, color):
    return f'<div class="card note" style="background:{color}"><div class="nt">{title}</div><div class="nb">{body}</div></div>'

FOOT = '''<div class="foot"><span>JOSONS SPICES · Parakkal Buildings, Aluva, Kerala</span><span>+91 94470 29905 · manudparakkal@hotmail.com</span></div>'''
KASAVU = '<div class="kasavu"></div>'

spice_cards = "".join(card(*x, cls="sm") for x in SPICES)
spice_cards += note("Whole &amp; graded", "Premium, FAQ and seconds grades for every price point.", "var(--turmeric)")
spice_cards += note("Samples first", "Ask for a sample before you place a bulk order.", "var(--chili)")
spice_cards += note("Current crop", "Ask us what is fresh in season right now.", "var(--leaf)")
nut_cards = "".join(card(*x) for x in NUTS) + note("Bulk ready", "Loose or packed to your spec — just ask.", "var(--leaf)")
herb_cards = "".join(card(*x, cls="sm") for x in HERBAL) + note("Need more?", "Tell us what you need — we source on request.", "var(--mace)")

html = f'''<!doctype html><html><head><meta charset="utf-8"><title>Josons Spices Brochure</title><style>
@page {{ size: A4; margin: 0 }}
:root {{ --leaf:#0F3D2E; --leaf2:#185A43; --turmeric:#E8A317; --chili:#B3261E; --mace:#C8102E;
        --cream:#FBF4E4; --gold:#C9A227; --ink:#2A1A10; --muted:#7A6555 }}
* {{ box-sizing:border-box; margin:0; padding:0 }}
body {{ font-family:Poppins,sans-serif; color:var(--ink); -webkit-print-color-adjust:exact }}
.page {{ width:210mm; height:297mm; position:relative; overflow:hidden; page-break-after:always; background:var(--cream) }}
.serif {{ font-family:Lora,serif }}
.kasavu {{ position:absolute; left:0; right:0; bottom:0; height:9mm;
   background:linear-gradient(var(--gold) 0 2mm, var(--cream) 2mm 3mm, var(--gold) 3mm 3.6mm, var(--leaf) 3.6mm) }}
.foot {{ position:absolute; left:14mm; right:14mm; bottom:12mm; display:flex; justify-content:space-between;
   font-size:7.5pt; color:var(--muted); letter-spacing:.3px; border-top:.3mm solid #e4d6b8; padding-top:2.5mm }}

/* COVER */
.cover {{ background:radial-gradient(circle at 75% 35%, #1d6b4f 0, var(--leaf) 55%, #0a2a20 100%); color:var(--cream) }}
.brand {{ position:absolute; top:16mm; left:16mm; display:flex; align-items:center; gap:4mm }}
.seal {{ width:17mm; height:17mm; border-radius:50%; border:.7mm solid var(--gold); display:flex; align-items:center;
   justify-content:center; font-family:Lora; font-size:20pt; font-weight:700; color:var(--gold) }}
.bname {{ font-weight:700; letter-spacing:4px; font-size:15pt }}
.bsub {{ font-size:7.5pt; letter-spacing:3px; color:var(--turmeric) }}
.logo {{ position:absolute; top:10mm; left:14mm; width:42mm; height:42mm }}
.logo2 {{ flex:none; width:36mm; height:36mm }}
.est {{ position:absolute; top:19mm; right:16mm; border:.4mm solid var(--gold); color:var(--gold); padding:2mm 4mm;
   border-radius:20mm; font-size:8pt; letter-spacing:2px }}
.collage {{ position:absolute; top:48mm; left:0; right:0; height:132mm }}
.dot {{ position:absolute; border-radius:50%; background-size:cover; background-position:center;
   border:1.6mm solid var(--cream); outline:.5mm solid var(--gold); outline-offset:1mm }}
.headline {{ position:absolute; left:16mm; right:16mm; top:186mm }}
.kicker {{ color:var(--turmeric); font-size:9pt; letter-spacing:4px; font-weight:600 }}
.h1 {{ font-family:Lora; font-size:38pt; line-height:1.05; margin-top:3mm }}
.h1 em {{ color:var(--turmeric); font-style:italic }}
.lede {{ font-size:10.5pt; line-height:1.6; margin-top:5mm; max-width:150mm; color:#e7dcc3; font-weight:300 }}
.pills {{ position:absolute; left:16mm; bottom:20mm; display:flex; gap:3mm }}
.pill {{ padding:2.2mm 5mm; border-radius:20mm; font-size:8.5pt; font-weight:600; color:var(--leaf) }}

/* ABOUT */
.about-top {{ height:106mm; background:var(--chili); color:var(--cream); position:relative; padding:15mm 16mm }}
.about-top .h2 {{ font-family:Lora; font-size:30pt; line-height:1.1; max-width:105mm }}
.about-top p {{ font-size:10pt; line-height:1.65; margin-top:6mm; max-width:100mm; font-weight:300 }}
.tray {{ position:absolute; right:14mm; top:17mm; width:68mm; height:66mm; background:url(img/tray.jpg) center/cover;
   border:2mm solid var(--gold); border-radius:3mm; transform:rotate(3deg) }}
.stats {{ display:flex; margin:-14mm 14mm 0; position:relative; background:#fff; border-radius:4mm;
   border:.4mm solid #e6d5b0 }}
.stat {{ flex:1; text-align:center; padding:6mm 2mm; border-right:.3mm solid #eee2c8 }}
.stat:last-child {{ border:0 }}
.stat b {{ display:block; font-family:Lora; font-size:24pt; color:var(--chili) }}
.stat span {{ font-size:7.5pt; letter-spacing:1.5px; color:var(--muted); text-transform:uppercase }}
.why {{ padding:9mm 16mm 0 }}
.sect {{ font-size:8.5pt; letter-spacing:4px; color:var(--chili); font-weight:600 }}
.h3 {{ font-family:Lora; font-size:22pt; color:var(--leaf); margin:2mm 0 5mm }}
.grid2 {{ display:grid; grid-template-columns:1fr 1fr; gap:5mm }}
.why .item {{ display:flex; gap:4mm }}
.ico {{ flex:none; width:12mm; height:12mm; border-radius:50%; display:flex; align-items:center; justify-content:center;
   color:#fff; font-weight:700; font-size:12pt }}
.why h4 {{ font-size:11pt; color:var(--leaf) }}
.why .item p {{ font-size:8.8pt; line-height:1.55; color:#5a4636; margin-top:1mm }}
.cats {{ display:flex; gap:4mm; margin-top:7mm }}
.cat {{ flex:1; border-radius:3mm; padding:5mm; color:#fff }}
.cat b {{ font-family:Lora; font-size:13pt; display:block }}
.cat span {{ font-size:8pt; opacity:.9 }}

/* CATALOGUE */
.band {{ padding:14mm 14mm 7mm; color:var(--cream); position:relative }}
.band .sect {{ color:var(--turmeric) }}
.band .h3 {{ color:var(--cream); margin:1mm 0 0 }}
.band .pg {{ position:absolute; right:14mm; top:15mm; font-family:Lora; font-size:30pt; opacity:.25 }}
.grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:4mm; padding:6mm 14mm 0 }}
.grid5 {{ grid-template-columns:repeat(5,1fr); gap:3.2mm }}
.card {{ background:#fff; border-radius:3mm; padding:2mm 2mm 3mm; border:.3mm solid #eadcbf }}
.ph {{ width:100%; aspect-ratio:1/1; border-radius:2mm; background-size:cover; background-position:center }}
.nm {{ font-weight:600; font-size:8.6pt; margin-top:2mm; color:var(--leaf); line-height:1.2 }}
.sb {{ font-size:6.6pt; color:var(--muted); margin-top:.6mm; line-height:1.3 }}
.card.sm .nm {{ font-size:7.8pt }} .card.sm .sb {{ font-size:6pt }}
.note {{ color:#fff; display:flex; flex-direction:column; justify-content:center; padding:5mm }}
.nt {{ font-family:Lora; font-size:13pt; font-weight:700; line-height:1.15 }}
.nb {{ font-size:8pt; margin-top:2.5mm; line-height:1.45; opacity:.95 }}
.subhead {{ padding:7mm 14mm 0; display:flex; align-items:baseline; gap:4mm }}
.subhead .h3 {{ margin:0; font-size:17pt }}
.subhead span {{ font-size:8pt; color:var(--muted) }}

.sign {{ margin:7mm 16mm 0; border-left:1.2mm solid var(--gold); padding:1mm 0 1mm 5mm }}
.sig-q {{ font-family:Lora; font-style:italic; font-size:11pt; color:var(--leaf); line-height:1.45 }}
.sig-n {{ font-size:9pt; font-weight:600; margin-top:2.5mm; color:var(--chili) }}
.sig-n span {{ font-weight:400; color:var(--muted) }}
.proc {{ display:grid; grid-template-columns:repeat(6,1fr); gap:3mm; padding:12mm 14mm 0 }}
.pstep {{ background:#fff; border:.3mm solid #eadcbf; border-radius:3mm; padding:5mm 3mm; min-height:44mm }}
.pstep b {{ display:inline-flex; width:9mm; height:9mm; border-radius:50%; color:#fff; font-size:8pt;
   align-items:center; justify-content:center }}
.pstep h4 {{ font-size:9.5pt; color:var(--leaf); margin-top:2.5mm }}
.pstep p {{ font-size:7pt; color:#5a4636; line-height:1.45; margin-top:1mm }}
.twocol {{ display:grid; grid-template-columns:1.25fr 1fr; gap:5mm; padding:11mm 14mm 0 }}
.box {{ background:#fff; border:.3mm solid #eadcbf; border-radius:3mm; padding:6mm }}
.bh {{ font-family:Lora; font-size:15pt; color:var(--leaf); margin:1.5mm 0 4mm }}
.cal {{ width:100%; border-collapse:collapse; font-size:7pt }}
.cal th {{ color:var(--muted); font-weight:600; padding-bottom:1.5mm; width:6.5% }}
.cal td {{ padding:2mm .3mm; border-top:.2mm solid #f0e6d0 }}
.cal td i {{ display:block; height:4.5mm; border-radius:1mm }}
.cal .cn {{ font-weight:600; color:var(--leaf); white-space:nowrap; padding-right:2mm; font-size:7.6pt }}
.fn {{ font-size:6.6pt; color:var(--muted); margin-top:3mm; line-height:1.4 }}
.spec {{ list-style:none }}
.spec li {{ font-size:8.4pt; line-height:1.45; color:#5a4636; padding:2.4mm 0 1.6mm 5mm; border-top:.2mm solid #f0e6d0; position:relative }}
.spec li:before {{ content:""; position:absolute; left:0; top:3mm; width:2mm; height:2mm; border-radius:50%; background:var(--turmeric) }}
.spec b {{ color:var(--leaf) }}
.who {{ padding:12mm 14mm 0 }}
.tags {{ display:flex; flex-wrap:wrap; gap:2.5mm }}
.tags span {{ background:var(--leaf); color:var(--cream); font-size:8pt; padding:2mm 4mm; border-radius:20mm }}
.cred {{ position:absolute; left:16mm; right:16mm; bottom:22mm; display:flex; gap:7mm; align-items:center;
   border-top:.3mm solid rgba(201,162,39,.5); padding-top:8mm }}
.seal2 {{ flex:none; width:32mm; height:32mm; border-radius:50%; border:.8mm solid var(--gold); outline:.3mm solid var(--gold);
   outline-offset:1.2mm; display:flex; flex-direction:column; align-items:center; justify-content:center; color:var(--gold);
   font-size:7pt; letter-spacing:2px }}
.seal2 b {{ font-family:Lora; font-size:20pt; letter-spacing:0; color:var(--cream) }}
.promise {{ flex:1 }}
.pq {{ font-family:Lora; font-style:italic; font-size:17pt; line-height:1.3; color:var(--cream) }}
.ps {{ font-size:8.5pt; color:var(--turmeric); margin-top:2.5mm; letter-spacing:.5px }}
.creds {{ flex:1; display:grid; grid-template-columns:1fr 1fr; gap:3mm 6mm }}
.cr span {{ display:block; font-size:7pt; letter-spacing:2px; color:var(--turmeric); text-transform:uppercase }}
.cr b {{ font-size:9.5pt; font-weight:500 }}
.cta {{ margin:5mm 14mm 0; padding:3mm 5mm; background:var(--mace); color:#fff; border-radius:2.5mm; font-size:9pt; font-weight:600 }}
.wide .ph {{ aspect-ratio:4/3 }}
.grid6 {{ grid-template-columns:repeat(6,1fr); gap:2.8mm }}
.grid6 .nt {{ font-size:10.5pt }} .grid6 .nb {{ font-size:7pt }}
.grid5 .nt {{ font-size:11.5pt }}
/* BACK */
.back {{ background:var(--leaf); color:var(--cream) }}
.back .top {{ padding:22mm 16mm 0 }}
.back .h1 {{ font-size:34pt }}
.steps {{ display:flex; gap:5mm; padding:12mm 16mm 0 }}
.step {{ flex:1; background:rgba(255,255,255,.06); border:.3mm solid rgba(201,162,39,.5); border-radius:3mm; padding:6mm 5mm }}
.step b {{ display:inline-flex; width:9mm; height:9mm; border-radius:50%; background:var(--turmeric); color:var(--leaf);
   align-items:center; justify-content:center; font-size:11pt }}
.step h4 {{ font-size:11pt; margin-top:3mm }}
.step p {{ font-size:8.5pt; color:#d9ceb5; margin-top:1.5mm; line-height:1.5 }}
.contact {{ margin:12mm 16mm 0; background:var(--cream); color:var(--ink); border-radius:4mm; display:flex; overflow:hidden }}
.cl {{ flex:1; padding:9mm 9mm }}
.cl h4 {{ font-family:Lora; font-size:18pt; color:var(--chili) }}
.row {{ display:flex; gap:4mm; margin-top:5mm; align-items:flex-start }}
.row .k {{ width:20mm; font-size:7.5pt; letter-spacing:2px; color:var(--muted); padding-top:1mm }}
.row .v {{ font-size:11pt; font-weight:600; color:var(--leaf); line-height:1.45 }}
.qr {{ width:62mm; background:var(--turmeric); display:flex; flex-direction:column; align-items:center; justify-content:center; padding:6mm }}
.qr img {{ width:40mm; height:40mm; background:#fff; padding:2mm; border-radius:2mm }}
.qr span {{ font-size:8.5pt; font-weight:600; color:var(--leaf); margin-top:3mm; text-align:center; line-height:1.35 }}
.strip {{ position:absolute; left:0; right:0; bottom:9mm; height:44mm; display:flex }}
.strip div {{ flex:1; background-size:cover; background-position:center }}
</style></head><body>

<!-- 1 COVER -->
<section class="page cover">
  <img class="logo" src="img/logo.png">
  <div class="est">ALUVA · KERALA · INDIA</div>
  <div class="collage">
    <div class="dot" style="width:78mm;height:78mm;left:72mm;top:24mm;background-image:url(img/m_mace.jpg)"></div>
    <div class="dot" style="width:52mm;height:52mm;left:14mm;top:12mm;background-image:url(img/m_turm.jpg)"></div>
    <div class="dot" style="width:46mm;height:46mm;left:150mm;top:2mm;background-image:url(img/m_pep.jpg)"></div>
    <div class="dot" style="width:44mm;height:44mm;left:12mm;top:72mm;background-image:url(img/m_nut.jpg)"></div>
    <div class="dot" style="width:50mm;height:50mm;left:154mm;top:62mm;background-image:url(img/m_ramp.jpg)"></div>
    <div class="dot" style="width:32mm;height:32mm;left:58mm;top:100mm;background-image:url(img/m_clove.jpg)"></div>
    <div class="dot" style="width:28mm;height:28mm;left:126mm;top:104mm;background-image:url(img/m_nutsh.jpg)"></div>
  </div>
  <div class="headline">
    <div class="kicker">WHOLESALE · TRADE · SUPPLY</div>
    <div class="h1">Straight from Kerala's<br><em>Spice Coast</em> to your warehouse.</div>
    <div class="lede">Whole spices, nuts, beans and Ayurvedic raw materials — sourced, graded and supplied from Aluva by a family with generations in the spice trade.</div>
  </div>
  <div class="pills">
    <div class="pill" style="background:var(--turmeric)">Spices &amp; Roots</div>
    <div class="pill" style="background:#F2C9A0">Nuts &amp; Beans</div>
    <div class="pill" style="background:#BFD8B8">Herbal Raw Materials</div>
  </div>
  {KASAVU}
</section>

<!-- 2 ABOUT -->
<section class="page">
  <div class="about-top">
    <div class="h2">Generations on the spice route.</div>
    <p>Handed down from father to son, the family's spice trade in Aluva has carried the Josons name since 1995. We buy from growers across Kerala, sort every lot by hand, and supply buyers who need consistent quality at a fair price.</p>
    <div class="tray"></div>
  </div>
  <div class="stats">
    <div class="stat"><b>1995</b><span>Josons founded</span></div>
    <div class="stat"><b>30+</b><span>Products</span></div>
    <div class="stat"><b>3</b><span>Product categories</span></div>
  </div>
  <div class="why">
    <div class="sect">WHY BUY FROM US</div>
    <div class="h3">What our customers count on</div>
    <div class="grid2">
      <div class="item"><div class="ico" style="background:var(--chili)">1</div><div><h4>Sourced at the source</h4><p>Bought directly from Kerala's growing belts — no long chain of middlemen between farm and buyer.</p></div></div>
      <div class="item"><div class="ico" style="background:var(--turmeric)">2</div><div><h4>A grade for every need</h4><p>From bold premium nutmeg to splits and extraction-quality seconds — buy exactly the quality your product calls for.</p></div></div>
      <div class="item"><div class="ico" style="background:var(--leaf2)">3</div><div><h4>Hand-sorted lots</h4><p>Every consignment is cleaned and checked before it leaves Aluva, so what you sample is what you receive.</p></div></div>
      <div class="item"><div class="ico" style="background:var(--mace)">4</div><div><h4>Personal service</h4><p>One family, one phone number. Quick quotes, honest advice on seasonality and pricing.</p></div></div>
    </div>
    <div class="cats">
      <div class="cat" style="background:var(--turmeric)"><b>Spices &amp; Roots</b><span>Pepper · Nutmeg · Mace · Cloves · Turmeric</span></div>
      <div class="cat" style="background:#8B4A2B"><b>Nuts &amp; Beans</b><span>Arecanut · Cashew · Coffee · Cocoa</span></div>
      <div class="cat" style="background:var(--leaf2)"><b>Herbal</b><span>Ayurvedic seeds, roots &amp; flowers</span></div>
    </div>
  </div>
    <div class="sign"><div class="sig-l"><div class="sig-q">&ldquo;Every lot that leaves Aluva carries the Josons name. We would not send you anything we would not buy ourselves.&rdquo;</div>
      <div class="sig-n">Manu Dominic Parakkal <span>· Proprietor, Josons Spices</span></div></div></div>
  </div>
  {FOOT}{KASAVU}
</section>

<!-- 3 QUALITY -->
<section class="page">
  <div class="band" style="background:linear-gradient(120deg,var(--leaf),#0a2a20)">
    <div class="sect">QUALITY &amp; EXPERTISE</div><div class="h3">From the farm gate to your godown</div>
  </div>
  <div class="proc">
    <div class="pstep"><b style="background:var(--chili)">01</b><h4>Source</h4><p>Bought from growers and primary markets across Kerala's spice belts.</p></div>
    <div class="pstep"><b style="background:var(--turmeric)">02</b><h4>Clean</h4><p>Stones, stalks, dust and foreign matter removed.</p></div>
    <div class="pstep"><b style="background:var(--mace)">03</b><h4>Grade</h4><p>Sorted by size, colour and soundness into clear grades.</p></div>
    <div class="pstep"><b style="background:#8B4A2B">04</b><h4>Dry &amp; check</h4><p>Moisture checked so stock travels and stores well.</p></div>
    <div class="pstep"><b style="background:var(--leaf2)">05</b><h4>Pack</h4><p>Packed to the buyer's weight and bag preference.</p></div>
    <div class="pstep"><b style="background:var(--gold)">06</b><h4>Dispatch</h4><p>Shipped from Aluva by road, rail or courier.</p></div>
  </div>
  <div class="twocol">
    <div class="box">
      <div class="sect">HARVEST CALENDAR</div>
      <div class="bh">When new crop arrives</div>
      <table class="cal"><tr><th></th>{"".join(f"<th>{m}</th>" for m in "JFMAMJJASOND")}</tr>
      {"".join(f'<tr><td class="cn">{n}</td>' + "".join(f'<td><i style="background:{c}"></i></td>' if (k+1) in ms else '<td></td>' for k in range(12)) + '</tr>' for n,c,ms in [
        ("Black pepper","#2A1A10",[11,12,1,2,3]),
        ("Cloves","#8B4A2B",[1,2,3,4]),
        ("Turmeric","#E8A317",[1,2,3,4]),
        ("Raw cashew","#9C7A3C",[1,2,3,4,5]),
        ("Nutmeg &amp; mace","#C8102E",[6,7,8]),
      ])}
      </table>
      <div class="fn">Indicative Indian/Kerala seasons; timing shifts with monsoon and altitude. Ask us about current-crop availability.</div>
    </div>
    <div class="box">
      <div class="sect">EVERY QUOTE STATES</div>
      <div class="bh">No guesswork for buyers</div>
      <ul class="spec">
        <li><b>Product &amp; grade</b> — e.g. bold, FAQ, splits, extraction</li>
        <li><b>Origin</b> — growing region in Kerala</li>
        <li><b>Moisture &amp; cleanliness</b> — as checked before dispatch</li>
        <li><b>Packing</b> — bag type and net weight</li>
        <li><b>Price &amp; validity</b> — current-crop rate and terms</li>
        <li><b>Sample</b> — sent on request before bulk orders</li>
      </ul>
    </div>
  </div>
  <div class="who">
    <div class="sect" style="margin-bottom:3mm">WHO WE SUPPLY</div>
    <div class="tags"><span>Spice traders &amp; wholesalers</span><span>Masala &amp; food processors</span><span>Ayurvedic manufacturers</span><span>Oleoresin &amp; extraction units</span><span>Exporters</span><span>Pooja &amp; supari dealers</span></div>
  </div>
  {FOOT}{KASAVU}
</section>

<!-- 4 SPICES -->
<section class="page">
  <div class="band" style="background:linear-gradient(120deg,var(--chili),#7d1a14)">
    <div class="sect">CATALOGUE · 01</div><div class="h3">Spices &amp; Aromatic Roots</div><div class="pg">01</div>
  </div>
  <div class="grid grid5">{spice_cards}</div>
  {FOOT}{KASAVU}
</section>

<!-- 4 NUTS + HERBAL -->
<section class="page">
  <div class="band" style="background:linear-gradient(120deg,#8B4A2B,#4f2614)">
    <div class="sect">CATALOGUE · 02</div><div class="h3">Nuts, Beans &amp; Herbal Raw Materials</div><div class="pg">02</div>
  </div>
  <div class="subhead"><div class="h3">Nuts &amp; Beans</div><span>Arecanut · coffee · cocoa · cashew</span></div>
  <div class="grid wide" style="padding-top:4mm">{nut_cards}</div>
  <div class="subhead"><div class="h3">Ayurvedic &amp; Herbal</div><span>For pharmacies, extractors &amp; traditional medicine makers</span></div>
  <div class="grid grid6" style="padding-top:4mm">{herb_cards}</div>
  {FOOT}{KASAVU}
</section>

<!-- 5 BACK -->
<section class="page back">
  <div class="top">
    <div class="kicker">LET'S DO BUSINESS</div>
    <div class="h1">Ordering is <em>simple.</em></div>
  </div>
  <div class="steps">
    <div class="step"><b>1</b><h4>Send an enquiry</h4><p>Tell us the product, grade and quantity you need.</p></div>
    <div class="step"><b>2</b><h4>Get a quote &amp; sample</h4><p>We reply with current pricing and can send a sample.</p></div>
    <div class="step"><b>3</b><h4>Confirm &amp; dispatch</h4><p>Packed to order and dispatched from Aluva.</p></div>
  </div>
  <div class="contact">
    <div class="cl">
      <h4>Josons Spices</h4>
      <div class="row"><div class="k">MOBILE</div><div class="v">+91 94470 29905</div></div>
      <div class="row"><div class="k">PHONE</div><div class="v">+91 484 262 3585</div></div>
      <div class="row"><div class="k">EMAIL</div><div class="v">manudparakkal@hotmail.com</div></div>
      <div class="row"><div class="k">VISIT</div><div class="v" style="font-size:9.5pt;font-weight:500">Parakkal Buildings<br>Aluva<br>Kerala</div></div>
    </div>
    <div class="qr"><img src="img/qr.png"><span>Scan to email<br>an enquiry</span></div>
  </div>
  <div class="cred">
    <img class="logo2" src="img/logo.png">
    <div class="promise"><div class="pq">Generations of trust, one lot at a time.</div>
      <div class="ps">A family-run trading house · Parakkal Buildings, Aluva, Kerala</div></div>
  </div>
  {KASAVU}
</section>
</body></html>'''

(D / 'flyer.html').write_text(html, encoding='utf-8')
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto((D / 'flyer.html').as_uri())
    pg.wait_for_load_state('networkidle')
    pg.pdf(path=str(D / 'Josons_Spices_Brochure_Classic.pdf'), format='A4', print_background=True,
           margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
    b.close()
print('done')
