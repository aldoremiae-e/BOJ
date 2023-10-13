N, M = map(int, input().split())
ci, cj, cd = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
visit = [[0] * M for _ in range(N)]
while True:
    # 청소
    if board[ci][cj] == 0 and visit[ci][cj] == 0:
        visit[ci][cj] = 1
        cnt += 1
    # 4방향 빈칸 탐색
    flag = True #4칸 모두 청소되어있을 때
    ni, nj, nd = ci, cj, cd
    for _ in range(4): # 반시계로 돌아서, 찾으면 그곳으로 이동
        nd = (nd - 1) % 4
        ni, nj = ci + dirs[nd][0], cj + dirs[nd][1]
        # 범위, 벽일 때 넘어가기
        if not (0 <= ni < N and 0 <= nj < M):
            continue
        if board[ni][nj] == 1 or visit[ni][nj] == 1:
            continue
        if board[ni][nj] == 0 and visit[ni][nj] == 0:
            flag = False
            break
    if flag:
        # 후진
        nd = (cd + 2) % 4
        ni, nj = dirs[nd][0] + ci, dirs[nd][1] + cj
        if board[ni][nj] == 1:
            break
        else:
            ci, cj = ni, nj
    else:
        ci, cj, cd = ni, nj, nd
print(cnt)