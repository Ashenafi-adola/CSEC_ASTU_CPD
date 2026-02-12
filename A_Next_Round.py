n, k = map(int, input().split())
scr = input()
scrs = list(map(int, scr.split()))
print(scrs)

advance = 0
for i in scrs:
    if i >= scrs[k-1]:
        advance += 1

print(advance)