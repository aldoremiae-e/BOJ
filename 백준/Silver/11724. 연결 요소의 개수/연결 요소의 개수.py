from sys import stdin

N, M = map(int, stdin.readline().split())
arr = [list(0 for _ in range(N)) for _ in range(N)]
cnt = 0
def dfs(cur):
    global cnt
    visited[cur] = 1
    for i in range(N):
        if arr[cur][i] == 1 and visited[i] == 0:
            dfs(i)

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    arr[u-1][v-1] = 1
    arr[v-1][u-1] = 1
s = set()
for i in range(N):
    visited = [0] * N
    dfs(i)
    s.add(tuple(visited))
print(len(s))