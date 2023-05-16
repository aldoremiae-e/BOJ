import sys
sys.setrecursionlimit(10 ** 9)
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(i, j):
    global cnt
    if i == (N-1) and j == (M-1):
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 0

    for di, dj in d:
        ci, cj = i + di, j + dj
        if (0 <= ci < N and 0 <= cj < M) and maps[ci][cj] < maps[i][j]:
            dp[i][j] += dfs(ci, cj)
    return dp[i][j]
cnt = 0
dp = [[-1] * M for _ in range(N)]
print(dfs(0, 0))