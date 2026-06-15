s, n = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    if s > x:
        s += y
    else:
        print("NO")
        break
else:
    print("YES")