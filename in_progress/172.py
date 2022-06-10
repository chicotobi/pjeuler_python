import functools

@functools.lru_cache(None)
def calc(n0,n1,n2,n3,n4,n5,n6,n7,n8,n9):
    if n0+n1+n2+n3+n4+n5+n6+n7+n8+n9==1:
        if n0==0:
            return 1
        else:
            return 0
    s = 0
    if n0>0:
        s += calc(n0-1,n1,n2,n3,n4,n5,n6,n7,n8,n9)
    if n1>0:
        s += calc(n0,n1-1,n2,n3,n4,n5,n6,n7,n8,n9)
    if n2>0:
        s += calc(n0,n1,n2-1,n3,n4,n5,n6,n7,n8,n9)
    if n3>0:
        s += calc(n0,n1,n2,n3-1,n4,n5,n6,n7,n8,n9)
    if n4>0:
        s += calc(n0,n1,n2,n3,n4-1,n5,n6,n7,n8,n9)
    if n5>0:
        s += calc(n0,n1,n2,n3,n4,n5-1,n6,n7,n8,n9)
    if n6>0:
        s += calc(n0,n1,n2,n3,n4,n5,n6-1,n7,n8,n9)
    if n7>0:
        s += calc(n0,n1,n2,n3,n4,n5,n6,n7-1,n8,n9)
    if n8>0:
        s += calc(n0,n1,n2,n3,n4,n5,n6,n7,n8-1,n9)
    if n9>0:
        s += calc(n0,n1,n2,n3,n4,n5,n6,n7,n8,n9-1)
    return s

sols = []

def split(n,k,arr):
    if n<0:
        return
    if k == 1:
        if n <= 3:
            sols.append(arr+[n])
        return
    split(n  ,k-1,arr+[0])
    split(n-1,k-1,arr+[1])
    split(n-2,k-1,arr+[2])
    split(n-3,k-1,arr+[3])

split(18,10,[])

n = 0
for sol in sols:
    n += calc(sol[0],sol[1],sol[2],sol[3],sol[4],sol[5],sol[6],sol[7],sol[8],sol[9])