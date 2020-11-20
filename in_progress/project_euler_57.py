num = 1
den = 1

counter = 0
for i in range(1000):

    print(num, den, num/den)
    if len(str(num)) > len(str(den)):
        counter += 1

    num_1 = num + den
    den_1 = den

    num_2 = den_1
    den_2 = num_1

    num = num_2 + den_2
    den = den_2

print(counter)