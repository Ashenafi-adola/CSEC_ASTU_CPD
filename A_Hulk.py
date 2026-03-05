n = int(input())
a1 = 'I hate '
a2 = 'I love '
a = ''
for i in range(n):
    if i%2 == 0:
        a += a1
    else:
        a += a2
    if i == n-1:
        a += 'it'
        break
    a += 'that '
print(a)