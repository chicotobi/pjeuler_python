import math
from fractions import Fraction as f

di = {1:[f(60,1)]}

nmax = 18
possible = set(di[1])
print(1,len(possible))
for n in range(2,nmax+1):
    di[n] = []
    for n1 in range(1,math.floor(n/2)+1):
        n2 = n - n1
        for el1 in di[n1]:
            for el2 in di[n2]:
                v1 = el1 + el2
                v2 = f(1,f(1,el1)+f(1,el2))
                di[n] += [v1]
                di[n] += [v2]
    s = set(di[n])
    di[n] = list(s)
    di[n] = [el for el in di[n] if el not in possible]    
    possible = possible.union(s)
    print(n,len(possible))