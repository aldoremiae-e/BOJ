from sys import stdin

T = int(stdin.readline())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for tc in range(T):
    n = int(stdin.readline())
    print(dp[n])
