from sys import stdin
# N == 0 이라면 경우의 수는 0이다. 근데 1<=N<=30
N = int(stdin.readline())

dp = [0] * (N+1)
dp[0] = 0

if N >= 2:
    dp[2] = 3
for i in range(4, N+1, 2):
    dp[i] = dp[i-2] * 3 + 2 # 새로생기는애들 2개
    for j in range(4, i, 2):
        # i-4 i-6 ... i-(i-2)
        dp[i] += dp[i-j] * 2
print(dp[N])