from functools import cache

def pos(l):
  return 2**len(list(i for i in l if i==1))

@cache
def partition(k,n):
  if n==1:
    if 0<=k and k<=2:
      return [[k]]
    else:
      return []
    
  # Last is zero
  tmp = partition(k,n-1)
  if len(tmp)>0:
    pars_0 = [i+[0] for i in tmp]
  else:
    pars_0 = []
  
  # Last is one
  tmp = partition(k-1,n-1)
  if len(tmp)>0:
    pars_1 = [i+[1] for i in tmp]
  else:
    pars_1 = []
    
  # Last is two
  tmp = partition(k-2,n-1)
  if len(tmp)>0:
    pars_2 = [i+[2] for i in tmp]
  else:
    pars_2 = []
  
  return pars_0+pars_1+pars_2  

@cache
def combs(k,n):
  if k==n:
    return partition(n,n)
  cmbs = combs(k,n-1)
  return [c+[c[-k]] for c in cmbs]
  
def a(k,n):
  return sum(pos(i) for i in combs(k,n))

# for n in range(1,20):
#   print()
#   for k in range(1,n+1):
#     print("k=",k,"n=",n,"a(k,n)=",a(k,n))    
    
for i in range(2,11):
  k = 2
  n = i
  print("k=",k,"n=",n,"a(k,n)=",a(k,n))    