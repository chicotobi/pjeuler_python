import bezier, math
from mpmath import mp
mp.dps = 50

def my_bezier(t,v):
  x0 = 1
  y0 = 0
  x1 = 1
  y1 = v
  x2 = v
  y2 = 1
  x3 = 0
  y3 = 1
  
  x0 = x0*t+x1*(1-t)
  y0 = y0*t+y1*(1-t)
  x1 = x1*t+x2*(1-t)
  y1 = y1*t+y2*(1-t)
  x2 = x2*t+x3*(1-t)
  y2 = y2*t+y3*(1-t)
  
  x0 = x0*t+x1*(1-t)
  y0 = y0*t+y1*(1-t)
  x1 = x1*t+x2*(1-t)
  y1 = y1*t+y2*(1-t)
  
  x0 = x0*t+x1*(1-t)
  y0 = y0*t+y1*(1-t)
  return x0,y0
  
def eval(N,v):
  #cv = bezier.Curve([[0,v,1,1],[1,1,v,0]],degree=3)
  l = 0
  a = -mp.pi/4
  xold, yold = my_bezier(0,v)
  for i in range(1,N+1):
    x,y = my_bezier(i/N,v)
    if i>0:
      l += ((x-xold)**2+(y-yold)**2)**.5
      a += (y+yold)*(x-xold)/2
    xold = x
    yold = y
  return l,a

N = 100000
v1 = 0.5517
v2 = 0.5518
l1,a1 = eval(N,v1)
l2,a2 = eval(N,v2)

aold = 1
while True:
  N = round(N*1.1)
  v = (v1+v2)/2
  l,a = eval(N,v)
  err = 100*(l-math.pi/2)/(math.pi/2)
  err = round(err,10)
  #print(v,l,a,err)
  print(v,l,a,aold,err)
  if a>0:
    v2 = v
  else:
    v1 = v
    