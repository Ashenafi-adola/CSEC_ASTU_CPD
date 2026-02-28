t = int(input())
for i in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    sp = 0
    pr = 0
    for j in ar:
        if j == 0:
            sp += 1
        else:
            if sp > pr:
                pr = sp
            sp = 0
    if sp > pr:
        pr = sp
    print(pr)