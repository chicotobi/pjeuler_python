#from pjeuler import gcd

# m = 1000
# v = [0]*m
# for x in range(1,m):
#   for y in range(x,m):
#     if x*y % (x+y)==0:      
#       n = x*y//(x+y)
#       v[n] += 1
#       print("1/"+str(x)+" + 1/"+str(y)+" = 1/"+str(n))

import sympy

for n in range(1,1000000):
  if sympy.divisor_count(n)<100:
    continue
  x = n+1
  a = 0
  while True:
    y = x*n/(x-n)
    if y < x:
      if a > 800:
        ndivs = sympy.divisor_count(n)
        print("For n="+str(n)+" with "+str(ndivs)+": "+str(a)+" solutions.")
      a = 0
      break
    if y==round(y):
      #print("1/"+str(x)+" + 1/"+str(round(y))+" = 1/"+str(n))
      a += 1
    x += 1