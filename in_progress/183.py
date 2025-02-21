from math import log, exp, floor
from sympy import factorint, gcd

def f(N,k):
  return (N/k)**k

def flog(N,k):
  return k * log(N/k)


def Df(N,k):
  return (N/k)**k * ( log(N/k) - 1)

def maximize(N):
  k1 = floor(N/exp(1))
  k2 = k1 + 1
  
  f1 = flog(N, k1)
  f2 = flog(N, k2)
  
  if f1 > f2:
    return k1
  else:
    return k2
  
s = 0
Nmax = 10000
for N in range(5,Nmax+1):
  sol = maximize(N)
  
  rem = sol // gcd(N, sol)
  
  tmp = set(factorint(rem).keys())
  
  if tmp.issubset(set([2,5])):
    s -= N
  else:
    s += N
  
  print(N,sol,s)