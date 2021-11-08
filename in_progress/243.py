import sympy

nmax = int(1e8)
minv = 1
for (i,phi) in enumerate(sympy.sieve.totientrange(1,nmax)):
  v = phi/max(i,1)
  if v < minv:
    print(i+1,v)
    minv = v
    if v<15499/94744:
      break