def is_prime(val):
    for i in range(2,round(val**0.5)+1):
        if not val%i:
            return False
    return True


n_diag = 1
n_primes = 0
for i in range(1,100000):

    base = 4*i**2-4*i+1

    if is_prime(base+2*i):
        n_primes += 1
    if is_prime(base+4*i):
        n_primes += 1
    if is_prime(base+6*i):
        n_primes += 1

    n_diag += 4
    ratio = n_primes/n_diag
    if i % 100 == 0:
        print(n_primes, n_diag, ratio)
    if ratio<0.1:
        print(2*i+1)
        quit()