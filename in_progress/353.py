from math import pi,acos
import numpy as np
import math
from mayavi import mlab
import scipy.sparse
import scipy.sparse.csgraph

def risk(p1,p2):
  x1,y1,z1 = p1
  x2,y2,z2 = p2
  alpha = acos((x1*x2+y1*y2+z1*z2)/r**2)
  return alpha**2

def dist(p1,p2):
  x1,y1,z1 = p1
  x2,y2,z2 = p2
  return abs(x1-x2)+abs(y1-y2)+abs(z1-z2)

def plot():
  idx = min_idx
  sol_pts = []
  while True:
    idx = sol[0,idx]
    if idx == -9999:
      break
    pt = pts[idx]
    sol_pts = [pt] + sol_pts
    
  x = sol_pts[-1][0]
  y = sol_pts[-1][1]
  if x * y !=0:
    l = r / (x**2+y**2)**.5
    x *= l
    y *= l
    p2 = (x,y,0)
  else:
    p2 = (r,0,0)
  sol_pts += [p2]
    
  # Create a sphere
  pi = np.pi
  cos = np.cos
  sin = np.sin
  phi, theta = np.mgrid[0:pi/2:21j, pi/4:pi/2:21j]
  
  x = r * sin(phi) * cos(theta)
  y = r * sin(phi) * sin(theta)
  z = r * cos(phi)
  
  xx,yy,zz = zip(*pts)
  xsol,ysol,zsol = zip(*sol_pts)
  
  
  mlab.figure(1, bgcolor=(1,1,1), fgcolor=(0, 0, 0), size=(800, 800))
  mlab.clf()
  mlab.mesh(x, y, z,color=(0,1,1),opacity=0.5)
  mlab.points3d(xx,yy,zz,color=(1,0,0),scale_factor=0.01*r)
  mlab.plot3d(xsol,ysol,zsol,line_width=20*r,tube_radius=r/500)
  mlab.view(66, 52, 3*r,focalpoint="auto")
  mlab.show()

s = 0
rs = [2**n-1 for n in range(1,16)]
for r in rs:
  print("Case: r=",r)
  
  print("Generate...")
  pts = []
  for x in range(r):
    if x%100==0:
      print(x," of ",r, " len(pts): ",len(pts))
    hlp = r**2-x**2
    for y in range(x,r):
      z2 = hlp-y**2
      if z2<0:
        break
      z = int(sqrt(z2))
      if z**2 == z2:
        pts.append((x,y,z))
        if z<=x:
          pts.append((z,x,y))
        if z<=y:
          pts.append((z,y,x))

  pts = list(set(pts))
  n = len(pts)+1
  
  start_idx = pts.index((0,0, r))
  goal_pts = [pt for pt in pts if pt[2]==0]
  goal_idxs = [n-1]
  for pt in goal_pts:
    goal_idxs.append(pts.index(pt))  
  
  print("Build...")
  max_dist = 10000 
  ii = []
  jj = []
  vv = []
  for i,p1 in enumerate(pts):
    for j,p2 in enumerate(pts):
      if i<j:
        if dist(p1,p2) < max_dist:
          rsk = risk(p1,p2)
          ii.append(i)
          jj.append(j)
          vv.append(rsk)
          ii.append(j)
          jj.append(i)
          vv.append(rsk)
    if i not in goal_idxs:
      p2 = (p1[0], p1[1], -p1[2])      
      if dist(p1,p2) < max_dist:
        rsk = risk(p1,p2)
        ii.append(i)
        jj.append(n-1)
        vv.append(rsk/2)
        ii.append(n-1)
        jj.append(i)
        vv.append(rsk/2)
  mat = scipy.sparse.csr_matrix((vv,(ii,jj)),shape=(n,n))
  print("Matrix has ",mat.count_nonzero()," elements.")
  
  print("Solve...")
  result, sol = scipy.sparse.csgraph.shortest_path(mat,indices=[start_idx],return_predecessors=True)
  
  min_dst = 1
  for idx in goal_idxs:
    dst = result[0,idx]/pi**2 * 2    
    if dst < min_dst:
      min_dst = dst
      min_idx = idx
  print("Minimum risk: ",round(min_dst,10))
  s += min_dst
print(round(s,10))