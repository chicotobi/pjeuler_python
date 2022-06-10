import functools

def party(s, P, res):
    res.append(P+[s])
    for i in range(1,len(s)):
        res = party(s[i:],P+[s[:i]],res)
    return res

@functools.lru_cache(None)
def indices(n):
    l = 'abcdefghijkl'
    l = l[:n]
    res = party(l,[],[])
    return [[ord(j[0])-97 for j in i] for i in res]

def split_str_by_idx(s,indices):
    return [s[i:j] for i,j in zip(indices, indices[1:]+[None])]

def check(i):
    kstr = str(i**2)    
    
    idxs = indices(len(kstr))
    for idx in idxs:
        res = split_str_by_idx(kstr,idx)
        s = sum(int(i) for i in res)
        if s == i:
            #print(i, res)
            return True
    return False

n = int(1e6)
s = 0
for i in range(2,n+1):
    if check(i):
        print(i,i**2)
        s += i**2
print(s)
  