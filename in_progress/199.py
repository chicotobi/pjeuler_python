def pjeuler199():
  import math
  
  k = 1+2/math.sqrt(3)
  
  ratio = 1 - 3 * 1/k**2
  gaps = [(-1,k,k),(-1,k,k),(-1,k,k),(k,k,k)]
    
  steps = 10
  for i in range(steps):
    new_gaps = []
    for (k1, k2, k3) in gaps:
      k_new = k1 + k2 + k3 + 2 * math.sqrt( k1*k2 + k2*k3 + k1*k3)
      new_gaps += [(k1,k3,k_new),(k1,k2,k_new),(k2,k3,k_new)]
      ratio -= 1/k_new**2
    gaps = new_gaps
  
  return round(ratio,8)