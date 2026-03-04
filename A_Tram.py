n = int(input())
pr = 0
re = 0
for i in range(n):
    a, b = map(int, input().split())
    re += b - a
    if re > pr:
        pr = re
print(pr)