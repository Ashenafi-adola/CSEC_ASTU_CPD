n = int(input())
a = list(map(int, input().split()))
s = sum(a)
h = s/2
i = 0
if n == 1:
    print(1, 0)
elif n == 2: 
    print(1, 1)
else:
    while s > h:
        s -= a[i]
        i += 1
    if s == h:
        print(i, n - i)
    elif h*2 - (s + a[i - 1]) <= s:
        print(i, n - i)
    else:
        print(i - 1, n - (i - 1))