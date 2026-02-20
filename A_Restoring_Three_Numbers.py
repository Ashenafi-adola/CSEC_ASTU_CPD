k = list(map(int, input().split()))
a = max(k)
d = []
for i in k:
    if i != a:
        d.append(a-i)
d.reverse()
for j in d:
    print(j, end=" ")