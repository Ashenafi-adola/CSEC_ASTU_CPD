t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    for j in a:
        if j != max(a) and j != min(a):
            print(j)
            break