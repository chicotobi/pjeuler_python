import numba as nb
import numpy as np
from math import sqrt, pi, acos

@nb.njit
def euler353(nL=15):
  res = 0
  for n in range(1,nL+1):
    lst = euler353_part1(n)
    r = euler353_part2(lst,n)
    res += r
  return round(res,10)

@nb.njit
def euler353_part1(n):
  r = 2**n-1
  rSq = r*r
  lst = [(0.,0.,0.)]
  lst.pop()
  # 2 zeros case
  lst += [(1.,0.,0.), (0.,1.,0.)]
  # 1 zero case
  for y in range(1,r):
    t = rSq - y*y
    x = int(sqrt(t))
    if x < y:
      break
    if x*x == t:
      lst += [(x/r,y/r,0.),(y/r,x/r,0.),(0.,x/r,y/r)]
  # 0 zeros case
  for z in range(1,r):
    if z%100==0:
      print(z)
    t0 = rSq - z*z
    for y in range(z,r):
      t = t0 - y*y
      if t <= 0:
        break
      x = int(sqrt(t))
      if x < y:
        break
      if x*x == t:
        if x == y and y == z:
          lst += [(z/r,x/r,y/r)]
        elif x == y:
          lst += [(z/r,x/r,y/r), (y/r,x/r,z/r)]
        elif y == z:
          lst += [(z/r,x/r,y/r), (x/r,y/r,z/r)]
        else:
          lst += [(z/r,x/r,y/r),(y/r,x/r,z/r),(x/r,y/r,z/r)]
  return lst

@nb.njit
def myDist(a,b):
  theta = acos(a[0]*b[0]+a[1]*b[1]+a[2]*b[2])
  return theta*theta

@nb.njit
def euler353_part2(lst,n):
  L = len(lst)
  Q = set([i for i in range(L)])
  dist = [ 999.0 ] * L
  dist[0] = 0.0
  c = 0
  d0 = 0
  while True:
    Q.remove(c)
    for i in Q:
      d = d0 + myDist(lst[c],lst[i])
      if d < dist[i]:
        dist[i] = d
    c, d0 = -1, 999.0
    for i in Q:
      if dist[i] < d0:
        c, d0 = i, dist[i]
    if c == -1:
      break
  minDist = 999
  for i in range(L-1,-1,-1):
    if dist[i] >= minDist:
      continue
    z,x,y = lst[i]
    d = dist[i] + 0.5*myDist([z,x,y],[-z,x,y])
    if d < minDist:
      minDist = d
  return 2*minDist/(pi*pi)