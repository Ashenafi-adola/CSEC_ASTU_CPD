t = int(input())
for i in range(t):
    k = int(input())
    tr = []
    for i in range(10000):
         j = str(i)
         if i%3 == 0 or j[len(j) - 1] == '3':
             continue
         tr.append(i)
         
    print(tr[k-1])