from collections import deque

def bfs(i, j, N, M, maps):
    visit = [[0] * M for _ in range(N)]
    q = deque()
    q.append((i, j))
    visit[i][j] = 1
    while q:
        si, sj = q.popleft()
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in d:
            ci, cj = si + di, sj + dj
            if 0 <= ci < N and 0 <= cj < M and maps[ci][cj] == 1 and visit[ci][cj] == 0:
                visit[ci][cj] = visit[si][sj] + 1
                q.append((ci, cj))
    if visit[N-1][M-1] == 0:
        return -1
    else:
        return visit[N-1][M-1]
                
def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = bfs(0, 0, n, m, maps)
    return answer