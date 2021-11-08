l = []
ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ps = [i**2 for i in ps]

v = 51

import math
import numpy as np
from scipy.special import binom

for n in range(v):
  for k in range(math.ceil(n/2)+1):
    x = round(binom(n,k))
    print(n,k,x)
    squarefree =  True
    for p in ps:
      if x % p == 0:
        squarefree = False
    if squarefree:
      l.append(x)

print(sum(np.unique(l)))