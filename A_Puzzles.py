n , m = map(int, input().split())
f = list(map(int, input().split()))
f.sort()
mn = max(f) - min(f)
for i in range(m-n+1):
    k = f[i:i+n]
    d = max(k) - min(k)
    if d < mn:
        mn = d
print(mn)