t = int(input())
for i in range(t):
    a, b, n = map(int, input().split())
    lis = list(map(int, input().split()))
    pr = b - 1
    for j in lis:
        if j <= a:
            pr += j
        else:
            pr += a
    print(pr)