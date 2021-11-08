import functools

@functools.lru_cache(None)
def nim(a,b,c):
  if a==0 and b==0 and c!=0:
    return 1
  if a==0 and b!=0 and c==0:
    return 1
  if a!=0 and b==0 and c==0:
    return 1
  if a==0 and b==c:
    return 0
  if b==0 and a==c:
    return 0
  if c==0 and a==b:
    return 0
  for a2 in range(a):
    if not nim(a2,b,c):
      return 1
  for b2 in range(b):
    if not nim(a,b2,c):
      return 1
  for c2 in range(c):
    if not nim(a,b,c2):
      return 1
  return 0
  

for i in range(1,51):
  a = i
  b = 2*i
  c = 3*i
  if not nim(a,b,c):
    print("nim(",a,",",b,",",c,") is zero.")


def A003714(n):

  tlist, s = [1, 2], 0
  
  while tlist[-1]+tlist[-2] <= n:
  
      tlist.append(tlist[-1]+tlist[-2])
  
  for d in tlist[::-1]:
  
      s *= 2
  
      if d <= n:
  
          s += 1
  
          n -= d
  
  return s # Chai Wah Wu, Jun 14 2018

i = 1
while True:
  if A003714(i) >= 2**30:
    break
  i+=1 