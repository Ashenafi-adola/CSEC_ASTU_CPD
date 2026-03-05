n = int(input())
s = list(input().lower())

if len(set(s)) == 26:
    print("YES")
else:
    print("NO")