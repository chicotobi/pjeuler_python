from functools import cache

@cache
def f(top_row, idx = 0, bottom_row = ()):
  if idx == len(top_row):
    return g(bottom_row)
  return sum(f(top_row, idx + 1, bottom_row + (col,)) for col in [i for i in range(3) if i != top_row[idx]])

@cache
def g(bottom_row, idx = 0, top_row = ()):
  if len(bottom_row) == 1:
    return 1
  if idx == len(bottom_row) - 1:
    return f(top_row)
  return sum(g(bottom_row, idx + 1, top_row + (col,)) for col in  [i for i in range(3) if i != bottom_row[idx] and i != bottom_row[idx+1]])

print(f((-1,) * 8))