t = int(input())

for i in range(t):
    pr = 0
    l = list(map(int, input().split()))
    for j in range(1, 4):
        if l[j] > l[0]:
            pr += 1
    print(pr)
