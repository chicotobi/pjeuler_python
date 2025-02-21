from functools import cache

@cache
def words(n, c1, c2, c3, w1, w2, w3, w4):
  if n == 3:
    if w1 or w2 or w3 or w4:
      return []
    return ['']
  
  k = []
  if c1+c2+c3 == 'REE':
    if w1:
      k += [i + 'F' for i in words(n-1, 'F', c1, c2, False, w2, w3, w4)]
  elif c1+c2+c3 == 'ARE':
    if w2:
      k += [i + 'F' for i in words(n-1, 'F', c1, c2, w1, False, w3, w4)]
  else:
    k += [i + 'F' for i in words(n-1, 'F', c1, c2, w1, w2, w3, w4)]
    
  if c1+c2+c3 == 'REA':
    if w3:
      k += [i + 'A' for i in words(n-1, 'A', c1, c2, w1, w2, False, w4)]
  else:
    k += [i + 'A' for i in words(n-1, 'A', c1, c2, w1, w2, w3, w4)]
    
  if c1+c2+c3 == 'EEF':
    if w4:
       k += [i + 'R' for i in words(n-1, 'R', c1, c2, w1, w2, w3, False)]
  else:
      k += [i + 'R' for i in words(n-1, 'R', c1, c2, w1, w2, w3, w4)]
    
  k += [i + 'E' for i in words(n-1, 'E', c1, c2, w1, w2, w3, w4)]

  return k

x = ['A','E','F','R']
s = []
N = 15
for c1 in x:
  for c2 in x:
    for c3 in x:
      s += [i + c1 + c2 +c3 for i in words(N,c1,c2,c3,True,True,True,True)]
print(s)