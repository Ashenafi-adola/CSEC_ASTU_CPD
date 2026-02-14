st = input()
caps = "QWERTYUIOPLKJHGFDSAZXCVBNM"
smls = "qwertyuioplkjhgfdsazxcvbnm"
c = 0
s = 0
for i in st:
    if i in caps:
        c += 1
    elif i in smls:
        s += 1
if c <= s:
    print(st.lower())
else:
    print(st.upper())
