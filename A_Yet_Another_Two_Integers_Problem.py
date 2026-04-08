t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    mv = 0
    d = abs(a - b)
    if d % 10 == 0:
        print(d//10)
    else:
        print(d//10 + 1)