from itertools import combinations
t,p=map(int,input().split())
r=len(str(t))
u=list(combinations(str(t),r-p))
u=(sorted(u))
j="".join(u[0])
print(j)
