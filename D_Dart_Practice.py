t = int(input())
for i in range(t):
    total = 0
    for j in range(1,11):
        s = input().lower()
        for k in range(1, 11):
            if s[k-1] == 'x':
                if j > 5:
                    j = 5 - (j - 6)
                if k > 5:
                    k = 5 - (k - 6)
                total += min(j, k)
    print(total)