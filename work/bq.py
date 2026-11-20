import sys, numpy as np, os
from PIL import Image, ImageOps
# bq.py leaf col(L/R) [n=3]: B column crops with generous overlap -> crops/q/B{leaf}{col}{k}.png
i=int(sys.argv[1]); col=sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 2; WW=int(sys.argv[4]) if len(sys.argv)>4 else 470
im=Image.open(f'/workspace/scotus/B/b-{i:04d}.jpg').convert('L')
a=np.asarray(ImageOps.autocontrast(im.resize((im.width//4,im.height//4)),cutoff=1)).astype(float)
H,W=a.shape; d=a<100
cols=d[int(.15*H):int(.85*H)].mean(0)
txt=(cols>0.06)&(cols<0.5)
sm=np.convolve(txt.astype(float),np.ones(9)/9,'same')>0.5
xs=np.where(sm)[0]; xs=xs[(xs>0.03*W)&(xs<0.97*W)]
# runs
runs=[];s=xs[0];p=xs[0]
for x in xs[1:]:
    if x>p+3: runs.append((s,p)); s=x
    p=x
runs.append((s,p)); runs=[r for r in runs if r[1]-r[0]>0.15*W]
L,R=runs[0],runs[-1]
if len(runs)<2: mid=(L[0]+L[1])//2; L=(L[0],mid); R=(mid,L[1])
sel=L if col=='L' else R
x0,x1=4*sel[0]-14,4*sel[1]+14
rows=d[:,sel[0]:sel[1]].mean(1); ys=np.where(rows>0.04)[0]; ys=ys[(ys>0.03*H)&(ys<0.97*H)]
y0,y1=4*ys.min(),4*ys.max()
h=(y1-y0)/n
os.makedirs('/workspace/scotus/crops/q',exist_ok=True)
for k in range(n):
    cr=im.crop((x0,max(0,int(y0+k*h)-45),x1,min(im.height,int(y0+(k+1)*h)+45))); cr=ImageOps.autocontrast(cr,cutoff=1)
    cr=cr.resize((WW,int(cr.height*WW/cr.width)),Image.LANCZOS)
    cr.save(f'/workspace/scotus/crops/q/B{i:02d}{col}{k}.png')
print(i,col,x0,x1,y0,y1,runs,cr.size)
