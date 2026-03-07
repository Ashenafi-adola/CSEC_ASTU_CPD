t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = list(input())
    d = ''
    a = []
    b = 0
    for j in s:
        if j not in d:
            d += j
            c = s.count(j)
            if c%2 != 0:
                b += 1
    if max(0, b - 1) <= k:
        print("YES")
    else:
        print("NO")