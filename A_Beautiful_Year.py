n = input()
a = int(n)
while True:
    a += 1
    j = 1
    for i in str(a):
        if str(a).count(i) > j:
            j = str(a).count(i)
    if j == 1:
        break
print(a)