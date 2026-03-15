t = int(input())
for i in range(t):
    a, b, n = map(int, input().split())
    lis = list(map(int, input().split()))
    d = b
    for j in lis:
        d += min(j, a-1)
    print(d)