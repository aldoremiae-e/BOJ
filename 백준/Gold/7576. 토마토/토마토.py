'''
옆에 두면 익는다 최소일수  => bfs
'''
from sys import stdin
from collections import deque

q = deque()
def bfs():
  global q
  while q:
    ci, cj = q.popleft()
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for di, dj in d:
      i, j = ci + di, cj + dj
      if (0 <= i < N and 0 <= j < M) and tomatos[j][i] != 1 and visited[j][i] == 0:
        if tomatos[j][i] == -1:
          continue
        else:
          visited[j][i] = visited[cj][ci] + 1
          q.append((i, j))

  
N, M = map(int, stdin.readline().split())
tomatos = [list(map(int, stdin.readline().split())) for _ in range(M)]
visited = [list(0 for _ in range(N))for _ in range(M)]
tomato = deque()

#print(tomatos, visited)
for j in range(M):
  for i in range(N):
    if tomatos[j][i] == 1:
      visited[j][i] = 1
      q.append((i, j))
  
bfs()
cnt = 0
for i in visited:
  for j in i:
    if j > cnt:
      cnt = j-1
  
flag = 0
for j in range(M):
  if flag == 1:
    print(-1)
    break
  for i in range(N):
    if tomatos[j][i] == 0 and visited[j][i] == 0:
      flag = 1
      break
if flag == 0:
  print(cnt)