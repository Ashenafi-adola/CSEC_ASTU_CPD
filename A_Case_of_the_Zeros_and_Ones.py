n = int(input())
s = input()
m = min(s.count('0'), s.count('1'))
print(len(s) - 2*m)