s = input()
d = []
for i in s:
    d.append(i)
if int(s)>0:
    print(int(s))
else:
    if len(s) > 1:
        if int(d[-2]) > int(d[-1]):
            d.pop(-2)
        else:
            d.pop()
    k = ''
    for j in d:
        k += j
    print(int(k))