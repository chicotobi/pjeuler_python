import numpy as np
from numpy.linalg import svd

s = '6,X,X,(vCC),(vI),X,X,X,(hH),B,O,(vCA),(vJE),X,(hFE,vD),O,O,O,O,(hA),O,I,(hJC,vB),O,O,(hJC),H,O,O,O,X,X,X,(hJE),O,O,X'
dim = int(s[0])

f = [['']*dim for i in range(dim)]

idx = 2
for (i,row) in enumerate(f):
  for (j,el) in enumerate(row):
    in_bracket = s[idx]=='('
    if in_bracket:
      offset = s[idx:].find(')') + 1
    else:
      offset = s[idx:].find(',')
    f[i][j] = s[idx:(idx+offset)]
    idx += offset + 1

# Find number of variables
n0 = [c for c in 'ABCDEFGHIJ' if c in s]
n1 = [(i,j) for (i,row) in enumerate(f) for (j,el) in enumerate(row) if el=='O']

var = {c:i for (i,c) in enumerate(n0)}
offset = len(n0)
for (i,el) in enumerate(n1):
  var[el] = offset+i

nvar = len(var)
neq = sum(c in 'hv' for c in s)
a = np.zeros((neq,nvar))
b = np.zeros((neq,1))

def add_eqn(ieq,i,j,sm,dr):
  if len(sm)==2:
    idx = var[sm[0]]
    a[ieq,idx] -= 10
    idx = var[sm[1]]
    a[ieq,idx] -= 1
  else:
    idx = var[sm[0]]
    a[ieq,idx] -= 1
  if dr=='h':
    j += 1
    while j < dim and f[i][j] in 'ABCDEFGHIJO' and f[i][j] != '':
      if f[i][j] == 'O':
        idx = var[(i,j)]
      else:
        idx = var[f[i][j]]
      a[ieq,idx] += 1
      j += 1
  if dr=='v':
    i += 1
    while i < dim and f[i][j] in 'ABCDEFGHIJO' and f[i][j] != '':
      if f[i][j] == 'O':
        idx = var[(i,j)]
      else:
        idx = var[f[i][j]]
      a[ieq,idx] += 1
      i += 1

# Parse equations
ieq = 0
for (i,row) in enumerate(f):
  for (j,el) in enumerate(row):
    if ',' in el:
      # Two equations
      idx = el.find(',')
      add_eqn(ieq,i,j,el[2:idx],el[1])
      ieq += 1
      add_eqn(ieq,i,j,el[idx+2:-1],el[idx+1])
      ieq += 1
    elif 'h' in el or 'v' in el:
      # One equation
      add_eqn(ieq,i,j,el[2:-1],el[1])
      ieq += 1


u, s, vh = svd(a, full_matrices=True)

v_goal = [8,4,2,6,0,3,5,7,1] + [1,9,6,8,7,1,9,3,2,1,4,3,7]