import math
import sympy
import functools

@functools.cache
def floorlog(N,p):
    return math.floor(math.log(N,p))

def S(N):
    S = 0
    
    primes = list(sympy.primerange(0, N))
    pp = len(primes)
    
    for i in range(pp):
        p = primes[i]
        if i%100 == 0:
            print(p/N)
        for j in range(i):
            q = primes[j]
            S += M(p,q,N)
    return S


def M(p,q,N):
    max_ep = floorlog(N,p)
    m = 0
    
    # Iterate over all possible candidates
    for ep in range(1,max_ep+1):
        remainder = N / p ** ep
        if remainder >= q:
            eq = floorlog(remainder,q)
            if eq > 0:
                x = p ** ep * q ** eq
                if x <= N and x > m:
                    m = x
    return m
