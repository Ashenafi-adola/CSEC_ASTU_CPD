n, h = map(int, input().split())
hs = list(map(int, input().split()))
wd = 0
for i in hs:
    if i <= h:
        wd += 1
    elif i%h == 0:
        wd += int(i/h)
    else:
        wd += int(i/h) + 1
print(wd)
