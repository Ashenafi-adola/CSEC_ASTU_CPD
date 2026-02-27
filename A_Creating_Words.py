t = int(input())
for i in range(t):
    a, b = map(list, input().split())
    a0 = a[0]
    b0 = b[0]
    a[0] = b0
    b[0] = a0
    print(''.join(a), ''.join(b))