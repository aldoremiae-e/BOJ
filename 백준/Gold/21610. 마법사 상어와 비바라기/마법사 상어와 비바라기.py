from collections import deque
# ci, cj = (si + di) % N, (si + dj) % N

# 구름 이동
def move(d, s):
    global cloud_q, cloud
    di, dj = dir[d][0], dir[d][1]
    ret_q = deque()
    while cloud_q:
        si, sj = cloud_q.popleft()
        ci, cj = (si + (di * s)) % N, (sj + (dj * s)) % N
        if 0 <= ci < N and 0 <= cj < N and cloud[ci][cj] == 0:
            cloud[ci][cj] = 1
            ret_q.append((ci, cj))
    return ret_q
def rain():
    global cloud_q, cloud
    for i in range(N):
        for j in range(N):
            # 칸의 바구니 물의 양 + 1
            if cloud[i][j] == 1:
                maps[i][j] += 1
    while cloud_q:
        si, sj = cloud_q.popleft()
        cnt = 0
        # 물복사 버그
        for i in range(1, 8, 2):
            di, dj = dir[i][0], dir[i][1]
            ci, cj = si + di, sj + dj
            if 0 <= ci < N and 0 <= cj < N and maps[ci][cj] != 0:
                cnt += 1
        maps[si][sj] += cnt

# 구름 x
def make_cloud():
    global cloud_q, cloud
    for i in range(N):
        for j in range(N):
            if maps[i][j] >= 2 and cloud[i][j] != 1:
                maps[i][j] -= 2
                cloud_q.append((i, j))
# 물복사버그
# 구름 생성 (구름이 사라진 칸 아니어야함)

dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

cloud_q = deque()
cloud_q.append((N-1, 0))
cloud_q.append((N-1, 1))
cloud_q.append((N-2, 0))
cloud_q.append((N-2, 1))
for _ in range(M):
    cloud = [[0] * N for _ in range(N)]
    od, os = map(int, input().split())
    od -= 1
    cloud_q = move(od, os)
    rain()
    make_cloud()
ans = 0
for i in range(N):
    for j in range(N):
       ans += maps[i][j]
print(ans)