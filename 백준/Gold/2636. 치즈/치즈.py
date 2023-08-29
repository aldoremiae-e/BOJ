from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    global ans, time
    q = deque()
    q.append((0, 0))
    visit = [[0] * M for _ in range(N)]
    visit[0][0] = 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    chz = deque()
    while q:
        i, j = q.popleft()
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if visit[ni][nj] == 1:
                continue
            if maps[ni][nj] == 0:
                visit[ni][nj] = 1
                q.append((ni, nj))
            else:
                visit[ni][nj] = 1
                maps[ni][nj] = 0
                chz.append((ni, nj))
        if not q:
            if len(chz) > 0:
                ans = len(chz)
                time += 1
                q = chz
                chz = deque()
            else:
                return
time = 0
ans = 0
bfs()
print(time)
print(ans)