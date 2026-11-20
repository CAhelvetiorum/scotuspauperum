import sys, numpy as np
from PIL import Image, ImageOps
# pz.py page [nstrips=5]: text block (excluding sparse marginalia) -> crops/z/Z{page}_{k}.png width ~1040
import os; os.makedirs('/workspace/scotus/crops/z',exist_ok=True)
p=int(sys.argv[1]); n=int(sys.argv[2]) if len(sys.argv)>2 else 5
im=Image.open(f'/workspace/scotus/native/a-{p-1:03d}.png').convert('L')
a=np.asarray(ImageOps.autocontrast(im,cutoff=1)).astype(float); H,W=a.shape
dark=a<110
cols=dark[int(.1*H):int(.9*H)].mean(0)
sm=np.convolve(cols,np.ones(15)/15,'same')
xs=np.where(sm>0.10)[0]; xs=xs[(xs>0.03*W)&(xs<0.98*W)]
x0,x1=max(0,xs.min()-14),min(W,xs.max()+14)
rows=dark[:,x0:x1].mean(1); ys=np.where(rows>0.02)[0]; ys=ys[(ys>0.015*H)&(ys<0.985*H)]
y0,y1=max(0,ys.min()-8),min(H,ys.max()+10)
h=(y1-y0)/n; s=1040/(x1-x0)
for k in range(n):
    c=im.crop((x0,int(y0+k*h)-10,x1,int(y0+(k+1)*h)+10))
    c=ImageOps.autocontrast(c,cutoff=1); c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
    c.save(f'/workspace/scotus/crops/z/Z{p}_{k}.png')
print(p,x0,x1,y0,y1,W,H)
