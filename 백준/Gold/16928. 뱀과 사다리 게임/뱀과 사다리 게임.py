from collections import deque
N, M = map(int, input().split())
info = {}
for _ in range(N+M):
    a, b = map(int, input().split())
    info[a] = b
ans = int(1e9)
def bfs():
    global ans
    q = deque()
    q.append((0, 1))
    visit = [False] * 101
    visit[1] = True
    while q:
        cnt, cur = q.popleft()
        if cur == 100:
            ans = min(ans, cnt)
            continue
        if cur in info:
            cur = info[cur]
            visit[cur] = True
        for i in range(6, 0, -1):
            nxt = cur + i
            if nxt > 100:
                continue
            if visit[nxt]:
                continue
            visit[nxt] = True
            q.append((cnt+1, nxt))
bfs()
print(ans)