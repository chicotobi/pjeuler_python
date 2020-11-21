import os
import math
import numpy as np
from functools import lru_cache

if True:
  n = 80
  a = np.zeros((n,n),dtype="uint32")
  for (i,line) in enumerate(open(os.getcwd()+"/pjeuler/input/81.txt")):
    for (j,val) in enumerate(str.split(line,sep=",")):
      a[i,j] = int(val)
else:
  n = 5    
  a = np.zeros((n,n),dtype="uint32")
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

ncalls = 0

def is_circle(l1,l2,l3):
  return (l1=="up" and l2=="left" and l3=="down") or (l1=="down" and l2=="left" and l3=="up")

import inspect

stack0 = len(inspect.stack(0))

max_stack = 0
ncalls =0
@lru_cache(None)
def f(i,j,l1,l2):
  global ncalls
  ncalls +=1
  if j==0:
    return a[i,0]
  # up
  if i>0 and l1!="down" and not is_circle("up",l1,l2):
    v_up = f(i-1,j,"up",l1)
  else:
    v_up = math.inf
  # down
  if i<n-1 and l2!="up" and not is_circle("down",l1,l2):
    v_down = f(i+1,j,"down",l1)
  else:
    v_down = math.inf
  # left
  if j>0:
    v_left = f(i,j-1,"left",l1)
  else:
    v_left = math.inf
  result = a[i,j] + min(v_up,v_down,v_left)
  return result

for j in range(n):
  vv = math.inf
  for i in range(n):
    vv = min(vv,f(i,j,"left","left"))
print("vv:",vv)
print("ncalls:",ncalls)
  