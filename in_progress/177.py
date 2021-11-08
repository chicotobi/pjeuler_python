import math
import functools

@functools.lru_cache(None)
def si(x):
    return math.sin(x/180*math.pi)

@functools.lru_cache(None)
def co(x):
    return math.cos(x/180*math.pi)

s = []
for a in range(1,179):      
    print(a)
    for c in range(1,179):
        b = 180 - a - c
        if b>1:
            for d in range(1,180-a):
                for e in range(1,180-c):
                    f = 180 - d - e
                    if f>1:        
                        nom = si(a+d)
                        den = si(e)*si(b)/si(f)/si(c)-co(a+d)
                        x = math.atan2(nom,den)*180/math.pi
                        if abs(round(x)-x)<1e-5:
                            x = int(x)
                            y = 180 - a - d - x
                            if x > 0 and f-x > 0 and y > 0 and b-y > 0:
                                check_val  = si(f)*si(c)*si(y)-si(b)*si(e)*si(x)
                                if abs(check_val) < 1e-9:
                                  s += [(d,a,y,b-y,c,e,f-x,x)]
                    
t = set()
for (a,b,c,d,e,f,g,h) in s:
    if (a,b,c,d,e,f,g,h) in t or (c,d,e,f,g,h,a,b) in t or (e,f,g,h,a,b,c,d) in t or (g,h,a,b,c,d,e,f) in t:
        continue
    if (h,g,f,e,d,c,b,a) in t or (f,e,d,c,b,a,h,g) in t or (d,c,b,a,h,g,f,e) in t or (b,a,h,g,f,e,d,c) in t:
        continue
    t.add((a,b,c,d,e,f,g,h))
print(len(t))
    
