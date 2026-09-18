import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = "YES"
    visited = set()
    visited.add(a[0])
    for j in range(1, n):
        if a[j] - 1 not in visited and a[j] + 1 not in visited:
            ans = "NO"
            break
        visited.add(a[j])
    print(ans)