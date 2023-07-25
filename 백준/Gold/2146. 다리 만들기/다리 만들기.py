from collections import deque
from pprint import pprint
def count_island(cnt, si, sj):
    global islands, bride_start
    q = deque()
    q.append((si, sj))
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    islands[si][sj] = cnt
    while q:
        ci, cj = q.popleft()
        flag = False
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if maps[ni][nj] == 1 and islands[ni][nj] == 0:
                q.append((ni, nj))
                islands[ni][nj] = cnt
            if maps[ni][nj] == 0:
                flag = True
        if flag:
            bride_start.append((ci, cj))


N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
islands = [[0] * N for _ in range(N)]
bride_start = deque()
cnt = 1
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and islands[i][j] == 0:
            count_island(cnt, i, j)
            cnt += 1
def bfs(si, sj):
    global dis
    visit = {}
    q = deque()
    q.append((si, sj))
    visit[(si, sj)] = 1
    cur_i = islands[si][sj]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        ci, cj = q.popleft()
        if visit[(ci, cj)] - 1 > dis:
            continue
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            if islands[ni][nj] != 0 and islands[ni][nj] != cur_i:
                dis = min(dis, visit[(ci, cj)] - 1)
                return
            if islands[ni][nj] == 0 and (ni, nj) not in visit:
                visit[(ni, nj)] = visit[(ci, cj)] + 1
                q.append((ni, nj))

# 다리놓기
dis = 201
for i, j in bride_start:
    bfs(i, j)
print(dis)