t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    ns = [0] + list(map(int, input().split()))
    rs = 2 * (x - ns[len(ns)-1])
    ma = ns[1] - ns[0]
    for i in range(1, len(ns)):
        if ns[i] - ns[i-1] > ma:
            ma = ns[i] - ns[i-1]
    print(max(ma, rs))