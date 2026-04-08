n = int(input())
a = list(map(int, input().split()))

ma = a[0]
mi = a[0]
mai = 0
mii = 0
for i,j in enumerate(a):
    if j > ma:
        ma = j
        mai = i
    if j <= mi:
        mi = j
        mii = i
if mii < mai:
    print(mai + (n - 1)-mii-1)
else:
    print(mai + ((n-1)-mii))
