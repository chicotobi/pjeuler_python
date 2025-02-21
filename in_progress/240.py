s = 0
for d1 in range(1,7):
  for d2 in range(1,7):
    for d3 in range(1,7):
      for d4 in range(1,7):
        for d5 in range(1,7):
          l = [d1,d2,d3,d4,d5]
          x = sorted([d1,d2,d3,d4,d5])[-3:]
          if sum(x) == 15:
            #print(l)
            s += 1
print(s)