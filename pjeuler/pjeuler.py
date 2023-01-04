import math
import functools
from functools import cache
import itertools
import collections
import numpy as np
import pandas as pd
import sympy
import scipy

def pjeuler(i):
  return eval("pjeuler"+str(i)+"()")

def get(i):
  import os.path
  if '__file__' in globals():
    return open(os.path.dirname(__file__)+'/input/'+str(i))
  else:
    from pathlib import Path
    home = str(Path.home())
    return open(home+'/pjeuler_python/pjeuler/input/'+str(i))

def my_hash(n):
  import hashlib
  return hashlib.md5(str(n).encode('utf-8')).hexdigest()

def pjeuler1():
  val = 0
  for i in range(1000):
    if i%3 == 0 or i%5 == 0:
      val += i
  return val

def pjeuler2():
  from .tools import fib
  arr = np.array(fib(40))
  arr = arr[arr%2==0]
  return sum(arr[arr<4e6])

def pjeuler3():
  from .tools import factors
  return factors(600851475143)[-1]

def pjeuler4():
  from .tools import is_palindrome
  n = 0
  for i in range(900,1000):
    for j in range(900,1000):
      k = i*j
      if is_palindrome(k) and k>n:
        n = k
  return n

def pjeuler5():
  from .tools import lcm
  return lcm(range(1,21))

def pjeuler6():
  return sum(range(101))**2-sum([i**2 for i in range(101)])

def pjeuler7():
  from .tools import primes
  return list(primes(110000))[10000]

def pjeuler8():
  from .tools import digits
  f = get(8)
  a = digits(f.read())
  f.close()
  m = lambda a,b: a*b
  return max([functools.reduce(m,a[i:i+13]) for i in range(len(a)-13)])

def pjeuler9():
  from .tools import gcd
  get_a = lambda k,m,n: k*(m**2-n**2)
  get_b = lambda k,m,n: 2*k*m*n
  get_c = lambda k,m,n: k*(m**2+n**2)
  for k in range(1,50):
      for m in range(1,50):
          for n in range(1,m):
              a = get_a(k,m,n)
              b = get_b(k,m,n)
              c = get_c(k,m,n)
              if a+b+c==1000 and gcd(m,n)==1:
                  return a*b*c

def pjeuler10():
  from .tools import primes
  return sum(list(primes(2000000)))

def pjeuler11():
  arr = np.zeros((20,20),dtype="uint8")
  f = get(11)
  for (i,line) in enumerate(f):
    for (j,val) in enumerate(str.split(line)):
      arr[i,j] = int(val)
  f.close()
  val = 0
  for i in range(20):
    for j in range(20):
      if i < 17:
        val = max(val,np.prod(arr[i:i+4,j]))
      if j < 17:
        val = max(val,np.prod(arr[i,j:j+4]))
      if i < 17 and j < 17:
        val = max(val,np.prod(arr[(range(i,i+4),range(j,j+4))]))
        val = max(val,np.prod(arr[(range(i,i+4),range(j+3,j-1,-1))]))
  return val

def pjeuler12():
  from .tools import triangle_numbers, n_divs
  for t in triangle_numbers():
    if n_divs(t)>500:
      return t

def pjeuler13():
  v = 0
  f = get(13)
  for line in f:
    v += int(line)
  f.close()
  return int(str(v)[:10])

def pjeuler14():
  from .tools import collatz
  n = 1000000
  l = [0]*(n+1)
  l[1]=1
  for i in range(2,n+1):
    v = i
    j = 0
    while True:
      if v==1 or (v < n+1 and l[v]!=0):
        j += l[v]
        break
      v = collatz(v)
      j += 1
    l[i]=j
  return l.index(max(l))

def pjeuler15():
  from .tools import nchoosek
  return nchoosek(40,20)

def pjeuler16():
  from .tools import digits
  return sum(digits(str(2**1000)))

def pjeuler17():
  from .tools import num2word
  sum = 0
  for i in range(1,1001):
      s = num2word(i).replace('-','').replace(' ','')
      sum += len(s)
  return sum

def pjeuler18():
  n = 15
  a = np.zeros((n,n),dtype="uint32")
  f = get(18)
  for (i,line) in enumerate(f):
    for (j,val) in enumerate(str.split(line,sep=" ")):
      a[i,j] = int(val)
  f.close()
  @cache
  def f(i,j):
    if i==n-1:
      return a[i,j]
    else:
      return a[i,j] + max(f(i+1,j),f(i+1,j+1))
  return f(0,0)

def pjeuler19():
  c = 0
  v = 0
  for y in range(1900,2001):
    m = [31,28,31,30,31,30,31,31,30,31,30,31]
    if y%4==0:
      m[1] += 1
      if y%100==0:
        m[1] -= 1
        if y%400==0:
          m[1] += 1
    for mo in m:
      v = (v+mo)%7
      if v==6 and y>1900:
        c +=1
  return c

def pjeuler20():
  from .tools import digits_int
  return sum(digits_int(math.factorial(100)))

def pjeuler21():
  from .tools import sum_divs
  s = 0
  for i in range(2,10000):
    j = sum_divs(i)
    if i<j and sum_divs(j)==i:
      s += i+j
  return int(s)

def pjeuler22():
  from .tools import lettervalue
  s = get(22)
  t = [i for i in s][0].replace('"','').split(",")
  s.close()
  t.sort()
  s = 0
  for (i,j) in enumerate(t):
    s += (i+1) * lettervalue(j)
  return s

def pjeuler23():
  from .tools import sum_divs
  l = []
  n = 28124
  l2 = [0]*n
  for i in range(2,n):
    if sum_divs(i)>i:
      l = l+[i]
      for j in l:
        k = i + j
        if k<n:
          l2[k] = 1
  return sum([i for i,j in enumerate(l2) if j==0])

def pjeuler24():
  symbols = [0,1,2,3,4,5,6,7,8,9]
  n = len(symbols)
  k = 1000000-1
  s = 0
  for i in range(n):
    x = math.factorial(n-i-1)
    idx = k//x
    s = 10*s + symbols[idx]
    symbols.remove(symbols[idx])
    k = k%x
  return s

def pjeuler25():
  from .tools import fib2
  for (i,j) in enumerate(fib2()):
    if math.log10(j)>999:
      return i+1

def pjeuler26():
  from .tools import periodic_decimal, primes
  d = {p: len(periodic_decimal(p)) for p in primes(1000)}
  return max(d, key=d.get)

def pjeuler27():
  from .tools import primes
  def f(a,b,n):
    return n**2+a*n+b
  p = list(primes(1000))
  s = set(primes(100000))
  best = 0
  prod = 0
  for a in range(-1000,1000):
    for b in p:
      for n in range(1,1000):
        if f(a,b,n) not in s:
          break
      if n>best:
        best = n
        prod = a*b
  return prod

def pjeuler28():
  n = 500
  return int((16*n**3 + 30*n**2 + 26*n + 3)/3)

def pjeuler29():
  l = []
  for a in range(2,101):
    for b in range(2,101):
      l = l + [a**b]
  return len(set(l))

def pjeuler30():
  from .tools import digits_int
  n = 6*9**5
  s = 0
  for i in range(2,n):
    if i == sum([k**5 for k in digits_int(i)]):
      s += i
  return s

def pjeuler31():
  l = [1,2,5,10,20,50,100,200]
  @cache
  def split(s,min_size):
    c = 0
    l2 = [i for i in l if min_size<=i]
    for i in l2:
      if s-i>=min_size:
        c += split(s-i,i)
    if s in l2:
      c += 1
    return c
  return split(200,0)

def pjeuler32():
  from .tools import digits_int
  x = set(range(1,10))
  s = []
  for a in range(1,10000):
    n = math.ceil(math.log10(a))
    max_b = round(min(a,10**(8-n), 10**(9-2*n)))
    for b in range(max_b):
      y = digits_int(a)+digits_int(b)+digits_int(a*b)
      if len(y)==9 and set(y)==x:
        s += [a*b]
  return sum(set(s))

def pjeuler33():
  from .tools import digits_int, gcd
  big_a = 1
  big_b = 1
  for a in range(10,100):
    for b in range(a+1,100):
      x = a/b
      l1 = digits_int(a)
      l2 = digits_int(b)
      common = set([x for x in l1 if x in l2])
      for c in common:
        if c==0:
          continue
        l1 = list(digits_int(a))
        l2 = list(digits_int(b))
        l1.remove(c)
        l2.remove(c)
        new_a = l1[0]
        new_b = l2[0]
        if new_b != 0:
          y = new_a/new_b
          if abs(x-y)<1e-3:
            big_a *= a
            big_b *= b
  return big_b // gcd(big_a,big_b)

def pjeuler34():
  from .tools import digits_int
  @cache
  def f(n):
    return math.factorial(n)
  s = 0
  for i in range(10,7*f(9)):
    if i == sum([f(j) for j in digits_int(i)]):
      s += i
  return s

def pjeuler35():
  from .tools import primes
  l = list(primes(1000000))
  def get_rotation(x):
    k = math.floor(math.log10(x))
    for i in range(k):
      x = x//10 + 10**k * (x%10)
      yield x
  n = 0
  s = set(l)
  for i in l:
    if all([j in s for j in get_rotation(i)]):
      n+=1
  return n

def pjeuler36():
  from .tools import is_palindrome, int2base
  return sum([i for i in range(1000000) if (is_palindrome(i) and is_palindrome(int2base(i,2)))])

def pjeuler37():
  from .tools import primes
  l = list(primes(1000000))
  s = set(l)
  def left_trunc(x):
    while x>9:
      k = math.floor(math.log10(x))
      x = x%(10**k)
      yield x
  def right_trunc(x):
    while x>9:
      x = x//10
      yield x
  n = 0
  for i in s:
    if i>7 and all([i in s for i in left_trunc(i)]) and all([i in s for i in right_trunc(i)]):
      n += i
  return n

