import math
import sympy


def S(N):
    S = 0
    
    primes = list(sympy.primerange(0, N))
    pp = len(primes)
    
    for i in range(pp):
        q = primes[i]
        if i%100 == 0:
            print(q/N)
        for j in range(i):
            p = primes[j]
            S += M(p,q,N)
    return S

def M(p,q,N):
    logN = math.log(N,p)
    k = math.log(q,p)
    max_eq = math.floor((logN - 1) / k)
    best_val = 0
    for eq in range(1,max_eq+1):
        ep = math.floor(logN - k * eq)
        val = ep + k * eq
        #print("check",p,"**",ep,"*",q,"**",eq,"with",round(p**val))
        if val > best_val:
            best_ep = ep
            best_eq = eq
            best_val = val
    if best_val == 0:
        return 0
    else:
        #print()
        return (p ** best_ep * q ** best_eq)

print(S(10_000_000))
#print(S(300))