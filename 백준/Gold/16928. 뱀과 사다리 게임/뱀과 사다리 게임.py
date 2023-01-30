from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
mymap = [0] * 101
for _ in range(N):
    a, b = map(int, stdin.readline().split())
    mymap[a] = b
for _ in range(M):
    c, d = map(int, stdin.readline().split())
    mymap[c] = d

#print(ladder, snake)

q = deque()
visit = [0] * 101
visit[0] = 1
def bfs(start):
    visit[start] = 1
    q.append(start)
    while q:
        # 현재 위치
        cur = q.popleft()
        # 만약 현재위치에 사다리가 있다면
        for i in range(1, 7):
            if visit[cur + i] == 0:
                if mymap[cur + i] != 0 and visit[mymap[cur + i]] == 0:
                    visit[cur + i] = visit[cur] + 1
                    visit[mymap[cur + i]] = visit[cur] + 1
                    q.append(mymap[cur + i])
                elif mymap[cur + i] == 0:
                    visit[cur + i] = visit[cur] + 1
                    q.append(cur + i)
            if cur + i == 100:
                return visit[100] - 1
print(bfs(1))