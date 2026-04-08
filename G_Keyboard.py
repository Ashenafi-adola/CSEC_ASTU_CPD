p = input()
s = input()

a = "qwertyuiop asdfghjkl; zxcvbnm,./"
pr = ''
if p == "R":
    for i in s:
        d = a.index(i)
        pr += a[d - 1]
    print(pr)
else:
    for i in s:
        d = a.index(i)
        pr += a[d + 1]
    print(pr)