import numpy as np
import functools

def n_from_lst(lst):
  primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
  return np.prod([float(b)**e for (b,e) in zip(primes,lst)])
  
def sol_from_lst(lst):
  ans = np.prod([2*x+1 for x in lst])
  return (ans+1)//2  

@functools.lru_cache(None)
def partition(number,maxlen):
  answer = [[number]]
  for x in range(1, number):
    for y in partition(number - x,maxlen-1):
      if len(y) <= maxlen - 1 and x >= max(y):
        answer.append([x]+y)
  return answer

val = 4000000
min_n = 1e20
max_len = 15
max_s = 20
for s in range(1,max_s+1):
  for p in partition(s,max_len):
    if sol_from_lst(p) > val:
      n = n_from_lst(p)
      if n < min_n:
        min_n = n
print(int(min_n))