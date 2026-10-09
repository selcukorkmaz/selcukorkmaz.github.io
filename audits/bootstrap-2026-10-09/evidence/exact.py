from fractions import Fraction
from collections import Counter
import math
from scipy.stats import norm
def sumdist(x, n=10):
    d=Counter({0:1})
    for _ in range(n):
        nd=Counter()
        for s,c in d.items():
            for v in x: nd[s+v]+=c
        d=nd
    return d
def diffdist(p,u):
    dp=sumdist(p); du=sumdist(u)
    dd=Counter()
    for a,ca in dp.items():
        for b,cb in du.items(): dd[a-b]+=ca*cb   # sum difference; diff of means = /10
    return dd
def analyse(p,u,label):
    dd=diffdist(p,u); tot=sum(dd.values()); assert tot==10**20
    ks=sorted(dd)
    mean=sum(k*c for k,c in dd.items())/tot/10
    var=sum((k/10-mean)**2*c for k,c in dd.items())/tot
    print(label,"mean",mean,"SE",math.sqrt(var),"max",max(ks)/10,"min",min(ks)/10, "npoints",len(ks))
    cum=0; cdf=[]
    for k in ks: cum+=dd[k]; cdf.append((k,cum))
    def q_inv(a):  # smallest k with CDF>=a (type 1)
        for k,c in cdf:
            if c>=a*tot: return k/10
    def q_gt(a):  # smallest k with CDF > a
        for k,c in cdf:
            if c>a*tot: return k/10
    print(" perc type1", q_inv(.025), q_inv(.975), " (CDF>a)", q_gt(.025), q_gt(.975))
    th=round((sum(p)-sum(u)))  # obs sum diff
    below=sum(c for k,c in dd.items() if k<th); at=dd.get(th,0)
    z0=norm.ppf(below/tot); z0mid=norm.ppf((below+at/2)/tot)
    mp=sum(p)/len(p); mu=sum(u)/len(u)
    L=[x-mp for x in p]+[-(x-mu) for x in u]
    a=sum(l**3 for l in L)/(6*sum(l**2 for l in L)**1.5)
    print(" P(below)",below/tot,"P(at)",at/tot,"z0",z0,"z0mid",z0mid,"a",a)
    for zz,lab in ((z0,'strict'),(z0mid,'mid')):
        al=[norm.cdf(zz+(zz+z)/(1-a*(zz+z))) for z in (norm.ppf(.025),norm.ppf(.975))]
        print(" BCa",lab,"alphas",al,"interval",q_inv(al[0]),q_inv(al[1]))
    return dd
p=[21,17,15,14,13,7,6,2,2,-3]; u=[11,10,9,5,2,1,0,-1,-9,-9]
analyse(p,u,"T1")
p45=[45]+p[1:]
analyse(p45,u,"45")
# copies of 45
from math import comb
pr=[comb(10,k)*0.1**k*0.9**(10-k) for k in range(11)]
print("P(0)",pr[0],"P(1)",pr[1],"P(>=2)",1-pr[0]-pr[1])
print("per copy (45-mean of other 9)/10", (45-sum(p45[1:])/9)/10, "45-21/10", 24/10, "(45-xbar)/10", (45-sum(p45)/10)/10)

def bca_conv(p,u):
    dd=diffdist(p,u); tot=sum(dd.values()); ks=sorted(dd); th=sum(p)-sum(u)
    below=sum(c for k,c in dd.items() if k<th); at=dd.get(th,0)
    mp=sum(p)/10; mu=sum(u)/10; L=[x-mp for x in p]+[-(x-mu) for x in u]; a=sum(l**3 for l in L)/(6*sum(l**2 for l in L)**1.5)
    cum=0; cdf=[]
    for k in ks: cum+=dd[k]; cdf.append((k,cum))
    q=lambda al: next(k for k,c in cdf if c>=al*tot)/10
    for lab,share in (('strict',below),('mid',below+at/2),('le',below+at)):
        z0=norm.ppf(share/tot); al=[norm.cdf(z0+(z0+z)/(1-a*(z0+z))) for z in (norm.ppf(.025),norm.ppf(.975))]
        print('  ',lab, round(z0,4), q(al[0]), q(al[1]))
print("T1"); bca_conv(p,u); print("45"); bca_conv(p45,u)
