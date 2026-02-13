n = int(input())
 
a = list(map(int, input().split()))
 
a.sort()
s = str(a[0])
 
for i in range(1, len(a)):
    s += f' {a[i]}'
    
print(s)