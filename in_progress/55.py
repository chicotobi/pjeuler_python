

n_lychrel = 0
for i in range(10000):
    lychrel = True
    val = i
    for counter in range(51):
        str_val = str(val)
        rev = str_val[::-1]
        if rev == str_val and counter>0:
            print(counter, rev)
            lychrel = False
            break
        else:
            val += int(rev)
    if lychrel:
        n_lychrel += 1
        print(i)
print(n_lychrel)
