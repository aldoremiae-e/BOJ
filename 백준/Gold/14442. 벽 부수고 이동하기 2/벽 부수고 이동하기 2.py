from collections import deque

N, M, K = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(N)]

def bfs():
    # K개 뚫었는 때의 visit[i][j][k] 에서의 경로
    if N == 1 and M == 1:
        return 1
    visit = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0, 0))
    visit[0][0][0] = 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        ci, cj, cw = q.popleft()
        if ci == N-1 and cj == M-1:
            return visit[ci][cj][cw]
        for di, dj in dirs:
            ni, nj = di + ci, dj + cj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            # 생각해줘야할 것
            # 방문했는지 안했는지
                # 벽일 때, 부술 수 있는 벽인지, 방문처리가 되지않은 벽인지
                # 부술수 없으면 못지나감
                # 방문처리가 되어있다면 보지않음 - 큐에 들어가 있을거임
            if maps[ni][nj] == 1 and cw < K and visit[ni][nj][cw+1] == 0:
                visit[ni][nj][cw+1] = visit[ci][cj][cw] + 1
                q.append((ni, nj, cw+1))
            elif maps[ni][nj] == 0 and visit[ni][nj][cw] == 0:
                visit[ni][nj][cw] = visit[ci][cj][cw] + 1
                q.append((ni, nj, cw))
    return -1

ans = bfs()
print(ans)