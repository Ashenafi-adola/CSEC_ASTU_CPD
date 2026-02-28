t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    x = 0
    y = 0
    for j in s:
        if j == 'U':
            y += 1
        elif j == 'D':
            y -= 1
        elif j == 'R':
            x += 1
        elif j == 'L':
            x -= 1
        if x == 1 and y == 1:
            break
    if x == 1 and y == 1:
        print("YES")
    else:
        print("NO")