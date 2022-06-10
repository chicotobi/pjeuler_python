import functools

N = 10000

@functools.lru_cache(None)
def canmake(total, digs):
    if digs < total:
        return False
    elif digs == total:
        return True
    else:
        t = 10
        while t < digs:
            cutoff = digs // t
            rest = digs % t
            if rest < total:
                if canmake(total - rest, cutoff):
                    return True
            t *= 10
    return False

total = 0
for n in (range(1_000_001)):
    if n%1000 == 0:
        print(n)
    if canmake(n, n*n):
        total += n*n
print(total-1)