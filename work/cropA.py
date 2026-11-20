import sys
from PIL import Image, ImageOps
# usage: cropA.py page x0 x1 y0 y1 n tag  (fractions; page 1-based; native 150dpi image, upscaled x2 Lanczos)
p,x0,x1,y0,y1,n,tag=sys.argv[1:]
im=Image.open(f'/workspace/scotus/native/a-{int(p)-1:03d}.png').convert('L')
W,H=im.size; x0,x1,y0,y1=[float(v) for v in (x0,x1,y0,y1)]; n=int(n)
h=(y1-y0)/n
for k in range(n):
    c=im.crop((int(x0*W),max(0,int((y0+k*h)*H)-6),int(x1*W),int((y0+(k+1)*h)*H)+6))
    c=ImageOps.autocontrast(c,cutoff=1)
    c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
    c.save(f'/workspace/scotus/crops/A{int(p):02d}{tag}_{k}.png')
