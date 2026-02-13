s = input()

lets = "abcdefghijklmnopqrstuvwxyz"
cur = 0
r, l = 0, 0
mv = 0
for i in s:
    iind = lets.index(i)
    if iind == cur:
        pass
    if iind > 12 and cur < 12:
        r = len(lets[cur:iind])
        l = len(lets[0:cur])+len(lets[iind-1:25])
        if l < r:
            mv += l
        else:
            mv += r
    elif iind < 12 and cur > 12:
        l = len(lets[0:iind]) + len(lets[cur:26]) 
        r = len(lets[iind: cur])
        if l < r:
            mv += l
        else:
            mv += r
    else:
        if cur > iind:
            mv += len(lets[iind: cur])
        else:
            mv += len(lets[cur:iind])
    cur = iind
print(mv)