n = int(input())
d = list(map(int, input().split()))
for i in d:
    ma = d[n-1] - d[0]
    ind = d.index(i)
    if ind == 0:
        mi = d[1] - i
    elif ind == n-1:
        mi = i - d[n-2]
    else:
        mi = min(i - d[ind-1], d[ind+1] - i)
        ma = max(i - d[0], d[n-1] -i)
    print(mi, ma)