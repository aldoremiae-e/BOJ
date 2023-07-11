# dfs로 풀어보자
import sys
sys.setrecursionlimit(10**4)
def dfs(si, sj):
    global visit
    visit[si][sj] = 1
    dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for di, dj in dirs:
        ni, nj = si + di, sj + dj
        if not (0 <= ni < h and 0 <= nj < w):
            continue
        if maps[ni][nj] == 1 and visit[ni][nj] == 0:
            dfs(ni, nj)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    visit = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visit[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)