t = int(input())

for i in range(1, t+1):
    sc = 0
    for j in range(10):
        s = input().lower()
        if j < 5:
            try:
                sc += min(s.index('x')+1, j +1)
            except:
                pass
        else:
            try:
                sc += min(s.index('x'), (j-5)+1)
            except:
                pass
    print(sc)
