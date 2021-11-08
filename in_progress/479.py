import pjeuler.tools

mm = 1000000007

def S(n):
  s = 0
  for k in range(2,n+1):
    v = 1 - k**2
    v2 = v/k**2*(1 - v**n)
    s += v2
  return s

for n in range(2,10):
  print("S(",n,"):",S(n))