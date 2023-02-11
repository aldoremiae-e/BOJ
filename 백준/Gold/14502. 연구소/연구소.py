from sys import stdin
from copy import deepcopy
from collections import deque

N, M = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(N)]

# 바이러스 퍼트리고 안전영역 세기
def bfs():
    visit = deepcopy(maps)
    q = deque()
    # q에 바이러스 위치 넣기
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                q.append((i, j))
    # 바이러스 퍼트리기
    while q:
        i, j = q.popleft()
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in d:
            ci, cj = i + di, j + dj
            if 0 <= ci < N and 0 <= cj < M and maps[ci][cj] == 0 and visit[ci][cj] == 0:
                visit[ci][cj] = 2
                q.append((ci, cj))
    # 안전영역 세기
    ret = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                ret += 1
    return ret

# 벽을 세우기
def wall(cnt):
    global ans
    if cnt == 3:
        # 벽 3개면 바이러스 퍼트리고 안전영역 세기
        res = bfs()
        if ans < res:
            ans = res
        return
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                # 백트래킹으로 벽세우기
                maps[i][j] = 1
                wall(cnt + 1)
                maps[i][j] = 0

ans = 0
wall(0)
print(ans)