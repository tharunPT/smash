q12,q22=input().split()
m=0
if len(q12)>len(q22):
   q12,q22=q22,q12
t=0
while t<len(q12):
    m+=(ord(q22[t])-ord(q12[t]))
    t+=1
for t in range(t,len(q22)):
    m+=ord(q22[t])-ord('a')+1
print(m)
