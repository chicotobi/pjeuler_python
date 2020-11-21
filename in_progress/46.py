import numpy as np

N = 100000

# generate some primes
primes = []
a = np.ones(N,dtype=np.int32)
a[0] = 0
while True:
    try:
        p = a.nonzero()[0][0]+1
        primes.append(p)
        a[p-1::p] = 0
    except:
        break

# create trial array
a = np.zeros(N,dtype=np.int32)
for i in range(1,int(N/2)):
    a[2*i+1] = 1
print(a)

primes = primes[1:]
print(primes)
for prime in primes:
    print(prime)
    for n in range(round(N**0.5)+1):
        num = prime + 2 * n**2
        if num < N and a[num] == 1:
            a[num] = 0
print(a.argmax())
