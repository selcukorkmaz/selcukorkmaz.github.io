import numpy as np, sys
from scipy import stats
rng=np.random.default_rng(int(sys.argv[2])); B=1999; R=int(sys.argv[3])
pop=sys.argv[1]
def draw(n,size):
    if pop=="normal": return rng.normal(0,8,(size,n))
    if pop=="exp": return 8*(rng.exponential(1,(size,n))-1)
    if pop=="lognorm":
        s=1.0; m=np.exp(s*s/2); sd=np.sqrt((np.exp(s*s)-1)*np.exp(s*s)); return 8*(rng.lognormal(0,s,(size,n))-m)/sd
res={}
for n in (5,10,20,40):
    cov={k:0 for k in ["t","welch","perc","bca","boott"]}; width={k:0.0 for k in cov}
    for r in range(R):
        a=draw(n,1)[0]; b=draw(n,1)[0]
        D=a.mean()-b.mean(); se=np.sqrt(a.var(ddof=1)/n+b.var(ddof=1)/n)
        tq=stats.t.ppf(.975,2*n-2); lo,hi=D-tq*se,D+tq*se; cov["t"]+=lo<=0<=hi; width["t"]+=hi-lo
        v1,v2=a.var(ddof=1)/n,b.var(ddof=1)/n; df=(v1+v2)**2/(v1**2/(n-1)+v2**2/(n-1)); wq=stats.t.ppf(.975,df)
        lo,hi=D-wq*se,D+wq*se; cov["welch"]+=lo<=0<=hi; width["welch"]+=hi-lo
        A=a[rng.integers(0,n,(B,n))]; Bb=b[rng.integers(0,n,(B,n))]
        d=A.mean(1)-Bb.mean(1)
        lo,hi=np.quantile(d,[.025,.975]); cov["perc"]+=lo<=0<=hi; width["perc"]+=hi-lo
        z0=stats.norm.ppf(np.clip(np.mean(d<D),1e-6,1-1e-6))
        L=np.concatenate([a-a.mean(), -(b-b.mean())]); acc=np.sum(L**3)/(6*np.sum(L**2)**1.5)
        al=[]
        for z in (stats.norm.ppf(.025),stats.norm.ppf(.975)):
            al.append(stats.norm.cdf(z0+(z0+z)/(1-acc*(z0+z))))
        lo,hi=np.quantile(d,al); cov["bca"]+=lo<=0<=hi; width["bca"]+=hi-lo
        ses=np.sqrt(A.var(1,ddof=1)/n+Bb.var(1,ddof=1)/n)
        with np.errstate(divide='ignore',invalid='ignore'):
            ts=(d-D)/ses
        ts=np.where(ses>0,ts,np.sign(d-D)*np.inf); ts=np.nan_to_num(ts,nan=0.0)
        ql,qh=np.quantile(ts,[.025,.975]); lo,hi=D-qh*se,D-ql*se; cov["boott"]+=lo<=0<=hi; width["boott"]+=hi-lo
    import json; print(json.dumps({"pop":pop,"n":n,"R":R,"cov":{k:int(v) for k,v in cov.items()},"wsum":{k:float(v) for k,v in width.items()}}),flush=True)
