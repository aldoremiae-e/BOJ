from collections import deque
def bfs(si, sj):
    global visit
    q = deque()
    ij_set = set()
    q.append((si, sj))
    visit[si][sj] = 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        ci, cj = q.popleft()
        ij_set.add((ci, cj))
        for di, dj in dirs:
            ni, nj = di + ci, dj + cj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if visit[ni][nj] == 1 or maps[ni][nj] == 0:
                continue
            visit[ni][nj] = 1
            q.append((ni, nj))
    return len(ij_set)
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]
cnt, area = 0, 0
for i in range(N):
    for j in range(M):
        if visit[i][j] == 0 and maps[i][j] == 1:
            area = max(area, bfs(i, j))
            cnt += 1
print(cnt)
print(area)