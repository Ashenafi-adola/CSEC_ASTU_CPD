q = int(input())
for i in range(q):
    n = int(input())
    s, t =map(list, input().split())
    if s.sort() == t.sort():
        print("YES")
    else:
        print("NO")