import sys
input = sys.stdin.readline
n, t = map(int, input().split())
a = list(map(int, input().split()))

books = 0
s = 0
l = 0
for r in range(n):
    s += a[r]
    while s > t:
        s -= a[l]
        l += 1
    books = max(books, r-l+1)
print(books)