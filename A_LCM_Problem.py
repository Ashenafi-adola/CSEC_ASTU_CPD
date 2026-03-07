t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    pr = True
    for j in range(a+1, b+1):
        if j%a == 0:
            print(a, j)
            pr = False
            break
    if pr:
        print(-1,-1)