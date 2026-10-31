import json, re
from PIL import Image
src=open('/root/flyer/build.py',encoding='utf-8').read()
ns={}; exec(src[src.index('SPICES = ['):src.index('def card(')],ns)
N=json.load(open('/root/site/names.json',encoding='utf-8'))
rows={r['id']:r for r in N['rows']}
sku2c={k:r['id'] for r in N['rows'] for k in r['skus']}
ALIAS={
 'arecanut':(["Betel nut","Supari"],["Beetelnut","Beettlenut","Betelnut"]),
 'mace':(["Javitri"],["Javatri","Javantry"]),
 'kudampuli':(["Kudampuli","Kokum","Garcinia","Brindleberry"],["Goraka","Kodampuli"]),
 'galangal':(["Greater galangal","Kulanjan"],["Kolingen","Kolinjan"]),
 'zedoary':(["White turmeric","Kachur"],["Kachoram"]),
 'ambahaldi':(["Boiled wild turmeric"],["Ambhaldi","Amba haldi","Ambehaldi"]),
 'allspice':(["Pimento","Jamaica pepper","Sarvasugandhi"],["Alspice"]),
 'long_pepper':(["Pippali","Indian long pepper"],["Tripalli","Thippali"]),
 'pepper_stem':(["Chavya","Chavak"],["Pepper stem","Peeper stem","Chavyam"]),
 'cashew':(["Cashew in shell","RCN"],["Kaju"]),
 'triphal':(["Tirphal","Indian prickly ash","Teppal"],["Triphal","Tefal"]),
 'marotti':(["Marotti","Hydnocarpus seeds"],["Marottykuru","Marotty"]),
 'cocculus':(["Fish berry","Levant nut"],["Coconas seeds","Kakkakkolli"]),
 'nux_vomica':(["Poison nut","Kuchla"],["Nuxvomica"]),
 'rampatri':(["Rampatri","Wild mace"],["Ram patri"]),
 'ramgot':(["Ramgot","Wild nutmeg"],[]),
 'cycas':(["Cycas flower","Madhana poo"],["Madhanakam poo","Madan mast"]),
 'poolamuttu':(["Marathi moggu","Poolamuttu"],["Marati moggu","Kapok"]),
 'nagkesar':(["Nagkesar","Nageshwar"],["Gotti nageshwar","Gota nagkesar"]),
 'black_pepper':(["Kali mirch"],["Pepper"]),
 'cloves':([],["Clove","Laung"]),'nutmeg':([],["Jaiphal"]),
 'wild_turmeric':(["Kasthuri manjal"],["Kasturi"]),'samudraphal':(["Barringtonia seeds"],[]),
}
RENAME={"Ambhaldi":"Ambahaldi","Pepper Stem":"Chavya (Pepper Stem)","Garcinia / Kudampuli":"Kudampuli (Malabar Tamarind)"}
GRADE={"Nutmeg":"Whole, shelled","Nutmeg with Shell":"Whole, in shell","Nutmeg Splits":"Second quality · splits","Nutmeg Shell Seconds":"Extraction quality",
 "Mace Flower":"Whole mace","Mace Slice":"Ordinary · slice","Arecanut":"Whole, first quality","Badala Arecanut":"Second quality","Mysore Arecanut":"Pooja grade · small",
 "Coffee Beans":"Clean green beans","Coffee with Shell":"Whole dried cherry","Ambhaldi":"Boiled & dried","Poolamuttu":"No. 1 grade"}
prods=[]
for cat,L in (("spices",ns['SPICES']),("nuts",ns['NUTS']),("herbal",ns['HERBAL'])):
    for p,n,s in L:
        cid=sku2c[n]; slug=re.sub(r'[^a-z0-9]+','-',RENAME.get(n,n).lower()).strip('-')
        im=Image.open(f'/root/flyer/img/{p}.jpg').convert('RGB'); im.thumbnail((560,560)); im.save(f'/root/site/build/img/{p}.jpg',quality=80)
        b=rows[cid]['bot']
        prods.append(dict(slug=slug,name=RENAME.get(n,n),sub=GRADE.get(n,'' if '[' in b else b),grade=n in GRADE,cat=cat,c=cid,img=f'img/{p}.jpg'))
comm={}
for r in N['rows']:
    a,so=ALIAS.get(r['id'],([],[]))
    comm[r['id']]=dict(en=r['en'],trade=r['trade'],bot=r['bot'],sa=r['sa'].rstrip('?') if not r['sa'].endswith('?') else '',
        names={k:v for k,v in r['names'].items() if not v.endswith('?')},   # public site: confirmed names only
        aka=a,search=so+[v.rstrip('?') for v in r['names'].values()],note=r['note'] if r['id'] in ('triphal','kudampuli','nux_vomica','cocculus','poolamuttu','ambahaldi','pepper_stem') else '')
for f,sz in [('m_mace',700),('m_turm',500),('m_pep',500),('m_nut',460),('m_ramp',500),('m_clove',380),('m_nutsh',340),('tray',600)]:
    im=Image.open(f'/root/flyer/img/{f}.jpg').convert('RGB'); im.thumbnail((sz,sz)); im.save(f'/root/site/build/img/{f}.jpg',quality=80)
Image.open('/root/flyer/img/logo.png').resize((320,320),Image.LANCZOS).save('/root/site/build/img/logo.png',optimize=True)
json.dump(dict(langs=N['langs'],states=N['states'],products=prods,comm=comm),open('/root/site/site_data.json','w'),ensure_ascii=False)
print(len(prods),'products,',len(comm),'commodities')
