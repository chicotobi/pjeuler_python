import numpy as np

f = open('p059_cipher.txt')
arr = f.readlines()[0].split(',')
arr = [int(a) for a in arr]
arr = np.asarray(arr)

for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            my_key = [a,b,c]*485
            my_key = np.asarray(my_key)

            sol1 = np.bitwise_xor(arr,my_key)
            sol = [chr(a) for a in sol1]
            sol = ''.join(sol)
            if 'that' in sol and 'have' in sol:
                print(a,b,c)
                print(sum(sol1))
                print(sol)
