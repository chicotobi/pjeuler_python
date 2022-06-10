import matplotlib.pyplot as plt
import numpy as np
  
n = 17
axes = [n, n, n]
data = np.ones(axes, dtype=bool)
  
alpha = 0.9
colors = np.empty(axes + [4], dtype=np.float32)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = 6
y = 4
z = 3

i0 = (n-x)//2
i1 = i0 + x - 1
j0 = (n-y)//2
j1 = j0 + y - 1
k0 = (n-z)//2
k1 = k0 + z - 1

def calc(a,b,c,n):
    count = 2*(a*b+a*c+b*c)
    if n>1:
      count += (n-1) * 4 * (a+b+c)
    if n>2:
      count += 4 * (n-2) * (n-1)
    return count


# Start
data[:,:,:] = False
for i in range(i0,i1+1):
    for j in range(j0,j1+1):
        for k in range(k0,k1+1):
            data[i,j,k] = True

colors[:] = [1, 0, 0, alpha]  # red
ax.voxels(data, facecolors=colors)

# First layer
n = 1
data[:,:,:] = False
for i in range(i0,i1+1):
    for j in range(j0,j1+1):
        data[i,j,k0-n] = True
        data[i,j,k1+n] = True
for i in range(i0,i1+1):
    for k in range(k0,k1+1):
        data[i,j0-n,k] = True
        data[i,j1+n,k] = True
for j in range(j0,j1+1):
    for k in range(k0,k1+1):
        data[i0-n,j,k] = True
        data[i1+n,j,k] = True
colors[:] = [0, 1, 0, alpha]
ax.voxels(data, facecolors=colors)
print(np.sum(data[:]))
print(calc(x,y,z,n))


# Second layer
n = 2
data[:,:,:] = False
for i in range(i0,i1+1):
    for j in range(j0,j1+1):
        data[i,j,k0-n] = True
        data[i,j,k1+n] = True
for i in range(i0,i1+1):
    for k in range(k0,k1+1):
        data[i,j0-n,k] = True
        data[i,j1+n,k] = True
for j in range(j0,j1+1):
    for k in range(k0,k1+1):
        data[i0-n,j,k] = True
        data[i1+n,j,k] = True
for i in range(i0,i1+1):
    data[i,j0-1,k0-1] = True
    data[i,j0-1,k1+1] = True
    data[i,j1+1,k0-1] = True
    data[i,j1+1,k1+1] = True
for j in range(j0,j1+1):
    data[i0-1,j,k0-1] = True
    data[i0-1,j,k1+1] = True
    data[i1+1,j,k0-1] = True
    data[i1+1,j,k1+1] = True
for k in range(k0,k1+1):
    data[i0-1,j0-1,k] = True
    data[i0-1,j1+1,k] = True
    data[i1+1,j0-1,k] = True
    data[i1+1,j1+1,k] = True
colors[:] = [0, 0, 1, alpha]
ax.voxels(data, facecolors=colors)
print(np.sum(data[:]))
print(calc(x,y,z,n))

# Third layer
n = 3
data[:,:,:] = False
for i in range(i0,i1+1):
    for j in range(j0,j1+1):
        data[i,j,k0-n] = True
        data[i,j,k1+n] = True
for i in range(i0,i1+1):
    for k in range(k0,k1+1):
        data[i,j0-n,k] = True
        data[i,j1+n,k] = True
for j in range(j0,j1+1):
    for k in range(k0,k1+1):
        data[i0-n,j,k] = True
        data[i1+n,j,k] = True
for i in range(i0,i1+1):
    for l in range(n-1):
        data[i,j0-n+l+1,k0-l-1] = True
        data[i,j1+l+1,k0-n+l+1] = True
        data[i,j0-n+l+1,k1+l+1] = True
        data[i,j1+l+1,k1+n-l-1] = True
for j in range(j0,j1+1):
    for l in range(n-1):
        data[i0-n+l+1,j,k0-l-1] = True
        data[i1+l+1,j,k0-n+l+1] = True
        data[i0-n+l+1,j,k1+l+1] = True
        data[i1+l+1,j,k1+n-l-1] = True
for k in range(k0,k1+1):
    for l in range(n-1):
        data[i0-n+l+1,j0-l-1,k] = True
        data[i1+l+1,j0-n+l+1,k] = True
        data[i0-n+l+1,j1+l+1,k] = True
        data[i1+l+1,j1+n-l-1,k] = True
for l in range(n-2):
    for m in range(l+1):
        data[i1+1+l-m,j0-n+2+l,k1+1+m] = True
        data[i1+1+l-m,j0-n+2+l,k0-1-m] = True
        data[i0-1-l+m,j0-n+2+l,k1+1+m] = True
        data[i0-1-l+m,j0-n+2+l,k0-1-m] = True
        data[i1+1+l-m,j1+n-2-l,k1+1+m] = True
        data[i1+1+l-m,j1+n-2-l,k0-1-m] = True
        data[i0-1-l+m,j1+n-2-l,k1+1+m] = True
        data[i0-1-l+m,j1+n-2-l,k0-1-m] = True
