cals = list(map(int, input().split()))
s = input()
tocals = 0
lis = []
for i in s:
    lis.append(int(i))
for i in lis:
    tocals += cals[i-1]
print(tocals)
