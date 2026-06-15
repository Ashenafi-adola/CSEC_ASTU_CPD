n = input()
a = []
for i in n:
    if i not in a:
        a.append(i)
if len(a) == 2 and '4' in a and '7' in a:
    print("YES")
elif int(n)%4 == 0 or int(n)%7 == 0:
    print("YES")
else:
    print("NO")