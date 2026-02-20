n = int(input())
con = 0
for i in range(n):
    car = input()
    if car =='++x'.upper() or car =="x++".upper():
        con+=1
    else:
        con-=1
print(con)
