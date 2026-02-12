s = input()

lets = "abcdefghijklmnopqrstuvwxyz"

cur = 0
r, l = 0, 0
mv = 0
for i in s:
    iind = lets.index(i)
    if iind == cur:
        pass
    if iind >= 13 and cur < 13:
        r = len(lets[iind:26]) + len(lets[0:iind])
        l = len(lets[iind:cur])
        if l < r:
            mv += l
            print('l1+')
        else:
            mv += r
            print('r1+')
    elif iind < 13 and cur >= 13:
        l = len(lets[0:iind]) + len(lets[cur:26]) 
        r = len(lets[iind: cur])
        if l < r:
            mv += l
            print('l2+')
        else:
            mv += r
            print('r2+')
    else:
        if cur > iind:
            mv += len(lets[iind: cur])
            print('l')
        else:
            mv += len(lets[cur:iind])
            print('r')
    cur = iind
print(mv)