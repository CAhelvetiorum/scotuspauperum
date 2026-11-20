import sys,re,glob
files=sys.argv[1]; pats=sys.argv[2:]
txt="".join(open(f).read() for f in sorted(glob.glob(files)))
for p in pats:
    print("==",p)
    for m in list(re.finditer(p,txt,re.I))[:3]:
        ns=re.findall(r"\[n(\d+)\]",txt[:m.start()])
        print("  n.",ns[-1] if ns else "?", "|", txt[max(0,m.start()-90):m.end()+60].replace("\n"," "))
