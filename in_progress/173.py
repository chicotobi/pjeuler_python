import functools

@functools.lru_cache(None)
def tiles_ring(l):
  if l==1:
    return 1
  else:
    return 4*l-4
  
@functools.lru_cache(None)
def n_pattern(maxw,ntiles):
  if maxw < 3:
    return 0
  tmp = tiles_ring(maxw)
  if ntiles >= tmp:
    return 1 + n_pattern(maxw-2,ntiles-tmp)
  else:
    return 0
  
ntiles = 1000000
n = 0
for i in range(1,ntiles//4+3):
  n += n_pattern(i,ntiles)
print(n)