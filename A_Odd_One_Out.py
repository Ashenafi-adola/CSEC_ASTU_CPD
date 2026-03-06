t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    for j in a:
        if a.count(j) == 1:
            print(j)
            break