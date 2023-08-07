from collections import deque
N = int(input())
M = int(input())
maps = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

q = deque()
visit = [0] * (N+1)
visit[1] = 1
cnt = 0
for bro in maps[1]:
    if visit[bro] == 0:
        cnt += 1
        q.append(bro)
        visit[bro] = 1
while q:
    me = q.popleft()
    for bro in maps[me]:
        if visit[bro] == 0:
            cnt += 1
            visit[bro] = 1
print(cnt)