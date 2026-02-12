n = int(input())
ns = list(map(int, input().split()))

se = 0
di = 0

it = 0
fn = len(ns)-1


for i in range(len(ns)):
    if i%2 == 0:
        if ns[it] > ns[fn]:
            se += ns[it]
            it += 1
        else:
            se += ns[fn]
            fn -= 1
    else:
        if ns[it] > ns[fn]:
            di += ns[it]
            it += 1
        else:
            di += ns[fn]
            fn -= 1

print(se, di)