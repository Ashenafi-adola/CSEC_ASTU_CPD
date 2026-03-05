a = int(input())
b = int(input())
c = int(input())
pr = 0
if (a + b + c) > pr:
    pr = (a + b + c)
if (a * b * c) > pr:
    pr = (a * b * c)
if a + (b * c )> pr:
    pr = a + (b * c)
if (a + b) * c > pr:
    pr = (a + b) * c
if (a * b) + c > pr:
    pr = a * b + c
if (a * c) + b > pr:
    pr = a * c + b
if a * (b + c) > pr:
    pr = a * (b + c)
    


print(pr)