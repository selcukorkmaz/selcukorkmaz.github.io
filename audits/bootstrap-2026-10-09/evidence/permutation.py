import numpy as np, itertools
u=np.array([11,10,9,5,2,1,0,-1,-9,-9.])
for p in (np.array([21,17,15,14,13,7,6,2,2,-3.]), np.array([45,17,15,14,13,7,6,2,2,-3.])):
    z=np.concatenate([p,u]); isp=np.r_[np.ones(10),np.zeros(10)]
    C=np.array(list(itertools.combinations(range(20),10)))
    S0=z[C].sum(1); K=isp[C].sum(1)
    d=p.mean()-u.mean()
    def pval(delta):
        tot=z.sum()-10*delta; S=S0-delta*K
        T=(2*S-tot)/10; Tobs=d-delta
        return np.mean(np.abs(T)>=abs(Tobs)-1e-9)
    grid=np.round(np.arange(-3,26,0.001),3)
    acc=[g for g in grid if pval(g)>0.05] if False else None
    # coarse then refine
    g=np.arange(-3,26,0.05); pv=np.array([pval(x) for x in g]); A=g[pv>0.05]
    print("contiguous", bool(np.all(pv[(g>=A.min())&(g<=A.max())]>0.05))); print(len(C), "coarse", A.min(), A.max(), "p at 0:",pval(0.0))
    def edge(a,b):  # a inside? find boundary
        for _ in range(40):
            m=(a+b)/2
            if (pval(m)>0.05)==(pval(a)>0.05): a=m
            else: b=m
        return (a+b)/2
    print("  lower edge", edge(A.min(),A.min()-0.05), "upper edge", edge(A.max(),A.max()+0.05))
