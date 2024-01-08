x = 290797

import numpy as np
from scipy.spatial import cKDTree

def f(x):
    return (x*x)%50515093

p = []
n = 2000000
A = np.zeros((n,2))
for i in range(n):
    y = f(x)
    A[i,:] = [x,y]
    x = f(y)           

res = cKDTree(A).query_pairs(23)
idx1, idx2 = list(res)[0]

res = sqrt(sum((A[idx1,]-A[idx2,])**2))
