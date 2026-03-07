n = int(input())
a = list(map(int, input().split()))
x = max(a)
mn = min(a)
ix = a.index(x)
a.reverse()
im = a.index(mn)
im = (n-1) - im

if ix > im:
    print(ix + (n-2-im))
elif ix < im:
    print(ix + (n-1-im))
else:
    print(0)
