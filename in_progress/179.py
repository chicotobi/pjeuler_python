n = int(1e7)
l = [0]*n
s = 0
for i in range(1,n):
  for j in range(i,n,i):
    l[j] += 1
  if l[i]==l[i-1]:
    s += 1