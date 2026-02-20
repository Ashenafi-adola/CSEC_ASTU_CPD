t = int(input())
main = []
for _ in range(t):
    n, k = map(int, input().split())
    probs = list(map(int, input().split()))
    probs.sort()
    rem = 0
    j = 0
    for i in range(n-1):
        if probs[i+1] - probs[i] <= k:
            j += 1
        else:
            j += 1
            if j > rem:
                rem = j 
            j = 0
    if rem > 0:
        main.append(n - rem) 
    else:
        main.append(0)
for i in main:
    print(i)