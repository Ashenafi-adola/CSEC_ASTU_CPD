n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))
for i in d:
    print(1440 - (i[0]*60 + i[1]))
