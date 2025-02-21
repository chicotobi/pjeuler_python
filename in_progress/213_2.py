from math import comb
from numpy import convolve as co

n = 30

d = [[dict({1:1}) for i in range(n)] for j in range(n)]


nrounds = 5
for round0 in range(nrounds):
  print(round0)
  d2 = [[dict() for i in range(n)] for j in range(n)]
  for i in range(n):
    for j in range(n):
      dict0 = dict({i:0 for i in range(n*n)})
      
      if i > 0:
        dxu = d[i-1][j]
      else:
        dxu = dict({0:1})
      if i < n - 1:
        dxd = d[i+1][j]
      else:
        dxd = dict({0:1})
      if j > 0:
        dxl = d[i][j-1]
      else:
        dxl = dict({0:1})
      if j < n - 1:
        dxr = d[i][j+1]
      else:
        dxr = dict({0:1})
        
      if i == 0:
        pu = 1
      elif i == 1:
        if j in [0, n-1]:
          pu = 1/2
        else:
          pu = 1/3
      else:
        if j in [0, n-1]:
          pu = 1/3
        else:
          pu = 1/4
  
      if i == n - 1:
        pd = 1
      elif i == n - 2:
        if j in [0, n-1]:
          pd = 1/2
        else:
          pd = 1/3
      else:
        if j in [0, n-1]:
          pd = 1/3
        else:
          pd = 1/4
        
        
      if j == 0:
        pl = 1
      elif j == 1:
        if i in [0, n-1]:
          pl = 1/2
        else:
          pl = 1/3
      else:
        if i in [0, n-1]:
          pl = 1/3
        else:
          pl = 1/4
          
      if j == n - 1:
        pr = 1
      elif j == n - 2:
        if i in [0, n-1]:
          pr = 1/2
        else:
          pr = 1/3
      else:
        if i in [0, n-1]:
          pr = 1/3
        else:
          pr = 1/4
        
      # Now create the four different discrete probability distributions
      dictu = dict({i:0 for i in range(n*n)})
      for (xu,ppu) in dxu.items():
        for vxu in range(xu+1):
          dictu[vxu] += comb(xu, vxu) * pu ** vxu * (1-pu) ** (xu-vxu) * ppu
          
      dictd = dict({i:0 for i in range(n*n)})
      for (xd,ppd) in dxd.items():
        for vxd in range(xd+1):
          dictd[vxd] += comb(xd, vxd) * pd ** vxd * (1-pd) ** (xd-vxd) * ppd
          
      dictl = dict({i:0 for i in range(n*n)})
      for (xl,ppl) in dxl.items():
        for vxl in range(xl+1):
          dictl[vxl] += comb(xl, vxl) * pl ** vxl * (1-pl) ** (xl-vxl) * ppl
          
      dictr = dict({i:0 for i in range(n*n)})
      for (xr,ppr) in dxr.items():
        for vxr in range(xr+1):
          dictr[vxr] += comb(xr, vxr) * pr ** vxr * (1-pr) ** (xr-vxr) * ppr
          
      # Convolution
      pu = list(dictu.values())
      pd = list(dictd.values())
      pl = list(dictl.values())
      pr = list(dictr.values())
      probs = co(pu,co(pd,co(pl,pr)))
      vals = list(range(len(probs)))
      d2[i][j] = dict(zip(vals,probs))
  
  # Now maybe simplify, otherwise everything explodes?
  for i in range(n):
    for j in range(n):
      d[i][j] = dict({k:v for (k,v) in d2[i][j].items() if v > 1e-6})