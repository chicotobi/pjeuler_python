from functools import lru_cache

@lru_cache(None)
def split(number,min_size):
  c = 0
  for i in range(min_size,number-min_size+1):
    c += split(number-i,i)
  if min_size<=number:
    c += 1
  return c
