import pandas as pd

def value(word):
    s = 0
    for l in range(len(word)):
        s += ord(word[l])-64
    return s


df = pd.read_csv('p022_names.txt')
s = df.columns.values.tolist()
s.sort()

sum = 0
for i in range(len(s)):
    sum += (i+1) * value(s[i])
print(sum)