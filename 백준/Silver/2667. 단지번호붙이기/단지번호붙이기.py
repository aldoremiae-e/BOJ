from sys import stdin
from collections import deque
N = int(stdin.readline())
my_map = [list(map(int, stdin.readline().strip())) for _ in range(N)]
visit = [[0] * N for _ in range(N)]
q = deque()
block = []
def bfs(si, sj):
    global block
    visit[si][sj] = 1
    q.append((si, sj))
    cnt = 1
    while q:
        ci, cj = q.popleft()
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for di, dj in d:
            ni, nj = di + ci, dj + cj
            if (0 <= ni < N and 0 <= nj < N) and (my_map[ni][nj] == 1 and visit[ni][nj] == 0):
                q.append((ni, nj))
                cnt += 1
                visit[ni][nj] = 1
    block.append(cnt)
    return cnt
danji = 0
for i in range(N):
    for j in range(N):
        if my_map[i][j] == 1 and visit[i][j] == 0:
            bfs(i, j)
            danji += 1
block = sorted(block)
print(danji)
for b in block:
    print(b)