import math
import functools
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
  from .tools import factors
  @functools.lru_cache(None)
  def f(x):
    y=collections.Counter(factors(x))
    return np.prod([(p**(n+1)-1)/(p-1) for (p,n) in y.items()])-x
  s = 0
  for i in range(2,10000):
    j = f(i)
    if i<j and f(j)==i:
      s += i+j
  return int(s)

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
