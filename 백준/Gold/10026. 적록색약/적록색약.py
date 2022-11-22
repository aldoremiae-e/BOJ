from sys import stdin
from collections import deque

def bfs(sx, sy):
  global cnt, visited
  q = deque([])
  visited[sy][sx] = -1
  q.append((sx,sy))
  d = [(1,0), (0,1), (-1,0), (0,-1)]
  while q:
    cx, cy = q.popleft()
    for dx, dy in d:
      x, y = cx + dx, cy + dy
      if (0 <= x < N and 0 <= y < N) and arr[y][x] == arr[sy][sx] and visited[y][x] == 0:
        visited[y][x] = -1
        q.append((x, y))
  cnt += 1
        
N = int(stdin.readline())
arr = [list(stdin.readline().rstrip()) for _ in range(N)]
visited = [list(0 for _ in range(N)) for _ in range(N)]
# 영역 개수
cnt = 0
# 정상
for i in range(N):
  for j in range(N):
    if visited[j][i] == 0:
      bfs(i, j)
print(cnt, end=' ')

visited = [list(0 for _ in range(N)) for _ in range(N)]
cnt = 0
# 적록색약
for i in range(N):
  for j in range(N):
    if arr[j][i] == 'G':
      arr[j][i] = 'R'
for i in range(N):
  for j in range(N):
    if visited[j][i] == 0:
      bfs(i, j)
print(cnt)