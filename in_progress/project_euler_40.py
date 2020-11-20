s = ''
c = 1
while len(s)<1e6:
    s += str(c)
    c += 1

a = 1
a *= int(s[1 -1])
a *= int(s[10-1])
a *= int(s[100-1])
a *= int(s[1000-1])
a *= int(s[10000-1])
a *= int(s[100000-1])
a *= int(s[1000000-1])
print(a)
