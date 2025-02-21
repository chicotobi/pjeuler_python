import scipy.optimize
import math

# Solve problem with smart initial values
def res(inp):
  x, l, alpha = inp
  r1 = (l**1 + 1)**2 - x**2 * (1+l** 2) + 2 * x**2 * l**1 * math.cos(1*alpha)
  r7 = (l**7 + 1)**2 - x**2 * (1+l**14) + 2 * x**2 * l**7 * math.cos(7*alpha)
  r8 = (l**8 + 1)**2 - x**2 * (1+l**16) + 2 * x**2 * l**8 * math.cos(8*alpha)
  return [r1, r7, r8]

x0 = [2, 1, math.pi / 4]
s = scipy.optimize.fsolve(res, x0, xtol = 1e-15)
l = s[1]

# Area for circular triangle
def area(r1,r2,r3):
  v = math.sqrt(r1*r2*r3*(r1+r2+r3))
  v1 = r1**2 * math.acos( 1 - 2*r2*r3 / (r1+r2) / (r1+r3) )
  v2 = r2**2 * math.acos( 1 - 2*r3*r1 / (r2+r3) / (r2+r1) )
  v3 = r3**2 * math.acos( 1 - 2*r1*r2 / (r3+r1) / (r3+r2) )
  return v - 0.5 * (v1 + v2 + v3)

# Area for triangle C0_C7_C8 and C0_C1_C8
A = area(1, l**7, l**8) + area(1, l, l**8)

# Integrate the infinite series with factor l**2
G = A / (1-l**2)
print(round(G,10))