t = int(input())
for i in range(t):
    n = input()
    if len(n) >= 4 and int(n) >= 2020:
        d = int(n)
        while d >= 2020:
            if d%2020 == 0 or d%2021 == 0:
                d = 0
                break
            if d%10 == 0:
                d -= 2020
            else:
                d -= 2021
        if d == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")