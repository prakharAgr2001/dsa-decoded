"""Every example + dry-run trace used in Season 1 reels, computed (not typed). Run: python3 notes/traces/compute.py"""
import math, itertools
def P(*a): print(*a)
pairs = lambda n: n*(n-1)//2
P('E03 anagrams', {w: ''.join(sorted(w)) for w in ['pat','tap','art','rat','apt','tar']}, 'pairs10k', pairs(10000))
s = {8,4,200,7,5,6,1}; best=0; tr=[]
for x in [8,4,200,7,5,6,1]:
    if x-1 in s: tr.append((x,'no','-')); continue
    y=x
    while y+1 in s: y+=1
    best=max(best,y-x+1); tr.append((x,'yes',y-x+1))
P('E04 LCS', tr, 'best', best, 'n*n 5000', 5000*5000)
c=None; k=0; tr=[]
for x in [3,1,3,3,2,3,1]:
    if k==0: c=x
    k += 1 if x==c else -1; tr.append((x,c,k))
P('E05 majority', tr)
mn=10**9; best=0; tr=[]
for i,p in enumerate([9,4,7,2,8,5]):
    mn=min(mn,p); best=max(best,p-mn); tr.append((i,p,mn,p-mn,best))
P('E06 stock', tr, pairs(5000))
cur=best=None; tr=[]; st=0
for i,x in enumerate([2,-4,3,-1,4,-6,2]):
    if cur is None or x>cur+x: cur=x; st=i
    else: cur+=x
    best=cur if best is None else max(best,cur); tr.append((i,x,cur,best,st))
