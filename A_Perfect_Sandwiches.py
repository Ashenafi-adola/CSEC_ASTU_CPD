t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if b >= a:
        print(-1)
    else:
        if a%b == 0 or a/b >= 2:
            print(b)
        else:
            print(a%b)