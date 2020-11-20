import numpy as np

N = 1000000

# generate some primes
primes = []
a = np.ones(N,dtype=np.int32)
a[0] = 0
idx = 0
while True:
    while idx < N-1 and a[idx]==0:
        idx += 1
    if idx == N-1:
        break
    p = idx+1
    primes.append(p)
    a[p-1::p] = 0
print('Done generating primes.')


def count_prime_factors(num):
    n_facs = 0
    pit = 0
    while num>1:
        p = primes[pit]
        acti = False
        while num % p == 0:
            acti = True
            num /= p
        if acti:
            n_facs += 1
        pit += 1
    return n_facs


run = 0
for i in range(N):
    n_facs = count_prime_factors(i)
    if n_facs == 4:
        run += 1
    else:
        run = 0
    if run == 4:
        print(i-3)
        break
