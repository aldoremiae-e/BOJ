'''
5:38
'''
N, M = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(ci, cj, si, sj, k):
    for di, dj in dirs:
        ni, nj = ci + di, cj + dj
        if not (0 <= ni < N and 0 <= nj < M):
            continue
        if board[ni][nj] != board[si][sj]:
            continue
        # 사이클을 찾았을 때
        if ni == si and nj == sj and k >= 4:
            return True
        if visit[ni][nj] == 1:
            continue
        visit[ni][nj] = 1
        if dfs(ni, nj, si, sj, k+1):
            return True
        visit[ni][nj] = 0
    return False
flag = False
for si in range(N):
    for sj in range(M):
        visit[si][sj] = 1
        if dfs(si, sj, si, sj, 1):
            print('Yes')
            exit()
print('No')