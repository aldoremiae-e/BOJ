# 벽을 세우고
# 바이러스 퍼트리고
# 0의 개수 세자

from sys import stdin
from collections import deque
from copy import deepcopy

N, M = map(int, stdin.readline().split())
maps = [list(map(int, stdin.readline().split())) for _ in range(N)]
# 0 빈칸 1 벽 2 바이러스

def wall(n):
    global ans
    if n == 3:
        vmaps = virus()
        cnt = 0
        for i in range(N):
            for j in range(M):
                if vmaps[i][j] == 0:
                    cnt += 1
        if ans < cnt:
            ans = cnt
        return
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                wall(n+1)
                maps[i][j] = 0

def virus():
    #q = deepcopy(vq)
    # 바이러스 위치 확인 => 어차피 deepcopy 할거면 그냥 안에서 돌려버리면?
    q = deque()
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 2:
                q.append((i, j))
    visit = deepcopy(maps) # 벽을 세운 맵을 카피해야함
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ci, cj = i + di, j + dj
            if 0 <= ci < N and 0 <= cj < M and visit[ci][cj] == 0:
                visit[ci][cj] = 2
                q.append((ci, cj))
    return visit


# 0의 개수 셀거임
ans = 0
wall(0)
print(ans)