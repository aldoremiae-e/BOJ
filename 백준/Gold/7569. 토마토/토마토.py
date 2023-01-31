# https://www.acmicpc.net/problem/7569 토마토
from pprint import pprint
from sys import stdin
from collections import deque
M, N, H = map(int, stdin.readline().split())
box = []
for _ in range(H):
    box.append([list(map(int, stdin.readline().split()))for _ in range(N)])

q = deque()
visit = [[[0] * M for _ in range(N)] for _ in range(H)]

def bfs():
    global visit
    while q:
        h, n, m = q.popleft()
        d = [(1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (0, -1, 0)]
        for dh, dn,dm in d:
            ch, cn, cm = h + dh, n + dn, m + dm
            if (0 <= ch < H and 0 <= cn < N) and (0 <= cm < M and visit[ch][cn][cm] == 0):
                if box[ch][cn][cm] == 0:
                    visit[ch][cn][cm] = visit[h][n][m] + 1
                    q.append((ch, cn, cm))

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                q.append((h, n, m))
                visit[h][n][m] = 1
            elif box[h][n][m] == -1:
                visit[h][n][m] = -1
bfs()
ans = 0
for h in range(H):
    if ans == -1:
        break
    for n in range(N):
        if ans == -1:
            break
        for m in range(M):
            if visit[h][n][m] == 0:
                ans = -1
                break
            else:
                if visit[h][n][m] > ans:
                    ans = visit[h][n][m]
if ans == -1:
    print(ans)
else:
    print(ans - 1)