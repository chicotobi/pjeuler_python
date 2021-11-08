score_pete = [0]*37
for i1 in range(1,5):
  for i2 in range(1,5):
    for i3 in range(1,5):
      for i4 in range(1,5):
        for i5 in range(1,5):
          for i6 in range(1,5):
            for i7 in range(1,5):
              for i8 in range(1,5):
                for i9 in range(1,5):
                  score_pete[i1+i2+i3+i4+i5+i6+i7+i8+i9] += 1/(4**9)

score_colin = [0]*37
for i1 in range(1,7):
  for i2 in range(1,7):
    for i3 in range(1,7):
      for i4 in range(1,7):
        for i5 in range(1,7):
          for i6 in range(1,7):
                  score_colin[i1+i2+i3+i4+i5+i6] += 1/(6**6)
                  
p_pete_beats_colin = 0
for res1 in range(1,37):
  for res2 in range(res1+1,37):
    p_pete_beats_colin += score_colin[res1]*score_pete[res2]