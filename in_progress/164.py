from functools import cache

maxn = 20

@cache
def f(x,y,n):
  if n == maxn:
    if x + y > 9:
      return 0
    else:
      return 10 - x - y
  if x + y > 9:
    return 0
  else:
    s = 0
    for z in range(10-x-y):
      s += f(y,z,n+1)
    return s
  
@cache
def f2(number,x,y,n):
  if n == maxn:
    if x + y > 9:
      return 0
    else:
      for i in range(10-x-y):
        print(10*number+i)
      return 10 - x - y
  if x + y > 9:
    return 0
  else:
    s = 0
    for z in range(10):
      s += f2(number*10+z,y,z,n+1)
    return s
  
ss = 0
for i in range(1,10):
  for j in range(10):
    res = f(i,j,3)
    #res = f2(10*i+j,i,j,3)
    ss += res
    #print(i,j,res)
print("all possibilities:",ss)