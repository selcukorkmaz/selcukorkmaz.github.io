import numpy as np
from scipy import stats
rng=np.random.default_rng(5); B=1999; R=3000
def draw(n): return 8*(rng.lognormal(0,1,n)-np.exp(.5))/np.sqrt((np.e-1)*np.e)
for n in (10,20):
    cov={'perc':0,'bc':0,'bca':0}; z0s=[]; accs=[]
    for r in range(R):
        a=draw(n); b=draw(n); D=a.mean()-b.mean()
        d=a[rng.integers(0,n,(B,n))].mean(1)-b[rng.integers(0,n,(B,n))].mean(1)
        z0=stats.norm.ppf(np.clip(np.mean(d<D),1e-6,1-1e-6)); L=np.r_[a-a.mean(),-(b-b.mean())]; acc=np.sum(L**3)/(6*np.sum(L**2)**1.5)
        z0s.append(z0); accs.append(acc)
        z=stats.norm.ppf([.025,.975])
        for k,(zz,aa) in {'perc':(0,0),'bc':(z0,0),'bca':(z0,acc)}.items():
            al=stats.norm.cdf(zz+(zz+z)/(1-aa*(zz+z))); lo,hi=np.quantile(d,al); cov[k]+=lo<=0<=hi
    print(n,{k:round(100*v/R,1) for k,v in cov.items()},'sd z0',round(np.std(z0s),3),'sd acc',round(np.std(accs),3),'mean|acc|',round(np.mean(np.abs(accs)),3))
