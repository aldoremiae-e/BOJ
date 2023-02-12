from sys import stdin

N = int(stdin.readline())
dairy = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
dp = [0] * (N+1) # 인덱스 N까지

for i in range(N):
    for j in range(i + dairy[i][0], N+1):
        dp[j] = max(dairy[i][1] + dp[i], dp[j])
print(dp[N])