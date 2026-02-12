s = input()
t = input()

mv = 0
for i in range(len(t)):
    if t[i] == s[mv]:
        mv += 1

print(mv+1)