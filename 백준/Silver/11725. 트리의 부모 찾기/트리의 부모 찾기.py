from sys import stdin
from collections import deque
# 노드의 수 N 간선의 수 N-1
N = int(stdin.readline())
visit = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
q = deque()
ans = [0] * (N+1)
def bfs(v):
    q.append(v)
    visit[v] = 1
    while q:
        parent = q.popleft()
        for i in graph[parent]:
            if visit[i] == 0:
                ans[i] = parent
                visit[i] = 1
                q.append(i)
bfs(1)
for i in range(2, N+1):
    print(ans[i])