t = int(input())
for i in range(t):
    n, a, b = map(int, input().split())
    if n % 2 == 0:
        if 2*a > b:
            print((n//2)*b)
        elif 2*a <= b:
            print(n*a)
    else:
        if 2*a > b:
            k = n - 1
            print((n//2)*b + a)
        else:
            print(n*a)