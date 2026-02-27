t = int(input())
for i in range(t):
    n = int(input())
    if n%2 != 0:
        print("YES")
    else:
        while True:
            n = int(n/2)
            if n % 2 != 0 and n > 1:
                print("YES")
                break
            if n == 1:
                print("NO")
                break