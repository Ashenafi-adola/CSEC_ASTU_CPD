t = int(input())
name = "Trumi"
for i in range(t):
    l = int(input())
    s = input()
    pr = 'YES'
    if len(s) != len(name):
        print("NO")
        continue
    for j in name:
        if j not in s:
            pr = "NO"
            break
    print(pr)