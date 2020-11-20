from collections import Counter


def is_pandigital(x):
    a = '123456789'
    return len(x) == 9 and Counter(x) == Counter(a)


for i in range(1,10000):
    a = ''
    for j in range(1,10):
        a += str(i*j)
        if is_pandigital(a):
            print(a)