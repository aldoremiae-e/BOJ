from collections import deque
i = 1
while True:
    N = int(input())
    if N == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(N)]

    def bfs():
        visit = [[-1] * N for _ in range(N)]
        visit[0][0] = maps[0][0]
        q = deque()
        q.append((0, 0))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            ci, cj = q.popleft()
            for di, dj in dirs:
                ni, nj = ci + di, cj + dj
                if not (0 <= ni < N and 0 <= nj < N):
                    continue
                num = maps[ni][nj] + visit[ci][cj]
                if visit[ni][nj] == -1:
                    # 방문하지않은 곳
                    visit[ni][nj] = num
                    q.append((ni, nj))
                else:
                    if num < visit[ni][nj]:
                        visit[ni][nj] = num
                        q.append((ni, nj))
        return visit[N-1][N-1]
    ans = bfs()
    print(f'Problem {i}: {ans}')
    i += 1