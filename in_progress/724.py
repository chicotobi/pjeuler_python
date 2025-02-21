def f(n,s,t):
  if t > 50:
    return 0
  if s == 0:
    return t/n
  v1 = s / n * f(n, s-1, t+1)
  v2 = (n-s) / n * f(n, s, t+1)
  return v1 + v2 + t/n

def f2(n,s,t):
  if s == 0:
    return t/n
  v1 = f2(n, s-1, t+1)
  v2 = (n-s) / s * (t+1) / n + t / s
  return v1 + v2

print(7/2        , f(  2,  2,0))
print(0 , f(  3,  3,0))
print(0 , f(  4,  4,0))
print(12019/720  , f(  5,  5,0))
#print(1427.193470, f(100,100,0))

print(7/2        , f2(  2,  2,0))
print(0        , f2(  3,  3,0))
print(0        , f2(  4,  4,0))
print(12019/720  , f2(  5,  5,0))

# s = 0
# for i in range(1,20):
#   p = 2**(-i)
#   v = (i+1) * (i+2) / 2
#   s += p * v
#   print(p,v,s)
