t = int(input())
for i in range(t):
    s = list(input())
    j = min(s.count('0'), s.count('1'))
    if j%2 == 0:
        print("NET")
    else:
        print("DA")