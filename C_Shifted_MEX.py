t = int(input())
for k in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = set(a)
    c = list(b)
    c.sort()
    if c[0] == 0:
        for i in range(len(c)+1):
            if i not in c:
                print(i)
                break
    elif c[0] > 0:
        for i in range(len(c) + 1):
            if i + c[0] not in c:
                print(i)
                break
    elif c[0] < 0:
        d = abs(c[0])
        for i in range(len(c)):
            c[i] = c[i] + d
        for i in range(len(c) + 1):
            if i not in c:
                print(i)
                break   