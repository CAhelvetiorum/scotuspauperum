import json,sys
p='/workspace/scotus/docs/text/manifest.json'; m=json.load(open(p))
ids={s['id'] for s in m['sections']}
for a in sys.argv[1:]:
    i,la,en,pg=a.split('|')
    if i not in ids: m['sections'].append({"id":i,"la":la,"en":en,"pages":pg})
json.dump(m,open(p,'w'),ensure_ascii=False,indent=2)
