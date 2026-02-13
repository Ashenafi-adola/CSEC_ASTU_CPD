ss = list(map(int, input().split()))
us = []
for i in ss:
    if i not in us:
        us.append(i)
print(4 - len(us))