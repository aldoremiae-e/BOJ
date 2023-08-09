def f(i, j, visited):
    q = [0] * (N*M)
    front = -1
    rear = -1
    rear += 1
    q[rear] = (i, j)
    visited[i][j] = 1
    while front != rear:
        front += 1
        i, j = q[front]
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0  <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                rear += 1
                q[rear] = (ni, nj)
                visited[ni][nj] = visited[i][j] + 1
# 0 이동가능
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

v1 = [[0]*M for _ in range(N)] # 0,0 부터의 거리
v2 = [[0]*M for _ in range(N)] # n-1, m-1 부터의 거리
f(0, 0, v1)
f(N-1,M-1, v2)

minV = 0
if N == 1 and M == 1: # 크기 1칸일 경우
    minV = 1
elif v1[N-1][M-1]:
    minV = v1[N-1][M-1] # 벽을 부수지 않았을 때의 최단거리
else:
    minV = 1000000

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            v1lst = []
            v2lst = []
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni, nj = i +di, j + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if v1[ni][nj]:
                        v1lst.append(v1[ni][nj])
                    if v2[ni][nj]:
                        v2lst.append(v2[ni][nj])
            if v1lst and v2lst:
                minV1 = min(v1lst) # 출발~ 벽까지
                minV2 = min(v2lst) # 벽 ~ 도착
                if minV > minV1 + minV2 + 1: # 벽이 없을 때 ~ 도착 최단거리
                    minV = minV1 + minV2 +1
if minV == 1000000:
    minV = -1
print(minV)