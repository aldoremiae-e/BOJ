'''
4:27 ~ 4:50
'''
blocks = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],
          [(0, 1), (1, 0), (1, 1)], [(1, 0), (2, 0), (2, 1)],
          [(0, 1), (0, 2), (1, 2)], [(0, 1), (1, 0), (2, 0)],
          [(1, 0), (1, 1), (1, 2)], [(2, -1), (1, 0), (2, 0)],
          [(1, -2), (1, -1), (1, 0)], [(0, 1), (1, 1), (2, 1)],
          [(0, 1), (0, 2), (1, 0)], [(1, 0), (1, 1), (2, 1)],
          [(1, -1), (1, 0), (0, 1)], [(1, -1), (1, 0), (2, -1)],
          [(0, 1), (1, 1), (1, 2)], [(1, 0), (1, 1), (2, 0)],
          [(1, -1), (1, 0), (1, 1)], [(1, -1), (1, 0), (2, 0)], [(0, 1), (0, 2), (1, 1)]]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
def go(si, sj):
    ret = 0
    for block in blocks:
        flag = True
        num = board[si][sj]
        for k in range(3):
            ni, nj = si + block[k][0], sj + block[k][1]
            if not (0 <= ni < N and 0 <= nj < M):
                flag = False
                break
            num += board[ni][nj]
        if flag:
            ret = max(ret, num)
    return ret
ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, go(i, j))

print(ans)