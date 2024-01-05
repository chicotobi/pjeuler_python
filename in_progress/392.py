import scipy.optimize
import math

def area(angles):
  x = [math.pi/2] + list(angles) + [0]
  A = [math.sin(x[i-1]) * (math.cos(x[i])-math.cos(x[i-1])) for i in range(1,N+2)]
  return 4 * sum(A)

N = 200
x0 = [math.pi/2/(N+1) * i for i in range(N,0,-1)]

print(round(scipy.optimize.minimize(area,x0,tol=1e-11).fun,10))