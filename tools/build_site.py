import re, json, sys
sys.path.insert(0,'/root/site')
from native import NATIVE, SA, PQ, QUAL
out='/home/claude/josons_site/index.html'
old=open(out,encoding='utf-8').read()
m=re.search(r'const D = (\{.*?\});\n',old,re.S)
D=json.loads(m.group(1))
for cid,c in D['comm'].items():
    nat={k:v for k,v in NATIVE.get(cid,{}).items() if k in c['names']}
    c['native']=nat
    c['sad']=SA.get(c['sa'],'')
    # every native entry must line up with a confirmed Latin name, and have the same number of " / " parts
    for k,v in nat.items(): assert len(v.split(' / '))==len(c['names'][k].split(' / ')),(cid,k,v,c['names'][k])
    miss=[k for k in c['names'] if k not in nat]
    if miss: print('no native:',cid,miss)
D['qual']=QUAL
for pr in D['products']:
    pr.pop('q',None)
    if pr['name'] in PQ: pr['q']=PQ[pr['name']]
    elif pr['name'].replace(' (Pepper Stem)','') in PQ: pr['q']=PQ[pr['name']]
print('qualified:',[pr['name'] for pr in D['products'] if 'q' in pr])
tpl=open('/root/site/site_template.html',encoding='utf-8').read()
open(out,'w',encoding='utf-8').write(tpl.replace('__DATA__',json.dumps(D,ensure_ascii=False)))
print('built', sum(len(c['native']) for c in D['comm'].values()),'native names')
