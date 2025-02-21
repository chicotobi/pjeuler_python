def is_black(N, x, y):
  return (x - 2 ** (N-1)) ** 2 + (y - 2 ** (N-1)) ** 2 <= 2 ** (2*N-2)

def plot(N):
  s = ''
  for i in range(2**N):
    for j in range(2**N):
      if is_black(N,i,j):
        s += '.'
      else:
        s += '#'
    s += '\n'
  print(s)
    
        