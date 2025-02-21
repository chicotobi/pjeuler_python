def f( *args):
  if len(args) == 2:
    return [i for i in args[0] if i in args[1]]
  else:
    return [i for i in args[0] if i in args[1] and i in args[2]]
          
def solve(ss):
  d = {}
  for i  in range(10):
    for j in range(10):
      for k in range(10):
        for l in range(10):
          if i+j+k+l == ss:
            
            if () not in d.keys():
              d[()] = set()
            d[()].add(i)
            
            if i not in d.keys():
              d[i] = set()
            d[i].add(j)
              
            if (i,j) not in d.keys():
              d[(i,j)] = set()
            d[(i,j)].add(k)
            
            if (i,j,k) not in d.keys():
              d[(i,j,k)] = set()
            d[(i,j,k)].add(l)  
            
  d = {k:sorted(list(v)) for (k,v) in d.items()}
  
  s = 0
  for a11 in d[()]:
    for a12 in d[a11]:
      print("ss",ss,"a11",a11,"a12",a12)
      for a13 in d[(a11,a12)]:
        for a14 in d[(a11,a12,a13)]:
          for a21 in d[a11]:
            for a22 in f( d[a12], d[a21], d[a11]):
              for a23 in f( d[a13], d[(a21,a22)], d[a14]):
                for a24 in f( d[a14], d[(a21,a22,a23)]):
                  for a31 in d[(a11,a21)]:
                    for a32 in f( d[(a12,a22)], d[a31], d[(a14,a23)]):
                      for a33 in f( d[(a13,a23)], d[(a31,a32)], d[(a11,a22)]):
                        for a34 in f( d[(a14,a24)], d[(a31,a32,a33)]):
                          for a41 in f( d[(a11,a21,a31)], d[(a14,a23,a32)]):
                            for a42 in f( d[a41], d[(a12,a22,a32)]):
                              for a43 in f( d[(a41,a42)], d[(a13,a23,a33)]):
                                for a44 in f( d[(a41,a42,a43)], d[(a14,a24,a34)], d[(a11,a22,a33)]):
                                  s += 1
                                  
                                  # print(a11,a12,a13,a14)
                                  # print(a21,a22,a23,a24)
                                  # print(a31,a32,a33,a34)
                                  # print(a41,a42,a43,a44)
                                  # print()
                                  
                                  if a11+a12+a13+a14 != ss:
                                    raise                                    
                                  if a21+a22+a23+a24 != ss:
                                    raise                                   
                                  if a31+a32+a33+a34 != ss:
                                    raise                                    
                                  if a41+a42+a43+a44 != ss:
                                    raise
                                                                      
                                  if a11+a21+a31+a41 != ss:
                                    raise                             
                                  if a12+a22+a32+a42 != ss:
                                    raise                                    
                                  if a13+a23+a33+a43 != ss:
                                    raise                             
                                  if a14+a24+a34+a44 != ss:
                                    raise
                                    
                                  if a11 + a22 + a33 + a44 != ss:
                                    raise
                                  if a41 + a32 + a23 + a14 != ss:
                                    raise
                                    
  return s

out = 0
for i in range(37):
  out += solve(i)
print(out)