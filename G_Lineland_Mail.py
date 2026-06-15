n = int(input())
ar = list(map(int, input().split()))
for i in range(n):
    if i == 0:
        print(ar[1] - ar[i], ar[n-1] - ar[0])
    elif i == n-1:
        print(ar[n-1] - ar[n-2], ar[n-1] - ar[0])
    else:
        print(min(ar[i+1] - ar[i], ar[i] - ar[i-1]), max(ar[i] - ar[0], ar[n-1]-ar[i]))