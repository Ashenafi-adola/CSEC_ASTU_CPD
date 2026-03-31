
n = 10
boxes = list(map(int,"86 89 89 86 86 89 86 86 89 89".split()))
boxes.sort()
print(boxes)
pr = 1
for i in range(n-1):
    if boxes[i] == boxes[i+1]:
        pr += 1
print(pr)