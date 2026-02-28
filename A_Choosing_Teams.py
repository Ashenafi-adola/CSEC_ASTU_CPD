n, k = map(int, input().split())
a = list(map(int, input().split()))
par = []
for i in a:
    if 5 - i >= k:
        par.append(i)
print(int(len(par)//3))