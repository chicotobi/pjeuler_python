from sympy import isprime

def sum_digits(x):
  return sum(int(i) for i in str(x))

def is_harshad(x):
  y = sum_digits(x)
  return (x // y) * y == x

# First, generate all right truncatable Hashard numbers?
right_truncatable_harshad = list(range(1,10))
tmp = right_truncatable_harshad

for n in range(12):
  tmp2 =  []
  for i in tmp:
    for j in range(10):
      x = i * 10 + j
      if is_harshad(x):
        tmp2 += [x]
  right_truncatable_harshad += tmp2
  tmp = tmp2

strong_right_truncatable_harshad = [i for i in right_truncatable_harshad if isprime(i // sum_digits(i))]

s = 0
for i in strong_right_truncatable_harshad:
  for j in range(10):
    x = i * 10 + j
    if isprime(x):
      if x < 1e14:
        s += x
print(s)