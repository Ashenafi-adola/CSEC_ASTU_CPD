t = int(input())
for i in range(t):
    n, a = map(int, input().split())
    b = list(map(int, input().split()))
    for j in range(n):
        l,r,k = map(int, input().split())
        ls = sum(b[:l+1]) + sum(b[r:])

        if ls%2 == 0 and (k%2 != 0 and (r-l)%2 != 0):
            print("YES")
        elif ls%2 == 0 and (k%2 == 0 or (r-l)%2 == 0):
            print("NO")
        elif ls%2 != 0 and (k%2 == 0 and (r-l)%2 == 0):
            print("NO")