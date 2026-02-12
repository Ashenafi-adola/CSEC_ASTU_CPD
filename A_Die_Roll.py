a, b = map(int, input().split())

poss = [1, 2, 3, 4, 5, 6]
nw = []

for i in poss:
    if i >= a and i >= b:
        nw.append(i)

if len(nw) == 3:
    print('1/2')
elif len(nw) == 2:
    print("1/3")
elif len(nw) == 0:
    print("0/1")
elif len(nw) == 4:
    print('2/3')
elif len(nw) == 1:
    print('1/6')
elif len(nw) == 5:
    print('5/6')
elif len(nw) == 6:
    print("1/1")