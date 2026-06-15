t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for j in a:
        s += abs(j)
    ops = 0
    seqs = []
    while True:
        for j in range(1, n+1):
            if a[j-1] > 0 :
                if j not in seqs:
                    seqs.append(j)
                    ops += 1
                for k in range(j):
                    a[k] = -a[k]
        if sum(a) == -s:
            break
    print(ops)
    for j in seqs:
        print(j, end=' ')
    print()