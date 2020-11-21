import os
import numpy as np

from functools import lru_cache

a = np.zeros((5,5),dtype="uint32")
a[0,0] = 131
a[0,1] = 673
a[0,2] = 234
a[0,3] = 103
a[0,4] = 18 
a[1,0] = 201
a[1,1] = 96 
a[1,2] = 342
a[1,3] = 965
a[1,4] = 150
a[2,0] = 630
a[2,1] = 803
a[2,2] = 746
a[2,3] = 422
a[2,4] = 111
a[3,0] = 537
a[3,1] = 699
a[3,2] = 497
a[3,3] = 121
a[3,4] = 956
a[4,0] = 805
a[4,1] = 732
a[4,2] = 524
a[4,3] = 37
a[4,4] = 331

a = np.zeros((80,80),dtype="uint32")
for (i,line) in enumerate(open(os.getcwd()+"/pjeuler/input/81.txt")):
  for (j,val) in enumerate(str.split(line,sep=",")):
    a[i,j] = int(val)

@lru_cache(None)
def f(i,j):
  if i==0 and j==0:
    v = 0
  elif i==0:
    v = f(i,j-1)
  elif j==0:
    v = f(i-1,j)
  else:
    v = min(f(i-1,j),f(i,j-1))
  return v+a[i,j]