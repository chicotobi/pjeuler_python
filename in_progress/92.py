
import sys
import functools
sys.path.append('./pjeuler/')
from tools import *

def digits_int(x):
  l = []
  while x>9:
    l.append(x%10)
    x = x//10
  l.append(x)
  l.reverse()
  return l

def f(x):
  import numpy as np
  return sum(np.array(digits_int(x))**2)

def pjeuler92():
  n = 10000000
  l = [0]*(n+1)
  l[1]=1
  l[89]=2
  for i in range(2,n+1):
    v = i
    while True:
      if v < n+1 and l[v]!=0:
        l[i]=l[v]
        break
      v = f(v)
  return sum(np.array(l)==2)

print(pjeuler92())