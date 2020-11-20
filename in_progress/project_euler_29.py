import numpy as np
v = []
for a in range(2,101):
    for b in range(2,101):
        v.append(a**b)
print(len(np.unique(v)))