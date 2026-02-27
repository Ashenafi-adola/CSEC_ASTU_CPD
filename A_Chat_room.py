s = list(input())
a = 'hello'
k = s.copy()
s.reverse()
for i in a:
    print(s)
    if i != 'l':
        while s.count(i) > 1:
            s.remove(i)
    else:
        while s.count(i) > 2:
            s.remove(i)
for j in k:
    print(s)
    if j not in a:
        s.remove(j)
s.reverse()
print(s)
if s == list(a):
    print("YES")
else:
    print("NO")