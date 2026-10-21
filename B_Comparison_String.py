t = int(input())
for _ in range(t):
    n = int(input())
    l = 1
    s = input()
    mx = 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            l += 1
            if l > mx:
                mx = l
        else:
            l = 1
    print(mx+1)