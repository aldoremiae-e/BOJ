from collections import deque
from copy import deepcopy
from pprint import pprint
R, C, T = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기
aircond = []
for i in range(R):
    if maps[i][0] == -1:
        aircond.append(i)
        aircond.append(i+1)
        break

def diff(q):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visit = [[0] * C for _ in range(R)]
    visit[aircond[0]][0] = -1
    visit[aircond[1]][0] = -1
    while q:
        i, j = q.popleft()
        dcnt = 0
        for di, dj in d:
            ci, cj = i + di, j + dj
            if 0 <= ci < R and 0 <= cj < C and maps[ci][cj] != -1:
                visit[ci][cj] += (maps[i][j] // 5)
                dcnt += 1
        visit[i][j] += maps[i][j] - (maps[i][j] // 5) * dcnt

    return visit

def air():
    visit = [[0] * C for _ in range(R)]
    visit[aircond[0]][0] = -1
    visit[aircond[1]][0] = -1
    for i in range(R):
        for j in range(C):
            if (i == 0 or i in aircond or i == R-1) or (j == 0 or j == C-1):
                continue
            else:
                visit[i][j] = maps[i][j]
    ui, di = aircond[0], aircond[1]
    cnt = 0
    while cnt < 4:
        if cnt == 0:
            visit[ui][1] = 0
            # 오른쪽
            for j in range(2, C):
                visit[ui][j] = maps[ui][j-1]
        if cnt == 1:
            # 위로
            for i in range(ui - 1, -1, -1):
                visit[i][-1] = maps[i+1][-1]
        if cnt == 2:
            # 왼쪽
            for j in range(C-2, -1, -1):
                visit[0][j] = maps[0][j+1]
        if cnt == 3:
            # 아래로
            for i in range(1, ui):
                visit[i][0] = maps[i-1][0]
        cnt += 1
    while cnt > 0:
        if (cnt % 4) == 0:
            visit[di][1] = 0
            # 오른쪽
            for j in range(2, C):
                visit[di][j] = maps[di][j - 1]
        if cnt == 3:
            # 아래로
            for i in range(di + 1, R):
                visit[i][-1] = maps[i-1][-1]
        if cnt == 2:
            # 왼쪽
            for j in range(C - 2, -1, -1):
                visit[-1][j] = maps[-1][j + 1]
        if cnt == 1:
            # 위로
            for i in range(R - 2, di, -1):
                visit[i][0] = maps[i+1][0]
        cnt -= 1
    return visit
# T초 만큼 돌거다

for time in range(T):
    # 미세먼지 확산
    dust = deque()
    for i in range(R):
        for j in range(C):
            if maps[i][j] != 0 and maps[i][j] != -1:
                dust.append((i, j))
    maps = diff(dust)
    maps = air()
ans = 0
for i in range(R):
    for j in range(C):
        if maps[i][j] > 0:
            ans += maps[i][j]
print(ans)