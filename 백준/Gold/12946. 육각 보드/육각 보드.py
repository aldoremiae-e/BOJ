import sys
sys.setrecursionlimit(int(1e7))
N = int(input())
A = [list(map(str, input().strip())) for _ in range(N)]
cnt = 0
dirs = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
visit = [[-1 for _ in range(N)] for _ in range(N)]
def dfs(i, j, c): # c는 컬러 0, 1 두개로 이분그래프 나타낼 것
    global cnt
    visit[i][j] = c # 0 색으로 칠함
    cnt = max(cnt, 1) # X가 하나라도 존재함
    for di, dj in dirs:
        ni, nj = di + i, dj + j
        if not (0 <= ni < N and 0 <= nj< N):
            continue
        # 인접한 칸이 X인경우
        if A[ni][nj] == 'X':
            # 인접해있는데 아직 색칠 안한 칸이라면
            if visit[ni][nj] == -1:
                dfs(ni, nj, 1-c)
            cnt = max(cnt, 2)    # 색을 2개 쓴 경우
            # 인접해있는데 이미 같은 색으로 색칠되어 있는 경우라면
            if visit[ni][nj] == c:
                cnt = max(cnt, 3)
'''
색은 최소 0개 최대 3개 칠할 수 있다.
'''
for i in range(N):
    for j in range(N):
        if A[i][j] == 'X' and visit[i][j] == -1:
            dfs(i, j, 0)

print(cnt)