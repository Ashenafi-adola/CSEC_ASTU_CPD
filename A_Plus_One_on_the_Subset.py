t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = max(a)
    c = min(a)
    print(b-c)