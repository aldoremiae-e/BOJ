from collections import deque
N, M = map(int, input().split())
maps = [[0] * M for _ in range(N)]
si, sj = 0, 0
fire_q = deque()
for i in range(N):
    s = input()
    for j in range(M):
        if s[j] == '#':
            maps[i][j] = 1
        elif s[j] == 'J':
            si, sj = i, j
            maps[i][j] = 2
        elif s[j] == 'F':
            maps[i][j] = 3
            fire_q.append((i, j, 1))

def fires(q):
    visit = [[int(1e9)] * M for _ in range(N)]
    if not q:
        return visit
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        ci, cj, ct = q.popleft()
        visit[ci][cj] = ct
        for di, dj in dirs:
            ni, nj = di + ci, dj + cj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if maps[ni][nj] == 1 or visit[ni][nj] != int(1e9):
                continue
            visit[ni][nj] = ct + 1
            q.append((ni, nj, ct+1))
    return visit

fire_maps = fires(fire_q)

def jhs(si, sj):
    q = deque()
    q.append((si, sj))
    visit = [[0] * M for _ in range(N)]
    visit[si][sj] = 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = di + ci, dj + cj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if maps[ni][nj] == 3:
                continue
            if maps[ni][nj] == 1 or visit[ni][nj] > 0:
                continue
            if fire_maps[ni][nj] <= visit[ci][cj]+1:
                continue
            visit[ni][nj] = visit[ci][cj] + 1
            q.append((ni, nj))
    return visit

jh_maps = jhs(si, sj)
min_time = int(1e9)
for i in range(N):
    if jh_maps[i][0] > 0:
        min_time = min(min_time, jh_maps[i][0])
    if jh_maps[i][M-1] > 0:
        min_time = min(min_time, jh_maps[i][M-1])
    if i == 0 or i == N-1:
        for j in range(1, M-1):
            if jh_maps[i][j] > 0:
                min_time = min(min_time, jh_maps[i][j])

if min_time == int(1e9):
    print('IMPOSSIBLE')
else:
    print(min_time)