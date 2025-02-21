import matplotlib.pyplot as plt
from functools import cache
from numpy import arctan2

@cache
def sols(last_x, last_y, last_angle, pts):
  if len(pts) == 0:
    return [0], [0], [[]]
  
  l = []
  a = []
  path = []
  
  for (new_x,new_y) in pts:
    
    dx = new_x - last_x
    dy = new_y - last_y
    
    angle = arctan2(dy,dx)
    
    if last_angle <= angle:
      continue
      
    l0 = (dx**2 + dy**2)**.5
    a0 = (k - last_x) * dy - dx * dy / 2
    
    new_pts = tuple([(x,y) for (x,y) in pts if (new_x < x and new_y <= y) or (new_x <= x and new_y < y)])
    
    l1, a1, path1 = sols(new_x, new_y, angle, new_pts)
    l += [l0 + i for i in l1]
    a += [a0 + i for i in a1]
    path += [[(new_x, new_y)] + j for j in path1]
    
  return l, a, path

def myplt(idx,allowed):
  fig = plt.figure()
  
  # Grid
  x = []
  y = []
  for i in range(k+1):
    plt.plot([0,k],[i,i],'-',c='k')
    plt.plot([i,i],[0,k],'-',c='k')
  
  # Allowed pt
  x = [i[0] for i in list(allowed)]
  y = [i[1] for i in list(allowed)]
  plt.plot(x,y,'.',c='b')
  
  sol = [(0,0)] + path[idx]
  x = [i[0] for i in sol]
  y = [i[1] for i in sol]   
  a0 = str(round( a[idx] / k / k       ,2))
  l0 = str(round( l[idx] / k           ,2))
  r0 = str(round( a[idx] / l[idx] / k  ,2))
  ttl = "k " + str(k) + " Area " + a0 + "\nLength "+ l0 + " Ratio " + r0
  plt.title(ttl)
  plt.plot(x,y,'.-',c='r')
  plt.axis('equal')
  ax = fig.gca()
  ax.grid(False)
  ax.set_xticks([])
  ax.set_yticks([])
  plt.show()

def update_allowed(pt):
  new_allowed = set()
  for (x,y) in pt:
    tmp = [(x,y)]
    if y > 0:
      tmp.append((x,y-1))
    if y < k:
      tmp.append((x,y+1))
    if x > 0:
      tmp.append((x-1,y))
      if y > 0:
        tmp.append((x-1,y-1))
      if y < k:
        tmp.append((x-1,y+1))
    if x < k:
      tmp.append((x+1,y))
      if y > 0:
        tmp.append((x+1,y-1))
      if y < k:
        tmp.append((x+1,y+1))
    new_allowed.update(tmp)
  if (0,0) in new_allowed:
    new_allowed.remove((0,0))
  return tuple(sorted(new_allowed))

k = 50
allowed = tuple([(0,k//2),(0,k),(k//2,k),(k,k)])
old_max_ratio = 0
loop = 0
angle = arctan2(1,-1)
while True:
  print("Loop",loop,"max_ratio",old_max_ratio)
  l, a, path = sols(0,0,angle,allowed)
  ratio = [i/j/k for (i,j) in zip(a,l)]
  
  max_ratio = max(ratio)
  sol_idx = ratio.index(max_ratio)
  
  myplt(sol_idx,allowed)
  
  if max_ratio - old_max_ratio < 1e-5:
    break
  
  loop += 1
  old_max_ratio = max_ratio  
  allowed = update_allowed(path[sol_idx])