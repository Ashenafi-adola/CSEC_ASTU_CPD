n = int(input())
ns = list(map(int, input().split()))
m = 0
ns.reverse()
if n > 1:
    while True:
        if len(ns) == 0 or ns[0] < 0:
            break
        if ns[0] > 0:
            ns.remove(ns[0])
    for i in range(len(ns)):
        if m + ns[i] <= 0:
            m += ns[i]
        elif ns[i] >= -m:
            m = 0
    if m <= 0:    
        print(-(m)) 
    else:
        print(0)
else:
    if ns[0] == -1:
        print(1)
    else:
        print(0)
