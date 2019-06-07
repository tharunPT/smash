p=input()
p=int(p)
q=[]
for j in range(0,p):
  n=input()
  q.append(n)
f=[]
for j in zip(*q):
  if j.count(j[0])==len(j):
    f.append(j[0])
  else:
    break
print(''.join(f))
  
