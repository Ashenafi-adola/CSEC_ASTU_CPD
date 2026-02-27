t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = a.copy()
    be = 0
    en = 0
    if k not in a:
        print('NO')
        continue
    if a.count(k) == 1:
        print("YES")
        continue
    for j in range(n):
        if b[j] == k:
            be = j
            break
    for j in range(n-1, 0, -1):
        if a[j] == k:
            en = j
            break
    c = b[be:en+1]
    nk = c.count(k)
    tobe = 'YES'
    for d in c:
        if d != k and c.count(d) >= nk:
            tobe = "NO"
            break
    print(tobe)