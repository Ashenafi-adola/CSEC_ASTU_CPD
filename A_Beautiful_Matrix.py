ls = []
for i in range(5):
    b = []
    b = list(map(int, input().split()))
    ls.append(b)
mv = 0
k = []
for i in ls:
    if 1 in i:
        k = i
        id = ls.index(i)
        if id == 4 or id == 0:
            mv += 2
        elif id == 1 or id == 3:
            mv += 1
for i in k:
    if i == 1:
        ind = k.index(i)
        if ind == 4 or ind == 0:
            mv += 2
        elif ind == 1 or ind == 3:
            mv += 1
print(mv)
