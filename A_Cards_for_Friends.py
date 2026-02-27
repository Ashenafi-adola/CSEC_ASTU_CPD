t = int(input())
for i in range(t):
    w, h, n = map(int, input().split())
    a = 1
    b = 1
    if w%2 == 0 and h%2 == 0:
        while w%2 == 0 and w != 0:
            w = w/2
            a *= 2
        while h%2 == 0 and h != 0:
            h = h/2
            b *= 2  
    elif h%2 == 0:
        while h%2 == 0 and h != 0:
            h = h/2
            b *= 2
    elif w%2 == 0:
        while w%2 == 0 and w != 0:
            w = w/2
            a *= 2  
    if a*b >= n:
        print("YES")
    else:
        print("NO")