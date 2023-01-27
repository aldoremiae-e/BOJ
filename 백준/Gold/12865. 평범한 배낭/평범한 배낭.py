from sys import stdin
N, K = map(int, stdin.readline().split())
lst = []
for i in range(N):
    W, V = map(int, stdin.readline().split())
    lst.append((W, V))
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = lst[i-1][0]
        v = lst[i-1][1]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
print(dp[N][K])