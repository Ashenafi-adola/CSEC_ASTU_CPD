t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    if a[2] < a[0] < a[1] < a[3] or a[2] < a[1] < a[0] < a[3]:
        print("NO")
    if a[3] < a[0] < a[1] < a[2] or a[3] < a[1] < a[0] < a[2]:
        print("NO")
    if a[0] < a[0] < a[1] < a[1] or a[0] < a[1] < a[0] < a[1]:
        print("NO")
    if a[1] < a[2] < a[3] < a[0] or a[0] < a[2] < a[3] < a[1]:
        print("NO")
    else:
        print("YES")