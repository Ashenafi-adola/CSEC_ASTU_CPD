n, m = map(int, input().split())
pr = ""
if n <= m:
    if n%2 == 0:
        pr = "Malvika"
    else:
        pr = "Akshat"
else:
    if m%2 == 0:
        pr = "Malvika"
    else:
        pr = "Akshat"
print(pr)