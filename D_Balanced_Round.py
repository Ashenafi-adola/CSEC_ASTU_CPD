t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    d.sort()
    a = 0
    b = 0
    for i in range(1, n):
        if d[i] - d[i-1] <= k:
            a += 1
        else:
            if a >= b:
                b = a
            a = 0
    if a >= b:
        b = a
    print(n - (b+1))