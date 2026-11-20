import sys,json
sys.path.insert(0,'work/c2'); from mk import load,split
# meta: key -> (id, title, pages, heading, trailing)
meta=json.loads(open(sys.argv[3]).read())
for k,ps in split(load(int(sys.argv[1]),int(sys.argv[2]))):
    if k not in meta: continue
    sid,title,pages,head,tail=meta[k]
    out=f'---\nsection: "{sid}"\ntitle: "{title}"\npages: "{pages}"\n---\n\n'
    if head: out+=f'{{#s{sid}-h .heading}} {head}\n\n'
    for i,p in enumerate(ps): out+=f'{{#s{sid}-{i+1:02d}}} {p}'+(tail if (tail and i==len(ps)-1) else '')+'\n\n'
    open(f'docs/text/latin/{sid}.md','w').write(out.rstrip('\n')+'\n'); print('wrote',sid,len(ps))
