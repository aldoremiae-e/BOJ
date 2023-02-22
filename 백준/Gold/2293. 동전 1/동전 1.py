from sys import stdin
from itertools import combinations

N, K = map(int, stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(N)]

# dp : 합이 i원이 되는데 필요한 동전의 개수를 통해, dp[K]를 구하자
dp = [0] * (K+1)
dp[0] = 1 # 어떠한 동전도 사용하지 않고 만들 수 있는 경우의 수

for coin in coins:
    for i in range(coin, K+1):
        dp[i] = dp[i] + dp[i-coin]
print(dp[K])