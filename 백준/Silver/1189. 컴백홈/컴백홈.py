R, C, K = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(R)]
visit = [[0] * C for _ in range(R)]
ans = 0
dirs = [(0, 1), (1, 0), (0 , -1), (-1, 0)]
def bt(i, j):
    global ans, visit
    if i == 0 and j == C-1:
        if visit[i][j] == K:
            ans += 1
            return
    for di, dj in dirs:
        ni, nj = di + i, dj + j
        if not (0 <= ni < R and 0 <= nj < C):
            continue
        if visit[ni][nj] != 0 or board[ni][nj] == 'T':
            continue
        visit[ni][nj] = visit[i][j] + 1
        bt(ni, nj)
        visit[ni][nj] = 0

visit[R-1][0] = 1
bt(R-1, 0)
print(ans)