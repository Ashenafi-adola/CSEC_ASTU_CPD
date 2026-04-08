n = int(input())
a = list(map(int, input().split()))
ch = 0
bi = 0
ba = 0
j = 1
for i in range(n):
    if j == 1:
        ch += a[i]
        j += 1
    elif j == 2:
        bi += a[i]
        j += 1
    else:
        ba += a[i]
        j = 1
if max(ch, bi, ba) == ch:
    print("chest")
elif max(ch, bi, ba) == ba:
    print("back")
else:
    print('biceps')