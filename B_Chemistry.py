t = int(input())
l = []
r = []
for i in range(t):
    n, k = map(int, input().split())
    s = list(input())
    for i in s:
        if i not in l:
            l.append(i)
            r.append(s.count(i))
    r.sort()
    for i in range(len(r)):
        if k == 0:
            break
        if r[i]%2 == 0 and k >= 2:
            r[i] -= 2
            k -= 2
        else:
            r[i] -= 1
            k -= 1
    if r.count(1) > 1 and sum(r) > 1:
        print("NO")
    