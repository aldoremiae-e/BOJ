from sys import stdin
from collections import deque

def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = 1
  while q:
    n = q.popleft()
    if n == K:
      return visited[n] - 1
    else:
      if n-1 >= 0:
        if visited[n-1] == 0 :
          q.append(n-1)
          visited[n-1] = visited[n] + 1
      if n+1 <= 100000:
        if visited[n+1] == 0:
          q.append(n+1) 
          visited[n+1] = visited[n] + 1
      if 2*n <= 100000:
        if visited[2*n] == 0:
          q.append(2*n)
          visited[2*n] = visited[n] + 1
      
N, K = map(int, stdin.readline().split())
visited = [0] * 100001

print(bfs(N))
