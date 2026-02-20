t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    d.sort()
    tr = 0
    nw = 0
    cur = d[0]
    for i in d:
        if tr > nw:
            nw = tr
        if i - cur <= k:
            tr += 1
        else:
            tr = 1
    print(n - nw-1)