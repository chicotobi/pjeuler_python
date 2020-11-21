import math
import functools
import itertools
import collections
import numpy as np

def pjeuler(i):
  return eval("pjeuler"+str(i)+"()")

def get(i):
  import os.path
  return open(os.path.dirname(__file__)+'/input/'+str(i))
  
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
  l = list(primes(100000))
  best = 0
  prod = 0
  for a in range(-1000,1000):
    for b in p:
      for n in range(1,1000):
        if f(a,b,n) not in l:
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
  from .tools import pentagonal_numbers, is_pentagonal
  l = []
  min_distance = 1e10
  for i in pentagonal_numbers():
    if i>1e8:
      break
    l += [i]
    for j in l:
      if is_pentagonal(i-j) and is_pentagonal(i+j) and i-j<min_distance:
        min_distance=i-j
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
  from .tools import smart_mod
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
