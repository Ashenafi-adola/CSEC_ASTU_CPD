t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sum(a)
    c = set(a)
    o = 0
    e = 0
    for j in c:
        if j%2 == 0:
            e += 1
        else:
            o += 1
    if o > 0 and e > 0:
        print("YES")
    elif b%2 == 0:
        print("NO")
    else:
        print("YES")