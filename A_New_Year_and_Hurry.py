n, k = map(int, input().split())
m = 240 - k
d = 0
i = 0
while d <= m:
    i += 1
    d += i*5
    if d > m:
        break
print(i)