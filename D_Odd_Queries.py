t = int(input())
for i in range(t):
    n, q = map(int, input().split())
    d = list(map(int, input().split()))
    for i in range(q):
        l, r, k = map(int, input().split())
        s = sum(d) - sum(d[l-1:r]) + (r-l+1)*k
        if s%2 == 0:
            print("NO")
        else:
            print("YES")