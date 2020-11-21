import numpy as np
import math
import functools
import string
digs = string.digits + string.ascii_letters

def primes(limit):
    a = [True] * (limit+1)
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit+1, i):
                a[n] = False
                
def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    adigits = []

    while x:
        adigits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        adigits.append('-')

    adigits.reverse()

    return ''.join(adigits)
 
def fib(n):
  arr = [1,1]
  for i in range(n-2):
    arr = arr+[arr[-2]+arr[-1]]
  return arr[0:n]

def small_s(n):
  if n<10:
    return n
  x = n//9
  return (n%9)*10**x+int("9"*x)

def big_s(k):
  x = 0
  for i in range(1,k+1):
    x += small_s(i)
  return x

def digits(s):
    return [int(a) for a in s]
  
def smart_mod(base,exp,mod):
  if exp==0:
    return 1
  b = digits(int2base(exp,2)[::-1])

  a = [base%mod]
  for i in range(len(b)-1):
    a.append((a[-1]**2)%mod)
  
  v = np.array(a)[np.array(b)==1]
  w = functools.reduce(lambda x,y:smart_mod_prod(x,y,mod),v)
  return w

q = 1000000007

def factors(m):
  if m<1:
    return []
  if m==1:
    return [1]
  n = math.floor(m**.5)
  f = []
  for p in primes(n):
    while m % p == 0:
        m /= p
        f.append(p)
    if(m==1):
      break
  if m != 1:
      f.append(int(m))
  return f

def smart_mod_prod(x,y,mod):
  v = [x]+factors(y)
  return functools.reduce(lambda x,y:x*y%mod,v)

def big_s_2(k):
  v = int((k%9+1)*(k%9+2)/2 + 5) 
  #v = v*10**(k//9)
  v = smart_mod_prod(v,smart_mod(10,k//9,q),q)
  return (v - 6 - k%q)%q

fs = fib(90)[1:]

s = 0
for i in fs:
  s += big_s_2(i)
s = s%q
print(s)