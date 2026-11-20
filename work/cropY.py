import sys, numpy as np
from PIL import Image, ImageOps
# cropY.py leaf [n]: find the two text columns as the two widest dense runs -> /tmp/Y{leaf}{L|R}{k}.png
leaf=int(sys.argv[1]); n=int(sys.argv[2]) if len(sys.argv)>2 else 2
im=Image.open(f'/workspace/scotus/B/b-{leaf:04d}.jpg').convert('L');W,H=im.size
a=np.asarray(ImageOps.autocontrast(im.resize((W//4,H//4)),cutoff=1)).astype(float); h,w=a.shape; d=a<100
cols=d[int(.2*h):int(.8*h)].mean(0); cols=np.convolve(cols,np.ones(9)/9,'same')
on=cols>0.10; runs=[];i=0
while i<w:
  if on[i]:
    j=i
    while j<w and on[j]: j+=1
    runs.append((j-i,i,j)); i=j
  else: i+=1
runs=sorted(sorted(runs)[-2:],key=lambda r:r[1])
out=[]
for side,(_,c0,c1) in zip('LR',runs):
  c0,c1=4*c0-25,4*c1+25
  rows=d[:,c0//4:c1//4].mean(1); ys=np.where(rows>0.05)[0]; ys=ys[(ys>0.03*h)&(ys<0.97*h)]
  y0,y1=4*ys.min(),4*ys.max()
  for k in range(n):
    t0=y0+k*(y1-y0)/n-35; t1=y0+(k+1)*(y1-y0)/n+35
    cr=im.crop((max(0,c0),int(max(0,t0)),min(W,c1),int(min(H,t1))));cr=ImageOps.autocontrast(cr,cutoff=1)
    cr=cr.resize((720,int(cr.height*720/cr.width)));cr.save(f'/tmp/Y{leaf}{side}{k}.png')
  out.append((side,c0,c1,y0,y1))
print(leaf,out)
