s = input()
if s[0] == s[0].lower() and s[1:] == s[1:].upper():
    print(s.swapcase())
elif s == s.upper():
    print(s.swapcase())
else:
    print(s)