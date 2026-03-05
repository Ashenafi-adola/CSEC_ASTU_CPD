a = "abcdefghijklmnopqrstuvwxyz"
s = input()
d = ''
k = 0
for i in s:
    if i in a and i not in d:
        d += i
        k += 1
print(k)