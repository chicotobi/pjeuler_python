from sympy import primerange

primes = set(primerange(1_000_000))

# cubes = [i**3 for i in range(10000)]

# for p in primes:
#   for a in range(1,p):
#     n = a**3
#     k3 =  n**2 * ( n + p)
#     if k3 in cubes:
#       print(p,n)


# for p in primes:
#   for n in range(1,3*p):
#     k3 =  n**2 * ( n + p)
#     if k3 in cubes:
#       k = round(k3**(1/3))
#       print(n,"** 3 + ",n,"** 2 * ",p," == ",k,"** 3")

listp = []
for a in range(1,1000):
  for m in range(1,2):
    p = 3 * a * m * (a + m) + 1
    if p in primes and p < 1_000_000:
      print(a**3,"** 3 + ",a**3,"** 2 * ",p," == ",(a+m)**3,"** 3")
      listp += [p]
      
sols = len(set(listp))
print("s:",sols)