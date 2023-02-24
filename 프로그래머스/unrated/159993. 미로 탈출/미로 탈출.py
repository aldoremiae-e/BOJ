from collections import deque
def bfs(si, sj, flag, N, M, mymaps):
    visit = [[0] * M for _ in range(N)]
    q = deque()
    q.append((si, sj))
    if flag == 0:
        visit[si][sj] = 1
    else:
        visit[si][sj] = flag
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        i, j = q.popleft()
        for di, dj in d:
            ci, cj = i + di, j + dj
            if 0 <= ci < N and 0 <= cj < M and visit[ci][cj] == 0 and mymaps[ci][cj] != 'X':
                if mymaps[ci][cj] == 'L' and flag == 0:
                    return visit[i][j]
                elif mymaps[ci][cj] == 'E' and flag > 0:
                    return visit[i][j] + 1
                else:
                    visit[ci][cj] = visit[i][j] + 1
                    q.append((ci,cj))
    return -1
def solution(maps):
    N = len(maps)
    M = len(maps[0])
    mymaps = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            mymaps[i][j] = maps[i][j]
            if maps[i][j] == 'S':
                SI, SJ = i, j
            elif maps[i][j] == 'L':
                LI, LJ = i, j
            elif maps[i][j] == 'E':
                EI, EJ = i , j
    cnt = bfs(SI, SJ, 0, N, M, mymaps)
    if cnt == -1:
        return cnt
    else:
        answer = bfs(LI, LJ, cnt, N, M, mymaps)
        return answer