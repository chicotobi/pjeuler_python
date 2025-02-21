from math import sqrt, floor

def f(x):
  return x / (1 - x**2 - x)

def finv(n):
  return (sqrt(5*n*n+2*n+1)-n-1) / 2 / n 

idx = 0
i = 1
while idx < 16:
  v = 5*i*i+2*i+1
  if round(sqrt(v))**2 == v:
    idx += 1
    y = round(sqrt(v))
    print(idx, i, y/i)
    i *= 6.8
    i = floor(i)
  i += 1