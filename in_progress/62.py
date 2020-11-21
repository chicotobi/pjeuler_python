n = 1
stop = False
for digits in range(1,20):
    arr = []
    d = {}
    while True:
        val = n**3
        if len(str(val)) > digits:
            break
        s = ''.join(sorted(str(val)))
        if s not in d:
            d[s] = []
        d[s].append(val)
        n += 1
    for key in d:
        if len(d[key])==5:
            print(key,d[key])
            stop = True
    if stop:
        quit()
