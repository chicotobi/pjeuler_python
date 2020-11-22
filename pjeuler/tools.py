import numpy as np	
import math
import collections
import functools
import string
import sympy.ntheory.primetest

def fib(n):
  arr = [1,1]
  for i in range(n-2):
    arr = arr+[arr[-2]+arr[-1]]
  return arr[0:n]

def fib2():
  a = 1
  yield a
  b = 1
  yield 1
  while True:
    [a,b] = [b,a+b]
    yield b

def primes(limit):
    a = [True] * (limit+1)
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit+1, i):
                a[n] = False

def factors(m):
  if m<1:
    return []
  if m==1:
    return [1]
  n = math.floor(m**.5)
  f = []
  for p in primes(n):
    while m % p == 0:
        m /= p
        f.append(p)
    if(m==1):
      break
  if m != 1:
      f.append(int(m))
  return f

def n_divs(m):
  f = factors(m)
  return np.prod(np.fromiter(collections.Counter(f).values(),dtype="int")+1)

def lettervalue(word):
  return sum(string.ascii_uppercase.index(c)+1 for c in word)

def is_palindrome(n):
    return str(n)==str(n)[::-1]

def lcm(*args):
    if len(args)>1:
        args = list(args)
    else:
        args = args[0]
    l = [collections.Counter(factors(x)) for x in args]
    r = functools.reduce(lambda a,b:a|b,l)
    return np.prod([x**y for (x,y) in r.items()])

def gcd(*args):
    if len(args)>1:
        args = list(args)
    else:
        args = args[0]
    l = [collections.Counter(factors(x)) for x in args]
    r = functools.reduce(lambda a,b:a&b,l)
    return np.prod([x**y for (x,y) in r.items()])
    
def digits(s):
    return [int(a) for a in s]

def collatz(n):
  if n%2 == 0:
    return int(n/2)
  else:
    return 3*n+1
  
def nchoosek(n,k):
  return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
  
def triangle_numbers():
  i = 0
  m = 1
  while True:
    i += m
    yield i
    m += 1
    
def num2word(num):
    wrds = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    wrds_2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if num == 1000:
        return 'one thousand'
    s = ''
    a = math.floor(num / 100)
    if a > 0:
        s += wrds[a-1] + ' hundred'
    b = num % 100
    if b == 0:
        return s
    if a > 0:
        s += ' and '
    if b < 20:
        s += wrds[b-1]
        return s
    c = math.floor(b/10)
    d = b % 10
    s += wrds_2[c-2]
    if d == 0:
        return s
    s += '-' + wrds[d-1]
    return s
  
def write_as_prime_sum(l,n,maxp):
  ps = primes(maxp)
  vals = 0
  for p in ps:
    if p==n:
      l.append(n)
      #print("+".join([str(a) for a in l]))
      vals += 1
    elif p<n:
      vals += write_as_prime_sum(l+[p], n-p,p)
  return vals

@functools.lru_cache(None)
def digits_int(x):
  l = []
  while x>9:
    l.append(x%10)
    x = x//10
  l.append(x)
  l.reverse()
  return l

def digits2int(x):
  return functools.reduce(lambda a,b:10*a+b,x)

def int2base(x, base):
    digs = string.digits + string.ascii_letters
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

def smart_mod(base,exp,mod):
  b = digits(int2base(exp,2)[::-1])

  a = [base%mod]
  for i in range(len(b)-1):
    a.append((a[-1]**2)%mod)
  
  v = np.array(a)[np.array(b)==1]
  w = functools.reduce(lambda x,y:smart_mod_prod(x,y,mod),v)
  return w

def smart_mod_prod(x,y,mod):
  v = [x]+factors(y)
  return functools.reduce(lambda x,y:x*y%mod,v)

@functools.lru_cache(None)
def sum_divs(x):
  y=collections.Counter(factors(x))
  return int(np.prod([(p**(n+1)-1)/(p-1) for (p,n) in y.items()])-x)

def periodic_decimal(denom):
  l = []
  if denom in [2,5]:
    return l
  nom = 1
  while True:
    nom *= 10
    l = l+[nom//denom]
    nom = nom%denom
    if nom==1:
      break
  return l

def is_pentagonal(x):
  n = 1/6*((24*x+1)**.5+1)
  return abs(n-round(n))<1e-8 
 
def is_triangle(x):
  n = 1/2*((8*x+1)**.5-1)
  return abs(n-round(n))<1e-8  

def pentagonal_numbers():
  i=0
  while True:
    i +=1
    yield int(i*(3*i-1)/2)
    
def hexagonal_numbers():
  i = 0
  while True:
    i += 1
    yield i*(2*i-1)
  
def is_prime(val):
  for i in range(2,round(val**0.5)+1):
      if not val%i:
          return False
  return True

@functools.lru_cache(None)
def is_prime_mr(val):
  return sympy.ntheory.primetest.mr(val,[2,3,5,7])