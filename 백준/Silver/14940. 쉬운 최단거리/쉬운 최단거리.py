from collections import deque
def bfs(si, sj):
    global visit
    q = deque()
    q.append((si, sj))
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ci, cj = di + i, dj + j
            if 0 <= ci < N and 0 <= cj < M and (ci, cj) != (si, sj):
                if input_maps[ci][cj] == 1 and visit[ci][cj] == 0:
                    visit[ci][cj] = visit[i][j] + 1
                    q.append((ci, cj))
N, M = map(int, input().split())
input_maps = [] * N
si, sj = 0, 0
for i in range(N):
    input_maps.append(list(map(int, input().split())))
    for j in range(M):
        if input_maps[i][j] == 2:
            si, sj = i , j
visit = [[0] * M for _ in range(N)]
bfs(si, sj)
for i in range(N):
    for j in range(M):
        if input_maps[i][j] == 1 and visit[i][j] == 0:
            print(-1, end=' ')
        else:
            print(visit[i][j], end= ' ')
    print()