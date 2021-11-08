tri = [(i+1)*(i+2)//2 for i in range(12345)]

def H(n):
  x = 0
  m = 1
  n -= 3
  while n>=0:
    x += tri[n] * m
    m += 1
    n -= 3
  return x

s = sum(H(i) for i in range(3,12346))