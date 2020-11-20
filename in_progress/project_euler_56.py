sum = 0
for a in range(101):
    for b in range(101):
        val = a ** b
        s = str(val)
        ss = 0
        for c in s:
            ss += int(c)
        sum = max(sum,ss)
print(sum)