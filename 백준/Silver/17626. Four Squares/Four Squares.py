from sys import stdin
from math import sqrt
N = int(stdin.readline())

dp = [0] * 50001
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 3
sqrt_nums = [1]
for i in range(4, N+1):
    if sqrt(i) == int(sqrt(i)):
        dp[i] = 1
        sqrt_nums.append(i)
    else:
        dp[i] = dp[sqrt_nums[-1]] + dp[i - sqrt_nums[-1]]
        for n in range(len(sqrt_nums)-2, 0, -1):
            if dp[i] > dp[sqrt_nums[n]] + dp[i-sqrt_nums[n]]:
                dp[i] = dp[sqrt_nums[n]] + dp[i-sqrt_nums[n]]
print(dp[N])