s1 = list(map(str, input()))
s2 = list(map(str, input()))

s2.reverse()
if s2 == s1:
    print("YES")
else:
    print("NO")

