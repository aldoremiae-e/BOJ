from sys import stdin
from collections import deque
def bfs(a, b):
    q = deque()
    q.append((a, ''))
    visit[a] = 1
    while q:
        c, ans = q.popleft()
        d = c * 2 if (c * 2) <= 9999 else (c * 2) % 10000
        s = c - 1 if c != 0 else 9999

        d1 = c // 1000 # 1
        d2 = (c % 1000) // 100 # 234 // 100 = 2
        d3 = ((c % 1000) % 100) // 10 # 234 % 100 = 34 // 10 = 3
        d4 = ((c % 1000) % 100) % 10 # 234 % 100 =34 % 10 = 4
        l = d2 * 1000 + d3 * 100 + d4 * 10 + d1
        r = d4 * 1000 + d1 * 100 + d2 * 10 + d3
        if b == d:
            return ans + 'D'
        elif b == s:
            return ans + 'S'
        elif b == l:
            return ans + 'L'
        elif b == r:
            return ans + 'R'

        if visit[d] == 0:
            visit[d] = 1
            q.append((d, ans + 'D'))
        if visit[s] == 0:
            visit[s] = 1
            q.append((s, ans + 'S'))
        if visit[l] == 0:
            visit[l] = 1
            q.append((l, ans + 'L'))
        if visit[r] == 0:
            visit[r] = 1
            q.append((r, ans + 'R'))

T = int(stdin.readline())
for _ in range(T):
    A, B = map(int, stdin.readline().split())
    visit = [0] * 10001
    print(bfs(A, B))
