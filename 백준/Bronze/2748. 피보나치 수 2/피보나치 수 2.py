from sys import stdin

N = int(stdin.readline())
dp = [0] * (N+1)
if N == 0:
    dp[0] = 0
if N >= 1:
    dp[0] = 0
    dp[1] = 1
if N > 1:
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[N])