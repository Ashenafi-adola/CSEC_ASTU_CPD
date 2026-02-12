n = int(input())
ns = list(map(int, input().split()))

unt = 0
i = 0
m = 0
while i < n-1:
    print(i)
    if ns[i] > 0 and ns[i+1] > 0:
        k = 0
        j = i
        while ns[j] > 0:
            m += ns[j]
            j += 1
            k += 1
        for i in range(m):
            if ns[j] < 0:
                m -= 1
            else:
                m += 1
            k += 1
        i += k
    elif ns[i] < 0 and m == 0:
        unt += 1
        i += 1
        
print(unt) 
