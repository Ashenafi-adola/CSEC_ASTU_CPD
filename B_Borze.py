s = input()
l = len(s)
i = 0
r = ''
while i < l:
    if s[i] == '.':
        r += '0'
        i += 1
    elif s[i:i+2] == '--':
        r += '2'
        i += 2
    elif s[i:i+2] == '-.':
        r += '1'
        i +=2
print(r)