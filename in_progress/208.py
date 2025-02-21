from math import sin, cos, pi
import matplotlib.pyplot as plt
import itertools

def curve_left(x, y, dir0):
  x += cos(pi * (dir0 - 0.2))
  y += sin(pi * (dir0 - 0.2))
  dir0 += -0.4
  return x, y, dir0
  
def curve_right(x, y, dir0):
  x += cos(pi * (dir0 + 0.2))
  y += sin(pi * (dir0 + 0.2))
  dir0 += 0.4
  return x, y, dir0

def apply(curves):
  x = 0
  y = 0
  dir0 = 0
  for i in curves:
    if i:
      x, y, dir0 = curve_right(x, y, dir0)
    else:
      x, y, dir0 = curve_left(x, y, dir0)
  return x, y

def rle(curve):
  v = []
  idx0 = 0
  idx1 = idx0
  cur_val = curve[idx1]
  while idx1 < len(curve):
    if curve[idx1] != cur_val:
      l = idx1 - idx0
      if cur_val:        
        l *= -1
      v.append(l)
      idx0 = idx1
      cur_val = curve[idx1]
    idx1 += 1
  l = idx1 - idx0
  if cur_val:
    l *= -1
  v.append(l)
  return v

def is_equivalent(already, cand):
  for i in range(len(cand)//2):
    if cand == already:
      return True
    cand = cand[2:] + cand[:2]
  return False

# example = 'lrlllrrrrlrrlrllllrllrlll'

closed_loops = []
for N in [20]: #[0,5,10,15,20,25]:
  pt = []
  s = 0
  for Nl in [10]: #[5*i for i in range(N//5+1)]:
    sall = 0
    spart = 0
    for comb in itertools.combinations(range(N),Nl):
      curve = [i in comb for i in range(N)]
      out = apply(curve)
      pt.append(out)
      sall += 1
      if abs(out[0])+abs(out[1]) < 0.01:
        closed_loops += [rle(curve)]
        s += 1
        spart += 1
    print("N",N,"Nl",Nl,"sall",sall,"spart",spart)
  print("N",N,"sall",sall,"s",s)
  print()
x = [p[0] for p in pt]
y = [p[1] for p in pt]
plt.plot(x,y,'.')

# Keep only starting with positive
closed_loops = [i for i in closed_loops if i[0] > 0]

# Drop if starting and ending with the same
closed_loops = [i for i in closed_loops if len(i)%2 == 0]

# Iterate over all loops
closed_loops_new = []
for cand in closed_loops:
  add = True
  for already in closed_loops_new:
    if is_equivalent(already, cand):
      add = False
  if add:
    closed_loops_new.append(cand)


# loops4 = sorted([standardize2(c) for c in loops3])
# loops5 = sorted(list(set(tuple(i) for i in loops4)))
  