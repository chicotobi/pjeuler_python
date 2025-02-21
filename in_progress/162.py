from functools import cache

t    = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
rem  = [        '2','3','4','5','6','7','8','9',    'B','C','D','E','F']
        
@cache
def brute(l,has_to_have_0, has_to_have_1, has_to_have_A, has_to_have_no_front_0):
  s = 0
  v = [i for i in t]
  for i in range(l-1):
    v = [j+k for j in v for k in t]
  for i in v:
    keep = True
    if has_to_have_0 and not '0' in i:
      keep = False
    if has_to_have_1 and not '1' in i:
      keep = False
    if has_to_have_A and not 'A' in i:
      keep = False
    if has_to_have_no_front_0 and i[0] == '0':
      keep = False
    if keep:
      s += 1
  return s

@cache
def f(l, has_to_have_0, has_to_have_1, has_to_have_A, has_to_have_no_front_0):
  if l == 3:
    return brute(l, has_to_have_0, has_to_have_1, has_to_have_A, has_to_have_no_front_0)
  sol = 13 * f(l-1, has_to_have_0, has_to_have_1, has_to_have_A, False) + \
    f(l-1, has_to_have_0, False        , has_to_have_A, False) + \
    f(l-1, has_to_have_0, has_to_have_1, False        , False)
  if not has_to_have_no_front_0: 
    sol += f(l-1, False        , has_to_have_1, has_to_have_A, False)      
  return sol    

def g(l):
  return sum(f(i,1,1,1,1) for i in range(3,l + 1))   

print(hex(g(16))[2:].upper())