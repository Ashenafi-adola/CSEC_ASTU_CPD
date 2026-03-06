n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a1 = a[1:]
b1 = b[1:]
if len(set(a1 + b1)) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")