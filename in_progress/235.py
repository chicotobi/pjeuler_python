def u(k,r):
  return (900-3*k)*r**(k-1)

def s(r):
  return sum([u(k,r) for k in range(1,5001)]) + 600000000000

r1 = 1.001
r2 = 1.003

while r2-r1>1e-16:
  r = (r1+r2)/2
  if s(r)>0:
    r1 = r
  else:
    r2 = r
  print(r)
    