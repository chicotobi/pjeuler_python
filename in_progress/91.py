n = 0
m = 50
for x1 in range(m+1):
  for y1 in range(m+1):
    for x2 in range(m+1):
      for y2 in range(m+1):
        if x1!=x2 or y1!=y2:
          if x1+y1>0 and x2+y2>0:
            a2 = x1**2+y1**2
            b2 = x2**2+y2**2
            c2 = (x1-x2)**2+(y1-y2)**2
            if a2+b2==c2 or a2+c2==b2 or b2+c2==a2:
              n +=1
n = int(n/2)
print(n)