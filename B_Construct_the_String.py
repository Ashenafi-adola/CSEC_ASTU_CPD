t = int(input())
lets = "qwertyuioplkjhgfdsazxcvbnm"
for i in range(t):
    n, a, b = map(int, input().split())
    temp = ''
    for j in range(b):
        temp += lets[j]
    s = ''
    j = 0
    while len(s) < n:
        if j == len(temp):
            j = 0
        s += temp[j]
        j += 1
    print(s)

