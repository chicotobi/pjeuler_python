def reverse(x):
    y = 0
    while x>9:
        y = 10 * y + (x%10)
        x = x // 10
    return 10*y+x

def only_odd_digits(x):
    while x>0:
        d = x%10
        if d==0 or d==2 or d==4 or d==6 or d==8:
            return False
        x = x // 10
    return True

N = int(1e9)
s = 0
for i in range(1,N):
    if i%1000000==0:
        print(i/N)
    if i%10!=0:
      v = i + reverse(i)
      if only_odd_digits(i+reverse(i)):
        s += 1
print(s)