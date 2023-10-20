from collections import deque
N, M = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(N)]
ai, aj, bi, bj = -1, -1, -1, -1
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            if ai == -1:
                ai, aj = i, j
            else:
                bi, bj = i, j
def go(ax, ay, bx, by, cnt):
    ans = -1
    if cnt > 10:
        return -1
    dead = 0
    if not (0 <= ax < N and 0 <= ay < M):
        dead += 1
    if not (0 <= bx < N and 0 <= by < M):
        dead += 1
    # 정답을 찾은 경우
    if dead == 1:
        return cnt
    # 불가능한 경우    # 둘다 떨어지거나, step이 10 초과면
    elif dead == 2:
        return -1
    # 갈경우 => 범위안에 들어오는 경우
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nx, ny, mx, my = ax+di, ay+dj, bx+di, by+dj
        if (0 <= nx < N and 0 <= ny < M and board[nx][ny] == '#'):
            nx, ny = ax, ay
        if (0 <= mx < N and 0 <= my < M and board[mx][my] == '#'):
            mx, my = bx, by
        temp = go(nx, ny, mx, my, cnt+1)
        if temp == -1:
            continue
        if ans == -1 or ans > temp:
            ans = temp
    return ans

print(go(ai, aj, bi, bj, 0))