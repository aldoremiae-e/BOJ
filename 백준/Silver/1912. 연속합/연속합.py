from sys import stdin
N = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))

dp = [0] * (N+1)
# dp[0]은 취급되면안됨
dp[0] = -1001
for i in range(1, N+1):
    dp[i] = max(dp[i-1] + lst[i-1], lst[i-1])
print(max(dp))
