from functools import cache

@cache
def f(tpl):
  l = list(tpl)
  n = len(l)
  dct = {i:0 for i in range(6)}
  if n == 1 and l[0] == 5:
    dct[1] = 1
    return dct
  for idx in range(n):
    l2 = [i for i in l]
    sheet = l2.pop(idx)
    if sheet == 1:
      l2 = l2 + [2,3,4,5]
    elif sheet == 2:
      l2 = l2 + [3,4,5]
    elif sheet == 3:
      l2 = l2 + [4,5]
    elif sheet == 4:
      l2 = l2 + [5]
    dct2 = f(tuple(l2))
    for i in range(5):
      dct[i] += dct2[i] * 1/n
  
  dct_out = {i:0 for i in range(6)}
  if n == 1:
    for i in range(5):
      dct_out[i+1] = dct[i]
    return dct_out
  else:
    return dct
    
res = f(tuple([1]))

out = 0 * res[2] + 1 * res[3] + 2 * res[4] + 3 * res[5]
print(round(out,6))