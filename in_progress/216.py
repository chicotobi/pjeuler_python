from sympy import isprime

s = 0
for n in range(int(5e7)):
  if n%100000==0:
    print(n)
  if isprime(2*n**2-1):
    s += 1