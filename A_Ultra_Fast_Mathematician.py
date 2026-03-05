n = list(input())
s = list(input())
pr = ''
for i, j in zip(n,s):
    if (i == '1' and j == '0') or (i == '0' and j == '1'):
        pr += '1'
    else:
        pr += '0'
print(pr)