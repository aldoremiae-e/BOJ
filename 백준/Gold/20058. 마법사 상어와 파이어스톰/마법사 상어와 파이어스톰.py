from collections import deque
from pprint import pprint
N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
Llst = list(map(int, input().split()))
n = 2 ** N
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def rotate(si, sj, l):
    global new_board
    #rot[si + j][sj + L - 1 - i] = maps[si + i][sj + j]
    for i in range(l):
        for j in range(l):
            new_board[si + j][sj + l - 1 - i] = board[si + i][sj + j]
    return
def check(ci, cj):
    ice = 0
    for di, dj in dirs:
        ni, nj = ci + di, cj + dj
        if not (0 <= ni < n and 0 <= nj < n):
            continue
        if new_board[ni][nj] > 0:
            ice += 1
    if ice < 3:
        return True
    else:
        return False

for L in Llst:
    # rotate
    l = 2 ** L
    new_board = [[0] * n for _ in range(n)]
    for i in range(0, n, l):
        for j in range(0, n, l):
            rotate(i, j, l)
    # 얼음이 있는 칸 3개 이상

    for i in range(n):
        for j in range(n):
            board[i][j] = new_board[i][j]
            if board[i][j] > 0 and check(i, j):
                board[i][j] -= 1

def bfs(si, sj):
    global visit, island
    q = deque()
    q.append((si, sj))
    visit[si][sj] = 1
    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in dirs:
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < n and 0 <= nj < n):
                continue
            if visit[ni][nj] == 1 or board[ni][nj] == 0:
                continue
            visit[ni][nj] = 1
            cnt += 1
            q.append((ni, nj))
    island = max(island, cnt)
    return

visit = [[0] * n for _ in range(n)]
ans = 0
island = 0
for i in range(n):
    for j in range(n):
       if board[i][j] == 0:
           continue
       ans += board[i][j]
       bfs(i, j)

print(ans)
print(island)