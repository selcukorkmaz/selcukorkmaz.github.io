from fractions import Fraction
from collections import Counter
from math import factorial
def comps(n,k):
    if k==1: yield (n,); return
    for i in range(n+1):
        for r in comps(n-i,k-1): yield (i,)+r
def meddist(x):
    vals=sorted(Counter(x).items()); v=[a for a,_ in vals]; w=[Fraction(c,len(x)) for _,c in vals]
    d=Counter()
    for c in comps(10,len(v)):
        pr=Fraction(factorial(10))
        for ci,wi in zip(c,w): pr=pr/factorial(ci)*wi**ci
        s=[]
        for vi,ci in zip(v,c): s+= [vi]*ci
        d[Fraction(s[4]+s[5],2)]+=pr
    assert sum(d.values())==1
    return d
p=[21,17,15,14,13,7,6,2,2,-3]; u=[11,10,9,5,2,1,0,-1,-9,-9]; p45=[45]+p[1:]
du=meddist(u)
for pp,lab in ((p,"T1"),(p45,"45")):
    dp=meddist(pp)
    dd=Counter()
    for a,ca in dp.items():
        for b,cb in du.items(): dd[a-b]+=ca*cb
    ks=sorted(dd); 
    mode=max(ks,key=lambda k:dd[k])
    import statistics
    print(lab,"obs median diff", statistics.median(pp)-statistics.median(u),"n values",len(ks),"mode",float(mode),float(dd[mode]))
    cum=0; lo=hi=None
    for k in ks:
        cum+=dd[k]
        if lo is None and cum>=Fraction(25,1000): lo=k; print("  cdf at lo",float(cum), "prev", float(cum-dd[k]))
        if hi is None and cum>=Fraction(975,1000): hi=k; print("  cdf at hi",float(cum),"prev",float(cum-dd[k]))
    print("  perc",float(lo),float(hi))
    top=sorted(ks,key=lambda k:-dd[k])[:4]; print("  top",[(float(k),round(float(dd[k]),4)) for k in top])
    mean=sum(k*c for k,c in dd.items()); sd=float(sum((k-mean)**2*c for k,c in dd.items()))**.5
    print("  mean",float(mean),"sd",sd)
