from pprint import pprint
from collections import deque
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    maps = [[['' for _ in range(C)] for _ in range(R)] for _ in range(L)]
    sl, sr, sc = 0, 0, 0
    i = 0
    while i < L:
        for j in range(R):
            lst = input()
            for k in range(C):
                maps[i][j][k] = lst[k]
                if lst[k] == 'S':
                    sl, sr, sc = i, j, k
        if input() == '':
            i += 1

    def dfs(sl, sr, sc):
        q = deque()
        q.append((sl, sr, sc))
        visit = [[[0 for _ in range(C)]for _ in range(R)]for _ in range(L)]
        visit[sl][sr][sc] = 1
        dirs = [(0, 0, 1), (0, 0, -1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]
        while q:
            cl, cr, cc = q.popleft()
            for dl, dr, dc in dirs:
                nl, nr, nc = dl + cl, dr + cr, dc + cc
                if not (0 <= nl < L and 0 <= nr < R and 0 <= nc < C):
                    continue
                if maps[nl][nr][nc] == 'E':
                    return visit[cl][cr][cc]
                if maps[nl][nr][nc] == '.' and visit[nl][nr][nc] == 0:
                    visit[nl][nr][nc] = visit[cl][cr][cc] + 1
                    q.append((nl, nr, nc))
        return 0

    ans = dfs(sl, sr, sc)
    if ans == 0:
        print('Trapped!')
    else:
        print(f'Escaped in {ans} minute(s).')