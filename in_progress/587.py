from math import sqrt, pi
from numpy import arcsin

def get_x(n):
  nom = -sqrt(2) * n**(3/2) + n**2 + n
  den = n**2+1
  return nom/den

def indefinite_integral(x):
  return 0.5 * (sqrt(x*(2-x)) - x * (sqrt(x*(2-x))-2) + 2*arcsin(sqrt(1 - x/2)))

def area2(x):
  return indefinite_integral(1) - indefinite_integral(x)

def area1(x,n):
  return 0.5 * x * x/n

def area(n):
  x = get_x(n)
  return area1(x,n) + area2(x)

def ratio(n):
  return area(n) / (1-pi/4)

# bisect to 0.001