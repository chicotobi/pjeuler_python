from functools import cache
from numpy import cumsum

@cache
def get_all_lines(n):
  if n < 2:
    return []
  if n < 4:
    return [[n]]
  x2 = [[2] + i for i in get_all_lines(n-2)]
  x3 = [[3] + i for i in get_all_lines(n-3)]
  return x2 + x3

x = get_all_lines(32)

x2 = [cumsum(i) for i in x]

all_lines = [i[:-1] for i in x2]

all_lines = [tuple(i) for i in all_lines]

@cache
def build_wall(last_line,n):
  if n > 7:
    print(n, build_wall.cache_info())
  if n == 0:
    return 1
  possibilities = 0
  for new_line in all_lines:
    allowed = True
    for i in last_line:
      if i in new_line:
        allowed = False
        break
    if allowed:
      possibilities += build_wall(new_line, n-1)
  return possibilities

sol = build_wall(tuple(),10)
print(sol)