n = int(input())
d = list(map(int, input().split()))
cur = d[0]
nw = 0
tr = 0
for i in d:
    if i >= cur:
        tr += 1
    if tr > nw:
        nw = tr
    if i < cur:
        tr = 1
    cur = i
print(nw)