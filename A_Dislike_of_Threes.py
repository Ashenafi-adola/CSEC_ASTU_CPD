t = int(input())
for i in range(t):
    k = int(input())
    tr = 1
    pr = 1
    while tr < k:
        if pr % 3 == 0 or str(pr)[-1] == 3:
            pr += 1
        if pr % 3 == 0 or str(pr)[-1] == 3:
            pr += 1
        pr += 1
        tr += 1
        
    print(pr)