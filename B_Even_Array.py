t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rec = []
    res = []
    mv = 0
    for i in range(n):
        rec.append(i%2)
        res.append(a[i]%2)
    if rec == res:
        print(0)
    elif rec.count(1) == res.count(1):
        for i, j in zip(rec, res):
            if i != j:
                mv += 1
        print(int(mv/2))
    else:
        print(-1)