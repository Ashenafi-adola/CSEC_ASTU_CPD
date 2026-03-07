t = int(input())
for i in range(t):
    n = int(input())
    if n <= 2:
        print("NO")
    else:
        if n%4 == 0:
            print("YES")
            d = 0
            for j in range(1, int(n/2)+1):
                print(2*j, end=' ')
                d += 2*j
            k = 0
            for j in range(1, int(n/2)):
                print(2*j-1, end=' ')
                k += 2*j - 1
            print(d - k)
        else:
            print("NO")