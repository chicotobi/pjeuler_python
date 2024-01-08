tuples = dict()
tuples[5] = []
tuples[6] = [(1,1,1,1,1,1)]

N = 20

for i in range(7,N+1):
    new = []
    #print(i)
    
    # Add from two below by adding 2 in any of the three directions
    for j in tuples[i-2]:
        new1 = (j[0]+1,j[1]  ,j[2]  ,j[3]+1,j[4]  ,j[5]  )
        new2 = (j[0]  ,j[1]+1,j[2]  ,j[3]  ,j[4]+1,j[5]  )
        new3 = (j[0]  ,j[1]  ,j[2]+1,j[3]  ,j[4]  ,j[5]+1)
        new += [new1,new2,new3]
        
    # Add from one below
    for j in tuples[i-1]:
        if j[0] > 1:
            tmp = (j[0]-1,j[1]+1,j[2]  ,j[3]  ,j[4]  ,j[5]+1)
            new += [tmp]
        if j[1] > 1:
            tmp = (j[0]+1,j[1]-1,j[2]+1,j[3]  ,j[4]  ,j[5]  )
            new += [tmp]
        if j[2] > 1:
            tmp = (j[0]  ,j[1]+1,j[2]-1,j[3]+1,j[4]  ,j[5]  )
            new += [tmp]
        if j[3] > 1:
            tmp = (j[0]  ,j[1]  ,j[2]+1,j[3]-1,j[4]+1,j[5]  )
            new += [tmp]
        if j[4] > 1:
            tmp = (j[0]  ,j[1]  ,j[2]  ,j[3]+1,j[4]-1,j[5]+1)
            new += [tmp]
        if j[5] > 1:
            tmp = (j[0]+1,j[1]  ,j[2]  ,j[3]  ,j[4]+1,j[5]-1)
            new += [tmp]
    
    # Remove identicals
    newnew = []
    for j in new:
        if (j[0],j[1],j[2],j[3],j[4],j[5]) in newnew:
            continue
        if (j[1],j[2],j[3],j[4],j[5],j[0]) in newnew:
            continue
        if (j[2],j[3],j[4],j[5],j[0],j[1]) in newnew:
            continue
        if (j[3],j[4],j[5],j[0],j[1],j[2]) in newnew:        
            continue
        if (j[4],j[5],j[0],j[1],j[2],j[3]) in newnew:
            continue
        if (j[5],j[0],j[1],j[2],j[3],j[4]) in newnew:
            continue
        
        if (j[5],j[4],j[3],j[2],j[1],j[0]) in newnew:
            continue
        if (j[0],j[5],j[4],j[3],j[2],j[1]) in newnew:
            continue
        if (j[1],j[0],j[5],j[4],j[3],j[2]) in newnew:
            continue
        if (j[2],j[1],j[0],j[5],j[4],j[3]) in newnew:
            continue
        if (j[3],j[2],j[1],j[0],j[5],j[4]) in newnew:
            continue
        if (j[4],j[3],j[2],j[1],j[0],j[5]) in newnew:
            continue
        newnew += [j]
        
    tuples[i] = newnew
    
from math import floor

def formula(n):
    return floor((2*n**3 + 45*n**2 + (273 + 96*(floor(n/3) - floor((n-1)/3)))*n + 1284 + 3*(3*n**2 + 45*n + 148)*(-1)**n)/1728)

def H2(n):
    return sum(formula(i) for i in range(n-5))

S = [len(v) for (k,v) in tuples.items() if k<=N]
print("S:",S)
H = [sum(len(v) for (k,v) in tuples.items() if k<i) for i in range(5,N+1) ]
print("H:",H)