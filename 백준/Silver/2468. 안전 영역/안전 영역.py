from sys import stdin
from copy import deepcopy
from collections import deque
from pprint import pprint

N = int(stdin.readline())
maps = [list(map(int, stdin.readline().split())) for _ in range(N)]

# 영역 채우기
def bfs(si, sj, H):
    global visit
    q = deque()
    visit[si][sj] = 1
    q.append((si, sj))
    while q:
        i, j = q.popleft()
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in d:
            ci, cj = i + di, j + dj
            if 0 <= ci < N and 0 <= cj < N and visit[ci][cj] == 0 and maps[ci][cj] >= H:
                visit[ci][cj] = 1
                q.append((ci, cj))

# 높이 최적화
minnum = 101
maxnum = 0
for i in range(N):
    for j in range(N):
        if minnum > maps[i][j]:
            minnum = maps[i][j]
        if maxnum < maps[i][j]:
            maxnum = maps[i][j]
            
ans = 0
for h in range(minnum, maxnum+1):
    # 영역 개수 cnt
    cnt = 0
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maps[i][j] >= h and visit[i][j] == 0:
                # 영역의 크기만큼 visit 채우기
                bfs(i, j, h)
                cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)