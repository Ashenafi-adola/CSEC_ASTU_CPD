t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if 2 in a:
        if a.count(2)%2 == 0:
            d = a.count(2)/2
            k = 0
            j = 0
            g = 0
            while k < d:
                if a[j] == 2:
                    g = j+1 
                    k += 1
                j += 1
            print(g)
        else:
            print(-1)
    else:
        print(1)