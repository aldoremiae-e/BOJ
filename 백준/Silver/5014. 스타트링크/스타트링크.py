from sys import stdin
from collections import deque

def bfs(f, s, e, u, d):
    q = deque()
    q.append((s, 0))
    visit[s] = 1
    flag = 0
    while q:
        c, cnt = q.popleft()
        uc = c + u
        dc = c - d
        if uc == e or dc == e:
            flag = 1
            return cnt+1
        if (1 <= uc <= f) and visit[uc] == 0:
            visit[uc] = 1
            q.append((uc, cnt+1))
        if (1 <= dc <= f) and visit[dc] == 0:
            visit[dc] = 1
            q.append((dc, cnt+1))
    if flag == 0:
        return 'use the stairs'


# 최대층, 현재위치, 목표층, 위, 아래
F, S, G, U, D = map(int, stdin.readline().split())
if S == G:
    print(0)
else:
    visit = [0] * (F+1)
    print(bfs(F, S, G, U, D))