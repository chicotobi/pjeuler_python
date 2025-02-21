import sympy

ss = 0
nmax = 1_000_000

for n in range(nmax):
  divs = sympy.divisors(n)
  s = 0
  if len(divs) >= 10:
    for a in divs:
      k = n // a
      if (a + k) % 4 == 0:
        b = (a+k) // 4
        if b < a:
          s += 1
    if s == 10:
      ss += 1