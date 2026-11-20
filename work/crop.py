import sys
from PIL import Image, ImageOps
p=int(sys.argv[1]); x0,x1,y0,y1=map(float,sys.argv[2:6]); n=int(sys.argv[6])
im=Image.open(f'hi/p-{p:02d}.png').convert('L')
W,H=im.size
h=(y1-y0)/n
for k in range(n):
    a=y0+k*h-0.005; b=y0+(k+1)*h+0.005
    c=im.crop((int(x0*W),int(a*H),int(x1*W),int(b*H)))
    c=ImageOps.autocontrast(c,cutoff=1)
    c.save(f'crops/p{p:02d}_{k}.png')
print('done')
