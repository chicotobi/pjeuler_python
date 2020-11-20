import numpy as np

N = 10000

perms = [[1,2,3,4],
         [1,2,4,3],
         [1,3,2,4],
         [1,3,4,2],
         [1,4,2,3],
         [1,4,3,2],
         [2,1,3,4],
         [2,1,4,3],
         [2,3,1,4],
         [2,3,4,1],
         [2,4,1,3],
         [2,4,3,1],
         [3,1,2,4],
         [3,1,4,2],
         [3,2,1,4],
         [3,2,4,1],
         [3,4,1,2],
         [3,4,2,1],
         [4,1,2,3],
         [4,1,3,2],
         [4,2,1,3],
         [4,2,3,1],
         [4,3,2,1],
         [4,3,1,2]
         ]

# generate some primes
primes = []
a = np.ones(N,dtype=np.int32)
a[0] = 0
idx = 0
while True:
    while idx < N-1 and a[idx]==0:
        idx += 1
    if idx == N-1:
        break
    p = idx+1
    primes.append(p)
    a[p-1::p] = 0
print('Done generating primes.')

print(primes)

for p in primes:
    strp = str(p)
    if len(strp) == 4:
        counter = 1
        cur_list = [p]
        for perm in perms:
            perm_strp = strp[perm[0]-1] + strp[perm[1]-1] + strp[perm[2]-1] + strp[perm[3]-1]
            if perm_strp[0] != '0':
                perm_p = int(perm_strp)
                if perm_p in primes and perm_p not in cur_list:
                    cur_list.append(perm_p)
                    counter += 1
        if counter > 2:
            diffs = []
            cur_list.sort()
            for i in range(len(cur_list)):
                for j in range(i+1,len(cur_list)):
                    for k in range(j+1,len(cur_list)):
                        if cur_list[k]-cur_list[j] == cur_list[j]-cur_list[i]:
                            print(cur_list[i],cur_list[j],cur_list[k])