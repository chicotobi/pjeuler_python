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
    a[(p+idx)::p] = 0
    idx +=1
print('Done generating primes.')

for p in primes:
    strp = str(p)
    for digit in range(10):
        if str(digit) in strp:
            counter = 1
            for d2 in range(digit+1,10):
                new_strp = strp.replace(str(digit),str(d2))
                new_p = int(new_strp)
                if a[new_p-1]:
                    counter += 1
            if counter>7:
                print(p)
                quit()

