t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    if (2*b - c)%a == 0 and 2*b != c and a != b:
        print("YES")
    elif (a+c)%(2*b) == 0:
        print("YES")
    elif (2*b - a)%c == 0 and 2*b != a:
        print("YES")
    else:
        print("NO")