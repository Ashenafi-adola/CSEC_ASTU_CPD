n = int(input())

s = input().upper()

rm = 0
for i in range(n - 1):
    if s[i] == s[i+1]:
        rm += 1
    
print(rm)