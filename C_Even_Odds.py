n, k = map(int, input().split())
h = 0
if n % 2 == 0:
    h = n//2
else:
    h = n//2 + 1

if k <= h:
    print(k + (k-1))
else:
    print(2*(k-h))