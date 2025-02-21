import random

r = list(range(50,29,-1))
h = 100

def get(r):
  s = r[0] + r[20]
  for i in range(20):
    x = ( 2 * h * (r[i] + r[i+1]) - h*h )**.5
    s += x
  return round(s*1000)


r = [50,48,46,44,42,40,38,36,34,32,30,31,33,35,37,39,41,43,45,47,49]
print(r, get(r))

min_length = 1e10
while True:
  res = get(r)
  if res < min_length:
    print(r, res)
    min_length = res
  random.shuffle(r)
  