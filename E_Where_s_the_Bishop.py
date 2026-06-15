t = int(input())
for i in range(t):
    count = 0
    c = True
    for j in range(9):
        s = input()
        if s.count("#") == 1 and count == 2:
            if c:
                print(j, s.index('#') + 1)
                c = False
        count = s.count('#')
            