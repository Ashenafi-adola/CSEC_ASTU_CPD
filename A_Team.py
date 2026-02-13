n = int(input())
rt = 0
for i in range(n):
    if sum(map(int, input().split())) >= 2:
        rt += 1
 
print(rt)