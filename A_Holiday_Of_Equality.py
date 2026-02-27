n = int(input())
a = list(map(int, input().split()))
m = max(a)
b = 0
for i in a:
    if i != m:
        b += m-i

print(b)