n = 21
m = 15

n = 120
m = 85

def test(n,m):
  return 2*m*(m-1)-n*(n-1)

def f(n):
  return .5*(1+(1+2*n*(n-1))**.5)

a = 1000000000000
for n in range(a,a+100000000):
  m = round(f(n))
  if test(n,m)==0:
    print(n,m)
    
    
e = 27830457