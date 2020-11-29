import numpy as np


def p_dice(n):
  l = {i:0 for i in range(2,2*n+1)}
  for i in range(1,n+1):
    for j in range(1,n+1):
      l[i+j] += 1/n**2
  return l

a = np.zeros((40,40))
for i in range(40):
  for (s,p) in p_dice(6).items():
    a[i,(i+s)%40] = p
b = np.zeros((40,40))
for i in range(40):
  if i in [2,17,33]:
    #CC
    b[i,i] = 14/16
    b[i,0] = 1/16
    b[i,10] = 1/16
  elif i in [7,22,36]:
    #CH
    b[i,i] = 6/16
    b[i,0] = 1/16
    b[i,10] = 1/16
    b[i,11] = 1/16
    b[i,24] = 1/16
    b[i,39] = 1/16
    b[i,5] = 1/16
    if i==7:
      b[i,15] = 2/16
      b[i,12] = 1/16
    elif i==22:
      b[i,25] = 2/16
      b[i,28] = 1/16
    elif i==36:
      b[i,5] = 2/16
      b[i,12] = 1/16 
    b[i,(i-3)] = 1/16
  elif i==30:
    b[30,10] = 1
  else:
    b[i,i] = 1
    
c = b.dot(a)
#c = c.transpose()
  
w,v = np.linalg.eig(c)

x = abs(v[:,0])
x /= sum(x)
di = {k:v for (k,v) in enumerate(list(x))}