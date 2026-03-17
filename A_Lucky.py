t = int(input())
for i in range(t):
    a = list(map(int, list(input())))
    if sum(a[:3]) == sum(a[3:]):
        print("YES")
    else:
        print("NO")