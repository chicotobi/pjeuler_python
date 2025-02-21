import numpy as np

n = 20

idx0 = 0

mat = np.zeros((n*n,n*n))

def pr(v):
  x = v.reshape(n,n).tolist()
  s = '\n'.join(' '.join('{:.3f}'.format(i) for i in j) for j in x)
  print(s)
  
def get_idx(i,j):
  return i * n + j

def get_ij(idx):
  return idx // n, idx % n

# Define the transition matrix
for i in range(n):
  for j in range(n):
    idx = get_idx(i,j)
  
    idxu = get_idx(i-1,j)
    idxd = get_idx(i+1,j)
    idxr = get_idx(i,j+1)
    idxl = get_idx(i,j-1)
    
    if i > 0:
      mat[idx,idxu] = 1
    if i < n - 1:
      mat[idx,idxd] = 1
    if j > 0:
      mat[idx,idxl] = 1
    if j < n - 1:
      mat[idx,idxr] = 1     

row_sum = np.sum(mat, axis=1)

mat2 = mat / row_sum[:,None]

mat3 = mat2.transpose()

v = np.ones((n*n,1))

for i in range(50):
  print()
  print("Step ",i)
  pr(v)
  v = mat3 @ v