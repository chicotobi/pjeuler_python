v = 60

elements = [(1,60)]

# elements = [(3,180),(2,120),(3,90),(1,60),(3,40),(2,30),(3,20)]


def add_serial(x,y):
  return x+y

def add_parallel(x,y):
  return 1/(1/x+1/y)

p0 = 0
n = 2
values = []
for i in range(2**n):
  comb = int2base(i,2).zfill(n)
  v = 60
  for j in range(n):
    if comb[j]=='1':
      v = add_serial(v)
    else:
      v = add_parallel(v)
  values.append(v)
        

values = sorted(list(set(values)))
