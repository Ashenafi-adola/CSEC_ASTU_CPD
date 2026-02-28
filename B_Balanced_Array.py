t = int(input())
for i in range(t):
    n = int(input())
    k = n
    if n <= 2:
        print("NO")
    else:
        while n > 0:
            if n%4 != 0:
                break
            n /= 4
            m = n
        if int(m) == 1:
            print("YES")
            j = list(range(2, k + 1, 2))
            l = list(range(1, k-2, 2))
            d = j + l + [sum(j) - sum(l)]
            for c in d:
                print(c, end=' ')
            print('')
        else:
            print("NO")