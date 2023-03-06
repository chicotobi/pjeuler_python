# n = 21
# m = 15

# n = 120
# m = 85

# def test(n,m):
#   return 2*m*(m-1)-n*(n-1)

# def f(n):
#   return .5*(1+(1+2*n*(n-1))**.5)

# a = 1000000000000
# for n in range(a,a+100000000):
#   m = round(f(n))
#   if test(n,m)==0:
#     print(n,m)

# e = 27830457

from sympy import gcd

nmax = 35

def frsum(a,b,c,d):
  return (a*d+b*c, b*d)

def simplify(nom, den):
  t = gcd(nom,den)
  nom /= t
  den /= t
  return nom, den

# For a best estimate
s_starting_with = {}
for i in range(2,nmax+1):
  nom = 0
  den = 1
  for j in range(i,nmax+1):
    nom, den = frsum(nom, den, 1, j**2)
    nom, den = simplify(nom, den)
  s_starting_with[i] = (nom, den)

def f(nom, den, l, n0):
  nom, den = simplify(nom, den)
  if n0 < 15:
    print('.'*n0, l)
  if n0 < nmax:
    tmpnom, tmpden = frsum(nom, den, s_starting_with[n0+1][0], s_starting_with[n0+1][1])
    if 2 * tmpnom >= tmpden:
      f(nom, den, l, n0+1)
  nom, den = frsum(nom, den, 1, n0**2)
  if 2 * nom == den:
    print("Success:",l)
  elif 2 * nom < den and n0 < nmax:
    f(nom, den, l+[n0], n0+1)
  return

nom = 1
den = 4
l = [2]
n0 = 3
f(nom, den, l, n0)