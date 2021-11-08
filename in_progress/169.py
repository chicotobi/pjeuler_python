import functools

@functools.lru_cache(None)
def f(x):
  if x<=1:
    return x
  if x%2==0:
    return f(x//2)
  else:
    return f(x//2)+f(x//2+1)
  
print(f(int(1e12)*int(1e13)+1))