colors[:] = [1, 1, 0, alpha]
ax.voxels(data, facecolors=colors)
print(np.sum(data[:]))
print(calc(x,y,z,n))


# Fourth layer
n = 4
data[:,:,:] = False
for i in range(i0,i1+1):
    for j in range(j0,j1+1):
        data[i,j,k0-n] = True
        data[i,j,k1+n] = True
for i in range(i0,i1+1):
    for k in range(k0,k1+1):
        data[i,j0-n,k] = True
        data[i,j1+n,k] = True
for j in range(j0,j1+1):
    for k in range(k0,k1+1):
        data[i0-n,j,k] = True
        data[i1+n,j,k] = True
for i in range(i0,i1+1):
    for l in range(n-1):
        data[i,j0-n+l+1,k0-l-1] = True
        data[i,j1+l+1,k0-n+l+1] = True
        data[i,j0-n+l+1,k1+l+1] = True
        data[i,j1+l+1,k1+n-l-1] = True
for j in range(j0,j1+1):
    for l in range(n-1):
        data[i0-n+l+1,j,k0-l-1] = True
        data[i1+l+1,j,k0-n+l+1] = True
        data[i0-n+l+1,j,k1+l+1] = True
        data[i1+l+1,j,k1+n-l-1] = True
for k in range(k0,k1+1):
    for l in range(n-1):
        data[i0-n+l+1,j0-l-1,k] = True
        data[i1+l+1,j0-n+l+1,k] = True
        data[i0-n+l+1,j1+l+1,k] = True
        data[i1+l+1,j1+n-l-1,k] = True
colors[:] = [1, 0, 1, alpha]
for l in range(n-2):
    for m in range(l+1):
        data[i1+1+l-m,j0-n+2+l,k1+1+m] = True
        data[i1+1+l-m,j0-n+2+l,k0-1-m] = True
        data[i0-1-l+m,j0-n+2+l,k1+1+m] = True
        data[i0-1-l+m,j0-n+2+l,k0-1-m] = True
        data[i1+1+l-m,j1+n-2-l,k1+1+m] = True
        data[i1+1+l-m,j1+n-2-l,k0-1-m] = True
        data[i0-1-l+m,j1+n-2-l,k1+1+m] = True
        data[i0-1-l+m,j1+n-2-l,k0-1-m] = True
ax.voxels(data, facecolors=colors)
print(np.sum(data[:]))
print(calc(x,y,z,n))


# Fifth layer
n = 5
data[:,:,:] = False
for i in range(i0,i1+1):
    for j in range(j0,j1+1):
        data[i,j,k0-n] = True
        data[i,j,k1+n] = True
for i in range(i0,i1+1):
    for k in range(k0,k1+1):
        data[i,j0-n,k] = True
        data[i,j1+n,k] = True
for j in range(j0,j1+1):
    for k in range(k0,k1+1):
        data[i0-n,j,k] = True
        data[i1+n,j,k] = True
for i in range(i0,i1+1):
    for l in range(n-1):
        data[i,j0-n+l+1,k0-l-1] = True
        data[i,j1+l+1,k0-n+l+1] = True
        data[i,j0-n+l+1,k1+l+1] = True
        data[i,j1+l+1,k1+n-l-1] = True
for j in range(j0,j1+1):
    for l in range(n-1):
        data[i0-n+l+1,j,k0-l-1] = True
        data[i1+l+1,j,k0-n+l+1] = True
        data[i0-n+l+1,j,k1+l+1] = True
        data[i1+l+1,j,k1+n-l-1] = True
for k in range(k0,k1+1):
    for l in range(n-1):
        data[i0-n+l+1,j0-l-1,k] = True
        data[i1+l+1,j0-n+l+1,k] = True
        data[i0-n+l+1,j1+l+1,k] = True
        data[i1+l+1,j1+n-l-1,k] = True
colors[:] = [0, 1, 1, alpha]
for l in range(n-2):
    for m in range(l+1):
        data[i1+1+l-m,j0-n+2+l,k1+1+m] = True
        data[i1+1+l-m,j0-n+2+l,k0-1-m] = True
        data[i0-1-l+m,j0-n+2+l,k1+1+m] = True
        data[i0-1-l+m,j0-n+2+l,k0-1-m] = True
        data[i1+1+l-m,j1+n-2-l,k1+1+m] = True
        data[i1+1+l-m,j1+n-2-l,k0-1-m] = True
        data[i0-1-l+m,j1+n-2-l,k1+1+m] = True
        data[i0-1-l+m,j1+n-2-l,k0-1-m] = True
ax.voxels(data, facecolors=colors)
print(np.sum(data[:]))
print(calc(x,y,z,n))
