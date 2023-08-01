N, M = map(int, input().split())
maps = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
for i in range(1, N+1):
    for j in range(1, M+1):
        maps[i][j] = max(maps[i-1][j], maps[i][j-1]) + maps[i][j]
print(maps[N][M])