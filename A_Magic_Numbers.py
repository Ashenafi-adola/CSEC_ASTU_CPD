n = input()
if n[0] == '4' or '444' in n or n.count('1') + n.count('4') != len(n):
    print("NO")
else:
    print("YES")
