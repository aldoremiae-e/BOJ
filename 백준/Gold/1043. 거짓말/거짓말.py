from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
# true[0] 진실을 아는 사람수 [1:] 사람 번호
true = list(map(int, stdin.readline().split()))
true = true[1:]
visited = [0] * (N+1)
mymap = list([0 for _ in range(N+1)] for _ in range(N+1))
arr = deque()
for _ in range(M):
    party = list(map(int, stdin.readline().split()))
    P = party[0]
    party = party[1:]
    arr.append(party)
    if P > 1:
        for i in range(P):
            mymap[party[i-1]][party[i]] = 1
            mymap[party[i]][party[i-1]] = 1
q = deque()

def bfs(start):
    global mymap
    q.append(start)
    visited[start] = 1
    while q:
        cur = q.popleft()
        for i in range(N+1):
            if visited[i] == 0 and mymap[cur][i] == 1:
                q.append(i)
                visited[i] = 1
for i in true:
    bfs(i)
cnt = 0
for i in arr:
    flag = 0
    for j in i:
        if visited[j] == 1:
            flag = 1
    if flag == 0:
        cnt += 1
print(cnt)