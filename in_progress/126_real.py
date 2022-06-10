def calc(a,b,c,n):
    return 2*(a*b+a*c+b*c) + 4 * (n-1) * (a+b+c+n-2)

vol_max = 200000
counter_max = 20000

counter = [0]*counter_max

for a in range(1,vol_max+1):
    for b in range(1,min(vol_max//a,a+1)):
        for c in range(1,min(vol_max//(a*b),b+1)):
            n = 1
            while True:
                v = calc(a,b,c,n)
                if v >= counter_max:
                    break
                counter[v] += 1
                n += 1

for (i,v) in enumerate(counter):
    if v==1000:
        print(i)
        break

for i in [22,46,78,118,154]:
    print(i,counter[i])
