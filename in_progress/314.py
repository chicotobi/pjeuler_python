from functools import cache
import matplotlib.pyplot as plt

@cache
def sols(lastx, lasty, n, m):
  if n == 0 and m == 0:
    return [0], [0]#, [[(0,0)]]
  l = []
  a = []
  #pt_all = []
  for x in range(n+1):
    for y in range(m+1):
      if x == 0 and y == 0:
        continue
      
      # I think, it needs to be convex
      if y == 0:
        if lasty == 0:
          continue
      elif lasty == 0:
        continue
      elif x/y <= lastx/lasty:
        continue
      
      l0 = (x**2 + y**2)**.5
      a0 = n * y - x * y / 2
      #l1, a1, pt1 = sols(x, y, n-x, m-y)
      l1, a1 = sols(x, y, n-x, m-y)
      l += [l0 + i for i in l1]
      a += [a0 + i for i in a1]
      #pt_all += [[(x,y)] + [(x + x1, y + y1) for (x1,y1) in j] for j in pt1]
  return l, a#, pt_all

def myplt(idx,cc):
  fig = plt.figure()
  
  # Grid
  x = []
  y = []
  for i in range(k+1):
    for j in range(k+1):
      x.append(i)
      y.append(j)
  plt.plot(x,y,'.',c='k')
  
  sol = pt[idx]
  x = [i[0] for i in sol]
  y = [i[1] for i in sol]   
  a0 = str(round( a[idx] / k / k       ,2))
  l0 = str(round( l[idx] / k           ,2))
  r0 = str(round( a[idx] / l[idx] / k  ,2))
  ttl = "k " + str(k) + " Area " + a0 + "\nLength "+ l0 + " Ratio " + r0
  plt.title(ttl)
  plt.plot(x,y,'.-',c=cc)
  plt.axis('equal')
  ax = fig.gca()
  ax.grid(False)
  ax.set_xticks([])
  ax.set_yticks([])

for k in [10,12,14,16,18,20]:
  print("k =",k)
  l, a, pt = sols(-1,1,k,k)
  pt = [[(0,0)] + i for i in pt]
  ratio = [i/j for (i,j) in zip(a,l)]
  
  max_ratio = max(ratio)
  sol_idx = ratio.index(max_ratio)

  myplt(sol_idx,'r',)