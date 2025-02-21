def generate_pyt_triple(N):
  for x in range(1,N):
      y = x+1
      z = y+1
      while z <= N:
          while z * z < x * x + y * y:
              z = z + 1
          if z * z == x * x + y * y and z <= N:
            yield((x,y))
          y = y + 1

def is_perfect_square(x):
  return round(x**.5)**2 == x

def print_sol(i,j,z):
  print()
  print("Partial solution:")
  y = z + i**2
  x = y + j**2
  print(x," > ",y," > ",z," > 0 ")
  
  if is_perfect_square(x+y):
    print("perfect x+y:",x+y,round((x+y)**.5))
  else:
    print("sad x+y:",x+y)
  
  if is_perfect_square(y+z):
    print("perfect y+z:",y+z,round((y+z)**.5))
  else:
    print("sad y+z:",y+z)
  
  if is_perfect_square(x+z):
    print("perfect x+z:",x+z,round((x+z)**.5))
  else:
    print("sad x+z:",x+z)

def f(N):
  for (i,j) in generate_pyt_triple(N):
    #print("i,j:",i,j)
    for z in range(1,10*i**2):
      d2 = 2*z + i**2
      if is_perfect_square(d2):
        b2 = d2 + j**2
        if is_perfect_square(b2):
          print_sol(i,j,z)
          a2 = b2 + i**2
          if is_perfect_square(a2):
            print_sol(i,j,z)
            return
           
f(2000)
    