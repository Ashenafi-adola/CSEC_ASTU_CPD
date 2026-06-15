n = int(input())
m = n + 1
for i in range(m):
    print(2*(n-i)*" "+"0",*range(1,i+1), *range(i-1, -1, -1))
for i in range(n):
    print(2*(i+1)*" "+"0", *range(1,n-i), *range(n-i-2, -1, -1))