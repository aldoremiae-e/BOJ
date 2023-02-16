from sys import stdin
from collections import deque
from copy import deepcopy
N, M = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(N)]

# 1을 찾아서
# 위아래오왼 중 0인게 2개 이상이면, 사라짐. =
def bfs(i, j):
    global maps
    que = deque()
    que.append((i, j))
    cheese_q = deque() # 공기와 2번이상 접촉한 치즈
    visit = [[0] * M for _ in range(N)] # 공기접촉
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while que:
        i, j = que.popleft()
        for di, dj in d:
            ci, cj = di + i, dj + j
            if 0 <= ci < N and 0 <= cj < M:
                if (maps[ci][cj] == 0 and visit[ci][cj] == 0) or maps[ci][cj] == 1:
                    # 공기이고, 방문처리가 안된 공간
                    visit[ci][cj] += 1
                    if maps[ci][cj] == 0:
                        que.append((ci, cj))
                    if maps[ci][cj] == 1:
                        if visit[ci][cj] >= 2 and (ci, cj) not in cheese_q:
                            cheese_q.append((ci, cj))
    return cheese_q

time = 0
while 1:
    ch_q = bfs(0, 0)

    if ch_q:
        for i, j in ch_q:
            maps[i][j] = 0
        time += 1
    else:
        print(time)
        break