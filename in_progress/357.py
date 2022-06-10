import pjeuler, math

n = 100000000

ps = list(pjeuler.primes(n))

set_ps = set(ps)

def factors(m):
  if m<1:
    return []
  if m==1:
    return [1]
  n = math.floor(m**.5)
  f = []
  for p in ps:
    while m % p == 0:
        m /= p
        f.append(p)
    if(m==1):
      break
    if p>n:
      break
  if m != 1:
      f.append(int(m))
  return f

s = 0
for (count,p) in enumerate(ps):
    i = p - 1
    v = 2 + i // 2
    if v not in set_ps:
        continue
    if i%4 == 0:
        continue
    fs = factors(i)
    b = True
    for j in fs:
        v = j + i//j
        if v not in ps:
            b = False
    if b:
        print(i)
        s += i