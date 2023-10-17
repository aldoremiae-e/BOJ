from collections import deque
from math import floor
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def bfs(board, L, R):
    visit = [[False] * N for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                continue
            visit[i][j] = True
            q = deque()
            q.append((i, j))
            q2 = [(i, j)]
            total = board[i][j]
            while q:
                ci, cj = q.popleft()
                for di, dj in dirs:
                    ni, nj = di + ci, dj + cj
                    if not (0 <= ni < N and 0 <= nj < N):
                        continue
                    if visit[ni][nj]:
                        continue
                    diff = abs(board[ci][cj] - board[ni][nj])
                    if L <= diff <= R:
                        flag = True
                        q.append((ni, nj))
                        q2.append((ni, nj))
                        visit[ni][nj] = True
                        total += board[ni][nj]
            val = total // len(q2)
            for x, y in q2:
                board[x][y] = val
    return flag

while True:
    if bfs(board, L, R):
        ans += 1
    else:
        print(ans)
        break