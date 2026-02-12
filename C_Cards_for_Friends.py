n = int(input())

main = []
for i in range(n):
    main.append(list(map(int, input().split())))

for i in main:
    if i[0]%2 == 0 or i[1]%2 == 0:
        if i[0]*i[1] >= i[2]:
            print("YES")
        else:
            print("NO")
    elif i[0]%2 != 0 and i[1]%2 != 0:
        if i[2] == 1:
            print("YES")
        else:
            print("NO")
