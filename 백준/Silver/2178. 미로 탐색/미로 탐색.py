from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
miro = [list(map(int, stdin.readline().strip())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
ans = 10000
q = deque()
def bfs(i, j):
    global cnt, ans
    q.append((i, j, 1))
    while q:
        si, sj, cnt = q.popleft()
        visit[si][sj] = 1

        if si == N-1 and sj == M-1:
            if cnt < ans:
                ans = cnt
            return
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for di, dj in d:
            ci = di + si
            cj = dj + sj
            if (0 <= ci < N and 0 <= cj < M) and miro[ci][cj] == 1 and visit[ci][cj] == 0:
                visit[ci][cj] = 1
                q.append((ci, cj, cnt+1))

bfs(0, 0)
print(ans)