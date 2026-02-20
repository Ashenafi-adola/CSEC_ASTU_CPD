t = int(input())
for i in range(t):
    k = 2
    x = 1
    n = int(input())
    while True:
        if n%(2**k - 1) == 0:
            x = n/(2**k - 1)
            break
        k += 1
    print(int(x))