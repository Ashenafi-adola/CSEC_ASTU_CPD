t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = a.copy()
    b.sort()
    if k > 1 or a == b:
        print("YES")
    else:
        print("NO")