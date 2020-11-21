from math import floor,sqrt

big_counter = 0
for n in range(10000):
    if floor(sqrt(n))**2==n:
        continue
    a = floor(sqrt(n))
    b = a
    c = 1
    init = []
    counter = 0
    while True:
        an = floor((sqrt(n)+b)*c/(n-b*b))
        cn = (n-b*b)/c
        bn = an *cn - b

        a = int(an)
        b = int(bn)
        c = int(cn)
        if init == []:
            init = [a,b,c]
        elif [a,b,c]==init:
            print(n, counter)
            break
        counter += 1
    if counter % 2:
        big_counter += 1
print(big_counter)