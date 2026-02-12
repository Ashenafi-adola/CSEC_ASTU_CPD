n, m = map(int, input().split())
s = n 
k = 1
d = 0
while True:
    #print(s)
    if d == m:
        d = 0
        s += 1
    s -= 1
    d += 1
    
    if s == 0:
        break
    k += 1

print(k)