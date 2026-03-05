t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    e = []
    o = []
    if n == 1:
        print("NO")
    else:
        for j in a:
            if j % 2 == 0:
                e.append(j)
            else:
                o.append(j)
        if sum(o)%2 == 0:
            print("YES")
        else:
            print("NO")