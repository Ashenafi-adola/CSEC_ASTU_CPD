t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    ma = 0
    for i in range(1,n):
        a = set(s[:i])
        b = set(s[i:])
        if len(a) + len(b) > ma:
            ma = len(a) + len(b)
        if ma == 26:
            break
    print(ma)