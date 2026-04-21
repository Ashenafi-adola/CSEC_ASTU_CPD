t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    tr = set()
    for j in range(1,n+1):
        tr.add(s[j-2:j])
    print(len(tr)-1)
