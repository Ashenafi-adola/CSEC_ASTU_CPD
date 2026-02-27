t = int(input())
for i in range(t):
    n = input()
    na = int(n)
    k = len(n) - 1
    le = 0
    while True:
        k -= 1
        m = int(n[0:k])
        print(m)
        if na%m == 0:
            le = len(n[:k])
            break
        
    print(le)