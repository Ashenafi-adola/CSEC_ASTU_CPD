from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = Counter(a)
    for j in b:
        if b[j] == 1:
            print(a.index(j)+1)
            break