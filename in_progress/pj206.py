a = 1020304050607080900
b = 1929394959697989990

a = round(a**.5)
b = round(b**.5)

for x in range(a,b,10):
  y = x**2
  success = True
  for i in range(9):
    y = y//100
    if y%10 != 9-i:
      success = False
      break
  if i>6:
    s = str(x**2)
    print(s[::2])
  if success:
    print(x)
    break
    
