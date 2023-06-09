from collections import deque
ans = 0
def bfs(si, sj):
    global ans
    q = deque()
    q.append((si, sj))
    visit = [[False] * M for _ in range(N)]
    visit[si][sj] = True
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        i, j = q.popleft()
        for di, dj in dir:
            ci, cj = di + i, dj + j
            if 0 <= ci < N and 0 <= cj < M and visit[ci][cj] == False:
                if maps[ci][cj] == 'X':
                    continue
                elif maps[ci][cj] == 'O':
                    visit[ci][cj] = True
                    q.append((ci, cj))
                elif maps[ci][cj] == 'P':
                    visit[ci][cj] = True
                    q.append((ci, cj))
                    ans += 1

N, M = map(int, input().split())
maps = [[''] * M for _ in range(N)]
si, sj = 0, 0
for i in range(N):
    s = input()
    for j in range(M):
        maps[i][j] = s[j]
        if maps[i][j] == 'I':
            si, sj = i, j
bfs(si, sj)
if ans == 0:
    print('TT')
else:
    print(ans)