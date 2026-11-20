import sys, numpy as np
from PIL import Image, ImageOps
# pg.py page [nstrips]  auto-detect text block, write crops/P{page}_{k}.png
p=int(sys.argv[1]); n=int(sys.argv[2]) if len(sys.argv)>2 else 2
im=Image.open(f'/workspace/scotus/native/a-{p-1:03d}.png').convert('L')
a=np.asarray(ImageOps.autocontrast(im,cutoff=1)).astype(float)
H,W=a.shape
dark=(a<110)
cols=dark[int(.05*H):int(.95*H)].mean(0); rows=dark[:,int(.05*W):int(.95*W)].mean(1)
xs=np.where(cols>0.03)[0]; xs=xs[(xs>0.04*W)&(xs<0.97*W)]
ys=np.where(rows>0.02)[0]; ys=ys[(ys>0.02*H)&(ys<0.97*H)]
x0,x1=max(0,xs.min()-12),min(W,xs.max()+12); y0,y1=max(0,ys.min()-8),min(H,ys.max()+10)
h=(y1-y0)/n
for k in range(n):
    c=im.crop((x0,int(y0+k*h)-8,x1,int(y0+(k+1)*h)+8))
    c=ImageOps.autocontrast(c,cutoff=1); c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
    c.save(f'/workspace/scotus/crops/P{p:02d}_{k}.png')
print(p,x0,x1,y0,y1)
