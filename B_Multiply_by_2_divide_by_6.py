t = int(input())
main = []
for _ in range(t):
    main.append(int(input()))

for j in main:
    mv = 0
    i = j
    while True:
        if i == 2 or i > j*2:
            print(-1)
            break
        if i == 1:
            print(mv)
            break
        elif i%6 == 0:
            i = i/6
        else:
            i = i*2
        mv += 1