import math

def area_minus(i):
  return (3*i-1)*(i+1)*(i-1)*(i-1) in numbers

def area_plus(i):
  return (3*i+1)*(i-1)*(i+1)*(i+1) in numbers

s = 0
N = int(1e10)

numbers = set([16*i**2 for i in range(1,N)])

for i in range(2,math.ceil(N/3)):
  if area_minus(i):
    print(i)
    s += 3*i-1
  if area_plus(i):
    print(i)
    s += 3*i+1