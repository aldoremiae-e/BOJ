from sys import stdin
from collections import deque
def bfs(si, sj):
    maps[si][sj] = 1
    q = deque()
    q. append((si, sj))
    d = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ci, cj = i + di, j + dj
            if 0 <= ci < N and 0 <= cj < N and maps[ci][cj] == 0:
                if ci == i2 and cj == j2:
                    return maps[i][j]
                else:
                    maps[ci][cj] = maps[i][j] + 1
                    q.append((ci, cj))
    return 0

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    maps = [[0] * N for _ in range(N)]
    i1, j1 = map(int,stdin.readline().split())
    i2, j2 = map(int,stdin.readline().split())

    ans = bfs(i1, j1)
    print(ans)