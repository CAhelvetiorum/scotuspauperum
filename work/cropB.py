import sys
from PIL import Image, ImageOps
# usage: cropB.py leafnum x0 x1 y0 y1 n tag   (fractions)
i,x0,x1,y0,y1,n,tag=sys.argv[1:]
im=Image.open(f'/workspace/scotus/B/b-{int(i):04d}.jpg').convert('L')
W,H=im.size; x0,x1,y0,y1=[float(v) for v in (x0,x1,y0,y1)]; n=int(n)
h=(y1-y0)/n
for k in range(n):
    c=im.crop((int(x0*W),int((y0+k*h)*H)-10,int(x1*W),int((y0+(k+1)*h)*H)+10))
    c=ImageOps.autocontrast(c,cutoff=1)
    if c.width>1100: c=c.resize((1100,int(c.height*1100/c.width)))
    c.save(f'/workspace/scotus/crops/B{int(i):02d}{tag}_{k}.png')
