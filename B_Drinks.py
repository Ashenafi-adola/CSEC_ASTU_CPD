n = int(input())
js = list(map(int, input().split()))
tot = n*100
su = sum(js)
pr = "%.12f" %((su/tot)*100)
print(pr)