def f(v):
    if len(v) == 2:
        a = v[0]
        b = v[1]
        up = a * b + 1
        down = b
    else:
        a = v.pop(0)
        u, d = f(v)
        up = a * u + d
        down = u
    return up, down


N = 100
w = [1]*N
w[0] = 2
for i in range(1, N):
    if i % 3 == 0:
        w[i-1] = round(i/3*2)

uu, dd = f(w)

print(sum(int(digit) for digit in str(uu)))