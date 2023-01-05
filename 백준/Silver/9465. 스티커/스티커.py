from sys import stdin
T = int(stdin.readline())

for tc in range(T):
    N = int(stdin.readline())
    sticker = list(list(map(int, stdin.readline().split())) for _ in range(2))
    # 상하좌우 안됨
    dp = [[0] * N for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] if dp[0][j-1] > dp[1][j-1] + sticker[0][j] else dp[1][j-1] + sticker[0][j]
        dp[1][j] = dp[1][j-1] if dp[1][j-1] > dp[0][j-1] + sticker[1][j] else dp[0][j-1] + sticker[1][j]
    if dp[0][N-1] > dp[1][N-1]:
        print(dp[0][N-1])
    else:
        print(dp[1][N-1])
