from sys import stdin

N = int(stdin.readline())
dp1 = [0] * (N+3)
dp2 = [0] * (N+3)
dp = [0] * (N+3)
dp1[2] = 3
dp2[2] = 2
dp[1] = 3
dp[2] = 7
for i in range(3, N+1):
    dp[i] = (dp1[i-1] * 3 + dp2[i-1] * 4) % 9901
    dp1[i] = (dp1[i-1] + dp2[i-1] * 2) % 9901
    dp2[i] = (dp1[i-1] + dp2[i-1]) % 9901
print(dp[N])