t = int(input())
for _ in range(t):
    c = [1]
    n, m = map(int, input().split())
    c.extend(list(map(int, input().split())))
    b = list(map(int, input().split()))
    c.sort()
    b.sort()
    p1, p2 = 0, 0
    counter = 0
    while p1 < n and p2 < n:
        if b[p2] > c[p1]:
            p1 += 1
            p2 += 1
        else:
            p2 += 1
            counter += 1
    print(counter)