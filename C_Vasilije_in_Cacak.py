t = int(input())
for i in range(t):
    n, k, x = map(int, input().split())
    d = n*(n+1)/2
    e = (n-k)*((n-k) + 1)/2
    c = (k)*(k+1)/2
    if d < x or x < c or d - e < x:
        print("NO")
    else:
        print("YES")