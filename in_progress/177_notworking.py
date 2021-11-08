import math

tri = []
s = 0
for a in range(1,179):
    for b in range(a,179):
        c = 180 - a - b
        if c>=b:
            tri += [(a,b,c)]

def si(x):
  return math.sin(x/180*math.pi)

def co(x):
  return math.cos(x/180*math.pi)

def at(x):
  return math.atan(x)*180/math.pi
        
s = []
for (a,b,c) in tri:
    for (d,e,f) in tri:
        x = at(si(a+d)/(co(a+d)+si(e)*si(b)/si(f)/si(c)))
        if abs(round(x)-x)<1e-9:
            x = round(x)
            y = 180 - a - d - x
            s += [(d,a,y,b-y,c,e,f-x,x)]
        