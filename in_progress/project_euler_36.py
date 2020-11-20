vals = 0

for n in range(1,1000000):
    s = str(n)
    if s == s[::-1]:
        t = bin(n)[2:]
        if t == t[::-1]:
            vals += n
            print(n,t)
print(vals)