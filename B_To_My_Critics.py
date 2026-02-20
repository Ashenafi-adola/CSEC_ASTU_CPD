t = int(input())
k = []
for _ in range(t):
    k.append(list(map(int, input().split())))
for i in k:
    for j in range(3):
        if i[0] + i[1] >= 10 or i[0] + i[2] >=10 or i[1] + i[2] >= 10:
            print("YES")
            break
        else:
            print("NO")
            break