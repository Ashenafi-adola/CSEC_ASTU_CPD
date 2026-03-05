n = int(input())
li = list(map(int, input().split()))
li.sort()
if n <= 2 or li[0] == li[n-1]:
    print(0)
else:
    c = li.count(li[n- 1])
    b = li.count(li[0])
    print(len(li) - (b+c))