P('E07 kadane', tr, 'subarrays', 5000*5001//2)
a=[2,3,4,5]; L=[1]*4; R=[1]*4
for i in range(1,4): L[i]=L[i-1]*a[i-1]
for i in range(2,-1,-1): R[i]=R[i+1]*a[i+1]
P('E08 product', L, R, [L[i]*R[i] for i in range(4)], 5000*4999)
a=[0,3,0,5,7]; w=0; tr=[]
for i in range(len(a)):
    if a[i]: a[w],a[i]=a[i],a[w]; tr.append((i,'swap',w,a[:])); w+=1
    else: tr.append((i,'skip',w,a[:]))
P('E09 move zeroes', tr)
t='topspot'; l,r=0,len(t)-1; tr=[]
while l<r: tr.append((l,r,t[l],t[r],t[l]==t[r])); l+=1; r-=1
P('E10 palindrome', tr)
a=[1,3,4,6,8,11]; l,r=0,5; tr=[]
while l<r:
    s_=a[l]+a[r]; tr.append((l,r,s_)); 
    if s_==10: break
    if s_<10: l+=1
    else: r-=1
P('E11 two sum II', tr)
a=[1,1,2,3,3,3,4]; slow=0; tr=[]
for f in range(1,len(a)):
    if a[f]!=a[slow]: slow+=1; a[slow]=a[f]; tr.append((f,'new',slow,a[:]))
    else: tr.append((f,'dup',slow,a[:]))
P('E12 remove dups k=',slow+1, tr)
a=[1,2,0,2,0,1]; lo=mid=0; hi=5; tr=[]
while mid<=hi:
    if a[mid]==0: a[lo],a[mid]=a[mid],a[lo]; tr.append(('0 swap lo',lo,mid,hi,a[:])); lo+=1; mid+=1
    elif a[mid]==1: tr.append(('1 skip',lo,mid,hi,a[:])); mid+=1
    else: a[mid],a[hi]=a[hi],a[mid]; tr.append(('2 swap hi',lo,mid,hi,a[:])); hi-=1
P('E13 sort colors', tr)
h=[3,7,2,6,4,8]; l,r=0,5; best=0; tr=[]
while l<r:
    ar=(r-l)*min(h[l],h[r]); best=max(best,ar); tr.append((l,r,r-l,min(h[l],h[r]),ar,best))
    if h[l]<h[r]: l+=1
    else: r-=1
P('E14 container', tr, 'brute', max((j-i)*min(h[i],h[j]) for i in range(6) for j in range(i+1,6)))
a=[-5,-2,0,1,3,4]; tr=[]
for i in range(len(a)-2):
    l,r=i+1,len(a)-1
    while l<r:
        s_=a[i]+a[l]+a[r]; tr.append((i,l,r,s_))
        if s_==0: l+=1; r-=1
        elif s_<0: l+=1
        else: r-=1
P('E15 3sum', tr, 'triples5000', 5000*4999*4998//6, [c for c in itertools.combinations(a,3) if sum(c)==0])
a=[4,2,7,1,8,3]; k=3; s_=sum(a[:3]); tr=[(0,2,s_)]
for r in range(3,6): s_+=a[r]-a[r-3]; tr.append((r-2,r,s_))
P('E17 window', tr, max(x[2] for x in tr)/3)
t='chaichai'; last={}; l=0; best=0; tr=[]
for r,c in enumerate(t):
    if c in last and last[c]>=l: l=last[c]+1
    last[c]=r; best=max(best,r-l+1); tr.append((r,c,l,r-l+1,best))
P('E18 substring', tr)
a=[2,3,1,4,5,2]; T=9; l=0; s_=0; best=99; tr=[]
for r in range(6):
    s_+=a[r]; tr.append(('add',l,r,s_))
    while s_>=T: best=min(best,r-l+1); tr.append(('hit',l,r,s_,r-l+1)); s_-=a[l]; l+=1; tr.append(('drop',l,r,s_))
P('E19 min size', tr, best)
a=[3,1,4,1,5,9]; pre=[0]
for x in a: pre.append(pre[-1]+x)
P('E20 prefix', pre, pre[5]-pre[1], sum(a[1:5]), 10000*5000)
a=[1,2,1,2,1]; K=3; cnt={0:1}; p=0; tot=0; tr=[]
for x in a: p+=x; add=cnt.get(p-K,0); tot+=add; cnt[p]=cnt.get(p,0)+1; tr.append((x,p,p-K,add,tot))
P('E21 subarray sum k', tr, sum(1 for i in range(5) for j in range(i,5) if sum(a[i:j+1])==3))
a=[2,5,8,12,16,23,38,56]; lo,hi=0,7; tr=[]
while lo<=hi:
    m=(lo+hi)//2; tr.append((lo,hi,m,a[m]))
    if a[m]==16: break
    if a[m]<16: lo=m+1
    else: hi=m-1
P('E22 binary', tr, math.ceil(math.log2(5001)), math.ceil(math.log2(1000001)))
a=[5,7,7,8,8,8,10]
def bs(first):
    lo,hi=0,6; ans=-1; tr=[]
    while lo<=hi:
        m=(lo+hi)//2; tr.append((lo,hi,m,a[m]))
        if a[m]==8: ans=m; (hi:=m-1) if first else (lo:=m+1)
        elif a[m]<8: lo=m+1
        else: hi=m-1
    return ans,tr
P('E23 first/last', bs(True), bs(False))
a=[1,3,5,4,2,6,1]; lo,hi=0,6; tr=[]
while lo<hi:
    m=(lo+hi)//2; tr.append((lo,hi,m,a[m],a[m+1]))
    if a[m]>a[m+1]: hi=m
    else: lo=m+1
P('E24 peak', tr, lo)
a=[15,18,22,3,6,9,12]; lo,hi=0,6; tr=[]
while lo<=hi:
    m=(lo+hi)//2; tr.append((lo,hi,m,a[m]))
    if a[m]==6: break
    if a[lo]<=a[m]:
        if a[lo]<=6<a[m]: hi=m-1
        else: lo=m+1
    else:
        if a[m]<6<=a[hi]: lo=m+1
        else: hi=m-1
P('E25 rotated', tr)
pl=[4,9,6,12]; H=8; hrs=lambda k: sum(math.ceil(p/k) for p in pl); lo,hi=1,12; tr=[]
while lo<hi:
    m=(lo+hi)//2; tr.append((lo,hi,m,hrs(m)))
    if hrs(m)<=H: hi=m
    else: lo=m+1
P('E26 koko', tr, lo, [(k,hrs(k)) for k in range(1,13)])
s='([]){}'; st=[]; tr=[]
for ch in s:
    if ch in '([{': st.append(ch); tr.append((ch,'push',''.join(st)))
    else: o=st.pop(); tr.append((ch,'pop '+o,''.join(st)))
P('E27 parens', tr)
a=[4,2,6,1,3]; ans=[-1]*5; st=[]; tr=[]
for i,x in enumerate(a):
    while st and a[st[-1]]<x: j=st.pop(); ans[j]=x; tr.append(('pop',j,x))
    st.append(i); tr.append(('push',i,[a[k] for k in st]))
P('E29 NGE', ans, tr)
a=[30,34,31,33,36,32]; ans=[0]*6; st=[]; tr=[]
for i,x in enumerate(a):
    while st and a[st[-1]]<x: j=st.pop(); ans[j]=i-j; tr.append(('pop',j,i-j))
    st.append(i); tr.append(('push',i,[a[k] for k in st]))
P('E30 temps', ans, tr)
