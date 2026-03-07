t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    k = a%b
    if k != 0:
        print(b-k)
    else:
        print(0)