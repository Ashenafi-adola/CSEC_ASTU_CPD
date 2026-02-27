n = int(input())
k = 0
if n % 2 == 0:
    k = n/2
else:
    k = n//2 - n
print(int(k))