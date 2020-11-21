from math import floor, sqrt


def fraction(v):
    if len(v) == 2:
        a = v[0]
        b = v[1]
        up = a * b + 1
        down = b
    else:
        a = v.pop(0)
        u, d = fraction(v)
        up = a * u + d
        down = u
    return up, down


def kettenbruch(n, m):
    ll = []
    a = floor(sqrt(n))
    b = a
    c = 1
    init = []
    counter = 0
    while counter < m:
        an = floor((sqrt(n) + b) * c / (n - b * b))
        cn = (n - b * b) / c
        bn = an * cn - b

        ll.append(a)

        a = int(an)
        b = int(bn)
        c = int(cn)
        counter += 1
    return ll


for i in range(2, 1000):
    if round(i**.5)**2 == i:
        continue
    for j in range(2, 100):
        ll = kettenbruch(i, j)
        up, down = fraction(ll)
        x = up
        y = down
        if x * x - i * y * y == 1:
            print("D: "+str(i)+" x: "+str(x))
            break
