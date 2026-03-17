n = int(input())
if n <= 5:
    print(0)
else:
    for i in range(1,n+1):
        am = 0
        k = 0
        for j in range(2, n):
            