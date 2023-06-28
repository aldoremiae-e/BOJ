from collections import deque

def bfs(N, K):
    global ans, visit
    q = deque()
    q.append(N)
    visit[N] = 0
    while q:
        cur = q.popleft()
        # K라면
        if cur == K:
            ans += 1
            continue
        graph = [cur-1, cur+1, cur*2]
        for n in graph:
            # 범위에 넘어간다면 예외처리
            if n < 0 or n >= 200001:
                continue
            # 방문하지 않았거나, 최소시간(현재시간+1)이 있을때
            if visit[n] == -1 or visit[n] == visit[cur] + 1:
                visit[n] = visit[cur] + 1
                q.append(n)
N, K = map(int, input().split())
time, ans = 0, 0
visit = [-1] * 200001

bfs(N, K)
time = visit[K]
print(time)
print(ans)