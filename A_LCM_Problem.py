t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    pr = True
    for j in range(a, b+1):
        if j*2 <= b:
            print(j, j*2)
            pr = False
            break
        else:
            break
    if pr:
        print(-1,-1)