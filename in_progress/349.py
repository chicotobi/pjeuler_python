import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

n = 2000

a = np.zeros((n,n))

x = n//2
y = n//2

steps = 50000
step = 0
rot = 0
arr = [0]*steps
n = 0
for step in range(steps):
    if a[x,y] == 0:
        n += 1
        a[x,y] = 1
        rot = (rot - 1) % 4
    else:
        n -= 1
        a[x,y] = 0
        rot = (rot + 1) % 4
    if rot == 0:
        x -= 1
    elif rot == 1:
        y -= 1
    elif rot == 2:
        x += 1
    else:
        y += 1
    arr[step] = n
    
# Get period length from Fourier analysis
periodic_part = arr[11000:]
indices = [i for (i,x) in enumerate(fft(periodic_part)) if np.real(x)>0 and i>0]
period = len(periodic_part) // min(indices)
incr = arr[11000+period] - arr[11000]

steps = 10**18
offset = steps%period
step_until_period = offset + 120 * period
step_until_end = steps - step_until_period
periods_until_end = step_until_end // period

n = arr[step_until_period-1] + incr * periods_until_end
print(n)