t = int(input())
for i in range(t):
    n = int(input())
    s = list(input())
    d = len(s)
    b = -1
    fr = 0
    pr = 0
    while s[b] != s[fr] and d != 0:
        d -= 2
        b -= 1
        fr += 1
        pr += 2
    print(n - pr)
