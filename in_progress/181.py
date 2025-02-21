import functools

@functools.cache
def comp(b1,w1,b2,w2):
  if b1 + w1 < b2 + w2:
    return True
  if b1 + w1 > b2 + w2:
    return False
  return b1 <= b2

@functools.cache
def f(lastb,lastw,nb,nw):
  if nb + nw == 0:
    return 1
  if lastb + lastw > nb + nw:
    return 0
  
  s = 0
  for b in range(nb+1):
    w0 = max(0, lastb + lastw - b)
    for w in range(w0,nw+1):
      if b + w == 0:
        continue
      if comp(lastb, lastw, b, w):
        s += f(b, w, nb - b, nw - w)
  return s

ans = f(0,0,60,40)