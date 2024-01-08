def intersections(rx2, ry2, x0, y0, xd, yd):
    t2 = rx2*yd*yd + ry2*xd*xd
    t1 = rx2*y0*yd + ry2*x0*xd
    t0 = rx2*y0*y0 + ry2*x0*x0 - rx2*ry2
    ca = t1 / t2
    cb = (t1*t1 - t0*t2)**.5 / t2
    return cb - ca, -cb - ca

def ellipsereflect(rx2, ry2, x, y, xd, yd):
    ca = x*x*ry2*ry2
    cb = y*y*rx2*rx2
    cc = x*y*rx2*ry2
    cd = (ca + cb) / 2
    return xd - (xd * ca + yd * cc) / cd, yd - (xd * cc + yd * cb) / cd

rx = 5
ry = 10

x0 = 0
y0 = 10.1

x2 = 1.4
y2 = -9.6

d = ((x2-x0)*(x2-x0)+(y2-y0)*(y2-y0))**.5

xd = (x2-x0) / d
yd = (y2-y0) / d

x = ( x0 + x2 ) / 2
y = ( y0 + y2 ) / 2

f = open("test.svg", "w")

f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="%.0f %.0f %.0f %.0f">\n' % (-rx-1, -ry-1, 2*rx+2, 2*ry+2))
f.write('<ellipse cx="0" cy="0" rx="%.3f" ry="%.3f" fill="#ffffff" stroke="#000000" stroke-width="0.01" />\n' % (rx, ry))
f.write('<path d="M%.3f%+.3f' % (x, y))
i = 0
xmin = 10
while True:
    t1, t2 = intersections(rx*rx, ry*ry, x, y, xd, yd)
    t = max(t1, t2)

    x += t * xd
    y += t * yd
    xmin = min(abs(x),xmin)
    f.write(' L%.3f%+.3f' % (x, -y))
    if abs(x) < 0.01 and y > 0:
        break
    i += 1
    xd, yd = ellipsereflect(rx*rx, ry*ry, x, y, xd, yd)
f.write('" fill="none" stroke="#0000ff" stroke-width="0.01" />\n')
f.write('</svg>\n')
f.close()
print(i)