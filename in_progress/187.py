import pjeuler

l = int(1e8)

ps = list(pjeuler.primes(l//2))

n = len(ps)

n_primes = [0,0]
for i in range(n-1):
  n_primes += [i+1] * (ps[i+1]-ps[i])
n_primes += [i+2] * (l-ps[-1])

s = 0
for p in ps:
  if p**2 > l:
    break
  p2 = l // p
  s += n_primes[p2] - n_primes[p-1]
print(s)