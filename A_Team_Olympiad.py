from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a1 = a.count(1)
a2 = a.count(2)
a3 = a.count(3)
teams = min(a1, a2, a3)
ind = []
child = []
for j,i in enumerate(a, 0):
    if child.count([i,j]) < teams:
        child.append([i,j])

print('\n')
for i in child:
    print(i)