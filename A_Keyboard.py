a = "qwertyuiop"
b = "asdfghjkl;"
c = "zxcvbnm,./"

d = input()
s = input()
prt = ''
if d == "R":
    for i in s:
        if i in a:
            prt += a[a.index(i)-1]
        elif i in b:
            prt += b[b.index(i)-1]
        elif i in c:
            prt += c[c.index(i)-1]
elif d == "L":
    for i in s:
        if i in a:
            prt += a[a.index(i)+1]
        elif i in b:
            prt += b[b.index(i)+1]
        elif i in c:
            prt += c[c.index(i)+1]
print(prt)