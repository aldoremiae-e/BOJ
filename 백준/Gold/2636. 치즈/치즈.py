from collections import deque

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

# 공기
def airs(i, j):
    global maps
    q = deque()
    q.append((i, j))
    v = [[0] * M for _ in range(N)]
    v[i][j] = 1
    maps[i][j] = 2
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < M):
                continue
            if v[ni][nj] == 1 or maps[ni][nj] == 1:
                continue
            if maps[ni][nj] == 0: # 외부공기로
                flag = True
                maps[ni][nj] = 2
                v[ni][nj] = 1
                q.append((ni, nj))
            if maps[ni][nj] == 2: # 이미 외부공기임
                v[ni][nj] = 1
                q.append((ni, nj))

def cheese(i, j):
    global melt, visit
    q = deque()
    q.append((i, j))

    visit[i][j] = 1

    while q:
        ci, cj = q.popleft()
        flag = False
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if visit[ni][nj] == 1:
                continue
            if maps[ni][nj] == 2:
                # 공기와 만남
                flag = True
            elif maps[ni][nj] == 1:
                # 치즈
                visit[ni][nj] = 1
                q.append((ni, nj))
        if flag:
            melt.append((ci, cj))


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ans = 0
time = 0
while True:
    airs(0, 0)

    visit = [[0] * M for _ in range(N)]
    melt = deque()
    for i in range(1, N-1):
        for j in range(1, M-1):
            if maps[i][j] == 1 and visit[i][j] == 0:
                cheese(i, j)
    cnt = len(melt)
    if cnt > 0:
        ans = cnt
    else:
        break

    while melt:
        mi, mj = melt.popleft()
        maps[mi][mj] = 2
    time += 1

print(time)
print(ans)