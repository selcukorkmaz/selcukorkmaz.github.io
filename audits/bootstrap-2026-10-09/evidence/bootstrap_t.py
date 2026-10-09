import numpy as np
prog=np.array([21,17,15,14,13,7,6,2,2,-3.]); usual=np.array([11,10,9,5,2,1,0,-1,-9,-9.])
rng=np.random.default_rng(2026)
for a in (prog, np.r_[45,prog[1:]]):
    D=a.mean()-usual.mean(); se=np.sqrt(a.var(ddof=1)/10+usual.var(ddof=1)/10)
    ts=[]
    for c in range(50):
        A=a[rng.integers(0,10,(200000,10))]; B=usual[rng.integers(0,10,(200000,10))]
        ts.append((A.mean(1)-B.mean(1)-D)/np.sqrt(A.var(1,ddof=1)/10+B.var(1,ddof=1)/10))
    ts=np.concatenate(ts); ql,qh=np.quantile(ts,[.025,.975])
    print("D",D,"se",round(se,4),"boot-t", round(D-qh*se,3), round(D-ql*se,3), "q", round(ql,3), round(qh,3))
