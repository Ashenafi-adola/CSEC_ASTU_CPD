n = int(input())
ls = []
for i in range(n):
    ls.append(input())
gp = 1
for i in range(n-1):
    if ls[i] != ls[i+1]:
        gp += 1
print(gp)
