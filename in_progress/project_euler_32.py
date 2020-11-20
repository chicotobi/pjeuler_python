import itertools
import numpy as np

vals = []

counter = 0
for a in itertools.permutations('123456789',9):
    b = ''.join(a)
    for i in range(1,9):
        for j in range(i+1,9):
            m1 = int(b[0:i])
            m2 = int(b[i:j])
            res = int(b[j:])
            if(m1*m2==res):
                print(m1,m2,res)
                vals.append(res)

print(vals)
vals.sort()
print(vals)
vals = np.unique(vals)
print(vals)
print(np.sum(vals))