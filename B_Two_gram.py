n = int(input())
s = input()
m = []
for i in range(n-1):
    m.append(s[i:i+2])
na = ''
ma = 0
for i in m:
    if m.count(i) > ma:
        na = i
        ma = m.count(i)
print(na)
