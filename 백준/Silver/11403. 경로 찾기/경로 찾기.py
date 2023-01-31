from sys import stdin
from collections import deque
N = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(N)]

check = []
q = deque()
def bfs(i):
    global check
    if i == N:
        return check
    q.append(i)
    visit = [0] * N
    while q:
        ci = q.popleft()
        for cj in range(N):
            if graph[ci][cj] == 1 and visit[cj] == 0:
                visit[cj] = 1
                q.append(cj)
    check.append(visit)
    bfs(i+1)

bfs(0)
for i in range(N):
    print(*check[i])