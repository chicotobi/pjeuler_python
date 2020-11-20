import math
import gmpy2, time

am = range(1000,15000,1000)
at = []
for m in am:
  ax = []
  ay = []
  l = []
  n = 0
  t0 = time.time()
  for x in range(1,m):
    s = x%4
    if s!=2:
      for y in range(1,min(x,m-x)):
          a = x**2+y**2+x*y
          if  gmpy2.is_square(a):
            n += 1
              #print(x%4,y%4)
                #ax = ax+[x]
                #ay = ay+[y]
                #l = l + [(x,y)]
                #print(a%3,a%4,a%5,a%6,a%7)
  t1 = time.time()-t0
  at = at + [t1]
  print("m=",m,"n=",n," took ",t1," seconds")

import matplotlib.pyplot as plt
plt.clf()
plt.plot(am,at,".")
plt.show()
from scipy.optimize import curve_fit
def myExpFunc(x, a, b):
    return a * np.power(x, b)
popt, pcov = curve_fit(myExpFunc, am, at)
plt.plot(range(1000,120000,1000), myExpFunc(range(1000,120000,1000), *popt), 'r-.')