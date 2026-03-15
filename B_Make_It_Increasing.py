t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = 0
    a.reverse()
    for j in range(n-1):
        while a[j] <= a[j+1]:
            if a[j+1] == 0:
                k = -1
                break
            a[j+1]//=2
            k += 1
        if k == -1:
            break
    print(k)