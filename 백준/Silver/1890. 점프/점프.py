from sys import stdin

N = int(stdin.readline())
maps = [list(map(int, stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        if dp[i][j] == 0:
            continue
        if 0 <= i + maps[i][j] < N:
            dp[i+maps[i][j]][j] += dp[i][j]
        if 0 <= j + maps[i][j] < N:
            dp[i][j+maps[i][j]] += dp[i][j]
print(dp[-1][-1])