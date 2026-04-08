t = int(input())
for i in range(t):
    n = int(input())
    s = ''
    for j in range(n,0,-1):
        s += f' {j}'
    print(s)