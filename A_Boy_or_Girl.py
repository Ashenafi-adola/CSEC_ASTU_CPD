s = input()
ls = []
for i in range(len(s)):
    ls.append(s[i])
for i in range(len(s)):
    n = ls.count(s[i])
    if n > 1:
        for j in range(n-1):
            ls.remove(s[i])
k = len(ls)
if k%2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
