from pjeuler import smart_mod

a = []
for i in range(1,2000):
  print(i)
  v = smart_mod(1777,i,100000000)
  a.append(v)