from math import floor
from itertools import permutations


def print_perm(p):
    s = ['in a'+str(v+4) for v in p]
    s = ['in a3'] + s
    print(s)

a3 = []
a4 = []
a5 = []
a6 = []
a7 = []
a8 = []

for n in range(200):
    val = int(n*(n+1)/2)
    if 1000<=val and val<10000:
        a3.append(val)
    val = n*n
    if 1000<=val and val<10000:
        a4.append(val)
    val = int(n*(3*n-1)/2)
    if 1000<=val and val<10000:
        a5.append(val)
    val = n*(2*n-1)
    if 1000<=val and val<10000:
        a6.append(val)
    val = int(n*(5*n-3)/2)
    if 1000<=val and val<10000:
        a7.append(val)
    val = n*(3*n-2)
    if 1000<=val and val<10000:
        a8.append(val)

a = [a4,a5,a6,a7,a8]

for p in permutations(range(5)):
    for n1 in a3:
        r1 = n1 % 100
        for n2 in a[p[0]]:
            if floor(n2*0.01)==r1:
                r2 = n2 % 100
                for n3 in a[p[1]]:
                    if floor(n3*0.01)==r2:
                        r3 = n3 % 100
                        for n4 in a[p[2]]:
                            if floor(n4*0.01)==r3:
                                r4 = n4 % 100
                                for n5 in a[p[3]]:
                                    if floor(n5*0.01)==r4:
                                        r5 = n5 % 100
                                        for n6 in a[p[4]]:
                                            if floor(n6*0.01)==r5:
                                                r6 = n6 % 100
                                                if floor(n1*0.01)==r6:
                                                    print_perm(p)
                                                    print(n1,n2,n3,n4,n5,n6)
                                                    print(n1+n2+n3+n4+n5+n6)

