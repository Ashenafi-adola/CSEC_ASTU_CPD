t = int(input())
for i in range(t):
    s = input()
    cdf = "codeforces"
    n = 0
    for i, j in zip(s, cdf):
        if i != j:
            n += 1
    print(n)