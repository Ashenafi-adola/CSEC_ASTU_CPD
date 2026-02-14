n = int(input())
ns = list(map(int, input().split()))
m = int(input())
main = []
for i in range(m):
    main.append(list(map(int, input().split())))
if len(ns) > 1:
    for j in main:
        if j[0] == 1:
            ns[1] += ns[0] - j[1]
            ns[0] = 0
        elif j[0] == n:
            ns[n-2] += ns[n-1] - (ns[j[0]-1] - j[1]) - 1
        else:
            ns[j[0]-2] += ns[j[0]-1] - (ns[j[0]-1] - j[1]) - 1
            ns[j[0]] +=  ns[j[0]-1] - j[1]
        ns[j[0] - 1] = 0
    for i in ns:
        print(i)
else:
    for i in main:
        if i[0] == 1:
            print(0)
            break
    if len(main) == 0:
        print(ns[0])
