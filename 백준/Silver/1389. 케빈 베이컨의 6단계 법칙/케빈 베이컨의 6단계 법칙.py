import sys
from collections import deque
# 유저 친구관계
lst = deque([])
N, M = map(int, sys.stdin.readline().split())
for _ in range(M):
    lst.append(list(map(int, sys.stdin.readline().split())))

arr = list([0 for _ in range(int(N))] for _ in range(int(N)))
for i in range(M):
    a = lst[i][0] - 1
    b = lst[i][1] - 1
    if arr[a][b] == 0 and arr[b][a] == 0:
        arr[a][b] = 1
        arr[b][a] = 1


def bfs(cur):
    q = deque([])
    visited = [0 for _ in range(N)]
    visited[cur] = 0
    q.append(cur)
    while q:
        person = q.popleft()
        for friend in range(N):
            if friend != cur and arr[person][friend] == 1 and visited[friend] == 0:
                q.append(friend)
                visited[friend] = visited[person] + 1
    return sum(visited)

cntlst = deque([])
for i in range(N):
    cntlst.append(bfs(i))
num = min(cntlst)
for i, v in enumerate(cntlst):
    if v == num:
        print(i + 1)
        break