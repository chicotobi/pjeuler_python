import functools

@functools.lru_cache(None)
def increasing_numbers_starting_with(l,i):
  if i==0:
    return 0
  if l==1:
    return 1
  n = 0
  for j in range(i,10):
    n += increasing_numbers_starting_with(l-1,j)
  return n

@functools.lru_cache(None)
def decreasing_numbers_starting_with(l,i):
  if i==0:
    return 0
  if l==1:
    return 1
  n = 1
  for j in range(i+1):
    n += decreasing_numbers_starting_with(l-1,j)
  return n

expo = 100
n = -9*expo
for l in range(1,expo+1):
  for i in range(10):
    n += increasing_numbers_starting_with(l,i)
  for i in range(10):
    n += decreasing_numbers_starting_with(l,i)
print(n)