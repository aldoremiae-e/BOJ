import sys
from collections import deque
N, M, V = map(int,sys.stdin.readline().split())
lst = list([0 for _ in range(N)] for _ in range(N))
for _ in range(M):
    y, x = map(int,sys.stdin.readline().split())
    lst[y-1][x-1] = 1
    lst[x-1][y-1] = 1

#dfs
visit = [0 for _ in range(N)]
def dfs(cur):
    print(cur+1, end=' ')
    visit[cur] = -1
    for i in range(N):
        if lst[cur][i] == 1 and visit[i] == 0:
            dfs(i)
#bfs
visited = [0 for _ in range(N)]
q = deque([])
def bfs(start):
    q.append(start)
    visited[start] = -1
    while q:
        cur = q.popleft()
        print(cur+1, end=' ')
        for i in range(N):
            if lst[cur][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = -1


dfs(V-1)
print('')
bfs(V-1)