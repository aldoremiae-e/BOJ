from sys import stdin

N, M = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
dp = [0] * (N+1)
for i in range(N):
    dp[i+1] = nums[i] + dp[i]

for _ in range(M):
    i, j = map(int, stdin.readline().split())
    print(dp[j] - dp[i-1])