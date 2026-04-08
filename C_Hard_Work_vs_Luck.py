n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

h = sum(a)//2
s = 0
t = 0
for i in a:
    t += 1
    s += i
    if s > h:
        print(t)
        break
print("security")