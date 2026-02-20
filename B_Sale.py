n, m = map(int, input().split())
k = list(map(int, input().split()))
k.sort()
sum = 0
for i in range(m):
    if k[i] < 0:
        sum += k[i]
print(-sum)