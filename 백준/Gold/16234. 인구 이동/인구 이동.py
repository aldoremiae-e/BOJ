from collections import deque
from copy import deepcopy
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def bfs(si, sj):
    global day, flag, visit
    q = deque()
    q2 = deque()
    q.append((si, sj))
    q2.append((si, sj))
    visit[si][sj] = 1
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    people = A[si][sj]
    ground = 1
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ci, cj = i + di, j + dj
            if 0 <= ci < N and 0 <= cj < N and visit[ci][cj] == 0:
                if L <= abs(A[i][j] - A[ci][cj]) <= R:
                    flag = 1
                    ground += 1
                    people += A[ci][cj]
                    visit[ci][cj] = 1
                    q.append((ci, cj))
                    q2.append((ci, cj))
    next_pp = people // ground
    if len(q2) > 1: 
        while q2:
            i, j = q2.popleft()
            A[i][j] = next_pp

day = 0
flag = 1
while flag:
    visit = [[0] * N for _ in range(N)]
    flag = 0
    for x in range(N):
        for y in range(N):
            if visit[x][y] == 0:
                bfs(x, y)
    day += 1
print(day-1)