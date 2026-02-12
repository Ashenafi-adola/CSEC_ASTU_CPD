a, b = map(int, input().split())

n = 0
k = True
while k:
    n += 1
    if (n*a)%10 == 0:
        k = False

    elif (n*a - b)%10 == 0:
        k=False

print(n)