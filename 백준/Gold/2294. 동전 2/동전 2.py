from sys import stdin
n, k = map(int, stdin.readline().split())
coins = set(int(stdin.readline()) for _ in range(n))
dp = [100001] * (k+1)
dp[0] = 1
'''
1 5 12
dp[0] = 1
dp[1] = dp[1-1] = 1
dp[2] = dp[1] + dp[2-1] = 2
dp[3] = dp[1] + dp[3-1] = 3
dp[4] = dp[1] + dp[4-1] = 4
dp[5] = dp[1] + dp[5-1] = 5 / dp[5-5] = 1 
dp[6] = 6 / dp[5] + dp[6-5] = 2
'''
for coin in coins:
    for i in range(coin, k+1):
        if i == coin:
            dp[i] = 1
        else:
            dp[i] = min(dp[i], dp[coin] + dp[i-coin])
if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])