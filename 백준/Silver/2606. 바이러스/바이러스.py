from sys import stdin
from collections import deque
n = int(stdin.readline())
link = int(stdin.readline())
visited = [0] * (n+1)
arr = [list(0 for _ in range(n+1)) for _ in range(n+1)]

def dfs(cur):
    visited[cur] = 1
    for i in range(n+1):
        if arr[cur][i] == 1 and visited[i] == 0:
            dfs(i)

for i in range(link):
    x, y = map(int, stdin.readline().split())
    arr[x][y] = 1
    arr[y][x] = 1

dfs(1)
cnt = 0
for i in visited:
    if i == 1:
        cnt += 1
print(cnt-1)