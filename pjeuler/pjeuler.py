import math
import functools
import itertools
import collections
import numpy as np

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
  a = f.read()
  f.close()
  return max([np.prod(digits(a[i:i+13])) for i in range(len(a)-13)])

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
  @functools.lru_cache(None)
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
  @functools.lru_cache(None)
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
  @functools.lru_cache(None)
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
  @functools.lru_cache(None)
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
  import pjeuler, math, functools
  fac = [math.factorial(i) for i in range(10)]

  @functools.lru_cache(None)
  def f(x):
    return sum([fac[i] for i in pjeuler.digits_int(x)])

  @functools.lru_cache(None)
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
  @functools.lru_cache(None)
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
  @functools.lru_cache(None)
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
  @functools.lru_cache(None)
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
  @functools.lru_cache(None)
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
  from .tools import digits_int
  @functools.lru_cache(None)
  def f(x):
    return sum(np.array(digits_int(x))**2)
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
  return sum(np.array(l)==2)

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