def pjeuler38():
  from .tools import digits
  s0 = set([1,2,3,4,5,6,7,8,9])
  m = 0
  for n in range(2,6):
    for i in range(1,10**math.ceil(9/n)):
      s = "".join(str(i*j) for j in range(1,n+1))
      if len(s)==9 and set(digits(s))==s0:
        m = max(m,int(s))
  return m

def pjeuler39():
  from .tools import gcd
  get_a = lambda k,m,n: k*(m**2-n**2)
  get_b = lambda k,m,n: 2*k*m*n
  get_c = lambda k,m,n: k*(m**2+n**2)
  l = [0]*1000
  for k in range(1,50):
      for m in range(1,50):
          for n in range(1,m):
              a = get_a(k,m,n)
              b = get_b(k,m,n)
              c = get_c(k,m,n)
              p = a+b+c
              if gcd(m,n)==1 and p<1000:
                l[p] += 1
  return [i for (i,j) in enumerate(l) if j==max(l)][0]

def pjeuler40():
  s = ''
  for i in range(1,185186):
      s += str(i)
  return np.prod([int(s[10**i-1]) for i in range(6)])

def pjeuler41():
  from .tools import digits_int, primes
  def is_pandigital(x):
    y = digits_int(x)
    return max(collections.Counter(y).values())==1 and max(y)==len(y)
  s = set(primes(10000000))
  s2 = [i for i in s if is_pandigital(i)]
  return max(s2)

def pjeuler42():
  from .tools import lettervalue, triangle_numbers
  f = get(42)
  s = [i for i in f][0].replace('"','').split(",")
  x = [lettervalue(i) for i in s]
  f.close()
  t = []
  for i in triangle_numbers():
    t += [i]
    if i>192:
      break
  return len([i for i in x if i in t])

def pjeuler43():
  from .tools import digits2int
  s = 0
  for i in itertools.permutations(range(10)):
    if digits2int(i[7:10])%17==0:
      if digits2int(i[6:9])%13==0:
        if digits2int(i[5:8])%11==0:
          if digits2int(i[4:7])%7==0:
            if digits2int(i[3:6])%5==0:
              if digits2int(i[2:5])%3==0:
                if digits2int(i[1:4])%2==0:
                  s += digits2int(i)
  return s

