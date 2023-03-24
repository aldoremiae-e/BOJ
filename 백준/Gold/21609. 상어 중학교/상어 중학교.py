# 검-1 무0 일(M)
# 그룹 (2개이상): 0, M 으로 이루어진 블록 - 인접한
# 기준블록 : i , j 가 가장작은 블록
from collections import deque
# 크기가 가장 큰 블록
def bfs(si, sj, m):
    global visit
    size = 1000 # 100의자리: 개수, 10의자리 무지개블록
    q = deque()
    q.append((si, sj))
    visit[si][sj] = 1
    while q:
        i, j = q.popleft()
        for di, dj in dir:
            ci, cj = i + di, j + dj
            if 0 <= ci < N and 0 <= cj < N and visit[ci][cj] == 0:
                if maps[ci][cj] == 0:
                    visit[ci][cj] = 1
                    size += 1001
                    q.append((ci, cj))
                elif maps[ci][cj] == m:
                    visit[ci][cj] = 1
                    size += 1000
                    q.append((ci, cj))
                else:
                    continue
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 0 and visit[i][j] == 1:
                visit[i][j] = 0
    return size
# 블록제거
def delb(si, sj, m):
    dq = deque()
    dq.append((si, sj))
    dvisit = [[0] * N for _ in range(N)]
    dvisit[si][sj] = 1
    maps[si][sj] = -2
    while dq:
        i, j = dq.popleft()
        for di, dj in dir:
            ci, cj = i + di, j + dj
            if 0 <= ci < N and 0 <= cj < N and (maps[ci][cj] == m or maps[ci][cj] == 0):
                visit[ci][cj] = 1
                maps[ci][cj] = -2
                dq.append((ci, cj))

def gravity():
    for i in range(N-2, -1, -1):
        for j in range(N):
            if maps[i][j] >= 0:
                ci = i+1
                if maps[ci][j] > -2:
                    continue
                while 1:
                    if ci == N:
                        ci -= 1
                        maps[ci][j] = maps[i][j]
                        maps[i][j] = -2
                        break
                    else:
                        if maps[ci][j] == -2:
                            ci += 1
                        elif maps[ci][j] != -2:
                            ci -= 1
                            maps[ci][j] = maps[i][j]
                            maps[i][j] = -2
                            break
def rot():
    rot_arr = [[0] * N for _ in range(N)]
    ci, cj = 0, 0
    for j in range(N-1, -1, -1):
        for i in range(N):
            rot_arr[ci][cj] = maps[i][j]
            cj = (cj + 1) % N
        ci += 1
    return rot_arr
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
ans = 0 # 답
if N == 1:
    print(ans)
else:
    while 1:
        visit = [[0] * N for _ in range(N)]
        big_size = 1000
        bi, bj = N-1, N-1
        for i in range(N):
            for j in range(N):
                if maps[i][j] > 0 and visit[i][j] == 0:
                    ret = bfs(i, j, maps[i][j])
                    if big_size <= ret:
                        bi, bj = i, j
                        big_size = ret
        # 블록 그룹이 존재하지 않을 때
        if big_size == 1000:
            break
        # 블록제거
        delb(bi, bj, maps[bi][bj])
        # 점수 획득
        ans += (big_size // 1000) ** 2
        # 중력 발생
        gravity()
        # 90도 회전
        maps = rot()
        gravity()
    print(ans)