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
  print(min_distance)
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
  from .tools import continued_fraction_period_length
  return sum([1 for i in range(10000) if continued_fraction_period_length(i)%2])

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

def pjeuler77():
  from .tools import write_as_prime_sum
  i = 2
  while write_as_prime_sum([],i,i)<=5000:
    i += 1
  return i

def pjeuler85():
  f = lambda a,b: a*(a+1)*b*(b+1)/4
  for i in range(100):
    for j in range(100):
        if(abs(f(i,j)-2000000)<1e3):
            return i*j
          
def pjeuler97():
  from .tools import smart_mod
  mod = int(1e10)
  return (28433*smart_mod(2,7830457,mod)+1)%mod