def pjeuler44():
  min_distance = 1e10
  l = []
  for i in range(1,5000):
    l = l + [i*(3*i-1)//2]
  s = set(l)
  for i in range(len(l)):
    if 2*l[i]>l[-1]:
      break
    for j in range(i):
      li=l[i]
      lj=l[j]
      if li-lj<min_distance and li-lj in s and li+lj in s:
        min_distance=li-lj
  return min_distance

def pjeuler45():
  from .tools import hexagonal_numbers, is_pentagonal, is_triangle
  for i in hexagonal_numbers():
    if i>40755 and is_pentagonal(i) and is_triangle(i):
      return i

def pjeuler46():
  from .tools import primes
  n = 10000
  ps = set(primes(n))
  for i in range(1,n):
    j = 2*i+1
    if j not in ps:
      found = False
      for p in ps:
        lim = math.ceil(((n - p)/2)**.5)
        for k in range(lim):
          if p+2*k**2==j:
            found = True
            break
        if found:
          break
      if not found:
        return 2*i+1

def pjeuler47():
  from .tools import factors
  run = 0
  for i in range(2,1000000):
    if len(collections.Counter(factors(i)))==4:
      run+=1
    else:
      run=0
    if run==4:
      return i-3

def pjeuler48():
  n = int(1e10)
  s = 0
  for i in range(1,1001):
    k = 1
    for j in range(i):
      k = (k*i)%n
    s = (s+k)%n
  return s

def pjeuler49():
  from .tools import primes, digits_int
  d = 3330
  s = set(primes(10000))
  for i in range(1000,10000-2*d):
    n1 = i
    n2 = i+d
    n3 = i+2*d
    if n1!=1487 and n1 in s and n2 in s and n3 in s:
      l1 = digits_int(n1)
      l1.sort()
      l2 = digits_int(n2)
      l2.sort()
      l3 = digits_int(n3)
      l3.sort()
      if l1==l2 and l1==l3:
        break
  return n1*int(1e8)+n2*int(1e4)+n3

def pjeuler50():
  from .tools import primes
  m = 1000000
  l = list(primes(m))
  s = set(l)
  for n in range(22,1000):
    found = False
    for i in range(len(l)-n):
      if l[i]*n < m:
        x = sum(l[i:i+n])
        if x < m and x in s:
          found = True
          break
    if found:
      max_x = x
  return max_x

def pjeuler51():
  from .tools import primes
  ps = list(primes(1000000))
  s = set(ps)
  for p in ps:
    strp = str(p)
    for digit in range(10):
        if str(digit) in strp:
            counter = 1
            for d2 in range(digit+1,10):
                new_p = int(strp.replace(str(digit),str(d2)))
                if new_p in s:
                    counter += 1
            if counter==8:
              return p

def pjeuler52():
  from .tools import digits_int
  for i in range(1,1000000):
    d1 = digits_int(i)
    d1.sort()
    d2 = digits_int(2*i)
    d2.sort()
    if d1==d2:
      d3 = digits_int(3*i)
      d3.sort()
      d4 = digits_int(4*i)
      d4.sort()
      d5 = digits_int(5*i)
      d5.sort()
      d6 = digits_int(6*i)
      d6.sort()
      if d1==d3 and d1==d4 and d1==d5 and d1==d6:
        break
  return i

def pjeuler53():
  from .tools import nchoosek
  i = 0
  for n in range(1,101):
    for k in range(1,n):
      if nchoosek(n,k)>1e6:
        i+=1
  return i

def pjeuler54():
  def is_royal_flush(ranks, suits):
      if is_straight(ranks, suits) and is_flush(ranks, suits) and ranks[0] == 10:
          return 10e6
      return 0
  def is_straight_flush(ranks, suits):
      if is_straight(ranks, suits) and is_flush(ranks, suits):
          return 9e6
      return 0
  def is_four(ranks, suits):
      x = collections.Counter(ranks).most_common(2)
      if x[0][1] == 4:
          return 8e6
      return 0
  def is_full_house(ranks, suits):
      x = collections.Counter(ranks).most_common(2)
      if x[0][1] == 3 and x[1][1] == 2:
          return 7e6 + x[0][0]*15 + x[1][0]
      return 0
  def is_flush(ranks, suits):
      if suits[0] == suits[1] and suits[0] == suits[2] and suits[0] == suits[3] and suits[0] == suits[4]:
          ranks.sort()
          return 6e6 + ranks[4] * 15 ** 4 + ranks[3] * 15 ** 3 + ranks[2] * 15 ** 2 + ranks[1] * 15 * ranks[0]
      return 0
  def is_straight(ranks, suits):
      x = collections.Counter(ranks).most_common(5)
      if x[0][1]==1 and ranks[4] - ranks[0] == 4:
          return 5e6 + ranks[0]
      return 0
  def is_three(ranks, suits):
      x = collections.Counter(ranks).most_common(5)
      if x[0][1] == 3:
          tmp = [x[1][0], x[2][0]]
          tmp.sort()
          return 4e6 + x[0][0] * 15 ** 2 + tmp[1] * 15 + tmp[0]
      return 0
  def is_two_pair(ranks, suits):
      global value
      x = collections.Counter(ranks).most_common(5)
      if x[0][1] == 2 and x[1][1] == 2:
          tmp = [x[0][0], x[1][0]]
          tmp.sort()
          return 3e6 + tmp[1] * 15 ** 2 + tmp[0] * 15 + x[2][0]
      return 0
  def is_one_pair(ranks, suits):
      global value
      x = collections.Counter(ranks).most_common(5)
      if x[0][1] == 2:
          tmp = [x[1][0], x[2][0], x[3][0]]
          tmp.sort()
          return 2e6 + x[0][0] * 15 ** 3 + tmp[2] * 15**2 + tmp[1] * 15 + tmp[0]
      return 0
  def is_high_card(ranks, suits):
      global value
      x = collections.Counter(ranks).most_common(5)
      if x[0][1] == 1:
          return 1e6 + ranks[4] * 15 ** 4 + ranks[3] * 15 ** 3 + ranks[2] * 15 ** 2 + ranks[1] * 15 + ranks[0]
      return 0
  def hand_to_rankssuits(hand):
      ranks = [
          10 if card[0] == 'T' else 11 if card[0] == 'J' else 12 if card[0] == 'Q' else 13 if card[0] == 'K' else 14 if
          card[0] == 'A' else int(card[0]) for card in hand]
      suits = [card[1] for card in hand]
      return ranks, suits
  def eval_hand(hand):
      ranks, suits = hand_to_rankssuits(hand)
      ranks.sort()
      functions = [is_royal_flush, is_straight_flush, is_four, is_full_house, is_flush,
                   is_straight, is_three, is_two_pair, is_one_pair, is_high_card]
      for f in functions:
        value = f(ranks, suits)
        if value>0:
          break
      return value
  f = get(54)
  wins = 0
  for both_hands in f.readlines():
      hand1 = both_hands.rstrip().split(' ')[:5]
      hand2 = both_hands.rstrip().split(' ')[5:]
      val1 = eval_hand(hand1)
      val2 = eval_hand(hand2)
      if val1 > val2:
          wins += 1
  f.close()
  return wins

def pjeuler55():
  n = 0
  for i in range(10000):
      lychrel = True
      val = i
      for counter in range(51):
          str_val = str(val)
          rev = str_val[::-1]
          if rev == str_val and counter>0:
              lychrel = False
              break
          val += int(rev)
      if lychrel:
          n += 1
  return n

def pjeuler56():
  from .tools import digits_int
  return max([sum(digits_int(a**b)) for a in range(101) for b in range(101)])

def pjeuler57():
  num = 1
  den = 2
  n = 0
  for i in range(1000):
      (num,den) = (den, num+2*den)
      if len(str(num+den)) > len(str(den)):
          n += 1
  return n

def pjeuler58():
  from .tools import is_prime
  n_primes = 0
  i = 0
  while True:
    i += 1
    base = 4*i**2-2*i+1
    n_primes += sum([is_prime(base+2*j*i) for j in range(4)])
    ratio = n_primes/(1+4*i)
    if ratio<0.1:
        break
  return 2*i+1

def pjeuler59():
  f = get(59)
  arr = [int(a) for a in f.readlines()[0].split(',')]
  f.close()

  k1 = np.bitwise_xor(32,collections.Counter(arr[0::3]).most_common(1)[0][0])
  k2 = np.bitwise_xor(32,collections.Counter(arr[1::3]).most_common(1)[0][0])
  k3 = np.bitwise_xor(32,collections.Counter(arr[2::3]).most_common(1)[0][0])
  my_key = [k1,k2,k3]*(len(arr)//3)

  return sum([x^y for(x,y) in zip(arr,my_key)])

def pjeuler60():
  from .tools import primes, is_prime_mr
  ps = list(primes(9000))

  di = {p: [] for p in ps}
  for p1 in ps:
   for p2 in ps:
    if p1<p2:
      if is_prime_mr(int(str(p1)+str(p2))) and is_prime_mr(int(str(p2)+str(p1))):
        di[p1] += [p2]
        di[p2] += [p1]

  s = 1e10
  for (k1,v1) in di.items():
    for k2 in v1:
      v2 = di[k2]
      for k3 in v2:
        v3 = di[k3]
        if k3 in v1:
          for k4 in v3:
            v4 = di[k4]
            if k4 in v1 and k4 in v2:
              for k5 in v4:
                if k5 in v1 and k5 in v2 and k5 in v3:
                  s = min(s,k1+k2+k3+k4+k5)
  return s

def pjeuler61():
  a3 = [i*(1*i+1)//2 for i in range(200)]
  a4 = [i*(2*i-0)//2 for i in range(200)]
  a5 = [i*(3*i-1)//2 for i in range(200)]
  a6 = [i*(4*i-2)//2 for i in range(200)]
  a7 = [i*(5*i-3)//2 for i in range(200)]
  a8 = [i*(6*i-4)//2 for i in range(200)]

  a3 = [i for i in a3 if 1000<=i<=9999]
  a4 = [i for i in a4 if 1000<=i<=9999]
  a5 = [i for i in a5 if 1000<=i<=9999]
  a6 = [i for i in a6 if 1000<=i<=9999]
  a7 = [i for i in a7 if 1000<=i<=9999]
  a8 = [i for i in a8 if 1000<=i<=9999]

  a = [a4,a5,a6,a7,a8]
  for p in itertools.permutations(range(5)):
      for n1 in a3:
          r1 = n1 % 100
          for n2 in a[p[0]]:
              if n2//100 == r1:
                  r2 = n2 % 100
                  for n3 in a[p[1]]:
                      if n3//100 == r2:
                          r3 = n3 % 100
                          for n4 in a[p[2]]:
                              if n4//100 == r3:
                                  r4 = n4 % 100
                                  for n5 in a[p[3]]:
                                      if n5//100 == r4:
                                          r5 = n5 % 100
                                          for n6 in a[p[4]]:
                                              if n6//100 == r5:
                                                  r6 = n6 % 100
                                                  if n1//100 == r6:
                                                      return n1+n2+n3+n4+n5+n6

def pjeuler62():
  d = {}
  for i in range(100000):
    val = i**3
    s = ''.join(sorted(str(val)))
    if s not in d:
      d[s] = []
    d[s].append(val)
  return min(functools.reduce(lambda x,y:x+y,[v for (k,v) in d.items() if len(v)==5]))

def pjeuler63():
  return sum([b==len(str(a**b)) for a in range(1,30) for b in range(1,30)])

def pjeuler64():
  from .tools import continued_fraction
  return sum([1 for i in range(10000) if continued_fraction(i,get_period=True)%2])

def pjeuler65():
  from .tools import digits_int, eval_continued_fraction_vector
  N = 100
  v = [2] + [1 if i%3 else round(i*2/3) for i in range(2,N+1)]
  return sum(digits_int(eval_continued_fraction_vector(v)[0]))

def pjeuler66():
  from .tools import continued_fraction,eval_continued_fraction_vector
  di = {}
  for D in range(1000):
    if round(D**.5)**2 == D:
      di[D] = D
    else:
      j = 0
      while True:
        j +=1
        v = continued_fraction(D, m=j)
        x, y = eval_continued_fraction_vector(v)
        if x**2-D*y**2==1:
          di[D] = x
          break
  return max(di,key=di.get)

def pjeuler67():
  n = 100
  a = np.zeros((n,n),dtype="uint32")
  f = get(67)
  for (i,line) in enumerate(f):
    for (j,val) in enumerate(str.split(line,sep=" ")):
      a[i,j] = int(val)
  f.close()
  @cache
  def f(i,j):
    if i==n-1:
      return a[i,j]
    else:
      return a[i,j] + max(f(i+1,j),f(i+1,j+1))
  return f(0,0)

def pjeuler68():
  m = 0
  for p in itertools.permutations(range(1,11)):
    if p[0]<min(p[1:5]):
      s1 = p[0]+p[5]+p[6]
      s2 = p[1]+p[6]+p[7]
      s3 = p[2]+p[7]+p[8]
      s4 = p[3]+p[8]+p[9]
      s5 = p[4]+p[9]+p[5]
      if s1==s2==s3==s4==s5:
        s = ''.join(str(p[i]) for i in (0,5,6,1,6,7,2,7,8,3,8,9,4,9,5))
        if len(s)==16:
          m = max(m,int(s))
  return m

def pjeuler69():
  from .tools import primes
  s = 1
  for i in primes(100):
    if s*i<1000000:
      s *= i
  return s

def pjeuler70():
  from .tools import primes
  N = int(1e7)
  ps = list(primes(4000))
  smallps = [i for i in ps if 2000<i]
  min_quotient=2
  for i in smallps:
    for j in smallps:
      if i*j<N:
        if ''.join(sorted(str(i*j))) == ''.join(sorted(str((i-1)*(j-1)))):
          if i*j/(i-1)/(j-1) < min_quotient:
            min_idx = i*j
            min_quotient = i*j/(i-1)/(j-1)
  return min_idx

def pjeuler71():
  x = 3/7
  y = 0
  for d in range(1,1000000):
    if d%7!=0:
      n = math.floor(x * d)
      if n/d > y:
        y = n/d
        best_n = n
  return best_n

def pjeuler72():
  from .tools import primes
  N = int(1e6)
  a = list(range(N+1))
  for p in primes(N):
    for i in range(math.ceil(N/p)+1):
      if i*p<N+1:
        a[i*p] = a[i*p] * (p-1) // p
  return sum(a[2:])

def pjeuler73():
  N = int(12000)
  a = list(range(4,N+1))
  counter = 0
  for d in a:
    n1 = math.ceil(d/3)
    n2 = math.floor(d/2)
    for n in range(n1,n2+1):
      if math.gcd(n,d)==1:
        counter += 1
  return counter

def pjeuler74():
  import pjeuler, math
  fac = [math.factorial(i) for i in range(10)]

  @cache
  def f(x):
    return sum([fac[i] for i in pjeuler.digits_int(x)])

  @cache
  def g(x0):
    x1 = f(x0)
    x2 = f(x1)
    if x0==x2:
      return 2
    x3 = f(x2)
    if x0==x3:
      return 3
    return g(x1)+1

  n = 0
  for i in range(int(1e6)):
    if g(i)==60:
      n += 1
  return n

def pjeuler75():
  N = 1500000
  l = [0]*(N+1)
  k_max = N//2
  for k in range(1,k_max+1):
    m_max = math.floor((N//(2*k))**.5)
    for m in range(1,m_max+1):
      n_max = min(m,N//(2*k*m) - m)
      for n in range(1,n_max+1):
        s = 2*k*m*(m+n)
        if s<=N:
          if (m*n)%2==0:
            if math.gcd(m,n)==1:
              l[s] +=1
  return sum([1 for (idx,i) in enumerate(l) if i==1])

def pjeuler76():
  @cache
  def split(number,min_size):
    c = 0
    for i in range(min_size,number-min_size+1):
      c += split(number-i,i)
    if min_size<=number:
      c += 1
    return c
  return split(100,1)-1

def pjeuler77():
  from .tools import write_as_prime_sum
  i = 2
  while write_as_prime_sum([],i,i)<=5000:
    i += 1
  return i

def pjeuler78():
  @cache
  def p(n):
    if n<0:
      return 0
    if n<=1:
      return 1
    k = 1
    x = 0
    k_min = math.floor(-((24*n+1)**.5-1)/6)
    k_max = math.ceil(((24*n+1)**.5+1)/6)+1
    for k in range(k_min,k_max):
      if k==0:
        continue
      idx = k*(3*k-1)//2
      val = p(n-idx)
      if k%2==0:
        x -= val
      else:
        x += val
    return x
  i = 0
  while True:
    i += 1
    x = p(i)
    if x%1000000==0:
      break
  return i

def pjeuler79():
  f = get(79)
  d = [i.strip() for i in f.readlines()]
  f.close()

  key = 0
  while True:
    for c in range(10):
      flag = False
      for row in d:
        if row[0]==str(c):
          flag = True
        if str(c) in row[1:]:
          flag = False
          break
      if flag:
        key = 10*key+c
        d = [d[i][1:] if d[i][0]==str(c) else d[i] for i in range(len(d))]
        d = [i for i in d if len(i)>0]
        if len(d)==0:
          return key

def pjeuler80():
  import mpmath
  from .tools import digits
  mpmath.mp.dps = 102
  s = 0
  for i in range(2,101):
    if round(i**.5)**2 != i:
      s += sum(digits(str(mpmath.mp.sqrt(i)).replace(".","")[:100]))
  return s

def pjeuler81():
  a = np.zeros((80,80),dtype="uint32")
  f = get(81)
  for (i,line) in enumerate(f):
    for (j,val) in enumerate(str.split(line,sep=",")):
     a[i,j] = int(val)
  f.close()
  @cache
  def f(i,j):
    if i==0 and j==0:
      v = 0
    elif i==0:
      v = f(i,j-1)
    elif j==0:
      v = f(i-1,j)
    else:
      v = min(f(i-1,j),f(i,j-1))
    return v+a[i,j]
  return f(79,79)

def pjeuler82():
  n = 80
  a = np.zeros((n,n),dtype="uint32")
  f = get(82)
  for (i,line) in enumerate(f):
    for (j,val) in enumerate(str.split(line,sep=",")):
      a[i,j] = int(val)
  f.close()
  @cache
  def f(i,j,l1,l2):
    if j==0:
      return a[i,0]
    # up
    if i>0 and l1!="down":
      v_up = f(i-1,j,"up",l1)
    else:
      v_up = math.inf
    # down
    if i<n-1 and l2!="up":
      v_down = f(i+1,j,"down",l1)
    else:
      v_down = math.inf
    # left
    if j>0:
      v_left = f(i,j-1,"left",l1)
    else:
      v_left = math.inf
    result = a[i,j] + min(v_up,v_down,v_left)
    return result

  for j in range(n):
    vv = math.inf
    for i in range(n):
      vv = min(vv,f(i,j,"left","left"))
  return vv

def pjeuler83():
  import scipy.sparse.csgraph
  n = 80
  a = np.zeros((80,80),dtype="uint32")
  f = get(83)
  for (i,line) in enumerate(f):
      for (j,val) in enumerate(str.split(line,sep=",")):
          a[i,j] = int(val)
  f.close()

  def idx(i,j):
      return i*n+j

  edge = 0
  b = np.zeros((np.prod(a.shape),np.prod(a.shape)))
  for i in range(n):
      for j in range(n):
          idx1 = idx(i,j)
          val1 = a[i,j]
          if i<a.shape[0]-1:
              idx2 = idx(i+1,j)
              val2 = a[i+1,j]
              b[idx1,idx2] = (val1+val2)/2
              b[idx2,idx1] = (val1+val2)/2
              edge +=1
          if j<a.shape[0]-1:
              idx2 = idx(i,j+1)
              val2 = a[i,j+1]
              b[idx1,idx2] = (val1+val2)/2
              b[idx2,idx1] = (val1+val2)/2
              edge +=1

  s = a[0,0]/2 + a[n-1,n-1]/2

  result = scipy.sparse.csgraph.dijkstra(b,indices=0)
  return result[n*n-1]+s

def pjeuler84():
  import numpy as np

  def f(field,doubles):
    return 40*doubles+field

  n = 4
  p = 1/n**2
  jail = 10

  # Dice matrix
  a = np.zeros((120,120))
  for i in range(40):
    for j in range(1,n+1):
      for k in range(1,n+1):
        idx = (i+j+k)%40
        if idx==30:
          if j!=k:
            a[f(i,0),f(jail,0)] += p
            a[f(i,1),f(jail,0)] += p
            a[f(i,2),f(jail,0)] += p
          else:
            a[f(i,0),f(jail,1)] += p
            a[f(i,1),f(jail,2)] += p
            a[f(i,2),f(jail,0)] += p
        else:
          if j!=k:
            a[f(i,0),f(idx,0)] += p
            a[f(i,1),f(idx,0)] += p
            a[f(i,2),f(idx,0)] += p
          else:
            a[f(i,0),f(idx,1)] += p
            a[f(i,1),f(idx,2)] += p
            a[f(i,2),f(jail,0)]  += p
  a = a.transpose()

  # Card matrix
  b = np.zeros((40,40))
  for i in range(40):
    if i in [2,17,33]:
      #CC
      b[i,i] += 14/16
      b[i,0] += 1/16
      b[i,10] += 1/16
    elif i in [7,22,36]:
      #CH
      b[i,i] += 6/16
      b[i,0] += 1/16
      b[i,10] += 1/16
      b[i,11] += 1/16
      b[i,24] += 1/16
      b[i,39] += 1/16
      b[i,5] += 1/16
      if i==7:
        b[i,15] += 2/16
        b[i,12] += 1/16
      elif i==22:
        b[i,25] += 2/16
        b[i,28] += 1/16
      elif i==36:
        b[i,5] += 2/16
        b[i,12] += 1/16
      b[i,(i-3)] += 1/16
    else:
      b[i,i] += 1
  b = b.transpose()

  # B as block matrix
  z = np.zeros((40,40))
  b = np.block([
    [b,z,z],
    [z,b,z],
    [z,z,b]
  ])

  # Build game matrix
  c = b.dot(a)

  # Eigen decomposition
  w,v = np.linalg.eig(c)
  x = abs(v[:,0])
  x /= sum(x)
  y = [x[i]+x[i+40]+x[i+80] for i in range(40)]
  di = {k:v for (k,v) in enumerate(list(y))}
  top = sorted(di.items(),key=lambda i:-i[1])
  return 10000*top[0][0] + 100*top[1][0] + top[2][0]

def pjeuler85():
  f = lambda a,b: a*(a+1)*b*(b+1)/4
  for i in range(100):
    for j in range(100):
        if(abs(f(i,j)-2000000)<1e3):
            return i*j

def pjeuler86():
  low = 100
  high = 2000

  while True:
    s = 0
    M = round(0.5*(low+high))
    for m in range(1,M):
        for n in range(1,m):
            if math.gcd(m,n)==1 and (m*n)%2==0:
                kmax = M//(m*n)+1
                for k in range(kmax+1):
                    n1 = k * (m**2-n**2)
                    n2 = 2*k*m*n
                    if n1>n2:
                        v = n2-(n1-1)//2
                        if n2 <= M and v>0:
                            s += v
                        v = n2//2
                        if n1 <= M:
                            s += v
                    if n2>n1:
                        if n2 <= M:
                            s += n1//2
                        v = n1-(n2-1)//2
                        if n1 <= M and v>0:
                            s += v
                    if n2==n1:
                        if n2 <= M:
                            s += (n1+n2)//2
    if s<1e6:
      low = M
    else:
      high = M
    if low+1 == high:
      break
  return high

def pjeuler87():
  from .tools import primes
  N = 50000000
  l = list(primes(math.floor(N**.5)))
  a = [False]*N
  for p2 in l:
    s = p2**2
    for p3 in l:
      t = s + p3**3
      if t<N:
        for p4 in l:
          u = t + p4**4
          if u<N:
            a[u] = True
  return sum(a)

def pjeuler88():
  import sympy.utilities.iterables

  def primes(limit):
      a = [True] * (limit+1)
      a[0] = a[1] = False
      for (i, isprime) in enumerate(a):
          if isprime:
              yield i
              for n in range(i*i, limit+1, i):
                  a[n] = False

  @cache
  def factors(m):
    if m in sps:
      return [int(m)]
    for p in ps:
      if m % p == 0:
          m /= p
          return [p] + factors(m)

  N = 12000
  ps = list(primes(2*N))
  sps = set(ps)

  min_k = {i:2*i for i in range(2,N+1)}

  for i in range(2,2*N+1):
      for partition in sympy.utilities.iterables.multiset_partitions(factors(i)):
          tmp = [np.prod(i) for i in partition]
          s = sum(tmp)
          if i-s>=0:
              nfacs = len(tmp)
              k = i - s + nfacs
              if k>1 and k<N+1 and i<min_k[k]:
                  min_k[k]=i

  return sum(set(min_k.values()))

def pjeuler89():
  def parse(s):
    s=s.replace('CM','DCCCC')
    s=s.replace('CD','CCCC')
    s=s.replace('XC','LXXXX')
    s=s.replace('XL','XXXX')
    s=s.replace('IX','VIIII')
    s=s.replace('IV','IIII')
    di = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    return sum([di[c] for c in s])

  def write(n):
    n1000 = n//1000
    n = n%1000
    n100 = n//100
    n = n%100
    n10 = n//10
    n = n%10
    n1 = n
    s1000 = 'M'*n1000

    if n100 in [1,2,3]:
      s100 = 'C'*n100
    elif n100 in [4]:
      s100 = 'CD'
    elif n100 in [5,6,7,8]:
      s100 = 'D' + 'C'*(n100-5)
    elif n100 in [9]:
      s100 = 'CM'
    else:
      s100 = ''

    if n10 in [1,2,3]:
      s10 = 'X'*n10
    elif n10 in [4]:
      s10 = 'XL'
    elif n10 in [5,6,7,8]:
      s10 = 'L' + 'X'*(n10-5)
    elif n10 in [9]:
      s10 = 'XC'
    else:
      s10 = ''

    if n1 in [1,2,3]:
      s1 = 'I'*n1
    elif n1 in [4]:
      s1 = 'IV'
    elif n1 in [5,6,7,8]:
      s1 = 'V' + 'I'*(n1-5)
    elif n1 in [9]:
      s1 = 'IX'
    else:
      s1 = ''

    return s1000+s100+s10+s1

  save = 0
  f = get(89)
  for r in f.readlines():
    rs = r.strip()
    n = parse(rs)
    r2 = write(n)
    save += len(rs)-len(r2)
  f.close()
  return save

def pjeuler90():
  import itertools

  def check(i,j):
      return (i in l1 and j in l2) or (j in l1 and i in l2)

  def check6(i):
      return (i in l1 and (6 in l2 or 9 in l2)) or ((6 in l1 or 9 in l1) and i in l2)
  s = 0
  for l1 in itertools.combinations(range(10),6):
      for l2 in itertools.combinations(range(10),6):
          if check(0,1) and check(0,4) and check6(0) and check6(1) and check(2,5) and check6(3) and check6(4) and check(8,1):
              s += 1
  return s//2

def pjeuler91():
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
  return n//2

def pjeuler92():
  @cache
  def f(x):
    i = 0
    while x>9:
      d = x%10
      i += d*d
      x = x//10
    return i+x*x

  n = 10000000
  l = [0]*(n+1)
  l[1]=1
  l[89]=2
  for i in range(2,n+1):
    v = i
    while True:
      if v < n+1 and l[v]!=0:
        l[i]=l[v]
        break
      v = f(v)
  return sum([1 for i in l if i==2])

def pjeuler93():
  def apply(x,y):
    l = [x+y,x-y,y-x,x*y]
    if x!=0:
      l += [y/x]
    if y!=0:
      l += [x/y]
    return l
  di = dict()
  for a in range(1,10):
    for b in range(a+1,10):
      for c in range(b+1,10):
        for d in range(c+1,10):
          arr = [False]*10000
          arr[0] = True
          for i in itertools.permutations([a,b,c,d]):
            for r1 in apply(i[0],i[1]):
              for r2 in apply(r1,i[2]):
                for r3 in apply(r2,i[3]):
                  if abs(round(r3)-r3)<1e-8 and r3>0:
                    arr[round(r3)] = True
              for r2 in apply(i[2],i[3]):
                for r3 in apply(r1,r2):
                  if abs(round(r3)-r3)<1e-8 and r3>0:
                    arr[round(r3)] = True
          di[a*1000+b*100+c*10+d] = min([idx for (idx,i) in enumerate(arr) if not i])-1
  return max(di, key=di.get)

def pjeuler94():
  def is_square(x):
      return round(x**.5)**2==x

  s = 0
  l = [5, 17, 65, 241, 901, 3361, 12545, 46817, 174725, 652081, 2433601, 9082321, 33895685, 126500417, 472105985,1761923521]

  for i in l:
    a = i
    b = i
    c = i+1
    perimeter = (a+b+c)
    p = perimeter//2
    area2 = p*(p-a)*(p-b)*(p-c)
    if is_square(area2) and perimeter<1e9:
        s += perimeter
    a = i
    b = i
    c = i-1
    perimeter = (a+b+c)
    p = perimeter//2
    area2 = p*(p-a)*(p-b)*(p-c)
    if is_square(area2) and perimeter<1e9:
        s += perimeter
  return s

def pjeuler95():
  from .tools import primes

  @cache
  def factors(m):
    if m in sps:
      return [int(m)]
    for p in ps:
      if m % p == 0:
          m /= p
          return [p] + factors(m)

  @cache
  def sum_divs(x):
    if x in sps or x==1:
        return 1
    y=collections.Counter(factors(x))
    return int(np.prod([(p**(n+1)-1)/(p-1) for (p,n) in y.items()])-x)

  N = int(1e6)

  ps = list(primes(int(N)))
  sps = set(ps)

  longest_chain = 0

  s = [0]*(N+1)

  for i in range(2,N+1):
      if s[i]!=0:
          continue
      k = i
      li = [k]
      s[k] = -1
      periodicity = 0
      while True:
          k = sum_divs(k)
          if k>N:
              break
          if k in li:
              idx = li.index(k)
              periodicity = len(li) - idx
              if periodicity>longest_chain:
                  longest_chain = periodicity
                  result = min(li[idx:])
              break
          if s[k] != 0:
              break
          s[k] = -1
          li += [k]
  return result

def pjeuler96():
  import copy

  f = get(96)
  a = np.empty((9,9),dtype=object)
  s = []
  for (i,l) in enumerate(f):
    if i%10==0:
      a = np.empty((9,9),dtype=object)
    if i%10!=0:
      v = [int(j) for j in l.rstrip()]
      for j in range(9):
        if v[j]==0:
          a[(i-1)%10,j] = [1,2,3,4,5,6,7,8,9]
        else:
          a[(i-1)%10,j] = [v[j]]
    if i%10==9:
      s.append(a)
  f.close()

  def solve_sudoku(a):
    while True:
      finished = True
      progress = False
      for i in range(9):
        for j in range(9):
          if len(a[i,j])==0:
            return None, False
          if len(a[i,j])==1:
            # Found a single number, delete other possibilities:
            v = a[i,j][0]
            for k in range(9):
              if k!= i and v in a[k,j]:
                a[k,j].remove(v)
                progress = True
              if k!= j and v in a[i,k]:
                a[i,k].remove(v)
                progress = True
            for k1 in range(3):
              for k2 in range(3):
                idx1 = math.floor(i/3)*3 + k1
                idx2 = math.floor(j/3)*3 + k2
                if idx1!=i and idx2!=j and v in a[idx1,idx2]:
                  a[idx1,idx2].remove(v)
                  progress = True
          else:
            finished = False
      if finished:
        return a, True
      if not progress:
        # Guess
        found = False
        for i in range(9):
          for j in range(9):
            if len(a[i,j])>1:
              found = True
              break
          if found:
            break
        v = a[i,j][0]
        b = copy.deepcopy(a)
        b[i,j] = [v]
        b, val = solve_sudoku(b)
        if val:
          return b, True
        a[i,j].remove(v)

  sol = 0
  for counter in range(len(s)):
    a,_ = solve_sudoku(s[counter])
    tmp = a[0,0][0]*100+a[0,1][0]*10+a[0,2][0]
    sol += tmp
  return sol

def pjeuler97():
  from .tools import smart_mod
  mod = int(1e10)
  return (28433*smart_mod(2,7830457,mod)+1)%mod

def pjeuler98():
  f = get(98)
  words = [i[1:-1] for i in f.readline().rsplit(",")]
  f.close()

  def all_different_digits(x):
      return len(set([c for c in str(x)]))==n

  def get_permutation(word1,word2):
      w1 = [c for c in word1]
      w2 = [c for c in word2]
      return [w2.index(i) for i in w1]


  final_list = []
  for i in range(len(words)):
      vi = sorted(words[i])
      for j in range(i+1,len(words)):
          vj = sorted(words[j])
          if vi==vj:
              n = len(words[i])
              lower = math.ceil((10**(n-1))**.5)
              upper = math.floor((10**n)**.5)

              perm = get_permutation(words[i],words[j])

              arr = []
              for k in range(lower,upper+1):
                  v2 = k**2
                  if len(str(v2))==n and all_different_digits(v2):
                      arr += [str(v2)]

              for k in arr:
                  v3 = ''.join([k[perm[m]] for m in range(n)])
                  if v3 in arr:
                      final_list += [int(k), int(v3)]
  return max(final_list)

def pjeuler99():
  f = get(99)
  max_idx = -1
  max_val = 0
  for (idx,i) in enumerate(f.readlines()):
    a,b = i.rsplit(",")
    a = int(a)
    b = int(b)
    if b*math.log(a) > max_val:
      max_idx = idx
      max_val = b*math.log(a)
  f.close()
  return max_idx + 1

def pjeuler100():
  b = 3
  n = 4
  while n<1e12:
      (b,n) = (3*b+2*n-2, 4*b+3*n-3)
  return b

def pjeuler101():
  import scipy.interpolate
  def g(x):
    return 1-x+x**2-x**3+x**4-x**5+x**6-x**7+x**8-x**9+x**10
  x = range(1,11)
  y = [g(i) for i in x]
  s = 0
  for j in range(1,11):
    v = scipy.interpolate.barycentric_interpolate(x[:j],y[:j],j+1)
    s += round(v.tolist())
  return s

def pjeuler102():
  f = get(102)
  n = 0
  for i in f:
    t = [int(i) for i in i.rsplit(',')]

    p0x = t[0]
    p0y = t[1]
    p1x = t[2]
    p1y = t[3]
    p2x = t[4]
    p2y = t[5]
    Area = 0.5 *(-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y)
    s = 1/(2*Area)*(p0y*p2x - p0x*p2y)
    t = 1/(2*Area)*(p0x*p1y - p0y*p1x)

    if s>0 and t>0 and 1-s-t>0:
      n += 1
  f.close()
  return n

def pjeuler104():
  a = 1
  b = 1
  k = 2
  arr = '123456789'
  while True:
    k += 1
    b, a = a+b, b
    end = b%1000000000
    end = ''.join(sorted(str(end)))==arr
    if end:
      begin = b//10**math.ceil(math.log10(b)-9)
      begin = ''.join(sorted(str(begin)))==arr
      if begin:
        break
  return k

def pjeuler107():
  import scipy.sparse.csgraph
  f = get(107)
  a = np.zeros((40,40))
  i = 0
  for l in f:
    j = 0
    for c in l.rsplit(','):
      if c!='-' and c!='-\n':
        a[i,j] = int(c.rstrip())
      j += 1
    i += 1
  f.close()
  res = scipy.sparse.csgraph.minimum_spanning_tree(a)
  return int(.5 * np.sum(a)-np.sum(res))

def pjeuler108():
  def n_from_lst(lst):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    return np.prod([float(b)**e for (b,e) in zip(primes,lst)])

  def sol_from_lst(lst):
    ans = np.prod([2*x+1 for x in lst])
    return (ans+1)//2

  @cache
  def partition(number,maxlen):
    answer = [[number]]
    for x in range(1, number):
      for y in partition(number - x,maxlen-1):
        if len(y) <= maxlen - 1 and x >= max(y):
          answer.append([x]+y)
    return answer

  val = 1000
  n = 1e10
  max_len = 10
  max_s = 10
  for s in range(1,max_s+1):
    for p in partition(s,max_len):
      if sol_from_lst(p) > val:
        n = min(n,n_from_lst(p))
  return(int(n))

def pjeuler109():
  fields = []
  for m in range(1,4):
    for n in list(range(1,21))+[25]:
      if m!=3 or n!=25:
        fields += [(m,n)]
  sols = 0
  for number in range(1,100):
    for (m1,n1) in fields:
        remain = number
        v = m1*n1
        if v > remain:
          continue
        if v == remain and m1 == 2:
          sols += 1
          continue
        remain2 = remain - v
        for (m2,n2) in fields:
          v = m2*n2
          if v > remain2:
            continue
          if v == remain2 and m2 == 2:
            sols += 1
            continue
          if m2>m1 or (m2==m1 and n2>=n1):
            remain3 = remain2 - v
            for (m3,n3) in fields:
              v = m3*n3
              if v == remain3 and m3 == 2:
                sols += 1
                continue
  return sols

def pjeuler110():
  def n_from_lst(lst):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    return np.prod([float(b)**e for (b,e) in zip(primes,lst)])

  def sol_from_lst(lst):
    ans = np.prod([2*x+1 for x in lst])
    return (ans+1)//2

  @cache
  def partition(number,maxlen):
    answer = [[number]]
    for x in range(1, number):
      for y in partition(number - x,maxlen-1):
        if len(y) <= maxlen - 1 and x >= max(y):
          answer.append([x]+y)
    return answer

  val = 4000000
  n = 1e20
  max_len = 15
  max_s = 20
  for s in range(1,max_s+1):
    for p in partition(s,max_len):
      if sol_from_lst(p) > val:
        n = min(n,n_from_lst(p))
  return(int(n))

def pjeuler112():
  def d(x):
    l = []
    while x>9:
      l.append(x%10)
      x = x//10
    l.append(x)
    l.reverse()
    return l

  def is_bouncy(n):
    digs = d(n)
    b1 = True
    b2 = True
    for i in range(len(digs)-1):
      if digs[i]>digs[i+1]:
        b1 = False
      if digs[i]<digs[i+1]:
        b2 = False
    return not b1 and not b2

  n = 0
  i = 0
  while True:
    i += 1
    n += is_bouncy(i)
    if n*100==i*99:
      break
  return i

def pjeuler113():
  @cache
  def increasing_numbers_starting_with(l,i):
    if i==0:
      return 0
    if l==1:
      return 1
    n = 0
    for j in range(i,10):
      n += increasing_numbers_starting_with(l-1,j)
    return n

  @cache
  def decreasing_numbers_starting_with(l,i):
    if i==0:
      return 0
    if l==1:
      return 1
    n = 1
    for j in range(i+1):
      n += decreasing_numbers_starting_with(l-1,j)
    return n

  expo = 100
  n = -9*expo
  for l in range(1,expo+1):
    for i in range(10):
      n += increasing_numbers_starting_with(l,i)
    for i in range(10):
      n += decreasing_numbers_starting_with(l,i)
  return n

def pjeuler114():
  @cache
  def split(l,red_allowed):
      if l<3:
          return 1
      n = 0
      n += split(l-1,True)
      if red_allowed:
          for i in range(3,l+1):
              n += split(l-i,False)
      return n
  return split(50,True)

def pjeuler115():
  @cache
  def split(m,l,red_allowed):
      if l<0:
          return 0
      if l<2:
          return 1
      n = 0
      n += split(m,l-1,True)
      if red_allowed:
          for i in range(m,l+1):
              n += split(m,l-i,False)
      return n

  n = 50
  while True:
      if split(50,n,True) > 1000000:
          break
      n += 1
  return n

def pjeuler116():
  @cache
  def split(l,c):
      if l<c:
          return 1
      return split(l-1,c)+split(l-c,c)
  return split(50,2)+split(50,3)+split(50,4)-3

def pjeuler117():
  @cache
  def split(l):
      if l<0:
          return 0
      if l<2:
          return 1
      return sum([split(l-i) for i in range(1,5)])
  return split(50)

def pjeuler119():
  from .tools import digit_sum
  l = []
  for base in range(2,100):
    for exp in range(2,10):
      if digit_sum(base**exp)==base:
        l.append(base**exp)
  l.sort()
  return l[29]

def pjeuler120():
  N = 1000
  s = 0
  for a in range(3,N+1):
      r = 2*a
      rmax = r
      while r != 0:
          rmax = max(rmax,r)
          r = (r+2*a)%(a**2)
      s += rmax
  return s

def pjeuler121():
  from .tools import int2base, digits
  p0 = 0
  n = 15
  for i in range(2**n):
    v = int2base(i,2).zfill(n)
    if 2*sum(digits(v)) > n:
      p = 1
      for j in range(n):
        if v[j]=='1':
          p *= 1/(j+2)
        else:
          p *= (j+1)/(j+2)
      p0 += p
  return math.floor(1/p0)

def pjeuler122():
  x = 200
  l = [None,[set([1])]]
  su = 0
  for k in range(2,x+1):
    sols = []
    for j1 in range(1,k//2+1):
      for s1 in l[k-j1]:
        if j1 in s1:
          sols.append(s1.union([k]))
    vmin = min(len(s) for s in sols)
    l.append([s for s in sols if len(s) == vmin])
    su += vmin-1
  return su

def pjeuler123():
  from .tools import primes
  ps = list(primes(250000))
  v = 1e10
  low = 1
  high = len(ps)
  while True:
    n = round(0.5*(low+high))
    if 2 * (n+1) * ps[n] < v:
      low = n
    else:
      high = n
    if low+1==high:
      break
  if high % 2 == 0:
    result = high + 1
  else:
    result = high + 2
  return result

def pjeuler124():
  from .tools import factors
  a = []
  l = 100000
  for i in range(1,l+1):
    a.append(np.prod(np.unique(factors(i))))
  df = pd.DataFrame({"n":range(1,l+1),"radn":a})
  return df.sort_values(["radn","n"]).reset_index().drop("index",axis=1).n[10000-1]

def pjeuler125():
  from .tools import is_palindrome
  sols = []
  m = 1e8
  for i in range(1,math.floor((m/2)**.5)+1):
    j = i
    n = j**2
    while True:
      j += 1
      n += j**2
      if n>=m:
        break
      if is_palindrome(n):
        sols.append(n)
  return sum(set(sols))

def pjeuler126():
  def calc(a,b,c,n):
    return 2*(a*b+a*c+b*c) + 4 * (n-1) * (a+b+c+n-2)

  vol_max = 200000
  counter_max = 20000

  counter = [0]*counter_max

  for a in range(1,vol_max+1):
    for b in range(1,min(vol_max//a,a+1)):
      for c in range(1,min(vol_max//(a*b),b+1)):
        n = 1
        while True:
          v = calc(a,b,c,n)
          if v >= counter_max:
            break
          counter[v] += 1
          n += 1

  for (i,v) in enumerate(counter):
    if v==1000:
      return i

def pjeuler145():
  def sols(n):
    if n%2==0:
      return 20*30**(n//2-1)
    if n%4==1:
      return 0
    if n%4==3:
      return 100*500**(n//4)
  return sum([sols(n) for n in range(1,10)])

def pjeuler155():
  from fractions import Fraction as f
  di = {1:[f(60,1)]}
  nmax = 18
  possible = set(di[1])
  print(1,len(possible))
  for n in range(2,nmax+1):
      di[n] = []
      for n1 in range(1,math.floor(n/2)+1):
          n2 = n - n1
          for el1 in di[n1]:
              for el2 in di[n2]:
                  v1 = el1 + el2
                  v2 = f(1,f(1,el1)+f(1,el2))
                  di[n] += [v1]
                  di[n] += [v2]
      s = set(di[n])
      di[n] = list(s)
      di[n] = [el for el in di[n] if el not in possible]
      possible = possible.union(s)
  return len(possible)

def pjeuler169():
  @cache
  def f(x):
    if x<=1:
      return x
    if x%2==0:
      return f(x//2)
    else:
      return f(x//2)+f(x//2+1)
  return f(int(1e12)*int(1e13)+1)

def pjeuler172():
  @cache
  def calc(n0,n1,n2,n3,n4,n5,n6,n7,n8,n9):
      if n0+n1+n2+n3+n4+n5+n6+n7+n8+n9==1:
          if n0==0:
              return 1
          else:
              return 0
      s = 0
      if n0>0:
          s += calc(n0-1,n1,n2,n3,n4,n5,n6,n7,n8,n9)
      if n1>0:
          s += calc(n0,n1-1,n2,n3,n4,n5,n6,n7,n8,n9)
      if n2>0:
          s += calc(n0,n1,n2-1,n3,n4,n5,n6,n7,n8,n9)
      if n3>0:
          s += calc(n0,n1,n2,n3-1,n4,n5,n6,n7,n8,n9)
      if n4>0:
          s += calc(n0,n1,n2,n3,n4-1,n5,n6,n7,n8,n9)
      if n5>0:
          s += calc(n0,n1,n2,n3,n4,n5-1,n6,n7,n8,n9)
      if n6>0:
          s += calc(n0,n1,n2,n3,n4,n5,n6-1,n7,n8,n9)
      if n7>0:
          s += calc(n0,n1,n2,n3,n4,n5,n6,n7-1,n8,n9)
      if n8>0:
          s += calc(n0,n1,n2,n3,n4,n5,n6,n7,n8-1,n9)
      if n9>0:
          s += calc(n0,n1,n2,n3,n4,n5,n6,n7,n8,n9-1)
      return s

  def split(n,k,arr):
      if n<0:
          return
      if k == 1:
          if n <= 3:
              sols.append(arr+[n])
          return
      split(n  ,k-1,arr+[0])
      split(n-1,k-1,arr+[1])
      split(n-2,k-1,arr+[2])
      split(n-3,k-1,arr+[3])

  sols = []
  split(18,10,[])
  n = 0
  for sol in sols:
      n += calc(sol[0],sol[1],sol[2],sol[3],sol[4],sol[5],sol[6],sol[7],sol[8],sol[9])
  return n

def pjeuler173():
  @cache
  def tiles_ring(l):
    if l==1:
      return 1
    else:
      return 4*l-4

  @cache
  def n_pattern(maxw,ntiles):
    if maxw < 3:
      return 0
    tmp = tiles_ring(maxw)
    if ntiles >= tmp:
      return 1 + n_pattern(maxw-2,ntiles-tmp)
    else:
      return 0

  ntiles = 1000000
  n = 0
  for i in range(1,ntiles//4+3):
    n += n_pattern(i,ntiles)
  return n

def pjeuler177():
  @functools.lru_cache(None)
  def si(x):
      return math.sin(x/180*math.pi)

  @functools.lru_cache(None)
  def co(x):
      return math.cos(x/180*math.pi)

  s = []
  for a in range(1,179):
      print(a)
      for c in range(1,179):
          b = 180 - a - c
          if b>1:
              for d in range(1,180-a):
                  for e in range(1,180-c):
                      f = 180 - d - e
                      if f>1:
                          nom = si(a+d)
                          den = si(e)*si(b)/si(f)/si(c)-co(a+d)
                          x = math.atan2(nom,den)*180/math.pi
                          if abs(round(x)-x)<1e-5:
                              x = int(x)
                              y = 180 - a - d - x
                              if x > 0 and f-x > 0 and y > 0 and b-y > 0:
                                  check_val  = si(f)*si(c)*si(y)-si(b)*si(e)*si(x)
                                  if abs(check_val) < 1e-9:
                                    s += [(d,a,y,b-y,c,e,f-x,x)]

  t = set()
  for (a,b,c,d,e,f,g,h) in s:
      if (a,b,c,d,e,f,g,h) in t or (c,d,e,f,g,h,a,b) in t or (e,f,g,h,a,b,c,d) in t or (g,h,a,b,c,d,e,f) in t:
          continue
      if (h,g,f,e,d,c,b,a) in t or (f,e,d,c,b,a,h,g) in t or (d,c,b,a,h,g,f,e) in t or (b,a,h,g,f,e,d,c) in t:
          continue
      t.add((a,b,c,d,e,f,g,h))
  return len(t)

def pjeuler179():
  n = int(1e7)
  l = [0]*n
  s = 0
  for i in range(1,n):
    for j in range(i,n,i):
      l[j] += 1
    if l[i]==l[i-1]:
      s += 1
  return s

def pjeuler187():
  def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

  l = int(1e8)
  ps = list(primes(l//2))
  n = len(ps)
  n_primes = [0,0]
  for i in range(n-1):
    n_primes += [i+1] * (ps[i+1]-ps[i])
  n_primes += [i+2] * (l-ps[-1])

  s = 0
  for p in ps:
    if p**2 > l:
      break
    p2 = l // p
    s += n_primes[p2] - n_primes[p-1]
  return s

def pjeuler191():
  # n = 2 => sol = 8
  # 00 0A 0L A0 AA AL L0 LA
  with_l_ending_LA_0A          = 1 # LA
  with_l_ending_AA             = 0 #
  with_l_ending_0L_AL_L0_00_A0 = 3 # 0L AL L0
  no_l_ending_0A      = 1
  no_l_ending_AA      = 1
  no_l_ending_00_A0   = 2
  n = with_l_ending_LA_0A + with_l_ending_AA + with_l_ending_0L_AL_L0_00_A0 + no_l_ending_0A + no_l_ending_AA + no_l_ending_00_A0

  for k in range(3,31):
      new_no_l_ending_0A    = no_l_ending_00_A0
      new_no_l_ending_AA    = no_l_ending_0A
      new_no_l_ending_00_A0 = no_l_ending_00_A0 + no_l_ending_0A + no_l_ending_AA

      new_with_l_ending_LA_0A = with_l_ending_0L_AL_L0_00_A0
      new_with_l_ending_AA = with_l_ending_LA_0A
      new_with_l_ending_0L_AL_L0_00_A0 = no_l_ending_0A + no_l_ending_AA + no_l_ending_00_A0 +\
          with_l_ending_0L_AL_L0_00_A0 + with_l_ending_LA_0A +\
              with_l_ending_AA

      no_l_ending_0A = new_no_l_ending_0A
      no_l_ending_AA = new_no_l_ending_AA
      no_l_ending_00_A0 = new_no_l_ending_00_A0

      with_l_ending_LA_0A = new_with_l_ending_LA_0A
      with_l_ending_AA = new_with_l_ending_AA
      with_l_ending_0L_AL_L0_00_A0 = new_with_l_ending_0L_AL_L0_00_A0

      n = with_l_ending_LA_0A + with_l_ending_AA + with_l_ending_0L_AL_L0_00_A0 + no_l_ending_0A + no_l_ending_AA + no_l_ending_00_A0
  return n

def pjeuler199():
  import math

  k = 1+2/math.sqrt(3)

  ratio = 1 - 3 * 1/k**2
  gaps = [(-1,k,k),(-1,k,k),(-1,k,k),(k,k,k)]

  steps = 10
  for i in range(steps):
    new_gaps = []
    for (k1, k2, k3) in gaps:
      k_new = k1 + k2 + k3 + 2 * math.sqrt( k1*k2 + k2*k3 + k1*k3)
      new_gaps += [(k1,k3,k_new),(k1,k2,k_new),(k2,k3,k_new)]
      ratio -= 1/k_new**2
    gaps = new_gaps

  return round(ratio,8)

def pjeuler203():
  l = []
  ps = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
  ps = [i**2 for i in ps]
  v = 51
  for n in range(v):
    for k in range(math.ceil(n/2)+1):
      x = round(scipy.special.binom(n,k))
      squarefree =  True
      for p in ps:
        if x % p == 0:
          squarefree = False
      if squarefree:
        l.append(x)
  return sum(np.unique(l))

def pjeuler205():
  score_pete = [0]*37
  for i1 in range(1,5):
    for i2 in range(1,5):
      for i3 in range(1,5):
        for i4 in range(1,5):
          for i5 in range(1,5):
            for i6 in range(1,5):
              for i7 in range(1,5):
                for i8 in range(1,5):
                  for i9 in range(1,5):
                    score_pete[i1+i2+i3+i4+i5+i6+i7+i8+i9] += 1/(4**9)

  score_colin = [0]*37
  for i1 in range(1,7):
    for i2 in range(1,7):
      for i3 in range(1,7):
        for i4 in range(1,7):
          for i5 in range(1,7):
            for i6 in range(1,7):
                    score_colin[i1+i2+i3+i4+i5+i6] += 1/(6**6)

  p_pete_beats_colin = 0
  for res1 in range(1,37):
    for res2 in range(res1+1,37):
      p_pete_beats_colin += score_colin[res1]*score_pete[res2]
  return round(p_pete_beats_colin,7)

def pjeuler206():
  a = round(1020304050607080900**.5)
  b = round(1929394959697989990**.5)
  for x in range(a,b,10):
    y = x**2
    success = True
    for i in range(9):
      y = y//100
      if y%10 != 9-i:
        success = False
        break
    if success:
      return x

def pjeuler216():
  s = 0
  for n in range(int(5e7)):
    if n%100000==0:
      print(n)
    if sympy.isprime(2*n**2-1):
      s += 1
  return s

def pjeuler235():
  def u(k,r):
    return (900-3*k)*r**(k-1)
  def s(r):
    return sum([u(k,r) for k in range(1,5001)]) + 600000000000
  r1 = 1
  r2 = 1.1

  while r2-r1>1e-12:
    r = (r1+r2)/2
    if s(r)>0:
      r1 = r
    else:
      r2 = r
  return round(r,12)

def pjeuler301():
  @cache
  def nim(a,b,c):
    if a==0 and b==0 and c!=0:
      return 1
    if a==0 and b!=0 and c==0:
      return 1
    if a!=0 and b==0 and c==0:
      return 1
    if a==0 and b==c:
      return 0
    if b==0 and a==c:
      return 0
    if c==0 and a==b:
      return 0
    for a2 in range(a):
      if not nim(a2,b,c):
        return 1
    for b2 in range(b):
      if not nim(a,b2,c):
        return 1
    for c2 in range(c):
      if not nim(a,b,c2):
        return 1
    return 0

  n = []
  for i in range(1,51):
    a = i
    b = 2*i
    c = 3*i
    if not nim(a,b,c):
      n += [i]

  def A003714(n):
    tlist, s = [1, 2], 0
    while tlist[-1]+tlist[-2] <= n:
        tlist.append(tlist[-1]+tlist[-2])
    for d in tlist[::-1]:
        s *= 2
        if d <= n:
            s += 1
            n -= d
    return s

  i = 1
  while True:
    i+=1
    if A003714(i) >= 2**30:
      return i

def pjeuler317():
  h = 100
  v = 20
  g = 9.81
  V = math.pi * v**2/4/g**3 * (v**2+2*g*h)**2
  return round(V,4)

def pjeuler345():
  @cache
  def val(m):
    n = len(m)
    if n == 1:
      return m[0][0]
    v = 0
    for i in range(n):
      m0 = tuple(row[1:] for (x,row) in enumerate(m) if x!=i)
      v0 = m[i][0] + val(m0)
      v = max(v,v0)
    return v

  d = get(345).read().splitlines()
  d = [i.split() for i in d]
  d = tuple(tuple(int(i) for i in j) for j in d)
  return val(d)

def pjeuler349():
  n = 2000

  a = np.zeros((n,n))

  x = n//2
  y = n//2

  steps = 50000
  step = 0
  rot = 0
  arr = [0]*steps
  n = 0
  for step in range(steps):
      if a[x,y] == 0:
          n += 1
          a[x,y] = 1
          rot = (rot - 1) % 4
      else:
          n -= 1
          a[x,y] = 0
          rot = (rot + 1) % 4
      if rot == 0:
          x -= 1
      elif rot == 1:
          y -= 1
      elif rot == 2:
          x += 1
      else:
          y += 1
      arr[step] = n

  # Get period length from Fourier analysis
  periodic_part = arr[11000:]
  indices = [i for (i,x) in enumerate(scipy.fft.fft(periodic_part)) if np.real(x)>0 and i>0]
  period = len(periodic_part) // min(indices)
  incr = arr[11000+period] - arr[11000]

  steps = 10**18
  offset = steps%period
  step_until_period = offset + 120 * period
  step_until_end = steps - step_until_period
  periods_until_end = step_until_end // period

  return arr[step_until_period-1] + incr * periods_until_end

def pjeuler353():
  #from mayavi import mlab
  import scipy.sparse
  import scipy.sparse.csgraph
  def risk(p1,p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    alpha = math.acos((x1*x2+y1*y2+z1*z2)/r**2)
    return alpha**2

  def dist(p1,p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return abs(x1-x2)+abs(y1-y2)+abs(z1-z2)

  def plot():
    idx = min_idx
    sol_pts = []
    while True:
      idx = sol[0,idx]
      if idx == -9999:
        break
      pt = pts[idx]
      sol_pts = [pt] + sol_pts

    x = sol_pts[-1][0]
    y = sol_pts[-1][1]
    if x * y !=0:
      l = r / (x**2+y**2)**.5
      x *= l
      y *= l
      p2 = (x,y,0)
    else:
      p2 = (r,0,0)
    sol_pts += [p2]

    # Create a sphere
    pi = np.pi
    cos = np.cos
    sin = np.sin
    phi, theta = np.mgrid[0:pi/2:21j, pi/4:pi/2:21j]

    x = r * sin(phi) * cos(theta)
    y = r * sin(phi) * sin(theta)
    z = r * cos(phi)

    xx,yy,zz = zip(*pts)
    xsol,ysol,zsol = zip(*sol_pts)


    mlab.figure(1, bgcolor=(1,1,1), fgcolor=(0, 0, 0), size=(800, 800))
    mlab.clf()
    mlab.mesh(x, y, z,color=(0,1,1),opacity=0.5)
    mlab.points3d(xx,yy,zz,color=(1,0,0),scale_factor=0.01*r)
    mlab.plot3d(xsol,ysol,zsol,line_width=20*r,tube_radius=r/500)
    mlab.view(66, 52, 3*r,focalpoint="auto")
    mlab.show()

  s = 0
  rs = [2**n-1 for n in range(1,16)]
  for r in rs:

    pts = []
    for x in range(r):
      hlp = r**2-x**2
      for y in range(x,r+1):
        z2 = hlp-y**2
        if z2<0:
          break
        z = round(math.sqrt(z2))
        if z**2 == z2:
          pts.append((x,y,z))
          if z<=x:
            pts.append((z,x,y))
          if z<=y:
            pts.append((z,y,x))

    pts = list(set(pts))
    n = len(pts)+1

    start_idx = pts.index((0,0, r))
    goal_pts = [pt for pt in pts if pt[2]==0]
    goal_idxs = [n-1]
    for pt in goal_pts:
      goal_idxs.append(pts.index(pt))

    max_dist = 10000
    ii = []
    jj = []
    vv = []
    for i,p1 in enumerate(pts):
      for j,p2 in enumerate(pts):
        if i<j:
          if dist(p1,p2) < max_dist:
            rsk = risk(p1,p2)
            ii.append(i)
            jj.append(j)
            vv.append(rsk)
            ii.append(j)
            jj.append(i)
            vv.append(rsk)
      if i not in goal_idxs:
        p2 = (p1[0], p1[1], -p1[2])
        if dist(p1,p2) < max_dist:
          rsk = risk(p1,p2)
          ii.append(i)
          jj.append(n-1)
          vv.append(rsk/2)
          ii.append(n-1)
          jj.append(i)
          vv.append(rsk/2)
    mat = scipy.sparse.csr_matrix((vv,(ii,jj)),shape=(n,n))

    result, sol = scipy.sparse.csgraph.shortest_path(mat,indices=[start_idx],return_predecessors=True)

    min_dst = 1
    for idx in goal_idxs:
      dst = result[0,idx]/math.pi**2 * 2
      if dst < min_dst:
        min_dst = dst
        min_idx = idx
    s += min_dst
  return round(s,10)

def pjeuler357():
  from .tools import primes
  from sympy import divisors
  n = 100000000
  primes = list(primes(n))
  set_ps = set(primes)
  nums = [p-1 for p in primes]
  smalls = [p for p in primes if p<n**.5]

  s = 0
  for(c,n) in enumerate(nums):

    # n = \prod_{i=1}^m p_i
    b = True
    for p in smalls:
      # Check if square-free
      if n%(p*p) == 0:
        b = False
        break
      # Check if \prod_{i=1, i\neq j}^m p_i + p_j is prime
      if n%p == 0:
        v = p + n//p
        if v not in set_ps:
          b = False
          break
    if not b:
      continue

    # Check if \prod_{i=1, i\neq j, i\neq k}^m p_i + p_j p_k is prime
    for p1 in smalls:
      if n%p1==0:
        for p2 in smalls:
          if p2>p1 :
            if n%(p1*p2) == 0:
              v = p1*p2 + n//(p1*p2)
              if v not in set_ps:
                b = False
                break
        if not b:
          break
    if not b:
      continue

    # Now just check directly all divisors
    for d in divisors(n):
      if n//d + d not in set_ps:
        b = False
    if b:
      s += n
  return s

def pjeuler363():
  import math
  from mpmath import mp
  mp.dps = 50

  def my_bezier(t,v):
    x0 = 1
    y0 = 0
    x1 = 1
    y1 = v
    x2 = v
    y2 = 1
    x3 = 0
    y3 = 1

    x0 = x0*t+x1*(1-t)
    y0 = y0*t+y1*(1-t)
    x1 = x1*t+x2*(1-t)
    y1 = y1*t+y2*(1-t)
    x2 = x2*t+x3*(1-t)
    y2 = y2*t+y3*(1-t)

    x0 = x0*t+x1*(1-t)
    y0 = y0*t+y1*(1-t)
    x1 = x1*t+x2*(1-t)
    y1 = y1*t+y2*(1-t)

    x0 = x0*t+x1*(1-t)
    y0 = y0*t+y1*(1-t)
    return x0,y0

  def eval(N,v):
    l = 0
    a = -mp.pi/4
    xold, yold = my_bezier(0,v)
    for i in range(1,N+1):
      x,y = my_bezier(i/N,v)
      if i>0:
        l += ((x-xold)**2+(y-yold)**2)**.5
        a += (y+yold)*(x-xold)/2
      xold = x
      yold = y
    return l,a

  N = 100000
  v1 = 0.5517
  v2 = 0.5518
  l1,a1 = eval(N,v1)
  l2,a2 = eval(N,v2)

  eold = 1
  while True:
    N = round(N*1.1)
    v = (v1+v2)/2
    l,a = eval(N,v)
    err = 100*(l-math.pi/2)/(math.pi/2)
    err = round(err,10)
    if a>0:
      v2 = v
    else:
      v1 = v
    if abs(eold-err)<1e-11:
      break
    eold = err
  return round(err,10)

def pjeuler493():
  from scipy.special import comb
  return round(7*(1-comb(60,20)/comb(70,20)),9)

def pjeuler504():
  m = 100

  dct = {}
  for a in range(1,m+1):
    for b in range(1,m+1):
      v = .25
      if a>1:
        v += (a-1) * .5
      if b>1:
        v += (b-1) * .5
      if a>1 and b>1:
        v += .5 * ( (a-1)*(b-1) - sympy.gcd(a,b) + 1)
      dct[(a,b)] = round(v*4)
      dct[(b,a)] = round(v*4)

  q = set(i**2 for i in range(0,400,2))
  s = 0
  for a in range(1,m+1):
    for b in range(1,m+1):
      v0 = dct[(a,b)]
      for c in range(1,m+1):
        v1 = v0 + dct[(b,c)]
        for d in range(1,m+1):
          v = v1 + dct[(c,d)] +dct[(d,a)]
          if v in q:
            s += 1
  return s

def pjeuler577():
  tri = [(i+1)*(i+2)//2 for i in range(12345)]
  def H(n):
    x = 0
    m = 1
    n -= 3
    while n>=0:
      x += tri[n] * m
      m += 1
      n -= 3
    return x
  return sum(H(i) for i in range(3,12346))

def pjeuler587():
  def get_x(n):
    nom = - math.sqrt(2) * n**(3/2) + n**2 + n
    den = n**2+1
    return nom/den

  def indefinite_integral(x):
    return 0.5 * (math.sqrt(x*(2-x)) - x * (math.sqrt(x*(2-x))-2) + 2*math.asin(math.sqrt(1 - x/2)))

  def area2(x):
    return indefinite_integral(1) - indefinite_integral(x)

  def area1(x,n):
    return 0.5 * x * x/n

  def area(n):
    x = get_x(n)
    return area1(x,n) + area2(x)

  def ratio(n):
    return area(n) / (1-math.pi/4) - 0.001

  n1 = 1
  n2 = 10000
  while True:
    n = round((n1+n2)/2)
    a = ratio(n)
    if a > 0:
      n1 = n
    else:
      n2 = n
    if n1+1==n2:
      return n2

def pjeuler808():
  from .tools import primes
  s = 0
  n = 0
  for i in primes(100_000_000):
    x = int(str(i**2)[::-1])
    j = round(x**.5)
    if j**2 == x:
      if i != j:
        if sympy.isprime(j):
          n += 1
          s += i**2
          if n == 50:
            return s