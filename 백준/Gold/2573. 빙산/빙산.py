from collections import deque
# 시작점 찾기
def find_start(arr):
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] > 0:
                return i, j
    return -1, -1
# 빙산 녹
def melt(si, sj, maps):
    q = deque()
    q.append((si, sj))
    visit = [[False] * M for _ in range(N)]
    visit[si][sj] = True
    new_maps = [[0] * M for _ in range(N)]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        ci, cj = q.popleft()
        nh = maps[ci][cj]
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if maps[ni][nj] == 0:
                nh -= 1
            else:
                if visit[ni][nj]:
                    continue
                visit[ni][nj] = True
                q.append((ni, nj))
        if nh >= 0:
            new_maps[ci][cj] = nh
        else:
            new_maps[ci][cj] = 0
    return new_maps
def bfs(si, sj, cnt):
    global visit2
    if cnt > 1:
        return True
    q = deque()
    q.append((si, sj))
    visit2[si][sj] = cnt
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if visit2[ni][nj] > 0:
                continue
            if maps[ni][nj] == 0:
                continue
            visit2[ni][nj] = cnt
            q.append((ni, nj))
    return False

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
year = 1
while True:
    mi, mj = find_start(maps)
    if mi == -1 and mj == -1:
        print(0)
        break
    # 녹이자
    maps = melt(mi, mj, maps)
    # 세자
    visit2 = [[0] * M for _ in range(N)]
    cnt = 1
    flag = False
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if maps[i][j] == 0:
                continue
            if visit2[i][j] > 0:
                continue
            flag = bfs(i, j, cnt)
            if not flag:
                cnt += 1
            else:
                break
        if flag:
            break
    if flag:
        print(year)
        break
    else:
        year += 1