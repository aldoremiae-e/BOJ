# https://www.acmicpc.net/problem/2193 이친수 dp
from sys import stdin
N = int(stdin.readline())
dp = [0] * (N+1)
if N == 1:
    dp[0] = 0
    dp[1] = 1
if N == 2:
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
if N >= 3:
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[N])