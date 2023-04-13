from collections import deque

def bfs(si, sj, num):
    q = deque()
    visit = [[0] * M for _ in range(N)]
    q.append((si, sj))
    visit[si][sj] = 1
    cnt = 1
    while q:
        ni, nj = q.popleft()
        for di, dj in dir:
            ci, cj = ni + di, nj + dj
            if 0 <= ci < N and 0 <= cj < M and maps[ci][cj] == num and visit[ci][cj] == 0:
                cnt += 1
                visit[ci][cj] = 1
                q.append((ci, cj))
    return cnt*num
def move(didx):
    #dice = [1, 3, 5, 6]  # 위0 오1 앞2 아래3
    ndice = [0, 0, 0, 0, 0, 0]
    if didx == 0: # ㅏ
        ndice[1] = dice[0] # 위 -> 오
        ndice[3] = dice[1] # 오 -> 아래
        ndice[2] = dice[2] # 앞 = 앞
        ndice[0] = 7 - ndice[3]
        ndice[4] = 7 - ndice[1]
        ndice[5] = 7 - ndice[2]
    elif didx == 1: # ㅜ
        ndice[2] = dice[0]
        ndice[1] = dice[1]
        ndice[3] = dice[2]
        ndice[0] = 7 - ndice[3]
        ndice[4] = 7 - ndice[1]
        ndice[5] = 7 - ndice[2]
    elif didx == 2:
        ndice[4] = dice[0]
        ndice[0] = dice[1]
        ndice[2] = dice[2]
        ndice[1] = 7 - ndice[4]
        ndice[3] = 7 - ndice[0]
        ndice[5] = 7 - ndice[2]
    elif didx == 3:
        ndice[5] = dice[0]
        ndice[1] = dice[1]
        ndice[0] = dice[2]
        ndice[2] = 7 - ndice[5]
        ndice[3] = 7 - ndice[0]
        ndice[4] = 7 - ndice[1]
    return ndice

N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dice = [1, 3, 5, 6, 4, 2] #위0 오1 앞2 아래3
# i 아랫면 ㅏ ㅜ ㅓ ㅗ 로갈때 [아래 오른 앞 / 왼(7-오른) 뒤(7-앞) 위(7-아래)]

ans = 0
ci, cj = 0, 0
didx = 0 # 0, 1, 2, 3 ( ㅏ ㅜ ㅓ ㅗ)
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
under = 6 # 첫 아랫면 인덱스
for i in range(K):
    # 1. 현재위치 이동
    if 0 <= ci + dir[didx][0] < N and 0 <= cj + dir[didx][1] < M:
        ci, cj = ci + dir[didx][0], cj + dir[didx][1]
    else:
        # 반대방향
        didx = (didx+2) % 4
        ci, cj = ci + dir[didx][0], cj + dir[didx][1]

    # 3. 현재위치 칸에서의 bfs
    ans += bfs(ci, cj, maps[ci][cj])

    # 2. 주사위 굴리기
    dice = move(didx)
    under = dice[3]  # A
    # 4. 주사위 방향 결정
    if under > maps[ci][cj]:
        # 시계방향
        didx = (didx + 1) % 4
    elif under < maps[ci][cj]:
        # 반시계방향
        didx = (didx - 1) % 4
print(ans)