from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())

q = deque()
visit = []
def bfs(cur):
    q.append((cur, 0))
    visit.append(cur)
    while q:
        num, cnt = q.popleft()
        if num == K or num * 2 == K:
            return cnt
        elif num - 1 == K or num + 1 == K:
            return cnt+1
        if 0 <= num * 2 <= 100000 and num * 2 not in visit:
            visit.append(num * 2)
            q.append((num * 2, cnt))
        if 0 <= num - 1 <= 100000 and num - 1 not in visit:
            visit.append(num - 1)
            q.append((num - 1, cnt + 1))
        if 0 <= num + 1 <= 100000 and num + 1 not in visit:
            visit.append(num + 1)
            q.append((num + 1, cnt + 1))


print(bfs(N))