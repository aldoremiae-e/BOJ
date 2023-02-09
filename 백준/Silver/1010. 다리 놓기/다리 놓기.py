from sys import stdin
T = int(stdin.readline())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    ans = 1
    for i in range(N):
        ans *= M
        M -= 1
    for j in range(1, N+1):
        ans //= j
    print(ans)