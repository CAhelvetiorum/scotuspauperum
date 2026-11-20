import json,sys
p='/workspace/scotus/docs/text/manifest.json';m=json.load(open(p))
i,la,en,pg=sys.argv[1:5]
m['sections']=[s for s in m['sections'] if s['id']!=i]+[{"id":i,"la":la,"en":en,"pages":pg}]
open(p,'w').write(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
