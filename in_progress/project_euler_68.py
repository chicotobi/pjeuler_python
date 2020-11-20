z = range(1, 10)
for a in z:
    for b in z:
        if a != b:
            S = 10 + a + b
            for f in z:
                if f not in [a, b]:
                    for c in z:
                        if c not in [a, b, f] and f + b + c == S:
                            for g in z:
                                if g not in [a, b, c, f]:
                                    for d in z:
                                        if d not in [a, b, c, f, g] and g + c + d == S:
                                            for e in z:
                                                if e not in [a, b, c, d, f, g]:
                                                    for h in z:
                                                        if h not in [a, b, c, d, e, f, g] and d + e + h == S:
                                                            for i in z:
                                                                if i not in [a, b, c, d, e, f, g, h] and a + e + i == S:
                                                                    if f == min([f, g, h, i]):
                                                                        print(f, b, c, g, c, d, h, d, e, i, e, a, 10, a,
                                                                              b)
                                                                    if g == min([f, g, h, i]):
                                                                        print(g, c, d, h, d, e, i, e, a, 10, a, b, f, b,
                                                                              c)
                                                                    if h == min([f, g, h, i]):
                                                                        print(h, d, e, i, e, a, 10, a, b, f, b, c, g, c,
                                                                              d)
                                                                    if i == min([f, g, h, i]):
                                                                        print(i, e, a, 10, a, b, f, b, c, g, c, d, h, d,
                                                                              e)
