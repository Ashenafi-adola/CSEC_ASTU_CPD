n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l.sort()
for i in range(1, n):
    if l[i][1] < l[i-1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")