t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = a[0]
    for j in a:
        k &= j
    print(k)