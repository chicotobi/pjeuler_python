from math import gcd, prod
from sympy import primefactors

hits = 0
ssum = 0
for c in range(120000):
  maxa = c//2
  for a in range(1,maxa+1):
    b = c-a
    if gcd(a,b) == 1 and gcd(a,c) == 1 and gcd(b,c) == 1:
      fa = primefactors(a)
      fb = primefactors(b)
      fc = primefactors(c)
      v = prod(set(fa+fb+fc))
      if v < c:
        print(a,b,c)
        ssum += c
        #break
print(ssum)