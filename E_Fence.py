n, k = map(int, input().split())
a = list(map(int, input().split()))
mi = sum(a[0:k])
pr = 1
s = sum(a[:k])
for i in range(1, n-k+1):
    s = s - a[i-1] + a[i+k-1]
    if s < mi:
        pr = i+1
        mi = s
print(pr)