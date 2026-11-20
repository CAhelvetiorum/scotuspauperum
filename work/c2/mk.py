import sys,re,glob
# usage: mk.py first last  -> prints sections dict as json
def load(a,b):
    t=''
    for p in range(a,b+1):
        s=open(f'work/c2/p{p:03d}.txt').read().strip()
        if s.startswith('##'): t+='\n'+s
        else: t+=' '+s
    return t
def split(t):
    secs=[];cur=('PRE',[])
    for part in re.split(r'\n?## ',t):
        part=part.strip()
        if not part: continue
        m=re.match(r'(D\d+(?:Q\d+)?)\n(.*)',part,re.S)
        if m:
            secs.append(cur);cur=(m.group(1),[m.group(2).strip()])
        else: cur[1].append(part)
    secs.append(cur);return secs
if __name__=='__main__':
    for k,ps in split(load(int(sys.argv[1]),int(sys.argv[2]))):
        print('=====',k,len(ps))
        for i,p in enumerate(ps): print(i+1,p[:70],'…',p[-40:])
