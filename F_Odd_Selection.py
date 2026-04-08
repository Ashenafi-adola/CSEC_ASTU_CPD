t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    countod = 0
    countev = 0
    for j in a:
        if j % 2 != 0:
            countod += 1
        else:
            countev += 1

    if x%2 != 0 and countod >= x:
        print("Yes")
    elif x%2 == 0 and countev > 0 and countod >= x-1:
        print("Yes")
    else:
        print("No")