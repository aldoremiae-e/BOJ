from sys import stdin
from collections import deque
from copy import deepcopy
N, M, K = map(int, stdin.readline().split())
maps = [[0] * M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            maps[i][j] = -1

def bfs(si, sj):
    global visit
    q = deque()
    q.append((si, sj))
    visit[si][sj] = 1
    count = 1
    while q:
        i, j = q.popleft()
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in d:
            ci, cj = i + di, j + dj
            if 0 <= ci < N and 0 <= cj < M and visit[ci][cj] == 0 and maps[ci][cj] == 0:
                visit[ci][cj] = 1
                count += 1
                q.append((ci, cj))
    return count
visit = deepcopy(maps)
cnt = 0
lst = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0 and visit[i][j] == 0:
            lst.append(bfs(i, j))
            cnt += 1
print(cnt)
lst = sorted(lst)
print(*lst)