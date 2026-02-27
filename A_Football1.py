s = input()
ret = "NO"
if len(s) < 7:
    print(ret)
else:
    for i in range(len(s)-6):
        k = s[i:i+7]
        if k.count('0') == 7 or k.count('1') == 7:
            ret = "YES"
            break
    print(ret)