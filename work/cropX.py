import sys, numpy as np
from PIL import Image, ImageOps
# cropX.py leaf [n=3]: auto-detect text block, column crops with generous overlap -> /tmp/X{leaf}{L|R}{k}.png
leaf=int(sys.argv[1]); n=int(sys.argv[2]) if len(sys.argv)>2 else 3
im=Image.open(f'/workspace/scotus/B/b-{leaf:04d}.jpg').convert('L');W,H=im.size
a=np.asarray(ImageOps.autocontrast(im.resize((W//4,H//4)),cutoff=1)).astype(float); h,w=a.shape; d=a<100
cols=d[int(.15*h):int(.85*h)].mean(0); xs=np.where(cols>0.15)[0]; xs=xs[(xs>0.03*w)&(xs<0.97*w)]
x0,x1=4*xs.min(),4*xs.max(); mid=(x0+x1)//2
rows=d[:,xs.min():xs.max()].mean(1); ys=np.where(rows>0.04)[0]; ys=ys[(ys>0.02*h)&(ys<0.98*h)]
y0,y1=4*ys.min(),4*ys.max()
for side,(c0,c1) in (('L',(x0-30,mid+60)),('R',(mid-60,x1+30))):
  for k in range(n):
    t0=y0+k*(y1-y0)/n-30; t1=y0+(k+1)*(y1-y0)/n+30
    cr=im.crop((max(0,c0),int(max(0,t0)),min(W,c1),int(min(H,t1))));cr=ImageOps.autocontrast(cr,cutoff=1)
    cr=cr.resize((640,int(cr.height*640/cr.width)));cr.save(f'/tmp/X{leaf}{side}{k}.png')
print(leaf,x0,x1,y0,y1)
