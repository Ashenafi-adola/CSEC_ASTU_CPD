t = int(input())
for j in range(t):
    n = input()
    m = int(n)
    li = []
    l = len(n)
    for i in range(l):
        k = int(n[i])*10**(l - (i+1))
        if k != 0:
            li.append(k)
    print(len(li))
    for i in li:
        print(i, end=' ')
    print('')