t = int(input())
for i in range(t):
    n, k, x = map(int, input().split())
    if x >= n:
        if n*(n+1)/2 - (n-k)*((n-k) + 1)/2 >= x:
            print("YES")
        else:
            print("NO")
    elif x < k:
        if k*(k+1)/2 > x:
            print("NO")
    else:
        print("NO")