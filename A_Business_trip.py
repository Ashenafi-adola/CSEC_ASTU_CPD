k = int(input())
mon = list(map(int, input().split()))
mon.sort(reverse=True)
n = 0
l = 0
for i in mon:
    if n < k:
        l += 1
        n += i
    else:
        break
if n < k:
    print(-1)
else:
    print(l)