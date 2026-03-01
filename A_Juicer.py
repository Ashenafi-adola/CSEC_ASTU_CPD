n, b, d = map(int, input().split())
li = list(map(int, input().split()))
su = 0
j = 0
for i in li:
    if i <= b:
        su += i
    if su > d:
        su = 0
        j += 1
print(j)