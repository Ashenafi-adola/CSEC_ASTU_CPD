t = int(input())
for _ in range(t):
    ss= []
    for i in range(9):
        s = input()
        if s.strip() != '':
            ss.append(s)
    for i in ss:
        if i == 'RRRRRRRR' :
            print('R')
            break
        elif i == 'BBBBBBBB':
            print('B')
            break
    else:
        for i in range(8):
            a = ss[1][i]
            if a != '.':
                for j in ss:
                    if j[i] != a:
                        break
                else:
                    print(a)
                    break