import copy
f = open('d185')

cor = []
d = []
for i in f:
  d.append(i.split(";")[0].rstrip())
  cor.append(int(i.split(";")[1][0]))

def solve(x,cor):
  if max(cor)>len(x[0]):
    return False
  if min(cor)<0:
    return False  
  if len(x[0])==1:
    s = set([i for (i,j) in zip(x,cor) if j==1])
    if len(s)==1:
      return str(s.pop())
    else:
      return False
  for i in range(10):
    if len(x[0]) == 8:
      print("hi")
    cor_new = []
    for (row_x,row_cor) in zip(x,cor):
      if row_x[0]==str(i):
        cor_new.append(row_cor-1)
      else:
        cor_new.append(row_cor)
    x_new = [i[1:] for i in x]
    result = solve(x_new,cor_new)
    if type(result) is str:
      return str(i)+result
    else:
      continue
  return False

solve(d,cor)