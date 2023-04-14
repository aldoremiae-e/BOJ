from collections import deque, Counter
def bfs(n, adj):
    q = deque()
    visit = [0 for _ in range(n+1)]
    q.append(1)
    visit[1] = 1
    while q:
        cur = q.popleft()
        for k in adj[cur]:
            if visit[k] == 0:
                visit[k] = visit[cur] + 1
                q.append(k)
    return visit
def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n+1)]
    for i, j in edge:
        adj[i].append(j)
        adj[j].append(i)
    v = bfs(n, adj)
    maxnum = max(v)
    for i in v:
        if i == maxnum:
            answer += 1
    return answer