from itertools import combinations
from collections import Counter
from numpy import prod
from math import factorial

# pe 491
# Possible splits are 23 : 67, 34 :  56, 45 : 45

def number_of_permutations_without_leading_zero(x):
    zeroes = sum(1 for i in x if i==0)
    if zeroes > 0:
        x1 = [i for i in x if i!=0] + (zeroes-1) * [0]
        return number_of_permutations(x) - number_of_permutations(x1)
    else:
        return number_of_permutations(x)

def number_of_permutations(x):
    nom = int(factorial(len(x)))
    denom = int(prod(list(factorial(i) for i in Counter(x).values())))
    return nom//denom

vals = range(20)
x = list(combinations(vals,10))
y = list(tuple(i for i in vals if i not in j) for j in x)

vals2 = list(range(10))*2
x2 = [tuple(vals2[i] for i in j) for j in x]
y2 = [tuple(vals2[i] for i in j) for j in y]



z = list(zip(x2,y2))

z = [(i,j) for (i,j) in z if sum(i) in [23,34,45,56,67]]

s = 0
for (i, el) in enumerate(z):
    x, y = el
    m = number_of_permutations_without_leading_zero(x)
    n = number_of_permutations(y)
    if m < 1e5 or n < 1e5:
        print(x,y,m,n)
    k = m*n
    s += m*n
print(s)