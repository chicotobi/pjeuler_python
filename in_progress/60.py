import numpy as np
import sys
import scipy.special as sc
from itertools import combinations

N = 1000000

# generate some primes
primes = []
a = np.ones(N + 1, dtype=np.int32)
a[0] = 0
a[1] = 0
for i in range(N + 1):
    if a[i]:
        primes.append(i)
        a[2 * i::i] = 0

print('Done primes')

small_primes = primes[:1500]
print('Largest prime in test group:', small_primes[-1])


def is_prime(val):
    if val < N:
        return a[val]
    for p in primes:
        if p * p > val:
            return True
        if not val % p:
            return False
    return True


l = len(small_primes)
prime_pairs = set()
for idx1 in range(l):
    print('\r' + str(idx1 / l), end='')
    sys.stdout.flush()
    for idx2 in range(idx1 + 1, l):
        p1 = small_primes[idx1]
        p2 = small_primes[idx2]
        q1 = int(str(p1) + str(p2))
        q2 = int(str(p2) + str(p1))
        if is_prime(q1) and is_prime(q2):
            s = frozenset([p1, p2])
            prime_pairs.add(s)
print('\r' + str(len(prime_pairs)), prime_pairs)

old_set = prime_pairs

for i in range(3):
    new_set = set()
    counter = 0
    ll = sc.binom(len(old_set),2)
    for set_pair in combinations(old_set, 2):
        counter +=1
        if counter % 100 == 0:
            print('\r'+str(counter/ll),end='')
        s1 = set_pair[0]
        s2 = set_pair[1]
        diff = s1.symmetric_difference(s2)
        if len(diff) == 2:
            if diff in prime_pairs:
                s = s1.union(s2)
                if s not in new_set:
                    new_set.add(s)
        old_set = new_set
    print('\r' + str(len(old_set)), old_set)

# eval
eval = [sum(list(s)) for s in old_set]
if len(eval)>0:
    print('Minimum sum:', np.min(eval))
else:
    print('Empty')