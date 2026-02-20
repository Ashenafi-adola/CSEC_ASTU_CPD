t = int(input())
out = []
for _ in range(t):
    a, b, c = map(int, input().split())
    n = 2*abs(a - b)
    dif = int(n/2)
    if a > n or b > n or c > n:
        print(-1)
    else:
        if c <= dif and dif != 1:
            print(c+dif)
        elif c > dif and c <= n and dif != 1:
            print(c-dif)
        else:
            print(-1)