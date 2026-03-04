n = int(input())
pr = 0
for i in range(n):
    p, q = map(int, input().split())
    if q - p >= 2:
        pr += 1
print(pr)