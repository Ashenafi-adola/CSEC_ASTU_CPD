n = int(input())
main = []

k = 0
for i in range(n):
    main.append(list(map(int, input().split())))

for i in main:
    for j in main:
        if j is not i:
            if i[0] == j[1]:
                k += 1

print(k)