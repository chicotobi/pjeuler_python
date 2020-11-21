import math

x = 3/7

max_d = 1000000
y = 0
for d in range(1,max_d):
  if d%7!=0:
    n = math.floor(x * d)
    if n/d > y:
      y = n/d
      best_n = n
      best_d = d