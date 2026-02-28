t = int(input())
for i in range(t):
    n = int(input())
    n2 = list(map(int, input().split()))
    ev = 0
    for k in n2:
        if k%2 == 0:
            ev += 1
    if ev == n:
        print("Yes")
    else:
        print("No")