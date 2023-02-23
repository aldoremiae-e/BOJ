from sys import stdin

N = int(stdin.readline())
dp = [0] * (N+2)
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N] * 4 + dp[N-1] * 2)