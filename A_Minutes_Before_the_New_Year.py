n = int(input())
for i in range(n):
    h, m = map(int, input().split())
    print(1440 - (h*60 + m))
