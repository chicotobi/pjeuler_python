counter = 0
for a in range(1,40):
    for b in range(1,40):
        val = a**b
        if len(str(val))==b:
            print(a, b,val,len(str(val)))
            counter += 1
print('number is',counter)