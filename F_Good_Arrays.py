t = int(input())
k = ''
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) == 1:
        k = "NO"
    elif len(a) == 2 and len(set(a)) == 2:
        k ="YES"
    elif len(set(a)) >= len(a)/2:
        k ="YES"
    else:
        k = "NO"
    print(k)