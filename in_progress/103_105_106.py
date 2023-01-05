from itertools import chain, combinations
from functools import cache

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

@cache
def is_special(t):
  if len(t) < 3:
    return True

  # Check for disjoints subsets B and C with a maximum of n-1 elements
  for idx in range(len(t)-1,-1,-1):
    t1 = t[:idx] + t[idx+1:]
    if not is_special(t1):
      return False

  # Check for subsets B and C with exactly n elements
  # That means, A = B + C and B intersect C = {}
  for t1 in powerset(t):
    if len(t1)==0 or len(t1)==len(t):
      continue
    s0 = set(t)
    s1 = set(t1)
    s2 = s0.difference(s1)
    if sum(s1) == sum(s2):
      return False
    if len(s1) > len(s2) and sum(s1)<=sum(s2):
      return False
  return True

@cache
def all_special_sets(suma,n):
  s = set()
  if n==1:
    t = tuple([suma])
    s.add(t)
    return s
  for x in range(suma):
    for t0 in all_special_sets(suma-x, n-1):
      if x not in t0:
        t1 = tuple(sorted(t0+tuple([x])))
        if is_special(t1):
          s.add(t1)
  return s

def pjeuler103():
  suma = 0
  while True:
    res = all_special_sets(suma, 7)
    if len(res) > 0:
      break
    suma += 1
  return int(''.join(str(i) for i in list(res)[0]))

def pjeuler105():
  d = [i.split(',') for i in open('../pjeuler/input/105').read().splitlines()]
  d = [tuple(int(k) for k in i) for i in d]

  s = 0
  for i in d:
    if is_special(i):
      s += sum(i)
  return s