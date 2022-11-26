from sys import stdin

N = int(stdin.readline())
dp = [0] * (N+3)
dp[1], dp[2], dp[3] = 1, 2, 3
for i in range(4, N+2):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N] % 10007)