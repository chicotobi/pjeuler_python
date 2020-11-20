import pandas as pd


def value(word):
    s = 0
    for l in range(len(word)):
        s += ord(word[l])-64
    return s


tris = []
for i in range(1,30):
    tris.append(int(0.5*i*(i+1)))

df = pd.read_csv('p042_words.txt')
s = df.columns.values.tolist()

counter = 0
for word in s:
    if value(word) in tris:
        counter += 1
print(counter)