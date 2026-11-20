import sys, numpy as np
from PIL import Image, ImageOps
# bcols.py leaf [nparts=3] [cols=LR]: auto-detect text block of B page, split into 2 columns, n parts each
i=int(sys.argv[1]); n=int(sys.argv[2]) if len(sys.argv)>2 else 3; which=sys.argv[3] if len(sys.argv)>3 else 'LR'
im=Image.open(f'/workspace/scotus/B/b-{i:04d}.jpg').convert('L')
a=np.asarray(ImageOps.autocontrast(im.resize((im.width//4,im.height//4)),cutoff=1)).astype(float)
H,W=a.shape; d=a<100
cols=d[int(.1*H):int(.9*H)].mean(0); xs=np.where(cols>0.08)[0]; xs=xs[(xs>0.05*W)&(xs<0.97*W)]
rows=d[:,xs.min():xs.max()].mean(1); ys=np.where(rows>0.04)[0]; ys=ys[(ys>0.03*H)&(ys<0.97*H)]
x0,x1,y0,y1=[4*v for v in (xs.min(),xs.max(),ys.min(),ys.max())]
mid=(x0+x1)//2
# find gutter near mid
seg=cols[(mid//4)-40:(mid//4)+40]; g=(mid//4)-40+int(np.argmin(seg)); mid=4*g
h=(y1-y0)/n
for c,(a0,a1) in zip('LR',[(x0-10,mid+8),(mid-8,x1+10)]):
  if c not in which: continue
  for k in range(n):
    cr=im.crop((a0,int(y0+k*h)-14,a1,int(y0+(k+1)*h)+14)); cr=ImageOps.autocontrast(cr,cutoff=1)
    cr=cr.resize((620,int(cr.height*620/cr.width)),Image.LANCZOS)
    cr.save(f'/workspace/scotus/crops/c/B{i:02d}{c}{k}.png')
print(i,x0,x1,y0,y1,mid)
