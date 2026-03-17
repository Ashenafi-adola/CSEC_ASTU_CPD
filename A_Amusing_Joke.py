s1 = input()
s1 += input()
s = input()
if len(s) == len(s1):
    for i in s:
        if s1.count(i) != s.count(i):
            print('NO')
            break
    else:
        print("YES")
else:
    print("NO")