import itertools

a = list(itertools.combinations(range(12), 6))
  
s = 0
l = [0,1,2,3,4,5,8,0,0,0,0,0]
for i1 in [6,9]:
  l[7] = i1 
  for i2 in range(10):
    l[8] = i2
    for i3 in range(10):
      l[9] = i3
      for i4 in range(10):
        l[10] = i4
        for i5 in range(10):
          l[11] = i4
          for c in a:
            d1 = [l[i] for i in range(12) if i in c]
            d2 = [l[i] for i in range(12) if i not in c]
            #print(d1,d2)
            s += 1
            