import sympy

m = 100

dct = {}
for a in range(1,m+1):
  for b in range(1,m+1):
    v = .25
    if a>1:
      v += (a-1) * .5
    if b>1:
      v += (b-1) * .5
    if a>1 and b>1:
      v += .5 * ( (a-1)*(b-1) - sympy.gcd(a,b) + 1)
    dct[(a,b)] = v
    dct[(b,a)] = v

s = 0
for a in range(1,m+1):
  print(a)
  for b in range(1,m+1):
    for c in range(1,m+1):
      for d in range(1,m+1):
        v = dct[(a,b)] + dct[(b,c)] + dct[(c,d)] +dct[(d,a)]
        if round(v**.5)**2 == round(v):
          s += 1
          #print(a,b,c,d,v)
print(s)