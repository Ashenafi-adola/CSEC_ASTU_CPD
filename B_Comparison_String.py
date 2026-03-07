t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    gt = 0
    lt = 0
    g = 0
    l = 0
    for j in s:
        if j == '>':
            g += 1
            if g > gt:
                gt = g
            l = 0
        else:
            l += 1
            if l > lt:
                lt = l
            g = 0
    print(max(gt, lt)+1)