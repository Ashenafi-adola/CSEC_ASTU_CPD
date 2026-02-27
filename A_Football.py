from collections import Counter
n = int(input())
des = []
for i in range(n):
    des.append(input())
counts = Counter(des)
print(counts.most_common(1)[0][0])