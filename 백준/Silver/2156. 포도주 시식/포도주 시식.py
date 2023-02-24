from sys import stdin
N = int(stdin.readline())
V = [int(stdin.readline()) for _ in range(N)]
dp = [0] * (N+2)
dp[1] = V[0]
if N >= 2:
    dp[2] = V[0] + V[1]
    for i in range(3, N+1):
        # 12_, 1_3, _23
        dp[i] = max(dp[i-1], dp[i-2] + V[i-1], dp[i-3] + V[i-2] + V[i-1])
print(dp[N])