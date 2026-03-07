t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    pr = True
    if len(a) == 1:
        print("YES")
    else:
        for j in range(1, len(a)):
            if a[j] - a[j-1] > 1:
                pr = False
                break
        if pr:
            print("YES")
        else:
            print("NO")